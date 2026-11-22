# Lane B round 2, pilot 1: falsification test of NTSD at small spans (pre-registered)

- **Date:** 2026-11-22.
- **Written:** before any search was run.
- **Owner instruction:** "move on to the next step" after reviewing the collaborators' contributions.
- **Budget:** one worker, under 1 GiB, at most 15 minutes elapsed.

## Statement under test

From `../siege/proof.md` §4.9:

- **TSD instance of span m.** Disjoint Sidon sets A and B inside one interval of m+1 integers, and a 2-coloring c of the pairs of U = A ∪ B with these properties:
  - c = 0 on every pair inside A;
  - c = 1 on every pair inside B;
  - c is proper on V(U): no directed L is monochromatic.
- **NTSD(β, m_0).** For m ≥ m_0, no TSD instance has |A|, |B| ≥ (1−β)Q(m).
- **Theorem R'.** NTSD with β > 0.046 at spans near 2.2·10^7 would be needed for any R4 use.

**Test.** For selected spans m ≤ 400, search for TSD instances that maximize ρ := min(|A|,|B|)/Q(m). The candidates are:
- (i) pairs of Bose translates A + j(q+1), trimmed by greedy point removal until colorable;
- (ii) translate pairs (G, G+t) of an optimal Golomb ruler G, trimmed the same way.

Colorability is decided by a complete backtracking search over the mixed pairs. Every reported coloring is re-checked against every L of V(U) by a separate routine.

**Q(m).** The values come from the optimal Golomb ruler lengths for up to 28 marks, cited from memory and labeled as such. ρ is also reported against the elementary upper bound on Q from `verify_four_rank.golomb_spans`. That bound is never smaller than the true Q, so the second ratio is a valid lower bound on the true ρ.

## Decision rules (fixed now)

- **Colorable instance with ρ ≥ 0.954 at some m ≥ 100.** This means β < 0.046 fails to be excluded there. The NTSD route is then in serious doubt as an R4 tool: record that the constant needed by Theorem R' is not supported at small spans, and recommend closing the route.
- **Best colorable ρ ≤ 0.90 at every tested m ≥ 100.** NTSD with β around 0.1 is consistent with the data. This is evidence only, and nothing about spans near 2.2·10^7. Recommend keeping NTSD as the lane-B target, with a proof attempt rather than a larger search.
- **Otherwise.** Inconclusive. Record it and do not enlarge the search automatically.

A finite search proves nothing about NTSD for large m. A found instance refutes only NTSD(β, m_0) for that β and every m_0 ≤ m.
