"""Find a fresh signal on the last closed candle and size its levels,
using the same rules and ATR sizing as the app and the backtest."""

from dataclasses import dataclass

import indicators as ind
import strategies


@dataclass(frozen=True)
class TradeSignal:
    symbol: str
    name: str
    direction: str
    candle_epoch: int
    entry: float
    stop: float
    target: float
    strategy: str
    proven: bool

    @property
    def key(self):
        return f"{self.symbol}:{self.candle_epoch}"


def closed_candles(frame, granularity_seconds, now_epoch):
    return frame[frame["epoch"] + granularity_seconds <= now_epoch].reset_index(drop=True)


def signal_on_last_candle(market, frame):
    signals = strategies.entry_signals(market["strategy"], frame, market["entry"])
    direction = int(signals[-1])
    if direction == 0:
        return None
    return _size(market, frame, direction)


def _size(market, frame, direction):
    entry = float(frame["close"].iloc[-1])
    risk = market["exit"]["stop_atr"] * float(ind.atr(frame, 14).iloc[-1])
    return TradeSignal(
        symbol=market["symbol"],
        name=market["name"],
        direction="Buy" if direction > 0 else "Sell",
        candle_epoch=int(frame["epoch"].iloc[-1]),
        entry=entry,
        stop=entry - direction * risk,
        target=entry + direction * risk * market["exit"]["reward_risk"],
        strategy=market["strategy"],
        proven=market["proven"],
    )
