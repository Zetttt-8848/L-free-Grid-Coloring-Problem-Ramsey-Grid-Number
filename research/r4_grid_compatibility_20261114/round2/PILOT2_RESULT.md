# Lane B round 2, pilot 2: result

**Outcome.**
- **q = 17 and q = 19:** the catalogued conflicts cover every uncolorable instance. This includes the parameters of the two round-1 G1-free cases (q = 17, t = 3, |A| = 12; q = 19, t = 3, |A| = 14): every uncolorable instance there has a type I or type II conflict.
- **q = 13:** 6 of 56 uncolorable instances have no C-collision and no type I or II conflict. Unit propagation alone does not refute them. A complete search refutes each with 2 to 4 branch decisions.

So pre-registered rule 3 fires, but only at the smallest tested size, and only with very shallow branching.

- **Run:** `conflict_check.py`, seed 20261122, 225 instances (25 for each q ∈ {13,17,19}, t ∈ {1,2,3}).
- **Results:** `conflict_check_results.json`. Every uncolorable instance's set A is stored.
- **Checks:**
  - Bose sets are built from a primitive element of GF(q^2), and every image u·Bose + s is verified Sidon in Z.
  - Colorings are re-checked against every L.
  - Soundness check: no conflict was reported on any of the 21 colorable instances, as must hold.
- **Caveat on the round-1 instances:** the two original sets were not stored. The statement above is about the regenerated family with the same parameters, not about those two exact sets.

## Data

| q | t | \|A\| | colorable | uncolorable | with type I/II | refuted by unit propagation |
|---|---|---|---:|---:|---:|---:|
| 13 | 1 | 11–12 | 0 | 25 | 23 | 23 |
| 13 | 2 | 9–11 | 6 | 19 | 17 | 17 |
| 13 | 3 | 8–10 | 13 | 12 | 10 | 10 |
| 17 | 1 | 15–16 | 0 | 25 | 25 | 25 |
| 17 | 2 | 13–15 | 0 | 25 | 25 | 25 |
| 17 | 3 | 12–14 | 2 | 23 | 23 | 23 |
| 19 | 1 | 17–18 | 0 | 25 | 25 | 25 |
| 19 | 2 | 15–17 | 0 | 25 | 25 | 25 |
| 19 | 3 | 14–16 | 0 | 25 | 25 | 25 |

- **No C-collisions anywhere,** as Proposition O predicts for this family.
- **Type I/II presence coincides exactly with refutation by unit propagation** in every instance tested.
- **Example of an uncovered instance:** q = 13, t = 1, A = {21,29,40,44,50,53,80,97,115,158,163}, B = A + 1.

## Reading

1. **The catalogue explains these cases.** Proposition 2G's two-generation conflicts explain every uncolorable instance here except a few small ones. The G1 gadget alone did not do that in round 1.
2. **The q = 13 exceptions are case splits, not forcing chains.** Fixing one or two mixed cells and propagating each branch refutes them. A conflict catalogue that includes "both values of one mixed cell propagate to contradictions" (a failed-literal step) would cover all 225 instances.
3. **Coverage grows with q in this sample.** Uncovered cases appear only at q = 13. This is evidence only; it says nothing about large q, and the instances are not near-maximal (|A|/Q(m) ≈ 0.55–0.85).

## Recommendation (lane B, next proof target)

Restate the NTSD proof target as a two-level forcing statement:

> **(NTSD-F).** For β small and m ≥ m_0, every collision-free pair of disjoint Sidon sets with |A|, |B| ≥ (1−β)Q(m) contains either a type I or type II conflict, or a mixed cell both of whose values lead to a type I or type II conflict after one further propagation step.

This is the smallest statement consistent with all data so far. A proof attempt should start from Proposition O's translate structure and Theorem P's threshold rule, as the round-1 commit query planned. It should not start by enlarging the search.
