# Lane B round 2, pilot 1: result

**Outcome: decision rule 2 fired, with weak evidence.** No colorable TSD instance with ρ above 0.857 was found at any tested span m ≥ 100. This is below the pre-registered threshold of 0.90, so NTSD with β around 0.1 is consistent with the data. This is evidence only, at small spans; nothing follows for spans near 2.2·10^7.

- **Run:** `ntsd_search.py`, seed 20261122, 780 s, 1 worker.
- **Results:** `ntsd_search_results.json` and `greedy_baseline_no_coloring.json`.
- **Validation:** every reported instance was re-checked by `check_tsd` against every L. The solver agrees with brute force on 300 small instances, 25 of them uncolorable.
- **Q(m):** the optimal Golomb ruler lengths, cited from memory. The recalled rulers for 10–14 marks were verified to be Sidon and of the tabulated length. Ratios against the elementary upper bound on Q, which are conservative, are stored too.

## Data

| Family | Span m | min(\|A\|,\|B\|) | Q(m) | ρ |
|---|---:|---:|---:|---:|
| Greedy growth, colorable | 97 | 10 | 12 | 0.833 |
| Greedy growth, colorable | 146 | 12 | 14 | 0.857 |
| Greedy growth, colorable | 193 | 13 | 16 | 0.813 |
| Greedy growth, colorable | 297 | 15 | 20 | 0.750 |
| Same greedy, **no coloring constraint** (baseline) | 100 / 150 / 200 / 300 | 11 / 13 / 14 / 17 | 12 / 14 / 17 / 20 | 0.917 / 0.929 / 0.824 / 0.850 |
| Optimal-ruler translate or reflection pairs, trimmed until colorable | 58–132 | 6–9 | 10–14 | 0.57–0.73 |

## Reading

1. **Greedy search is a weak test.** The plain greedy search for disjoint Sidon pairs, ignoring colorability, already stops at ρ ≈ 0.82–0.93. The coloring constraint lowers greedy results by roughly one or two points per set. The numbers therefore bound what this search can reach, not what TSD instances can reach.
2. **The informative data is the near-optimal pairs.** Pairs built from optimal rulers (ρ = 1 before trimming) needed heavy trimming before they became colorable, down to ρ ≈ 0.57–0.73. This agrees with the round-1 observations: near-maximal Bose and translate pairs had no TSD coloring, and gadget G1 obstructs translates. Near-maximality and TSD colorability seem to conflict strongly at these sizes.
3. **No instance reached the 0.954 danger threshold**, so the NTSD route is not closed by this pilot.

As the pre-registration requires, the search was not enlarged.

## Recommended next lane-B task

Attempt a proof, not a larger search. Use Theorem P and the type I/II conflicts (`../siege/proof.md` §4.10) to target an explicit statement: every TSD instance with |A|, |B| ≥ (1−β)Q(m) contains a C-collision, a type I conflict or a type II conflict.

The cheapest discriminating sub-step is the finite check that round 1 could not run. Do the two G1-free uncolorable instances (q = 17 and q = 19, t = 3) contain a type I or type II conflict? A "no" would mean the conflict catalogue is incomplete. That would be a reason to change the statement before attempting a proof.
