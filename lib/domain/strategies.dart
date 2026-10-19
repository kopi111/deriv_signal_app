import 'market_series.dart';
import 'setup_check.dart';

/// Dart twins of research/strategies.py. Each rule is written once as a
/// list of conditions, so the checklist the app shows IS the entry rule.
abstract class Strategy {
  const Strategy(this.params);

  final Map<String, num> params;

  String get id;
  String get title;
  String get plainEnglish;

  SetupCheck check(MarketSeries series, int bar, TradeDirection direction);

  /// +1 buy, -1 sell, 0 nothing — same contract as the Python signals.
  int signalAt(MarketSeries series, int bar) {
    final buy = check(series, bar, TradeDirection.buy).triggered;
    final sell = check(series, bar, TradeDirection.sell).triggered;
    if (buy == sell) return 0;
    return buy ? 1 : -1;
  }

  int intParam(String name) => params[name]!.toInt();

  static Strategy create(String id, Map<String, num> params) => switch (id) {
        'trend_pullback' => TrendPullback(params),
        'ema_bounce' => EmaBounce(params),
        'donchian_breakout' => DonchianBreakout(params),
        'rsi2_reversion' => Rsi2Reversion(params),
        'bollinger_reversion' => BollingerReversion(params),
        'macd_pullback' => MacdPullback(params),
        'ema_cross' => EmaCross(params),
        'legacy_rsi_crossback' => RsiCrossback(params),
        'legacy_ema_cross' => QuickTargetEmaCross(params),
        'legacy_macd_cross' => MacdCross(params),
        _ => throw ArgumentError.value(id, 'id', 'Unknown strategy'),
      };
}

bool crossedAbove(List<double> line, int bar, double level) =>
    bar > 0 && line[bar - 1] < level && line[bar] >= level;

bool crossedBelow(List<double> line, int bar, double level) =>
    bar > 0 && line[bar - 1] > level && line[bar] <= level;

bool gapCrossedAbove(List<double> line, List<double> reference, int bar) =>
    bar > 0 && line[bar - 1] - reference[bar - 1] < 0 && line[bar] - reference[bar] >= 0;

bool gapCrossedBelow(List<double> line, List<double> reference, int bar) =>
    bar > 0 && line[bar - 1] - reference[bar - 1] > 0 && line[bar] - reference[bar] <= 0;

String price(double value) {
  final magnitude = value.abs();
  if (magnitude < 10) return value.toStringAsFixed(5);
  if (magnitude < 1000) return value.toStringAsFixed(3);
  return value.toStringAsFixed(2);
}

String oneDecimal(double value) => value.toStringAsFixed(1);

List<Condition> trendConditions(MarketSeries series, int bar, TradeDirection direction) {
  final close = series.closes[bar];
  final ema50 = series.ema(50)[bar];
  final ema200 = series.ema(200)[bar];
  final isBuy = direction == TradeDirection.buy;
  return [
    Condition(
      isBuy ? 'Price above the 200 EMA' : 'Price below the 200 EMA',
      isBuy ? close > ema200 : close < ema200,
      'price ${price(close)} vs EMA200 ${price(ema200)}',
    ),
    Condition(
      isBuy ? '50 EMA above 200 EMA (uptrend)' : '50 EMA below 200 EMA (downtrend)',
      isBuy ? ema50 > ema200 : ema50 < ema200,
      'EMA50 ${price(ema50)} vs EMA200 ${price(ema200)}',
    ),
  ];
}

class TrendPullback extends Strategy {
  const TrendPullback(super.params);

  @override
  String get id => 'trend_pullback';
  @override
  String get title => 'Trend pullback';
  @override
  String get plainEnglish =>
      'Trade with the main trend after a dip. The trend must be clear on the 50 and '
      '200 EMAs, then RSI(14) has to turn back up out of the pullback zone.';

