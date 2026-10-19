# Signal Desk (deriv_signal_app)

Flutter app that tells you when to take a trade on Deriv markets. It shows
Entry, Stop loss and Take profit, the checklist of reasons behind each signal,
and the strategy's out-of-sample track record.

## How signals are made

1. `research/` (Python) tests 7 strategy types on each market, on 1h and 15m
   Deriv candles: trend pullback, EMA bounce, channel breakout, RSI(2) snap-back,
   range fade, MACD pullback and EMA crossover.
2. Anchored walk-forward: settings are tuned only on older data and scored on the
   next unseen period, with the spread charged on every trade.
3. A strategy passes only if, on unseen data, it has 30+ trades, profit factor ≥ 1.2,
   ≥ 0.08R per trade, is profitable in 4 of 6 periods, beats random entries with the
   same stop and target (p ≤ 0.05), and does not lose on a final untouched 15% of history.
4. `build_playbook.py` writes `assets/strategies.json`, the one strategy per market that the app trades.
5. The app evaluates **closed candles only**, so signals never repaint.
   `test/signal_parity_test.dart` proves the Dart rules fire on exactly the same candles
   as the Python backtest (2,404 signals, bar for bar).

## Results (2026-09-18)

56 markets (26 volatility/step/jump indices, 26 forex pairs, 4 metals, Bitcoin), 1h and
15m, 10 strategy types including the 3 from the old dashboard: 1,120 tests. 9 passed:
V25 (1s), V15 (1s), V25, V150 (1s), V90 (1s), V75 (1s), Step Index, Bitcoin and EUR/AUD.
Caution: 7 of the 9 are on Deriv's random-number synthetics, where any edge is luck by
definition. Synthetics passed 1.7% of their tests against 0.3% for real markets, which
shows the passes are mostly the test's own false-positive rate. Demo-trade before real
money. Gold (XAU/USD) is pinned in the app as a near miss.
Full table: `research/output/REPORT.md`.

## Refresh the research

    cd research
    rm -rf output/runs
    python3 prefetch.py        # history one market at a time (Deriv rate-limits bursts)
    python3 run_research.py    # ~5 min on 16 cores
    python3 build_playbook.py
    python3 export_parity_fixture.py && cd .. && flutter test

## Run

Android (phone):

    flutter build apk --release        # -> build/app/outputs/flutter-apk/app-release.apk

Web:

    flutter build web --release && cd build/web && python3 -m http.server 8099

## Alerts while the app is closed (Android)

`lib/background/` runs an Android foreground service ("Watching 8 markets" in the
status bar). `SafeBootReceiver.kt` restarts it after a reboot and replaces the
plugin's receiver, which crashes on Android 15 when a force-stopped app is reopened.
It runs the same SignalDesk and engine as the screen and posts a
high-priority notification for every new signal. It restarts on phone boot.
On the phone: allow notifications, and set Battery > Unrestricted for Signal Desk,
or the phone's battery saver may pause it.

`signal_worker/` is an optional Python version of the same watcher for an always-on
machine (`--dry-run` prints alerts; `--service-account key.json` pushes via Firebase).

## Deriv feed and your own app ID

The public test app id 1089 refuses live subscriptions (it answers "Symbol is invalid"),
so the feed falls back to polling the last 3 candles every 20 seconds. With your own
app id it streams live automatically:

1. Log in at https://api.deriv.com, go to Dashboard, then Register application (scopes: Read).
2. Optional: create a Read-only API token under Account settings, API token.
3. Build with `--dart-define=DERIV_APP_ID=<id> --dart-define=DERIV_API_TOKEN=<token>`.

Deriv silently drops requests sent together, so requests go out one at a time from a queue.
History depth: 1h is about 1 year, 15m is about 7 months.
