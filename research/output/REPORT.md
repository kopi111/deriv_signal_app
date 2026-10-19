# Strategy research, 2026-09-18

9 of 1120 market/timeframe/strategy combinations passed every check.

Rules: {'min_trades': 30, 'min_profit_factor': 1.2, 'min_expectancy_r': 0.08, 'min_positive_folds': 4, 'max_random_p': 0.05}

Feed failures: none

| Market | TF | Strategy | OOS trades | PF | Exp R | Total R | Folds + | Random p | Lockbox R | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| Gold / USD | 1h | donchian_breakout | 36 | 1.51 | 0.281 | 10.1 | 5/6 | 0.163 | 4.0 | fail: beats random |
| Gold / USD | 1h | macd_pullback | 30 | 1.34 | 0.191 | 5.7 | 4/6 | 0.307 | -0.0 | fail: beats random |
| Gold / USD | 1h | legacy_rsi_crossback | 101 | 1.08 | 0.021 | 2.1 | 3/6 | 0.203 | -4.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Gold / USD | 1h | trend_pullback | 26 | 0.85 | -0.099 | -2.6 | 3/6 | 1.0 | -1.0 | fail: enough trades, profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Gold / USD | 1h | legacy_ema_cross | 67 | 0.87 | -0.042 | -2.8 | 3/6 | 1.0 | -6.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Gold / USD | 1h | bollinger_reversion | 36 | 0.85 | -0.097 | -3.5 | 2/6 | 1.0 | -0.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Gold / USD | 1h | legacy_macd_cross | 118 | 0.94 | -0.029 | -3.5 | 2/6 | 1.0 | -5.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Gold / USD | 1h | ema_bounce | 84 | 0.89 | -0.074 | -6.2 | 3/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Gold / USD | 1h | rsi2_reversion | 52 | 0.82 | -0.122 | -6.3 | 3/6 | 1.0 | 1.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Gold / USD | 1h | ema_cross | 49 | 0.68 | -0.211 | -10.3 | 1/6 | 1.0 | -0.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Silver / USD | 1h | trend_pullback | 33 | 1.46 | 0.252 | 8.3 | 4/6 | 0.177 | -1.1 | fail: beats random, lockbox not negative |
| Silver / USD | 1h | macd_pullback | 34 | 1.12 | 0.077 | 2.6 | 3/6 | 0.473 | 1.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Silver / USD | 1h | ema_bounce | 77 | 0.98 | -0.01 | -0.8 | 3/6 | 1.0 | -4.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Silver / USD | 1h | legacy_rsi_crossback | 67 | 0.95 | -0.015 | -1.0 | 3/6 | 1.0 | -0.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Silver / USD | 1h | legacy_macd_cross | 114 | 0.98 | -0.008 | -1.0 | 4/6 | 1.0 | 7.0 | fail: profit factor, expectancy, beats random |
| Silver / USD | 1h | rsi2_reversion | 57 | 0.96 | -0.028 | -1.6 | 1/6 | 1.0 | 5.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Silver / USD | 1h | bollinger_reversion | 39 | 0.82 | -0.115 | -4.5 | 3/6 | 1.0 | 7.6 | fail: profit factor, expectancy, consistent folds, beats random |
| Silver / USD | 1h | legacy_ema_cross | 51 | 0.79 | -0.105 | -5.3 | 2/6 | 1.0 | -1.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Silver / USD | 1h | ema_cross | 47 | 0.68 | -0.218 | -10.2 | 3/6 | 1.0 | -8.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Silver / USD | 1h | donchian_breakout | 73 | 0.78 | -0.144 | -10.5 | 3/6 | 1.0 | -3.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 1h | trend_pullback | 48 | 1.07 | 0.042 | 2.0 | 2/6 | 0.42 | -4.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 1h | rsi2_reversion | 51 | 1.04 | 0.023 | 1.2 | 3/6 | 0.403 | 4.0 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / USD | 1h | macd_pullback | 33 | 1.0 | 0.001 | 0.0 | 4/6 | 1.0 | 2.0 | fail: profit factor, expectancy, beats random |
| EUR / USD | 1h | legacy_rsi_crossback | 25 | 0.85 | -0.055 | -1.4 | 1/6 | 1.0 | 0.4 | fail: enough trades, profit factor, expectancy, consistent folds, beats random |
| EUR / USD | 1h | donchian_breakout | 53 | 0.81 | -0.125 | -6.6 | 3/6 | 1.0 | -2.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 1h | bollinger_reversion | 42 | 0.69 | -0.206 | -8.7 | 2/6 | 1.0 | 2.6 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / USD | 1h | legacy_macd_cross | 142 | 0.8 | -0.065 | -9.3 | 1/6 | 1.0 | -0.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 1h | legacy_ema_cross | 76 | 0.7 | -0.141 | -10.7 | 3/6 | 1.0 | -7.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 1h | ema_cross | 50 | 0.6 | -0.278 | -13.9 | 3/6 | 1.0 | -4.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 1h | ema_bounce | 108 | 0.73 | -0.19 | -20.5 | 2/6 | 1.0 | -8.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / USD | 1h | legacy_rsi_crossback | 29 | 1.19 | 0.053 | 1.5 | 4/6 | 0.167 | -1.1 | fail: enough trades, profit factor, expectancy, beats random, lockbox not negative |
| GBP / USD | 1h | macd_pullback | 30 | 0.86 | -0.084 | -2.5 | 2/6 | 1.0 | 1.5 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / USD | 1h | bollinger_reversion | 66 | 0.93 | -0.047 | -3.1 | 2/6 | 1.0 | -2.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / USD | 1h | trend_pullback | 29 | 0.53 | -0.339 | -9.8 | 1/6 | 1.0 | 1.3 | fail: enough trades, profit factor, expectancy, consistent folds, beats random |
| GBP / USD | 1h | legacy_macd_cross | 128 | 0.75 | -0.085 | -10.8 | 0/6 | 1.0 | -12.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / USD | 1h | donchian_breakout | 65 | 0.71 | -0.2 | -13.0 | 2/6 | 1.0 | -7.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / USD | 1h | legacy_ema_cross | 81 | 0.66 | -0.161 | -13.1 | 2/6 | 1.0 | -7.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / USD | 1h | ema_cross | 57 | 0.6 | -0.302 | -17.2 | 1/6 | 1.0 | -0.0 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / USD | 1h | rsi2_reversion | 77 | 0.63 | -0.259 | -19.9 | 0/6 | 1.0 | 5.8 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / USD | 1h | ema_bounce | 80 | 0.52 | -0.363 | -29.0 | 0/6 | 1.0 | -4.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / USD | 1h | macd_pullback | 28 | 1.08 | 0.047 | 1.3 | 3/6 | 0.26 | 3.0 | fail: enough trades, profit factor, expectancy, consistent folds, beats random |
| AUD / USD | 1h | legacy_rsi_crossback | 102 | 0.82 | -0.054 | -5.5 | 3/6 | 1.0 | -0.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / USD | 1h | rsi2_reversion | 51 | 0.81 | -0.115 | -5.9 | 2/6 | 1.0 | 0.5 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / USD | 1h | legacy_ema_cross | 60 | 0.75 | -0.125 | -7.5 | 2/6 | 1.0 | -3.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / USD | 1h | trend_pullback | 28 | 0.52 | -0.357 | -10.0 | 1/6 | 1.0 | 5.5 | fail: enough trades, profit factor, expectancy, consistent folds, beats random |
| AUD / USD | 1h | donchian_breakout | 50 | 0.66 | -0.23 | -11.5 | 1/6 | 1.0 | -3.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / USD | 1h | ema_cross | 57 | 0.65 | -0.244 | -13.9 | 2/6 | 1.0 | 1.0 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / USD | 1h | ema_bounce | 83 | 0.73 | -0.187 | -15.6 | 2/6 | 1.0 | 2.9 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / USD | 1h | legacy_macd_cross | 122 | 0.73 | -0.128 | -15.6 | 3/6 | 1.0 | 4.0 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / USD | 1h | bollinger_reversion | 82 | 0.73 | -0.195 | -16.0 | 2/6 | 1.0 | -5.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / JPY | 1h | ema_bounce | 98 | 1.04 | 0.025 | 2.4 | 2/6 | 0.523 | -2.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / JPY | 1h | rsi2_reversion | 53 | 1.06 | 0.038 | 2.0 | 3/6 | 0.333 | -6.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / JPY | 1h | legacy_ema_cross | 48 | 1.1 | 0.04 | 1.9 | 3/6 | 0.2 | -0.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / JPY | 1h | legacy_rsi_crossback | 83 | 1.01 | 0.003 | 0.3 | 2/6 | 0.127 | 1.5 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / JPY | 1h | macd_pullback | 31 | 0.98 | -0.011 | -0.3 | 4/6 | 1.0 | 2.3 | fail: profit factor, expectancy, beats random |
| USD / JPY | 1h | trend_pullback | 15 | 0.8 | -0.137 | -2.1 | 2/6 | 1.0 | -1.0 | fail: enough trades, profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / JPY | 1h | ema_cross | 55 | 0.83 | -0.11 | -6.0 | 2/6 | 1.0 | 2.4 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / JPY | 1h | donchian_breakout | 38 | 0.76 | -0.171 | -6.5 | 2/6 | 1.0 | 4.7 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / JPY | 1h | legacy_macd_cross | 125 | 0.64 | -0.135 | -16.9 | 1/6 | 1.0 | 2.3 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / JPY | 1h | bollinger_reversion | 45 | 0.3 | -0.573 | -25.8 | 0/6 | 1.0 | -0.0 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / JPY | 1h | legacy_rsi_crossback | 48 | 1.19 | 0.06 | 2.9 | 3/6 | 0.17 | 0.5 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / JPY | 1h | legacy_ema_cross | 66 | 1.1 | 0.041 | 2.7 | 3/6 | 0.173 | 2.2 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / JPY | 1h | ema_cross | 59 | 0.95 | -0.028 | -1.6 | 3/6 | 1.0 | -0.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / JPY | 1h | donchian_breakout | 31 | 0.86 | -0.079 | -2.4 | 2/6 | 1.0 | 6.0 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / JPY | 1h | legacy_macd_cross | 93 | 0.83 | -0.081 | -7.5 | 1/6 | 1.0 | 6.5 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / JPY | 1h | bollinger_reversion | 42 | 0.72 | -0.202 | -8.5 | 2/6 | 1.0 | -6.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / JPY | 1h | trend_pullback | 27 | 0.46 | -0.418 | -11.3 | 2/6 | 1.0 | -2.5 | fail: enough trades, profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / JPY | 1h | rsi2_reversion | 77 | 0.72 | -0.188 | -14.5 | 1/6 | 1.0 | -4.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / JPY | 1h | macd_pullback | 45 | 0.53 | -0.352 | -15.8 | 1/6 | 1.0 | 4.6 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / JPY | 1h | ema_bounce | 84 | 0.61 | -0.286 | -24.0 | 0/6 | 1.0 | 2.6 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / CAD | 1h | ema_bounce | 119 | 1.12 | 0.079 | 9.3 | 3/6 | 0.197 | 8.1 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / CAD | 1h | rsi2_reversion | 76 | 1.19 | 0.105 | 8.0 | 3/6 | 0.163 | -4.2 | fail: profit factor, consistent folds, beats random, lockbox not negative |
| USD / CAD | 1h | legacy_ema_cross | 60 | 1.11 | 0.028 | 1.7 | 2/6 | 0.097 | -0.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CAD | 1h | macd_pullback | 28 | 0.9 | -0.065 | -1.8 | 4/6 | 1.0 | 2.0 | fail: enough trades, profit factor, expectancy, beats random |
| USD / CAD | 1h | donchian_breakout | 51 | 0.9 | -0.064 | -3.3 | 3/6 | 1.0 | 10.4 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / CAD | 1h | trend_pullback | 44 | 0.79 | -0.148 | -6.5 | 1/6 | 1.0 | -0.0 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / CAD | 1h | legacy_rsi_crossback | 76 | 0.66 | -0.133 | -10.1 | 2/6 | 1.0 | -4.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CAD | 1h | ema_cross | 40 | 0.58 | -0.312 | -12.5 | 1/6 | 1.0 | 5.0 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / CAD | 1h | legacy_macd_cross | 113 | 0.63 | -0.161 | -18.2 | 0/6 | 1.0 | -10.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CAD | 1h | bollinger_reversion | 43 | 0.22 | -0.668 | -28.7 | 0/6 | 1.0 | -9.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 1h | ema_cross | 49 | 1.08 | 0.053 | 2.6 | 3/6 | 0.18 | -5.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 1h | legacy_rsi_crossback | 46 | 1.09 | 0.036 | 1.7 | 2/6 | 0.107 | 4.2 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / CHF | 1h | legacy_macd_cross | 145 | 1.03 | 0.011 | 1.6 | 4/6 | 0.043 | -15.1 | fail: profit factor, expectancy, lockbox not negative |
| USD / CHF | 1h | trend_pullback | 25 | 0.74 | -0.18 | -4.5 | 1/6 | 1.0 | -6.3 | fail: enough trades, profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 1h | donchian_breakout | 38 | 0.81 | -0.132 | -5.0 | 3/6 | 1.0 | 2.0 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / CHF | 1h | macd_pullback | 36 | 0.78 | -0.142 | -5.1 | 2/6 | 1.0 | -4.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 1h | rsi2_reversion | 81 | 0.83 | -0.119 | -9.6 | 2/6 | 1.0 | -9.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 1h | legacy_ema_cross | 91 | 0.63 | -0.141 | -12.9 | 0/6 | 1.0 | -2.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 1h | ema_bounce | 80 | 0.72 | -0.194 | -15.5 | 2/6 | 1.0 | -14.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 1h | bollinger_reversion | 52 | 0.46 | -0.424 | -22.0 | 0/6 | 1.0 | 4.4 | fail: profit factor, expectancy, consistent folds, beats random |
| NZD / USD | 1h | legacy_rsi_crossback | 36 | 1.09 | 0.029 | 1.0 | 4/6 | 0.3 | -3.0 | fail: profit factor, expectancy, beats random, lockbox not negative |
| NZD / USD | 1h | donchian_breakout | 43 | 1.02 | 0.013 | 0.6 | 4/6 | 0.36 | -3.0 | fail: profit factor, expectancy, beats random, lockbox not negative |
| NZD / USD | 1h | legacy_ema_cross | 67 | 0.95 | -0.018 | -1.2 | 2/6 | 1.0 | -2.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 1h | bollinger_reversion | 47 | 0.86 | -0.088 | -4.1 | 3/6 | 1.0 | -5.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 1h | rsi2_reversion | 89 | 0.9 | -0.066 | -5.8 | 1/6 | 1.0 | 5.6 | fail: profit factor, expectancy, consistent folds, beats random |
| NZD / USD | 1h | legacy_macd_cross | 134 | 0.81 | -0.061 | -8.2 | 1/6 | 1.0 | -0.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 1h | ema_cross | 53 | 0.77 | -0.158 | -8.4 | 2/6 | 1.0 | -3.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 1h | ema_bounce | 104 | 0.86 | -0.087 | -9.0 | 2/6 | 1.0 | -2.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 1h | macd_pullback | 44 | 0.66 | -0.225 | -9.9 | 3/6 | 1.0 | -3.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 1h | trend_pullback | 33 | 0.49 | -0.372 | -12.3 | 1/6 | 1.0 | 3.0 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / JPY | 1h | bollinger_reversion | 68 | 1.02 | 0.013 | 0.9 | 4/6 | 0.18 | -3.5 | fail: profit factor, expectancy, beats random, lockbox not negative |
| EUR / JPY | 1h | ema_cross | 58 | 1.01 | 0.006 | 0.3 | 2/6 | 0.327 | -5.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / JPY | 1h | trend_pullback | 17 | 0.71 | -0.208 | -3.5 | 3/6 | 1.0 | -2.6 | fail: enough trades, profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / JPY | 1h | legacy_ema_cross | 68 | 0.85 | -0.052 | -3.5 | 3/6 | 1.0 | 4.5 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / JPY | 1h | legacy_rsi_crossback | 87 | 0.79 | -0.068 | -5.9 | 3/6 | 1.0 | -2.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / JPY | 1h | legacy_macd_cross | 103 | 0.83 | -0.081 | -8.4 | 3/6 | 1.0 | 8.8 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / JPY | 1h | macd_pullback | 32 | 0.48 | -0.406 | -13.0 | 1/6 | 1.0 | -2.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / JPY | 1h | rsi2_reversion | 55 | 0.66 | -0.25 | -13.8 | 1/6 | 1.0 | -4.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / JPY | 1h | ema_bounce | 75 | 0.71 | -0.2 | -15.0 | 2/6 | 1.0 | -5.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / JPY | 1h | donchian_breakout | 52 | 0.6 | -0.29 | -15.1 | 1/6 | 1.0 | 7.4 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / JPY | 1h | ema_bounce | 67 | 1.42 | 0.233 | 15.6 | 3/6 | 0.053 | -6.0 | fail: consistent folds, beats random, lockbox not negative |
| AUD / JPY | 1h | macd_pullback | 25 | 1.54 | 0.291 | 7.3 | 4/6 | 0.157 | -5.0 | fail: enough trades, beats random, lockbox not negative |
| AUD / JPY | 1h | donchian_breakout | 56 | 1.1 | 0.064 | 3.6 | 2/6 | 0.333 | 12.1 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / JPY | 1h | ema_cross | 39 | 1.12 | 0.077 | 3.0 | 3/6 | 0.38 | 2.1 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / JPY | 1h | legacy_macd_cross | 129 | 0.88 | -0.036 | -4.6 | 2/6 | 1.0 | -0.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / JPY | 1h | rsi2_reversion | 57 | 0.82 | -0.122 | -6.9 | 3/6 | 1.0 | -7.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / JPY | 1h | legacy_ema_cross | 60 | 0.77 | -0.115 | -6.9 | 3/6 | 1.0 | 1.0 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / JPY | 1h | trend_pullback | 62 | 0.81 | -0.129 | -8.0 | 1/6 | 1.0 | -9.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / JPY | 1h | bollinger_reversion | 47 | 0.72 | -0.19 | -8.9 | 2/6 | 1.0 | -20.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / JPY | 1h | legacy_rsi_crossback | 127 | 0.63 | -0.159 | -20.2 | 1/6 | 1.0 | 1.0 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / GBP | 1h | bollinger_reversion | 62 | 0.91 | -0.056 | -3.5 | 2/6 | 1.0 | 6.3 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / GBP | 1h | trend_pullback | 21 | 0.6 | -0.286 | -6.0 | 3/6 | 1.0 | -1.0 | fail: enough trades, profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 1h | legacy_ema_cross | 66 | 0.74 | -0.131 | -8.7 | 2/6 | 1.0 | 0.6 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / GBP | 1h | legacy_macd_cross | 112 | 0.74 | -0.101 | -11.3 | 3/6 | 1.0 | -3.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 1h | donchian_breakout | 34 | 0.53 | -0.335 | -11.4 | 1/6 | 1.0 | -4.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 1h | macd_pullback | 42 | 0.59 | -0.291 | -12.2 | 2/6 | 1.0 | -11.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 1h | ema_bounce | 67 | 0.73 | -0.19 | -12.7 | 1/6 | 1.0 | -13.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 1h | rsi2_reversion | 50 | 0.58 | -0.3 | -15.0 | 0/6 | 1.0 | -14.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 1h | legacy_rsi_crossback | 82 | 0.56 | -0.23 | -18.8 | 0/6 | 1.0 | 2.7 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / GBP | 1h | ema_cross | 68 | 0.55 | -0.321 | -21.8 | 1/6 | 1.0 | -12.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Bitcoin / USD | 1h | ema_cross | 62 | 1.51 | 0.268 | 16.6 | 4/6 | 0.047 | 14.2 | PASS |
| Bitcoin / USD | 1h | macd_pullback | 38 | 1.06 | 0.041 | 1.6 | 3/6 | 0.403 | 0.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Bitcoin / USD | 1h | bollinger_reversion | 35 | 0.92 | -0.057 | -2.0 | 3/6 | 1.0 | -3.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Bitcoin / USD | 1h | ema_bounce | 95 | 0.96 | -0.025 | -2.4 | 3/6 | 1.0 | 6.3 | fail: profit factor, expectancy, consistent folds, beats random |
| Bitcoin / USD | 1h | donchian_breakout | 81 | 0.86 | -0.088 | -7.1 | 2/6 | 1.0 | -3.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Bitcoin / USD | 1h | trend_pullback | 47 | 0.75 | -0.172 | -8.1 | 1/6 | 1.0 | 0.8 | fail: profit factor, expectancy, consistent folds, beats random |
| Bitcoin / USD | 1h | rsi2_reversion | 76 | 0.82 | -0.115 | -8.8 | 2/6 | 1.0 | 0.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Bitcoin / USD | 1h | legacy_macd_cross | 203 | 0.82 | -0.074 | -15.1 | 2/6 | 1.0 | 6.1 | fail: profit factor, expectancy, consistent folds, beats random |
| Bitcoin / USD | 1h | legacy_ema_cross | 148 | 0.71 | -0.105 | -15.6 | 1/6 | 1.0 | 0.9 | fail: profit factor, expectancy, consistent folds, beats random |
| Bitcoin / USD | 1h | legacy_rsi_crossback | 243 | 0.83 | -0.081 | -19.6 | 3/6 | 1.0 | -3.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 | 1h | rsi2_reversion | 79 | 1.32 | 0.192 | 15.2 | 5/6 | 0.097 | -10.0 | fail: beats random, lockbox not negative |
| Volatility 75 | 1h | legacy_ema_cross | 142 | 1.27 | 0.105 | 14.9 | 4/6 | 0.053 | 7.3 | fail: beats random |
| Volatility 75 | 1h | macd_pullback | 57 | 1.12 | 0.07 | 4.0 | 3/6 | 0.363 | -2.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 | 1h | trend_pullback | 100 | 1.06 | 0.037 | 3.7 | 3/6 | 0.373 | -7.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 | 1h | legacy_macd_cross | 172 | 1.0 | 0.0 | 0.0 | 2/6 | 1.0 | 9.3 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 | 1h | legacy_rsi_crossback | 171 | 0.99 | -0.002 | -0.4 | 3/6 | 1.0 | 4.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 | 1h | ema_bounce | 109 | 0.99 | -0.009 | -1.0 | 2/6 | 1.0 | -11.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 | 1h | ema_cross | 84 | 0.94 | -0.039 | -3.2 | 2/6 | 1.0 | 12.9 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 | 1h | bollinger_reversion | 72 | 0.75 | -0.165 | -11.9 | 1/6 | 1.0 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 | 1h | donchian_breakout | 84 | 0.77 | -0.159 | -13.3 | 2/6 | 1.0 | -17.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 | 1h | bollinger_reversion | 96 | 1.46 | 0.249 | 23.9 | 5/6 | 0.023 | -10.3 | fail: lockbox not negative |
| Volatility 100 | 1h | legacy_rsi_crossback | 136 | 1.11 | 0.042 | 5.7 | 4/6 | 0.307 | 5.9 | fail: profit factor, expectancy, beats random |
| Volatility 100 | 1h | macd_pullback | 54 | 1.14 | 0.079 | 4.3 | 3/6 | 0.307 | -2.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 | 1h | ema_bounce | 199 | 1.03 | 0.018 | 3.5 | 3/6 | 0.283 | -18.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 | 1h | rsi2_reversion | 72 | 1.05 | 0.028 | 2.0 | 2/6 | 0.35 | -9.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 | 1h | legacy_macd_cross | 151 | 1.01 | 0.005 | 0.7 | 3/6 | 0.343 | -1.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 | 1h | trend_pullback | 75 | 0.91 | -0.061 | -4.6 | 2/6 | 1.0 | -9.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 | 1h | ema_cross | 93 | 0.85 | -0.093 | -8.6 | 3/6 | 1.0 | 3.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 100 | 1h | legacy_ema_cross | 132 | 0.8 | -0.09 | -11.9 | 2/6 | 1.0 | -3.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 | 1h | donchian_breakout | 101 | 0.76 | -0.168 | -17.0 | 1/6 | 1.0 | -16.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 (1s) | 1h | bollinger_reversion | 73 | 1.49 | 0.245 | 17.9 | 5/6 | 0.01 | -14.5 | fail: lockbox not negative |
| Volatility 100 (1s) | 1h | ema_cross | 98 | 1.26 | 0.14 | 13.7 | 5/6 | 0.053 | 4.0 | fail: beats random |
| Volatility 100 (1s) | 1h | trend_pullback | 55 | 1.41 | 0.218 | 12.0 | 4/6 | 0.033 | -13.0 | fail: lockbox not negative |
| Volatility 100 (1s) | 1h | legacy_ema_cross | 118 | 1.26 | 0.068 | 8.0 | 5/6 | 0.153 | 3.6 | fail: expectancy, beats random |
| Volatility 100 (1s) | 1h | macd_pullback | 54 | 1.2 | 0.111 | 6.0 | 3/6 | 0.14 | -3.0 | fail: consistent folds, beats random, lockbox not negative |
| Volatility 100 (1s) | 1h | legacy_rsi_crossback | 150 | 0.98 | -0.006 | -0.8 | 2/6 | 1.0 | -6.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 (1s) | 1h | legacy_macd_cross | 170 | 0.91 | -0.033 | -5.6 | 4/6 | 1.0 | -1.0 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 100 (1s) | 1h | rsi2_reversion | 87 | 0.89 | -0.072 | -6.2 | 2/6 | 1.0 | 1.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 100 (1s) | 1h | donchian_breakout | 47 | 0.54 | -0.314 | -14.8 | 1/6 | 1.0 | 1.3 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 100 (1s) | 1h | ema_bounce | 172 | 0.74 | -0.177 | -30.4 | 2/6 | 1.0 | -12.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Step Index | 1h | legacy_ema_cross | 95 | 1.53 | 0.177 | 16.8 | 5/6 | 0.02 | 0.7 | PASS |
| Step Index | 1h | ema_cross | 81 | 1.07 | 0.042 | 3.4 | 5/6 | 0.387 | 7.1 | fail: profit factor, expectancy, beats random |
| Step Index | 1h | donchian_breakout | 83 | 0.85 | -0.096 | -8.0 | 3/6 | 1.0 | 5.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Step Index | 1h | legacy_rsi_crossback | 95 | 0.76 | -0.102 | -9.7 | 2/6 | 1.0 | 4.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Step Index | 1h | ema_bounce | 134 | 0.84 | -0.104 | -14.0 | 3/6 | 1.0 | -5.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Step Index | 1h | trend_pullback | 39 | 0.52 | -0.372 | -14.5 | 1/6 | 1.0 | 2.8 | fail: profit factor, expectancy, consistent folds, beats random |
| Step Index | 1h | macd_pullback | 53 | 0.61 | -0.278 | -14.7 | 0/6 | 1.0 | 4.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Step Index | 1h | legacy_macd_cross | 195 | 0.73 | -0.096 | -18.6 | 0/6 | 1.0 | 9.9 | fail: profit factor, expectancy, consistent folds, beats random |
| Step Index | 1h | rsi2_reversion | 114 | 0.77 | -0.165 | -18.8 | 3/6 | 1.0 | -1.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Step Index | 1h | bollinger_reversion | 111 | 0.72 | -0.199 | -22.1 | 1/6 | 1.0 | 7.7 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 (1s) | 1h | donchian_breakout | 64 | 2.01 | 0.473 | 30.3 | 5/6 | 0.003 | 0.8 | PASS |
| Volatility 75 (1s) | 1h | ema_cross | 83 | 1.17 | 0.098 | 8.1 | 3/6 | 0.173 | 2.8 | fail: profit factor, consistent folds, beats random |
| Volatility 75 (1s) | 1h | bollinger_reversion | 81 | 1.12 | 0.07 | 5.7 | 2/6 | 0.257 | 13.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 (1s) | 1h | legacy_ema_cross | 94 | 1.02 | 0.008 | 0.7 | 2/6 | 0.35 | 0.8 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 (1s) | 1h | rsi2_reversion | 122 | 0.97 | -0.016 | -2.0 | 2/6 | 1.0 | -5.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 (1s) | 1h | ema_bounce | 142 | 0.94 | -0.039 | -5.5 | 2/6 | 1.0 | -6.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 (1s) | 1h | legacy_macd_cross | 228 | 0.81 | -0.059 | -13.5 | 2/6 | 1.0 | -5.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 (1s) | 1h | trend_pullback | 32 | 0.42 | -0.453 | -14.5 | 1/6 | 1.0 | 8.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 (1s) | 1h | legacy_rsi_crossback | 172 | 0.78 | -0.101 | -17.4 | 2/6 | 1.0 | 3.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 (1s) | 1h | macd_pullback | 41 | 0.4 | -0.466 | -19.1 | 1/6 | 1.0 | -5.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 10 | 1h | rsi2_reversion | 149 | 1.35 | 0.208 | 31.0 | 3/6 | 0.023 | 0.1 | fail: consistent folds |
| Jump 10 | 1h | legacy_rsi_crossback | 186 | 1.29 | 0.114 | 21.1 | 5/6 | 0.03 | -12.2 | fail: lockbox not negative |
| Jump 10 | 1h | donchian_breakout | 49 | 1.48 | 0.256 | 12.5 | 5/6 | 0.11 | -1.0 | fail: beats random, lockbox not negative |
| Jump 10 | 1h | ema_bounce | 130 | 0.98 | -0.013 | -1.7 | 3/6 | 1.0 | -9.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 10 | 1h | ema_cross | 69 | 0.85 | -0.099 | -6.8 | 3/6 | 1.0 | 2.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 10 | 1h | legacy_ema_cross | 110 | 0.79 | -0.075 | -8.2 | 2/6 | 1.0 | 1.6 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 10 | 1h | legacy_macd_cross | 160 | 0.84 | -0.068 | -10.9 | 2/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 10 | 1h | trend_pullback | 96 | 0.83 | -0.115 | -11.0 | 1/6 | 1.0 | -3.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 10 | 1h | bollinger_reversion | 81 | 0.79 | -0.136 | -11.0 | 1/6 | 1.0 | -0.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 10 | 1h | macd_pullback | 69 | 0.74 | -0.176 | -12.2 | 2/6 | 1.0 | 1.7 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 25 | 1h | bollinger_reversion | 69 | 1.13 | 0.082 | 5.6 | 3/6 | 0.283 | 10.8 | fail: profit factor, consistent folds, beats random |
| Jump 25 | 1h | ema_cross | 114 | 1.05 | 0.034 | 3.9 | 4/6 | 0.387 | -2.5 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Jump 25 | 1h | legacy_ema_cross | 93 | 1.05 | 0.022 | 2.1 | 3/6 | 0.35 | 0.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 25 | 1h | donchian_breakout | 89 | 1.03 | 0.018 | 1.6 | 2/6 | 0.473 | -7.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 25 | 1h | macd_pullback | 57 | 0.99 | -0.005 | -0.3 | 2/6 | 1.0 | 1.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 25 | 1h | legacy_rsi_crossback | 153 | 0.92 | -0.033 | -5.1 | 2/6 | 1.0 | 1.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 25 | 1h | legacy_macd_cross | 158 | 0.9 | -0.042 | -6.6 | 2/6 | 1.0 | 2.7 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 25 | 1h | ema_bounce | 121 | 0.8 | -0.13 | -15.7 | 2/6 | 1.0 | 0.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 25 | 1h | trend_pullback | 108 | 0.72 | -0.194 | -20.9 | 1/6 | 1.0 | 3.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 25 | 1h | rsi2_reversion | 118 | 0.75 | -0.182 | -21.5 | 2/6 | 1.0 | 7.9 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 50 | 1h | donchian_breakout | 68 | 1.24 | 0.141 | 9.6 | 3/6 | 0.267 | 0.0 | fail: consistent folds, beats random |
| Jump 50 | 1h | rsi2_reversion | 148 | 1.02 | 0.014 | 2.0 | 2/6 | 0.383 | 6.1 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 50 | 1h | ema_cross | 77 | 1.03 | 0.018 | 1.4 | 4/6 | 0.36 | -11.0 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Jump 50 | 1h | ema_bounce | 120 | 1.01 | 0.004 | 0.5 | 3/6 | 0.413 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 50 | 1h | legacy_ema_cross | 94 | 0.98 | -0.008 | -0.8 | 4/6 | 1.0 | 0.5 | fail: profit factor, expectancy, beats random |
| Jump 50 | 1h | macd_pullback | 40 | 0.94 | -0.037 | -1.5 | 3/6 | 1.0 | -0.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 50 | 1h | legacy_rsi_crossback | 93 | 0.93 | -0.033 | -3.1 | 4/6 | 1.0 | -0.3 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Jump 50 | 1h | bollinger_reversion | 75 | 0.9 | -0.066 | -4.9 | 3/6 | 1.0 | -0.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 50 | 1h | legacy_macd_cross | 169 | 0.77 | -0.092 | -15.6 | 2/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 50 | 1h | trend_pullback | 57 | 0.6 | -0.298 | -17.0 | 1/6 | 1.0 | -7.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 75 | 1h | ema_bounce | 124 | 1.11 | 0.065 | 8.0 | 4/6 | 0.22 | 6.2 | fail: profit factor, expectancy, beats random |
| Jump 75 | 1h | ema_cross | 74 | 1.16 | 0.088 | 6.5 | 5/6 | 0.23 | -1.2 | fail: profit factor, beats random, lockbox not negative |
| Jump 75 | 1h | rsi2_reversion | 109 | 1.03 | 0.022 | 2.4 | 2/6 | 0.373 | 6.1 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 75 | 1h | legacy_rsi_crossback | 74 | 0.96 | -0.018 | -1.3 | 3/6 | 1.0 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 75 | 1h | legacy_ema_cross | 108 | 0.92 | -0.039 | -4.2 | 3/6 | 1.0 | -2.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 75 | 1h | donchian_breakout | 84 | 0.92 | -0.056 | -4.7 | 3/6 | 1.0 | 3.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 75 | 1h | legacy_macd_cross | 145 | 0.92 | -0.038 | -5.5 | 3/6 | 1.0 | -6.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 75 | 1h | macd_pullback | 45 | 0.77 | -0.163 | -7.3 | 3/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 75 | 1h | bollinger_reversion | 56 | 0.81 | -0.132 | -7.4 | 3/6 | 1.0 | 2.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 75 | 1h | trend_pullback | 31 | 0.46 | -0.414 | -12.8 | 1/6 | 1.0 | 1.6 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 100 | 1h | legacy_ema_cross | 79 | 1.37 | 0.137 | 10.8 | 4/6 | 0.043 | -3.8 | fail: lockbox not negative |
| Jump 100 | 1h | ema_cross | 74 | 1.14 | 0.084 | 6.2 | 4/6 | 0.27 | -2.3 | fail: profit factor, beats random, lockbox not negative |
| Jump 100 | 1h | donchian_breakout | 88 | 1.07 | 0.04 | 3.5 | 3/6 | 0.367 | 4.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 100 | 1h | ema_bounce | 141 | 1.03 | 0.014 | 2.0 | 4/6 | 0.31 | -15.5 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Jump 100 | 1h | bollinger_reversion | 89 | 0.98 | -0.015 | -1.3 | 3/6 | 1.0 | 11.2 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 100 | 1h | macd_pullback | 46 | 0.78 | -0.143 | -6.6 | 3/6 | 1.0 | -0.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 100 | 1h | rsi2_reversion | 75 | 0.76 | -0.164 | -12.3 | 1/6 | 1.0 | 5.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 100 | 1h | trend_pullback | 59 | 0.55 | -0.312 | -18.4 | 2/6 | 1.0 | -0.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 100 | 1h | legacy_rsi_crossback | 279 | 0.83 | -0.069 | -19.3 | 2/6 | 1.0 | 3.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 100 | 1h | legacy_macd_cross | 213 | 0.72 | -0.103 | -21.9 | 1/6 | 1.0 | -2.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 (1s) | 1h | donchian_breakout | 103 | 1.21 | 0.117 | 12.0 | 5/6 | 0.113 | 15.5 | fail: beats random |
| Volatility 10 (1s) | 1h | ema_bounce | 134 | 1.15 | 0.084 | 11.2 | 4/6 | 0.22 | 7.1 | fail: profit factor, beats random |
| Volatility 10 (1s) | 1h | rsi2_reversion | 113 | 1.14 | 0.081 | 9.1 | 5/6 | 0.177 | 9.0 | fail: profit factor, beats random |
| Volatility 10 (1s) | 1h | ema_cross | 89 | 1.11 | 0.072 | 6.4 | 3/6 | 0.19 | -7.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 (1s) | 1h | legacy_rsi_crossback | 169 | 1.05 | 0.023 | 3.8 | 4/6 | 0.353 | -5.4 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 10 (1s) | 1h | trend_pullback | 24 | 0.96 | -0.027 | -0.6 | 2/6 | 1.0 | 1.7 | fail: enough trades, profit factor, expectancy, consistent folds, beats random |
| Volatility 10 (1s) | 1h | legacy_macd_cross | 144 | 0.94 | -0.025 | -3.7 | 1/6 | 1.0 | -11.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 (1s) | 1h | legacy_ema_cross | 137 | 0.92 | -0.037 | -5.0 | 2/6 | 1.0 | -2.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 (1s) | 1h | macd_pullback | 48 | 0.73 | -0.177 | -8.5 | 2/6 | 1.0 | 2.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 10 (1s) | 1h | bollinger_reversion | 99 | 0.77 | -0.165 | -16.4 | 2/6 | 1.0 | -4.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 15 (1s) | 1h | legacy_ema_cross | 122 | 1.41 | 0.107 | 13.0 | 4/6 | 0.013 | -4.5 | fail: lockbox not negative |
| Volatility 15 (1s) | 1h | ema_cross | 84 | 1.26 | 0.143 | 12.0 | 4/6 | 0.147 | -2.3 | fail: beats random, lockbox not negative |
| Volatility 15 (1s) | 1h | macd_pullback | 45 | 1.15 | 0.089 | 4.0 | 3/6 | 0.29 | -4.0 | fail: profit factor, consistent folds, beats random, lockbox not negative |
| Volatility 15 (1s) | 1h | donchian_breakout | 87 | 1.01 | 0.006 | 0.5 | 2/6 | 0.433 | -2.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 15 (1s) | 1h | legacy_rsi_crossback | 83 | 1.0 | -0.0 | -0.0 | 4/6 | 1.0 | -0.5 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 15 (1s) | 1h | trend_pullback | 33 | 0.75 | -0.167 | -5.5 | 2/6 | 1.0 | 18.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 15 (1s) | 1h | ema_bounce | 98 | 0.84 | -0.104 | -10.2 | 3/6 | 1.0 | 3.8 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 15 (1s) | 1h | legacy_macd_cross | 210 | 0.83 | -0.06 | -12.5 | 2/6 | 1.0 | -8.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 15 (1s) | 1h | rsi2_reversion | 81 | 0.67 | -0.228 | -18.5 | 1/6 | 1.0 | 10.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 15 (1s) | 1h | bollinger_reversion | 96 | 0.67 | -0.225 | -21.6 | 1/6 | 1.0 | 7.6 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 (1s) | 1h | bollinger_reversion | 52 | 2.34 | 0.565 | 29.4 | 4/6 | 0.0 | 1.9 | PASS |
| Volatility 25 (1s) | 1h | legacy_ema_cross | 142 | 1.42 | 0.109 | 15.5 | 4/6 | 0.017 | -3.0 | fail: lockbox not negative |
| Volatility 25 (1s) | 1h | donchian_breakout | 78 | 1.25 | 0.149 | 11.6 | 4/6 | 0.11 | -9.0 | fail: beats random, lockbox not negative |
| Volatility 25 (1s) | 1h | legacy_rsi_crossback | 145 | 1.18 | 0.073 | 10.6 | 4/6 | 0.127 | -1.4 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 25 (1s) | 1h | legacy_macd_cross | 227 | 1.04 | 0.011 | 2.5 | 3/6 | 0.333 | -1.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 (1s) | 1h | trend_pullback | 54 | 0.9 | -0.063 | -3.4 | 3/6 | 1.0 | 3.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 (1s) | 1h | macd_pullback | 61 | 0.8 | -0.128 | -7.8 | 3/6 | 1.0 | 2.1 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 (1s) | 1h | ema_cross | 87 | 0.56 | -0.312 | -27.2 | 1/6 | 1.0 | 6.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 (1s) | 1h | rsi2_reversion | 90 | 0.55 | -0.316 | -28.4 | 1/6 | 1.0 | 5.8 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 (1s) | 1h | ema_bounce | 126 | 0.48 | -0.392 | -49.4 | 0/6 | 1.0 | 2.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 30 (1s) | 1h | rsi2_reversion | 122 | 1.07 | 0.046 | 5.6 | 4/6 | 0.497 | -5.1 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 30 (1s) | 1h | ema_cross | 74 | 1.01 | 0.009 | 0.7 | 3/6 | 0.533 | -5.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 30 (1s) | 1h | legacy_ema_cross | 71 | 0.96 | -0.017 | -1.2 | 3/6 | 1.0 | -1.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 30 (1s) | 1h | donchian_breakout | 68 | 0.96 | -0.026 | -1.8 | 3/6 | 1.0 | 2.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 30 (1s) | 1h | macd_pullback | 54 | 0.79 | -0.15 | -8.1 | 1/6 | 1.0 | 2.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 30 (1s) | 1h | legacy_macd_cross | 198 | 0.83 | -0.056 | -11.1 | 3/6 | 1.0 | -0.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 30 (1s) | 1h | legacy_rsi_crossback | 140 | 0.76 | -0.09 | -12.6 | 2/6 | 1.0 | 6.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 30 (1s) | 1h | trend_pullback | 53 | 0.48 | -0.395 | -20.9 | 0/6 | 1.0 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 30 (1s) | 1h | bollinger_reversion | 104 | 0.65 | -0.237 | -24.7 | 0/6 | 1.0 | 13.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 30 (1s) | 1h | ema_bounce | 125 | 0.62 | -0.279 | -34.9 | 1/6 | 1.0 | -4.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 (1s) | 1h | ema_cross | 67 | 1.48 | 0.243 | 16.3 | 6/6 | 0.063 | -6.5 | fail: beats random, lockbox not negative |
| Volatility 50 (1s) | 1h | macd_pullback | 51 | 1.42 | 0.216 | 11.0 | 3/6 | 0.137 | 3.4 | fail: consistent folds, beats random |
| Volatility 50 (1s) | 1h | ema_bounce | 100 | 1.13 | 0.073 | 7.3 | 2/6 | 0.32 | -11.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 (1s) | 1h | trend_pullback | 64 | 1.17 | 0.103 | 6.6 | 3/6 | 0.32 | 5.0 | fail: profit factor, consistent folds, beats random |
| Volatility 50 (1s) | 1h | rsi2_reversion | 71 | 1.14 | 0.086 | 6.1 | 4/6 | 0.293 | 4.4 | fail: profit factor, beats random |
| Volatility 50 (1s) | 1h | legacy_macd_cross | 152 | 1.1 | 0.036 | 5.5 | 4/6 | 0.233 | 4.0 | fail: profit factor, expectancy, beats random |
| Volatility 50 (1s) | 1h | legacy_ema_cross | 92 | 0.97 | -0.012 | -1.1 | 3/6 | 1.0 | -7.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 (1s) | 1h | bollinger_reversion | 99 | 0.89 | -0.071 | -7.0 | 1/6 | 1.0 | -3.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 (1s) | 1h | legacy_rsi_crossback | 104 | 0.84 | -0.073 | -7.6 | 2/6 | 1.0 | 2.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 50 (1s) | 1h | donchian_breakout | 85 | 0.71 | -0.21 | -17.8 | 2/6 | 1.0 | -7.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 90 (1s) | 1h | legacy_macd_cross | 174 | 1.42 | 0.097 | 16.9 | 4/6 | 0.037 | 2.3 | PASS |
| Volatility 90 (1s) | 1h | rsi2_reversion | 137 | 1.1 | 0.064 | 8.8 | 4/6 | 0.173 | 11.3 | fail: profit factor, expectancy, beats random |
| Volatility 90 (1s) | 1h | bollinger_reversion | 95 | 1.11 | 0.071 | 6.8 | 4/6 | 0.13 | 3.7 | fail: profit factor, expectancy, beats random |
| Volatility 90 (1s) | 1h | macd_pullback | 48 | 1.21 | 0.112 | 5.4 | 3/6 | 0.163 | -7.5 | fail: consistent folds, beats random, lockbox not negative |
| Volatility 90 (1s) | 1h | ema_bounce | 153 | 1.02 | 0.01 | 1.6 | 3/6 | 0.377 | -4.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 90 (1s) | 1h | legacy_rsi_crossback | 56 | 0.79 | -0.09 | -5.0 | 3/6 | 1.0 | 3.9 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 90 (1s) | 1h | ema_cross | 79 | 0.9 | -0.07 | -5.5 | 3/6 | 1.0 | -8.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 90 (1s) | 1h | legacy_ema_cross | 112 | 0.83 | -0.084 | -9.4 | 2/6 | 1.0 | -9.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 90 (1s) | 1h | donchian_breakout | 67 | 0.66 | -0.247 | -16.5 | 1/6 | 1.0 | -5.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 90 (1s) | 1h | trend_pullback | 88 | 0.72 | -0.198 | -17.4 | 2/6 | 1.0 | -4.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 150 (1s) | 1h | trend_pullback | 63 | 1.54 | 0.299 | 18.8 | 4/6 | 0.03 | 7.4 | PASS |
| Volatility 150 (1s) | 1h | legacy_rsi_crossback | 282 | 1.16 | 0.066 | 18.6 | 5/6 | 0.067 | -9.9 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 150 (1s) | 1h | rsi2_reversion | 82 | 1.23 | 0.128 | 10.5 | 4/6 | 0.12 | -4.5 | fail: beats random, lockbox not negative |
| Volatility 150 (1s) | 1h | bollinger_reversion | 68 | 1.28 | 0.155 | 10.5 | 4/6 | 0.127 | 5.0 | fail: beats random |
| Volatility 150 (1s) | 1h | macd_pullback | 54 | 1.26 | 0.144 | 7.8 | 2/6 | 0.147 | -9.1 | fail: consistent folds, beats random, lockbox not negative |
| Volatility 150 (1s) | 1h | legacy_macd_cross | 141 | 1.05 | 0.021 | 3.0 | 3/6 | 0.337 | 0.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 150 (1s) | 1h | ema_bounce | 120 | 1.01 | 0.005 | 0.6 | 4/6 | 0.343 | -1.2 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 150 (1s) | 1h | donchian_breakout | 90 | 0.94 | -0.039 | -3.5 | 3/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 150 (1s) | 1h | ema_cross | 85 | 0.86 | -0.085 | -7.2 | 2/6 | 1.0 | -20.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 150 (1s) | 1h | legacy_ema_cross | 115 | 0.59 | -0.204 | -23.5 | 2/6 | 1.0 | 2.6 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 250 (1s) | 1h | trend_pullback | 43 | 1.04 | 0.024 | 1.1 | 3/6 | 0.253 | -9.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 1h | macd_pullback | 52 | 1.02 | 0.012 | 0.6 | 3/6 | 0.323 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 1h | bollinger_reversion | 83 | 0.99 | -0.005 | -0.4 | 3/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 1h | donchian_breakout | 67 | 0.73 | -0.178 | -12.0 | 2/6 | 1.0 | 0.7 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 250 (1s) | 1h | legacy_ema_cross | 109 | 0.71 | -0.117 | -12.7 | 2/6 | 1.0 | -15.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 1h | legacy_rsi_crossback | 107 | 0.63 | -0.16 | -17.1 | 2/6 | 1.0 | 0.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 250 (1s) | 1h | ema_bounce | 136 | 0.8 | -0.127 | -17.3 | 2/6 | 1.0 | -18.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 1h | ema_cross | 84 | 0.67 | -0.232 | -19.5 | 1/6 | 1.0 | -3.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 1h | legacy_macd_cross | 210 | 0.71 | -0.098 | -20.7 | 0/6 | 1.0 | -1.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 1h | rsi2_reversion | 85 | 0.63 | -0.255 | -21.7 | 1/6 | 1.0 | -11.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 | 1h | ema_bounce | 94 | 1.33 | 0.191 | 17.9 | 3/6 | 0.097 | -2.7 | fail: consistent folds, beats random, lockbox not negative |
| Volatility 10 | 1h | trend_pullback | 86 | 1.29 | 0.168 | 14.4 | 3/6 | 0.153 | 7.6 | fail: consistent folds, beats random |
| Volatility 10 | 1h | rsi2_reversion | 136 | 1.14 | 0.086 | 11.6 | 3/6 | 0.29 | 4.0 | fail: profit factor, consistent folds, beats random |
| Volatility 10 | 1h | legacy_rsi_crossback | 16 | 7.5 | 0.406 | 6.5 | 5/6 | 0.007 | -1.0 | fail: enough trades, lockbox not negative |
| Volatility 10 | 1h | ema_cross | 72 | 1.07 | 0.044 | 3.2 | 3/6 | 0.343 | -6.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 | 1h | macd_pullback | 52 | 1.07 | 0.044 | 2.3 | 3/6 | 0.363 | 1.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 10 | 1h | donchian_breakout | 84 | 0.95 | -0.032 | -2.7 | 4/6 | 1.0 | -1.5 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 10 | 1h | bollinger_reversion | 85 | 0.9 | -0.064 | -5.5 | 2/6 | 1.0 | -8.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 | 1h | legacy_ema_cross | 115 | 0.88 | -0.06 | -6.9 | 2/6 | 1.0 | -9.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 | 1h | legacy_macd_cross | 194 | 0.83 | -0.07 | -13.5 | 2/6 | 1.0 | -12.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 | 1h | bollinger_reversion | 47 | 1.27 | 0.159 | 7.5 | 4/6 | 0.16 | 1.9 | fail: beats random |
| Volatility 25 | 1h | ema_bounce | 162 | 1.06 | 0.036 | 5.9 | 4/6 | 0.363 | -13.9 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 25 | 1h | donchian_breakout | 92 | 1.02 | 0.011 | 1.0 | 3/6 | 0.527 | -4.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 | 1h | macd_pullback | 56 | 1.0 | -0.003 | -0.2 | 2/6 | 1.0 | -5.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 | 1h | trend_pullback | 94 | 0.94 | -0.037 | -3.5 | 2/6 | 1.0 | -7.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 | 1h | legacy_rsi_crossback | 84 | 0.72 | -0.124 | -10.4 | 3/6 | 1.0 | 0.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 | 1h | ema_cross | 99 | 0.84 | -0.111 | -11.0 | 1/6 | 1.0 | -7.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 | 1h | legacy_macd_cross | 199 | 0.88 | -0.057 | -11.3 | 2/6 | 1.0 | 3.3 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 | 1h | legacy_ema_cross | 133 | 0.8 | -0.1 | -13.3 | 2/6 | 1.0 | -6.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 | 1h | rsi2_reversion | 100 | 0.7 | -0.207 | -20.7 | 2/6 | 1.0 | -9.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 | 1h | legacy_rsi_crossback | 52 | 1.16 | 0.065 | 3.4 | 3/6 | 0.253 | 1.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 50 | 1h | bollinger_reversion | 112 | 0.93 | -0.045 | -5.0 | 4/6 | 1.0 | 5.1 | fail: profit factor, expectancy, beats random |
| Volatility 50 | 1h | macd_pullback | 46 | 0.78 | -0.153 | -7.0 | 2/6 | 1.0 | -1.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 | 1h | ema_bounce | 106 | 0.89 | -0.072 | -7.7 | 3/6 | 1.0 | -5.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 | 1h | trend_pullback | 83 | 0.83 | -0.114 | -9.5 | 2/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 | 1h | legacy_macd_cross | 196 | 0.88 | -0.052 | -10.3 | 2/6 | 1.0 | -7.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 | 1h | donchian_breakout | 60 | 0.73 | -0.177 | -10.6 | 2/6 | 1.0 | -10.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 | 1h | ema_cross | 72 | 0.78 | -0.15 | -10.8 | 3/6 | 1.0 | -4.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 | 1h | rsi2_reversion | 102 | 0.82 | -0.118 | -12.1 | 2/6 | 1.0 | 4.3 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 50 | 1h | legacy_ema_cross | 128 | 0.62 | -0.168 | -21.5 | 0/6 | 1.0 | 3.6 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / AUD | 1h | trend_pullback | 65 | 1.38 | 0.21 | 13.7 | 4/6 | 0.023 | -0.0 | PASS |
| EUR / AUD | 1h | macd_pullback | 44 | 1.13 | 0.08 | 3.5 | 3/6 | 0.143 | -3.5 | fail: profit factor, consistent folds, beats random, lockbox not negative |
| EUR / AUD | 1h | bollinger_reversion | 47 | 1.1 | 0.063 | 3.0 | 3/6 | 0.127 | -1.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / AUD | 1h | ema_bounce | 73 | 1.05 | 0.03 | 2.2 | 3/6 | 0.203 | -5.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / AUD | 1h | legacy_rsi_crossback | 33 | 0.8 | -0.096 | -3.2 | 2/6 | 1.0 | 0.9 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / AUD | 1h | legacy_ema_cross | 93 | 0.86 | -0.043 | -4.0 | 2/6 | 1.0 | -2.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / AUD | 1h | legacy_macd_cross | 123 | 0.84 | -0.067 | -8.3 | 3/6 | 1.0 | -6.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / AUD | 1h | donchian_breakout | 37 | 0.68 | -0.227 | -8.4 | 2/6 | 1.0 | 0.0 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / AUD | 1h | ema_cross | 54 | 0.69 | -0.203 | -11.0 | 2/6 | 1.0 | 6.0 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / AUD | 1h | rsi2_reversion | 67 | 0.74 | -0.165 | -11.1 | 3/6 | 1.0 | -7.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 1h | trend_pullback | 30 | 1.27 | 0.152 | 4.6 | 3/6 | 0.117 | -8.0 | fail: consistent folds, beats random, lockbox not negative |
| EUR / CAD | 1h | legacy_rsi_crossback | 18 | 1.79 | 0.227 | 4.1 | 4/6 | 0.063 | 2.3 | fail: enough trades, beats random |
| EUR / CAD | 1h | rsi2_reversion | 55 | 1.01 | 0.009 | 0.5 | 3/6 | 0.14 | -11.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 1h | macd_pullback | 35 | 0.69 | -0.206 | -7.2 | 1/6 | 1.0 | -5.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 1h | legacy_ema_cross | 86 | 0.72 | -0.097 | -8.3 | 3/6 | 1.0 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 1h | ema_cross | 49 | 0.71 | -0.195 | -9.5 | 3/6 | 1.0 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 1h | legacy_macd_cross | 124 | 0.78 | -0.077 | -9.5 | 2/6 | 1.0 | -0.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 1h | bollinger_reversion | 54 | 0.69 | -0.213 | -11.5 | 2/6 | 1.0 | 4.0 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / CAD | 1h | donchian_breakout | 51 | 0.64 | -0.251 | -12.8 | 1/6 | 1.0 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 1h | ema_bounce | 139 | 0.69 | -0.214 | -29.8 | 1/6 | 1.0 | -19.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 1h | macd_pullback | 29 | 1.22 | 0.121 | 3.5 | 3/6 | 0.037 | 1.5 | fail: enough trades, consistent folds |
| EUR / CHF | 1h | legacy_ema_cross | 65 | 1.07 | 0.029 | 1.9 | 4/6 | 0.097 | -5.2 | fail: profit factor, expectancy, beats random, lockbox not negative |
| EUR / CHF | 1h | trend_pullback | 34 | 0.99 | -0.006 | -0.2 | 2/6 | 1.0 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 1h | ema_bounce | 68 | 0.95 | -0.034 | -2.3 | 1/6 | 1.0 | 4.0 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / CHF | 1h | donchian_breakout | 51 | 0.91 | -0.061 | -3.1 | 3/6 | 1.0 | -1.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 1h | rsi2_reversion | 85 | 0.9 | -0.065 | -5.5 | 2/6 | 1.0 | 7.8 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / CHF | 1h | ema_cross | 46 | 0.79 | -0.139 | -6.4 | 1/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 1h | legacy_rsi_crossback | 53 | 0.65 | -0.157 | -8.3 | 1/6 | 1.0 | -0.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 1h | legacy_macd_cross | 124 | 0.69 | -0.129 | -16.1 | 2/6 | 1.0 | -6.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 1h | bollinger_reversion | 53 | 0.54 | -0.346 | -18.3 | 1/6 | 1.0 | -6.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 1h | rsi2_reversion | 48 | 1.16 | 0.097 | 4.7 | 2/6 | 0.09 | -3.0 | fail: profit factor, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 1h | macd_pullback | 32 | 1.03 | 0.016 | 0.5 | 1/6 | 0.19 | 2.1 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / NZD | 1h | trend_pullback | 37 | 1.01 | 0.005 | 0.2 | 3/6 | 0.183 | 3.2 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / NZD | 1h | legacy_macd_cross | 118 | 0.94 | -0.018 | -2.1 | 2/6 | 1.0 | -3.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 1h | donchian_breakout | 32 | 0.85 | -0.092 | -2.9 | 2/6 | 1.0 | -11.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 1h | legacy_rsi_crossback | 35 | 0.69 | -0.133 | -4.7 | 3/6 | 1.0 | 0.6 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / NZD | 1h | ema_bounce | 96 | 0.89 | -0.067 | -6.4 | 1/6 | 1.0 | -3.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 1h | legacy_ema_cross | 67 | 0.73 | -0.101 | -6.8 | 0/6 | 1.0 | -4.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 1h | ema_cross | 49 | 0.73 | -0.189 | -9.3 | 3/6 | 1.0 | -0.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 1h | bollinger_reversion | 74 | 0.58 | -0.305 | -22.6 | 0/6 | 1.0 | -0.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 1h | ema_bounce | 67 | 1.2 | 0.114 | 7.6 | 2/6 | 0.14 | -4.0 | fail: consistent folds, beats random, lockbox not negative |
| GBP / AUD | 1h | trend_pullback | 26 | 1.1 | 0.058 | 1.5 | 3/6 | 0.237 | -2.0 | fail: enough trades, profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 1h | legacy_rsi_crossback | 45 | 1.04 | 0.018 | 0.8 | 3/6 | 0.17 | -4.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 1h | macd_pullback | 36 | 1.01 | 0.007 | 0.2 | 2/6 | 0.3 | -2.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 1h | ema_cross | 46 | 0.95 | -0.033 | -1.5 | 2/6 | 1.0 | 3.6 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / AUD | 1h | legacy_ema_cross | 53 | 0.87 | -0.044 | -2.3 | 3/6 | 1.0 | 0.0 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / AUD | 1h | rsi2_reversion | 47 | 0.87 | -0.075 | -3.5 | 1/6 | 1.0 | -8.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 1h | bollinger_reversion | 52 | 0.87 | -0.09 | -4.7 | 2/6 | 1.0 | 1.0 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / AUD | 1h | legacy_macd_cross | 118 | 0.82 | -0.062 | -7.3 | 1/6 | 1.0 | -3.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 1h | donchian_breakout | 43 | 0.73 | -0.178 | -7.7 | 1/6 | 1.0 | -2.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 1h | ema_bounce | 67 | 1.19 | 0.106 | 7.1 | 3/6 | 0.09 | -4.2 | fail: profit factor, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 1h | legacy_rsi_crossback | 89 | 1.09 | 0.038 | 3.4 | 2/6 | 0.117 | -0.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 1h | legacy_ema_cross | 60 | 0.95 | -0.02 | -1.2 | 2/6 | 1.0 | -5.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 1h | legacy_macd_cross | 100 | 0.9 | -0.047 | -4.7 | 3/6 | 1.0 | 0.6 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / CAD | 1h | bollinger_reversion | 57 | 0.82 | -0.127 | -7.2 | 3/6 | 1.0 | 0.3 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / CAD | 1h | macd_pullback | 35 | 0.71 | -0.206 | -7.2 | 2/6 | 1.0 | -1.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 1h | ema_cross | 48 | 0.67 | -0.22 | -10.6 | 2/6 | 1.0 | -3.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 1h | donchian_breakout | 39 | 0.45 | -0.436 | -17.0 | 0/6 | 1.0 | -4.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 1h | trend_pullback | 36 | 0.25 | -0.667 | -24.0 | 1/6 | 1.0 | -0.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 1h | rsi2_reversion | 57 | 0.36 | -0.502 | -28.6 | 0/6 | 1.0 | -9.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 1h | macd_pullback | 37 | 0.94 | -0.035 | -1.3 | 3/6 | 1.0 | -12.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 1h | trend_pullback | 27 | 0.81 | -0.13 | -3.5 | 2/6 | 1.0 | -4.1 | fail: enough trades, profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 1h | legacy_rsi_crossback | 102 | 0.87 | -0.052 | -5.3 | 3/6 | 1.0 | 5.3 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / CHF | 1h | bollinger_reversion | 64 | 0.87 | -0.086 | -5.5 | 2/6 | 1.0 | -4.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 1h | ema_cross | 55 | 0.8 | -0.141 | -7.7 | 2/6 | 1.0 | -8.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 1h | ema_bounce | 71 | 0.79 | -0.135 | -9.6 | 2/6 | 1.0 | -14.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 1h | donchian_breakout | 42 | 0.53 | -0.355 | -14.9 | 1/6 | 1.0 | -3.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 1h | legacy_macd_cross | 116 | 0.66 | -0.13 | -15.1 | 2/6 | 1.0 | -2.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 1h | legacy_ema_cross | 71 | 0.53 | -0.253 | -18.0 | 1/6 | 1.0 | -1.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 1h | rsi2_reversion | 49 | 0.44 | -0.425 | -20.8 | 0/6 | 1.0 | -7.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 1h | trend_pullback | 39 | 1.34 | 0.199 | 7.8 | 4/6 | 0.087 | 3.6 | fail: beats random |
| GBP / NZD | 1h | donchian_breakout | 44 | 1.04 | 0.023 | 1.0 | 2/6 | 0.207 | -5.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 1h | legacy_macd_cross | 122 | 1.0 | -0.001 | -0.1 | 3/6 | 1.0 | -4.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 1h | ema_bounce | 80 | 0.98 | -0.016 | -1.3 | 4/6 | 1.0 | 1.9 | fail: profit factor, expectancy, beats random |
| GBP / NZD | 1h | macd_pullback | 39 | 0.85 | -0.102 | -4.0 | 2/6 | 1.0 | 2.8 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / NZD | 1h | legacy_rsi_crossback | 52 | 0.8 | -0.078 | -4.0 | 3/6 | 1.0 | -0.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 1h | rsi2_reversion | 62 | 0.89 | -0.076 | -4.7 | 2/6 | 1.0 | 0.0 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / NZD | 1h | bollinger_reversion | 53 | 0.86 | -0.096 | -5.1 | 3/6 | 1.0 | -1.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 1h | legacy_ema_cross | 68 | 0.75 | -0.109 | -7.4 | 3/6 | 1.0 | -5.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 1h | ema_cross | 74 | 0.61 | -0.276 | -20.4 | 0/6 | 1.0 | -7.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 1h | macd_pullback | 30 | 1.24 | 0.138 | 4.1 | 3/6 | 0.157 | -5.7 | fail: consistent folds, beats random, lockbox not negative |
| AUD / CAD | 1h | legacy_rsi_crossback | 55 | 0.88 | -0.041 | -2.2 | 2/6 | 1.0 | 2.6 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / CAD | 1h | bollinger_reversion | 71 | 0.92 | -0.048 | -3.4 | 2/6 | 1.0 | 0.0 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / CAD | 1h | legacy_ema_cross | 80 | 0.83 | -0.067 | -5.4 | 4/6 | 1.0 | -0.9 | fail: profit factor, expectancy, beats random, lockbox not negative |
| AUD / CAD | 1h | trend_pullback | 29 | 0.63 | -0.267 | -7.7 | 3/6 | 1.0 | -5.8 | fail: enough trades, profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 1h | ema_cross | 55 | 0.7 | -0.202 | -11.1 | 3/6 | 1.0 | 1.2 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / CAD | 1h | legacy_macd_cross | 130 | 0.76 | -0.125 | -16.3 | 2/6 | 1.0 | -11.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 1h | rsi2_reversion | 48 | 0.53 | -0.362 | -17.4 | 2/6 | 1.0 | -13.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 1h | ema_bounce | 91 | 0.7 | -0.197 | -17.9 | 2/6 | 1.0 | -13.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 1h | donchian_breakout | 56 | 0.46 | -0.431 | -24.2 | 1/6 | 1.0 | -3.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 1h | ema_bounce | 62 | 1.01 | 0.005 | 0.3 | 3/6 | 0.063 | 2.0 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / CHF | 1h | macd_pullback | 26 | 1.0 | -0.0 | -0.0 | 1/6 | 1.0 | 4.9 | fail: enough trades, profit factor, expectancy, consistent folds, beats random |
| AUD / CHF | 1h | legacy_rsi_crossback | 48 | 0.98 | -0.007 | -0.3 | 2/6 | 1.0 | -1.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 1h | ema_cross | 64 | 0.95 | -0.032 | -2.0 | 3/6 | 1.0 | 0.1 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / CHF | 1h | trend_pullback | 29 | 0.82 | -0.114 | -3.3 | 2/6 | 1.0 | -0.5 | fail: enough trades, profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 1h | legacy_macd_cross | 112 | 0.86 | -0.052 | -5.8 | 2/6 | 1.0 | -7.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 1h | bollinger_reversion | 41 | 0.67 | -0.243 | -10.0 | 1/6 | 1.0 | -3.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 1h | rsi2_reversion | 59 | 0.62 | -0.273 | -16.1 | 1/6 | 1.0 | -2.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 1h | donchian_breakout | 43 | 0.46 | -0.413 | -17.8 | 0/6 | 1.0 | -0.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 1h | legacy_ema_cross | 88 | 0.53 | -0.214 | -18.8 | 0/6 | 1.0 | -4.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 1h | ema_cross | 56 | 1.11 | 0.065 | 3.6 | 3/6 | 0.113 | 2.3 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / NZD | 1h | bollinger_reversion | 50 | 0.98 | -0.01 | -0.5 | 3/6 | 1.0 | -3.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 1h | donchian_breakout | 69 | 0.88 | -0.08 | -5.5 | 3/6 | 1.0 | -5.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 1h | legacy_ema_cross | 80 | 0.74 | -0.103 | -8.2 | 3/6 | 1.0 | 3.0 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / NZD | 1h | macd_pullback | 33 | 0.54 | -0.348 | -11.5 | 2/6 | 1.0 | 0.0 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / NZD | 1h | ema_bounce | 75 | 0.71 | -0.192 | -14.4 | 3/6 | 1.0 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 1h | rsi2_reversion | 56 | 0.52 | -0.358 | -20.0 | 1/6 | 1.0 | -5.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 1h | legacy_rsi_crossback | 85 | 0.57 | -0.243 | -20.7 | 2/6 | 1.0 | -1.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 1h | legacy_macd_cross | 128 | 0.63 | -0.169 | -21.7 | 0/6 | 1.0 | -8.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 1h | trend_pullback | 47 | 0.36 | -0.521 | -24.5 | 1/6 | 1.0 | 4.5 | fail: profit factor, expectancy, consistent folds, beats random |
| NZD / JPY | 1h | ema_bounce | 69 | 1.21 | 0.122 | 8.4 | 4/6 | 0.05 | -11.0 | fail: lockbox not negative |
| NZD / JPY | 1h | donchian_breakout | 46 | 1.17 | 0.109 | 5.0 | 4/6 | 0.093 | 0.4 | fail: profit factor, beats random |
| NZD / JPY | 1h | legacy_rsi_crossback | 52 | 0.86 | -0.057 | -3.0 | 3/6 | 1.0 | 1.5 | fail: profit factor, expectancy, consistent folds, beats random |
| NZD / JPY | 1h | bollinger_reversion | 44 | 0.89 | -0.076 | -3.3 | 2/6 | 1.0 | -5.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 1h | macd_pullback | 25 | 0.75 | -0.183 | -4.6 | 1/6 | 1.0 | -3.0 | fail: enough trades, profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 1h | trend_pullback | 42 | 0.75 | -0.161 | -6.8 | 3/6 | 1.0 | -10.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 1h | rsi2_reversion | 73 | 0.85 | -0.103 | -7.5 | 1/6 | 1.0 | -0.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 1h | legacy_macd_cross | 111 | 0.68 | -0.127 | -14.1 | 0/6 | 1.0 | -1.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 1h | ema_cross | 46 | 0.57 | -0.327 | -15.1 | 1/6 | 1.0 | 4.5 | fail: profit factor, expectancy, consistent folds, beats random |
| NZD / JPY | 1h | legacy_ema_cross | 69 | 0.57 | -0.22 | -15.2 | 0/6 | 1.0 | -5.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CAD / JPY | 1h | macd_pullback | 34 | 1.78 | 0.412 | 14.0 | 5/6 | 0.0 | -4.0 | fail: lockbox not negative |
| CAD / JPY | 1h | legacy_macd_cross | 112 | 1.16 | 0.04 | 4.5 | 4/6 | 0.02 | -2.1 | fail: profit factor, expectancy, lockbox not negative |
| CAD / JPY | 1h | legacy_rsi_crossback | 40 | 1.37 | 0.075 | 3.0 | 3/6 | 0.05 | 0.7 | fail: expectancy, consistent folds |
| CAD / JPY | 1h | rsi2_reversion | 55 | 1.07 | 0.047 | 2.6 | 3/6 | 0.22 | -7.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CAD / JPY | 1h | legacy_ema_cross | 81 | 0.92 | -0.036 | -2.9 | 2/6 | 1.0 | 0.7 | fail: profit factor, expectancy, consistent folds, beats random |
| CAD / JPY | 1h | ema_cross | 54 | 0.82 | -0.118 | -6.4 | 2/6 | 1.0 | 7.3 | fail: profit factor, expectancy, consistent folds, beats random |
| CAD / JPY | 1h | bollinger_reversion | 44 | 0.65 | -0.257 | -11.3 | 1/6 | 1.0 | -3.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CAD / JPY | 1h | trend_pullback | 64 | 0.74 | -0.181 | -11.6 | 2/6 | 1.0 | -7.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CAD / JPY | 1h | ema_bounce | 94 | 0.74 | -0.18 | -16.9 | 1/6 | 1.0 | -1.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CAD / JPY | 1h | donchian_breakout | 40 | 0.44 | -0.433 | -17.3 | 0/6 | 1.0 | -3.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 1h | ema_cross | 53 | 1.01 | 0.009 | 0.5 | 3/6 | 0.27 | -5.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 1h | legacy_rsi_crossback | 102 | 0.96 | -0.015 | -1.5 | 2/6 | 1.0 | -0.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 1h | legacy_macd_cross | 100 | 0.96 | -0.019 | -1.9 | 2/6 | 1.0 | 0.3 | fail: profit factor, expectancy, consistent folds, beats random |
| CHF / JPY | 1h | legacy_ema_cross | 76 | 0.85 | -0.059 | -4.5 | 3/6 | 1.0 | -3.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 1h | donchian_breakout | 44 | 0.73 | -0.183 | -8.0 | 2/6 | 1.0 | 1.4 | fail: profit factor, expectancy, consistent folds, beats random |
| CHF / JPY | 1h | rsi2_reversion | 80 | 0.74 | -0.166 | -13.3 | 3/6 | 1.0 | 3.3 | fail: profit factor, expectancy, consistent folds, beats random |
| CHF / JPY | 1h | ema_bounce | 89 | 0.77 | -0.155 | -13.8 | 1/6 | 1.0 | 10.8 | fail: profit factor, expectancy, consistent folds, beats random |
| CHF / JPY | 1h | macd_pullback | 38 | 0.44 | -0.427 | -16.2 | 1/6 | 1.0 | -4.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 1h | bollinger_reversion | 51 | 0.53 | -0.33 | -16.8 | 2/6 | 1.0 | -3.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 1h | trend_pullback | 43 | 0.36 | -0.518 | -22.3 | 1/6 | 1.0 | 0.5 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / SEK | 1h | macd_pullback | 31 | 0.78 | -0.151 | -4.7 | 2/6 | 1.0 | -7.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 1h | bollinger_reversion | 54 | 0.63 | -0.259 | -14.0 | 1/6 | 1.0 | -4.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 1h | legacy_rsi_crossback | 40 | 0.37 | -0.355 | -14.2 | 0/6 | 1.0 | -2.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 1h | legacy_macd_cross | 101 | 0.65 | -0.187 | -18.9 | 2/6 | 1.0 | 0.8 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / SEK | 1h | legacy_ema_cross | 70 | 0.45 | -0.29 | -20.3 | 0/6 | 1.0 | -2.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 1h | donchian_breakout | 47 | 0.42 | -0.47 | -22.1 | 1/6 | 1.0 | -4.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 1h | ema_cross | 56 | 0.49 | -0.396 | -22.2 | 0/6 | 1.0 | -11.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 1h | trend_pullback | 36 | 0.27 | -0.625 | -22.5 | 0/6 | 1.0 | -3.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 1h | rsi2_reversion | 57 | 0.32 | -0.561 | -32.0 | 0/6 | 1.0 | 0.5 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / SEK | 1h | ema_bounce | 82 | 0.37 | -0.504 | -41.4 | 1/6 | 1.0 | -8.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 1h | legacy_rsi_crossback | 43 | 0.74 | -0.099 | -4.3 | 3/6 | 1.0 | 1.1 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / MXN | 1h | macd_pullback | 41 | 0.74 | -0.183 | -7.5 | 2/6 | 1.0 | -2.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 1h | legacy_ema_cross | 101 | 0.78 | -0.082 | -8.3 | 2/6 | 1.0 | -7.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 1h | donchian_breakout | 41 | 0.7 | -0.209 | -8.6 | 1/6 | 1.0 | -3.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 1h | trend_pullback | 40 | 0.56 | -0.316 | -12.6 | 2/6 | 1.0 | -5.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 1h | bollinger_reversion | 51 | 0.64 | -0.255 | -13.0 | 2/6 | 1.0 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 1h | legacy_macd_cross | 110 | 0.65 | -0.128 | -14.0 | 2/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 1h | ema_cross | 59 | 0.6 | -0.287 | -16.9 | 1/6 | 1.0 | -10.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 1h | ema_bounce | 68 | 0.63 | -0.26 | -17.7 | 2/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 1h | rsi2_reversion | 81 | 0.63 | -0.266 | -21.6 | 1/6 | 1.0 | -3.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 1h | macd_pullback | 23 | 1.53 | 0.252 | 5.8 | 5/6 | 0.09 | 3.4 | fail: enough trades, beats random |
| USD / SEK | 1h | legacy_rsi_crossback | 37 | 0.71 | -0.133 | -4.9 | 2/6 | 1.0 | -4.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 1h | trend_pullback | 34 | 0.6 | -0.282 | -9.6 | 1/6 | 1.0 | -5.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 1h | bollinger_reversion | 55 | 0.72 | -0.191 | -10.5 | 1/6 | 1.0 | -8.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 1h | legacy_macd_cross | 132 | 0.74 | -0.087 | -11.5 | 2/6 | 1.0 | 3.6 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / SEK | 1h | ema_cross | 67 | 0.7 | -0.215 | -14.4 | 2/6 | 1.0 | -0.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 1h | donchian_breakout | 57 | 0.53 | -0.36 | -20.5 | 1/6 | 1.0 | -5.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 1h | ema_bounce | 96 | 0.68 | -0.24 | -23.1 | 2/6 | 1.0 | -5.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 1h | legacy_ema_cross | 92 | 0.46 | -0.275 | -25.3 | 1/6 | 1.0 | -7.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 1h | rsi2_reversion | 52 | 0.31 | -0.596 | -31.0 | 0/6 | 1.0 | -4.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 1h | legacy_macd_cross | 133 | 0.96 | -0.012 | -1.7 | 3/6 | 1.0 | -8.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 1h | macd_pullback | 31 | 0.83 | -0.113 | -3.5 | 2/6 | 1.0 | -3.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 1h | donchian_breakout | 32 | 0.8 | -0.138 | -4.4 | 1/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 1h | legacy_ema_cross | 103 | 0.81 | -0.061 | -6.3 | 1/6 | 1.0 | -3.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 1h | bollinger_reversion | 64 | 0.84 | -0.103 | -6.6 | 2/6 | 1.0 | -1.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 1h | trend_pullback | 18 | 0.43 | -0.444 | -8.0 | 1/6 | 1.0 | -2.5 | fail: enough trades, profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 1h | rsi2_reversion | 53 | 0.77 | -0.16 | -8.5 | 1/6 | 1.0 | 7.3 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / NOK | 1h | ema_bounce | 98 | 0.72 | -0.187 | -18.3 | 2/6 | 1.0 | -7.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 1h | legacy_rsi_crossback | 91 | 0.61 | -0.201 | -18.3 | 1/6 | 1.0 | -3.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 1h | ema_cross | 59 | 0.44 | -0.438 | -25.9 | 0/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 1h | trend_pullback | 22 | 0.47 | -0.383 | -8.4 | 2/6 | 1.0 | -3.0 | fail: enough trades, profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 1h | legacy_rsi_crossback | 30 | 0.37 | -0.313 | -9.4 | 2/6 | 1.0 | -5.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 1h | donchian_breakout | 44 | 0.68 | -0.219 | -9.7 | 1/6 | 1.0 | -3.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 1h | rsi2_reversion | 53 | 0.56 | -0.336 | -17.8 | 1/6 | 1.0 | -7.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 1h | macd_pullback | 35 | 0.31 | -0.571 | -20.0 | 1/6 | 1.0 | -10.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 1h | bollinger_reversion | 58 | 0.53 | -0.359 | -20.8 | 1/6 | 1.0 | -9.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 1h | legacy_ema_cross | 79 | 0.32 | -0.389 | -30.7 | 1/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 1h | legacy_macd_cross | 105 | 0.46 | -0.319 | -33.5 | 0/6 | 1.0 | -4.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 1h | ema_cross | 78 | 0.3 | -0.573 | -44.7 | 0/6 | 1.0 | -3.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 1h | ema_bounce | 99 | 0.4 | -0.474 | -46.9 | 0/6 | 1.0 | -14.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 1h | legacy_rsi_crossback | 27 | 1.21 | 0.082 | 2.2 | 4/6 | 0.203 | -1.8 | fail: enough trades, beats random, lockbox not negative |
| Platinum / USD | 1h | bollinger_reversion | 39 | 1.02 | 0.013 | 0.5 | 2/6 | 0.307 | 4.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Platinum / USD | 1h | legacy_ema_cross | 67 | 0.95 | -0.021 | -1.4 | 2/6 | 1.0 | -4.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 1h | ema_cross | 54 | 0.96 | -0.029 | -1.6 | 2/6 | 1.0 | 3.9 | fail: profit factor, expectancy, consistent folds, beats random |
| Platinum / USD | 1h | macd_pullback | 35 | 0.91 | -0.061 | -2.1 | 2/6 | 1.0 | -0.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 1h | rsi2_reversion | 45 | 0.83 | -0.108 | -4.9 | 2/6 | 1.0 | 3.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Platinum / USD | 1h | legacy_macd_cross | 116 | 0.88 | -0.05 | -5.8 | 3/6 | 1.0 | -0.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 1h | ema_bounce | 67 | 0.84 | -0.107 | -7.2 | 3/6 | 1.0 | -4.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 1h | donchian_breakout | 42 | 0.67 | -0.226 | -9.5 | 1/6 | 1.0 | -1.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 1h | trend_pullback | 44 | 0.69 | -0.224 | -9.8 | 2/6 | 1.0 | -5.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 1h | legacy_rsi_crossback | 52 | 1.42 | 0.107 | 5.6 | 5/6 | 0.023 | -1.0 | fail: lockbox not negative |
| Palladium / USD | 1h | bollinger_reversion | 62 | 1.06 | 0.038 | 2.4 | 3/6 | 0.057 | 7.1 | fail: profit factor, expectancy, consistent folds, beats random |
| Palladium / USD | 1h | donchian_breakout | 52 | 1.03 | 0.016 | 0.8 | 3/6 | 0.127 | -4.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 1h | legacy_macd_cross | 84 | 0.95 | -0.023 | -1.9 | 3/6 | 1.0 | 11.2 | fail: profit factor, expectancy, consistent folds, beats random |
| Palladium / USD | 1h | legacy_ema_cross | 67 | 0.79 | -0.071 | -4.7 | 2/6 | 1.0 | -1.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 1h | macd_pullback | 46 | 0.76 | -0.163 | -7.5 | 3/6 | 1.0 | -1.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 1h | rsi2_reversion | 43 | 0.72 | -0.192 | -8.2 | 1/6 | 1.0 | -9.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 1h | ema_cross | 57 | 0.74 | -0.165 | -9.4 | 3/6 | 1.0 | 0.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Palladium / USD | 1h | trend_pullback | 39 | 0.42 | -0.433 | -16.9 | 1/6 | 1.0 | 0.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Palladium / USD | 1h | ema_bounce | 87 | 0.54 | -0.357 | -31.1 | 1/6 | 1.0 | -9.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Gold / USD | 15m | ema_cross | 182 | 0.97 | -0.018 | -3.3 | 1/6 | 1.0 | 2.8 | fail: profit factor, expectancy, consistent folds, beats random |
| Gold / USD | 15m | legacy_rsi_crossback | 161 | 0.93 | -0.031 | -5.0 | 3/6 | 1.0 | 1.7 | fail: profit factor, expectancy, consistent folds, beats random |
| Gold / USD | 15m | rsi2_reversion | 286 | 0.93 | -0.043 | -12.2 | 4/6 | 1.0 | 2.7 | fail: profit factor, expectancy, beats random |
| Gold / USD | 15m | donchian_breakout | 192 | 0.89 | -0.07 | -13.4 | 3/6 | 1.0 | -3.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Gold / USD | 15m | legacy_macd_cross | 483 | 0.91 | -0.031 | -15.1 | 2/6 | 1.0 | 9.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Gold / USD | 15m | legacy_ema_cross | 271 | 0.72 | -0.117 | -31.6 | 0/6 | 1.0 | 6.7 | fail: profit factor, expectancy, consistent folds, beats random |
| Gold / USD | 15m | macd_pullback | 162 | 0.69 | -0.229 | -37.0 | 0/6 | 1.0 | 8.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Gold / USD | 15m | ema_bounce | 394 | 0.86 | -0.094 | -37.2 | 1/6 | 1.0 | -4.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Gold / USD | 15m | bollinger_reversion | 202 | 0.72 | -0.19 | -38.3 | 1/6 | 1.0 | 3.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Gold / USD | 15m | trend_pullback | 182 | 0.67 | -0.224 | -40.8 | 1/6 | 1.0 | 8.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Silver / USD | 15m | donchian_breakout | 171 | 1.15 | 0.082 | 14.0 | 5/6 | 0.113 | -6.4 | fail: profit factor, beats random, lockbox not negative |
| Silver / USD | 15m | ema_bounce | 260 | 0.98 | -0.015 | -3.9 | 3/6 | 1.0 | -20.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Silver / USD | 15m | macd_pullback | 132 | 0.92 | -0.056 | -7.4 | 1/6 | 1.0 | -6.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Silver / USD | 15m | rsi2_reversion | 234 | 0.93 | -0.046 | -10.8 | 4/6 | 1.0 | -15.1 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Silver / USD | 15m | ema_cross | 193 | 0.89 | -0.07 | -13.5 | 3/6 | 1.0 | -1.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Silver / USD | 15m | legacy_rsi_crossback | 206 | 0.76 | -0.078 | -16.0 | 1/6 | 1.0 | 0.3 | fail: profit factor, expectancy, consistent folds, beats random |
| Silver / USD | 15m | bollinger_reversion | 131 | 0.8 | -0.132 | -17.3 | 1/6 | 1.0 | -4.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Silver / USD | 15m | trend_pullback | 217 | 0.84 | -0.108 | -23.4 | 2/6 | 1.0 | -5.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Silver / USD | 15m | legacy_ema_cross | 303 | 0.73 | -0.096 | -29.0 | 1/6 | 1.0 | 2.1 | fail: profit factor, expectancy, consistent folds, beats random |
| Silver / USD | 15m | legacy_macd_cross | 459 | 0.7 | -0.12 | -55.1 | 0/6 | 1.0 | -7.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 15m | ema_cross | 186 | 1.01 | 0.004 | 0.7 | 4/6 | 0.027 | -22.9 | fail: profit factor, expectancy, lockbox not negative |
| EUR / USD | 15m | rsi2_reversion | 197 | 0.93 | -0.041 | -8.1 | 4/6 | 1.0 | -11.0 | fail: profit factor, expectancy, beats random, lockbox not negative |
| EUR / USD | 15m | legacy_rsi_crossback | 107 | 0.74 | -0.114 | -12.2 | 2/6 | 1.0 | -1.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 15m | trend_pullback | 91 | 0.61 | -0.271 | -24.7 | 1/6 | 1.0 | -12.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 15m | bollinger_reversion | 181 | 0.77 | -0.146 | -26.4 | 1/6 | 1.0 | -21.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 15m | legacy_macd_cross | 468 | 0.82 | -0.067 | -31.3 | 2/6 | 1.0 | -27.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 15m | macd_pullback | 152 | 0.68 | -0.225 | -34.2 | 0/6 | 1.0 | -17.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 15m | legacy_ema_cross | 364 | 0.66 | -0.137 | -50.0 | 0/6 | 1.0 | -8.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 15m | donchian_breakout | 178 | 0.59 | -0.289 | -51.4 | 0/6 | 1.0 | -9.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / USD | 15m | ema_bounce | 369 | 0.76 | -0.162 | -59.8 | 0/6 | 1.0 | -13.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / USD | 15m | donchian_breakout | 158 | 1.19 | 0.105 | 16.6 | 4/6 | 0.007 | -18.1 | fail: profit factor, lockbox not negative |
| GBP / USD | 15m | ema_cross | 232 | 0.9 | -0.061 | -14.1 | 3/6 | 1.0 | -23.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / USD | 15m | legacy_rsi_crossback | 314 | 0.81 | -0.082 | -25.7 | 1/6 | 1.0 | -3.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / USD | 15m | legacy_ema_cross | 298 | 0.75 | -0.091 | -27.1 | 0/6 | 1.0 | -13.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / USD | 15m | bollinger_reversion | 181 | 0.7 | -0.207 | -37.5 | 0/6 | 1.0 | -11.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / USD | 15m | legacy_macd_cross | 509 | 0.75 | -0.08 | -40.6 | 1/6 | 1.0 | -5.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / USD | 15m | trend_pullback | 111 | 0.48 | -0.383 | -42.5 | 1/6 | 1.0 | 9.2 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / USD | 15m | ema_bounce | 317 | 0.7 | -0.2 | -63.4 | 0/6 | 1.0 | -12.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / USD | 15m | macd_pullback | 185 | 0.53 | -0.347 | -64.1 | 0/6 | 1.0 | -13.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / USD | 15m | rsi2_reversion | 314 | 0.64 | -0.245 | -76.8 | 1/6 | 1.0 | 9.8 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / USD | 15m | legacy_rsi_crossback | 159 | 0.92 | -0.026 | -4.1 | 2/6 | 1.0 | -3.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / USD | 15m | trend_pullback | 88 | 0.87 | -0.084 | -7.4 | 3/6 | 1.0 | -4.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / USD | 15m | macd_pullback | 164 | 0.79 | -0.139 | -22.8 | 2/6 | 1.0 | -12.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / USD | 15m | donchian_breakout | 191 | 0.8 | -0.127 | -24.3 | 2/6 | 1.0 | 0.3 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / USD | 15m | legacy_ema_cross | 282 | 0.72 | -0.106 | -29.8 | 1/6 | 1.0 | -18.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / USD | 15m | bollinger_reversion | 291 | 0.85 | -0.104 | -30.3 | 0/6 | 1.0 | -10.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / USD | 15m | ema_cross | 195 | 0.76 | -0.16 | -31.2 | 2/6 | 1.0 | -4.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / USD | 15m | rsi2_reversion | 207 | 0.75 | -0.161 | -33.4 | 0/6 | 1.0 | -7.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / USD | 15m | ema_bounce | 313 | 0.77 | -0.158 | -49.5 | 1/6 | 1.0 | -22.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / USD | 15m | legacy_macd_cross | 501 | 0.68 | -0.118 | -59.3 | 1/6 | 1.0 | -16.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / JPY | 15m | trend_pullback | 91 | 0.95 | -0.03 | -2.7 | 3/6 | 1.0 | -2.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / JPY | 15m | macd_pullback | 172 | 0.89 | -0.068 | -11.7 | 2/6 | 1.0 | -0.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / JPY | 15m | legacy_macd_cross | 387 | 0.93 | -0.032 | -12.2 | 3/6 | 1.0 | 6.2 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / JPY | 15m | legacy_rsi_crossback | 334 | 0.87 | -0.045 | -15.0 | 1/6 | 1.0 | -12.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / JPY | 15m | bollinger_reversion | 236 | 0.84 | -0.105 | -24.9 | 1/6 | 1.0 | -18.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / JPY | 15m | legacy_ema_cross | 273 | 0.79 | -0.101 | -27.7 | 0/6 | 1.0 | 0.1 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / JPY | 15m | ema_bounce | 267 | 0.83 | -0.11 | -29.4 | 2/6 | 1.0 | -13.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / JPY | 15m | rsi2_reversion | 220 | 0.79 | -0.135 | -29.6 | 0/6 | 1.0 | 1.8 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / JPY | 15m | ema_cross | 237 | 0.7 | -0.203 | -48.2 | 1/6 | 1.0 | -7.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / JPY | 15m | donchian_breakout | 193 | 0.56 | -0.32 | -61.7 | 0/6 | 1.0 | 10.0 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / JPY | 15m | bollinger_reversion | 219 | 1.0 | -0.002 | -0.3 | 2/6 | 1.0 | -0.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / JPY | 15m | legacy_rsi_crossback | 121 | 0.76 | -0.108 | -13.1 | 2/6 | 1.0 | -5.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / JPY | 15m | legacy_ema_cross | 249 | 0.82 | -0.068 | -16.9 | 3/6 | 1.0 | -11.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / JPY | 15m | ema_cross | 201 | 0.82 | -0.11 | -22.1 | 2/6 | 1.0 | 2.0 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / JPY | 15m | donchian_breakout | 177 | 0.81 | -0.127 | -22.5 | 1/6 | 1.0 | 15.3 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / JPY | 15m | trend_pullback | 156 | 0.77 | -0.152 | -23.8 | 1/6 | 1.0 | -6.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / JPY | 15m | legacy_macd_cross | 392 | 0.86 | -0.064 | -25.3 | 2/6 | 1.0 | -14.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / JPY | 15m | macd_pullback | 144 | 0.73 | -0.187 | -27.0 | 1/6 | 1.0 | -15.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / JPY | 15m | rsi2_reversion | 222 | 0.66 | -0.23 | -51.1 | 2/6 | 1.0 | -7.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / JPY | 15m | ema_bounce | 381 | 0.6 | -0.282 | -107.6 | 0/6 | 1.0 | -12.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CAD | 15m | rsi2_reversion | 299 | 1.03 | 0.019 | 5.6 | 4/6 | 0.01 | 3.3 | fail: profit factor, expectancy |
| USD / CAD | 15m | trend_pullback | 89 | 1.09 | 0.053 | 4.7 | 3/6 | 0.043 | 0.8 | fail: profit factor, expectancy, consistent folds |
| USD / CAD | 15m | legacy_rsi_crossback | 119 | 0.67 | -0.169 | -20.1 | 1/6 | 1.0 | -11.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CAD | 15m | macd_pullback | 148 | 0.61 | -0.267 | -39.5 | 0/6 | 1.0 | 3.2 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / CAD | 15m | ema_bounce | 349 | 0.81 | -0.123 | -43.0 | 0/6 | 1.0 | -17.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CAD | 15m | ema_cross | 209 | 0.63 | -0.254 | -53.0 | 0/6 | 1.0 | -4.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CAD | 15m | legacy_macd_cross | 414 | 0.72 | -0.139 | -57.5 | 1/6 | 1.0 | -11.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CAD | 15m | bollinger_reversion | 215 | 0.62 | -0.268 | -57.7 | 0/6 | 1.0 | -6.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CAD | 15m | donchian_breakout | 177 | 0.55 | -0.34 | -60.1 | 0/6 | 1.0 | -10.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CAD | 15m | legacy_ema_cross | 358 | 0.55 | -0.175 | -62.7 | 0/6 | 1.0 | -14.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 15m | bollinger_reversion | 169 | 0.86 | -0.086 | -14.6 | 2/6 | 1.0 | -29.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 15m | legacy_rsi_crossback | 161 | 0.75 | -0.123 | -19.8 | 2/6 | 1.0 | 1.4 | fail: profit factor, expectancy, consistent folds, beats random |
| USD / CHF | 15m | trend_pullback | 92 | 0.65 | -0.255 | -23.5 | 1/6 | 1.0 | -11.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 15m | legacy_ema_cross | 269 | 0.78 | -0.106 | -28.6 | 2/6 | 1.0 | -13.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 15m | ema_cross | 233 | 0.8 | -0.128 | -29.8 | 1/6 | 1.0 | -22.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 15m | donchian_breakout | 184 | 0.75 | -0.168 | -31.0 | 1/6 | 1.0 | -18.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 15m | rsi2_reversion | 215 | 0.75 | -0.171 | -36.7 | 2/6 | 1.0 | -9.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 15m | macd_pullback | 161 | 0.6 | -0.279 | -45.0 | 0/6 | 1.0 | -1.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 15m | ema_bounce | 288 | 0.68 | -0.221 | -63.8 | 0/6 | 1.0 | -16.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / CHF | 15m | legacy_macd_cross | 402 | 0.65 | -0.178 | -71.6 | 1/6 | 1.0 | -19.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 15m | trend_pullback | 102 | 0.72 | -0.195 | -19.9 | 1/6 | 1.0 | -18.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 15m | legacy_rsi_crossback | 111 | 0.53 | -0.23 | -25.5 | 1/6 | 1.0 | -7.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 15m | legacy_ema_cross | 283 | 0.78 | -0.105 | -29.8 | 1/6 | 1.0 | -13.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 15m | bollinger_reversion | 152 | 0.71 | -0.2 | -30.4 | 1/6 | 1.0 | -3.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 15m | ema_cross | 193 | 0.75 | -0.163 | -31.5 | 2/6 | 1.0 | -26.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 15m | macd_pullback | 152 | 0.61 | -0.266 | -40.4 | 0/6 | 1.0 | -15.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 15m | donchian_breakout | 206 | 0.66 | -0.237 | -48.9 | 1/6 | 1.0 | -17.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 15m | ema_bounce | 298 | 0.7 | -0.213 | -63.3 | 0/6 | 1.0 | -47.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 15m | legacy_macd_cross | 451 | 0.7 | -0.142 | -64.2 | 1/6 | 1.0 | -16.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / USD | 15m | rsi2_reversion | 245 | 0.56 | -0.308 | -75.4 | 0/6 | 1.0 | -28.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / JPY | 15m | legacy_macd_cross | 383 | 1.02 | 0.007 | 2.7 | 2/6 | 0.01 | -16.4 | fail: profit factor, expectancy, consistent folds, lockbox not negative |
| EUR / JPY | 15m | trend_pullback | 83 | 0.94 | -0.04 | -3.3 | 2/6 | 1.0 | -6.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / JPY | 15m | legacy_ema_cross | 298 | 0.95 | -0.025 | -7.4 | 3/6 | 1.0 | -32.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / JPY | 15m | macd_pullback | 156 | 0.8 | -0.128 | -19.9 | 1/6 | 1.0 | -18.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / JPY | 15m | legacy_rsi_crossback | 179 | 0.73 | -0.14 | -25.1 | 1/6 | 1.0 | -5.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / JPY | 15m | bollinger_reversion | 217 | 0.82 | -0.118 | -25.6 | 2/6 | 1.0 | 2.4 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / JPY | 15m | ema_cross | 235 | 0.79 | -0.137 | -32.2 | 2/6 | 1.0 | -18.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / JPY | 15m | donchian_breakout | 175 | 0.71 | -0.194 | -34.0 | 1/6 | 1.0 | 2.9 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / JPY | 15m | rsi2_reversion | 191 | 0.64 | -0.249 | -47.5 | 0/6 | 1.0 | -5.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / JPY | 15m | ema_bounce | 275 | 0.62 | -0.264 | -72.6 | 0/6 | 1.0 | -20.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / JPY | 15m | donchian_breakout | 199 | 0.96 | -0.022 | -4.3 | 4/6 | 1.0 | 0.1 | fail: profit factor, expectancy, beats random |
| AUD / JPY | 15m | trend_pullback | 87 | 0.75 | -0.17 | -14.8 | 2/6 | 1.0 | -3.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / JPY | 15m | legacy_ema_cross | 261 | 0.81 | -0.064 | -16.8 | 1/6 | 1.0 | -23.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / JPY | 15m | rsi2_reversion | 202 | 0.85 | -0.096 | -19.3 | 2/6 | 1.0 | 7.1 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / JPY | 15m | legacy_rsi_crossback | 269 | 0.82 | -0.083 | -22.4 | 2/6 | 1.0 | -6.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / JPY | 15m | ema_cross | 213 | 0.84 | -0.107 | -22.7 | 2/6 | 1.0 | -23.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / JPY | 15m | macd_pullback | 137 | 0.75 | -0.17 | -23.2 | 3/6 | 1.0 | 1.8 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / JPY | 15m | bollinger_reversion | 245 | 0.83 | -0.114 | -27.9 | 2/6 | 1.0 | -10.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / JPY | 15m | legacy_macd_cross | 388 | 0.83 | -0.079 | -30.6 | 2/6 | 1.0 | -1.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / JPY | 15m | ema_bounce | 373 | 0.85 | -0.099 | -37.1 | 1/6 | 1.0 | 2.9 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / GBP | 15m | legacy_rsi_crossback | 111 | 0.74 | -0.105 | -11.7 | 0/6 | 1.0 | 2.0 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / GBP | 15m | trend_pullback | 79 | 0.57 | -0.298 | -23.6 | 1/6 | 1.0 | -17.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 15m | legacy_ema_cross | 282 | 0.6 | -0.205 | -57.7 | 1/6 | 1.0 | -20.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 15m | donchian_breakout | 149 | 0.41 | -0.46 | -68.5 | 0/6 | 1.0 | -44.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 15m | rsi2_reversion | 223 | 0.53 | -0.34 | -75.7 | 0/6 | 1.0 | -21.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 15m | macd_pullback | 159 | 0.34 | -0.53 | -84.3 | 0/6 | 1.0 | -24.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 15m | bollinger_reversion | 202 | 0.4 | -0.459 | -92.8 | 0/6 | 1.0 | -38.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 15m | legacy_macd_cross | 441 | 0.52 | -0.218 | -96.1 | 0/6 | 1.0 | -41.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 15m | ema_cross | 236 | 0.43 | -0.421 | -99.4 | 0/6 | 1.0 | -34.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / GBP | 15m | ema_bounce | 370 | 0.41 | -0.443 | -163.8 | 0/6 | 1.0 | -64.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Bitcoin / USD | 15m | rsi2_reversion | 421 | 1.08 | 0.047 | 19.6 | 4/6 | 0.013 | -14.8 | fail: profit factor, expectancy, lockbox not negative |
| Bitcoin / USD | 15m | trend_pullback | 113 | 0.78 | -0.136 | -15.3 | 1/6 | 1.0 | 1.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Bitcoin / USD | 15m | legacy_rsi_crossback | 133 | 0.6 | -0.163 | -21.6 | 1/6 | 1.0 | -10.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Bitcoin / USD | 15m | ema_cross | 286 | 0.83 | -0.107 | -30.6 | 1/6 | 1.0 | -7.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Bitcoin / USD | 15m | bollinger_reversion | 208 | 0.77 | -0.149 | -31.0 | 2/6 | 1.0 | -0.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Bitcoin / USD | 15m | donchian_breakout | 326 | 0.84 | -0.099 | -32.3 | 1/6 | 1.0 | -22.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Bitcoin / USD | 15m | macd_pullback | 190 | 0.74 | -0.179 | -34.1 | 1/6 | 1.0 | -27.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Bitcoin / USD | 15m | ema_bounce | 520 | 0.86 | -0.09 | -47.0 | 0/6 | 1.0 | -41.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Bitcoin / USD | 15m | legacy_macd_cross | 642 | 0.78 | -0.087 | -55.6 | 0/6 | 1.0 | -7.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Bitcoin / USD | 15m | legacy_ema_cross | 398 | 0.66 | -0.15 | -59.6 | 0/6 | 1.0 | -17.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 | 15m | donchian_breakout | 303 | 1.02 | 0.01 | 3.0 | 3/6 | 0.44 | 14.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 | 15m | trend_pullback | 114 | 0.98 | -0.013 | -1.5 | 3/6 | 1.0 | -10.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 | 15m | legacy_rsi_crossback | 94 | 0.9 | -0.049 | -4.6 | 3/6 | 1.0 | -2.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 | 15m | ema_cross | 312 | 0.96 | -0.023 | -7.3 | 3/6 | 1.0 | 4.6 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 | 15m | legacy_macd_cross | 888 | 0.94 | -0.018 | -16.3 | 2/6 | 1.0 | -15.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 | 15m | bollinger_reversion | 320 | 0.92 | -0.051 | -16.4 | 3/6 | 1.0 | -8.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 | 15m | rsi2_reversion | 537 | 0.93 | -0.042 | -22.4 | 2/6 | 1.0 | -16.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 | 15m | ema_bounce | 539 | 0.93 | -0.043 | -23.4 | 2/6 | 1.0 | -13.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 | 15m | macd_pullback | 261 | 0.84 | -0.105 | -27.5 | 1/6 | 1.0 | -12.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 | 15m | legacy_ema_cross | 465 | 0.7 | -0.122 | -56.5 | 0/6 | 1.0 | 9.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 100 | 15m | rsi2_reversion | 333 | 0.98 | -0.013 | -4.3 | 3/6 | 1.0 | 2.9 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 100 | 15m | ema_cross | 303 | 0.96 | -0.027 | -8.3 | 3/6 | 1.0 | 9.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 100 | 15m | legacy_rsi_crossback | 456 | 0.95 | -0.024 | -10.8 | 1/6 | 1.0 | -3.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 | 15m | legacy_macd_cross | 721 | 0.95 | -0.015 | -11.0 | 3/6 | 1.0 | -18.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 | 15m | donchian_breakout | 339 | 0.92 | -0.056 | -19.1 | 2/6 | 1.0 | -5.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 | 15m | macd_pullback | 173 | 0.77 | -0.148 | -25.6 | 1/6 | 1.0 | -2.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 | 15m | ema_bounce | 528 | 0.89 | -0.073 | -38.4 | 1/6 | 1.0 | 4.7 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 100 | 15m | trend_pullback | 293 | 0.79 | -0.144 | -42.2 | 1/6 | 1.0 | 4.9 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 100 | 15m | legacy_ema_cross | 581 | 0.8 | -0.078 | -45.4 | 1/6 | 1.0 | -5.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 | 15m | bollinger_reversion | 320 | 0.77 | -0.159 | -50.8 | 0/6 | 1.0 | 15.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 100 (1s) | 15m | bollinger_reversion | 473 | 1.18 | 0.109 | 51.5 | 5/6 | 0.007 | -5.2 | fail: profit factor, lockbox not negative |
| Volatility 100 (1s) | 15m | legacy_macd_cross | 813 | 1.13 | 0.052 | 42.2 | 5/6 | 0.023 | -15.1 | fail: profit factor, expectancy, lockbox not negative |
| Volatility 100 (1s) | 15m | legacy_rsi_crossback | 88 | 1.33 | 0.115 | 10.2 | 4/6 | 0.07 | -0.7 | fail: beats random, lockbox not negative |
| Volatility 100 (1s) | 15m | donchian_breakout | 238 | 1.04 | 0.024 | 5.8 | 3/6 | 0.217 | -9.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 (1s) | 15m | ema_cross | 303 | 0.97 | -0.02 | -6.2 | 3/6 | 1.0 | 7.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 100 (1s) | 15m | ema_bounce | 391 | 0.91 | -0.056 | -21.8 | 3/6 | 1.0 | -17.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 (1s) | 15m | legacy_ema_cross | 541 | 0.88 | -0.045 | -24.2 | 2/6 | 1.0 | -0.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 (1s) | 15m | macd_pullback | 225 | 0.8 | -0.132 | -29.6 | 1/6 | 1.0 | -4.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 (1s) | 15m | trend_pullback | 328 | 0.78 | -0.151 | -49.5 | 1/6 | 1.0 | -5.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 100 (1s) | 15m | rsi2_reversion | 533 | 0.85 | -0.095 | -50.7 | 1/6 | 1.0 | -5.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Step Index | 15m | macd_pullback | 183 | 1.36 | 0.207 | 37.9 | 5/6 | 0.003 | -3.0 | fail: lockbox not negative |
| Step Index | 15m | ema_cross | 388 | 1.16 | 0.092 | 35.7 | 5/6 | 0.023 | 2.0 | fail: profit factor |
| Step Index | 15m | ema_bounce | 440 | 1.1 | 0.066 | 28.9 | 3/6 | 0.067 | 8.8 | fail: profit factor, expectancy, consistent folds, beats random |
| Step Index | 15m | rsi2_reversion | 307 | 1.06 | 0.036 | 11.1 | 2/6 | 0.183 | 4.6 | fail: profit factor, expectancy, consistent folds, beats random |
| Step Index | 15m | legacy_macd_cross | 775 | 1.02 | 0.011 | 8.5 | 3/6 | 0.163 | 9.6 | fail: profit factor, expectancy, consistent folds, beats random |
| Step Index | 15m | donchian_breakout | 251 | 1.05 | 0.032 | 8.0 | 5/6 | 0.23 | -5.6 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Step Index | 15m | legacy_rsi_crossback | 174 | 0.76 | -0.127 | -22.0 | 1/6 | 1.0 | -0.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Step Index | 15m | trend_pullback | 206 | 0.83 | -0.119 | -24.4 | 1/6 | 1.0 | -3.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Step Index | 15m | legacy_ema_cross | 450 | 0.85 | -0.061 | -27.4 | 0/6 | 1.0 | -22.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Step Index | 15m | bollinger_reversion | 398 | 0.89 | -0.071 | -28.4 | 3/6 | 1.0 | 36.8 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 (1s) | 15m | rsi2_reversion | 583 | 1.08 | 0.05 | 29.4 | 4/6 | 0.09 | -16.5 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 75 (1s) | 15m | donchian_breakout | 360 | 1.1 | 0.059 | 21.1 | 3/6 | 0.103 | 5.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 (1s) | 15m | ema_cross | 305 | 1.06 | 0.041 | 12.4 | 4/6 | 0.117 | 9.0 | fail: profit factor, expectancy, beats random |
| Volatility 75 (1s) | 15m | trend_pullback | 226 | 1.07 | 0.041 | 9.3 | 3/6 | 0.307 | 9.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 (1s) | 15m | macd_pullback | 219 | 1.07 | 0.039 | 8.6 | 3/6 | 0.293 | 19.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 (1s) | 15m | ema_bounce | 652 | 1.0 | 0.002 | 1.1 | 3/6 | 1.0 | 9.7 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 (1s) | 15m | legacy_ema_cross | 356 | 0.91 | -0.035 | -12.5 | 3/6 | 1.0 | -2.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 (1s) | 15m | legacy_rsi_crossback | 247 | 0.86 | -0.064 | -15.9 | 1/6 | 1.0 | -1.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 75 (1s) | 15m | legacy_macd_cross | 584 | 0.94 | -0.029 | -16.7 | 2/6 | 1.0 | 11.3 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 75 (1s) | 15m | bollinger_reversion | 248 | 0.82 | -0.118 | -29.3 | 2/6 | 1.0 | 20.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 10 | 15m | trend_pullback | 142 | 1.28 | 0.148 | 21.1 | 6/6 | 0.077 | -2.3 | fail: beats random, lockbox not negative |
| Jump 10 | 15m | donchian_breakout | 328 | 1.09 | 0.056 | 18.3 | 5/6 | 0.193 | 19.2 | fail: profit factor, expectancy, beats random |
| Jump 10 | 15m | legacy_macd_cross | 657 | 1.05 | 0.018 | 11.8 | 3/6 | 0.127 | -4.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 10 | 15m | legacy_ema_cross | 526 | 1.06 | 0.019 | 10.1 | 3/6 | 0.063 | 2.9 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 10 | 15m | macd_pullback | 240 | 1.04 | 0.023 | 5.5 | 3/6 | 0.347 | 3.3 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 10 | 15m | ema_bounce | 547 | 1.01 | 0.004 | 2.0 | 3/6 | 0.507 | 6.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 10 | 15m | legacy_rsi_crossback | 505 | 1.0 | 0.001 | 0.5 | 2/6 | 1.0 | -4.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 10 | 15m | bollinger_reversion | 473 | 0.95 | -0.033 | -15.4 | 3/6 | 1.0 | -27.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 10 | 15m | ema_cross | 423 | 0.9 | -0.064 | -27.0 | 1/6 | 1.0 | -15.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 10 | 15m | rsi2_reversion | 531 | 0.89 | -0.072 | -38.2 | 2/6 | 1.0 | -3.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 25 | 15m | bollinger_reversion | 445 | 1.06 | 0.035 | 15.7 | 3/6 | 0.16 | 9.1 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 25 | 15m | trend_pullback | 261 | 0.96 | -0.023 | -6.1 | 3/6 | 1.0 | -5.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 25 | 15m | ema_cross | 406 | 0.98 | -0.015 | -6.1 | 2/6 | 1.0 | -11.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 25 | 15m | legacy_ema_cross | 387 | 0.91 | -0.039 | -15.2 | 2/6 | 1.0 | 0.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 25 | 15m | macd_pullback | 222 | 0.89 | -0.071 | -15.8 | 2/6 | 1.0 | -8.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 25 | 15m | legacy_macd_cross | 813 | 0.94 | -0.025 | -20.0 | 2/6 | 1.0 | 8.8 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 25 | 15m | donchian_breakout | 315 | 0.87 | -0.079 | -25.0 | 2/6 | 1.0 | 18.6 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 25 | 15m | legacy_rsi_crossback | 544 | 0.86 | -0.065 | -35.5 | 3/6 | 1.0 | 1.6 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 25 | 15m | rsi2_reversion | 459 | 0.85 | -0.1 | -45.9 | 1/6 | 1.0 | 2.1 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 25 | 15m | ema_bounce | 520 | 0.84 | -0.108 | -56.2 | 1/6 | 1.0 | -30.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 50 | 15m | ema_bounce | 463 | 1.15 | 0.092 | 42.7 | 4/6 | 0.057 | 3.9 | fail: profit factor, beats random |
| Jump 50 | 15m | trend_pullback | 333 | 1.19 | 0.111 | 37.1 | 4/6 | 0.033 | 10.5 | fail: profit factor |
| Jump 50 | 15m | macd_pullback | 206 | 1.17 | 0.11 | 22.6 | 4/6 | 0.107 | 23.0 | fail: profit factor, beats random |
| Jump 50 | 15m | ema_cross | 375 | 1.08 | 0.055 | 20.5 | 5/6 | 0.18 | 5.3 | fail: profit factor, expectancy, beats random |
| Jump 50 | 15m | rsi2_reversion | 400 | 1.0 | 0.0 | 0.2 | 3/6 | 1.0 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 50 | 15m | donchian_breakout | 271 | 0.99 | -0.005 | -1.3 | 3/6 | 1.0 | -0.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 50 | 15m | legacy_rsi_crossback | 226 | 0.91 | -0.031 | -7.0 | 2/6 | 1.0 | -8.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 50 | 15m | legacy_ema_cross | 484 | 0.93 | -0.028 | -13.7 | 2/6 | 1.0 | 25.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 50 | 15m | legacy_macd_cross | 625 | 0.95 | -0.024 | -15.2 | 3/6 | 1.0 | -9.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 50 | 15m | bollinger_reversion | 350 | 0.91 | -0.058 | -20.2 | 2/6 | 1.0 | 11.3 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 75 | 15m | macd_pullback | 200 | 1.11 | 0.066 | 13.2 | 3/6 | 0.167 | -6.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 75 | 15m | bollinger_reversion | 341 | 1.01 | 0.004 | 1.5 | 4/6 | 0.31 | -18.5 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Jump 75 | 15m | trend_pullback | 496 | 1.0 | 0.003 | 1.3 | 3/6 | 1.0 | 28.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 75 | 15m | ema_cross | 283 | 0.97 | -0.02 | -5.7 | 3/6 | 1.0 | -1.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 75 | 15m | ema_bounce | 380 | 0.96 | -0.024 | -9.0 | 3/6 | 1.0 | 12.1 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 75 | 15m | donchian_breakout | 286 | 0.95 | -0.034 | -9.8 | 1/6 | 1.0 | -16.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 75 | 15m | legacy_ema_cross | 481 | 0.96 | -0.021 | -9.9 | 3/6 | 1.0 | -4.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 75 | 15m | legacy_macd_cross | 649 | 0.93 | -0.029 | -18.7 | 2/6 | 1.0 | -2.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 75 | 15m | rsi2_reversion | 513 | 0.91 | -0.058 | -29.5 | 3/6 | 1.0 | 18.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 75 | 15m | legacy_rsi_crossback | 408 | 0.75 | -0.083 | -34.0 | 1/6 | 1.0 | 12.9 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 100 | 15m | rsi2_reversion | 404 | 1.17 | 0.105 | 42.2 | 4/6 | 0.003 | -10.0 | fail: profit factor, lockbox not negative |
| Jump 100 | 15m | trend_pullback | 143 | 1.2 | 0.12 | 17.1 | 4/6 | 0.087 | -17.5 | fail: beats random, lockbox not negative |
| Jump 100 | 15m | bollinger_reversion | 297 | 1.06 | 0.035 | 10.5 | 3/6 | 0.167 | -12.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 100 | 15m | macd_pullback | 223 | 1.08 | 0.045 | 10.0 | 4/6 | 0.21 | -24.8 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Jump 100 | 15m | ema_bounce | 536 | 0.99 | -0.005 | -2.9 | 2/6 | 1.0 | -33.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 100 | 15m | legacy_rsi_crossback | 480 | 0.96 | -0.016 | -7.6 | 3/6 | 1.0 | 16.7 | fail: profit factor, expectancy, consistent folds, beats random |
| Jump 100 | 15m | legacy_macd_cross | 616 | 0.94 | -0.027 | -16.9 | 3/6 | 1.0 | -13.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 100 | 15m | legacy_ema_cross | 500 | 0.89 | -0.038 | -19.2 | 2/6 | 1.0 | -4.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 100 | 15m | donchian_breakout | 295 | 0.87 | -0.085 | -25.0 | 2/6 | 1.0 | -12.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Jump 100 | 15m | ema_cross | 386 | 0.89 | -0.071 | -27.6 | 2/6 | 1.0 | -14.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 (1s) | 15m | trend_pullback | 105 | 1.27 | 0.141 | 14.8 | 4/6 | 0.083 | -1.1 | fail: beats random, lockbox not negative |
| Volatility 10 (1s) | 15m | legacy_ema_cross | 392 | 0.97 | -0.012 | -4.8 | 2/6 | 1.0 | -15.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 (1s) | 15m | donchian_breakout | 298 | 0.97 | -0.018 | -5.5 | 3/6 | 1.0 | 12.5 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 10 (1s) | 15m | legacy_rsi_crossback | 143 | 0.77 | -0.087 | -12.5 | 1/6 | 1.0 | -0.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 (1s) | 15m | legacy_macd_cross | 735 | 0.93 | -0.023 | -16.9 | 3/6 | 1.0 | -22.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 (1s) | 15m | ema_cross | 348 | 0.89 | -0.072 | -25.2 | 3/6 | 1.0 | -2.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 (1s) | 15m | macd_pullback | 200 | 0.8 | -0.13 | -25.9 | 2/6 | 1.0 | 0.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 10 (1s) | 15m | bollinger_reversion | 428 | 0.88 | -0.077 | -32.8 | 2/6 | 1.0 | 17.1 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 10 (1s) | 15m | ema_bounce | 430 | 0.87 | -0.085 | -36.6 | 3/6 | 1.0 | 3.2 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 10 (1s) | 15m | rsi2_reversion | 394 | 0.85 | -0.097 | -38.0 | 2/6 | 1.0 | 16.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 15 (1s) | 15m | macd_pullback | 209 | 1.41 | 0.238 | 49.8 | 6/6 | 0.007 | 2.0 | PASS |
| Volatility 15 (1s) | 15m | legacy_macd_cross | 866 | 1.05 | 0.022 | 19.4 | 4/6 | 0.043 | 7.9 | fail: profit factor, expectancy |
| Volatility 15 (1s) | 15m | donchian_breakout | 283 | 1.08 | 0.054 | 15.3 | 5/6 | 0.2 | -29.9 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 15 (1s) | 15m | ema_cross | 343 | 1.02 | 0.014 | 4.8 | 3/6 | 0.237 | 7.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 15 (1s) | 15m | ema_bounce | 446 | 1.02 | 0.01 | 4.6 | 4/6 | 0.453 | -26.2 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 15 (1s) | 15m | trend_pullback | 462 | 1.01 | 0.003 | 1.6 | 3/6 | 0.473 | -4.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 15 (1s) | 15m | legacy_rsi_crossback | 215 | 0.89 | -0.05 | -10.7 | 2/6 | 1.0 | -0.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 15 (1s) | 15m | bollinger_reversion | 331 | 0.94 | -0.039 | -12.8 | 3/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 15 (1s) | 15m | legacy_ema_cross | 453 | 0.91 | -0.035 | -15.9 | 2/6 | 1.0 | 12.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 15 (1s) | 15m | rsi2_reversion | 352 | 0.89 | -0.07 | -24.5 | 1/6 | 1.0 | -13.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 (1s) | 15m | legacy_macd_cross | 717 | 1.1 | 0.031 | 22.0 | 4/6 | 0.06 | 5.2 | fail: profit factor, expectancy, beats random |
| Volatility 25 (1s) | 15m | rsi2_reversion | 271 | 1.1 | 0.062 | 16.8 | 5/6 | 0.167 | 10.1 | fail: profit factor, expectancy, beats random |
| Volatility 25 (1s) | 15m | legacy_rsi_crossback | 618 | 0.99 | -0.005 | -2.9 | 3/6 | 1.0 | 3.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 (1s) | 15m | legacy_ema_cross | 424 | 0.95 | -0.013 | -5.5 | 2/6 | 1.0 | -13.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 (1s) | 15m | ema_cross | 393 | 0.93 | -0.042 | -16.6 | 2/6 | 1.0 | 7.2 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 (1s) | 15m | macd_pullback | 212 | 0.8 | -0.132 | -28.1 | 2/6 | 1.0 | 21.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 (1s) | 15m | donchian_breakout | 280 | 0.85 | -0.104 | -29.1 | 1/6 | 1.0 | -13.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 (1s) | 15m | trend_pullback | 170 | 0.69 | -0.21 | -35.7 | 2/6 | 1.0 | 4.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 (1s) | 15m | bollinger_reversion | 298 | 0.8 | -0.134 | -40.0 | 1/6 | 1.0 | 19.3 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 (1s) | 15m | ema_bounce | 458 | 0.7 | -0.198 | -90.8 | 1/6 | 1.0 | -7.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 30 (1s) | 15m | ema_bounce | 521 | 1.09 | 0.052 | 27.3 | 3/6 | 0.113 | -15.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 30 (1s) | 15m | donchian_breakout | 269 | 1.17 | 0.101 | 27.1 | 4/6 | 0.103 | -1.1 | fail: profit factor, beats random, lockbox not negative |
| Volatility 30 (1s) | 15m | macd_pullback | 209 | 1.01 | 0.009 | 1.9 | 2/6 | 0.467 | -10.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 30 (1s) | 15m | trend_pullback | 133 | 0.89 | -0.066 | -8.8 | 3/6 | 1.0 | -2.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 30 (1s) | 15m | bollinger_reversion | 291 | 0.94 | -0.038 | -11.0 | 3/6 | 1.0 | 1.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 30 (1s) | 15m | legacy_macd_cross | 619 | 0.94 | -0.024 | -14.8 | 3/6 | 1.0 | 10.6 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 30 (1s) | 15m | legacy_rsi_crossback | 391 | 0.9 | -0.046 | -17.8 | 1/6 | 1.0 | 0.9 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 30 (1s) | 15m | rsi2_reversion | 345 | 0.87 | -0.081 | -28.1 | 1/6 | 1.0 | -6.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 30 (1s) | 15m | legacy_ema_cross | 481 | 0.85 | -0.065 | -31.1 | 1/6 | 1.0 | -8.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 30 (1s) | 15m | ema_cross | 340 | 0.81 | -0.131 | -44.5 | 1/6 | 1.0 | 12.2 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 50 (1s) | 15m | ema_cross | 268 | 1.18 | 0.109 | 29.3 | 4/6 | 0.053 | -0.6 | fail: profit factor, beats random, lockbox not negative |
| Volatility 50 (1s) | 15m | ema_bounce | 353 | 1.11 | 0.064 | 22.6 | 4/6 | 0.113 | -1.6 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 50 (1s) | 15m | rsi2_reversion | 312 | 1.04 | 0.026 | 8.1 | 3/6 | 0.273 | 9.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 50 (1s) | 15m | donchian_breakout | 285 | 1.03 | 0.018 | 5.0 | 4/6 | 0.227 | -1.9 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 50 (1s) | 15m | legacy_ema_cross | 311 | 0.98 | -0.007 | -2.1 | 3/6 | 1.0 | 6.2 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 50 (1s) | 15m | bollinger_reversion | 248 | 0.98 | -0.011 | -2.8 | 2/6 | 1.0 | -13.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 (1s) | 15m | trend_pullback | 237 | 0.9 | -0.063 | -15.0 | 3/6 | 1.0 | -5.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 (1s) | 15m | macd_pullback | 246 | 0.86 | -0.088 | -21.8 | 2/6 | 1.0 | 2.1 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 50 (1s) | 15m | legacy_rsi_crossback | 231 | 0.77 | -0.096 | -22.2 | 2/6 | 1.0 | 6.1 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 50 (1s) | 15m | legacy_macd_cross | 936 | 0.93 | -0.024 | -22.2 | 1/6 | 1.0 | -18.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 90 (1s) | 15m | legacy_rsi_crossback | 263 | 1.06 | 0.018 | 4.9 | 4/6 | 0.287 | 6.1 | fail: profit factor, expectancy, beats random |
| Volatility 90 (1s) | 15m | ema_bounce | 534 | 1.0 | 0.002 | 1.2 | 2/6 | 1.0 | -34.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 90 (1s) | 15m | legacy_ema_cross | 405 | 0.93 | -0.02 | -8.3 | 2/6 | 1.0 | -0.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 90 (1s) | 15m | bollinger_reversion | 391 | 0.94 | -0.042 | -16.3 | 3/6 | 1.0 | 9.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 90 (1s) | 15m | trend_pullback | 432 | 0.94 | -0.038 | -16.4 | 3/6 | 1.0 | -20.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 90 (1s) | 15m | donchian_breakout | 238 | 0.87 | -0.082 | -19.5 | 3/6 | 1.0 | 4.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 90 (1s) | 15m | macd_pullback | 256 | 0.88 | -0.078 | -19.9 | 3/6 | 1.0 | 2.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 90 (1s) | 15m | ema_cross | 331 | 0.89 | -0.072 | -24.0 | 2/6 | 1.0 | -14.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 90 (1s) | 15m | legacy_macd_cross | 814 | 0.89 | -0.041 | -33.2 | 1/6 | 1.0 | 15.2 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 90 (1s) | 15m | rsi2_reversion | 412 | 0.83 | -0.116 | -48.0 | 2/6 | 1.0 | -13.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 150 (1s) | 15m | legacy_ema_cross | 384 | 1.17 | 0.069 | 26.6 | 5/6 | 0.017 | 16.9 | fail: profit factor, expectancy |
| Volatility 150 (1s) | 15m | bollinger_reversion | 290 | 1.1 | 0.06 | 17.5 | 5/6 | 0.123 | -16.0 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 150 (1s) | 15m | ema_bounce | 781 | 1.01 | 0.008 | 5.9 | 3/6 | 0.193 | -39.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 150 (1s) | 15m | donchian_breakout | 253 | 0.99 | -0.007 | -1.7 | 3/6 | 1.0 | 3.1 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 150 (1s) | 15m | legacy_macd_cross | 599 | 0.95 | -0.023 | -13.9 | 2/6 | 1.0 | -21.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 150 (1s) | 15m | ema_cross | 337 | 0.91 | -0.063 | -21.3 | 2/6 | 1.0 | 5.3 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 150 (1s) | 15m | trend_pullback | 211 | 0.82 | -0.12 | -25.3 | 2/6 | 1.0 | -14.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 150 (1s) | 15m | macd_pullback | 196 | 0.77 | -0.164 | -32.2 | 1/6 | 1.0 | -18.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 150 (1s) | 15m | legacy_rsi_crossback | 593 | 0.82 | -0.091 | -53.9 | 2/6 | 1.0 | -1.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 150 (1s) | 15m | rsi2_reversion | 370 | 0.76 | -0.166 | -61.3 | 1/6 | 1.0 | -30.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 15m | macd_pullback | 215 | 0.91 | -0.063 | -13.5 | 2/6 | 1.0 | -4.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 15m | legacy_rsi_crossback | 302 | 0.83 | -0.082 | -24.9 | 1/6 | 1.0 | 0.7 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 250 (1s) | 15m | bollinger_reversion | 376 | 0.86 | -0.089 | -33.5 | 2/6 | 1.0 | -18.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 15m | legacy_macd_cross | 595 | 0.87 | -0.06 | -35.5 | 1/6 | 1.0 | -7.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 15m | donchian_breakout | 337 | 0.81 | -0.13 | -43.7 | 1/6 | 1.0 | -39.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 15m | trend_pullback | 307 | 0.79 | -0.145 | -44.4 | 1/6 | 1.0 | 5.8 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 250 (1s) | 15m | legacy_ema_cross | 401 | 0.78 | -0.111 | -44.7 | 0/6 | 1.0 | -11.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 15m | ema_cross | 347 | 0.77 | -0.158 | -54.7 | 1/6 | 1.0 | -7.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 15m | ema_bounce | 662 | 0.84 | -0.107 | -70.7 | 2/6 | 1.0 | -36.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 250 (1s) | 15m | rsi2_reversion | 430 | 0.65 | -0.257 | -110.5 | 1/6 | 1.0 | -21.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 | 15m | ema_bounce | 573 | 1.15 | 0.096 | 54.8 | 5/6 | 0.04 | -13.1 | fail: profit factor, lockbox not negative |
| Volatility 10 | 15m | trend_pullback | 355 | 1.11 | 0.066 | 23.5 | 3/6 | 0.27 | -3.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 | 15m | ema_cross | 306 | 1.07 | 0.046 | 13.9 | 3/6 | 0.263 | -7.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 | 15m | macd_pullback | 213 | 1.05 | 0.034 | 7.2 | 3/6 | 0.413 | 5.6 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 10 | 15m | rsi2_reversion | 380 | 0.98 | -0.011 | -4.0 | 4/6 | 1.0 | -29.1 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 10 | 15m | donchian_breakout | 316 | 0.98 | -0.013 | -4.2 | 2/6 | 1.0 | -19.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 10 | 15m | legacy_ema_cross | 365 | 0.97 | -0.013 | -4.8 | 1/6 | 1.0 | 10.6 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 10 | 15m | legacy_rsi_crossback | 171 | 0.86 | -0.054 | -9.3 | 2/6 | 1.0 | 3.7 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 10 | 15m | legacy_macd_cross | 619 | 0.91 | -0.042 | -26.2 | 2/6 | 1.0 | 14.7 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 10 | 15m | bollinger_reversion | 411 | 0.84 | -0.109 | -44.6 | 1/6 | 1.0 | 15.9 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 | 15m | ema_cross | 327 | 1.22 | 0.138 | 45.2 | 4/6 | 0.037 | 16.1 | PASS |
| Volatility 25 | 15m | donchian_breakout | 275 | 1.09 | 0.059 | 16.2 | 4/6 | 0.22 | -14.1 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 25 | 15m | macd_pullback | 191 | 1.09 | 0.06 | 11.4 | 3/6 | 0.207 | -6.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 | 15m | legacy_macd_cross | 878 | 1.03 | 0.011 | 9.6 | 3/6 | 0.123 | -12.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 | 15m | legacy_ema_cross | 542 | 1.02 | 0.008 | 4.2 | 4/6 | 0.17 | 6.3 | fail: profit factor, expectancy, beats random |
| Volatility 25 | 15m | rsi2_reversion | 560 | 1.0 | 0.002 | 1.1 | 2/6 | 1.0 | -32.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 | 15m | trend_pullback | 131 | 1.01 | 0.005 | 0.7 | 5/6 | 0.49 | -7.0 | fail: profit factor, expectancy, beats random, lockbox not negative |
| Volatility 25 | 15m | ema_bounce | 508 | 0.97 | -0.022 | -11.3 | 1/6 | 1.0 | -24.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 25 | 15m | legacy_rsi_crossback | 168 | 0.75 | -0.089 | -15.0 | 1/6 | 1.0 | 2.2 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 25 | 15m | bollinger_reversion | 337 | 0.9 | -0.065 | -22.0 | 2/6 | 1.0 | -18.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 | 15m | bollinger_reversion | 307 | 1.02 | 0.012 | 3.8 | 3/6 | 0.18 | -2.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 | 15m | legacy_macd_cross | 813 | 1.01 | 0.003 | 2.1 | 2/6 | 0.273 | 1.7 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 50 | 15m | legacy_rsi_crossback | 418 | 0.97 | -0.009 | -3.8 | 3/6 | 1.0 | -0.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 50 | 15m | rsi2_reversion | 294 | 0.95 | -0.027 | -8.1 | 2/6 | 1.0 | -1.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 | 15m | ema_cross | 348 | 0.94 | -0.039 | -13.4 | 1/6 | 1.0 | -4.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 | 15m | legacy_ema_cross | 421 | 0.89 | -0.043 | -18.2 | 2/6 | 1.0 | 1.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 50 | 15m | trend_pullback | 391 | 0.88 | -0.072 | -28.2 | 2/6 | 1.0 | 7.4 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 50 | 15m | ema_bounce | 531 | 0.87 | -0.085 | -45.3 | 3/6 | 1.0 | 28.0 | fail: profit factor, expectancy, consistent folds, beats random |
| Volatility 50 | 15m | donchian_breakout | 340 | 0.79 | -0.136 | -46.4 | 1/6 | 1.0 | -13.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Volatility 50 | 15m | macd_pullback | 197 | 0.64 | -0.255 | -50.3 | 1/6 | 1.0 | 3.0 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / AUD | 15m | legacy_rsi_crossback | 132 | 1.2 | 0.077 | 10.1 | 4/6 | 0.007 | -3.0 | fail: expectancy, lockbox not negative |
| EUR / AUD | 15m | trend_pullback | 86 | 0.9 | -0.065 | -5.6 | 3/6 | 1.0 | -4.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / AUD | 15m | macd_pullback | 168 | 0.94 | -0.039 | -6.5 | 3/6 | 1.0 | -20.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / AUD | 15m | legacy_macd_cross | 393 | 0.89 | -0.05 | -19.5 | 2/6 | 1.0 | -26.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / AUD | 15m | legacy_ema_cross | 282 | 0.7 | -0.114 | -32.2 | 0/6 | 1.0 | -26.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / AUD | 15m | ema_cross | 245 | 0.76 | -0.155 | -38.0 | 1/6 | 1.0 | -36.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / AUD | 15m | donchian_breakout | 171 | 0.67 | -0.235 | -40.2 | 1/6 | 1.0 | -9.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / AUD | 15m | ema_bounce | 314 | 0.78 | -0.152 | -47.6 | 2/6 | 1.0 | -34.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / AUD | 15m | bollinger_reversion | 253 | 0.73 | -0.192 | -48.6 | 1/6 | 1.0 | -18.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / AUD | 15m | rsi2_reversion | 206 | 0.65 | -0.241 | -49.6 | 1/6 | 1.0 | -13.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 15m | trend_pullback | 102 | 0.78 | -0.143 | -14.6 | 1/6 | 1.0 | -12.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 15m | legacy_rsi_crossback | 74 | 0.51 | -0.245 | -18.1 | 1/6 | 1.0 | 1.7 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / CAD | 15m | macd_pullback | 145 | 0.72 | -0.194 | -28.1 | 1/6 | 1.0 | -30.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 15m | legacy_ema_cross | 265 | 0.63 | -0.191 | -50.7 | 0/6 | 1.0 | -16.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 15m | rsi2_reversion | 201 | 0.6 | -0.275 | -55.3 | 0/6 | 1.0 | -22.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 15m | bollinger_reversion | 173 | 0.53 | -0.328 | -56.7 | 0/6 | 1.0 | -39.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 15m | donchian_breakout | 261 | 0.67 | -0.219 | -57.2 | 1/6 | 1.0 | -34.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 15m | legacy_macd_cross | 468 | 0.56 | -0.184 | -86.2 | 0/6 | 1.0 | -32.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 15m | ema_cross | 249 | 0.52 | -0.355 | -88.5 | 1/6 | 1.0 | -19.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CAD | 15m | ema_bounce | 373 | 0.61 | -0.278 | -103.6 | 0/6 | 1.0 | -68.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 15m | legacy_rsi_crossback | 96 | 0.53 | -0.24 | -23.1 | 0/6 | 1.0 | -7.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 15m | trend_pullback | 94 | 0.6 | -0.277 | -26.0 | 2/6 | 1.0 | -5.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 15m | donchian_breakout | 175 | 0.52 | -0.34 | -59.6 | 2/6 | 1.0 | -19.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 15m | bollinger_reversion | 145 | 0.42 | -0.45 | -65.2 | 0/6 | 1.0 | -29.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 15m | macd_pullback | 158 | 0.44 | -0.425 | -67.1 | 0/6 | 1.0 | -19.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 15m | ema_cross | 212 | 0.49 | -0.36 | -76.3 | 0/6 | 1.0 | -23.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 15m | rsi2_reversion | 206 | 0.48 | -0.373 | -76.8 | 0/6 | 1.0 | -23.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 15m | legacy_ema_cross | 281 | 0.42 | -0.279 | -78.5 | 0/6 | 1.0 | -12.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 15m | legacy_macd_cross | 415 | 0.55 | -0.248 | -102.8 | 0/6 | 1.0 | -11.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / CHF | 15m | ema_bounce | 328 | 0.46 | -0.403 | -132.2 | 0/6 | 1.0 | -35.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 15m | legacy_rsi_crossback | 172 | 0.91 | -0.041 | -7.0 | 3/6 | 1.0 | 4.8 | fail: profit factor, expectancy, consistent folds, beats random |
| EUR / NZD | 15m | ema_cross | 197 | 0.85 | -0.099 | -19.6 | 2/6 | 1.0 | -20.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 15m | donchian_breakout | 192 | 0.81 | -0.117 | -22.4 | 0/6 | 1.0 | -25.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 15m | macd_pullback | 147 | 0.73 | -0.185 | -27.3 | 1/6 | 1.0 | -21.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 15m | trend_pullback | 83 | 0.53 | -0.354 | -29.4 | 0/6 | 1.0 | -8.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 15m | bollinger_reversion | 153 | 0.71 | -0.21 | -32.1 | 1/6 | 1.0 | -14.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 15m | legacy_macd_cross | 475 | 0.77 | -0.093 | -44.3 | 2/6 | 1.0 | -5.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 15m | rsi2_reversion | 224 | 0.68 | -0.216 | -48.4 | 2/6 | 1.0 | -16.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 15m | legacy_ema_cross | 330 | 0.6 | -0.155 | -51.2 | 0/6 | 1.0 | -20.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / NZD | 15m | ema_bounce | 336 | 0.59 | -0.285 | -95.6 | 0/6 | 1.0 | -23.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 15m | legacy_rsi_crossback | 93 | 0.82 | -0.085 | -7.9 | 2/6 | 1.0 | -10.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 15m | legacy_ema_cross | 235 | 0.76 | -0.116 | -27.3 | 1/6 | 1.0 | -10.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 15m | macd_pullback | 150 | 0.7 | -0.192 | -28.9 | 1/6 | 1.0 | -19.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 15m | legacy_macd_cross | 401 | 0.82 | -0.085 | -34.0 | 1/6 | 1.0 | -15.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 15m | bollinger_reversion | 156 | 0.61 | -0.283 | -44.1 | 0/6 | 1.0 | -21.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 15m | trend_pullback | 158 | 0.59 | -0.293 | -46.3 | 0/6 | 1.0 | -3.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 15m | rsi2_reversion | 208 | 0.6 | -0.284 | -59.2 | 0/6 | 1.0 | -28.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 15m | donchian_breakout | 194 | 0.56 | -0.314 | -60.9 | 0/6 | 1.0 | -8.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 15m | ema_cross | 209 | 0.58 | -0.305 | -63.7 | 0/6 | 1.0 | -9.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / AUD | 15m | ema_bounce | 329 | 0.69 | -0.201 | -66.2 | 1/6 | 1.0 | -34.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 15m | legacy_ema_cross | 248 | 0.87 | -0.059 | -14.6 | 1/6 | 1.0 | -5.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 15m | legacy_rsi_crossback | 108 | 0.71 | -0.15 | -16.2 | 1/6 | 1.0 | -4.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 15m | trend_pullback | 127 | 0.58 | -0.293 | -37.2 | 1/6 | 1.0 | -11.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 15m | donchian_breakout | 191 | 0.69 | -0.213 | -40.6 | 1/6 | 1.0 | -37.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 15m | ema_cross | 216 | 0.7 | -0.201 | -43.5 | 0/6 | 1.0 | -14.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 15m | bollinger_reversion | 161 | 0.6 | -0.275 | -44.3 | 2/6 | 1.0 | -20.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 15m | macd_pullback | 157 | 0.56 | -0.299 | -47.0 | 1/6 | 1.0 | -15.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 15m | rsi2_reversion | 311 | 0.67 | -0.222 | -69.1 | 1/6 | 1.0 | -48.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 15m | ema_bounce | 308 | 0.62 | -0.253 | -78.0 | 0/6 | 1.0 | -46.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CAD | 15m | legacy_macd_cross | 471 | 0.55 | -0.193 | -90.8 | 0/6 | 1.0 | -28.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 15m | legacy_rsi_crossback | 140 | 0.42 | -0.34 | -47.6 | 1/6 | 1.0 | -5.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 15m | donchian_breakout | 168 | 0.54 | -0.345 | -58.0 | 1/6 | 1.0 | -16.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 15m | trend_pullback | 87 | 0.18 | -0.728 | -63.3 | 0/6 | 1.0 | -21.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 15m | macd_pullback | 168 | 0.4 | -0.463 | -77.8 | 0/6 | 1.0 | -24.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 15m | bollinger_reversion | 174 | 0.28 | -0.583 | -101.4 | 0/6 | 1.0 | -31.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 15m | rsi2_reversion | 215 | 0.38 | -0.493 | -105.9 | 0/6 | 1.0 | -52.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 15m | legacy_ema_cross | 309 | 0.38 | -0.368 | -113.6 | 0/6 | 1.0 | -32.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 15m | ema_cross | 245 | 0.36 | -0.505 | -123.7 | 0/6 | 1.0 | -32.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 15m | legacy_macd_cross | 477 | 0.41 | -0.277 | -132.1 | 0/6 | 1.0 | -28.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / CHF | 15m | ema_bounce | 412 | 0.3 | -0.569 | -234.6 | 0/6 | 1.0 | -66.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 15m | legacy_rsi_crossback | 101 | 0.7 | -0.143 | -14.4 | 1/6 | 1.0 | -1.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 15m | ema_cross | 181 | 0.8 | -0.131 | -23.7 | 3/6 | 1.0 | 3.5 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / NZD | 15m | bollinger_reversion | 175 | 0.75 | -0.167 | -29.3 | 0/6 | 1.0 | 1.7 | fail: profit factor, expectancy, consistent folds, beats random |
| GBP / NZD | 15m | trend_pullback | 80 | 0.47 | -0.406 | -32.5 | 1/6 | 1.0 | -19.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 15m | legacy_ema_cross | 271 | 0.61 | -0.172 | -46.6 | 0/6 | 1.0 | -1.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 15m | rsi2_reversion | 203 | 0.66 | -0.237 | -48.1 | 0/6 | 1.0 | -13.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 15m | macd_pullback | 147 | 0.54 | -0.336 | -49.4 | 1/6 | 1.0 | -7.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 15m | legacy_macd_cross | 480 | 0.67 | -0.142 | -68.3 | 0/6 | 1.0 | -17.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 15m | donchian_breakout | 235 | 0.57 | -0.3 | -70.6 | 0/6 | 1.0 | -17.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| GBP / NZD | 15m | ema_bounce | 346 | 0.56 | -0.306 | -105.9 | 0/6 | 1.0 | -28.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 15m | legacy_rsi_crossback | 118 | 1.02 | 0.007 | 0.8 | 3/6 | 0.0 | -9.1 | fail: profit factor, expectancy, consistent folds, lockbox not negative |
| AUD / CAD | 15m | trend_pullback | 103 | 0.63 | -0.263 | -27.1 | 2/6 | 1.0 | -2.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 15m | bollinger_reversion | 171 | 0.74 | -0.182 | -31.0 | 1/6 | 1.0 | -42.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 15m | donchian_breakout | 149 | 0.59 | -0.287 | -42.8 | 0/6 | 1.0 | -21.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 15m | ema_cross | 208 | 0.69 | -0.214 | -44.5 | 1/6 | 1.0 | -23.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 15m | macd_pullback | 141 | 0.48 | -0.394 | -55.6 | 1/6 | 1.0 | -21.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 15m | legacy_macd_cross | 394 | 0.71 | -0.143 | -56.2 | 0/6 | 1.0 | -25.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 15m | rsi2_reversion | 200 | 0.59 | -0.294 | -58.9 | 0/6 | 1.0 | -24.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 15m | legacy_ema_cross | 342 | 0.59 | -0.195 | -66.7 | 0/6 | 1.0 | -13.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CAD | 15m | ema_bounce | 315 | 0.61 | -0.274 | -86.3 | 0/6 | 1.0 | -39.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 15m | legacy_rsi_crossback | 103 | 0.49 | -0.22 | -22.7 | 1/6 | 1.0 | -13.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 15m | trend_pullback | 84 | 0.36 | -0.492 | -41.4 | 0/6 | 1.0 | -25.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 15m | bollinger_reversion | 136 | 0.5 | -0.384 | -52.3 | 0/6 | 1.0 | -38.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 15m | macd_pullback | 154 | 0.52 | -0.363 | -55.9 | 0/6 | 1.0 | -30.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 15m | legacy_ema_cross | 266 | 0.47 | -0.268 | -71.2 | 0/6 | 1.0 | -39.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 15m | rsi2_reversion | 213 | 0.5 | -0.389 | -82.8 | 0/6 | 1.0 | -57.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 15m | ema_cross | 243 | 0.5 | -0.385 | -93.5 | 1/6 | 1.0 | -35.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 15m | donchian_breakout | 220 | 0.39 | -0.483 | -106.2 | 0/6 | 1.0 | -23.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 15m | legacy_macd_cross | 418 | 0.48 | -0.31 | -129.8 | 0/6 | 1.0 | -40.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / CHF | 15m | ema_bounce | 343 | 0.44 | -0.444 | -152.2 | 0/6 | 1.0 | -71.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 15m | trend_pullback | 96 | 0.65 | -0.249 | -23.9 | 0/6 | 1.0 | -10.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 15m | donchian_breakout | 178 | 0.78 | -0.148 | -26.4 | 0/6 | 1.0 | -12.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 15m | legacy_rsi_crossback | 93 | 0.4 | -0.374 | -34.8 | 0/6 | 1.0 | -6.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 15m | ema_cross | 182 | 0.63 | -0.252 | -45.8 | 0/6 | 1.0 | -10.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 15m | legacy_ema_cross | 255 | 0.65 | -0.185 | -47.1 | 1/6 | 1.0 | -20.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 15m | macd_pullback | 140 | 0.53 | -0.346 | -48.5 | 1/6 | 1.0 | -17.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 15m | bollinger_reversion | 130 | 0.46 | -0.429 | -55.8 | 1/6 | 1.0 | -4.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 15m | rsi2_reversion | 281 | 0.5 | -0.394 | -110.8 | 0/6 | 1.0 | 4.6 | fail: profit factor, expectancy, consistent folds, beats random |
| AUD / NZD | 15m | legacy_macd_cross | 430 | 0.51 | -0.279 | -120.1 | 0/6 | 1.0 | -10.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| AUD / NZD | 15m | ema_bounce | 340 | 0.51 | -0.361 | -122.8 | 0/6 | 1.0 | -28.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 15m | donchian_breakout | 188 | 0.97 | -0.019 | -3.5 | 2/6 | 1.0 | -14.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 15m | legacy_rsi_crossback | 79 | 0.65 | -0.153 | -12.1 | 1/6 | 1.0 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 15m | trend_pullback | 87 | 0.79 | -0.144 | -12.5 | 2/6 | 1.0 | -0.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 15m | bollinger_reversion | 234 | 0.86 | -0.088 | -20.7 | 2/6 | 1.0 | -37.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 15m | legacy_ema_cross | 267 | 0.59 | -0.171 | -45.7 | 0/6 | 1.0 | -12.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 15m | macd_pullback | 159 | 0.55 | -0.315 | -50.0 | 0/6 | 1.0 | -8.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 15m | rsi2_reversion | 234 | 0.68 | -0.215 | -50.4 | 0/6 | 1.0 | -9.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 15m | legacy_macd_cross | 482 | 0.72 | -0.114 | -54.9 | 1/6 | 1.0 | -24.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 15m | ema_cross | 267 | 0.66 | -0.244 | -65.3 | 1/6 | 1.0 | -21.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| NZD / JPY | 15m | ema_bounce | 352 | 0.58 | -0.307 | -108.2 | 0/6 | 1.0 | -12.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CAD / JPY | 15m | legacy_rsi_crossback | 80 | 0.77 | -0.107 | -8.6 | 2/6 | 1.0 | -0.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CAD / JPY | 15m | trend_pullback | 83 | 0.73 | -0.175 | -14.5 | 1/6 | 1.0 | -4.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CAD / JPY | 15m | donchian_breakout | 226 | 0.67 | -0.236 | -53.2 | 1/6 | 1.0 | -22.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CAD / JPY | 15m | macd_pullback | 145 | 0.42 | -0.436 | -63.2 | 1/6 | 1.0 | -12.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CAD / JPY | 15m | rsi2_reversion | 221 | 0.59 | -0.294 | -64.9 | 0/6 | 1.0 | 10.2 | fail: profit factor, expectancy, consistent folds, beats random |
| CAD / JPY | 15m | ema_cross | 226 | 0.59 | -0.298 | -67.3 | 0/6 | 1.0 | 12.8 | fail: profit factor, expectancy, consistent folds, beats random |
| CAD / JPY | 15m | bollinger_reversion | 182 | 0.46 | -0.394 | -71.7 | 0/6 | 1.0 | -16.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CAD / JPY | 15m | legacy_ema_cross | 271 | 0.44 | -0.285 | -77.2 | 0/6 | 1.0 | -9.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CAD / JPY | 15m | legacy_macd_cross | 401 | 0.56 | -0.243 | -97.6 | 0/6 | 1.0 | -22.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CAD / JPY | 15m | ema_bounce | 418 | 0.53 | -0.341 | -142.7 | 0/6 | 1.0 | -17.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 15m | legacy_rsi_crossback | 78 | 0.56 | -0.175 | -13.6 | 2/6 | 1.0 | -5.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 15m | bollinger_reversion | 214 | 0.8 | -0.133 | -28.5 | 1/6 | 1.0 | -17.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 15m | legacy_ema_cross | 265 | 0.76 | -0.118 | -31.3 | 2/6 | 1.0 | -15.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 15m | trend_pullback | 122 | 0.6 | -0.285 | -34.8 | 0/6 | 1.0 | -10.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 15m | macd_pullback | 155 | 0.68 | -0.23 | -35.6 | 1/6 | 1.0 | -12.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 15m | donchian_breakout | 185 | 0.66 | -0.234 | -43.2 | 1/6 | 1.0 | -5.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 15m | rsi2_reversion | 194 | 0.64 | -0.256 | -49.6 | 0/6 | 1.0 | -15.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 15m | ema_cross | 240 | 0.67 | -0.225 | -53.9 | 0/6 | 1.0 | -20.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 15m | legacy_macd_cross | 460 | 0.67 | -0.137 | -62.9 | 1/6 | 1.0 | -17.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| CHF / JPY | 15m | ema_bounce | 430 | 0.59 | -0.301 | -129.4 | 0/6 | 1.0 | -35.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 15m | legacy_rsi_crossback | 102 | 0.46 | -0.32 | -32.7 | 0/6 | 1.0 | -13.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 15m | trend_pullback | 104 | 0.14 | -0.766 | -79.6 | 0/6 | 1.0 | -22.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 15m | macd_pullback | 176 | 0.17 | -0.737 | -129.7 | 0/6 | 1.0 | -40.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 15m | bollinger_reversion | 203 | 0.15 | -0.777 | -157.7 | 0/6 | 1.0 | -69.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 15m | donchian_breakout | 216 | 0.16 | -0.744 | -160.7 | 0/6 | 1.0 | -42.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 15m | ema_cross | 235 | 0.19 | -0.703 | -165.1 | 0/6 | 1.0 | -50.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 15m | legacy_ema_cross | 364 | 0.28 | -0.509 | -185.4 | 0/6 | 1.0 | -81.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 15m | rsi2_reversion | 255 | 0.15 | -0.769 | -196.2 | 0/6 | 1.0 | -61.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 15m | legacy_macd_cross | 492 | 0.25 | -0.542 | -266.7 | 0/6 | 1.0 | -103.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| EUR / SEK | 15m | ema_bounce | 495 | 0.15 | -0.761 | -376.8 | 0/6 | 1.0 | -150.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 15m | legacy_rsi_crossback | 92 | 0.62 | -0.153 | -14.1 | 1/6 | 1.0 | -3.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 15m | bollinger_reversion | 168 | 0.66 | -0.245 | -41.1 | 0/6 | 1.0 | -24.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 15m | rsi2_reversion | 216 | 0.67 | -0.212 | -45.7 | 0/6 | 1.0 | -28.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 15m | macd_pullback | 151 | 0.54 | -0.339 | -51.3 | 1/6 | 1.0 | -32.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 15m | legacy_ema_cross | 249 | 0.61 | -0.209 | -52.2 | 0/6 | 1.0 | -18.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 15m | donchian_breakout | 202 | 0.62 | -0.264 | -53.2 | 1/6 | 1.0 | -14.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 15m | trend_pullback | 156 | 0.52 | -0.349 | -54.5 | 0/6 | 1.0 | -18.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 15m | ema_cross | 204 | 0.56 | -0.319 | -65.1 | 0/6 | 1.0 | -41.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 15m | legacy_macd_cross | 409 | 0.55 | -0.228 | -93.3 | 0/6 | 1.0 | -32.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / MXN | 15m | ema_bounce | 323 | 0.5 | -0.373 | -120.3 | 0/6 | 1.0 | -59.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 15m | legacy_rsi_crossback | 100 | 0.6 | -0.158 | -15.8 | 1/6 | 1.0 | -9.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 15m | trend_pullback | 105 | 0.39 | -0.496 | -52.0 | 0/6 | 1.0 | -9.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 15m | bollinger_reversion | 169 | 0.52 | -0.376 | -63.6 | 0/6 | 1.0 | -38.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 15m | macd_pullback | 166 | 0.42 | -0.452 | -75.0 | 0/6 | 1.0 | -21.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 15m | donchian_breakout | 179 | 0.44 | -0.434 | -77.6 | 1/6 | 1.0 | -24.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 15m | legacy_ema_cross | 286 | 0.53 | -0.275 | -78.8 | 0/6 | 1.0 | -16.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 15m | ema_cross | 234 | 0.53 | -0.348 | -81.5 | 0/6 | 1.0 | -13.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 15m | rsi2_reversion | 222 | 0.46 | -0.42 | -93.3 | 0/6 | 1.0 | -37.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 15m | legacy_macd_cross | 485 | 0.44 | -0.284 | -137.7 | 0/6 | 1.0 | -56.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / SEK | 15m | ema_bounce | 476 | 0.45 | -0.41 | -195.2 | 0/6 | 1.0 | -66.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 15m | legacy_rsi_crossback | 76 | 0.67 | -0.151 | -11.5 | 0/6 | 1.0 | -9.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 15m | trend_pullback | 106 | 0.55 | -0.316 | -33.5 | 2/6 | 1.0 | -5.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 15m | donchian_breakout | 152 | 0.54 | -0.334 | -50.7 | 1/6 | 1.0 | -29.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 15m | rsi2_reversion | 230 | 0.53 | -0.328 | -75.5 | 0/6 | 1.0 | -12.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 15m | legacy_ema_cross | 333 | 0.56 | -0.243 | -81.1 | 0/6 | 1.0 | -32.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 15m | ema_cross | 267 | 0.56 | -0.308 | -82.2 | 0/6 | 1.0 | -56.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 15m | macd_pullback | 150 | 0.31 | -0.549 | -82.3 | 0/6 | 1.0 | -40.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 15m | bollinger_reversion | 191 | 0.41 | -0.447 | -85.4 | 0/6 | 1.0 | -29.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 15m | ema_bounce | 326 | 0.49 | -0.387 | -126.1 | 0/6 | 1.0 | -70.6 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / NOK | 15m | legacy_macd_cross | 509 | 0.47 | -0.253 | -128.9 | 0/6 | 1.0 | -46.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 15m | legacy_rsi_crossback | 107 | 0.22 | -0.518 | -55.4 | 1/6 | 1.0 | -9.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 15m | trend_pullback | 107 | 0.16 | -0.752 | -80.5 | 0/6 | 1.0 | -20.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 15m | macd_pullback | 152 | 0.12 | -0.807 | -122.6 | 0/6 | 1.0 | -44.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 15m | ema_cross | 213 | 0.16 | -0.735 | -156.6 | 0/6 | 1.0 | -56.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 15m | bollinger_reversion | 202 | 0.13 | -0.79 | -159.5 | 0/6 | 1.0 | -81.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 15m | legacy_ema_cross | 324 | 0.21 | -0.598 | -193.6 | 0/6 | 1.0 | -65.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 15m | rsi2_reversion | 249 | 0.11 | -0.823 | -204.9 | 0/6 | 1.0 | -67.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 15m | donchian_breakout | 257 | 0.12 | -0.808 | -207.6 | 0/6 | 1.0 | -58.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 15m | legacy_macd_cross | 509 | 0.21 | -0.581 | -295.6 | 0/6 | 1.0 | -116.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| USD / PLN | 15m | ema_bounce | 508 | 0.09 | -0.847 | -430.1 | 0/6 | 1.0 | -163.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 15m | legacy_rsi_crossback | 155 | 0.97 | -0.014 | -2.2 | 3/6 | 1.0 | -4.1 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 15m | trend_pullback | 89 | 0.76 | -0.155 | -13.8 | 2/6 | 1.0 | -8.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 15m | bollinger_reversion | 175 | 0.77 | -0.152 | -26.5 | 2/6 | 1.0 | -5.5 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 15m | ema_cross | 178 | 0.72 | -0.189 | -33.6 | 2/6 | 1.0 | -3.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 15m | rsi2_reversion | 221 | 0.77 | -0.156 | -34.4 | 2/6 | 1.0 | -25.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 15m | donchian_breakout | 170 | 0.67 | -0.229 | -39.0 | 1/6 | 1.0 | -1.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 15m | legacy_ema_cross | 307 | 0.67 | -0.128 | -39.2 | 0/6 | 1.0 | -9.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 15m | macd_pullback | 155 | 0.58 | -0.304 | -47.1 | 0/6 | 1.0 | -4.0 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 15m | ema_bounce | 269 | 0.75 | -0.175 | -47.2 | 2/6 | 1.0 | -7.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Platinum / USD | 15m | legacy_macd_cross | 445 | 0.71 | -0.12 | -53.3 | 0/6 | 1.0 | -17.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 15m | legacy_rsi_crossback | 53 | 0.79 | -0.078 | -4.1 | 2/6 | 1.0 | -3.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 15m | trend_pullback | 80 | 0.57 | -0.303 | -24.2 | 2/6 | 1.0 | -14.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 15m | legacy_ema_cross | 243 | 0.71 | -0.149 | -36.3 | 1/6 | 1.0 | -12.9 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 15m | bollinger_reversion | 176 | 0.67 | -0.236 | -41.5 | 2/6 | 1.0 | -8.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 15m | rsi2_reversion | 202 | 0.65 | -0.239 | -48.3 | 1/6 | 1.0 | -35.4 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 15m | macd_pullback | 129 | 0.46 | -0.409 | -52.7 | 0/6 | 1.0 | -26.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 15m | ema_cross | 231 | 0.61 | -0.266 | -61.4 | 0/6 | 1.0 | -41.3 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 15m | legacy_macd_cross | 402 | 0.64 | -0.188 | -75.7 | 0/6 | 1.0 | -22.2 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 15m | donchian_breakout | 219 | 0.45 | -0.429 | -94.0 | 0/6 | 1.0 | -1.7 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
| Palladium / USD | 15m | ema_bounce | 298 | 0.55 | -0.33 | -98.3 | 0/6 | 1.0 | -55.8 | fail: profit factor, expectancy, consistent folds, beats random, lockbox not negative |
