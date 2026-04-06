# AwsEventLoop CPU Profile Analysis — New Profiles

**Profiles analyzed:**
- `3pclient-benchmark/cli-default.html`
- `3pclient-benchmark/java-tm-crt-default.html`

---

## CLI Default (`cli-default.html`)

### Summary

**`AwsEventLoop` threads collectively consumed 62.33%** of all CPU samples across **36 entries** (36 unique thread IDs).

### All AwsEventLoop Threads by CPU % (sorted)

| Thread | CPU % |
|---|---|
| AwsEventLoop15 | 6.68% |
| AwsEventLoop16 | 2.08% |
| AwsEventLoop24 | 2.03% |
| AwsEventLoop26 | 1.92% |
| AwsEventLoop30 | 1.92% |
| AwsEventLoop13 | 1.90% |
| AwsEventLoop31 | 1.88% |
| AwsEventLoop32 | 1.88% |
| AwsEventLoop25 | 1.87% |
| AwsEventLoop20 | 1.85% |
| AwsEventLoop8  | 1.85% |
| AwsEventLoop35 | 1.83% |
| AwsEventLoop7  | 1.79% |
| AwsEventLoop5  | 1.78% |
| AwsEventLoop9  | 1.71% |
| AwsEventLoop17 | 1.69% |
| AwsEventLoop27 | 1.68% |
| AwsEventLoop23 | 1.64% |
| AwsEventLoop12 | 1.60% |
| AwsEventLoop22 | 1.59% |
| AwsEventLoop18 | 1.58% |
| AwsEventLoop19 | 1.54% |
| AwsEventLoop6  | 1.52% |
| AwsEventLoop11 | 1.52% |
| AwsEventLoop28 | 1.51% |
| AwsEventLoop1  | 1.41% |
| AwsEventLoop10 | 1.38% |
| AwsEventLoop29 | 1.35% |
| AwsEventLoop4  | 1.35% |
| AwsEventLoop33 | 1.30% |
| AwsEventLoop36 | 1.28% |
| AwsEventLoop2  | 1.25% |
| AwsEventLoop21 | 1.24% |
| AwsEventLoop34 | 1.11% |
| AwsEventLoop3  | 0.93% |
| AwsEventLoop14 | 0.89% |

### Aggregate Statistics

| Metric | Value |
|---|---|
| **Total AwsEventLoop CPU %** | **62.33%** |
| Number of flame graph entries | 36 |
| Highest single thread (AwsEventLoop15) | 6.68% |
| Lowest single thread (AwsEventLoop14) | 0.89% |

### Observations

- **AwsEventLoop15 is the outlier** at 6.68% — roughly 3× the next highest thread (AwsEventLoop16 at 2.08%).
- The remaining 35 threads are **very tightly clustered** between 0.89% and 2.08%, indicating excellent load distribution across the event loop threads.
- At **62.33%**, the CLI default configuration dedicates a large majority of CPU time to CRT native I/O threads.

---

## Java TM CRT Default (`java-tm-crt-default.html`)

### Summary

**`AwsEventLoop` threads collectively consumed 72.29%** of all CPU samples across **77 entries** (73 unique thread IDs, with a few threads appearing more than once at different stack depths).

### All AwsEventLoop Threads by CPU % (sorted)

