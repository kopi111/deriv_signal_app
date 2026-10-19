import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../domain/strategies.dart' show price;
import '../state/instrument_board.dart';
import '../state/signal_desk.dart';
import 'candle_chart.dart';
import 'desk_theme.dart';
import 'position_calculator.dart';
import 'setup_checklist.dart';
import 'trade_ticket.dart';
import 'track_record.dart';

class InstrumentScreen extends StatelessWidget {
  const InstrumentScreen({super.key, required this.symbol});

  final String symbol;

  @override
  Widget build(BuildContext context) {
    final board = context.watch<SignalDesk>().board(symbol);
    return Scaffold(
      appBar: AppBar(
        backgroundColor: DeskColors.petrol,
        title: Text(board.entry.name, style: DeskType.display(26)),
        actions: [
          if (board.lastPrice != null)
            Padding(
              padding: const EdgeInsets.only(right: 16),
              child: Center(child: Text(price(board.lastPrice!), style: DeskType.figure(22))),
            ),
        ],
      ),
      body: board.hasData ? _Details(board: board) : _Pending(board: board),
    );
  }
}

class _Details extends StatelessWidget {
  const _Details({required this.board});

  final InstrumentBoard board;

  @override
  Widget build(BuildContext context) {
    final plan = board.plan;
    final showPlan = plan != null && board.hasOpenPlan;
    return ListView(
      padding: const EdgeInsets.fromLTRB(16, 4, 16, 32),
      children: [
        Text('${board.strategy.title} on ${board.entry.timeframe} candles',
            style: DeskType.body(15, color: DeskColors.muted)),
        const SizedBox(height: 12),
        if (showPlan) TradeTicket(board: board, plan: plan) else _NoTrade(board: board),
        const SizedBox(height: 18),
        CandleChart(series: board.series, forming: board.forming, plan: showPlan ? plan : null),
        _Section(
          title: showPlan ? 'Why this trade' : 'What I am waiting for',
          child: _Reasons(board: board, showPlan: showPlan),
        ),
        _Section(
          title: 'How the rule works',
          child: Text(board.strategy.plainEnglish, style: DeskType.body(15)),
        ),
        if (showPlan)
          _Section(title: 'Position size', child: PositionCalculator(entry: board.entry, plan: plan)),
        _Section(title: 'Track record', child: TrackRecord(entry: board.entry)),
      ],
    );
  }
}

class _Reasons extends StatelessWidget {
  const _Reasons({required this.board, required this.showPlan});

  final InstrumentBoard board;
  final bool showPlan;

  @override
  Widget build(BuildContext context) {
    if (showPlan) {
      final plan = board.plan!;
      return SetupChecklist(setup: board.strategy.check(board.series, plan.signalBar, plan.direction));
    }
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        for (final setup in board.setups) ...[
          Text('${setup.direction.label} setup: ${setup.metCount} of ${setup.conditions.length} conditions met',
              style: DeskType.body(15, color: DeskColors.of(setup.direction), weight: FontWeight.w600)),
          SetupChecklist(setup: setup),
          const SizedBox(height: 10),
        ],
      ],
    );
  }
}

class _NoTrade extends StatelessWidget {
  const _NoTrade({required this.board});

  final InstrumentBoard board;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(18),
      decoration: const BoxDecoration(
        color: DeskColors.surface,
        border: Border(top: BorderSide(color: DeskColors.waiting, width: 4)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('Stay out', style: DeskType.display(48, color: DeskColors.waiting)),
          const SizedBox(height: 6),
          Text('No setup on the last closed candle. The checklist below shows how close each side is. '
              'The app checks again when the current candle closes.',
              style: DeskType.body(15, color: DeskColors.muted)),
        ],
      ),
    );
  }
}

class _Pending extends StatelessWidget {
  const _Pending({required this.board});

  final InstrumentBoard board;

  @override
  Widget build(BuildContext context) {
    final text = board.feedState == FeedState.failed
        ? 'Deriv refused this market: ${board.failure}'
        : 'Loading candle history from Deriv…';
    return Center(child: Padding(
      padding: const EdgeInsets.all(24),
      child: Text(text, style: DeskType.body(16, color: DeskColors.muted), textAlign: TextAlign.center),
    ));
  }
}

class _Section extends StatelessWidget {
  const _Section({required this.title, required this.child});

  final String title;
  final Widget child;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(top: 28),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(title, style: DeskType.display(24)),
          const SizedBox(height: 10),
          child,
        ],
      ),
    );
  }
}
