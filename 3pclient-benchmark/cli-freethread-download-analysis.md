# CLI Free-Threading Download — AwsEventLoop CPU Profile Analysis

**Profile source:** `cli-freethread-download.html`
**Tool:** `analyze_aws_event_loops.py`

## Summary

The flame graph profile of `cli-crt` with Python 3.14t free-threading (no GIL) shows that **`AwsEventLoop` threads collectively consumed 69.37%** of all CPU samples. A total of **39 AwsEventLoop thread entries** were captured across 36 unique thread IDs (threads 1, 2, and 3 appear more than once at different stack depths).

---

## All AwsEventLoop Threads by CPU % (sorted)

| Thread | CPU % |
|---|---|
| AwsEventLoop24 | 11.01% ⚠ outlier |
| AwsEventLoop23 | 3.21% |
| AwsEventLoop14 | 2.28% |
| AwsEventLoop5  | 2.27% |
| AwsEventLoop19 | 2.26% |
| AwsEventLoop10 | 2.22% |
| AwsEventLoop33 | 2.09% |
| AwsEventLoop11 | 2.09% |
| AwsEventLoop26 | 2.07% |
| AwsEventLoop2  | 1.99% |
| AwsEventLoop8  | 1.93% |
| AwsEventLoop35 | 1.92% |
| AwsEventLoop18 | 1.85% |
| AwsEventLoop15 | 1.84% |
| AwsEventLoop4  | 1.84% |
| AwsEventLoop20 | 1.83% |
| AwsEventLoop17 | 1.82% |
| AwsEventLoop30 | 1.78% |
| AwsEventLoop31 | 1.46% |
| AwsEventLoop29 | 1.46% |
| AwsEventLoop25 | 1.45% |
| AwsEventLoop32 | 1.42% |
| AwsEventLoop34 | 1.37% |
| AwsEventLoop1  | 1.37% |
| AwsEventLoop9  | 1.34% |
| AwsEventLoop36 | 1.31% |
| AwsEventLoop13 | 1.29% |
| AwsEventLoop6  | 1.25% |
| AwsEventLoop16 | 1.23% |
| AwsEventLoop21 | 1.18% |
| AwsEventLoop22 | 1.14% |
| AwsEventLoop28 | 1.11% |
| AwsEventLoop7  | 0.97% |
| AwsEventLoop27 | 0.96% |
| AwsEventLoop12 | 0.89% |
| AwsEventLoop3  | 0.73% |
| *(duplicate entries for threads 2, 1, 3)* | ≤ 0.40% each |

---

## Aggregate Statistics

| Metric | Value |
|---|---|
| **Total AwsEventLoop CPU %** | **69.37%** |
| Number of flame graph entries | 39 |
| Unique thread count | 36 |
| Highest single thread (AwsEventLoop24) | 11.01% |
| Lowest unique thread (AwsEventLoop3) | 0.73% |

---

## Observations

- **AwsEventLoop24 is a dramatic outlier** at 11.01% — more than 3× the next highest thread (AwsEventLoop23 at 3.21%). This is the largest single-thread outlier across all profiles analyzed and likely represents a hot connection or uneven scheduling in this run.
- Outside of the outlier, threads are **reasonably well distributed** from 0.73% to 3.21%.
- At **69.37%**, the free-threading profile falls between the CLI default (62.33%) and the Java TM (72.29%) — consistent with the +40% throughput gain (3.7 → 5.18 Gb/s). Removing the GIL allows more CPU to reach CRT native threads.

---

## Comparison with Other Profiles

| Profile | AwsEventLoop % | Unique Threads | Top Outlier | Throughput |
|---|---|---|---|---|
| `crt-python-default.html` | **93.97%** | 36 | AwsEventLoop12 (6.23%) | 54.6 Gb/s |
| `java-crt-client.html` | 75.01% | 79 | AwsEventLoop55 (3.04%) | 22.88 Gb/s |
| `java-crt-transfer-manager.html` | 72.29% | 77 | AwsEventLoop51 (5.25%) | 8.48 Gb/s |
| **`cli-freethread-download.html`** | **69.37%** | **36** | **AwsEventLoop24 (11.01%)** | **5.18 Gb/s** |
| `cli-perf-profile.html` (with GIL) | 62.33% | 36 | AwsEventLoop15 (6.68%) | 3.7 Gb/s |

Free-threading raises the CRT share from 62.33% to 69.37% (+7 percentage points), confirming that removing the GIL frees up CPU that was previously blocked on Python thread switching — and redirects it to native I/O work.