  @override
  SetupCheck check(MarketSeries series, int bar, TradeDirection direction) {
    final rsi = series.rsi(14);
    final level = direction == TradeDirection.buy
        ? params['rsi_level']!.toDouble()
        : 100 - params['rsi_level']!.toDouble();
    final turned = direction == TradeDirection.buy
        ? crossedAbove(rsi, bar, level)
        : crossedBelow(rsi, bar, level);
    return SetupCheck(direction, [
      ...trendConditions(series, bar, direction),
      Condition(
        direction == TradeDirection.buy
            ? 'RSI(14) turned up through ${oneDecimal(level)}'
            : 'RSI(14) turned down through ${oneDecimal(level)}',
        turned,
        bar > 0 ? 'RSI ${oneDecimal(rsi[bar - 1])} → ${oneDecimal(rsi[bar])}' : '',
      ),
    ]);
  }
}

class EmaBounce extends Strategy {
  const EmaBounce(super.params);

  @override
  String get id => 'ema_bounce';
  @override
  String get title => 'EMA bounce';
  @override
  String get plainEnglish =>
      'In a trend, price dips into the moving average and the candle closes back '
      'on the trend side. That shows buyers (or sellers) defending the level.';

  @override
  SetupCheck check(MarketSeries series, int bar, TradeDirection direction) {
    final period = intParam('touch_period');
    final line = series.ema(period)[bar];
    final candle = series.candles[bar];
    final isBuy = direction == TradeDirection.buy;
    return SetupCheck(direction, [
      ...trendConditions(series, bar, direction),
      Condition(
        'Candle touched the $period EMA',
        isBuy ? candle.low <= line : candle.high >= line,
        '${isBuy ? 'low' : 'high'} ${price(isBuy ? candle.low : candle.high)} vs EMA$period ${price(line)}',
      ),
      Condition(
        isBuy ? 'Closed back above it, green candle' : 'Closed back below it, red candle',
        isBuy
            ? candle.close > line && candle.close > candle.open
            : candle.close < line && candle.close < candle.open,
        'open ${price(candle.open)} close ${price(candle.close)}',
      ),
    ]);
  }
}

class DonchianBreakout extends Strategy {
  const DonchianBreakout(super.params);

  @override
  String get id => 'donchian_breakout';
  @override
  String get title => 'Channel breakout';
  @override
  String get plainEnglish =>
      'Price closes beyond the highest high (or lowest low) of recent candles '
      'while ADX confirms a real trend and the 200 EMA agrees with the direction.';

  @override
  SetupCheck check(MarketSeries series, int bar, TradeDirection direction) {
    final period = intParam('period');
    final adxMin = params['adx_min']!.toDouble();
    final isBuy = direction == TradeDirection.buy;
    final boundary = isBuy ? series.priorHighest(period) : series.priorLowest(period);
    final closes = series.closes;
    final adx = series.adx(14)[bar];
    final ema200 = series.ema(200)[bar];
    return SetupCheck(direction, [
      Condition(
        isBuy ? 'Closed above the $period-candle high' : 'Closed below the $period-candle low',
        isBuy ? gapCrossedAbove(closes, boundary, bar) : gapCrossedBelow(closes, boundary, bar),
        'close ${price(closes[bar])} vs ${isBuy ? 'high' : 'low'} ${price(boundary[bar])}',
      ),
      Condition('ADX above ${adxMin.toStringAsFixed(0)} (trending)', adx > adxMin,
          'ADX ${oneDecimal(adx)}'),
      Condition(
        isBuy ? 'Price above the 200 EMA' : 'Price below the 200 EMA',
        isBuy ? closes[bar] > ema200 : closes[bar] < ema200,
        'EMA200 ${price(ema200)}',
      ),
    ]);
  }
}

class Rsi2Reversion extends Strategy {
  const Rsi2Reversion(super.params);

