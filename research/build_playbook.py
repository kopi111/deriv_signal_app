"""Pick one strategy per market from output/results.json and write the
app's playbook (../assets/strategies.json) plus output/REPORT.md.

Markets kopi asked for are always listed, proven or not. The best Jump
index is chosen by result. Other markets are listed if they pass, or if
they are a near miss: solid on unseen data but short of one check.
"""

import json
import math
from pathlib import Path

from data import GRANULARITY_SECONDS

HERE = Path(__file__).parent
RESULTS = HERE / "output" / "results.json"
REPORT = HERE / "output" / "REPORT.md"
PLAYBOOK = HERE.parent / "assets" / "strategies.json"
REQUESTED = ["R_100", "1HZ100V", "R_75", "1HZ75V", "stpRNG", "frxXAUUSD"]
JUMP_PREFIX = "JD"
NEAR_MISS = {"min_profit_factor": 1.3, "min_positive_folds": 4, "min_trades": 30}


def strength(result):
    oos = result["walk_forward"]
    return (1 if result["survives"] else 0, oos["expectancy_r"] * math.sqrt(max(oos["trades"], 1)))


def best_per_symbol(instruments):
    best = {}
    for run in instruments:
        for result in run["results"]:
            candidate = (strength(result), run, result)
            current = best.get(run["symbol"])
            if current is None or candidate[0] > current[0]:
                best[run["symbol"]] = candidate
    return best


def is_near_miss(result):
    oos = result["walk_forward"]
    return (oos["profit_factor"] >= NEAR_MISS["min_profit_factor"]
            and oos["trades"] >= NEAR_MISS["min_trades"]
            and result["positive_folds"] >= NEAR_MISS["min_positive_folds"]
            and result["lockbox"]["total_r"] >= 0)


def worth_listing(entry):
    score, _, result = entry
    return score[0] == 1 or is_near_miss(result)


def choose(best):
    jumps = [symbol for symbol in best if symbol.startswith(JUMP_PREFIX)]
    best_jump = max(jumps, key=lambda symbol: best[symbol][0]) if jumps else None
    requested = REQUESTED + ([best_jump] if best_jump else [])
    passing = [s for s, entry in best.items() if worth_listing(entry) and s not in requested]
    return requested + sorted(passing, key=lambda s: best[s][0], reverse=True)


FAILURE_EXPLANATIONS = {
    "enough trades": "too few trades to judge",
    "profit factor": "profit too thin after costs",
    "expectancy": "average win per trade too small",
    "consistent folds": "profitable in too few test periods",
    "beats random": "random entries did about as well",
    "lockbox not negative": "lost money on the newest data",
}


def explain(failed_checks):
    return [FAILURE_EXPLANATIONS[check] for check in failed_checks]


def playbook_row(run, result):
    return {
        "symbol": run["symbol"], "name": run["name"], "group": run["group"],
        "timeframe": run["timeframe"], "granularity": GRANULARITY_SECONDS[run["timeframe"]],
        "strategy": result["strategy"], "entry": result["params"]["entry"],
        "exit": result["params"]["exit"], "proven": result["survives"],
        "failed_checks": explain(result["failed_checks"]), "walk_forward": result["walk_forward"],
        "lockbox": result["lockbox"], "random_p": result["random_p"],
        "positive_folds": result["positive_folds"], "fold_count": len(result["folds"]),
        "tested_from": run["from"], "tested_to": run["to"],
    }


def report_table(instruments):
    lines = ["| Market | TF | Strategy | OOS trades | PF | Exp R | Total R | Folds + | Random p | Lockbox R | Verdict |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for run in instruments:
        for result in run["results"]:
            oos = result["walk_forward"]
            verdict = "PASS" if result["survives"] else "fail: " + ", ".join(result["failed_checks"])
            lines.append(f"| {run['name']} | {run['timeframe']} | {result['strategy']} | {oos['trades']} | "
                         f"{oos['profit_factor']} | {oos['expectancy_r']} | {oos['total_r']} | "
                         f"{result['positive_folds']}/{len(result['folds'])} | {result['random_p']} | "
                         f"{result['lockbox']['total_r']} | {verdict} |")
    return "\n".join(lines)


def main():
    payload = json.loads(RESULTS.read_text())
    best = best_per_symbol(payload["instruments"])
    rows = [playbook_row(best[symbol][1], best[symbol][2]) for symbol in choose(best)]
    passing = sum(1 for run in payload["instruments"] for r in run["results"] if r["survives"])
    tested = sum(len(run["results"]) for run in payload["instruments"])
    PLAYBOOK.parent.mkdir(exist_ok=True)
    PLAYBOOK.write_text(json.dumps({"generated": payload["generated"], "tested": tested,
                                    "passed": passing, "instruments": rows}, indent=1))
    REPORT.write_text(f"# Strategy research, {payload['generated'][:10]}\n\n"
                      f"{passing} of {tested} market/timeframe/strategy combinations passed every check.\n\n"
                      f"Rules: {payload['rules']}\n\nFeed failures: {payload['failures'] or 'none'}\n\n"
                      + report_table(payload["instruments"]) + "\n")
    for row in rows:
        oos = row["walk_forward"]
        print(f"{row['symbol']:10} {row['timeframe']:4} {row['strategy']:20} proven={row['proven']!s:5} "
              f"trades={oos['trades']} PF={oos['profit_factor']} totalR={oos['total_r']} p={row['random_p']} "
              f"lockbox={row['lockbox']['total_r']}")


if __name__ == "__main__":
    main()
