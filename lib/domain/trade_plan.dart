import 'market_series.dart';
import 'setup_check.dart';

enum PlanStatus {
  enterNow('Enter now'),
  running('In play'),
  targetHit('Target hit'),
  stopHit('Stopped out'),
  expired('Expired');

  const PlanStatus(this.label);
  final String label;

  bool get isOpen => this == enterNow || this == running;
}

/// Entry, stop and target for a signal, sized from ATR at the signal candle
/// exactly as research/backtest.py does. Entry is the signal candle's close,
/// which is where the next candle opens on a continuous market.
class TradePlan {
  TradePlan._({
    required this.direction,
    required this.signalBar,
    required this.signalEpoch,
    required this.entry,
    required this.stop,
    required this.target,
    required this.rewardRisk,
  });

  factory TradePlan.fromSignal({
    required MarketSeries series,
    required int signalBar,
    required TradeDirection direction,
    required double stopAtr,
    required double rewardRisk,
  }) {
    final entry = series.closes[signalBar];
    final risk = stopAtr * series.atr(14)[signalBar];
    return TradePlan._(
      direction: direction,
      signalBar: signalBar,
      signalEpoch: series.candles[signalBar].epoch,
      entry: entry,
      stop: entry - direction.sign * risk,
      target: entry + direction.sign * risk * rewardRisk,
      rewardRisk: rewardRisk,
    );
  }

  static const maxHoldBars = 48;

  final TradeDirection direction;
  final int signalBar;
  final int signalEpoch;
  final double entry;
  final double stop;
  final double target;
  final double rewardRisk;

  double get riskDistance => (entry - stop).abs();
  double get rewardDistance => (target - entry).abs();

  /// Walks the candles after the signal. Stop wins a candle that touches both.
  PlanStatus statusOn(MarketSeries series) {
    final lastBar = series.lastIndex;
    if (lastBar == signalBar) return PlanStatus.enterNow;
    for (var bar = signalBar + 1; bar <= lastBar; bar++) {
      if (_touchedStop(series, bar)) return PlanStatus.stopHit;
      if (_touchedTarget(series, bar)) return PlanStatus.targetHit;
      if (bar - signalBar >= maxHoldBars) return PlanStatus.expired;
    }
    return PlanStatus.running;
  }

  double openResultInR(double currentPrice) =>
      (currentPrice - entry) * direction.sign / riskDistance;

  bool _touchedStop(MarketSeries series, int bar) => direction == TradeDirection.buy
      ? series.lows[bar] <= stop
      : series.highs[bar] >= stop;

  bool _touchedTarget(MarketSeries series, int bar) => direction == TradeDirection.buy
      ? series.highs[bar] >= target
      : series.lows[bar] <= target;
}
