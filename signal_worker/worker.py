"""Always-on signal worker. Every CHECK_EVERY seconds it looks at each
market in assets/strategies.json and, when a candle has just closed with a
signal, sends one alert. Alerts already sent are remembered on disk.

    .venv/bin/python worker.py --dry-run            # print alerts only
    .venv/bin/python worker.py --service-account key.json
"""

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "research"))

from data import ThinHistory, fetch_recent  # noqa: E402
from notifiers import ConsoleNotifier, FcmNotifier  # noqa: E402
from trade_signal import closed_candles, signal_on_last_candle  # noqa: E402

PLAYBOOK = ROOT / "assets" / "strategies.json"
SENT_LOG = Path(__file__).parent / "sent_alerts.json"
CHECK_EVERY = 30
TOPIC = "signals"


class SentAlerts:
    def __init__(self, path):
        self._path = path
        self._keys = set(json.loads(path.read_text())) if path.exists() else set()

    def __contains__(self, key):
        return key in self._keys

    def remember(self, key):
        self._keys.add(key)
        self._path.write_text(json.dumps(sorted(self._keys)[-500:]))


class MarketWatch:
    """Remembers the last closed candle seen per market, so each is checked once."""

    def __init__(self, markets):
        self._markets = markets
        self._last_checked = {}

    def fresh_signals(self, now_epoch):
        for market in self._markets:
            signal = self._check(market, now_epoch)
            if signal is not None:
                yield signal

    def _check(self, market, now_epoch):
        frame = closed_candles(fetch_recent(market["symbol"], market["granularity"]),
                               market["granularity"], now_epoch)
        last_epoch = int(frame["epoch"].iloc[-1])
        if self._last_checked.get(market["symbol"]) == last_epoch:
            return None
        self._last_checked[market["symbol"]] = last_epoch
        return signal_on_last_candle(market, frame)


def check_once(watch, sent, notifier):
    for signal in watch.fresh_signals(int(time.time())):
        if signal.key in sent:
            continue
        notifier.send(signal)
        sent.remember(signal.key)


def run(notifier):
    markets = json.loads(PLAYBOOK.read_text())["instruments"]
    watch, sent = MarketWatch(markets), SentAlerts(SENT_LOG)
    print(f"watching {len(markets)} markets, checking every {CHECK_EVERY}s", flush=True)
    while True:
        try:
            check_once(watch, sent, notifier)
        except (ThinHistory, OSError) as error:
            print(f"[retry] Deriv fetch failed: {error}", flush=True)
        time.sleep(CHECK_EVERY)


def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="print alerts instead of pushing")
    mode.add_argument("--service-account", type=Path, help="Firebase service account JSON key")
    return parser.parse_args()


def main():
    arguments = parse_arguments()
    notifier = ConsoleNotifier() if arguments.dry_run else FcmNotifier(arguments.service_account, TOPIC)
    run(notifier)


if __name__ == "__main__":
    main()
