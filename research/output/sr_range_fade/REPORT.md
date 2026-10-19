# Support/resistance range fade

## What a PASS is worth

Every rate below comes from the same test run on random walks, which hold no
support or resistance at all, so each PASS there is a false pass.

- Luck check: random walks matched to a pair, 15m: 2/40 (5%) on the limit trigger, no tests on rejection.
- Luck check: random walks matched to a pair, 5m: 2/30 (7%) on the limit trigger, no tests on rejection.
- Luck check: random walks at synthetic volatility, 15m: 4/20 (20%) on the limit trigger, 0/20 (0%) on rejection.

## Did a pass reproduce?

A level that is really there should hold at another granularity and in
another year. Walk-forward expectancy on the limit trigger, by run:

| Market | Deriv synthetics from the chart photos, 15m | Forex pairs and metals, 15m | Deriv synthetics from the chart photos, 5m | Forex pairs and metals, 5m | Ten years of Dukascopy hourly history, 1h |
|---|---|---|---|---|---|
| 1HZ30V | -0.049R (1592) FAIL | not run | +0.041R (2649) PASS | not run | not run |
| 1HZ75V | +0.026R (1620) PASS | not run | +0.031R (2558) PASS | not run | not run |
| JD10 | +0.079R (1446) PASS | not run | +0.076R (2341) FAIL | not run | not run |
| frxEURAUD | not run | +0.085R (432) PASS | not run | -0.005R (52) FAIL | -0.053R (1330) FAIL |
| frxGBPAUD | not run | +0.070R (294) PASS | not run | -0.305R (52) FAIL | not run |
| frxUSDCAD | not run | +0.015R (269) PASS | not run | not run | -0.029R (3027) FAIL |
| frxXPTUSD | not run | +0.020R (553) PASS | not run | not run | not run |

## Deriv synthetics from the chart photos, 15m

Published rule 2/14 (14%) — limit 2/7 (29%), rejection 0/7 (0%). Strict rule 1/14 (7%) — limit 1/7 (14%), rejection 0/7 (0%).

| Market | Trigger | WF trades | Win | WF exp | WF PF | Lockbox exp | p vs random | Folds up | Verdict | Strict |
|---|---|---|---|---|---|---|---|---|---|---|
| Jump 10 | limit | 1446 | 27.2% | +0.079R | 1.11 | +0.142R | 0.017 | 4/6 | PASS | PASS |
| Volatility 75 (1s) | limit | 1620 | 26.0% | +0.026R | 1.03 | +0.179R | 0.027 | 3/6 | PASS | FAIL |
| Volatility 90 (1s) | limit | 1650 | 26.7% | +0.026R | 1.04 | -0.008R | 0.0 | 3/6 | FAIL | FAIL |
| Volatility 10 (1s) | limit | 1515 | 26.0% | +0.021R | 1.03 | -0.142R | 0.01 | 4/6 | FAIL | FAIL |
| Volatility 15 (1s) | limit | 1668 | 25.7% | +0.013R | 1.02 | +0.171R | 0.103 | 3/6 | FAIL | FAIL |
| Volatility 25 (1s) | limit | 1850 | 25.3% | -0.010R | 0.99 | -0.082R | 0.043 | 1/6 | FAIL | FAIL |
| Volatility 30 (1s) | limit | 1592 | 24.1% | -0.049R | 0.94 | -0.021R | 0.517 | 2/6 | FAIL | FAIL |
| Jump 10 | rejection | 1379 | 18.9% | -0.024R | 0.97 | +0.231R | 0.343 | 3/6 | FAIL | FAIL |
| Volatility 10 (1s) | rejection | 811 | 27.1% | -0.061R | 0.92 | -0.210R | 0.577 | 3/6 | FAIL | FAIL |
| Volatility 15 (1s) | rejection | 997 | 26.1% | -0.099R | 0.87 | -0.016R | 0.593 | 0/6 | FAIL | FAIL |
| Volatility 25 (1s) | rejection | 1019 | 26.3% | -0.101R | 0.86 | -0.191R | 0.733 | 0/6 | FAIL | FAIL |
| Volatility 75 (1s) | rejection | 1195 | 26.0% | -0.102R | 0.86 | +0.064R | 0.1 | 1/6 | FAIL | FAIL |
| Volatility 30 (1s) | rejection | 1030 | 25.8% | -0.116R | 0.84 | -0.197R | 0.713 | 2/6 | FAIL | FAIL |
| Volatility 90 (1s) | rejection | 1047 | 22.7% | -0.138R | 0.82 | +0.020R | 0.777 | 2/6 | FAIL | FAIL |

## Forex pairs and metals, 15m

Published rule 4/68 (6%) — limit 4/34 (12%), rejection 0/34 (0%). Strict rule 2/68 (3%) — limit 2/34 (6%), rejection 0/34 (0%).

