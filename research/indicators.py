"""Indicators defined so they can be ported bar-for-bar to Dart.

EMA seeds on the first close (adjust=False). RSI, ATR and ADX use Wilder
smoothing, expressed as an EMA with alpha = 1/period.
"""

import numpy as np
import pandas as pd


def ema(series, period):
    return series.ewm(span=period, adjust=False).mean()


def wilder(series, period):
    return series.ewm(alpha=1 / period, adjust=False).mean()


def rsi(close, period):
    change = close.diff().fillna(0.0)
    average_gain = wilder(change.clip(lower=0), period)
    average_loss = wilder(-change.clip(upper=0), period)
    strength = average_gain / average_loss.replace(0, np.nan)
    return (100 - 100 / (1 + strength)).fillna(100.0)


def true_range(frame):
    previous_close = frame["close"].shift(1).fillna(frame["close"])
    return pd.concat([
        frame["high"] - frame["low"],
        (frame["high"] - previous_close).abs(),
        (frame["low"] - previous_close).abs(),
    ], axis=1).max(axis=1)


def atr(frame, period=14):
    return wilder(true_range(frame), period)


def adx(frame, period=14):
    up_move = frame["high"].diff().fillna(0.0)
    down_move = (-frame["low"].diff()).fillna(0.0)
    plus_dm = up_move.where((up_move > down_move) & (up_move > 0), 0.0)
    minus_dm = down_move.where((down_move > up_move) & (down_move > 0), 0.0)
    range_average = wilder(true_range(frame), period).replace(0, np.nan)
    plus_di = 100 * wilder(plus_dm, period) / range_average
    minus_di = 100 * wilder(minus_dm, period) / range_average
    spread = (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    return wilder((100 * spread).fillna(0.0), period)


def macd(close, fast=12, slow=26, signal=9):
    line = ema(close, fast) - ema(close, slow)
    return line, ema(line, signal)


def bollinger(close, period=20, width=2.0):
    middle = close.rolling(period).mean()
    deviation = close.rolling(period).std(ddof=0)
    return middle - width * deviation, middle, middle + width * deviation


def prior_highest(high, period):
    return high.shift(1).rolling(period).max()


def prior_lowest(low, period):
    return low.shift(1).rolling(period).min()
