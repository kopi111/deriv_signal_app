"""Entry rules. Each rule reads closed bars only and returns +1 (buy),
-1 (sell) or 0 per bar. A trade is entered on the NEXT bar's open."""

import itertools

import numpy as np
import pandas as pd

import indicators as ind

EXIT_GRID = {"stop_atr": [1.5, 2.0], "reward_risk": [1.5, 2.0]}
LEGACY_EXIT_GRID = {"stop_atr": [2.0, 3.0], "reward_risk": [0.375, 0.5, 0.833]}


def _crossed_above(series, level):
    return (series.shift(1) < level) & (series >= level)


def _crossed_below(series, level):
    return (series.shift(1) > level) & (series <= level)


def _combine(longs, shorts):
    return (longs.astype(int) - shorts.astype(int)).to_numpy()


def _trend(frame):
    close = frame["close"]
    ema50, ema200 = ind.ema(close, 50), ind.ema(close, 200)
    uptrend = (close > ema200) & (ema50 > ema200)
    downtrend = (close < ema200) & (ema50 < ema200)
    return uptrend, downtrend


def trend_pullback(frame, rsi_level):
    uptrend, downtrend = _trend(frame)
    strength = ind.rsi(frame["close"], 14)
    longs = uptrend & _crossed_above(strength, rsi_level)
    shorts = downtrend & _crossed_below(strength, 100 - rsi_level)
    return _combine(longs, shorts)


def ema_bounce(frame, touch_period):
    uptrend, downtrend = _trend(frame)
    touch = ind.ema(frame["close"], touch_period)
    bullish_rejection = (frame["low"] <= touch) & (frame["close"] > touch) & (frame["close"] > frame["open"])
    bearish_rejection = (frame["high"] >= touch) & (frame["close"] < touch) & (frame["close"] < frame["open"])
    return _combine(uptrend & bullish_rejection, downtrend & bearish_rejection)


def donchian_breakout(frame, period, adx_min):
    close = frame["close"]
    ema200 = ind.ema(close, 200)
    trending = ind.adx(frame, 14) > adx_min
    upper = ind.prior_highest(frame["high"], period)
    lower = ind.prior_lowest(frame["low"], period)
    longs = _crossed_above(close - upper, 0) & trending & (close > ema200)
    shorts = _crossed_below(close - lower, 0) & trending & (close < ema200)
    return _combine(longs, shorts)


def rsi2_reversion(frame, oversold):
    close = frame["close"]
    ema200 = ind.ema(close, 200)
    fast_rsi = ind.rsi(close, 2)
    longs = (close > ema200) & _crossed_below(fast_rsi, oversold)
    shorts = (close < ema200) & _crossed_above(fast_rsi, 100 - oversold)
    return _combine(longs, shorts)


def bollinger_reversion(frame, adx_max):
    close = frame["close"]
    lower, _, upper = ind.bollinger(close, 20, 2.0)
    ranging = ind.adx(frame, 14) < adx_max
    longs = ranging & _crossed_above(close - lower, 0)
    shorts = ranging & _crossed_below(close - upper, 0)
    return _combine(longs, shorts)


def macd_pullback(frame, trend_period):
    close = frame["close"]
    trend_line = ind.ema(close, trend_period)
    line, signal = ind.macd(close)
    gap = line - signal
    longs = (close > trend_line) & (line < 0) & _crossed_above(gap, 0)
    shorts = (close < trend_line) & (line > 0) & _crossed_below(gap, 0)
    return _combine(longs, shorts)


def ema_cross(frame, fast, slow):
    close = frame["close"]
    gap = ind.ema(close, fast) - ind.ema(close, slow)
    return _combine(_crossed_above(gap, 0), _crossed_below(gap, 0))


def rsi_crossback(frame, period, oversold, overbought):
    strength = ind.rsi(frame["close"], period)
    return _combine(_crossed_above(strength, oversold), _crossed_below(strength, overbought))


def macd_cross(frame):
    line, signal = ind.macd(frame["close"])
    gap = line - signal
    return _combine(_crossed_above(gap, 0), _crossed_below(gap, 0))


STRATEGIES = {
    "trend_pullback": (trend_pullback, {"rsi_level": [35, 40, 45]}),
    "ema_bounce": (ema_bounce, {"touch_period": [20, 50]}),
    "donchian_breakout": (donchian_breakout, {"period": [20, 55], "adx_min": [20, 25]}),
    "rsi2_reversion": (rsi2_reversion, {"oversold": [5, 10]}),
    "bollinger_reversion": (bollinger_reversion, {"adx_max": [20, 25]}),
    "macd_pullback": (macd_pullback, {"trend_period": [100, 200]}),
    "ema_cross": (ema_cross, {"fast": [9, 20], "slow": [50]}),
    "legacy_rsi_crossback": (rsi_crossback, {"period": [5, 9, 14], "oversold": [20, 25, 30],
                                             "overbought": [70, 75]}, LEGACY_EXIT_GRID),
    "legacy_ema_cross": (ema_cross, {"fast": [5, 12], "slow": [21, 26]}, LEGACY_EXIT_GRID),
    "legacy_macd_cross": (macd_cross, {}, LEGACY_EXIT_GRID),
}


def _expand(grid):
    keys = list(grid)
    return [dict(zip(keys, values)) for values in itertools.product(*grid.values())]


def _exit_grid(strategy_name):
    definition = STRATEGIES[strategy_name]
    return definition[2] if len(definition) > 2 else EXIT_GRID


def parameter_sets(strategy_name):
    entry_grid = STRATEGIES[strategy_name][1]
    return [
        {"entry": entry, "exit": exit_params}
        for entry in _expand(entry_grid)
        for exit_params in _expand(_exit_grid(strategy_name))
    ]


def entry_signals(strategy_name, frame, entry_params):
    rule = STRATEGIES[strategy_name][0]
    return rule(frame, **entry_params)
