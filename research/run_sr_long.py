"""The range fade over ~10 years of Dukascopy hourly history.

The Deriv runs cover about a year, which is one market regime. These files
reach back to 2016, so a level-based edge has to survive several.
"""

import argparse
import json

import numpy as np
import pandas as pd

from instruments import INSTRUMENTS
from run_long_history import DUKASCOPY_TO_DERIV, LONG_DIR, long_frame

YEARS_DIR = LONG_DIR / "years"

import run_sr_backtest as sr


def available_markets():
    return [name for name in DUKASCOPY_TO_DERIV if (LONG_DIR / f"{name}.csv").exists()]


def frame_for(name):
    """The assembled file, or whatever whole years are on disk for a part-downloaded market."""
    if (LONG_DIR / f"{name}.csv").exists():
        return long_frame(name)
    years = sorted(YEARS_DIR.glob(f"{name}-[0-9][0-9][0-9][0-9].csv"))
    if not years:
        raise FileNotFoundError(f"{name}: no hourly history downloaded")
    raw = pd.concat([pd.read_csv(path) for path in years]).drop_duplicates("timestamp")
    traded = raw[raw["volume"] > 0].sort_values("timestamp")
    return pd.DataFrame({
        "epoch": (traded["timestamp"] // 1000).astype(int),
        "open": traded["open"], "high": traded["high"],
        "low": traded["low"], "close": traded["close"],
    }).reset_index(drop=True)


def instrument_for(name):
    symbol = DUKASCOPY_TO_DERIV[name]
    return next(item for item in INSTRUMENTS if item["symbol"] == symbol)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--triggers", default="limit,rejection")
    parser.add_argument("--markets", default=",".join(available_markets()))
    parser.add_argument("--label", default="long_1h")
    args = parser.parse_args()

    rng = np.random.default_rng(20260921)
    results = []
    for name in args.markets.split(","):
        frame = frame_for(name)
        instrument = instrument_for(name)
        for trigger in args.triggers.split(","):
            result = sr.test_frame(frame, instrument, "1h", trigger, rng)
            result["verdict"] = sr.verdict(result)
            results.append(result)
            walk, lock = result["walk_forward"], result["lockbox"]
            print(
                f"{result['verdict']:4}  {instrument['symbol']:10} {trigger:9} "
                f"{len(frame):6} bars  wf: {walk['trades']:4} trades  win {walk['win_rate']:.3f}  "
                f"exp {walk['expectancy_r']:+.3f}R  PF {walk['profit_factor']:.2f}  "
                f"| lock exp {lock['expectancy_r']:+.3f}R  | p={result['beat_random_p']}",
                flush=True,
            )

    sr.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report = sr.OUTPUT_DIR / f"results_{args.label}.json"
    report.write_text(json.dumps(results, indent=2))
    print(f"\nwrote {report}")


if __name__ == "__main__":
    main()
