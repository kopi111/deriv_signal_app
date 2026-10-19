import 'dart:math' as math;

import 'candle.dart';

/// Bar-for-bar ports of research/indicators.py. EMAs seed on the first
/// value; RSI, ATR and ADX use Wilder smoothing (alpha = 1 / period).
/// Warm-up values that pandas leaves as NaN are NaN here too, so every
/// comparison against them is false in both languages.
class Indicators {
  static List<double> ema(List<double> values, int period) =>
      _smooth(values, 2 / (period + 1));

  static List<double> wilder(List<double> values, int period) =>
      _smooth(values, 1 / period);

  static List<double> rsi(List<double> closes, int period) {
    final changes = [0.0, for (var i = 1; i < closes.length; i++) closes[i] - closes[i - 1]];
    final gains = wilder([for (final c in changes) math.max(c, 0.0)], period);
    final losses = wilder([for (final c in changes) math.max(-c, 0.0)], period);
    return [
      for (var i = 0; i < closes.length; i++)
        losses[i] == 0 ? 100.0 : 100 - 100 / (1 + gains[i] / losses[i]),
    ];
  }

  static List<double> trueRange(List<Candle> candles) => [
        for (var i = 0; i < candles.length; i++)
          _trueRangeAt(candles[i], i == 0 ? candles[i].close : candles[i - 1].close),
      ];

  static List<double> atr(List<Candle> candles, int period) =>
      wilder(trueRange(candles), period);

  static List<double> adx(List<Candle> candles, int period) {
    final plusMoves = <double>[0];
    final minusMoves = <double>[0];
    for (var i = 1; i < candles.length; i++) {
      final up = candles[i].high - candles[i - 1].high;
      final down = candles[i - 1].low - candles[i].low;
      plusMoves.add(up > down && up > 0 ? up : 0);
      minusMoves.add(down > up && down > 0 ? down : 0);
    }
    final rangeAverage = atr(candles, period);
    final plusSmoothed = wilder(plusMoves, period);
    final minusSmoothed = wilder(minusMoves, period);
    final directional = [
      for (var i = 0; i < candles.length; i++)
        _directionalSpread(plusSmoothed[i], minusSmoothed[i], rangeAverage[i]),
    ];
    return wilder(directional, period);
  }

  static (List<double>, List<double>) macd(List<double> closes) {
    final fast = ema(closes, 12);
    final slow = ema(closes, 26);
    final line = [for (var i = 0; i < closes.length; i++) fast[i] - slow[i]];
    return (line, ema(line, 9));
  }

  static (List<double>, List<double>, List<double>) bollinger(
      List<double> closes, int period, double width) {
    final lower = <double>[];
    final middle = <double>[];
    final upper = <double>[];
    for (var i = 0; i < closes.length; i++) {
      if (i + 1 < period) {
        lower.add(double.nan);
        middle.add(double.nan);
        upper.add(double.nan);
        continue;
      }
      final window = closes.sublist(i + 1 - period, i + 1);
      final mean = window.reduce((a, b) => a + b) / period;
      final variance =
          window.map((v) => (v - mean) * (v - mean)).reduce((a, b) => a + b) / period;
      final deviation = math.sqrt(variance);
      lower.add(mean - width * deviation);
      middle.add(mean);
      upper.add(mean + width * deviation);
    }
    return (lower, middle, upper);
  }

  static List<double> priorHighest(List<double> highs, int period) =>
      _priorExtreme(highs, period, math.max);

  static List<double> priorLowest(List<double> lows, int period) =>
      _priorExtreme(lows, period, math.min);

  static List<double> _smooth(List<double> values, double alpha) {
    final smoothed = <double>[];
    for (var i = 0; i < values.length; i++) {
      smoothed.add(i == 0 ? values[0] : alpha * values[i] + (1 - alpha) * smoothed[i - 1]);
    }
    return smoothed;
  }

  static double _trueRangeAt(Candle candle, double previousClose) => [
        candle.high - candle.low,
        (candle.high - previousClose).abs(),
        (candle.low - previousClose).abs(),
      ].reduce(math.max);

  static double _directionalSpread(double plus, double minus, double range) {
    if (range == 0) return 0;
    final plusIndex = 100 * plus / range;
    final minusIndex = 100 * minus / range;
    final total = plusIndex + minusIndex;
    return total == 0 ? 0 : 100 * (plusIndex - minusIndex).abs() / total;
  }

  static List<double> _priorExtreme(
      List<double> values, int period, double Function(double, double) pick) {
    return [
      for (var i = 0; i < values.length; i++)
        i < period ? double.nan : values.sublist(i - period, i).reduce(pick),
    ];
  }
}
