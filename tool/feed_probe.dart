// Manual check of the live Deriv feed: dart run tool/feed_probe.dart
// ignore_for_file: avoid_print
import 'package:deriv_signal_app/data/deriv_feed.dart';

Future<void> main() async {
  final feed = DerivFeed(DerivConnection.fromEnvironment());
  final seen = <String, int>{};
  feed.updates.listen((update) {
    final kind = update.runtimeType.toString();
    seen['$kind ${update.symbol}'] = (seen['$kind ${update.symbol}'] ?? 0) + 1;
    if (update is FeedFailure) print('FAILURE ${update.symbol}: ${update.error}');
  });
  for (final symbol in ['R_75', 'frxXAUUSD', 'JD10', '1HZ100V', 'stpRNG', 'R_100', '1HZ75V', 'cryBTCUSD']) {
    feed.watch(symbol, 3600);
  }
  await Future<void>.delayed(const Duration(seconds: 25));
  print('streaming: ${feed.isStreaming}');
  seen.forEach((key, count) => print('$key x$count'));
  feed.close();
}
