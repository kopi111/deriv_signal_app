enum TradeDirection {
  buy(1, 'Buy'),
  sell(-1, 'Sell');

  const TradeDirection(this.sign, this.label);
  final int sign;
  final String label;
}

/// One rule of a setup, with the live numbers that decided it.
class Condition {
  const Condition(this.label, this.met, this.evidence);

  final String label;
  final bool met;
  final String evidence;
}

/// Every condition a strategy needs for one direction, evaluated on one bar.
class SetupCheck {
  const SetupCheck(this.direction, this.conditions);

  final TradeDirection direction;
  final List<Condition> conditions;

  bool get triggered => conditions.every((condition) => condition.met);
  int get metCount => conditions.where((condition) => condition.met).length;
}
