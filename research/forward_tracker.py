"""Forward record of the Signal Desk playbook.

Every market in assets/strategies.json is replayed from the moment the
playbook was generated up to the last closed candle, with the research's own
entry rules, spreads and trade simulation. Nothing after that moment was seen
while the strategies were chosen, so the record is out-of-sample.

The whole record is recomputed on each run (the rules are fixed, so the past
never changes); run it hourly and it grows. Output: output/forward/.

    python3 research/forward_tracker.py                # the app's playbook
    python3 research/forward_tracker.py --all-markets  # every researched market
"""

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

import backtest
import build_playbook
import data
import strategies
from instruments import INSTRUMENTS, spread_for
from validate import prepare_bars

ROOT = Path(__file__).resolve().parent.parent
PLAYBOOK = ROOT / "assets" / "strategies.json"
OUTPUT_DIR = Path(__file__).parent / "output" / "forward"
ALL_MARKETS_OUTPUT_DIR = Path(__file__).parent / "output" / "forward_all"
FETCH_COUNT = 5000
PAUSE_BETWEEN_MARKETS_SECONDS = 2


def iso(epoch):
    return datetime.fromtimestamp(epoch, timezone.utc).strftime("%Y-%m-%d %H:%M")


def closed_candles(market):
    frame = data.fetch_recent(market["symbol"], market["granularity"], FETCH_COUNT)
    still_forming = frame["epoch"] + market["granularity"] > time.time()
    return frame[~still_forming].reset_index(drop=True)


def first_tracked_bar(frame, start_epoch):
    tracked = np.flatnonzero(frame["epoch"].to_numpy() >= start_epoch)
    if len(tracked) == 0 or tracked[0] < backtest.WARMUP_BARS:
        raise data.ThinHistory(f"not enough warm-up history before {iso(start_epoch)}")
    return int(tracked[0])


def trade_record(frame, bars, signal_bar, direction, exit_params, spread):
    trade, exit_bar = backtest.simulate_trade(bars, signal_bar, direction, exit_params, spread)
    epochs = frame["epoch"].to_numpy()
    held_bars = exit_bar - trade.entry_bar + 1
    reached_end_of_data = exit_bar == len(epochs) - 1
    hit_stop_or_target = trade.result_r <= -0.999 or abs(trade.result_r - exit_params["reward_risk"]) < 1e-9
    is_open = reached_end_of_data and held_bars < backtest.MAX_HOLD_BARS and not hit_stop_or_target
    return {
        "signal_at": iso(epochs[signal_bar]),
        "side": "BUY" if direction > 0 else "SELL",
        "entry": round(float(bars["open"][trade.entry_bar] + direction * spread), 5),
        "status": "open" if is_open else ("win" if trade.result_r > 0 else "loss"),
        "result_r": round(float(trade.result_r), 2),
        "closed_at": None if is_open else iso(epochs[exit_bar]),
    }, exit_bar


def replay(market, start_epoch):
    frame = closed_candles(market)
    bars = prepare_bars(frame)
    spread = spread_for(instrument_for(market["symbol"]), bars)
    signals = strategies.entry_signals(market["strategy"], frame, market["entry"])
    trades, free_from = [], first_tracked_bar(frame, start_epoch)
    for signal_bar in np.flatnonzero(signals):
        if signal_bar < free_from:
            continue
        if signal_bar + 1 >= len(frame):
            trades.append(pending_record(frame, signal_bar, int(signals[signal_bar])))
            break
        record, exit_bar = trade_record(frame, bars, signal_bar, int(signals[signal_bar]), market["exit"], spread)
        trades.append(record)
        free_from = exit_bar + 1
    return trades, iso(frame["epoch"].iloc[-1])


def pending_record(frame, signal_bar, direction):
    return {"signal_at": iso(frame["epoch"].iloc[signal_bar]), "side": "BUY" if direction > 0 else "SELL",
            "entry": None, "status": "open", "result_r": 0.0, "closed_at": None}


