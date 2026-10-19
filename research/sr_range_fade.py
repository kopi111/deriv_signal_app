"""Support/resistance range fade: the setup drawn in the September chart photos.

Swing pivots become horizontal levels. When price reaches a level the trade
fades it -- short at resistance, long at support -- with the stop just beyond
the level and the target at the opposite side of the range. Position size is
fixed-risk, so every result is expressed in R-multiples.

Levels are taken from candle bodies rather than wicks, matching how the lines
sit on the photographed charts. A level is live once its pivot is confirmed
and stays live until it ages out or price closes through it.

NO_LEVEL marks a bar with no usable level on that side.
"""

from dataclasses import dataclass

import numpy as np
import pandas as pd

NO_LEVEL = np.nan


@dataclass(frozen=True)
class RangeTrade:
    entry_bar: int
    direction: int
    result_r: float
    reward_risk: float


@dataclass(frozen=True)
class FadeRules:
    pivot_reach: int
    stop_share: float
    min_reward_risk: float
    level_memory: int
    max_hold_bars: int
    trigger: str


def _body_extremes(frame):
    body_high = np.maximum(frame["open"].to_numpy(), frame["close"].to_numpy())
    body_low = np.minimum(frame["open"].to_numpy(), frame["close"].to_numpy())
    return body_high, body_low


def _confirmed_pivots(values, reach, want_high):
    """Bar index at which each pivot becomes visible, paired with its price."""
    window = 2 * reach + 1
    rolling = pd.Series(values).rolling(window, center=True)
    extreme = rolling.max().to_numpy() if want_high else rolling.min().to_numpy()
    at_pivot = np.flatnonzero(values == extreme)
    return [(int(bar) + reach, float(values[bar])) for bar in at_pivot]


def _admit_due_levels(live, pending, next_index, bar):
    while next_index < len(pending) and pending[next_index][0] <= bar:
        live.append(pending[next_index])
        next_index += 1
    return next_index


def _retire_stale_levels(live, bar, memory):
    return [level for level in live if bar - level[0] <= memory]


def _nearest_above(live, price):
    above = [level[1] for level in live if level[1] > price]
    return min(above) if above else NO_LEVEL


def _nearest_below(live, price):
    below = [level[1] for level in live if level[1] < price]
    return max(below) if below else NO_LEVEL


def range_bounds(frame, pivot_reach, level_memory):
    """The nearest live resistance above and support below, for every bar."""
    body_high, body_low = _body_extremes(frame)
    pending_highs = _confirmed_pivots(body_high, pivot_reach, want_high=True)
    pending_lows = _confirmed_pivots(body_low, pivot_reach, want_high=False)
    close = frame["close"].to_numpy()

    resistance = np.full(len(close), NO_LEVEL)
    support = np.full(len(close), NO_LEVEL)
    live_highs, live_lows = [], []
    next_high, next_low = 0, 0

    for bar in range(len(close)):
        next_high = _admit_due_levels(live_highs, pending_highs, next_high, bar)
        next_low = _admit_due_levels(live_lows, pending_lows, next_low, bar)
        live_highs = _retire_stale_levels(live_highs, bar, level_memory)
        live_lows = _retire_stale_levels(live_lows, bar, level_memory)
        resistance[bar] = _nearest_above(live_highs, close[bar])
        support[bar] = _nearest_below(live_lows, close[bar])
    return resistance, support


def exit_result(bars, direction, entry, stop, target, first_bar, last_bar, reward_risk):
    """R-multiple and exit bar, assuming the stop wins any bar that touches both."""
    highs = bars["high"][first_bar:last_bar]
    lows = bars["low"][first_bar:last_bar]
    stop_hits = lows <= stop if direction > 0 else highs >= stop
    target_hits = highs >= target if direction > 0 else lows <= target
    first_stop = int(np.argmax(stop_hits)) if stop_hits.any() else len(highs)
    first_target = int(np.argmax(target_hits)) if target_hits.any() else len(highs)

    if first_stop <= first_target and first_stop < len(highs):
        return -1.0, first_bar + first_stop
    if first_target < len(highs):
        return reward_risk, first_bar + first_target
    risk = abs(entry - stop)
    exit_price = bars["close"][last_bar - 1]
    return float((exit_price - entry) * direction / risk), last_bar - 1


