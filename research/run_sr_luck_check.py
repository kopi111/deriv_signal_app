"""Luck check for the range fade: the same test on random-walk prices.

A random walk has no support or resistance, so every PASS here is a false
pass and the pass rate is this test's false-positive rate. Bar counts match
the Deriv histories the real run uses.
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

import data
import instruments as inst
import run_sr_backtest as sr

OUTPUT_DIR = sr.OUTPUT_DIR
BARS_PER_TIMEFRAME = {"5m": 60000, "15m": 35000}
BAR_SECONDS = {"5m": 300, "15m": 900}
MARKET_COUNT = 12
SEED_BASE = {"5m": 50_000, "15m": 60_000}
START_PRICE = 1000.0
TICKS_PER_BAR = 60
VOLATILITY_PER_TICK = 0.0006


def random_instrument(seed, like=None):
    """A random market; with `like`, it carries that instrument's cost in price terms."""
    instrument = {"symbol": f"RANDOM_{seed}", "name": f"Random walk {seed}",
                  "group": "Synthetic", "synthetic": True}
    if like is None:
        return instrument
    instrument["name"] += f" like {like['symbol']}"
    instrument.pop("synthetic")
    instrument["spread_price_share"] = like["spread_price_share"]
    return instrument


def cost_and_volatility(symbol, timeframe):
    """A cached market's spread as a share of price, and its per-tick volatility."""
    instrument = next(item for item in inst.INSTRUMENTS if item["symbol"] == symbol)
    frame = data.load_candles(symbol, timeframe=timeframe, pages=12, minimum_bars=3000)
    median_price = float(np.nanmedian(frame["close"]))
    spread_share = (instrument["spread_price_share"] if "spread_price_share" in instrument
                    else instrument["spread"] / median_price)
    bar_volatility = float(np.std(np.diff(np.log(frame["close"].to_numpy()))))
    return ({"symbol": symbol, "spread_price_share": spread_share},
            bar_volatility / np.sqrt(TICKS_PER_BAR))


def random_frame(seed, timeframe, bar_count, drifting=False, volatility=None):
    """Candles from a tick-level random walk with no support or resistance.

    Exponentiating a zero-mean log path drifts price upward by half the
    variance each tick, which hands a fade at support a real edge. Unless
    `drifting` is asked for, that drift is removed so price is a martingale
    and any PASS is purely the test's own false-positive.
    """
    rng = np.random.default_rng(seed)
    tick_volatility = VOLATILITY_PER_TICK if volatility is None else volatility
    steps = rng.normal(0, tick_volatility, size=(bar_count, TICKS_PER_BAR))
    if not drifting:
        steps -= tick_volatility ** 2 / 2
    path = START_PRICE * np.exp(np.cumsum(steps.ravel())).reshape(bar_count, TICKS_PER_BAR)
    opens = np.concatenate([[START_PRICE], path[:-1, -1]])
    return pd.DataFrame({
        "epoch": np.arange(bar_count) * BAR_SECONDS[timeframe],
        "open": opens,
        "high": np.maximum(path.max(axis=1), opens),
        "low": np.minimum(path.min(axis=1), opens),
        "close": path[:, -1],
    })


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeframe", default="15m")
    parser.add_argument("--triggers", default="limit,rejection")
    parser.add_argument("--markets", type=int, default=MARKET_COUNT)
    parser.add_argument("--drifting", action="store_true",
                        help="keep the upward price drift of an exponentiated log walk")
    parser.add_argument("--bars", type=int, default=None,
                        help="bars per random market, to match the history a real run had")
    parser.add_argument("--seed-offset", type=int, default=0,
                        help="shift the market seeds, to add markets to an earlier run")
    parser.add_argument("--like", default=None,
                        help="match a cached market's volatility and spread, e.g. frxEURAUD")
    args = parser.parse_args()

    bar_count = args.bars or BARS_PER_TIMEFRAME[args.timeframe]
    like, volatility = (cost_and_volatility(args.like, args.timeframe)
                        if args.like else (None, None))
    rng = np.random.default_rng(20260921)
    results = []
    for index in range(args.markets):
        seed = SEED_BASE[args.timeframe] + args.seed_offset + index
        frame = random_frame(seed, args.timeframe, bar_count, args.drifting, volatility)
        instrument = random_instrument(seed, like)
        for trigger in args.triggers.split(","):
            result = sr.test_frame(frame, instrument, args.timeframe, trigger, rng)
            result["verdict"] = sr.verdict(result)
            results.append(result)
            walk_stats, lock = result["walk_forward"], result["lockbox"]
            print(
                f"{result['verdict']:4}  {instrument['symbol']:12} {trigger:9} "
                f"wf: {walk_stats['trades']:4} trades  win {walk_stats['win_rate']:.3f}  "
                f"exp {walk_stats['expectancy_r']:+.3f}R  | lock exp {lock['expectancy_r']:+.3f}R  "
                f"| p={result['beat_random_p']}",
                flush=True,
            )

    false_passes = [r for r in results if r["verdict"] == "PASS"]
    summary = {
        "timeframe": args.timeframe,
        "drifting": args.drifting,
        "like": args.like,
        "tests": len(results),
        "false_passes": len(false_passes),
        "false_pass_rate": round(len(false_passes) / len(results), 3),
        "results": results,
    }
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    suffix = "_drifting" if args.drifting else "_flat"
    if args.like:
        suffix += f"_like-{args.like}"
    if args.seed_offset:
        suffix += f"_seeds{args.seed_offset}"
    if args.bars:
        suffix += f"_bars{args.bars}"
    report = OUTPUT_DIR / f"luck_{args.timeframe}{suffix}_{args.triggers.replace(',', '-')}.json"
    report.write_text(json.dumps(summary, indent=2))
    print(f"\n{summary['false_passes']}/{summary['tests']} false passes "
          f"({summary['false_pass_rate']:.1%})\nwrote {report}")


if __name__ == "__main__":
    main()
