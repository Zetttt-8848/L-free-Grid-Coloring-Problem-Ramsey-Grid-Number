# Notes (director, rewritten at round 3 plan)

## Status
- Goal = entry 1 (OPEN): P1 plus Part D at (D-a) or (D-b). P1 is PROVED (entry 9; round1_q1 Part A is the cleanest chain). Part D is unsettled. Audit is not triggered.
- The ledger after the round-3 block holds entries 1-29:
  - 18-22: the digit families (round2_q1): proper; UW(lambda) and the energy/union-growth refutations, also on finite shift sets; non-embeddable.
  - 23: OPEN, the surviving D-b variants.
  - 24: single-L coupling (q2).
  - 25: forced energy (q3).
  - 26: Lemma F / AABA forcing (q4).
  - 27: summed rank inequality (q4).
  - 28: OPEN, AABA/ABAA.
  - 29: OPEN, the arm-agreement deficit (AD), mine.
- Rank-neighbor inequality quote: round2_q4.md lines 57-61. Single-class Golomb quote: round2_q4.md lines 13-39. Digit family: round2_q1.answer.md lines 3-186. Shared facts preamble: scratchpad facts.md.

## Checks done this step
- Digit family (round2_q1): random instances, scratchpad digit3.py: 150 instances, 0 monochromatic L. Counts checked with digit4.py.
  - CAVEAT: atoms must be below their copy's shift. With atoms above the shift there are monochromatic L's. This was my test bug, not the construction's; I flagged it in the queries.
- Lemma F and the AABA forcing were rechecked by hand: they are fine.
- Summed rank inequality: fine.
- A background python job (task bm748ey2m, digit4.py, first version) has an infinite loop. I could not kill it (taskkill was denied). I told the orchestrator.

## Key insight (round 3 plan)
- The digit families have min_e N_e(h)/(h|F_h|) -> 0. The consumer needs exactly c < v/(3K) ≈ 1/146 in "min_e N_e <= c h |F_h|".
- Regime = agreement rate 1/3 of the words z_d(u) = chi(u+d,u), i.e. random-like. Properness excludes the corner color from the agreements at every pair (u,v), so independent row and column words would agree at rate 2/9 only.
- The D-a target is therefore an agreement deficit (AD) under a density/near-cap hypothesis. Sparse designs have rate 1, so a hypothesis is needed.
- A ternary-cap bound on Lambda(h) misses by a factor of 3.
- An attempted "K3 < 3K" shortcut is WRONG: ternary-source fibers have no Golomb split, and D_c has density 1/4.

## Route impressions
- D-a: research-hard; (AD) is the cleanest formulation. Expect partial or conditional output.
- D-b as posed (regime-size classes): out of reach of explicit construction. The sparse variants are done.
  - q3 tries fibers >= 2 and polynomial classes.
- D-c: q2 tries an explicit balanced digit realization. If it succeeds, D-c+ is refuted for arbitrary sources. That is not the goal, but it is good material for "Other routes".
- AABA (q1): a local, settleable question. Value toward a joint bound is uncertain.
- Do not weaken the goal. The final document presents P1 plus the D-b sparse refutations plus the conditionals.

## Round 3 wave (all four "kind: attempt")
- q1: AABA/ABAA.
- q2: D-c balanced realization.
- q3: D-b with fibers >= m.
- q4: D-a agreement deficit (AD).

## Next round checks
- Verify every returned construction by enumerating all L's, both middle orders, with a script on small parameters. Keep atoms below their shift.
- If a witness for AABA is given as rows, check its properness with a script.
- Escalation from round 4 (ESC_ROUND=4): name a single missing statement. The best candidate is (AD) or the joint fiber bound (entries 29, 17).
- If any complete D-a chain appears, it needs 2 verify queries carrying P1 (round1_q1 Part A) plus the chain verbatim.
