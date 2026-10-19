import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../domain/candle.dart';
import '../domain/market_series.dart';
import '../domain/trade_plan.dart';
import 'desk_theme.dart';

/// Recent closed candles plus the forming one, the 50/200 EMAs, and the
/// plan's levels as dashed lines. The signal candle gets a marker.
class CandleChart extends StatelessWidget {
  const CandleChart({super.key, required this.series, this.forming, this.plan});

  final MarketSeries series;
  final Candle? forming;
  final TradePlan? plan;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 240,
      child: CustomPaint(
        painter: _ChartPainter(series, forming, plan),
        child: const SizedBox.expand(),
      ),
    );
  }
}

class _ChartPainter extends CustomPainter {
  _ChartPainter(this.series, this.forming, this.plan);

  final MarketSeries series;
  final Candle? forming;
  final TradePlan? plan;
  static const _visible = 80;

  @override
  void paint(Canvas canvas, Size size) {
    if (series.length < _visible) return;
    final first = series.length - _visible;
    final candles = [...series.candles.sublist(first), ?forming];
    final levels = [if (plan != null) ...[plan!.stop, plan!.target]];
    final high = [...candles.map((c) => c.high), ...levels].reduce(math.max);
    final low = [...candles.map((c) => c.low), ...levels].reduce(math.min);
    final step = size.width / candles.length;
    double x(int index) => (index + 0.5) * step;
    double y(double value) => 6 + (high - value) / (high - low) * (size.height - 12);

    _drawLine(canvas, series.ema(200).sublist(first), x, y, DeskColors.waiting.withValues(alpha: 0.7));
    _drawLine(canvas, series.ema(50).sublist(first), x, y, DeskColors.muted.withValues(alpha: 0.6));
    for (var i = 0; i < candles.length; i++) {
      _drawCandle(canvas, candles[i], x(i), step, y, isForming: i == _visible);
    }
    if (plan != null) _drawPlan(canvas, size, plan!, first, x, y);
  }

  void _drawCandle(Canvas canvas, Candle candle, double centre, double step,
      double Function(double) y, {required bool isForming}) {
    final color = candle.close >= candle.open ? DeskColors.buy : DeskColors.sell;
    final paint = Paint()..color = isForming ? color.withValues(alpha: 0.45) : color;
    canvas.drawLine(Offset(centre, y(candle.high)), Offset(centre, y(candle.low)), paint..strokeWidth = 1);
    final top = y(math.max(candle.open, candle.close));
    final bottom = y(math.min(candle.open, candle.close));
    final body = Rect.fromLTRB(centre - step * 0.32, top, centre + step * 0.32, math.max(bottom, top + 1));
    canvas.drawRect(body, paint);
  }

  void _drawLine(Canvas canvas, List<double> values, double Function(int) x,
      double Function(double) y, Color color) {
    final path = Path()..moveTo(x(0), y(values[0]));
    for (var i = 1; i < values.length; i++) {
      path.lineTo(x(i), y(values[i]));
    }
    canvas.drawPath(path, Paint()
      ..color = color
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.4);
  }

  void _drawPlan(Canvas canvas, Size size, TradePlan plan, int first,
      double Function(int) x, double Function(double) y) {
    final startIndex = plan.signalBar - first;
    final startX = startIndex >= 0 ? x(startIndex) : 0.0;
    _dashed(canvas, startX, size.width, y(plan.target), DeskColors.buy);
    _dashed(canvas, startX, size.width, y(plan.entry), DeskColors.ink);
    _dashed(canvas, startX, size.width, y(plan.stop), DeskColors.sell);
    if (startIndex >= 0) {
      canvas.drawCircle(Offset(startX, y(plan.entry)), 4, Paint()..color = DeskColors.of(plan.direction));
    }
  }

  void _dashed(Canvas canvas, double from, double to, double y, Color color) {
    final paint = Paint()
      ..color = color.withValues(alpha: 0.8)
      ..strokeWidth = 1;
    for (var x = from; x < to; x += 8) {
      canvas.drawLine(Offset(x, y), Offset(math.min(x + 4, to), y), paint);
    }
  }

  @override
  bool shouldRepaint(_ChartPainter old) => true;
}