def _fade_at_level(bars, rules, bar, direction, level, opposite, spread):
    """One fade trade, or None when the geometry fails the reward filter.

    Direction is +1 long at support, -1 short at resistance. The spread always
    worsens the fill, and the stop sits beyond the level by a share of the range.
    """
    span = abs(level - opposite)
    if span <= 0:
        return None
    first_bar = bar if rules.trigger == "limit" else bar + 1
    if first_bar >= len(bars["close"]):
        return None

    entry = (level if rules.trigger == "limit" else bars["open"][first_bar])
    entry += direction * spread
    stop = level - direction * rules.stop_share * span
    target = opposite
    risk = abs(entry - stop)
    if risk <= 0:
        return None
    reward_risk = abs(target - entry) / risk
    if reward_risk < rules.min_reward_risk:
        return None

    if rules.trigger == "limit" and _stopped_on_fill_bar(bars, direction, stop, first_bar):
        return RangeTrade(first_bar, direction, -1.0, reward_risk), first_bar

    scan_from = first_bar + 1 if rules.trigger == "limit" else first_bar
    last_bar = min(scan_from + rules.max_hold_bars, len(bars["close"]))
    if scan_from >= last_bar:
        return None
    result_r, exit_bar = exit_result(
        bars, direction, entry, stop, target, scan_from, last_bar, reward_risk
    )
    return RangeTrade(first_bar, direction, result_r, reward_risk), exit_bar


def _stopped_on_fill_bar(bars, direction, stop, bar):
    """A limit fill is intrabar, so only the stop may resolve on that same bar."""
    if direction > 0:
        return bars["low"][bar] <= stop
    return bars["high"][bar] >= stop


def _touches_resistance(bars, rules, bar, resistance):
    if np.isnan(resistance):
        return False
    if rules.trigger == "limit":
        return bars["high"][bar] >= resistance
    return bars["high"][bar] >= resistance and bars["close"][bar] < resistance


def _touches_support(bars, rules, bar, support):
    if np.isnan(support):
        return False
    if rules.trigger == "limit":
        return bars["low"][bar] <= support
    return bars["low"][bar] <= support and bars["close"][bar] > support


def run(bars, resistance, support, rules, spread, warmup):
    """Every fade the rules produce, one position at a time."""
    trades, free_from = [], warmup
    bar_count = len(bars["close"])
    for bar in range(warmup, bar_count - 2):
        if bar < free_from:
            continue
        level, opposite, direction = NO_LEVEL, NO_LEVEL, 0
        if _touches_resistance(bars, rules, bar, resistance[bar]):
            level, opposite, direction = resistance[bar], support[bar], -1
        elif _touches_support(bars, rules, bar, support[bar]):
            level, opposite, direction = support[bar], resistance[bar], 1
        if direction == 0 or np.isnan(opposite):
            continue
        outcome = _fade_at_level(bars, rules, bar, direction, level, opposite, spread)
        if outcome is None:
            continue
        trade, exit_bar = outcome
        trades.append(trade)
        free_from = exit_bar + 1
    return trades


def summarize(trades):
    results = np.array([trade.result_r for trade in trades])
    if len(results) == 0:
        return {"trades": 0, "win_rate": 0.0, "profit_factor": 0.0,
                "expectancy_r": 0.0, "total_r": 0.0, "avg_reward_risk": 0.0}
    gains = results[results > 0].sum()
    losses = -results[results < 0].sum()
    return {
        "trades": int(len(results)),
        "win_rate": round(float((results > 0).mean()), 3),
        "profit_factor": round(float(gains / losses), 2) if losses > 0 else 99.0,
        "expectancy_r": round(float(results.mean()), 3),
        "total_r": round(float(results.sum()), 1),
        "avg_reward_risk": round(float(np.mean([t.reward_risk for t in trades])), 2),
    }
