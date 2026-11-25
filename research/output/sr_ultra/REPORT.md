# AlgoAlpha "Support & Resistance Ultra Toolkit" — Python port + backtest

Date: 2026-10-22 · Code: `research/sr_ultra.py` (engine), `research/run_sr_ultra.py` (backtest)
Data: cached Deriv candles in `research/cache/` (offline). 18 real markets (15 FX majors/crosses +
Gold, Silver, Platinum) at **15m** (~24,000 bars each) and **1h** (~6,000 bars each).

## Verdict: no tradable edge. Every market, every signal, both timeframes — negative.

| Timeframe | Signal | Markets positive | Pooled net R | Mean R/trade | t-stat | Random-walk control (mean R) |
|---|---|---|---|---|---|---|
| 15m | rejection | **0 / 18** | −13,605 | −0.68 | −103 | −0.42 |
| 15m | sweep | **0 / 18** | −5,895 | −0.64 | −63 | −0.43 |
| 15m | breakout | **0 / 18** | −9,859 | −0.66 | −85 | −0.41 |
| 1h | rejection | **0 / 18** | −1,608 | −0.35 | −19 | −0.19 |
| 1h | sweep | **0 / 18** | −871 | −0.38 | −15 | −0.22 |
| 1h | breakout | **0 / 18** | −1,246 | −0.35 | −17 | −0.19 |

## What was ported
The indicator's **Pivots** mode and its live zone tracking, faithfully:
- Pivots confirmed `pivot_length` bars each side; two same-side pivots within `max_gap` and within a
  volatility tolerance (`match_mult` × 40-bar stdev of closes) form a **band** (edge = pivot extreme,
  thickness = how far their OHLC reach back). Non-repainting: a zone is dated at the bar it becomes visible.
- Per bar: **break** (close through the far edge), **rejection** (entered the zone, then closed back out
  the near edge), **sweep** (wick pierces the far edge, body closes back inside). These are the indicator's
  own event definitions, line for line.

## How each signal was traded
The indicator names no trade, so each flag became its most literal trade: rejection and sweep → fade
back into the range; break → trade with the break. Entry at the next open, pay the instrument's spread,
risk 0.5·ATR to a 2:1 reward, one position at a time, held ≤96 bars. Results in R-multiples.

## Why it loses
- Pooled win rate is **11% at 15m, 22% at 1h**. At 2:1 reward you need **>33.3%** just to break even,
  so the payoff geometry is underwater before costs. With a 2·ATR target and a 1·ATR stop plus a 96-bar
  hold cap, the near stop is hit far more often than the far target, and many winners time out — so the
  hit rate never approaches breakeven. The zones do nothing to change this.
- Against the **random-walk control** (martingale prices with no real support or resistance), the real
  markets do **no better — slightly worse** per trade (15m: −0.68R real vs −0.42R luck). A genuine S/R
  edge would make the real mean R *beat* the control. It does not. The signals carry no directional
  information the geometry and spread don't already erase.
- This matches the earlier [S/R range-fade study](../sr_range_fade/REPORT.md): support/resistance fades
  on these instruments are noise once costs are paid.

## "Do the opposite" (tested 2026-10-22)
Flipping every trade's direction (same zones, same 2:1 / 1·ATR construction, spread still paid) loses
almost exactly as much, 15m pooled: rejection −13,605R normal vs **−13,385R inverted**; sweep −5,895 vs
−5,923; breakout −9,859 vs −9,109. Win rate stays ~11% both ways. Flipping cannot rescue it because the
loss is not a wrong-direction signal — it is (a) the spread, paid whichever way you trade, and (b) the
2:1-with-hold-cap geometry, which hits the near stop more than the far target in **both** directions. A
signal with no predictive edge gives none back when mirrored.

## Honest limits
- One trade model (fixed 2:1, 0.5·ATR stop, next-open entry). A different stop/target or an exit at the
  opposite zone edge would change the numbers, but a −100 t-stat across 36 market-timeframe runs with a
  losing random-walk control is not rescued by parameter choice.
- The indicator's **"mitigation" estimate** (its break-before-expiry probability) was not calibration-
  tested here — the engine computes zones and events; the mitigation cohort stat is a possible follow-up.
- Default indicator parameters used (pivot_length 7, max_gap 100, match_mult 1.0, expiry 500, stop-on-break).

## Reproduce
```bash
cd ~/projects/deriv_signal_app/research
python3 run_sr_ultra.py --timeframe 15m
python3 run_sr_ultra.py --timeframe 1h
```
