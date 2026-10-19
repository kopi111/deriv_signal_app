import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../domain/strategies.dart' show price;
import '../state/instrument_board.dart';
import '../state/signal_desk.dart';
import 'desk_theme.dart';
import 'instrument_screen.dart';

class DeskScreen extends StatelessWidget {
  const DeskScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final desk = context.watch<SignalDesk>();
    final boards = desk.boards;
    final trades = boards.where((b) => b.hasOpenPlan).toList();
    final watching = boards.where((b) => !b.hasOpenPlan).toList();
    return ListView(
      padding: const EdgeInsets.fromLTRB(16, 20, 16, 24),
      children: [
        Text('Signal desk', style: DeskType.display(40)),
        const SizedBox(height: 4),
        Text(_summary(boards, desk.feed.isStreaming), style: DeskType.body(15, color: DeskColors.muted)),
        const SizedBox(height: 22),
        Text('Trades on', style: DeskType.display(24)),
        const SizedBox(height: 8),
        if (trades.isEmpty)
          Text('Nothing to take right now. Every market below is still waiting for its setup.',
              style: DeskType.body(15, color: DeskColors.muted))
        else
          for (final board in trades) _TradeRow(board: board),
        const SizedBox(height: 26),
        Text('Watching', style: DeskType.display(24)),
        const SizedBox(height: 4),
        for (final board in watching) _WatchRow(board: board),
      ],
    );
  }

  String _summary(List<InstrumentBoard> boards, bool streaming) {
    final live = boards.where((b) => b.hasData).length;
    final updates = streaming ? 'Streaming live prices.' : 'Prices refresh every 20 seconds.';
    return '$live of ${boards.length} markets live. $updates Signals are decided on closed candles only.';
  }
}

void _open(BuildContext context, InstrumentBoard board) => Navigator.of(context).push(
    MaterialPageRoute(builder: (_) => InstrumentScreen(symbol: board.entry.symbol)));

class _TradeRow extends StatelessWidget {
  const _TradeRow({required this.board});

  final InstrumentBoard board;

  @override
  Widget build(BuildContext context) {
    final plan = board.plan!;
    final color = DeskColors.of(plan.direction);
    final status = plan.statusOn(board.series);
    return InkWell(
      onTap: () => _open(context, board),
      child: Container(
        margin: const EdgeInsets.only(bottom: 10),
        padding: const EdgeInsets.all(14),
        decoration: BoxDecoration(
          color: DeskColors.surface,
          border: Border(left: BorderSide(color: color, width: 4)),
        ),
        child: Row(
          children: [
            SizedBox(width: 72, child: Text(plan.direction.label, style: DeskType.display(34, color: color))),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(board.entry.name, style: DeskType.body(17, weight: FontWeight.w600)),
                  Text('${status.label}. ${board.strategy.title}',
                      style: DeskType.body(14, color: DeskColors.muted)),
                  if (!board.entry.proven)
                    Text('unproven', style: DeskType.body(13, color: DeskColors.waiting)),
                ],
              ),
            ),
            Column(
              crossAxisAlignment: CrossAxisAlignment.end,
              children: [
                _Level('TP', plan.target, DeskColors.buy),
                _Level('In', plan.entry, DeskColors.ink),
                _Level('SL', plan.stop, DeskColors.sell),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class _Level extends StatelessWidget {
  const _Level(this.label, this.value, this.color);

  final String label;
  final double value;
  final Color color;

  @override
  Widget build(BuildContext context) => Text('$label ${price(value)}', style: DeskType.figure(15, color: color));
}

class _WatchRow extends StatelessWidget {
  const _WatchRow({required this.board});

  final InstrumentBoard board;

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () => _open(context, board),
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 12),
        decoration: const BoxDecoration(border: Border(bottom: BorderSide(color: DeskColors.line))),
        child: Row(
          children: [
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(children: [
                    Flexible(child: Text(board.entry.name, style: DeskType.body(17, weight: FontWeight.w600))),
                    const SizedBox(width: 8),
                    if (!board.entry.proven)
                      Text('unproven', style: DeskType.body(13, color: DeskColors.waiting)),
                  ]),
                  Text('${board.strategy.title}, ${board.entry.timeframe}',
                      style: DeskType.body(14, color: DeskColors.muted)),
                ],
              ),
            ),
            _Readiness(board: board),
            const SizedBox(width: 14),
            SizedBox(
              width: 92,
              child: Text(board.lastPrice == null ? '…' : price(board.lastPrice!),
                  textAlign: TextAlign.right, style: DeskType.figure(18)),
            ),
          ],
        ),
      ),
    );
  }
}

/// How many of the closest setup's conditions are already met.
class _Readiness extends StatelessWidget {
  const _Readiness({required this.board});

  final InstrumentBoard board;

  @override
  Widget build(BuildContext context) {
    if (board.setups.isEmpty) return const SizedBox(width: 60);
    final setup = board.closestSetup;
    final color = DeskColors.of(setup.direction);
    return SizedBox(
      width: 60,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('${setup.direction.label} ${setup.metCount}/${setup.conditions.length}',
              style: DeskType.figure(14, color: color)),
          const SizedBox(height: 3),
          Row(children: [
            for (final condition in setup.conditions)
              Expanded(
                child: Container(
                  height: 4,
                  margin: const EdgeInsets.only(right: 2),
                  color: condition.met ? color : DeskColors.line,
                ),
              ),
          ]),
        ],
      ),
    );
  }
}
