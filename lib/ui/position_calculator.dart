import 'package:flutter/material.dart';

import '../domain/playbook.dart';
import '../domain/trade_plan.dart';
import 'desk_theme.dart';

/// Turns "risk 1% of my account" into a volume for this trade's stop.
class PositionCalculator extends StatefulWidget {
  const PositionCalculator({super.key, required this.entry, required this.plan});

  final PlaybookEntry entry;
  final TradePlan plan;

  @override
  State<PositionCalculator> createState() => _PositionCalculatorState();
}

class _PositionCalculatorState extends State<PositionCalculator> {
  double balance = 1000;
  double riskPercent = 1;

  double get riskAmount => balance * riskPercent / 100;

  @override
  Widget build(BuildContext context) {
    final sizing = LotSizing.forSymbol(widget.entry.symbol, widget.entry.group);
    final lots = sizing.lotsFor(riskAmount, widget.plan);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            Expanded(child: _field('Account balance (USD)', balance, (v) => balance = v)),
            const SizedBox(width: 12),
            Expanded(child: _field('Risk per trade (%)', riskPercent, (v) => riskPercent = v)),
          ],
        ),
        const SizedBox(height: 14),
        Text('You risk \$${riskAmount.toStringAsFixed(2)} to make '
            '\$${(riskAmount * widget.plan.rewardRisk).toStringAsFixed(2)}.',
            style: DeskType.body(16, weight: FontWeight.w600)),
        const SizedBox(height: 4),
        Text(
          lots == null
              ? 'Volume: this pair is priced in a non-USD currency, size it in MT5.'
              : 'Volume ≈ ${lots.toStringAsFixed(sizing.decimals)} lots '
                  '(contract size ${sizing.contractSize.toStringAsFixed(0)}). '
                  'Check the symbol’s contract size in MT5 before trading.',
          style: DeskType.body(14, color: DeskColors.muted),
        ),
      ],
    );
  }

  Widget _field(String label, double value, void Function(double) assign) {
    return TextFormField(
      initialValue: value.toStringAsFixed(value % 1 == 0 ? 0 : 2),
      keyboardType: const TextInputType.numberWithOptions(decimal: true),
      style: DeskType.figure(18),
      decoration: InputDecoration(labelText: label),
      onChanged: (text) {
        final parsed = double.tryParse(text);
        if (parsed != null && parsed > 0) setState(() => assign(parsed));
      },
    );
  }
}

class LotSizing {
  const LotSizing(this.contractSize, this.quoteIsUsd, this.baseIsUsd, this.decimals);

  factory LotSizing.forSymbol(String symbol, String group) {
    final pair = symbol.replaceFirst('frx', '');
    return switch (group) {
      'Forex' => LotSizing(100000, pair.endsWith('USD'), pair.startsWith('USD'), 2),
      'Metals' => LotSizing(pair.startsWith('XAG') ? 5000 : 100, true, false, 2),
      _ => const LotSizing(1, true, false, 3),
    };
  }

  final double contractSize;
  final bool quoteIsUsd;
  final bool baseIsUsd;
  final int decimals;

  double? lotsFor(double riskUsd, TradePlan plan) {
    final lossPerLotInQuote = plan.riskDistance * contractSize;
    if (quoteIsUsd) return riskUsd / lossPerLotInQuote;
    if (baseIsUsd) return riskUsd / (lossPerLotInQuote / plan.entry);
    return null;
  }
}
