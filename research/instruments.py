"""Instruments under test. Spreads are conservative estimates of Deriv's
quoted spread, charged once per trade in price units."""

import numpy as np

SYNTHETIC_SPREAD_ATR_SHARE = 0.05

INSTRUMENTS = [
    {"symbol": "frxXAUUSD", "name": "Gold / USD", "group": "Metals", "spread": 0.40},
    {"symbol": "frxXAGUSD", "name": "Silver / USD", "group": "Metals", "spread": 0.035},
    {"symbol": "frxEURUSD", "name": "EUR / USD", "group": "Forex", "spread": 0.00015},
    {"symbol": "frxGBPUSD", "name": "GBP / USD", "group": "Forex", "spread": 0.0002},
    {"symbol": "frxAUDUSD", "name": "AUD / USD", "group": "Forex", "spread": 0.00015},
    {"symbol": "frxUSDJPY", "name": "USD / JPY", "group": "Forex", "spread": 0.015},
    {"symbol": "frxGBPJPY", "name": "GBP / JPY", "group": "Forex", "spread": 0.03},
    {"symbol": "frxUSDCAD", "name": "USD / CAD", "group": "Forex", "spread": 0.0002},
    {"symbol": "frxUSDCHF", "name": "USD / CHF", "group": "Forex", "spread": 0.0002},
    {"symbol": "frxNZDUSD", "name": "NZD / USD", "group": "Forex", "spread": 0.0002},
    {"symbol": "frxEURJPY", "name": "EUR / JPY", "group": "Forex", "spread": 0.02},
    {"symbol": "frxAUDJPY", "name": "AUD / JPY", "group": "Forex", "spread": 0.02},
    {"symbol": "frxEURGBP", "name": "EUR / GBP", "group": "Forex", "spread": 0.00015},
    {"symbol": "cryBTCUSD", "name": "Bitcoin / USD", "group": "Crypto", "spread_price_share": 0.0005},
    {"symbol": "R_75", "name": "Volatility 75", "group": "Synthetic", "synthetic": True},
    {"symbol": "R_100", "name": "Volatility 100", "group": "Synthetic", "synthetic": True},
    {"symbol": "1HZ100V", "name": "Volatility 100 (1s)", "group": "Synthetic", "synthetic": True},
    {"symbol": "stpRNG", "name": "Step Index", "group": "Synthetic", "synthetic": True},
    {"symbol": "1HZ75V", "name": "Volatility 75 (1s)", "group": "Synthetic", "synthetic": True},
    {"symbol": "JD10", "name": "Jump 10", "group": "Synthetic", "synthetic": True},
    {"symbol": "JD25", "name": "Jump 25", "group": "Synthetic", "synthetic": True},
    {"symbol": "JD50", "name": "Jump 50", "group": "Synthetic", "synthetic": True},
    {"symbol": "JD75", "name": "Jump 75", "group": "Synthetic", "synthetic": True},
    {"symbol": "JD100", "name": "Jump 100", "group": "Synthetic", "synthetic": True},
    {"symbol": "1HZ10V", "name": "Volatility 10 (1s)", "group": "Synthetic", "synthetic": True},
    {"symbol": "1HZ15V", "name": "Volatility 15 (1s)", "group": "Synthetic", "synthetic": True},
    {"symbol": "1HZ25V", "name": "Volatility 25 (1s)", "group": "Synthetic", "synthetic": True},
    {"symbol": "1HZ30V", "name": "Volatility 30 (1s)", "group": "Synthetic", "synthetic": True},
    {"symbol": "1HZ50V", "name": "Volatility 50 (1s)", "group": "Synthetic", "synthetic": True},
    {"symbol": "1HZ90V", "name": "Volatility 90 (1s)", "group": "Synthetic", "synthetic": True},
    {"symbol": "1HZ150V", "name": "Volatility 150 (1s)", "group": "Synthetic", "synthetic": True},
    {"symbol": "1HZ250V", "name": "Volatility 250 (1s)", "group": "Synthetic", "synthetic": True},
    {"symbol": "R_10", "name": "Volatility 10", "group": "Synthetic", "synthetic": True},
    {"symbol": "R_25", "name": "Volatility 25", "group": "Synthetic", "synthetic": True},
    {"symbol": "R_50", "name": "Volatility 50", "group": "Synthetic", "synthetic": True},
    {"symbol": "frxEURAUD", "name": "EUR / AUD", "group": "Forex", "spread": 0.0003},
    {"symbol": "frxEURCAD", "name": "EUR / CAD", "group": "Forex", "spread": 0.0003},
    {"symbol": "frxEURCHF", "name": "EUR / CHF", "group": "Forex", "spread": 0.0002},
    {"symbol": "frxEURNZD", "name": "EUR / NZD", "group": "Forex", "spread": 0.0004},
    {"symbol": "frxGBPAUD", "name": "GBP / AUD", "group": "Forex", "spread": 0.0004},
    {"symbol": "frxGBPCAD", "name": "GBP / CAD", "group": "Forex", "spread": 0.0004},
    {"symbol": "frxGBPCHF", "name": "GBP / CHF", "group": "Forex", "spread": 0.0004},
    {"symbol": "frxGBPNZD", "name": "GBP / NZD", "group": "Forex", "spread": 0.0005},
    {"symbol": "frxAUDCAD", "name": "AUD / CAD", "group": "Forex", "spread": 0.0003},
    {"symbol": "frxAUDCHF", "name": "AUD / CHF", "group": "Forex", "spread": 0.0003},
    {"symbol": "frxAUDNZD", "name": "AUD / NZD", "group": "Forex", "spread": 0.0003},
    {"symbol": "frxNZDJPY", "name": "NZD / JPY", "group": "Forex", "spread": 0.03},
    {"symbol": "frxCADJPY", "name": "CAD / JPY", "group": "Forex", "spread": 0.03},
    {"symbol": "frxCHFJPY", "name": "CHF / JPY", "group": "Forex", "spread": 0.04},
    {"symbol": "frxEURSEK", "name": "EUR / SEK", "group": "Forex", "spread": 0.008},
    {"symbol": "frxUSDMXN", "name": "USD / MXN", "group": "Forex", "spread": 0.006},
    {"symbol": "frxUSDSEK", "name": "USD / SEK", "group": "Forex", "spread": 0.006},
    {"symbol": "frxUSDNOK", "name": "USD / NOK", "group": "Forex", "spread": 0.006},
    {"symbol": "frxUSDPLN", "name": "USD / PLN", "group": "Forex", "spread": 0.004},
    {"symbol": "frxXPTUSD", "name": "Platinum / USD", "group": "Metals", "spread": 2.0},
    {"symbol": "frxXPDUSD", "name": "Palladium / USD", "group": "Metals", "spread": 3.0},
]


def spread_for(instrument, bars):
    if instrument.get("synthetic"):
        return SYNTHETIC_SPREAD_ATR_SHARE * float(np.nanmedian(bars["atr"]))
    if "spread_price_share" in instrument:
        return instrument["spread_price_share"] * float(np.nanmedian(bars["close"]))
    return instrument["spread"]