| Market | Trigger | WF trades | Win | WF exp | WF PF | Lockbox exp | p vs random | Folds up | Verdict | Strict |
|---|---|---|---|---|---|---|---|---|---|---|
| AUD / CHF | limit | 29 | 55.2% | +0.689R | 2.66 | +1.664R | 0.0 | 4/6 | FAIL | FAIL |
| GBP / CHF | limit | 19 | 42.1% | +0.269R | 1.46 | -0.018R | 0.0 | 3/6 | FAIL | FAIL |
| NZD / USD | limit | 129 | 35.7% | +0.175R | 1.27 | -0.106R | 0.0 | 5/6 | FAIL | FAIL |
| EUR / AUD | limit | 432 | 33.1% | +0.085R | 1.13 | +0.186R | 0.0 | 4/6 | PASS | PASS |
| GBP / AUD | limit | 294 | 33.0% | +0.070R | 1.10 | +0.092R | 0.0 | 3/6 | PASS | FAIL |
| USD / SEK | limit | 77 | 33.8% | +0.057R | 1.09 | -0.306R | 0.0 | 5/6 | FAIL | FAIL |
| AUD / NZD | limit | 58 | 32.8% | +0.048R | 1.07 | -0.248R | 0.0 | 2/6 | FAIL | FAIL |
| Platinum / USD | limit | 553 | 30.0% | +0.020R | 1.03 | +0.310R | 0.0 | 3/6 | PASS | FAIL |
| USD / CAD | limit | 269 | 31.2% | +0.015R | 1.02 | +0.034R | 0.0 | 4/6 | PASS | PASS |
| GBP / CAD | limit | 160 | 31.2% | -0.006R | 0.99 | +0.356R | 0.0 | 4/6 | FAIL | FAIL |
| EUR / USD | limit | 505 | 29.9% | -0.008R | 0.99 | +0.330R | 0.0 | 3/6 | FAIL | FAIL |
| USD / MXN | limit | 203 | 30.5% | -0.009R | 0.99 | -0.298R | 0.0 | 3/6 | FAIL | FAIL |
| USD / CHF | limit | 160 | 30.6% | -0.016R | 0.98 | +0.198R | 0.0 | 2/6 | FAIL | FAIL |
| AUD / JPY | limit | 554 | 28.9% | -0.017R | 0.98 | -0.159R | 0.0 | 1/6 | FAIL | FAIL |
| GBP / USD | limit | 434 | 29.7% | -0.023R | 0.97 | +0.025R | 0.0 | 3/6 | FAIL | FAIL |
| Gold / USD | limit | 1029 | 24.7% | -0.023R | 0.97 | -0.017R | 0.407 | 2/6 | FAIL | FAIL |
| GBP / JPY | limit | 420 | 29.0% | -0.030R | 0.96 | -0.007R | 0.0 | 2/6 | FAIL | FAIL |
| CAD / JPY | limit | 105 | 30.5% | -0.034R | 0.95 | -0.290R | 0.0 | 3/6 | FAIL | FAIL |
| CHF / JPY | limit | 261 | 29.9% | -0.034R | 0.95 | -0.253R | 0.0 | 3/6 | FAIL | FAIL |
| AUD / USD | limit | 605 | 28.6% | -0.047R | 0.93 | -0.032R | 0.0 | 2/6 | FAIL | FAIL |
| Silver / USD | limit | 799 | 25.5% | -0.048R | 0.93 | +0.187R | 0.23 | 3/6 | FAIL | FAIL |
| EUR / NZD | limit | 235 | 29.4% | -0.054R | 0.92 | +0.283R | 0.0 | 3/6 | FAIL | FAIL |
| GBP / NZD | limit | 168 | 29.2% | -0.067R | 0.91 | +0.372R | 0.0 | 2/6 | FAIL | FAIL |
| NZD / JPY | limit | 195 | 30.3% | -0.073R | 0.90 | -0.266R | 0.0 | 1/6 | FAIL | FAIL |
| EUR / CAD | limit | 117 | 28.2% | -0.093R | 0.87 | -0.074R | 0.0 | 3/6 | FAIL | FAIL |
| AUD / CAD | limit | 173 | 27.7% | -0.097R | 0.87 | +0.134R | 0.0 | 3/6 | FAIL | FAIL |
| USD / NOK | limit | 45 | 26.7% | -0.111R | 0.84 | -0.413R | 0.0 | 2/6 | FAIL | FAIL |
| EUR / JPY | limit | 546 | 26.6% | -0.116R | 0.84 | -0.006R | 0.0 | 2/6 | FAIL | FAIL |
| EUR / GBP | limit | 119 | 27.7% | -0.136R | 0.81 | +0.518R | 0.0 | 3/6 | FAIL | FAIL |
| Palladium / USD | limit | 218 | 27.1% | -0.142R | 0.81 | +0.225R | 0.0 | 1/6 | FAIL | FAIL |
| USD / JPY | limit | 803 | 24.8% | -0.162R | 0.78 | -0.096R | 0.0 | 0/6 | FAIL | FAIL |
| EUR / CHF | limit | 150 | 25.3% | -0.165R | 0.78 | +0.196R | 0.0 | 2/6 | FAIL | FAIL |
| EUR / SEK | limit | 51 | 21.6% | -0.374R | 0.51 | -1.000R | 0.0 | 1/6 | FAIL | FAIL |
| USD / PLN | limit | 84 | 11.9% | -0.630R | 0.28 | +0.422R | 0.0 | 0/6 | FAIL | FAIL |
| GBP / JPY | rejection | 95 | 30.5% | +0.008R | 1.01 | -0.356R | 0.0 | 3/6 | FAIL | FAIL |
| AUD / CAD | rejection | 77 | 32.5% | -0.001R | 1.00 | -1.000R | 0.0 | 3/6 | FAIL | FAIL |
| EUR / USD | rejection | 108 | 30.6% | -0.023R | 0.97 | -0.088R | 0.0 | 3/6 | FAIL | FAIL |
| USD / MXN | rejection | 77 | 29.9% | -0.045R | 0.94 | -1.000R | 0.0 | 2/6 | FAIL | FAIL |
| Gold / USD | rejection | 937 | 26.5% | -0.086R | 0.88 | -0.101R | 0.153 | 2/6 | FAIL | FAIL |
| CHF / JPY | rejection | 80 | 27.5% | -0.100R | 0.86 | -0.371R | 0.0 | 2/6 | FAIL | FAIL |
| Platinum / USD | rejection | 244 | 27.0% | -0.124R | 0.83 | +0.336R | 0.0 | 0/6 | FAIL | FAIL |
| EUR / CAD | rejection | 48 | 29.2% | -0.136R | 0.81 | +0.345R | 0.0 | 2/6 | FAIL | FAIL |
| AUD / JPY | rejection | 260 | 26.5% | -0.148R | 0.80 | -0.348R | 0.043 | 1/6 | FAIL | FAIL |
| Silver / USD | rejection | 514 | 25.1% | -0.156R | 0.79 | +0.193R | 0.847 | 2/6 | FAIL | FAIL |
| USD / CAD | rejection | 93 | 26.9% | -0.159R | 0.78 | -0.115R | 0.0 | 1/6 | FAIL | FAIL |
| AUD / CHF | rejection | 18 | 33.3% | -0.181R | 0.73 | +2.100R | 0.0 | 2/6 | FAIL | FAIL |
| USD / PLN | rejection | 33 | 24.2% | -0.184R | 0.76 | -0.013R | 0.0 | 1/6 | FAIL | FAIL |
| GBP / USD | rejection | 158 | 24.7% | -0.209R | 0.72 | -0.493R | 0.0 | 2/6 | FAIL | FAIL |
| USD / JPY | rejection | 263 | 24.0% | -0.227R | 0.70 | -0.066R | 0.037 | 1/6 | FAIL | FAIL |
| AUD / USD | rejection | 116 | 24.1% | -0.257R | 0.66 | -0.649R | 0.007 | 2/6 | FAIL | FAIL |
| GBP / CAD | rejection | 37 | 21.6% | -0.273R | 0.65 | -1.000R | 0.0 | 1/6 | FAIL | FAIL |
| EUR / NZD | rejection | 81 | 22.2% | -0.296R | 0.62 | +0.033R | 0.03 | 1/6 | FAIL | FAIL |
| EUR / JPY | rejection | 205 | 21.5% | -0.304R | 0.61 | -0.010R | 0.003 | 1/6 | FAIL | FAIL |
| EUR / AUD | rejection | 155 | 21.3% | -0.329R | 0.58 | -0.147R | 0.0 | 0/6 | FAIL | FAIL |
| NZD / JPY | rejection | 94 | 23.4% | -0.333R | 0.57 | -0.357R | 0.007 | 1/6 | FAIL | FAIL |
| GBP / NZD | rejection | 56 | 21.4% | -0.355R | 0.55 | -0.130R | 0.0 | 0/6 | FAIL | FAIL |
| EUR / GBP | rejection | 35 | 20.0% | -0.368R | 0.53 | -1.000R | 0.0 | 0/6 | FAIL | FAIL |
| CAD / JPY | rejection | 30 | 23.3% | -0.408R | 0.47 | -0.779R | 0.013 | 2/6 | FAIL | FAIL |
| EUR / CHF | rejection | 42 | 23.8% | -0.424R | 0.43 | +1.372R | 0.0 | 2/6 | FAIL | FAIL |
| USD / SEK | rejection | 39 | 17.9% | -0.449R | 0.45 | -0.817R | 0.037 | 2/6 | FAIL | FAIL |
| NZD / USD | rejection | 49 | 16.3% | -0.472R | 0.43 | -0.259R | 0.0 | 0/6 | FAIL | FAIL |
| GBP / AUD | rejection | 93 | 17.2% | -0.478R | 0.42 | -0.328R | 0.06 | 1/6 | FAIL | FAIL |
| USD / CHF | rejection | 53 | 17.0% | -0.504R | 0.38 | +0.043R | 0.113 | 1/6 | FAIL | FAIL |
| EUR / SEK | rejection | 36 | 16.7% | -0.544R | 0.35 | +0.000R | 0.02 | 1/6 | FAIL | FAIL |
| AUD / NZD | rejection | 44 | 15.9% | -0.571R | 0.31 | -0.400R | 0.703 | 0/6 | FAIL | FAIL |
| Palladium / USD | rejection | 72 | 15.3% | -0.585R | 0.31 | -0.209R | 0.677 | 0/6 | FAIL | FAIL |
| USD / NOK | rejection | 19 | 10.5% | -0.599R | 0.29 | +0.633R | 0.11 | 0/6 | FAIL | FAIL |
| GBP / CHF | rejection | 24 | 12.5% | -0.682R | 0.22 | +0.651R | 0.14 | 0/6 | FAIL | FAIL |

