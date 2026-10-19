"""Fetch 5m history for the instruments that appear in the chart photos."""

import sys

import data

PHOTO_SYMBOLS = ["1HZ10V", "1HZ15V", "1HZ25V", "1HZ30V", "1HZ75V", "1HZ90V", "JD10"]


def main():
    for symbol in PHOTO_SYMBOLS:
        try:
            frame = data.load_candles(symbol, timeframe="5m", pages=12, minimum_bars=5000)
            print(f"{symbol}: {len(frame)} bars", flush=True)
        except Exception as error:
            print(f"{symbol}: FAILED {error}", file=sys.stderr, flush=True)


if __name__ == "__main__":
    main()
