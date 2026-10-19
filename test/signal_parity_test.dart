import 'dart:convert';
import 'dart:io';

import 'package:deriv_signal_app/domain/candle.dart';
import 'package:deriv_signal_app/domain/market_series.dart';
import 'package:deriv_signal_app/domain/strategies.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  final samples = jsonDecode(File('test/fixtures/parity.json').readAsStringSync()) as List;

  for (final sample in samples.cast<Map<String, dynamic>>()) {
    final series = MarketSeries([
      for (final row in (sample['candles'] as List).cast<Map<String, dynamic>>())
        Candle.fromDeriv(row),
    ]);

    test('${sample['symbol']}: ATR matches Python', () {
      final expected = (sample['atr'] as List).cast<num>();
      final actual = series.atr(14);
      for (var bar = 0; bar < expected.length; bar++) {
        expect(actual[bar], closeTo(expected[bar].toDouble(), 1e-6), reason: 'bar $bar');
      }
    });

    for (final testCase in (sample['cases'] as List).cast<Map<String, dynamic>>()) {
      final params = (testCase['params'] as Map).cast<String, num>();
      test('${sample['symbol']}: ${testCase['strategy']} $params signals match Python', () {
        final strategy = Strategy.create(testCase['strategy'] as String, params);
        final expected = (testCase['signals'] as List).cast<int>();
        final mismatches = [
          for (var bar = 0; bar < expected.length; bar++)
            if (strategy.signalAt(series, bar) != expected[bar]) bar,
        ];
        expect(mismatches, isEmpty,
            reason: '${mismatches.length} of ${expected.length} bars differ');
      });
    }
  }
}