## Deriv synthetics from the chart photos, 5m

Published rule 2/14 (14%) — limit 2/7 (29%), rejection 0/7 (0%). Strict rule 2/14 (14%) — limit 2/7 (29%), rejection 0/7 (0%).

| Market | Trigger | WF trades | Win | WF exp | WF PF | Lockbox exp | p vs random | Folds up | Verdict | Strict |
|---|---|---|---|---|---|---|---|---|---|---|
| Jump 10 | limit | 2341 | 27.0% | +0.076R | 1.10 | -0.009R | 0.0 | 4/6 | FAIL | FAIL |
| Volatility 10 (1s) | limit | 2778 | 26.7% | +0.056R | 1.08 | -0.007R | 0.003 | 5/6 | FAIL | FAIL |
| Volatility 30 (1s) | limit | 2649 | 26.1% | +0.041R | 1.06 | +0.023R | 0.007 | 4/6 | PASS | PASS |
| Volatility 75 (1s) | limit | 2558 | 25.8% | +0.031R | 1.04 | +0.044R | 0.0 | 4/6 | PASS | PASS |
| Volatility 15 (1s) | limit | 2471 | 25.3% | -0.002R | 1.00 | -0.037R | 0.157 | 3/6 | FAIL | FAIL |
| Volatility 90 (1s) | limit | 2688 | 24.6% | -0.025R | 0.97 | -0.006R | 0.163 | 2/6 | FAIL | FAIL |
| Volatility 25 (1s) | limit | 2594 | 23.6% | -0.066R | 0.91 | +0.175R | 0.607 | 0/6 | FAIL | FAIL |
| Volatility 10 (1s) | rejection | 2004 | 25.3% | +0.017R | 1.02 | -0.032R | 0.003 | 2/6 | FAIL | FAIL |
| Volatility 75 (1s) | rejection | 1363 | 27.9% | -0.015R | 0.98 | -0.053R | 0.197 | 2/6 | FAIL | FAIL |
| Jump 10 | rejection | 2222 | 20.0% | -0.020R | 0.97 | +0.026R | 0.17 | 2/6 | FAIL | FAIL |
| Volatility 30 (1s) | rejection | 1785 | 25.6% | -0.078R | 0.89 | +0.110R | 0.883 | 1/6 | FAIL | FAIL |
| Volatility 90 (1s) | rejection | 1463 | 26.2% | -0.087R | 0.88 | -0.050R | 0.877 | 1/6 | FAIL | FAIL |
| Volatility 25 (1s) | rejection | 1355 | 25.4% | -0.108R | 0.86 | +0.014R | 0.93 | 1/6 | FAIL | FAIL |
| Volatility 15 (1s) | rejection | 1403 | 25.2% | -0.115R | 0.85 | -0.251R | 0.98 | 1/6 | FAIL | FAIL |

