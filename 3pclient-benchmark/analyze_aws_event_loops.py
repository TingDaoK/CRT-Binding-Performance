#!/usr/bin/env python3
"""
Analyze AwsEventLoop* CPU% from perf flamegraph HTML files.

Usage:
    python3 analyze_aws_event_loops.py <file1.html> [file2.html ...]

Example:
    python3 analyze_aws_event_loops.py cli-default.html java-tm-crt-default.html crt-python-default.html
"""

import re
import sys
from pathlib import Path


def analyze(filepath: str) -> dict:
    content = Path(filepath).read_text(encoding="utf-8")
    matches = re.findall(
        r'<title>(AwsEventLoop\S*)\s+\([^)]+,\s*([\d.]+)%\)</title>', content
    )
    total = sum(float(pct) for _, pct in matches)
    entries = [(name, float(pct)) for name, pct in matches]
    entries_sorted = sorted(entries, key=lambda x: x[1], reverse=True)
    return {
        "file": filepath,
        "entries": entries_sorted,
        "total": total,
        "count": len(entries),
    }


def print_report(result: dict):
    print(f"\n{'='*60}")
    print(f"File: {result['file']}")
    print(f"{'='*60}")
    print(f"{'Thread':<25} {'CPU %':>8}")
    print(f"{'-'*34}")
    for name, pct in result["entries"]:
        marker = "  ← outlier" if pct == result["entries"][0][1] and pct > 3 else ""
        print(f"{name:<25} {pct:>7.2f}%{marker}")
    print(f"{'-'*34}")
    print(f"{'TOTAL':<25} {result['total']:>7.2f}%")
    print(f"{'Entries':<25} {result['count']:>7}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    results = []
    for filepath in sys.argv[1:]:
        try:
            result = analyze(filepath)
            print_report(result)
            results.append(result)
        except FileNotFoundError:
            print(f"ERROR: File not found: {filepath}", file=sys.stderr)

    if len(results) > 1:
        print(f"\n{'='*60}")
        print("COMPARISON SUMMARY")
        print(f"{'='*60}")
        print(f"{'File':<40} {'AwsEventLoop %':>16} {'Threads':>8} {'Top Outlier':>20}")
        print(f"{'-'*86}")
        for r in results:
            top_name, top_pct = r["entries"][0] if r["entries"] else ("n/a", 0)
            print(
                f"{Path(r['file']).name:<40} {r['total']:>15.2f}% {r['count']:>8}   {top_name} ({top_pct:.2f}%)"
            )


if __name__ == "__main__":
    main()