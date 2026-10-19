import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import 'background/market_watch_service.dart';
import 'background/playbook_loader.dart';
import 'data/deriv_feed.dart';
import 'domain/strategies.dart' show price;
import 'state/signal_desk.dart';
import 'ui/alerts_screen.dart';
import 'ui/desk_screen.dart';
import 'ui/desk_theme.dart';
import 'ui/research_screen.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final playbook = await loadPlaybook();
  await MarketWatchService.start();
  runApp(ChangeNotifierProvider(
    create: (_) => SignalDesk(playbook, DerivFeed(DerivConnection.fromEnvironment())),
    child: const SignalDeskApp(),
  ));
}

class SignalDeskApp extends StatelessWidget {
  const SignalDeskApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Signal Desk',
      debugShowCheckedModeBanner: false,
      theme: buildDeskTheme(),
      home: const DeskShell(),
    );
  }
}

class DeskShell extends StatefulWidget {
  const DeskShell({super.key});

  @override
  State<DeskShell> createState() => _DeskShellState();
}

class _DeskShellState extends State<DeskShell> {
  int tab = 0;
  StreamSubscription<SignalAlert>? alertSubscription;

  @override
  void initState() {
    super.initState();
    alertSubscription = context.read<SignalDesk>().freshAlerts.listen(_announce);
  }

  void _announce(SignalAlert alert) {
    SystemSound.play(SystemSoundType.alert);
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(
      backgroundColor: DeskColors.raised,
      duration: const Duration(seconds: 12),
      content: Text(
        '${alert.plan.direction.label} ${alert.board.entry.name} at ${price(alert.plan.entry)}. '
        'SL ${price(alert.plan.stop)}, TP ${price(alert.plan.target)}.',
        style: DeskType.body(15),
      ),
    ));
  }

  @override
  void dispose() {
    alertSubscription?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final alertCount = context.watch<SignalDesk>().alerts.length;
    return Scaffold(
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 720),
            child: const [DeskScreen(), AlertsScreen(), ResearchScreen()][tab],
          ),
        ),
      ),
      bottomNavigationBar: NavigationBar(
        selectedIndex: tab,
        onDestinationSelected: (index) => setState(() => tab = index),
        destinations: [
          const NavigationDestination(icon: Icon(Icons.candlestick_chart), label: 'Desk'),
          NavigationDestination(
            icon: Badge(isLabelVisible: alertCount > 0, label: Text('$alertCount'),
                child: const Icon(Icons.notifications_none)),
            label: 'Signals',
          ),
          const NavigationDestination(icon: Icon(Icons.science_outlined), label: 'Research'),
        ],
      ),
    );
  }
}
