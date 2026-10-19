import '../domain/candle.dart';
import '../domain/market_series.dart';
import '../domain/playbook.dart';
import '../domain/setup_check.dart';
import '../domain/strategies.dart';
import '../domain/trade_plan.dart';

enum FeedState { connecting, live, failed }

/// Live view of one instrument: closed candles, the forming candle, the
/// latest trade plan and the setup checklist on the last closed candle.
/// Only closed candles are ever evaluated, so a signal never repaints.
class InstrumentBoard {
  InstrumentBoard(this.entry) : strategy = Strategy.create(entry.strategyId, entry.entryParams);

  final PlaybookEntry entry;
  final Strategy strategy;
  FeedState feedState = FeedState.connecting;
  String failure = '';
  Candle? forming;
  MarketSeries series = MarketSeries(const []);
  TradePlan? plan;
  List<SetupCheck> setups = const [];

  bool get hasData => series.length > 250;
  double? get lastPrice => forming?.close ?? (series.length > 0 ? series.closes.last : null);
  PlanStatus? get planStatus => plan?.statusOn(series);
  bool get hasOpenPlan => planStatus?.isOpen ?? false;

  SetupCheck get closestSetup =>
      setups.reduce((best, next) => next.metCount > best.metCount ? next : best);

  void loadHistory(List<Candle> candles) {
    feedState = FeedState.live;
    forming = candles.isEmpty ? null : candles.last;
    _replaceSeries(candles.isEmpty ? candles : candles.sublist(0, candles.length - 1));
  }

  /// Returns the new plan when the candle that just closed produced a signal.
  TradePlan? updateForming(Candle candle) {
    final previous = forming;
    if (previous != null && candle.epoch < previous.epoch) return null;
    forming = candle;
    if (previous == null || candle.epoch == previous.epoch) return null;
    final signalBefore = plan?.signalEpoch;
    _replaceSeries([...series.candles, previous]);
    final fresh = plan != null && plan!.signalEpoch != signalBefore && plan!.signalBar == series.lastIndex;
    return fresh ? plan : null;
  }

  void markFailed(String message) {
    feedState = FeedState.failed;
    failure = message;
  }

  void _replaceSeries(List<Candle> closed) {
    series = MarketSeries(closed);
    if (!hasData) return;
    setups = [
      strategy.check(series, series.lastIndex, TradeDirection.buy),
      strategy.check(series, series.lastIndex, TradeDirection.sell),
    ];
    plan = _latestPlan();
  }

  TradePlan? _latestPlan() {
    final oldest = series.lastIndex - TradePlan.maxHoldBars;
    for (var bar = series.lastIndex; bar > oldest && bar > 250; bar--) {
      final signal = strategy.signalAt(series, bar);
      if (signal != 0) return _planAt(bar, signal);
    }
    return null;
  }

  TradePlan _planAt(int bar, int signal) => TradePlan.fromSignal(
        series: series,
        signalBar: bar,
        direction: signal > 0 ? TradeDirection.buy : TradeDirection.sell,
        stopAtr: entry.stopAtr,
        rewardRisk: entry.rewardRisk,
      );
}