| Thread | CPU % |
|---|---|
| AwsEventLoop51 | 5.25% |
| AwsEventLoop52 | 1.46% |
| AwsEventLoop23 | 1.38% |
| AwsEventLoop19 | 1.34% |
| AwsEventLoop2  | 1.30% |
| AwsEventLoop17 | 1.24% |
| AwsEventLoop14 | 1.25% |
| AwsEventLoop24 | 1.23% |
| AwsEventLoop70 | 1.22% |
| AwsEventLoop11 | 1.21% |
| AwsEventLoop39 | 1.21% |
| AwsEventLoop49 | 1.20% |
| AwsEventLoop50 | 1.19% |
| AwsEventLoop56 | 1.19% |
| AwsEventLoop58 | 1.16% |
| AwsEventLoop54 | 1.15% |
| AwsEventLoop62 | 1.15% |
| AwsEventLoop38 | 1.14% |
| AwsEventLoop48 | 1.12% |
| AwsEventLoop22 | 1.11% |
| AwsEventLoop61 | 1.10% |
| AwsEventLoop57 | 1.02% |
| AwsEventLoop29 | 1.02% |
| AwsEventLoop69 | 1.01% |
| AwsEventLoop1  | 0.98% |
| AwsEventLoop13 | 0.98% |
| AwsEventLoop9  | 0.98% |
| AwsEventLoop6  | 0.98% |
| AwsEventLoop64 | 0.97% |
| AwsEventLoop10 | 0.97% |
| AwsEventLoop15 | 0.96% |
| AwsEventLoop28 | 0.95% |
| AwsEventLoop37 | 0.94% |
| AwsEventLoop32 | 0.92% |
| AwsEventLoop12 | 0.92% |
| AwsEventLoop42 | 0.92% |
| AwsEventLoop27 | 0.91% |
| AwsEventLoop63 | 0.89% |
| AwsEventLoop44 | 0.89% |
| AwsEventLoop45 | 0.87% |
| AwsEventLoop35 | 0.86% |
| AwsEventLoop26 | 0.85% |
| AwsEventLoop21 | 0.84% |
| AwsEventLoop33 | 0.83% |
| AwsEventLoop43 | 0.83% |
| AwsEventLoop68 | 0.81% |
| AwsEventLoop7  | 0.81% |
| AwsEventLoop30 | 0.80% |
| AwsEventLoop65 | 0.84% |
| AwsEventLoop53 | 0.88% |
| AwsEventLoop31 | 0.78% |
| AwsEventLoop67 | 0.78% |
| AwsEventLoop4  | 0.78% |
| AwsEventLoop59 | 0.77% |
| AwsEventLoop41 | 0.76% |
| AwsEventLoop40 | 0.76% |
| AwsEventLoop25 | 0.75% |
| AwsEventLoop46 | 0.75% |
| AwsEventLoop16 | 0.74% |
| AwsEventLoop18 | 0.74% |
| AwsEventLoop20 | 0.74% |
| AwsEventLoop47 | 0.74% |
| AwsEventLoop66 | 0.73% |
| AwsEventLoop60 | 0.71% |
| AwsEventLoop36 | 0.70% |
| AwsEventLoop34 | 0.66% |
| AwsEventLoop71 | 0.66% |
| AwsEventLoop55 | 0.53% |
| AwsEventLoop8  | 0.49% |
| AwsEventLoop72 | 0.31% |
| *(small duplicate entries for threads 3, 1, 7, 5, 2)* | ≤ 0.03% each |

### Aggregate Statistics

| Metric | Value |
|---|---|
| **Total AwsEventLoop CPU %** | **72.29%** |
| Number of flame graph entries | 77 |
| Highest single thread (AwsEventLoop51) | 5.25% |
| Lowest unique thread (AwsEventLoop72) | 0.31% |

### Observations

- **AwsEventLoop51 is the outlier** at 5.25% — roughly 3.6× the next highest thread (AwsEventLoop52 at 1.46%).
- The remaining threads are mostly clustered between 0.31% and 1.46%, with good overall load balancing.
- At **72.29%**, the Java TM CRT Default profile dedicates nearly three-quarters of all CPU to event loop threads — consistent with a heavily I/O-bound workload.

---

## Side-by-Side Comparison

| Metric | CLI Default | Java TM CRT Default |
|---|---|---|
| **Total AwsEventLoop CPU %** | **62.33%** | **72.29%** |
| Number of entries | 36 | 77 |
| Unique thread count | 36 | 73 |
| Top outlier thread | AwsEventLoop15 (6.68%) | AwsEventLoop51 (5.25%) |
| Typical thread range | 0.89% – 2.08% | 0.31% – 1.46% |
| Thread distribution | Very tight cluster | Tight cluster |

**Key takeaways:**
- Both profiles show a single hot outlier thread (~5–7%) with the rest well load-balanced.
- The Java TM CRT Default uses **2× more event loop threads** (73 vs. 36), consistent with a higher-concurrency transfer manager configuration.
- The Java TM CRT Default has a **higher total AwsEventLoop share** (72.29% vs. 62.33%), indicating more of its CPU budget goes to native I/O compared to the CLI default configuration.