"""Run evaluate_market over many (instrument, frame source) jobs in
parallel, saving each result as it finishes so a crash loses nothing."""

import json
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

from run_research import evaluate_market, to_json_value


def _run_job(job):
    instrument, timeframe, load_frame, saved = job
    if saved.exists():
        return json.loads(saved.read_text())
    result = evaluate_market(instrument, load_frame(), timeframe, np.random.default_rng(7))
    saved.write_text(json.dumps(result, default=to_json_value))
    print(f"done {instrument['symbol']} {timeframe}", flush=True)
    return json.loads(saved.read_text())


def run_sweep(jobs, runs_dir: Path):
    runs_dir.mkdir(parents=True, exist_ok=True)
    with ProcessPoolExecutor() as pool:
        return list(pool.map(_run_job, jobs))


def passes(results):
    return [(run["symbol"], run["timeframe"], r["strategy"]) for run in results
            for r in run["results"] if r["survives"]]


def test_count(results):
    return sum(len(run["results"]) for run in results)
