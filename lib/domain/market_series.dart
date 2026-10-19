import 'candle.dart';
import 'indicators.dart';

/// Closed candles plus lazily computed, cached indicator lines.
class MarketSeries {
  MarketSeries(List<Candle> candles) : candles = List.unmodifiable(candles);

  final List<Candle> candles;
  final Map<String, List<double>> _cache = {};

  int get length => candles.length;
  int get lastIndex => candles.length - 1;

  List<double> get opens => _cached('open', () => [for (final c in candles) c.open]);
  List<double> get highs => _cached('high', () => [for (final c in candles) c.high]);
  List<double> get lows => _cached('low', () => [for (final c in candles) c.low]);
  List<double> get closes => _cached('close', () => [for (final c in candles) c.close]);

  List<double> ema(int period) => _cached('ema$period', () => Indicators.ema(closes, period));
  List<double> rsi(int period) => _cached('rsi$period', () => Indicators.rsi(closes, period));
  List<double> atr(int period) => _cached('atr$period', () => Indicators.atr(candles, period));
  List<double> adx(int period) => _cached('adx$period', () => Indicators.adx(candles, period));

  List<double> get macdLine => _macd().$1;
  List<double> get macdSignal => _macd().$2;

  List<double> bollingerLower(int period, double width) => _bollinger(period, width).$1;
  List<double> bollingerUpper(int period, double width) => _bollinger(period, width).$3;

  List<double> priorHighest(int period) =>
      _cached('hh$period', () => Indicators.priorHighest(highs, period));
  List<double> priorLowest(int period) =>
      _cached('ll$period', () => Indicators.priorLowest(lows, period));

  (List<double>, List<double>) _macd() {
    final line = _cached('macd', () => Indicators.macd(closes).$1);
    return (line, _cached('macdSignal', () => Indicators.ema(line, 9)));
  }

  (List<double>, List<double>, List<double>) _bollinger(int period, double width) {
    final key = 'bb$period/$width';
    if (!_cache.containsKey('$key/lower')) {
      final (lower, middle, upper) = Indicators.bollinger(closes, period, width);
      _cache['$key/lower'] = lower;
      _cache['$key/middle'] = middle;
      _cache['$key/upper'] = upper;
    }
    return (_cache['$key/lower']!, _cache['$key/middle']!, _cache['$key/upper']!);
  }

  List<double> _cached(String key, List<double> Function() build) =>
      _cache.putIfAbsent(key, build);
}
