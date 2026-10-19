import 'dart:convert';
import 'dart:io';

import 'package:deriv_signal_app/domain/candle.dart';
import 'package:deriv_signal_app/domain/playbook.dart';
import 'package:deriv_signal_app/state/instrument_board.dart';
import 'package:flutter_test/flutter_test.dart';

PlaybookEntry entry() => PlaybookEntry.fromJson({
      'symbol': 'frxXAUUSD', 'name': 'Gold', 'group': 'Metals', 'timeframe': '1h',
      'granularity': 3600, 'strategy': 'ema_cross', 'entry': {'fast': 9, 'slow': 50},
      'exit': {'stop_atr': 2, 'reward_risk': 2}, 'proven': true, 'failed_checks': [],
      'walk_forward': _result, 'lockbox': _result, 'random_p': 0.01, 'positive_folds': 5,
      'fold_count': 6, 'tested_from': '2025-09-18', 'tested_to': '2026-09-18',
    });

const _result = {'trades': 1, 'win_rate': 1, 'profit_factor': 1, 'expectancy_r': 0,
    'total_r': 0, 'max_drawdown_r': 0};

List<Candle> fixtureCandles() {
  final samples = jsonDecode(File('test/fixtures/parity.json').readAsStringSync()) as List;
  return [
    for (final row in (samples.first['candles'] as List).cast<Map<String, dynamic>>())
      Candle.fromDeriv(row),
  ];
}

void main() {
  test('the newest history candle is treated as forming, not closed', () {
    final candles = fixtureCandles();
    final board = InstrumentBoard(entry())..loadHistory(candles);
    expect(board.series.length, candles.length - 1);
    expect(board.forming!.epoch, candles.last.epoch);
  });

  test('ticks inside the forming candle never change the closed series', () {
    final candles = fixtureCandles();
    final board = InstrumentBoard(entry())..loadHistory(candles);
    final last = candles.last;
    board.updateForming(Candle(epoch: last.epoch, open: last.open, high: last.high * 1.05,
        low: last.low, close: last.high * 1.05));
    expect(board.series.length, candles.length - 1);
  });

  test('a new candle opening closes the previous one', () {
    final candles = fixtureCandles();
    final board = InstrumentBoard(entry())..loadHistory(candles);
    final last = candles.last;
    board.updateForming(Candle(epoch: last.epoch + 3600, open: last.close, high: last.close,
        low: last.close, close: last.close));
    expect(board.series.length, candles.length);
    expect(board.series.candles.last.epoch, last.epoch);
  });

  test('an older candle from a poll batch is ignored', () {
    final candles = fixtureCandles();
    final board = InstrumentBoard(entry())..loadHistory(candles);
    board.updateForming(candles[candles.length - 3]);
    expect(board.forming!.epoch, candles.last.epoch);
    expect(board.series.length, candles.length - 1);
  });
}
