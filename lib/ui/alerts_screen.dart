import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../domain/strategies.dart' show price;
import '../state/signal_desk.dart';
import 'desk_theme.dart';
import 'instrument_screen.dart';

class AlertsScreen extends StatelessWidget {
  const AlertsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final alerts = context.watch<SignalDesk>().alerts;
    return ListView(
      padding: const EdgeInsets.fromLTRB(16, 20, 16, 24),
      children: [
        Text('Signals', style: DeskType.display(40)),
        const SizedBox(height: 4),
        Text('Every new signal since the app opened. Keep the app open to catch them.',
            style: DeskType.body(15, color: DeskColors.muted)),
        const SizedBox(height: 18),
        if (alerts.isEmpty)
          Text('No new signals yet. They arrive when a candle closes with every condition met.',
              style: DeskType.body(15, color: DeskColors.muted)),
        for (final alert in alerts)
          ListTile(
            contentPadding: EdgeInsets.zero,
            onTap: () => Navigator.of(context).push(MaterialPageRoute(
                builder: (_) => InstrumentScreen(symbol: alert.board.entry.symbol))),
            leading: Text(alert.plan.direction.label,
                style: DeskType.display(26, color: DeskColors.of(alert.plan.direction))),
            title: Text(alert.board.entry.name, style: DeskType.body(16, weight: FontWeight.w600)),
            subtitle: Text(
                'Entry ${price(alert.plan.entry)}  SL ${price(alert.plan.stop)}  TP ${price(alert.plan.target)}',
                style: DeskType.figure(14, color: DeskColors.muted)),
            trailing: Text(TimeOfDay.fromDateTime(alert.raisedAt).format(context),
                style: DeskType.figure(14, color: DeskColors.muted)),
          ),
      ],
    );
  }
}