## Forex pairs and metals, 5m

Published rule 0/2 (0%) — limit 0/2 (0%), rejection no tests. Strict rule 0/2 (0%) — limit 0/2 (0%), rejection no tests.

| Market | Trigger | WF trades | Win | WF exp | WF PF | Lockbox exp | p vs random | Folds up | Verdict | Strict |
|---|---|---|---|---|---|---|---|---|---|---|
| EUR / AUD | limit | 52 | 30.8% | -0.005R | 0.99 | -0.044R | 0.0 | 3/6 | FAIL | FAIL |
| GBP / AUD | limit | 52 | 23.1% | -0.305R | 0.60 | +1.198R | 0.0 | 4/6 | FAIL | FAIL |

## Ten years of Dukascopy hourly history, 1h

Published rule 0/16 (0%) — limit 0/8 (0%), rejection 0/8 (0%). Strict rule 0/16 (0%) — limit 0/8 (0%), rejection 0/8 (0%).

| Market | Trigger | WF trades | Win | WF exp | WF PF | Lockbox exp | p vs random | Folds up | Verdict | Strict |
|---|---|---|---|---|---|---|---|---|---|---|
| AUD / USD | limit | 3053 | 28.8% | -0.027R | 0.96 | -0.077R | 0.0 | 1/6 | FAIL | FAIL |
| USD / CAD | limit | 3027 | 29.0% | -0.029R | 0.96 | -0.161R | 0.0 | 2/6 | FAIL | FAIL |
| EUR / USD | limit | 3209 | 28.2% | -0.037R | 0.95 | -0.025R | 0.0 | 1/6 | FAIL | FAIL |
| EUR / AUD | limit | 1330 | 29.2% | -0.053R | 0.92 | +0.100R | 0.0 | 1/6 | FAIL | FAIL |
| GBP / USD | limit | 3413 | 27.0% | -0.072R | 0.90 | -0.059R | 0.0 | 1/6 | FAIL | FAIL |
| USD / JPY | limit | 2908 | 27.0% | -0.077R | 0.89 | -0.047R | 0.053 | 1/6 | FAIL | FAIL |
| Bitcoin / USD | limit | 4916 | 25.5% | -0.079R | 0.89 | -0.117R | 0.203 | 1/6 | FAIL | FAIL |
| Gold / USD | limit | 3331 | 26.2% | -0.100R | 0.86 | +0.048R | 0.137 | 0/6 | FAIL | FAIL |
| USD / CAD | rejection | 1350 | 29.6% | -0.104R | 0.85 | -0.228R | 0.023 | 0/6 | FAIL | FAIL |
| Bitcoin / USD | rejection | 2191 | 27.3% | -0.140R | 0.80 | -0.161R | 0.937 | 0/6 | FAIL | FAIL |
| AUD / USD | rejection | 1525 | 27.1% | -0.172R | 0.76 | -0.178R | 0.723 | 0/6 | FAIL | FAIL |
| USD / JPY | rejection | 1326 | 27.5% | -0.173R | 0.76 | -0.068R | 0.93 | 0/6 | FAIL | FAIL |
| EUR / USD | rejection | 1394 | 28.2% | -0.176R | 0.75 | -0.111R | 0.773 | 0/6 | FAIL | FAIL |
| GBP / USD | rejection | 1447 | 26.4% | -0.182R | 0.75 | -0.104R | 0.883 | 0/6 | FAIL | FAIL |
| Gold / USD | rejection | 1616 | 25.8% | -0.193R | 0.74 | -0.079R | 0.427 | 0/6 | FAIL | FAIL |
| EUR / AUD | rejection | 509 | 25.7% | -0.201R | 0.73 | -0.203R | 0.0 | 0/6 | FAIL | FAIL |

