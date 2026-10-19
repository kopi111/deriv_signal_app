"""Write ../test/fixtures/parity.json: real candles plus the Python signal
for every bar, every strategy and every parameter set. The Dart parity
test must reproduce each one."""

import json
from pathlib import Path

import indicators as ind
import strategies
from data import load_candles

FIXTURE = Path(__file__).parent.parent / "test" / "fixtures" / "parity.json"
SAMPLES = [("frxXAUUSD", "1h"), ("R_75", "1h"), ("frxEURUSD", "15m")]
BARS = 1500


def cases_for(frame):
    cases = []
    for name in strategies.STRATEGIES:
        for params in strategies.parameter_sets(name)[::4]:
            signals = strategies.entry_signals(name, frame, params["entry"])
            cases.append({"strategy": name, "params": params["entry"],
                          "signals": [int(value) for value in signals]})
    return cases


def main():
    samples = []
    for symbol, timeframe in SAMPLES:
        frame = load_candles(symbol, timeframe).tail(BARS).reset_index(drop=True)
        samples.append({
            "symbol": symbol,
            "candles": frame.to_dict(orient="records"),
            "atr": [round(float(v), 10) for v in ind.atr(frame, 14)],
            "cases": cases_for(frame),
        })
    FIXTURE.parent.mkdir(parents=True, exist_ok=True)
    FIXTURE.write_text(json.dumps(samples))
    print(f"wrote {FIXTURE} ({sum(len(s['cases']) for s in samples)} cases)")


if __name__ == "__main__":
    main()