def instrument_for(symbol):
    return next(instrument for instrument in INSTRUMENTS if instrument["symbol"] == symbol)


def market_summary(market, trades, last_candle):
    closed = [t for t in trades if t["status"] != "open"]
    results = np.array([t["result_r"] for t in closed])
    gains, losses = results[results > 0].sum(), -results[results < 0].sum()
    return {
        "symbol": market["symbol"], "name": market["name"], "timeframe": market["timeframe"],
        "strategy": market["strategy"], "proven": market["proven"], "last_candle": last_candle,
        "closed": len(closed), "wins": int((results > 0).sum()), "losses": int((results <= 0).sum()),
        "total_r": round(float(results.sum()), 2) if len(results) else 0.0,
        "profit_factor": round(float(gains / losses), 2) if losses > 0 else None,
        "open": sum(t["status"] == "open" for t in trades), "trades": trades,
    }


def track_all(playbook):
    start_epoch = datetime.fromisoformat(playbook["generated"]).timestamp()
    records, failures = [], []
    for market in playbook["instruments"]:
        try:
            trades, last_candle = replay(market, start_epoch)
            records.append(market_summary(market, trades, last_candle))
        except Exception as error:
            failures.append({"symbol": market["symbol"], "error": str(error)})
            print(f"{market['symbol']}: FAILED - {error}", file=sys.stderr, flush=True)
        time.sleep(PAUSE_BETWEEN_MARKETS_SECONDS)
    return records, failures


def overall(records):
    closed = [t for r in records for t in r["trades"] if t["status"] != "open"]
    results = np.array([t["result_r"] for t in closed])
    return {"closed": len(closed), "wins": int((results > 0).sum()),
            "total_r": round(float(results.sum()), 2) if len(results) else 0.0}


def report_lines(playbook, records, failures, updated):
    total = overall(records)
    lines = [
        "# Signal Desk forward record", "",
        f"Tracking since the playbook was built: **{playbook['generated'][:16].replace('T', ' ')} UTC**. "
        f"Updated {updated} UTC.", "",
        "R = multiples of the amount risked per trade (risk $10 a trade: +1R = +$10, -1R = -$10). "
        "Spread is already charged.", "",
        f"**All markets: {total['closed']} closed trades, {total['wins']} wins, {total['total_r']:+.2f}R**", "",
        "| Market | TF | Strategy | Proven | Closed | Won | Lost | Total R | PF | Open |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in sorted(records, key=lambda r: -r["total_r"]):
        pf = "-" if r["profit_factor"] is None else r["profit_factor"]
        lines.append(f"| {r['name']} | {r['timeframe']} | {r['strategy']} | {'yes' if r['proven'] else 'no'} | "
                     f"{r['closed']} | {r['wins']} | {r['losses']} | {r['total_r']:+.2f} | {pf} | {r['open']} |")
    lines += [f"\n**Not checked this run:** {f['symbol']} - {f['error']}" for f in failures]
    return lines


def all_markets_playbook():
    """Each researched market with the strategy the research ranked best for it."""
    results = json.loads(build_playbook.RESULTS.read_text())
    best = build_playbook.best_per_symbol(results["instruments"])
    rows = [build_playbook.playbook_row(run, result) for _, run, result in best.values()]
    return {"generated": results["generated"], "instruments": rows}


def main():
    all_markets = "--all-markets" in sys.argv
    playbook = all_markets_playbook() if all_markets else json.loads(PLAYBOOK.read_text())
    output_dir = ALL_MARKETS_OUTPUT_DIR if all_markets else OUTPUT_DIR
    records, failures = track_all(playbook)
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    output_dir.mkdir(parents=True, exist_ok=True)
    ledger = {"playbook_generated": playbook["generated"], "updated": updated,
              "overall": overall(records), "markets": records, "failures": failures}
    (output_dir / "ledger.json").write_text(json.dumps(ledger, indent=1))
    report = "\n".join(report_lines(playbook, records, failures, updated)) + "\n"
    (output_dir / "REPORT.md").write_text(report)
    print(report)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
