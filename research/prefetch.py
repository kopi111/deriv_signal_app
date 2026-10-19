"""Download every market's history one at a time, backing off when Deriv
rate-limits, so the parallel sweep only ever reads the cache."""

import time

from data import ThinHistory, load_candles
from instruments import INSTRUMENTS
from run_research import TIMEFRAMES

RATE_LIMIT_PAUSE = 60
ATTEMPTS = 5


def fetch_with_backoff(symbol, timeframe):
    for attempt in range(1, ATTEMPTS + 1):
        try:
            return load_candles(symbol, timeframe)
        except ThinHistory as error:
            if "rate limit" not in str(error) or attempt == ATTEMPTS:
                raise
            print(f"rate limited on {symbol} {timeframe}, waiting {RATE_LIMIT_PAUSE}s", flush=True)
            time.sleep(RATE_LIMIT_PAUSE)


def main():
    for timeframe in TIMEFRAMES:
        for instrument in INSTRUMENTS:
            fetch_with_backoff(instrument["symbol"], timeframe)
    print("all history cached", flush=True)


if __name__ == "__main__":
    main()
