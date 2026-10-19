import 'dart:async';
import 'dart:ui';

import 'package:flutter/foundation.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_background_service/flutter_background_service.dart';

import '../data/deriv_feed.dart';
import '../state/signal_desk.dart';
import 'playbook_loader.dart';
import 'signal_notifications.dart';

/// Keeps watching markets after the app is closed, using an Android
/// foreground service. It runs the same SignalDesk as the screen, so a
/// background alert is exactly the signal the app would show.
class MarketWatchService {
  static const _statusNotificationId = 888;

  static bool get isSupported => !kIsWeb && defaultTargetPlatform == TargetPlatform.android;

  static Future<void> start() async {
    if (!isSupported) return;
    final notifications = SignalNotifications();
    await notifications.initialize();
    await notifications.requestPermission();
    await FlutterBackgroundService().configure(
      androidConfiguration: AndroidConfiguration(
        onStart: watchMarketsInBackground,
        isForegroundMode: true,
        autoStart: true,
        autoStartOnBoot: true,
        notificationChannelId: SignalNotifications.watchChannelId,
        initialNotificationTitle: 'Signal Desk',
        initialNotificationContent: 'Starting market watch',
        foregroundServiceNotificationId: _statusNotificationId,
        foregroundServiceTypes: [AndroidForegroundType.specialUse],
      ),
      iosConfiguration: IosConfiguration(autoStart: false),
    );
  }
}

@pragma('vm:entry-point')
Future<void> watchMarketsInBackground(ServiceInstance service) async {
  DartPluginRegistrant.ensureInitialized();
  WidgetsFlutterBinding.ensureInitialized();
  final notifications = SignalNotifications();
  await notifications.initialize();
  final desk = SignalDesk(await loadPlaybook(), DerivFeed(DerivConnection.fromEnvironment()));
  desk.freshAlerts.listen(notifications.announce);
  Timer.periodic(const Duration(minutes: 1), (_) => _reportStatus(service, desk));
  service.on('stop').listen((_) {
    desk.dispose();
    service.stopSelf();
  });
}

void _reportStatus(ServiceInstance service, SignalDesk desk) {
  if (service is! AndroidServiceInstance) return;
  final live = desk.boards.where((board) => board.hasData).length;
  final open = desk.boards.where((board) => board.hasOpenPlan).length;
  final now = DateTime.now();
  final time = '${now.hour.toString().padLeft(2, '0')}:${now.minute.toString().padLeft(2, '0')}';
  service.setForegroundNotificationInfo(
    title: 'Watching $live markets',
    content: '$open trades on. Last check $time.',
  );
}
