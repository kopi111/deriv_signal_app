import 'package:flutter/material.dart';

import '../domain/strategies.dart' show price;
import '../domain/trade_plan.dart';
import 'desk_theme.dart';

/// Target, entry and stop drawn to scale, with the live price as a marker.
/// The reward and risk bands are proportional, so 2:1 looks like 2:1.
class PriceLadder extends StatelessWidget {
  const PriceLadder({super.key, required this.plan, required this.livePrice});

  final TradePlan plan;
  final double livePrice;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 190,
      child: CustomPaint(
        painter: _LadderPainter(plan, livePrice),
        child: const SizedBox.expand(),
      ),
    );
  }
}

class _LadderPainter extends CustomPainter {
  _LadderPainter(this.plan, this.livePrice);

  final TradePlan plan;
  final double livePrice;
  static const _barLeft = 0.0;
  static const _barWidth = 14.0;

  @override
  void paint(Canvas canvas, Size size) {
    final high = [plan.target, plan.stop, livePrice].reduce((a, b) => a > b ? a : b);
    final low = [plan.target, plan.stop, livePrice].reduce((a, b) => a < b ? a : b);
    double y(double value) => 8 + (high - value) / (high - low) * (size.height - 16);

    _band(canvas, y(plan.target), y(plan.entry), DeskColors.buy.withValues(alpha: 0.55));
    _band(canvas, y(plan.entry), y(plan.stop), DeskColors.sell.withValues(alpha: 0.55));
    _level(canvas, size, y(plan.target), 'Take profit', plan.target, DeskColors.buy);
    _level(canvas, size, y(plan.entry), 'Entry', plan.entry, DeskColors.ink);
    _level(canvas, size, y(plan.stop), 'Stop loss', plan.stop, DeskColors.sell);
    _liveMarker(canvas, y(livePrice));
  }

  void _band(Canvas canvas, double top, double bottom, Color color) {
    final rect = Rect.fromLTRB(_barLeft, top < bottom ? top : bottom, _barLeft + _barWidth,
        top < bottom ? bottom : top);
    canvas.drawRect(rect, Paint()..color = color);
  }

  void _level(Canvas canvas, Size size, double y, String label, double value, Color color) {
    canvas.drawLine(Offset(_barWidth + 6, y), Offset(size.width, y),
        Paint()
          ..color = color.withValues(alpha: 0.35)
          ..strokeWidth = 1);
    _text(canvas, label, DeskType.body(13, color: DeskColors.muted), Offset(_barWidth + 12, y - 19));
    final figure = _layout(price(value), DeskType.figure(18, color: color));
    figure.paint(canvas, Offset(size.width - figure.width, y - 22));
  }

  void _liveMarker(Canvas canvas, double y) {
    final path = Path()
      ..moveTo(_barWidth + 1, y)
      ..lineTo(_barWidth + 9, y - 5)
      ..lineTo(_barWidth + 9, y + 5)
      ..close();
    canvas.drawPath(path, Paint()..color = DeskColors.waiting);
  }

  void _text(Canvas canvas, String text, TextStyle style, Offset at) =>
      _layout(text, style).paint(canvas, at);

  TextPainter _layout(String text, TextStyle style) =>
      TextPainter(text: TextSpan(text: text, style: style), textDirection: TextDirection.ltr)
        ..layout();

  @override
  bool shouldRepaint(_LadderPainter old) => old.livePrice != livePrice || old.plan != plan;
}