## Luck check: random walks matched to a pair, 15m

Published rule 2/40 (5%) — limit 2/40 (5%), rejection no tests. Strict rule 0/40 (0%) — limit 0/40 (0%), rejection no tests.

| Market | Trigger | WF trades | Win | WF exp | WF PF | Lockbox exp | p vs random | Folds up | Verdict | Strict |
|---|---|---|---|---|---|---|---|---|---|---|
| Random walk 60018 like frxEURAUD | limit | 429 | 32.6% | +0.051R | 1.08 | -0.256R | 0.0 | 4/6 | FAIL | FAIL |
| Random walk 60004 like frxGBPAUD | limit | 538 | 32.2% | +0.029R | 1.04 | -0.282R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60017 like frxEURAUD | limit | 694 | 31.3% | +0.016R | 1.02 | +0.031R | 0.0 | 3/6 | PASS | FAIL |
| Random walk 60004 like frxEURAUD | limit | 486 | 31.3% | +0.009R | 1.01 | -0.225R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60015 like frxEURAUD | limit | 657 | 30.6% | +0.004R | 1.01 | +0.007R | 0.0 | 3/6 | PASS | FAIL |
| Random walk 60000 like frxGBPAUD | limit | 298 | 31.2% | +0.003R | 1.00 | -0.019R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 60016 like frxEURAUD | limit | 737 | 30.8% | +0.000R | 1.00 | -0.123R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 60027 like frxEURAUD | limit | 381 | 31.2% | -0.003R | 1.00 | -0.152R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 60007 like frxEURAUD | limit | 757 | 30.5% | -0.004R | 0.99 | -0.136R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 60022 like frxEURAUD | limit | 353 | 31.2% | -0.004R | 0.99 | -0.022R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 60002 like frxGBPAUD | limit | 225 | 31.1% | -0.007R | 0.99 | -0.140R | 0.0 | 4/6 | FAIL | FAIL |
| Random walk 60008 like frxGBPAUD | limit | 339 | 31.6% | -0.010R | 0.99 | -0.115R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60001 like frxEURAUD | limit | 612 | 29.9% | -0.013R | 0.98 | -0.276R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60002 like frxEURAUD | limit | 367 | 30.8% | -0.015R | 0.98 | -0.122R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 60008 like frxEURAUD | limit | 784 | 30.0% | -0.018R | 0.97 | +0.044R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 60009 like frxGBPAUD | limit | 415 | 30.4% | -0.025R | 0.96 | -0.083R | 0.0 | 4/6 | FAIL | FAIL |
| Random walk 60001 like frxGBPAUD | limit | 265 | 30.2% | -0.029R | 0.96 | -0.439R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60029 like frxEURAUD | limit | 507 | 30.2% | -0.031R | 0.96 | -0.026R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60003 like frxEURAUD | limit | 426 | 30.0% | -0.036R | 0.95 | +0.288R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60003 like frxGBPAUD | limit | 351 | 30.5% | -0.039R | 0.94 | +0.213R | 0.0 | 4/6 | FAIL | FAIL |
| Random walk 60009 like frxEURAUD | limit | 599 | 29.7% | -0.040R | 0.94 | -0.199R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 60013 like frxEURAUD | limit | 643 | 29.5% | -0.044R | 0.94 | -0.100R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60019 like frxEURAUD | limit | 639 | 29.0% | -0.044R | 0.94 | -0.058R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60000 like frxEURAUD | limit | 726 | 28.9% | -0.046R | 0.94 | -0.114R | 0.0 | 1/6 | FAIL | FAIL |
| Random walk 60023 like frxEURAUD | limit | 589 | 29.4% | -0.046R | 0.94 | -0.082R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60011 like frxEURAUD | limit | 635 | 29.0% | -0.052R | 0.93 | -0.115R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60014 like frxEURAUD | limit | 524 | 29.2% | -0.054R | 0.92 | -0.125R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 60025 like frxEURAUD | limit | 734 | 29.0% | -0.060R | 0.92 | +0.037R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60012 like frxEURAUD | limit | 482 | 28.8% | -0.064R | 0.91 | -0.186R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60006 like frxEURAUD | limit | 451 | 28.8% | -0.075R | 0.89 | -0.018R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60020 like frxEURAUD | limit | 754 | 27.6% | -0.080R | 0.89 | +0.055R | 0.0 | 1/6 | FAIL | FAIL |
| Random walk 60010 like frxEURAUD | limit | 774 | 28.0% | -0.082R | 0.89 | +0.076R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60007 like frxGBPAUD | limit | 515 | 28.2% | -0.090R | 0.87 | +0.551R | 0.0 | 1/6 | FAIL | FAIL |
| Random walk 60006 like frxGBPAUD | limit | 276 | 27.9% | -0.102R | 0.86 | +0.053R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60028 like frxEURAUD | limit | 558 | 27.2% | -0.107R | 0.85 | -0.142R | 0.007 | 2/6 | FAIL | FAIL |
| Random walk 60026 like frxEURAUD | limit | 493 | 27.6% | -0.110R | 0.85 | -0.226R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60021 like frxEURAUD | limit | 538 | 27.1% | -0.112R | 0.85 | -0.142R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 60024 like frxEURAUD | limit | 497 | 26.2% | -0.158R | 0.79 | +0.082R | 0.0 | 1/6 | FAIL | FAIL |
| Random walk 60005 like frxEURAUD | limit | 562 | 25.6% | -0.177R | 0.76 | +0.018R | 0.0 | 1/6 | FAIL | FAIL |
| Random walk 60005 like frxGBPAUD | limit | 352 | 24.1% | -0.231R | 0.70 | -0.065R | 0.0 | 1/6 | FAIL | FAIL |

