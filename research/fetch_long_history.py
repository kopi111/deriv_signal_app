"""Download multi-year hourly bid candles from Dukascopy, one year at a
time, retrying each year until it covers its full range. Dukascopy
throttles bulk downloads, so partial files are common; every year is
checked before it is accepted."""

import subprocess
import sys
import time
from pathlib import Path

import pandas as pd

LONG_DIR = Path(__file__).parent / "cache" / "long"
YEARS_DIR = LONG_DIR / "years"
FIRST_YEAR, LAST_DATE = 2016, "2026-09-17"
ATTEMPTS = 6
COVERAGE_SLACK_DAYS = 10


def download_year(instrument, year):
    start = f"{year}-01-01"
    end = LAST_DATE if year == int(LAST_DATE[:4]) else f"{year + 1}-01-01"
    target = YEARS_DIR / f"{instrument}-{year}.csv"
    for attempt in range(1, ATTEMPTS + 1):
        folder = YEARS_DIR / f"tmp-{instrument}-{year}"
        folder.mkdir(parents=True, exist_ok=True)
        subprocess.run(["npx", "--yes", "dukascopy-node", "-i", instrument, "-from", start, "-to", end,
                        "-t", "h1", "-f", "csv", "-v", "-dir", str(folder), "-r", "5", "-bs", "2", "-bp", "2000"],
                       capture_output=True, timeout=900)
        files = list(folder.glob("*.csv"))
        if files and _covers(files[0], end):
            files[0].rename(target)
            folder.rmdir()
            return target
        for stale in files:
            stale.unlink()
        print(f"  {instrument} {year}: incomplete (attempt {attempt}), pausing", flush=True)
        time.sleep(30 * attempt)
    raise RuntimeError(f"{instrument} {year}: never downloaded in full")


def _covers(path, end):
    if path.stat().st_size == 0:
        return False
    last = pd.to_datetime(pd.read_csv(path)["timestamp"].max(), unit="ms")
    return (pd.Timestamp(end) - last).days <= COVERAGE_SLACK_DAYS


def assemble(instrument):
    frames = [pd.read_csv(path) for path in sorted(YEARS_DIR.glob(f"{instrument}-*.csv"))]
    whole = pd.concat(frames).drop_duplicates("timestamp").sort_values("timestamp")
    whole.to_csv(LONG_DIR / f"{instrument}.csv", index=False)
    return len(whole)


def main(instruments):
    YEARS_DIR.mkdir(parents=True, exist_ok=True)
    for instrument in instruments:
        for year in range(FIRST_YEAR, int(LAST_DATE[:4]) + 1):
            if not (YEARS_DIR / f"{instrument}-{year}.csv").exists():
                download_year(instrument, year)
        print(f"{instrument}: {assemble(instrument)} bars", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
