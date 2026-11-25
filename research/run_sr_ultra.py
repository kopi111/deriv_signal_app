"""Backtest of the AlgoAlpha S&R Ultra signals, with a random-walk luck control.

The indicator only draws zones and flags events; it names no trade. So each flag is turned
into the most literal trade it implies and asked the one question that matters: does acting on
it beat chance, after costs?

  * rejection : price was turned away at a zone -> trade back into the range (fade).
  * sweep     : a wick pierced the zone then closed back inside -> fade, same direction.
  * breakout  : a close went through the zone -> trade with the break (continuation).

Every trade enters at the next open, pays the instrument's spread, risks a fixed share of ATR
to a fixed reward:risk, and holds one position at a time. Results are in R-multiples, so they
add across instruments. The same signals are then run on martingale random walks, which have no
real support or resistance: any profit there is the test's own false-positive rate, the lesson
the earlier S/R range-fade study turned on.
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

import data
import indicators as ind
import instruments as inst
import sr_range_fade as fade
import sr_ultra
from run_sr_luck_check import random_frame, TICKS_PER_BAR

OUTPUT_DIR = Path(__file__).parent / "output" / "sr_ultra"
WARMUP_BARS = 250
STOP_ATR_SHARE = 0.5
REWARD_RISK = 2.0
MAX_HOLD_BARS = 96
SIGNALS = ("rejection", "sweep", "breakout")

REAL_SYMBOLS = [
    "frxEURUSD", "frxGBPUSD", "frxAUDUSD", "frxNZDUSD", "frxUSDCAD", "frxUSDCHF", "frxUSDJPY",
    "frxEURJPY", "frxGBPJPY", "frxAUDJPY", "frxEURGBP", "frxEURAUD", "frxGBPAUD", "frxAUDNZD",
    "frxUSDMXN", "frxXAUUSD", "frxXAGUSD", "frxXPTUSD",
]


def load_cached(symbol, timeframe):
    """Read a symbol's cached candles straight from disk, so the run stays offline."""
    path = data.CACHE_DIR / f"{symbol}_{timeframe}.csv"
    if not path.exists():
        raise FileNotFoundError(f"no cache for {symbol} {timeframe}")
    return pd.read_csv(path)


def prepare_bars(frame):
    bars = {col: frame[col].to_numpy() for col in ("open", "high", "low", "close")}
    bars["atr"] = ind.atr(frame, 14).to_numpy()
    return bars


def _direction_for(signal, events, bar):
    """The trade direction a signal implies at a bar, or 0 when it did not fire."""
    if signal == "rejection":
        return 1 if events.bull_reject[bar] else -1 if events.bear_reject[bar] else 0
    if signal == "sweep":
        return 1 if events.bull_sweep[bar] else -1 if events.bear_sweep[bar] else 0
    return 1 if events.bull_break[bar] else -1 if events.bear_break[bar] else 0


def run_signal(bars, events, signal, spread):
    """Every trade the signal produces, one position at a time, as R-multiples."""
    close = bars["close"]
    atr = bars["atr"]
    n = len(close)
    results = []
    free_from = WARMUP_BARS
    for bar in range(WARMUP_BARS, n - 2):
        if bar < free_from:
            continue
        direction = _direction_for(signal, events, bar)
        if direction == 0:
            continue
        entry_bar = bar + 1
        risk = STOP_ATR_SHARE * atr[bar]
        if not np.isfinite(risk) or risk <= 0:
            continue
        entry = close[entry_bar] if entry_bar < n else close[bar]
        entry = bars["open"][entry_bar] + direction * spread
        stop = entry - direction * risk
        target = entry + direction * REWARD_RISK * risk
        last_bar = min(entry_bar + MAX_HOLD_BARS, n)
        if entry_bar >= last_bar:
            continue
        result_r, exit_bar = fade.exit_result(
            bars, direction, entry, stop, target, entry_bar, last_bar, REWARD_RISK)
        results.append(result_r)
        free_from = exit_bar + 1
    return np.array(results)


