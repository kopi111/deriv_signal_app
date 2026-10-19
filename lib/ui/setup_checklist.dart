import 'package:flutter/material.dart';

import '../domain/setup_check.dart';
import 'desk_theme.dart';

/// The entry rule as a checklist: each line is a condition with the live
/// numbers that decided it. All ticked means the strategy fires.
class SetupChecklist extends StatelessWidget {
  const SetupChecklist({super.key, required this.setup});

  final SetupCheck setup;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [for (final condition in setup.conditions) _ConditionRow(condition)],
    );
  }
}

class _ConditionRow extends StatelessWidget {
  const _ConditionRow(this.condition);

  final Condition condition;

  @override
  Widget build(BuildContext context) {
    final color = condition.met ? DeskColors.buy : DeskColors.muted;
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Icon(condition.met ? Icons.check_circle : Icons.radio_button_unchecked, size: 20, color: color),
          const SizedBox(width: 10),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(condition.label,
                    style: DeskType.body(15, color: condition.met ? DeskColors.ink : DeskColors.muted)),
                if (condition.evidence.isNotEmpty)
                  Text(condition.evidence, style: DeskType.figure(14, color: DeskColors.muted)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
