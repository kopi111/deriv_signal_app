"""Anchored walk-forward, a random-entry baseline, and an untouched lockbox.

The last LOCKBOX_SHARE of history is never seen while choosing strategies.
Walk-forward runs on the rest: before each test fold, parameters are
re-chosen on all data preceding it, so every counted trade is out-of-sample.
"""

import numpy as np

import backtest
import indicators as ind
import strategies

LOCKBOX_SHARE = 0.15
FOLD_COUNT = 10
FIRST_TEST_FOLD = 4
MIN_TRAIN_TRADES = 15
RANDOM_TRIALS = 300


def prepare_bars(frame):
    bars = {column: frame[column].to_numpy() for column in ["open", "high", "low", "close"]}
    bars["atr"] = ind.atr(frame, 14).to_numpy()
    return bars


def _selection_score(trades):
    if len(trades) < MIN_TRAIN_TRADES:
        return -np.inf
    results = np.array([t.result_r for t in trades])
    return results.mean() * np.sqrt(len(results))


def _within(trades, start, end):
    return [t for t in trades if start <= t.entry_bar < end]


class StrategyTrial:
    """Every parameter set of one strategy, simulated once over the full history."""

    def __init__(self, name, frame, bars, spread):
        self.name = name
        self.runs = []
        for params in strategies.parameter_sets(name):
            signals = strategies.entry_signals(name, frame, params["entry"])
            self.runs.append((params, backtest.run(bars, signals, params["exit"], spread)))

    def best_params(self, start, end):
        scored = [(_selection_score(_within(trades, start, end)), params) for params, trades in self.runs]
        return max(scored, key=lambda pair: pair[0])[1]

    def trades_for(self, params, start, end):
        trades = next(trades for candidate, trades in self.runs if candidate is params)
        return _within(trades, start, end)


def fold_edges(bar_count):
    usable_end = int(bar_count * (1 - LOCKBOX_SHARE))
    edges = np.linspace(backtest.WARMUP_BARS, usable_end, FOLD_COUNT + 1).astype(int)
    return edges, usable_end


def walk_forward(trial, edges):
    folds, trades = [], []
    for fold in range(FIRST_TEST_FOLD, FOLD_COUNT):
        params = trial.best_params(backtest.WARMUP_BARS, edges[fold])
        fold_trades = trial.trades_for(params, edges[fold], edges[fold + 1])
        folds.append({"params": params, "total_r": round(sum(t.result_r for t in fold_trades), 2)})
        trades += fold_trades
    return folds, trades


def random_entry_p_value(bars, trades, exit_params, spread, window, rng):
    if not trades:
        return 1.0
    actual = sum(t.result_r for t in trades)
    long_share = np.mean([t.direction > 0 for t in trades])
    beaten = 0
    for _ in range(RANDOM_TRIALS):
        signal_bars = rng.integers(window[0], window[1] - 2, size=len(trades))
        directions = np.where(rng.random(len(trades)) < long_share, 1, -1)
        total = sum(
            backtest.simulate_trade(bars, bar, direction, exit_params, spread)[0].result_r
            for bar, direction in zip(signal_bars, directions)
        )
        beaten += total >= actual
    return round(beaten / RANDOM_TRIALS, 3)
