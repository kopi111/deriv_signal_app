"""AlgoAlpha "Support & Resistance Ultra Toolkit", ported to Python for backtesting.

The TradingView indicator detects zones two ways and tracks what price does at them.
This port keeps the Pivots mode, which is its default and the one with a tradable signal:

  * A swing high (or low) is a pivot once `pivot_length` bars on each side confirm it.
  * Two same-side pivots within `max_gap` bars whose prices sit within a volatility
    tolerance -- `match_mult` times the 40-bar stdev of closes -- form a zone. The zone
    is a band: its edge is the extreme of the two pivots and its thickness is how far the
    pivots' own OHLC reach back from that edge.
  * A live zone is watched bar by bar. The indicator's own words:
      - break   : a close through the far edge (support broken by close < bottom).
      - reject  : price entered the zone, then a later bar closes back out the near edge.
      - sweep   : a wick pierces the far edge but the body closes back inside.
    Rejections and sweeps are the fade signals; a break is the breakout signal.

Only confirmed, non-repainting state is emitted: a pivot is dated at the bar it becomes
visible (pivot + length), exactly as the indicator back-draws the box to the formation but
ages it from admission. Nothing here looks ahead.

The engine returns, per bar, boolean event flags and, for each live zone touched, the
indicator's "mitigation" estimate so its headline claim can be tested for calibration.
"""

from dataclasses import dataclass

import numpy as np
import pandas as pd

VOL_LENGTH = 40


@dataclass
class Zone:
    top: float
    bottom: float
    is_support: bool
    born: int
    broken_age: int | None = None
    was_touch: bool = False
    visit_open: bool = False
    rejected_visit: bool = False
    swept_visit: bool = False


@dataclass
class UltraRules:
    pivot_length: int = 7
    max_gap: int = 100
    match_mult: float = 1.0
    expiry_bars: int = 500
    stop_on_break: bool = True


@dataclass
class ZoneEvents:
    """Per-bar signal flags, aligned to the bar whose close confirms them."""
    bull_reject: np.ndarray
    bear_reject: np.ndarray
    bull_sweep: np.ndarray
    bear_sweep: np.ndarray
    bull_break: np.ndarray
    bear_break: np.ndarray


def _confirmed_pivots(values, length, want_high):
    """Each pivot's visible bar (centre + length) and its price, non-repainting."""
    window = 2 * length + 1
    rolling = pd.Series(values).rolling(window, center=True)
    extreme = (rolling.max() if want_high else rolling.min()).to_numpy()
    centres = np.flatnonzero(values == extreme)
    return [(int(c) + length, float(values[c])) for c in centres if int(c) + length < len(values)]


def _zone_bounds(price_a, ohlc_a, price_b, ohlc_b, is_resistance, tolerance):
    """The band two paired pivots form: edge from the extreme, thickness from their OHLC."""
    if is_resistance:
        edge = max(ohlc_a["h"], ohlc_b["h"])
        reach = max(edge - value for value in _ohlc_values(ohlc_a, ohlc_b)
                    if 0.0 <= edge - value <= tolerance)
        thickness = max(abs(price_a - price_b), reach)
        return edge, edge - thickness
    edge = min(ohlc_a["l"], ohlc_b["l"])
    reach = max(value - edge for value in _ohlc_values(ohlc_a, ohlc_b)
                if 0.0 <= value - edge <= tolerance)
    thickness = max(abs(price_a - price_b), reach)
    return edge + thickness, edge


def _ohlc_values(ohlc_a, ohlc_b):
    for ohlc in (ohlc_a, ohlc_b):
        yield from (ohlc["o"], ohlc["h"], ohlc["l"], ohlc["c"])


def _pair_pivots(pivots, ohlc_by_bar, is_resistance, tolerance, max_gap):
    """Walk pivots in time; pair each with the newest earlier pivot inside gap and tolerance.

    Returns the zones in creation order, each as (top, bottom, born_bar).
    """
    created = []
    memory = []
    for bar, price in pivots:
        matched = None
        for previous_bar, previous_price in reversed(memory):
            gap = bar - previous_bar
            if gap <= 0 or gap > max_gap:
                continue
            if abs(price - previous_price) <= tolerance:
                matched = (previous_bar, previous_price)
                break
        if matched is not None:
            prev_bar, prev_price = matched
            top, bottom = _zone_bounds(
                prev_price, ohlc_by_bar[prev_bar], price, ohlc_by_bar[bar], is_resistance, tolerance
            )
            if top > bottom:
                created.append((round(top, 10), round(bottom, 10), bar))
        memory.append((bar, price))
        memory = [item for item in memory if bar - item[0] <= max_gap]
    return created


