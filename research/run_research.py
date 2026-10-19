"""Test every strategy on every instrument and write the verdicts.

Outputs: output/results.json (everything), output/REPORT.md (readable),
and ../assets/strategies.json (the playbook the app trades).
"""

import json
import sys
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

import backtest
import strategies
import validate
from data import ThinHistory, load_candles
from instruments import INSTRUMENTS, spread_for

OUTPUT_DIR = Path(__file__).parent / "output"
RUNS_DIR = OUTPUT_DIR / "runs"
APP_PLAYBOOK = Path(__file__).parent.parent / "assets" / "strategies.json"
TIMEFRAMES = ["1h", "15m"]

SURVIVAL_RULES = {
    "min_trades": 30,
    "min_profit_factor": 1.2,
    "min_expectancy_r": 0.08,
    "min_positive_folds": 4,
    "max_random_p": 0.05,
}


def verdict(result):
    oos = result["walk_forward"]
    checks = {
        "enough trades": oos["trades"] >= SURVIVAL_RULES["min_trades"],
        "profit factor": oos["profit_factor"] >= SURVIVAL_RULES["min_profit_factor"],
        "expectancy": oos["expectancy_r"] >= SURVIVAL_RULES["min_expectancy_r"],
        "consistent folds": result["positive_folds"] >= SURVIVAL_RULES["min_positive_folds"],
        "beats random": result["random_p"] <= SURVIVAL_RULES["max_random_p"],
        "lockbox not negative": result["lockbox"]["total_r"] >= 0,
    }
    return all(checks.values()), [name for name, passed in checks.items() if not passed]


def evaluate(strategy_name, frame, bars, spread, rng):
    trial = validate.StrategyTrial(strategy_name, frame, bars, spread)
    edges, usable_end = validate.fold_edges(len(frame))
    folds, oos_trades = validate.walk_forward(trial, edges)
    final_params = trial.best_params(backtest.WARMUP_BARS, usable_end)
    lockbox = trial.trades_for(final_params, usable_end, len(frame))
    summary = backtest.summarize(oos_trades)
    random_p = 1.0
    if summary["profit_factor"] > 1:
        window = (edges[validate.FIRST_TEST_FOLD], usable_end)
        random_p = validate.random_entry_p_value(bars, oos_trades, final_params["exit"], spread, window, rng)
    result = {
        "strategy": strategy_name,
        "params": final_params,
        "walk_forward": summary,
        "folds": folds,
        "positive_folds": sum(fold["total_r"] > 0 for fold in folds),
        "random_p": random_p,
        "lockbox": backtest.summarize(lockbox),
        "in_sample": backtest.summarize(trial.trades_for(final_params, backtest.WARMUP_BARS, usable_end)),
    }
    result["survives"], result["failed_checks"] = verdict(result)
    return result


def research_instrument(instrument, timeframe, rng):
    return evaluate_market(instrument, load_candles(instrument["symbol"], timeframe), timeframe, rng)


def evaluate_market(instrument, frame, timeframe, rng):
    bars = validate.prepare_bars(frame)
    spread = spread_for(instrument, bars)
    results = [evaluate(name, frame, bars, spread, rng) for name in strategies.STRATEGIES]
    first = datetime.fromtimestamp(frame["epoch"].iloc[0], timezone.utc).date().isoformat()
    last = datetime.fromtimestamp(frame["epoch"].iloc[-1], timezone.utc).date().isoformat()
    return {**instrument, "timeframe": timeframe, "spread_used": spread, "bars": len(frame), "from": first, "to": last,
            "results": sorted(results, key=lambda r: r["walk_forward"]["total_r"], reverse=True)}


def to_json_value(value):
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    if isinstance(value, np.bool_):
        return bool(value)
    raise TypeError(f"cannot serialise {type(value).__name__}")


def research_job(job):
    instrument, timeframe = job
    saved = RUNS_DIR / f"{instrument['symbol']}_{timeframe}.json"
    if saved.exists():
        return json.loads(saved.read_text())
    try:
        run = research_instrument(instrument, timeframe, np.random.default_rng(7))
    except ThinHistory as error:
        print(f"FAILED {instrument['symbol']} {timeframe}: {error}", file=sys.stderr, flush=True)
        return {"failure": {"symbol": instrument["symbol"], "timeframe": timeframe, "error": str(error)}}
    saved.write_text(json.dumps(run, default=to_json_value))
    print(f"done {instrument['symbol']} {timeframe}", flush=True)
    return json.loads(saved.read_text())


def main():
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    jobs = [(instrument, timeframe) for timeframe in TIMEFRAMES for instrument in INSTRUMENTS]
    with ProcessPoolExecutor() as pool:
        outcomes = list(pool.map(research_job, jobs))
    report = [outcome for outcome in outcomes if "failure" not in outcome]
    failures = [outcome["failure"] for outcome in outcomes if "failure" in outcome]
    payload = {"generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
               "timeframes": TIMEFRAMES, "rules": SURVIVAL_RULES,
               "failures": failures, "instruments": report}
    (OUTPUT_DIR / "results.json").write_text(json.dumps(payload, indent=1, default=to_json_value))


if __name__ == "__main__":
    main()
