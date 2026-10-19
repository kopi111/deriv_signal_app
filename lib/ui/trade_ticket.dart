import 'package:flutter/material.dart';

import '../domain/strategies.dart' show price;
import '../domain/trade_plan.dart';
import '../state/instrument_board.dart';
import 'desk_theme.dart';
import 'price_ladder.dart';

/// The verdict: direction, status, the ladder of levels, and the live result.
class TradeTicket extends StatelessWidget {
  const TradeTicket({super.key, required this.board, required this.plan});

  final InstrumentBoard board;
  final TradePlan plan;

  @override
  Widget build(BuildContext context) {
    final color = DeskColors.of(plan.direction);
    final status = plan.statusOn(board.series);
    final live = board.lastPrice ?? plan.entry;
    return Container(
      padding: const EdgeInsets.fromLTRB(18, 16, 18, 18),
      decoration: BoxDecoration(
        color: DeskColors.surface,
        border: Border(top: BorderSide(color: color, width: 4)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              Text(plan.direction.label, style: DeskType.display(56, color: color)),
              const SizedBox(width: 14),
              Padding(
                padding: const EdgeInsets.only(bottom: 6),
                child: Text(status.label, style: DeskType.body(17, weight: FontWeight.w600)),
              ),
              const Spacer(),
              if (status.isOpen)
                Padding(
                  padding: const EdgeInsets.only(bottom: 6),
                  child: Text(_openResult(live), style: DeskType.figure(22, color: DeskColors.waiting)),
                ),
            ],
          ),
          const SizedBox(height: 4),
          Text(_signalLine(status), style: DeskType.body(14, color: DeskColors.muted)),
          const SizedBox(height: 16),
          PriceLadder(plan: plan, livePrice: live),
          const SizedBox(height: 8),
          Text(
            'Reward to risk ${plan.rewardRisk.toStringAsFixed(1)} : 1. '
            'Stop ${price(plan.riskDistance)} away, target ${price(plan.rewardDistance)} away. '
            'Close by hand if neither is hit within ${TradePlan.maxHoldBars} candles.',
            style: DeskType.body(14, color: DeskColors.muted),
          ),
        ],
      ),
    );
  }

  String _openResult(double live) {
    final r = plan.openResultInR(live);
    return '${r >= 0 ? '+' : ''}${r.toStringAsFixed(2)}R now';
  }

  String _signalLine(PlanStatus status) {
    final at = DateTime.fromMillisecondsSinceEpoch(plan.signalEpoch * 1000).toLocal();
    final time = '${at.day}/${at.month} ${at.hour.toString().padLeft(2, '0')}:${at.minute.toString().padLeft(2, '0')}';
    final candles = board.series.lastIndex - plan.signalBar;
    return switch (status) {
      PlanStatus.enterNow => 'Signal on the candle that opened $time. Enter at market now.',
      PlanStatus.running => 'Signal on the $time candle, $candles candles ago. Only enter late if price is still near the entry.',
      _ => 'Signal on the $time candle. This trade is finished; wait for the next one.',
    };
  }
}
