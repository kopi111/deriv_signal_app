import 'package:flutter_local_notifications/flutter_local_notifications.dart';

import '../domain/strategies.dart' show price;
import '../state/signal_desk.dart';

/// Android notification channels and the trade-signal notification itself.
class SignalNotifications {
  static const watchChannelId = 'market_watch';
  static const signalChannelId = 'trade_signals';

  final _plugin = FlutterLocalNotificationsPlugin();

  AndroidFlutterLocalNotificationsPlugin? get _android =>
      _plugin.resolvePlatformSpecificImplementation<AndroidFlutterLocalNotificationsPlugin>();

  Future<void> initialize() async {
    await _plugin.initialize(
      settings: const InitializationSettings(android: AndroidInitializationSettings('@mipmap/ic_launcher')),
    );
    await _android?.createNotificationChannel(const AndroidNotificationChannel(
      watchChannelId,
      'Market watch',
      description: 'Shows that Signal Desk is watching markets in the background.',
      importance: Importance.low,
    ));
    await _android?.createNotificationChannel(const AndroidNotificationChannel(
      signalChannelId,
      'Trade signals',
      description: 'A candle closed with every condition met.',
      importance: Importance.high,
    ));
  }

  Future<bool> requestPermission() async => await _android?.requestNotificationsPermission() ?? true;

  Future<void> announce(SignalAlert alert) {
    final plan = alert.plan;
    final entry = alert.board.entry;
    final caution = entry.proven ? '' : ' Unproven setup, trade small.';
    return _plugin.show(
      id: alert.board.entry.symbol.hashCode ^ plan.signalEpoch,
      title: '${plan.direction.label} ${entry.name}',
      body: 'Entry ${price(plan.entry)}, SL ${price(plan.stop)}, TP ${price(plan.target)}.$caution',
      notificationDetails: const NotificationDetails(
        android: AndroidNotificationDetails(
          signalChannelId,
          'Trade signals',
          importance: Importance.high,
          priority: Priority.high,
          category: AndroidNotificationCategory.alarm,
        ),
      ),
      payload: entry.symbol,
    );
  }
}