def zone_events(frame, rules, tolerance_series=None):
    """Run the full zone lifecycle and return per-bar fade/break signals."""
    high = frame["high"].to_numpy()
    low = frame["low"].to_numpy()
    close = frame["close"].to_numpy()
    open_ = frame["open"].to_numpy()
    n = len(close)

    if tolerance_series is None:
        vol = pd.Series(close).rolling(VOL_LENGTH).std().to_numpy()
        tolerance_series = np.where(np.isnan(vol), np.inf, vol) * rules.match_mult

    ohlc_by_bar = {i: {"o": open_[i], "h": high[i], "l": low[i], "c": close[i]} for i in range(n)}
    median_tolerance = float(np.nanmedian(tolerance_series[np.isfinite(tolerance_series)]))

    res_pivots = _confirmed_pivots(high, rules.pivot_length, want_high=True)
    sup_pivots = _confirmed_pivots(low, rules.pivot_length, want_high=False)
    res_zones = _pair_pivots(res_pivots, ohlc_by_bar, True, median_tolerance, rules.max_gap)
    sup_zones = _pair_pivots(sup_pivots, ohlc_by_bar, False, median_tolerance, rules.max_gap)

    zones_by_birth = {}
    for top, bottom, born in res_zones:
        zones_by_birth.setdefault(born, []).append(Zone(top, bottom, False, born))
    for top, bottom, born in sup_zones:
        zones_by_birth.setdefault(born, []).append(Zone(top, bottom, True, born))

    events = ZoneEvents(*[np.zeros(n, dtype=bool) for _ in range(6)])
    live = []

    for bar in range(n):
        for zone in zones_by_birth.get(bar, []):
            intact = close[bar] >= zone.bottom if zone.is_support else close[bar] <= zone.top
            if intact and not _overlaps(live, zone):
                live.append(zone)
        _step_zones(live, bar, high, low, close, open_, rules, events)
        live = [z for z in live if z.broken_age is None and bar - z.born < rules.expiry_bars]

    return events


def _overlaps(live, candidate):
    for zone in live:
        if candidate.bottom <= zone.top and candidate.top >= zone.bottom:
            return True
    return False


def _step_zones(live, bar, high, low, close, open_, rules, events):
    for zone in live:
        age = bar - zone.born
        if age <= 0 or zone.broken_age is not None:
            continue
        touched = high[bar] >= zone.bottom and low[bar] <= zone.top
        new_visit = touched and not zone.was_touch
        if new_visit:
            zone.visit_open = True
            zone.rejected_visit = False
            zone.swept_visit = False

        closed_through = close[bar] < zone.bottom if zone.is_support else close[bar] > zone.top
        if closed_through:
            zone.broken_age = age
            if zone.is_support:
                events.bear_break[bar] = True
            else:
                events.bull_break[bar] = True
        else:
            safe_close = close[bar] > zone.top if zone.is_support else close[bar] < zone.bottom
            body_low = min(open_[bar], close[bar])
            body_high = max(open_[bar], close[bar])
            wick_through = touched and (
                (low[bar] < zone.bottom and body_low >= zone.bottom) if zone.is_support
                else (high[bar] > zone.top and body_high <= zone.top))
            swept = wick_through and not zone.swept_visit
            rejected = zone.visit_open and safe_close and not zone.rejected_visit
            if swept:
                zone.swept_visit = True
                if zone.is_support:
                    events.bull_sweep[bar] = True
                else:
                    events.bear_sweep[bar] = True
            if rejected:
                zone.rejected_visit = True
                if zone.is_support:
                    events.bull_reject[bar] = True
                else:
                    events.bear_reject[bar] = True
            if not touched:
                zone.visit_open = False
        zone.was_touch = touched
