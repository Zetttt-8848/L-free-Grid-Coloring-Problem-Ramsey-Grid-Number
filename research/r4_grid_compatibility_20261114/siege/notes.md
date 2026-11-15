# Notes (director, rewritten at the round-4 plan step)

## Status
- Goal: entry 1 (OPEN), unchanged. It asks for P1 plus Part D at (D-a) or (D-b).
  - P1 is PROVED (entry 9; round1_q1 Part A, lines 7-90 of the answer file, is the cleanest chain).
  - No complete proof of the goal exists. Audit not triggered. Escalation is active from round 4.
- The ledger after the round-4 block has entries 1-41:
  - 30 ABAA forcing (round3_q1)
  - 31/32 the lifted family, proper; it kills D-b variants (b) and (a, alpha<1/2) (round3_q3)
  - 33 the prefix lemma (round3_q4)
  - 34/35 the round3_q2 family; D-c+ refuted without hypotheses
  - 36 density obstruction, modulo the corners theorem
  - 37 color Cauchy-Schwarz (mine, round4_plan)
  - 38 OPEN D-b survivors
  - 39 OPEN D-c under H1-H3
  - 40 RETRACT 23
  - 41 OPEN MS
- MISSING STATEMENT (entry 41): a joint prefix deficit with explicit delta, unconditional, for every proper ternary source, every d and every lambda:
  sum_{l<=lambda} sum_e r_{S_e(d)}(l) <= (1-delta) sum_{l<=lambda} 3(Q(S-l)+Q(S-l-1)), with S = span F_d(D).
  - Chain: entry 9, then entry 27 (summed rank inequality), then entry 33 (prefix), then MS, then the conversion delta -> delta'.
  - The conversion is still uncomputed (elementary). No rounding issue arises: use the real-valued P*(H) = sum_lambda max(0, H - (1-delta)C_{3v}(lambda)), which scales exactly.

## Checks done this step (scratchpad, evidence only)
- r3q2.py: the round3_q2 family at k = 1, 2, 3 has 0 monochromatic L's (32/144/336 L's). Golomb colors are (2..2,1..1); request colors are {0,1} for U'' and {0,2} for U', as claimed.
- r3q3.py: the lifted family, p in {5,7}, 1-2 copies, k = 2-3, 3 seeds each: 0 monochromatic L's (up to 2772 L's); N_e = 2kr exactly.
- pos.py: the color Cauchy-Schwarz identity and inequality hold on 200 random sets and partitions.

## Key insights
- Entry 37: in the regime, both sides of sum a_l r_{F_d(D)}(l) <= a_0|F_d| + 9 sum a_l v_l are about 8.5e4. The regime is at near-equality, i.e. local equidistribution of the classes plus saturated caps.
- This "second-order outer inequality" (rectangle counts u, u+d, u+l, u+l+d of D_c) gives, to leading order, the same exclusion n ~ 2.1e7 as the first-order one (both give n^{1/4} ~ 48 sqrt2). So it is not a saving by itself. It could become a second consumer if it is combined with a 2D positivity lower bound on the monochromatic rectangle counts of the diagonal word. Not pursued.
- On intervals, the caps force agreement rates below 1/3 once S-l > ~324. Proper ternary sources on long intervals are bounded anyway (three-color triangle).
- Two disjoint near-max Sidon sets exist (Singer set plus a translate minus one point). So no saving comes from additive combinatorics alone; the L's must be used.

## Route impressions
- MS is research-hard; I expect partial output. A refutation needs saturated constructions (near-max Sidon pieces), probably out of reach. Watch for q4 producing a constant-ratio family (useful).
- If MS is proved, the [GOAL] becomes provable only after delta' is computed. Check whether the q1-q3 answers do it; otherwise the next missing statement is the delta' computation, a finite optimization.
- D-b at regime size: explicit constructions look hopeless. Do not weaken the goal.

## Round 4 wave (6 queries, all "kind: attempt", all on MS)
- q1 = q2 = q3: closing task (byte-identical).
- q4: refute MS.
- q5: named Fourier-uniformity approach.
- q6: bare (statements only; derive the chain; new first move).

## Next round
- Round 5 of 6 counts as "one further round"? Check the brief wording.
- Verify any construction with a script (both middle orders; atoms below shifts).
- If a full MS proof plus the conversion appears, record PROVED [GOAL] and send 2 verify queries carrying P1 Part A, entries 27/33, the MS proof and the conversion, verbatim.
- If MS is refuted: record it under dead ends and build the next line. Candidates are D-c under H1-H3 (entry 39), or a second-order consumer through entry 37.
