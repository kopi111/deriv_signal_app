"""Luck check: the full test on computer-generated random-walk prices.
A random walk has no edge by construction, so every strategy that passes
here is a false pass. The pass rate is the test's false-positive rate.
Market sizes match Deriv's: 1h = 1 year, 15m = about 7 months."""

import functools
import json
from pathlib import Path

import numpy as np
import pandas as pd

from sweep import passes, run_sweep, test_count

OUTPUT = Path(__file__).parent / "output"
MARKETS_PER_TIMEFRAME = 40
BARS = {"1h": 8760, "15m": 20000}
SECONDS = {"1h": 3600, "15m": 900}
TICKS_PER_BAR = 60
VOLATILITY_PER_TICK = 0.0006


def random_walk_frame(seed, timeframe):
    rng = np.random.default_rng(seed)
    bars = BARS[timeframe]
    steps = rng.normal(0, VOLATILITY_PER_TICK, size=(bars, TICKS_PER_BAR))
    path = 1000 * np.exp(np.cumsum(steps.ravel())).reshape(bars, TICKS_PER_BAR)
    opens = np.concatenate([[1000.0], path[:-1, -1]])
    return pd.DataFrame({
        "epoch": np.arange(bars) * SECONDS[timeframe],
        "open": opens,
        "high": np.maximum(path.max(axis=1), opens),
        "low": np.minimum(path.min(axis=1), opens),
        "close": path[:, -1],
    })


def jobs():
    runs = OUTPUT / "luck_runs"
    for timeframe in BARS:
        for index in range(MARKETS_PER_TIMEFRAME):
            seed = index + (0 if timeframe == "1h" else 10_000)
            instrument = {"symbol": f"RANDOM_{seed}", "name": f"Random walk {seed}",
                          "group": "Synthetic", "synthetic": True}
            yield (instrument, timeframe, functools.partial(random_walk_frame, seed, timeframe),
                   runs / f"random_{seed}_{timeframe}.json")


def main():
    results = run_sweep(list(jobs()), OUTPUT / "luck_runs")
    false_passes, tested = passes(results), test_count(results)
    summary = {"tests": tested, "false_passes": len(false_passes),
               "false_pass_rate": round(len(false_passes) / tested, 4), "passes": false_passes}
    (OUTPUT / "luck_check.json").write_text(json.dumps(summary, indent=1))
    print(json.dumps({k: v for k, v in summary.items() if k != "passes"}))


if __name__ == "__main__":
    main()