def summarize(results):
    if len(results) == 0:
        return {"trades": 0, "win_rate": None, "mean_r": None, "net_r": 0.0, "t_stat": None}
    wins = float((results > 0).mean())
    mean = float(results.mean())
    net = float(results.sum())
    t = float(mean / (results.std(ddof=1) / np.sqrt(len(results)))) if len(results) > 1 and results.std() > 0 else None
    return {"trades": len(results), "win_rate": round(wins, 3), "mean_r": round(mean, 4),
            "net_r": round(net, 1), "t_stat": None if t is None else round(t, 2)}


def test_frame(frame, spread, rules):
    events = sr_ultra.zone_events(frame, rules)
    bars = prepare_bars(frame)
    return {signal: summarize(run_signal(bars, events, signal, spread)) for signal in SIGNALS}


def real_run(timeframe, rules):
    rows = {}
    totals = {signal: [] for signal in SIGNALS}
    for symbol in REAL_SYMBOLS:
        try:
            frame = load_cached(symbol, timeframe)
        except Exception as error:
            print(f"  {symbol}: skipped ({error})", flush=True)
            continue
        bars = prepare_bars(frame)
        instrument = next(item for item in inst.INSTRUMENTS if item["symbol"] == symbol)
        spread = inst.spread_for(instrument, bars)
        per_signal = {}
        events = sr_ultra.zone_events(frame, rules)
        for signal in SIGNALS:
            results = run_signal(bars, events, signal, spread)
            per_signal[signal] = summarize(results)
            totals[signal].append(results)
        rows[symbol] = {"bars": len(frame), "spread": round(float(spread), 6), **per_signal}
        print(f"  {symbol} ({len(frame)}b): " + " | ".join(
            f"{s} {per_signal[s]['net_r']:+.0f}R/{per_signal[s]['trades']}" for s in SIGNALS), flush=True)
    pooled = {signal: summarize(np.concatenate(totals[signal]) if totals[signal] else np.array([]))
              for signal in SIGNALS}
    return {"rows": rows, "pooled": pooled}


def luck_run(timeframe, rules, markets, bars_each):
    """The same signals on martingale random walks; every net R here is false-positive."""
    totals = {signal: [] for signal in SIGNALS}
    # Match a real market's cost and volatility, from the cache, so the control is comparable.
    reference = load_cached("frxEURUSD", timeframe)
    bar_vol = float(np.std(np.diff(np.log(reference["close"].to_numpy()))))
    per_tick_vol = bar_vol / np.sqrt(TICKS_PER_BAR)
    spread_share = next(i for i in inst.INSTRUMENTS if i["symbol"] == "frxEURUSD")["spread"] \
        / float(np.nanmedian(reference["close"]))
    for seed in range(markets):
        frame = random_frame(70_000 + seed, "15m", bars_each, drifting=False, volatility=per_tick_vol)
        bars = prepare_bars(frame)
        spread = spread_share * float(np.nanmedian(frame["close"]))
        events = sr_ultra.zone_events(frame, rules)
        for signal in SIGNALS:
            totals[signal].append(run_signal(bars, events, signal, spread))
    return {signal: summarize(np.concatenate(totals[signal])) for signal in SIGNALS}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeframe", default="15m", choices=["15m", "1h"])
    parser.add_argument("--luck-markets", type=int, default=12)
    parser.add_argument("--luck-bars", type=int, default=20000)
    args = parser.parse_args()

    rules = sr_ultra.UltraRules()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Real markets ({args.timeframe}):", flush=True)
    real = real_run(args.timeframe, rules)
    print(f"Luck check ({args.luck_markets} random walks):", flush=True)
    luck = luck_run(args.timeframe, rules, args.luck_markets, args.luck_bars)

    report = {"timeframe": args.timeframe, "rules": vars(rules), "real": real, "luck": luck}
    out = OUTPUT_DIR / f"results_{args.timeframe}.json"
    out.write_text(json.dumps(report, indent=2))
    print(f"\nPooled real vs luck ({args.timeframe}):", flush=True)
    for signal in SIGNALS:
        r, l = real["pooled"][signal], luck[signal]
        print(f"  {signal:9s} real {r['net_r']:+8.1f}R  mean {r['mean_r']}  t {r['t_stat']}  "
              f"({r['trades']} tr)   |   luck {l['net_r']:+8.1f}R  mean {l['mean_r']}", flush=True)
    print(f"\nSaved {out}", flush=True)


if __name__ == "__main__":
    main()
