class Candle {
  const Candle({
    required this.epoch,
    required this.open,
    required this.high,
    required this.low,
    required this.close,
  });

  factory Candle.fromDeriv(Map<String, dynamic> json) => Candle(
        epoch: _asInt(json['open_time'] ?? json['epoch']),
        open: _asDouble(json['open']),
        high: _asDouble(json['high']),
        low: _asDouble(json['low']),
        close: _asDouble(json['close']),
      );

  final int epoch;
  final double open;
  final double high;
  final double low;
  final double close;

  DateTime get openedAt =>
      DateTime.fromMillisecondsSinceEpoch(epoch * 1000, isUtc: true);

  static double _asDouble(Object? value) =>
      value is num ? value.toDouble() : double.parse(value.toString());

  static int _asInt(Object? value) =>
      value is num ? value.toInt() : int.parse(value.toString());
}
