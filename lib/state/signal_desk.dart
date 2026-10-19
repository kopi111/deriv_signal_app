import 'dart:async';

import 'package:flutter/foundation.dart';

import '../data/deriv_feed.dart';
import '../domain/playbook.dart';
import '../domain/trade_plan.dart';
import 'instrument_board.dart';

class SignalAlert {
  SignalAlert(this.board, this.plan) : raisedAt = DateTime.now();

  final InstrumentBoard board;
  final TradePlan plan;
  final DateTime raisedAt;
}

/// Owns every instrument board and routes the live feed into them.
class SignalDesk extends ChangeNotifier {
  SignalDesk(this.playbook, this.feed) {
    for (final entry in playbook.entries) {
      _boards[entry.symbol] = InstrumentBoard(entry);
    }
    _subscription = feed.updates.listen(_apply);
    for (final entry in playbook.entries) {
      feed.watch(entry.symbol, entry.granularitySeconds);
    }
  }

  final Playbook playbook;
  final DerivFeed feed;
  final Map<String, InstrumentBoard> _boards = {};
  final List<SignalAlert> alerts = [];
  final _freshAlerts = StreamController<SignalAlert>.broadcast();
  late final StreamSubscription<CandleUpdate> _subscription;

  Stream<SignalAlert> get freshAlerts => _freshAlerts.stream;

  /// Open trades first, then boards closest to a setup.
  List<InstrumentBoard> get boards => _boards.values.toList()..sort(_byUrgency);

  InstrumentBoard board(String symbol) => _boards[symbol]!;

  void _apply(CandleUpdate update) {
    final board = _boards[update.symbol];
    if (board == null) return;
    switch (update) {
      case CandleHistory(:final candles):
        board.loadHistory(candles);
      case FormingCandle(:final candle):
        final plan = board.updateForming(candle);
        if (plan != null) _raise(SignalAlert(board, plan));
      case FeedFailure(:final error):
        board.markFailed(error.message);
    }
    notifyListeners();
  }

  void _raise(SignalAlert alert) {
    alerts.insert(0, alert);
    _freshAlerts.add(alert);
  }

  static int _byUrgency(InstrumentBoard a, InstrumentBoard b) {
    final open = _openRank(a).compareTo(_openRank(b));
    if (open != 0) return open;
    final proven = (b.entry.proven ? 1 : 0).compareTo(a.entry.proven ? 1 : 0);
    if (proven != 0) return proven;
    return _readiness(b).compareTo(_readiness(a));
  }

  static int _openRank(InstrumentBoard board) => switch (board.planStatus) {
        PlanStatus.enterNow => 0,
        PlanStatus.running => 1,
        _ => 2,
      };

  static double _readiness(InstrumentBoard board) {
    if (board.setups.isEmpty) return 0;
    final setup = board.closestSetup;
    return setup.metCount / setup.conditions.length;
  }

  @override
  void dispose() {
    _subscription.cancel();
    _freshAlerts.close();
    feed.close();
    super.dispose();
  }
}
