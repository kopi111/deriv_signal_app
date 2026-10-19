import 'package:deriv_signal_app/domain/candle.dart';
import 'package:deriv_signal_app/domain/market_series.dart';
import 'package:deriv_signal_app/domain/setup_check.dart';
import 'package:deriv_signal_app/domain/trade_plan.dart';
import 'package:flutter_test/flutter_test.dart';

Candle bar(int index, double open, double high, double low, double close) =>
    Candle(epoch: index * 3600, open: open, high: high, low: low, close: close);

List<Candle> flatHistory(int count) => [for (var i = 0; i < count; i++) bar(i, 100, 101, 99, 100)];

TradePlan buyPlanOn(MarketSeries series) => TradePlan.fromSignal(
      series: series,
      signalBar: 19,
      direction: TradeDirection.buy,
      stopAtr: 1,
      rewardRisk: 2,
    );

void main() {
  test('levels are sized from ATR at the signal candle', () {
    final plan = buyPlanOn(MarketSeries(flatHistory(20)));
    expect(plan.entry, 100);
    expect(plan.stop, closeTo(98, 1e-9));
    expect(plan.target, closeTo(104, 1e-9));
  });

  test('a plan on the last closed candle says enter now', () {
    final series = MarketSeries(flatHistory(20));
    expect(buyPlanOn(series).statusOn(series), PlanStatus.enterNow);
  });

  test('target touched later marks the plan as won', () {
    final series = MarketSeries([...flatHistory(20), bar(20, 100, 104.5, 99.5, 104)]);
    expect(buyPlanOn(MarketSeries(flatHistory(20))).statusOn(series), PlanStatus.targetHit);
  });

  test('a candle touching both stop and target counts as stopped out', () {
    final series = MarketSeries([...flatHistory(20), bar(20, 100, 105, 97, 101)]);
    expect(buyPlanOn(MarketSeries(flatHistory(20))).statusOn(series), PlanStatus.stopHit);
  });

  test('plans expire after the maximum hold', () {
    final series = MarketSeries(flatHistory(20 + TradePlan.maxHoldBars));
    expect(buyPlanOn(MarketSeries(flatHistory(20))).statusOn(series), PlanStatus.expired);
  });
}
