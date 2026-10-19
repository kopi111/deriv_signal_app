/// Research verdict for one instrument, read from assets/strategies.json.
class PlaybookEntry {
  PlaybookEntry.fromJson(Map<String, dynamic> json)
      : symbol = json['symbol'] as String,
        name = json['name'] as String,
        group = json['group'] as String,
        timeframe = json['timeframe'] as String,
        granularitySeconds = json['granularity'] as int,
        strategyId = json['strategy'] as String,
        entryParams = (json['entry'] as Map).cast<String, num>(),
        stopAtr = (json['exit']['stop_atr'] as num).toDouble(),
        rewardRisk = (json['exit']['reward_risk'] as num).toDouble(),
        proven = json['proven'] as bool,
        failedChecks = (json['failed_checks'] as List).cast<String>(),
        outOfSample = TestResult.fromJson(json['walk_forward'] as Map<String, dynamic>),
        lockbox = TestResult.fromJson(json['lockbox'] as Map<String, dynamic>),
        randomBeatShare = (json['random_p'] as num).toDouble(),
        positiveFolds = json['positive_folds'] as int,
        foldCount = json['fold_count'] as int,
        testedFrom = json['tested_from'] as String,
        testedTo = json['tested_to'] as String;

  final String symbol;
  final String name;
  final String group;
  final String timeframe;
  final int granularitySeconds;
  final String strategyId;
  final Map<String, num> entryParams;
  final double stopAtr;
  final double rewardRisk;
  final bool proven;
  final List<String> failedChecks;
  final TestResult outOfSample;
  final TestResult lockbox;
  final double randomBeatShare;
  final int positiveFolds;
  final int foldCount;
  final String testedFrom;
  final String testedTo;

  bool get isSynthetic => group == 'Synthetic';
}

class TestResult {
  TestResult.fromJson(Map<String, dynamic> json)
      : trades = json['trades'] as int,
        winRate = (json['win_rate'] as num).toDouble(),
        profitFactor = (json['profit_factor'] as num).toDouble(),
        expectancyR = (json['expectancy_r'] as num).toDouble(),
        totalR = (json['total_r'] as num).toDouble(),
        maxDrawdownR = (json['max_drawdown_r'] as num).toDouble();

  final int trades;
  final double winRate;
  final double profitFactor;
  final double expectancyR;
  final double totalR;
  final double maxDrawdownR;
}

class Playbook {
  Playbook.fromJson(Map<String, dynamic> json)
      : generated = json['generated'] as String,
        testedCount = json['tested'] as int,
        passedCount = json['passed'] as int,
        entries = [
          for (final row in (json['instruments'] as List).cast<Map<String, dynamic>>())
            PlaybookEntry.fromJson(row),
        ];

  final String generated;
  final int testedCount;
  final int passedCount;
  final List<PlaybookEntry> entries;
}
