import 'dart:async';
import 'dart:convert';

import 'package:web_socket_channel/web_socket_channel.dart';

import '../domain/candle.dart';

class DerivFeedException implements Exception {
  DerivFeedException(this.message);
  final String message;

  @override
  String toString() => 'Deriv feed: $message';
}

/// One update for a subscribed instrument: the history on first contact,
/// then every tick's version of the forming candle.
sealed class CandleUpdate {
  const CandleUpdate(this.symbol);
  final String symbol;
}

class CandleHistory extends CandleUpdate {
  const CandleHistory(super.symbol, this.candles);
  final List<Candle> candles;
}

class FormingCandle extends CandleUpdate {
  const FormingCandle(super.symbol, this.candle);
  final Candle candle;
}

class FeedFailure extends CandleUpdate {
  const FeedFailure(super.symbol, this.error);
  final DerivFeedException error;
}

/// Connection settings, passed at build time:
/// `--dart-define=DERIV_APP_ID=12345 --dart-define=DERIV_API_TOKEN=abc`.
/// The token is optional; a read-only token is enough.
class DerivConnection {
  const DerivConnection({required this.appId, required this.apiToken});

  factory DerivConnection.fromEnvironment() => const DerivConnection(
        appId: String.fromEnvironment('DERIV_APP_ID', defaultValue: publicTestAppId),
        apiToken: String.fromEnvironment('DERIV_API_TOKEN'),
      );

  static const publicTestAppId = '1089';

  final String appId;
  final String apiToken;

  Uri get endpoint => Uri.parse('wss://ws.derivws.com/websockets/v3?app_id=$appId');
  bool get hasToken => apiToken.isNotEmpty;
}

/// Wraps Deriv's WebSocket API. Each symbol loads its history with a live
/// candle subscription. If Deriv refuses subscriptions (the public test
/// app id does since 2026), the feed switches to polling the last few
/// candles, where every poll re-sends the just-closed candle with its final
/// values. Deriv silently drops requests that arrive together, so requests
/// go out one at a time from a queue; a rate-limit reply pauses the queue
/// and retries the same request. Reconnects after a drop.
class DerivFeed {
  DerivFeed(this.connection, {this.historyCandles = 1500});

  static const _pollEvery = Duration(seconds: 20);
  static const _rateLimitPause = Duration(seconds: 30);
  static const _historyRequest = 1;
  static const _pollRequest = 2;
  static const _authorizeRequest = 3;
  static const _pollCandles = 3;
  static const _replyTimeout = Duration(seconds: 8);
  static const _reconnectAfter = Duration(seconds: 5);

  final DerivConnection connection;
  final int historyCandles;
  final Map<String, int> _granularityBySymbol = {};
  final _updates = StreamController<CandleUpdate>.broadcast();
  final List<Map<String, Object>> _queue = [];
  WebSocketChannel? _channel;
  Timer? _poller;
  Timer? _replyWatchdog;
  bool _awaitingReply = false;
  bool _pausedForRateLimit = false;
  bool _streamingRefused = false;
  bool _closed = false;

  Stream<CandleUpdate> get updates => _updates.stream;
  bool get isStreaming => !_streamingRefused;

  void watch(String symbol, int granularitySeconds) {
    _granularityBySymbol[symbol] = granularitySeconds;
    _ensureConnected();
    _requestHistory(symbol, granularitySeconds);
  }

  void close() {
    _closed = true;
    _poller?.cancel();
    _replyWatchdog?.cancel();
    _channel?.sink.close();
    _updates.close();
  }

  void _ensureConnected() {
    if (_channel != null) return;
    final channel = WebSocketChannel.connect(connection.endpoint);
    _channel = channel;
    channel.stream.listen(_onMessage, onDone: _onDisconnect, onError: (_) => _onDisconnect());
    _poller = Timer.periodic(_pollEvery, (_) => _pollIfNotStreaming());
    if (connection.hasToken) {
      _send({'authorize': connection.apiToken, 'req_id': _authorizeRequest});
    }
  }

  void _pollIfNotStreaming() {
    if (_streamingRefused) _granularityBySymbol.forEach(_poll);
  }

