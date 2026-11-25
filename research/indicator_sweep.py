"""Parameter sweep over the indicators — and an honest in-sample vs out-of-sample split.

Searching many settings and keeping the winner is curve-fitting: on any data some setting looks
great by luck. So each setting is chosen on the FIRST 70% of history and then judged ONLY on the
last 30% it never saw. A setting that wins in-sample and dies out-of-sample was noise.
"""

import numpy as np
import pandas as pd

import instruments as inst
import run_sr_ultra as r
from indicator_winrate import rsi, signals_rsi, signals_ma_cross, signals_bollinger, backtest

MAJORS_GOLD = ["frxEURUSD", "frxGBPUSD", "frxUSDJPY", "frxAUDUSD", "frxUSDCAD", "frxXAUUSD"]
TIMEFRAME = "1h"
SPLIT = 0.70


def net_over(close, opens, sig, rsi_vals, spread, mean_reversion, lo, hi):
    """Pooled net % of trades whose entry bar falls in [lo, hi) of the series."""
    results = []
    n = len(close); free = 60
    for i in range(60, n - 2):
        if i < free or sig[i] == 0 or not (lo <= i < hi):
            continue
        d = int(sig[i]); entry = opens[i + 1] + d * spread
        exit_bar = min(i + 1 + 24, n - 1)
        if mean_reversion and rsi_vals is not None:
            for j in range(i + 1, min(i + 1 + 24, n)):
                if (d > 0 and rsi_vals[j] >= 50) or (d < 0 and rsi_vals[j] <= 50):
                    exit_bar = j; break
        results.append((close[exit_bar] - entry) * d / entry)
        free = exit_bar + 1
    return np.array(results)


def evaluate(make_signal, mean_reversion):
    """Pooled train net and test net for one parameter set, across all markets."""
    train, test = [], []
    for sym in MAJORS_GOLD:
        frame = r.load_cached(sym, TIMEFRAME)
        close = frame["close"].to_numpy(); opens = frame["open"].to_numpy()
        spread = next(i for i in inst.INSTRUMENTS if i["symbol"] == sym).get("spread", 0.0002)
        sig, rsi_vals = make_signal(close)
        cut = int(len(close) * SPLIT)
        train.append(net_over(close, opens, sig, rsi_vals, spread, mean_reversion, 60, cut))
        test.append(net_over(close, opens, sig, rsi_vals, spread, mean_reversion, cut, len(close)))
    tr = np.concatenate(train) if train else np.array([])
    te = np.concatenate(test) if test else np.array([])
    return tr, te


def line(label, tr, te):
    def fmt(a):
        if len(a) == 0:
            return "   n/a"
        return f"{100*a.sum():+7.1f}% ({len(a)}tr, {100*(a>0).mean():.0f}%w)"
    return f"{label:28s} train {fmt(tr):30s}  test {fmt(te)}"


def sweep_rsi():
    print("\n### RSI mean reversion — period / thresholds ###")
    best = None
    for period in (2, 3, 5, 7, 14):
        for lo, hi in ((5, 95), (10, 90), (20, 80), (30, 70)):
            tr, te = evaluate(lambda c, p=period, L=lo, H=hi: signals_rsi(c, p, L, H), True)
            label = f"RSI({period}) {lo}/{hi}"
            print("  " + line(label, tr, te))
            score = 100 * tr.sum() if len(tr) else -1e9
            if best is None or score > best[0]:
                best = (score, label, te)
    print(f"  >> best IN-SAMPLE: {best[1]}  -> OUT-OF-SAMPLE net "
          f"{100*best[2].sum():+.1f}% [{'PROFIT' if best[2].sum()>0 else 'loss'}]")


def sweep_ma():
    print("\n### MA cross (trend) — fast / slow ###")
    best = None
    for fast in (10, 20, 50):
        for slow in (50, 100, 200):
            if fast >= slow:
                continue
            tr, te = evaluate(lambda c, f=fast, s=slow: signals_ma_cross(c, f, s), False)
            label = f"EMA {fast}/{slow}"
            print("  " + line(label, tr, te))
            score = 100 * tr.sum() if len(tr) else -1e9
            if best is None or score > best[0]:
                best = (score, label, te)
    print(f"  >> best IN-SAMPLE: {best[1]}  -> OUT-OF-SAMPLE net "
          f"{100*best[2].sum():+.1f}% [{'PROFIT' if best[2].sum()>0 else 'loss'}]")


def sweep_bollinger():
    print("\n### Bollinger fade — period / width ###")
    best = None
    for period in (10, 20, 50):
        for width in (1.5, 2.0, 2.5, 3.0):
            tr, te = evaluate(lambda c, p=period, w=width: signals_bollinger(c, p, w), False)
            label = f"BB({period}, {width}sd)"
            print("  " + line(label, tr, te))
            score = 100 * tr.sum() if len(tr) else -1e9
            if best is None or score > best[0]:
                best = (score, label, te)
    print(f"  >> best IN-SAMPLE: {best[1]}  -> OUT-OF-SAMPLE net "
          f"{100*best[2].sum():+.1f}% [{'PROFIT' if best[2].sum()>0 else 'loss'}]")


def main():
    print(f"Indicator parameter sweep — majors + gold, {TIMEFRAME}, 70% train / 30% test\n")
    sweep_rsi()
    sweep_bollinger()
    sweep_ma()


if __name__ == "__main__":
    main()
