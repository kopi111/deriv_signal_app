"""The same test on ~10 years of Dukascopy hourly history for real markets.
Walk-forward folds become roughly a year each, and the untouched lockbox is
the last ~1.5 years, so a strategy has to survive several market regimes."""

import functools
import json
from pathlib import Path

import pandas as pd

from instruments import INSTRUMENTS
from sweep import passes, run_sweep, test_count

HERE = Path(__file__).parent
LONG_DIR = HERE / "cache" / "long"
OUTPUT = HERE / "output"
DUKASCOPY_TO_DERIV = {
    "xauusd": "frxXAUUSD", "xagusd": "frxXAGUSD", "eurusd": "frxEURUSD", "gbpusd": "frxGBPUSD",
    "usdjpy": "frxUSDJPY", "audusd": "frxAUDUSD", "usdcad": "frxUSDCAD", "euraud": "frxEURAUD",
    "gbpnzd": "frxGBPNZD", "btcusd": "cryBTCUSD",
}


def long_frame(name):
    raw = pd.read_csv(LONG_DIR / f"{name}.csv")
    traded = raw[raw["volume"] > 0]
    return pd.DataFrame({
        "epoch": (traded["timestamp"] // 1000).astype(int),
        "open": traded["open"], "high": traded["high"],
        "low": traded["low"], "close": traded["close"],
    }).reset_index(drop=True)


def jobs():
    by_symbol = {instrument["symbol"]: instrument for instrument in INSTRUMENTS}
    for name, symbol in DUKASCOPY_TO_DERIV.items():
        if (LONG_DIR / f"{name}.csv").exists():
            yield (by_symbol[symbol], "1h", functools.partial(long_frame, name),
                   OUTPUT / "long_runs" / f"{symbol}_1h.json")


def report_rows(results):
    rows = []
    for run in results:
        for r in run["results"]:
            oos = r["walk_forward"]
            rows.append({"market": run["name"], "from": run["from"], "to": run["to"], "strategy": r["strategy"],
                         "params": r["params"], "trades": oos["trades"], "profit_factor": oos["profit_factor"],
                         "total_r": oos["total_r"], "positive_folds": r["positive_folds"],
                         "random_p": r["random_p"], "lockbox_r": r["lockbox"]["total_r"],
                         "survives": r["survives"], "failed": r["failed_checks"]})
    return rows


def main():
    results = run_sweep(list(jobs()), OUTPUT / "long_runs")
    summary = {"tests": test_count(results), "passes": passes(results), "rows": report_rows(results)}
    (OUTPUT / "long_history.json").write_text(json.dumps(summary, indent=1))
    print(f"{len(summary['passes'])} of {summary['tests']} passed over the long history")


if __name__ == "__main__":
    main()
