"""Deriv candle history: paged fetch over WebSocket with a CSV cache."""

import asyncio
import json
import time
from pathlib import Path

import pandas as pd
import websockets

DERIV_ENDPOINTS = (
    "wss://ws.derivws.com/websockets/v3?app_id=1089",
    "wss://red.binaryws.com/websockets/v3?app_id=1089",
    "wss://green.binaryws.com/websockets/v3?app_id=1089",
    "wss://blue.binaryws.com/websockets/v3?app_id=1089",
)
CACHE_DIR = Path(__file__).parent / "cache"
CACHE_MAX_AGE_SECONDS = 6 * 3600
GRANULARITY_SECONDS = {"5m": 300, "15m": 900, "1h": 3600, "4h": 14400}


class ThinHistory(Exception):
    """Raised when Deriv returns less history than a backtest needs."""


class DerivUnreachable(Exception):
    """Raised when every Deriv endpoint refuses the connection."""


async def _open_socket():
    """Connect to the first endpoint that answers; Deriv fronts fail one at a time."""
    failures = []
    for endpoint in DERIV_ENDPOINTS:
        try:
            return await websockets.connect(endpoint, max_size=None, open_timeout=15)
        except Exception as error:
            failures.append(f"{endpoint.split('/')[2]}: {error}")
    raise DerivUnreachable("; ".join(failures))


async def _request_page(socket, symbol, granularity, end):
    await socket.send(json.dumps({
        "ticks_history": symbol, "count": 5000, "end": end,
        "granularity": granularity, "style": "candles",
    }))
    response = json.loads(await socket.recv())
    if "error" in response:
        raise ThinHistory(f"{symbol}: {response['error']['message']}")
    return response.get("candles", [])


PAGE_ATTEMPTS = 3
PAGE_RETRY_SECONDS = 5


async def _page_with_retry(socket, symbol, granularity, end):
    """Deriv answers some pages with a generic error; a short wait clears it."""
    for attempt in range(PAGE_ATTEMPTS):
        try:
            return await _request_page(socket, symbol, granularity, end)
        except ThinHistory as error:
            if attempt == PAGE_ATTEMPTS - 1:
                raise
            print(f"{symbol}: {error}; retrying page", flush=True)
            await asyncio.sleep(PAGE_RETRY_SECONDS)


async def _fetch_pages(symbol, granularity, pages):
    candles, end = [], "latest"
    async with await _open_socket() as socket:
        for _ in range(pages):
            try:
                page = await _page_with_retry(socket, symbol, granularity, end)
            except ThinHistory as error:
                print(f"{symbol}: stopping at {len(candles)} candles ({error})", flush=True)
                break
            if not page:
                break
            candles = page + candles
            end = str(page[0]["epoch"] - 1)
    return candles


def _to_frame(candles):
    frame = pd.DataFrame(candles).drop_duplicates("epoch").sort_values("epoch")
    return frame[["epoch", "open", "high", "low", "close"]].astype(float).reset_index(drop=True)


def _cache_path(symbol, timeframe):
    return CACHE_DIR / f"{symbol}_{timeframe}.csv"


def _is_fresh(path):
    return path.exists() and time.time() - path.stat().st_mtime < CACHE_MAX_AGE_SECONDS


def load_candles(symbol, timeframe="1h", pages=12, minimum_bars=3000):
    path = _cache_path(symbol, timeframe)
    if _is_fresh(path):
        return pd.read_csv(path)
    try:
        candles = asyncio.run(_fetch_pages(symbol, GRANULARITY_SECONDS[timeframe], pages))
    except Exception as error:
        return _stale_cache_or_raise(path, symbol, timeframe, error)
    frame = _to_frame(candles)
    if len(frame) < minimum_bars:
        raise ThinHistory(f"{symbol} {timeframe}: only {len(frame)} bars, need {minimum_bars}")
    if _longer_cache(path, len(frame)):
        print(f"{symbol} {timeframe}: fetched {len(frame)} bars, keeping the longer cache", flush=True)
        return pd.read_csv(path)
    CACHE_DIR.mkdir(exist_ok=True)
    frame.to_csv(path, index=False)
    return frame


def _longer_cache(path, fetched_bars):
    """A short fetch must never replace history a longer run already paid for."""
    if not path.exists():
        return False
    return sum(1 for _ in path.open()) - 1 > fetched_bars


def _stale_cache_or_raise(path, symbol, timeframe, error):
    """Deriv is unreachable: fall back to cached bars, saying how old they are."""
    if not path.exists():
        raise error
    age_hours = (time.time() - path.stat().st_mtime) / 3600
    print(f"{symbol} {timeframe}: Deriv unreachable ({error}); "
          f"using cache {age_hours:.0f}h old", flush=True)
    return pd.read_csv(path)


def fetch_recent(symbol, granularity_seconds, count=1500):
    """Latest candles straight from Deriv, no cache. Includes the forming candle."""
    return _to_frame(asyncio.run(_fetch_count(symbol, granularity_seconds, count)))


async def _fetch_count(symbol, granularity, count):
    async with await _open_socket() as socket:
        await socket.send(json.dumps({
            "ticks_history": symbol, "count": count, "end": "latest",
            "granularity": granularity, "style": "candles",
        }))
        response = json.loads(await socket.recv())
    if "error" in response:
        raise ThinHistory(f"{symbol}: {response['error']['message']}")
    return response.get("candles", [])
