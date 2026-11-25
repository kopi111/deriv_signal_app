"""Win rate vs profit for classic indicators — the lesson that a high win rate can still lose.

Each strategy is the textbook version. For every one we report the win rate AND the money, because
a strategy can win most of its trades and still bleed: small wins, rare big losses. Costs (the real
spread) are paid on every trade. Returns are the plain percentage move captured, net of spread.

  * RSI(2) mean reversion  — Larry Connors' famous high-win-rate rule.
  * RSI(14) mean reversion — classic oversold/overbought.
  * Bollinger fade         — buy the lower band, sell the upper.
  * MA cross (trend)       — the opposite style, for contrast.
"""

import numpy as np
import pandas as pd

import instruments as inst
import run_sr_ultra as r

MAJORS_GOLD = ["frxEURUSD", "frxGBPUSD", "frxUSDJPY", "frxAUDUSD", "frxUSDCAD", "frxXAUUSD"]
TIMEFRAME = "1h"
MAX_HOLD = 24


def rsi(close, period):
    delta = np.diff(close, prepend=close[0])
    gain = pd.Series(np.where(delta > 0, delta, 0.0)).ewm(alpha=1 / period, adjust=False).mean()
    loss = pd.Series(np.where(delta < 0, -delta, 0.0)).ewm(alpha=1 / period, adjust=False).mean()
    rs = gain / loss.replace(0, np.nan)
    return (100 - 100 / (1 + rs)).to_numpy()


def signals_rsi(close, period, low, high):
    r_ = rsi(close, period)
    return np.where(r_ < low, 1, np.where(r_ > high, -1, 0)), r_


def signals_bollinger(close, period=20, width=2.0):
    s = pd.Series(close)
    mid = s.rolling(period).mean()
    sd = s.rolling(period).std()
    sig = np.where(close < (mid - width * sd), 1, np.where(close > (mid + width * sd), -1, 0))
    return sig, None


def signals_ma_cross(close, fast=20, slow=50):
    s = pd.Series(close)
    f = s.ewm(span=fast, adjust=False).mean()
    g = s.ewm(span=slow, adjust=False).mean()
    cross = np.sign(f - g).to_numpy()
    sig = np.zeros(len(close))
    sig[1:] = np.where((cross[1:] > 0) & (cross[:-1] <= 0), 1,
                       np.where((cross[1:] < 0) & (cross[:-1] >= 0), -1, 0))
    return sig, None


def backtest(close, opens, sig, rsi_vals, spread, mean_reversion):
    """Enter next bar; mean-reversion exits when RSI reverts to 50 or after MAX_HOLD; trend holds MAX_HOLD."""
    results = []
    n = len(close)
    free = 60
    for i in range(60, n - 2):
        if i < free or sig[i] == 0:
            continue
        d = int(sig[i])
        entry = opens[i + 1] + d * spread
        exit_bar = min(i + 1 + MAX_HOLD, n - 1)
        if mean_reversion and rsi_vals is not None:
            for j in range(i + 1, min(i + 1 + MAX_HOLD, n)):
                if (d > 0 and rsi_vals[j] >= 50) or (d < 0 and rsi_vals[j] <= 50):
                    exit_bar = j
                    break
        ret = (close[exit_bar] - entry) * d / entry
        results.append(ret)
        free = exit_bar + 1
    return np.array(results)


def summarize(results, label):
    if len(results) == 0:
        return f"{label:22s}  no trades"
    win = 100 * (results > 0).mean()
    wins = results[results > 0]
    losses = results[results <= 0]
    avg_win = 100 * wins.mean() if len(wins) else 0
    avg_loss = 100 * losses.mean() if len(losses) else 0
    net = 100 * results.sum()
    exp = 100 * results.mean()
    verdict = "PROFIT" if net > 0 else "loss"
    return (f"{label:22s}  trades {len(results):5d}  win {win:5.1f}%  "
            f"avgW {avg_win:+.3f}% avgL {avg_loss:+.3f}%  exp/trade {exp:+.4f}%  net {net:+8.1f}%  [{verdict}]")


def run_strategy(name, make_signal, mean_reversion):
    print(f"\n=== {name} ===")
    pooled = []
    for sym in MAJORS_GOLD:
        frame = r.load_cached(sym, TIMEFRAME)
        close = frame["close"].to_numpy()
        opens = frame["open"].to_numpy()
        sig, rsi_vals = make_signal(close)
        spread = inst.spread_for(r.prepare_bars(frame), None) if False else \
            next(i for i in inst.INSTRUMENTS if i["symbol"] == sym).get("spread", 0.0002)
        results = backtest(close, opens, sig, rsi_vals, spread, mean_reversion)
        pooled.append(results)
        print("  " + summarize(results, sym.replace("frx", "")))
    allr = np.concatenate(pooled) if pooled else np.array([])
    print("  " + summarize(allr, "POOLED"))


def main():
    print(f"Indicator win-rate vs profit — majors + gold, {TIMEFRAME}, spread paid\n")
    run_strategy("RSI(2) mean reversion (<10 / >90)", lambda c: signals_rsi(c, 2, 10, 90), True)
    run_strategy("RSI(14) mean reversion (<30 / >70)", lambda c: signals_rsi(c, 14, 30, 70), True)
    run_strategy("Bollinger fade (20, 2sd)", signals_bollinger, False)
    run_strategy("MA cross (EMA20/50, trend)", signals_ma_cross, False)


if __name__ == "__main__":
    main()
