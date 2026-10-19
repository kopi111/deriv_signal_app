"""Walk-forward test of the support/resistance range fade.

Parameters are re-chosen on everything before each test fold, so every counted
trade is out-of-sample. The final slice of history is a lockbox that selection
never sees. A random-entry baseline keeps the same range geometry and payoff
and randomises only where the trade is placed, which isolates whether touching
the level is doing any work.
"""

import argparse
import json
from pathlib import Path

import numpy as np

import data
import indicators as ind
import instruments as inst
import sr_range_fade as fade

PHOTO_SYMBOLS = ["1HZ10V", "1HZ15V", "1HZ25V", "1HZ30V", "1HZ75V", "1HZ90V", "JD10"]
BARS_PER_DAY = {"5m": 288, "15m": 96, "1h": 24}
WARMUP_BARS = 250
LOCKBOX_SHARE = 0.15
FOLD_COUNT = 10
FIRST_TEST_FOLD = 4
MIN_TRAIN_TRADES = 15
RANDOM_TRIALS = 300
OUTPUT_DIR = Path(__file__).parent / "output" / "sr_range_fade"

PIVOT_REACH_CHOICES = (5, 8, 12)
STOP_SHARE_CHOICES = (0.10, 0.20, 0.30)
LEVEL_MEMORY_CHOICES = (300, 800)
MIN_REWARD_RISK = 2.0


def rule_sets(trigger, max_hold_bars):
    return [
        fade.FadeRules(reach, stop_share, MIN_REWARD_RISK, memory, max_hold_bars, trigger)
        for reach in PIVOT_REACH_CHOICES
        for stop_share in STOP_SHARE_CHOICES
        for memory in LEVEL_MEMORY_CHOICES
    ]


def prepare_bars(frame):
    bars = {column: frame[column].to_numpy() for column in ["open", "high", "low", "close"]}
    bars["atr"] = ind.atr(frame, 14).to_numpy()
    return bars


def _selection_score(trades):
    if len(trades) < MIN_TRAIN_TRADES:
        return -np.inf
    results = np.array([trade.result_r for trade in trades])
    return results.mean() * np.sqrt(len(results))


def _within(trades, start, end):
    return [trade for trade in trades if start <= trade.entry_bar < end]


class FadeTrial:
    """Every rule set simulated once over the full history."""

    def __init__(self, frame, bars, spread, trigger, max_hold_bars):
        self.runs = []
        bounds_cache = {}
        for rules in rule_sets(trigger, max_hold_bars):
            key = (rules.pivot_reach, rules.level_memory)
            if key not in bounds_cache:
                bounds_cache[key] = fade.range_bounds(frame, *key)
            resistance, support = bounds_cache[key]
            trades = fade.run(bars, resistance, support, rules, spread, WARMUP_BARS)
            self.runs.append((rules, trades))

    def best_rules(self, start, end):
        scored = [(_selection_score(_within(trades, start, end)), index)
                  for index, (_, trades) in enumerate(self.runs)]
        return self.runs[max(scored, key=lambda pair: pair[0])[1]][0]

    def trades_for(self, rules, start, end):
        trades = next(found for candidate, found in self.runs if candidate is rules)
        return _within(trades, start, end)


def fold_edges(bar_count):
    usable_end = int(bar_count * (1 - LOCKBOX_SHARE))
    edges = np.linspace(WARMUP_BARS, usable_end, FOLD_COUNT + 1).astype(int)
    return edges, usable_end


def walk_forward(trial, edges):
    folds, trades = [], []
    for fold in range(FIRST_TEST_FOLD, FOLD_COUNT):
        rules = trial.best_rules(WARMUP_BARS, edges[fold])
        fold_trades = trial.trades_for(rules, edges[fold], edges[fold + 1])
        folds.append({
            "pivot_reach": rules.pivot_reach,
            "stop_share": rules.stop_share,
            "level_memory": rules.level_memory,
            "trades": len(fold_trades),
            "total_r": round(sum(trade.result_r for trade in fold_trades), 2),
        })
        trades += fold_trades
    return folds, trades


def _random_trade(bars, resistance, support, rules, spread, bar, direction, reward_risk):
    span = abs(resistance[bar] - support[bar])
    if np.isnan(span) or span <= 0:
        return 0.0
    risk = rules.stop_share * span
    entry = bars["close"][bar] + direction * spread
    stop = entry - direction * risk
    target = entry + direction * risk * reward_risk
    last_bar = min(bar + 1 + rules.max_hold_bars, len(bars["close"]))
    if bar + 1 >= last_bar:
        return 0.0
    result_r, _ = fade.exit_result(
        bars, direction, entry, stop, target, bar + 1, last_bar, reward_risk
    )
    return result_r