  void _requestHistory(String symbol, int granularitySeconds) => _send({
        ..._candleRequest(symbol, granularitySeconds, historyCandles, _historyRequest),
        if (!_streamingRefused) 'subscribe': 1,
      });

  void _poll(String symbol, int granularitySeconds) =>
      _send(_candleRequest(symbol, granularitySeconds, _pollCandles, _pollRequest));

  Map<String, Object> _candleRequest(String symbol, int granularity, int count, int kind) => {
        'ticks_history': symbol,
        'count': count,
        'end': 'latest',
        'granularity': granularity,
        'style': 'candles',
        'req_id': kind,
      };

  void _send(Map<String, Object> request) {
    final duplicate = _queue.any((queued) =>
        queued['ticks_history'] == request['ticks_history'] && queued['req_id'] == request['req_id']);
    if (duplicate) return;
    _queue.add(request);
    _sendNext();
  }

  void _sendNext() {
    if (_awaitingReply || _pausedForRateLimit || _queue.isEmpty || _channel == null) return;
    _awaitingReply = true;
    _channel!.sink.add(jsonEncode(_queue.removeAt(0)));
    _replyWatchdog = Timer(_replyTimeout, _replyArrived);
  }

  void _replyArrived() {
    _replyWatchdog?.cancel();
    _awaitingReply = false;
    _sendNext();
  }

  void _onMessage(dynamic raw) {
    final message = jsonDecode(raw as String) as Map<String, dynamic>;
    if (message['msg_type'] == 'ohlc') {
      _onStreamedCandle(message['ohlc'] as Map<String, dynamic>);
      return;
    }
    _replyArrived();
    if (message['error'] != null) {
      _onError(message);
      return;
    }
    if (message['msg_type'] == 'candles') _onCandles(message);
  }

  void _onStreamedCandle(Map<String, dynamic> ohlc) =>
      _updates.add(FormingCandle(ohlc['symbol'].toString(), Candle.fromDeriv(ohlc)));

  void _onCandles(Map<String, dynamic> message) {
    final symbol = _symbolOf(message);
    final candles = _candlesFrom(message['candles'] as List);
    if (message['req_id'] == _historyRequest) {
      _updates.add(CandleHistory(symbol, candles));
      return;
    }
    for (final candle in candles) {
      _updates.add(FormingCandle(symbol, candle));
    }
  }

  void _onError(Map<String, dynamic> message) {
    final echo = message['echo_req'] as Map? ?? const {};
    final text = (message['error'] as Map)['message'].toString();
    if ((message['error'] as Map)['code'] == 'RateLimit') {
      _retryAfterPause(Map<String, Object>.from(echo));
      return;
    }
    if (echo['subscribe'] == 1) {
      if (!_streamingRefused) _switchToPolling();
      return;
    }
    _updates.add(FeedFailure(_symbolOf(message), DerivFeedException(text)));
  }

  void _retryAfterPause(Map<String, Object> request) {
    _pausedForRateLimit = true;
    _queue.insert(0, request);
    Timer(_rateLimitPause, () {
      _pausedForRateLimit = false;
      _sendNext();
    });
  }

  void _switchToPolling() {
    _streamingRefused = true;
    _queue.removeWhere((queued) => queued['subscribe'] == 1);
    _granularityBySymbol.forEach(_requestHistory);
  }

  String _symbolOf(Map<String, dynamic> message) {
    final echo = message['echo_req'];
    return echo is Map ? (echo['ticks_history'] ?? '').toString() : '';
  }

  List<Candle> _candlesFrom(List rows) =>
      [for (final row in rows.cast<Map<String, dynamic>>()) Candle.fromDeriv(row)];

  void _onDisconnect() {
    _poller?.cancel();
    _replyWatchdog?.cancel();
    _awaitingReply = false;
    _queue.clear();
    _channel = null;
    if (_closed) return;
    Timer(_reconnectAfter, _resubscribeAll);
  }

  void _resubscribeAll() {
    if (_closed || _granularityBySymbol.isEmpty) return;
    _ensureConnected();
    _granularityBySymbol.forEach(_requestHistory);
  }
}
