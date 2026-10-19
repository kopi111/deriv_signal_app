import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../domain/playbook.dart';
import '../domain/strategies.dart';
import '../state/signal_desk.dart';
import 'desk_theme.dart';

class ResearchScreen extends StatelessWidget {
  const ResearchScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final playbook = context.read<SignalDesk>().playbook;
    final entries = [...playbook.entries]
      ..sort(_passedFirstThenTotal);
    return ListView(
      padding: const EdgeInsets.fromLTRB(16, 20, 16, 24),
      children: [
        Text('How the strategies were chosen', style: DeskType.display(34)),
        const SizedBox(height: 10),
        Text(
          'Seven strategy types were tested on every market, on 1-hour and 15-minute candles. '
          'Settings were only ever tuned on older data and then scored on the next, unseen period '
          '(walk-forward), with the spread charged on every trade. A strategy passes only if it is '
          'profitable on unseen data, holds up in most periods, beats random entries using the same '
          'stop and target, and does not lose on a final untouched slice of history.',
          style: DeskType.body(15),
        ),
        const SizedBox(height: 10),
        Text(
          'Only ${playbook.passedCount} of ${playbook.testedCount} market, timeframe and strategy '
          'combinations passed. With that many tries, a couple of passes can happen by luck, so '
          'even the passes need a few weeks of small-size trading before you trust them.',
          style: DeskType.body(15, weight: FontWeight.w600),
        ),
        const SizedBox(height: 8),
        Text('Results are in R: 1R is the amount risked on a trade. Tested ${_dates(entries)}. '
            'Updated ${playbook.generated.substring(0, 10)}.',
            style: DeskType.body(14, color: DeskColors.muted)),
        const SizedBox(height: 18),
        for (final entry in entries) _ResultRow(entry: entry),
      ],
    );
  }

  static int _passedFirstThenTotal(PlaybookEntry a, PlaybookEntry b) {
    if (a.proven != b.proven) return a.proven ? -1 : 1;
    return b.outOfSample.totalR.compareTo(a.outOfSample.totalR);
  }

  String _dates(List<PlaybookEntry> entries) =>
      entries.isEmpty ? '' : 'up to ${entries.first.testedTo}';
}

class _ResultRow extends StatelessWidget {
  const _ResultRow({required this.entry});

  final PlaybookEntry entry;

  @override
  Widget build(BuildContext context) {
    final result = entry.outOfSample;
    final color = entry.proven ? DeskColors.buy : DeskColors.waiting;
    final strategy = Strategy.create(entry.strategyId, entry.entryParams);
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 12),
      decoration: const BoxDecoration(border: Border(bottom: BorderSide(color: DeskColors.line))),
      child: Row(
        children: [
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(entry.name, style: DeskType.body(16, weight: FontWeight.w600)),
                Text('${strategy.title}, ${entry.timeframe}. ${entry.proven ? 'Passed' : 'No proven edge'}',
                    style: DeskType.body(14, color: color)),
              ],
            ),
          ),
          Column(
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              Text('${result.totalR >= 0 ? '+' : ''}${result.totalR.toStringAsFixed(1)}R',
                  style: DeskType.figure(20)),
              Text('PF ${result.profitFactor.toStringAsFixed(2)}, ${result.trades} trades',
                  style: DeskType.body(13, color: DeskColors.muted)),
            ],
          ),
        ],
      ),
    );
  }
}