## Luck check: random walks matched to a pair, 5m

Published rule 2/30 (7%) — limit 2/30 (7%), rejection no tests. Strict rule 1/30 (3%) — limit 1/30 (3%), rejection no tests.

| Market | Trigger | WF trades | Win | WF exp | WF PF | Lockbox exp | p vs random | Folds up | Verdict | Strict |
|---|---|---|---|---|---|---|---|---|---|---|
| Random walk 50002 like frxEURAUD | limit | 75 | 40.0% | +0.269R | 1.45 | +0.338R | 0.0 | 4/6 | PASS | PASS |
| Random walk 50014 like frxEURAUD | limit | 117 | 37.6% | +0.192R | 1.31 | -0.031R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50027 like frxEURAUD | limit | 80 | 36.2% | +0.161R | 1.25 | -0.060R | 0.0 | 5/6 | FAIL | FAIL |
| Random walk 50000 like frxEURAUD | limit | 155 | 36.1% | +0.148R | 1.23 | -0.240R | 0.0 | 4/6 | FAIL | FAIL |
| Random walk 50020 like frxEURAUD | limit | 126 | 34.9% | +0.107R | 1.16 | +0.133R | 0.0 | 3/6 | PASS | FAIL |
| Random walk 50017 like frxEURAUD | limit | 124 | 34.7% | +0.104R | 1.16 | -0.243R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50001 like frxEURAUD | limit | 62 | 33.9% | +0.097R | 1.15 | -0.120R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50028 like frxEURAUD | limit | 55 | 34.5% | +0.083R | 1.13 | -0.153R | 0.0 | 4/6 | FAIL | FAIL |
| Random walk 50010 like frxEURAUD | limit | 168 | 32.7% | +0.048R | 1.07 | -0.027R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50005 like frxEURAUD | limit | 48 | 31.2% | +0.015R | 1.02 | -0.145R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50022 like frxEURAUD | limit | 81 | 30.9% | -0.008R | 0.99 | +0.256R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50013 like frxEURAUD | limit | 84 | 29.8% | -0.025R | 0.96 | +0.714R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50018 like frxEURAUD | limit | 60 | 30.0% | -0.039R | 0.94 | -0.615R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50015 like frxEURAUD | limit | 54 | 29.6% | -0.042R | 0.94 | +0.456R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50007 like frxEURAUD | limit | 134 | 29.9% | -0.046R | 0.93 | -0.288R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50016 like frxEURAUD | limit | 78 | 29.5% | -0.070R | 0.90 | +0.588R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 50019 like frxEURAUD | limit | 78 | 28.2% | -0.096R | 0.87 | -0.094R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50009 like frxEURAUD | limit | 209 | 27.8% | -0.099R | 0.86 | -0.058R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50004 like frxEURAUD | limit | 80 | 27.5% | -0.128R | 0.82 | -0.493R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50024 like frxEURAUD | limit | 115 | 27.0% | -0.134R | 0.82 | +0.105R | 0.0 | 0/6 | FAIL | FAIL |
| Random walk 50021 like frxEURAUD | limit | 150 | 26.7% | -0.148R | 0.80 | +0.130R | 0.0 | 1/6 | FAIL | FAIL |
| Random walk 50023 like frxEURAUD | limit | 88 | 26.1% | -0.172R | 0.77 | +0.380R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 50025 like frxEURAUD | limit | 90 | 25.6% | -0.180R | 0.76 | +0.005R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 50012 like frxEURAUD | limit | 190 | 25.8% | -0.187R | 0.75 | -0.280R | 0.0 | 1/6 | FAIL | FAIL |
| Random walk 50008 like frxEURAUD | limit | 80 | 25.0% | -0.188R | 0.75 | +1.241R | 0.0 | 2/6 | FAIL | FAIL |
| Random walk 50029 like frxEURAUD | limit | 100 | 24.0% | -0.227R | 0.70 | +0.165R | 0.0 | 3/6 | FAIL | FAIL |
| Random walk 50003 like frxEURAUD | limit | 87 | 21.8% | -0.324R | 0.59 | -0.299R | 0.0 | 1/6 | FAIL | FAIL |
| Random walk 50026 like frxEURAUD | limit | 96 | 18.8% | -0.398R | 0.51 | -0.531R | 0.0 | 1/6 | FAIL | FAIL |
| Random walk 50006 like frxEURAUD | limit | 106 | 18.9% | -0.408R | 0.50 | -0.204R | 0.287 | 1/6 | FAIL | FAIL |
| Random walk 50011 like frxEURAUD | limit | 56 | 17.9% | -0.438R | 0.47 | -0.132R | 0.003 | 0/6 | FAIL | FAIL |

