"""Build the S/R range-fade report from every result file in the output folder."""

import json
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "output" / "sr_range_fade"
REPORT = OUTPUT_DIR / "REPORT.md"
HEADER = ("| Market | Trigger | WF trades | Win | WF exp | WF PF | Lockbox exp | p vs random | Folds up | Verdict | Strict |\n"
          "|---|---|---|---|---|---|---|---|---|---|---|\n")
STRICT_FOLD_SHARE = 2 / 3


def load(*patterns):
    results = []
    for pattern in patterns:
        for path in sorted(OUTPUT_DIR.glob(pattern)):
            payload = json.loads(path.read_text())
            results += payload["results"] if isinstance(payload, dict) else payload
    return results


def folds_up(result):
    """Test folds whose R total is positive: an edge should not live in one fold."""
    folds = result["folds"]
    return sum(1 for fold in folds if fold["total_r"] > 0), len(folds)


def strict_verdict(result):
    """The published rule plus fold consistency, since the loose rule passes noise."""
    up, total = folds_up(result)
    if result["verdict"] != "PASS":
        return "FAIL"
    return "PASS" if up >= STRICT_FOLD_SHARE * total else "FAIL"


def row(result):
    walk, lock = result["walk_forward"], result["lockbox"]
    up, total = folds_up(result)
    return (f"| {result['name']} | {result['trigger']} | {walk['trades']} | "
            f"{walk['win_rate']:.1%} | {walk['expectancy_r']:+.3f}R | {walk['profit_factor']:.2f} | "
            f"{lock['expectancy_r']:+.3f}R | {result['beat_random_p']} | {up}/{total} | "
            f"{result['verdict']} | {strict_verdict(result)} |")


def table(results):
    ordered = sorted(results, key=lambda r: (r["trigger"], -r["walk_forward"]["expectancy_r"]))
    return HEADER + "\n".join(row(result) for result in ordered) + "\n"


def pass_rate(results, trigger=None, rule="verdict"):
    chosen = [r for r in results if trigger is None or r["trigger"] == trigger]
    if not chosen:
        return "no tests"
    verdict = (lambda r: r["verdict"]) if rule == "verdict" else strict_verdict
    passes = sum(1 for r in chosen if verdict(r) == "PASS")
    return f"{passes}/{len(chosen)} ({passes / len(chosen):.0%})"


def section(title, results):
    if not results:
        return f"## {title}\n\nNo results.\n"
    return (f"## {title}\n\nPublished rule {pass_rate(results)} — "
            f"limit {pass_rate(results, 'limit')}, rejection {pass_rate(results, 'rejection')}. "
            f"Strict rule {pass_rate(results, rule='strict')} — "
            f"limit {pass_rate(results, 'limit', 'strict')}, "
            f"rejection {pass_rate(results, 'rejection', 'strict')}.\n\n"
            + table(results))


def calibration_note(groups):
    """State the false-pass rates, since a PASS only means as much as they allow."""
    lines = ["## What a PASS is worth", "",
             "Every rate below comes from the same test run on random walks, which hold no",
             "support or resistance at all, so each PASS there is a false pass.", ""]
    for title, results in groups:
        if "Luck check" in title and results:
            lines.append(f"- {title}: {pass_rate(results, 'limit')} on the limit trigger, "
                         f"{pass_rate(results, 'rejection')} on rejection.")
    return "\n".join(lines) + "\n\n"


def reproduction_table(groups):
    """Where a market passed, what the same market did in every other run."""
    passed = {result["symbol"] for _, results in groups
              for result in results if result["verdict"] == "PASS"
              and not result["symbol"].startswith("RANDOM_")}
    if not passed:
        return ""
    lines = ["## Did a pass reproduce?", "",
             "A level that is really there should hold at another granularity and in",
             "another year. Walk-forward expectancy on the limit trigger, by run:", "",
             "| Market | " + " | ".join(title for title, results in groups
                                        if results and "Luck check" not in title) + " |",
             "|---" * (1 + sum(1 for title, results in groups
                               if results and "Luck check" not in title)) + "|"]
    for symbol in sorted(passed):
        cells = []
        for title, results in groups:
            if not results or "Luck check" in title:
                continue
            found = [r for r in results if r["symbol"] == symbol and r["trigger"] == "limit"]
            cells.append(f"{found[0]['walk_forward']['expectancy_r']:+.3f}R "
                         f"({found[0]['walk_forward']['trades']}) {found[0]['verdict']}"
                         if found else "not run")
        lines.append(f"| {symbol} | " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n\n"


def main():
    groups = [
        ("Deriv synthetics from the chart photos, 15m", load("results_15m.json")),
        ("Forex pairs and metals, 15m", load("results_15m_pairs_*.json")),
        ("Deriv synthetics from the chart photos, 5m",
         load("results_5m.json", "results_5m_photogroup_*.json")),
        ("Forex pairs and metals, 5m", load("results_5m_pairs_*.json")),
        ("Ten years of Dukascopy hourly history, 1h", load("results_long_1h*.json")),
        ("Luck check: random walks matched to a pair, 15m", load("luck_15m_flat_like-*.json")),
        ("Luck check: random walks matched to a pair, 5m", load("luck_5m_flat_like-*.json")),
        ("Luck check: random walks at synthetic volatility, 15m",
         load("luck_15m.json", "luck_15m_flat_limit.json", "luck_15m_flat_rejection.json")),
    ]
    body = calibration_note(groups) + reproduction_table(groups) + "\n".join(
        section(title, results) for title, results in groups)
    REPORT.write_text("# Support/resistance range fade\n\n" + body)
    print(f"wrote {REPORT}")
    for title, results in groups:
        print(f"{title}: {pass_rate(results)}")


if __name__ == "__main__":
    main()