def random_entry_p_value(bars, frame, trades, rules, spread, window, rng):
    """Share of random-placement runs that match or beat the real total."""
    if not trades:
        return 1.0
    actual = sum(trade.result_r for trade in trades)
    long_share = float(np.mean([trade.direction > 0 for trade in trades]))
    reward_risk = float(np.mean([trade.reward_risk for trade in trades]))
    resistance, support = fade.range_bounds(frame, rules.pivot_reach, rules.level_memory)
    beaten = 0
    for _ in range(RANDOM_TRIALS):
        bars_drawn = rng.integers(window[0], window[1] - 2, size=len(trades))
        directions = np.where(rng.random(len(trades)) < long_share, 1, -1)
        total = sum(
            _random_trade(bars, resistance, support, rules, spread, int(bar), int(direction), reward_risk)
            for bar, direction in zip(bars_drawn, directions)
        )
        beaten += total >= actual
    return round(beaten / RANDOM_TRIALS, 3)


def test_symbol(symbol, timeframe, trigger, rng):
    frame = data.load_candles(symbol, timeframe=timeframe, pages=12, minimum_bars=3000)
    instrument = next(item for item in inst.INSTRUMENTS if item["symbol"] == symbol)
    return test_frame(frame, instrument, timeframe, trigger, rng)


def test_frame(frame, instrument, timeframe, trigger, rng):
    bars = prepare_bars(frame)
    spread = inst.spread_for(instrument, bars)
    max_hold_bars = BARS_PER_DAY[timeframe]

    trial = FadeTrial(frame, bars, spread, trigger, max_hold_bars)
    edges, usable_end = fold_edges(len(frame))
    folds, wf_trades = walk_forward(trial, edges)

    final_rules = trial.best_rules(WARMUP_BARS, usable_end)
    lockbox_trades = trial.trades_for(final_rules, usable_end, len(frame))
    p_value = random_entry_p_value(
        bars, frame, wf_trades, final_rules, spread, (edges[FIRST_TEST_FOLD], usable_end), rng
    )
    return {
        "symbol": instrument["symbol"],
        "name": instrument["name"],
        "timeframe": timeframe,
        "trigger": trigger,
        "bars": int(len(frame)),
        "spread": round(float(spread), 6),
        "walk_forward": fade.summarize(wf_trades),
        "lockbox": fade.summarize(lockbox_trades),
        "beat_random_p": p_value,
        "chosen_rules": {
            "pivot_reach": final_rules.pivot_reach,
            "stop_share": final_rules.stop_share,
            "level_memory": final_rules.level_memory,
            "min_reward_risk": final_rules.min_reward_risk,
            "max_hold_bars": final_rules.max_hold_bars,
        },
        "folds": folds,
    }


def verdict(result):
    walk = result["walk_forward"]
    lock = result["lockbox"]
    passes = (
        walk["trades"] >= 30
        and walk["expectancy_r"] > 0
        and lock["expectancy_r"] > 0
        and result["beat_random_p"] <= 0.05
    )
    return "PASS" if passes else "FAIL"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeframe", default="5m")
    parser.add_argument("--triggers", default="limit,rejection")
    parser.add_argument("--symbols", default=",".join(PHOTO_SYMBOLS))
    parser.add_argument("--label", default=None,
                        help="name for the results file, when a run covers part of a set")
    args = parser.parse_args()

    rng = np.random.default_rng(20260921)
    results = []
    for trigger in args.triggers.split(","):
        for symbol in args.symbols.split(","):
            try:
                result = test_symbol(symbol, args.timeframe, trigger, rng)
            except Exception as error:
                print(f"{symbol} {trigger}: FAILED {error}", flush=True)
                continue
            result["verdict"] = verdict(result)
            results.append(result)
            walk, lock = result["walk_forward"], result["lockbox"]
            print(
                f"{result['verdict']:4}  {symbol:8} {trigger:9} "
                f"wf: {walk['trades']:4} trades  win {walk['win_rate']:.3f}  "
                f"exp {walk['expectancy_r']:+.3f}R  PF {walk['profit_factor']:.2f}  "
                f"| lock exp {lock['expectancy_r']:+.3f}R  | p={result['beat_random_p']}",
                flush=True,
            )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report = OUTPUT_DIR / f"results_{args.label or args.timeframe}.json"
    report.write_text(json.dumps(results, indent=2))
    print(f"\nwrote {report}")


if __name__ == "__main__":
    main()