  @override
  String get id => 'rsi2_reversion';
  @override
  String get title => 'RSI(2) snap-back';
  @override
  String get plainEnglish =>
      'A short, sharp move against the main trend usually snaps back. The trade '
      'follows the 200 EMA direction when the 2-period RSI hits an extreme.';

  @override
  SetupCheck check(MarketSeries series, int bar, TradeDirection direction) {
    final oversold = params['oversold']!.toDouble();
    final rsi = series.rsi(2);
    final close = series.closes[bar];
    final ema200 = series.ema(200)[bar];
    final isBuy = direction == TradeDirection.buy;
    return SetupCheck(direction, [
      Condition(
        isBuy ? 'Price above the 200 EMA' : 'Price below the 200 EMA',
        isBuy ? close > ema200 : close < ema200,
        'price ${price(close)} vs EMA200 ${price(ema200)}',
      ),
      Condition(
        isBuy
            ? 'RSI(2) dropped below ${oversold.toStringAsFixed(0)}'
            : 'RSI(2) rose above ${(100 - oversold).toStringAsFixed(0)}',
        isBuy ? crossedBelow(rsi, bar, oversold) : crossedAbove(rsi, bar, 100 - oversold),
        bar > 0 ? 'RSI(2) ${oneDecimal(rsi[bar - 1])} → ${oneDecimal(rsi[bar])}' : '',
      ),
    ]);
  }
}

class BollingerReversion extends Strategy {
  const BollingerReversion(super.params);

  @override
  String get id => 'bollinger_reversion';
  @override
  String get title => 'Range fade';
  @override
  String get plainEnglish =>
      'When the market is ranging (low ADX), price that stretches outside the '
      'Bollinger band and closes back inside tends to return toward the middle.';

  @override
  SetupCheck check(MarketSeries series, int bar, TradeDirection direction) {
    final adxMax = params['adx_max']!.toDouble();
    final isBuy = direction == TradeDirection.buy;
    final band = isBuy ? series.bollingerLower(20, 2) : series.bollingerUpper(20, 2);
    final closes = series.closes;
    final adx = series.adx(14)[bar];
    return SetupCheck(direction, [
      Condition('ADX below ${adxMax.toStringAsFixed(0)} (ranging)', adx < adxMax,
          'ADX ${oneDecimal(adx)}'),
      Condition(
        isBuy ? 'Closed back above the lower band' : 'Closed back below the upper band',
        isBuy ? gapCrossedAbove(closes, band, bar) : gapCrossedBelow(closes, band, bar),
        'close ${price(closes[bar])} vs band ${price(band[bar])}',
      ),
    ]);
  }
}

class MacdPullback extends Strategy {
  const MacdPullback(super.params);

  @override
  String get id => 'macd_pullback';
  @override
  String get title => 'MACD pullback turn';
  @override
  String get plainEnglish =>
      'In a trend, MACD dips below zero during the pullback. The entry is the '
      'moment the MACD line crosses its signal line back in the trend direction.';

  @override
  SetupCheck check(MarketSeries series, int bar, TradeDirection direction) {
    final period = intParam('trend_period');
    final trendLine = series.ema(period)[bar];
    final line = series.macdLine;
    final signal = series.macdSignal;
    final close = series.closes[bar];
    final isBuy = direction == TradeDirection.buy;
    return SetupCheck(direction, [
      Condition(
        isBuy ? 'Price above the $period EMA' : 'Price below the $period EMA',
        isBuy ? close > trendLine : close < trendLine,
        'price ${price(close)} vs EMA$period ${price(trendLine)}',
      ),
      Condition(
        isBuy ? 'MACD below zero (pullback)' : 'MACD above zero (pullback)',
        isBuy ? line[bar] < 0 : line[bar] > 0,
        'MACD ${price(line[bar])}',
      ),
      Condition(
        isBuy ? 'MACD crossed up over its signal' : 'MACD crossed down under its signal',
        isBuy ? gapCrossedAbove(line, signal, bar) : gapCrossedBelow(line, signal, bar),
        'MACD ${price(line[bar])} vs signal ${price(signal[bar])}',
      ),
    ]);
  }
}

