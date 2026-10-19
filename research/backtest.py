"""Trade simulation in R-multiples (1R = the distance to the stop).

Signal on bar i's close -> enter at bar i+1's open, paying the full spread.
Stop and target are fixed from ATR at the signal bar. If a bar touches
both, the stop is assumed hit first. Trades still open after MAX_HOLD_BARS
exit at that bar's close. One position at a time.
"""

from dataclasses import dataclass

import numpy as np

MAX_HOLD_BARS = 48
WARMUP_BARS = 250


@dataclass(frozen=True)
class Trade:
    entry_bar: int
    direction: int
    result_r: float


def _exit_offset(direction, highs, lows, stop, target):
    stop_hits = lows <= stop if direction > 0 else highs >= stop
    target_hits = highs >= target if direction > 0 else lows <= target
    first_stop = np.argmax(stop_hits) if stop_hits.any() else len(highs)
    first_target = np.argmax(target_hits) if target_hits.any() else len(highs)
    return first_stop, first_target


def simulate_trade(bars, signal_bar, direction, exit_params, spread):
    entry_bar = signal_bar + 1
    last_bar = min(entry_bar + MAX_HOLD_BARS, len(bars["close"]))
    entry = bars["open"][entry_bar] + direction * spread
    risk = exit_params["stop_atr"] * bars["atr"][signal_bar]
    stop = entry - direction * risk
    target = entry + direction * risk * exit_params["reward_risk"]
    highs, lows = bars["high"][entry_bar:last_bar], bars["low"][entry_bar:last_bar]
    first_stop, first_target = _exit_offset(direction, highs, lows, stop, target)
    if first_stop <= first_target and first_stop < len(highs):
        return Trade(entry_bar, direction, (stop - entry) * direction / risk), entry_bar + first_stop
    if first_target < len(highs):
        return Trade(entry_bar, direction, exit_params["reward_risk"]), entry_bar + first_target
    exit_price = bars["close"][last_bar - 1]
    return Trade(entry_bar, direction, (exit_price - entry) * direction / risk), last_bar - 1


def run(bars, signals, exit_params, spread):
    trades, free_from = [], WARMUP_BARS
    for signal_bar in np.flatnonzero(signals):
        if signal_bar < free_from or signal_bar + 2 >= len(signals):
            continue
        trade, exit_bar = simulate_trade(bars, signal_bar, int(signals[signal_bar]), exit_params, spread)
        trades.append(trade)
        free_from = exit_bar + 1
    return trades


def summarize(trades):
    results = np.array([t.result_r for t in trades])
    if len(results) == 0:
        return {"trades": 0, "win_rate": 0.0, "profit_factor": 0.0, "expectancy_r": 0.0,
                "total_r": 0.0, "max_drawdown_r": 0.0}
    gains, losses = results[results > 0].sum(), -results[results < 0].sum()
    equity = np.cumsum(results)
    drawdown = np.max(np.maximum.accumulate(np.concatenate([[0], equity]))[1:] - equity)
    return {
        "trades": int(len(results)),
        "win_rate": round(float((results > 0).mean()), 3),
        "profit_factor": round(float(gains / losses), 2) if losses > 0 else 99.0,
        "expectancy_r": round(float(results.mean()), 3),
        "total_r": round(float(results.sum()), 1),
        "max_drawdown_r": round(float(drawdown), 1),
    }