## Luck check: random walks at synthetic volatility, 15m

Published rule 4/40 (10%) — limit 4/20 (20%), rejection 0/20 (0%). Strict rule 3/40 (8%) — limit 3/20 (15%), rejection 0/20 (0%).

| Market | Trigger | WF trades | Win | WF exp | WF PF | Lockbox exp | p vs random | Folds up | Verdict | Strict |
|---|---|---|---|---|---|---|---|---|---|---|
| Random walk 60004 | limit | 1707 | 27.8% | +0.108R | 1.15 | -0.025R | 0.0 | 4/6 | FAIL | FAIL |
| Random walk 60000 | limit | 1653 | 27.4% | +0.090R | 1.12 | -0.053R | 0.0 | 5/6 | FAIL | FAIL |
| Random walk 60000 | limit | 1612 | 27.0% | +0.076R | 1.10 | -0.036R | 0.01 | 3/6 | FAIL | FAIL |
| Random walk 60002 | limit | 1741 | 27.4% | +0.065R | 1.09 | +0.022R | 0.0 | 5/6 | PASS | PASS |
| Random walk 60003 | limit | 1688 | 26.6% | +0.059R | 1.08 | -0.012R | 0.013 | 3/6 | FAIL | FAIL |
| Random walk 60001 | limit | 1601 | 26.4% | +0.047R | 1.06 | +0.035R | 0.043 | 5/6 | PASS | PASS |
| Random walk 60006 | limit | 1677 | 27.1% | +0.039R | 1.05 | +0.133R | 0.0 | 4/6 | PASS | PASS |
| Random walk 60004 | limit | 1756 | 25.9% | +0.031R | 1.04 | +0.094R | 0.07 | 3/6 | FAIL | FAIL |
| Random walk 60007 | limit | 1888 | 26.1% | +0.020R | 1.03 | -0.108R | 0.05 | 5/6 | FAIL | FAIL |
| Random walk 60007 | limit | 1856 | 26.1% | +0.020R | 1.03 | -0.073R | 0.04 | 3/6 | FAIL | FAIL |
| Random walk 60002 | limit | 1731 | 26.2% | +0.017R | 1.02 | +0.055R | 0.003 | 3/6 | PASS | FAIL |
| Random walk 60009 | limit | 1621 | 26.1% | +0.014R | 1.02 | +0.018R | 0.093 | 3/6 | FAIL | FAIL |
| Random walk 60006 | limit | 1809 | 26.3% | +0.004R | 1.01 | -0.016R | 0.02 | 3/6 | FAIL | FAIL |
| Random walk 60003 | limit | 1679 | 25.3% | +0.002R | 1.00 | +0.055R | 0.13 | 2/6 | FAIL | FAIL |
| Random walk 60001 | limit | 1665 | 25.3% | -0.003R | 1.00 | -0.021R | 0.41 | 4/6 | FAIL | FAIL |
| Random walk 60009 | limit | 1687 | 25.8% | -0.004R | 1.00 | +0.117R | 0.27 | 3/6 | FAIL | FAIL |
| Random walk 60008 | limit | 1896 | 24.7% | -0.030R | 0.96 | +0.156R | 0.26 | 3/6 | FAIL | FAIL |
| Random walk 60008 | limit | 1881 | 24.0% | -0.055R | 0.93 | +0.127R | 0.567 | 0/6 | FAIL | FAIL |
| Random walk 60005 | limit | 1872 | 23.9% | -0.064R | 0.92 | -0.051R | 0.647 | 1/6 | FAIL | FAIL |
| Random walk 60005 | limit | 1883 | 23.0% | -0.101R | 0.87 | -0.011R | 0.937 | 0/6 | FAIL | FAIL |
| Random walk 60004 | rejection | 1143 | 29.6% | +0.029R | 1.04 | -0.046R | 0.077 | 4/6 | FAIL | FAIL |
| Random walk 60002 | rejection | 1221 | 25.1% | +0.016R | 1.02 | -0.116R | 0.0 | 4/6 | FAIL | FAIL |
| Random walk 60001 | rejection | 1356 | 22.1% | -0.003R | 1.00 | -0.204R | 0.41 | 4/6 | FAIL | FAIL |
| Random walk 60009 | rejection | 951 | 28.9% | -0.015R | 0.98 | -0.145R | 0.057 | 3/6 | FAIL | FAIL |
| Random walk 60004 | rejection | 1199 | 28.4% | -0.017R | 0.98 | +0.012R | 0.003 | 3/6 | FAIL | FAIL |
| Random walk 60003 | rejection | 1260 | 28.3% | -0.033R | 0.95 | -0.134R | 0.02 | 2/6 | FAIL | FAIL |
| Random walk 60000 | rejection | 790 | 27.5% | -0.036R | 0.95 | -0.113R | 0.617 | 3/6 | FAIL | FAIL |
| Random walk 60001 | rejection | 1024 | 27.0% | -0.066R | 0.91 | -0.174R | 0.863 | 0/6 | FAIL | FAIL |
| Random walk 60002 | rejection | 1748 | 19.3% | -0.069R | 0.91 | -0.189R | 0.183 | 0/6 | FAIL | FAIL |
| Random walk 60007 | rejection | 1695 | 18.9% | -0.069R | 0.92 | -0.288R | 0.233 | 2/6 | FAIL | FAIL |
| Random walk 60008 | rejection | 1740 | 19.3% | -0.071R | 0.91 | -0.052R | 0.13 | 1/6 | FAIL | FAIL |
| Random walk 60007 | rejection | 1665 | 18.1% | -0.075R | 0.91 | -0.307R | 0.333 | 1/6 | FAIL | FAIL |
| Random walk 60009 | rejection | 1435 | 24.7% | -0.080R | 0.89 | -0.054R | 0.813 | 1/6 | FAIL | FAIL |
| Random walk 60005 | rejection | 1044 | 26.8% | -0.082R | 0.89 | -0.068R | 0.653 | 1/6 | FAIL | FAIL |
| Random walk 60000 | rejection | 1183 | 25.5% | -0.087R | 0.88 | -0.101R | 0.617 | 1/6 | FAIL | FAIL |
| Random walk 60006 | rejection | 986 | 27.0% | -0.088R | 0.88 | -0.162R | 0.047 | 1/6 | FAIL | FAIL |
| Random walk 60008 | rejection | 1345 | 23.6% | -0.095R | 0.88 | -0.057R | 0.613 | 1/6 | FAIL | FAIL |
| Random walk 60006 | rejection | 986 | 26.7% | -0.099R | 0.86 | -0.176R | 0.043 | 0/6 | FAIL | FAIL |
| Random walk 60003 | rejection | 915 | 25.7% | -0.117R | 0.84 | -0.017R | 0.963 | 1/6 | FAIL | FAIL |
| Random walk 60005 | rejection | 1133 | 25.1% | -0.147R | 0.80 | -0.168R | 0.537 | 1/6 | FAIL | FAIL |