class EmaCross extends Strategy {
  const EmaCross(super.params);

  @override
  String get id => 'ema_cross';
  @override
  String get title => 'EMA crossover';
  @override
  String get plainEnglish =>
      'The fast moving average crosses the slow one, signalling a change of trend.';

  @override
  SetupCheck check(MarketSeries series, int bar, TradeDirection direction) {
    final fast = intParam('fast');
    final slow = intParam('slow');
    final fastLine = series.ema(fast);
    final slowLine = series.ema(slow);
    final isBuy = direction == TradeDirection.buy;
    return SetupCheck(direction, [
      Condition(
        isBuy ? '$fast EMA crossed above $slow EMA' : '$fast EMA crossed below $slow EMA',
        isBuy ? gapCrossedAbove(fastLine, slowLine, bar) : gapCrossedBelow(fastLine, slowLine, bar),
        'EMA$fast ${price(fastLine[bar])} vs EMA$slow ${price(slowLine[bar])}',
      ),
    ]);
  }
}

/// From the old dashboard: RSI leaves an extreme and crosses back.
class RsiCrossback extends Strategy {
  const RsiCrossback(super.params);

  @override
  String get id => 'legacy_rsi_crossback';
  @override
  String get title => 'RSI cross-back';
  @override
  String get plainEnglish =>
      'From your old dashboard. When RSI has been oversold (or overbought) and crosses '
      'back, price is expected to bounce. Uses a wide stop and a quick, small target.';

  @override
  SetupCheck check(MarketSeries series, int bar, TradeDirection direction) {
    final period = intParam('period');
    final rsi = series.rsi(period);
    final isBuy = direction == TradeDirection.buy;
    final level = (isBuy ? params['oversold']! : params['overbought']!).toDouble();
    return SetupCheck(direction, [
      Condition(
        isBuy
            ? 'RSI($period) crossed back up through ${level.toStringAsFixed(0)}'
            : 'RSI($period) crossed back down through ${level.toStringAsFixed(0)}',
        isBuy ? crossedAbove(rsi, bar, level) : crossedBelow(rsi, bar, level),
        bar > 0 ? 'RSI ${oneDecimal(rsi[bar - 1])} → ${oneDecimal(rsi[bar])}' : '',
      ),
    ]);
  }
}

/// From the old dashboard: EMA crossover with a wide stop and a quick target.
class QuickTargetEmaCross extends EmaCross {
  const QuickTargetEmaCross(super.params);

  @override
  String get id => 'legacy_ema_cross';
  @override
  String get title => 'Fast EMA crossover';
  @override
  String get plainEnglish =>
      'From your old dashboard. A fast EMA crossing a slightly slower one marks a turn. '
      'The target is small and the stop is wide, so it wins often but each loss costs more.';
}

/// From the old dashboard: MACD line crossing its signal line.
class MacdCross extends Strategy {
  const MacdCross(super.params);

  @override
  String get id => 'legacy_macd_cross';
  @override
  String get title => 'MACD crossover';
  @override
  String get plainEnglish =>
      'From your old dashboard. The MACD line crossing its signal line marks a shift in momentum.';

  @override
  SetupCheck check(MarketSeries series, int bar, TradeDirection direction) {
    final line = series.macdLine;
    final signal = series.macdSignal;
    final isBuy = direction == TradeDirection.buy;
    return SetupCheck(direction, [
      Condition(
        isBuy ? 'MACD crossed up over its signal' : 'MACD crossed down under its signal',
        isBuy ? gapCrossedAbove(line, signal, bar) : gapCrossedBelow(line, signal, bar),
        'MACD ${price(line[bar])} vs signal ${price(signal[bar])}',
      ),
    ]);
  }
}
