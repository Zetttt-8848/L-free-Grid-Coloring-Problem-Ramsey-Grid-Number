# Notes (director, rewritten at the round-5 plan step)

## Status
- Goal: entry 1 (OPEN), never proved, never raised. P1 is PROVED (entry 9; round1_q1 Part A is the cleanest chain). Part D open.
- Ledger after the round-5 block: entries 1-54.
  - 42 Theorem A (conversion, round4_q6). I re-checked every step: the algebra H_tot - E_0 > 3 sqrt(alpha) H*, Lemma A1 (b),(c), and K <= K^Pi. Sound.
  - 43 Lemma W / Corollary U (round4_q2); 44 no single mixed pattern forbidden; 45 TSD => MS up to an O(m0) error; 46 OPEN TSD.
  - 47 near-extremality transfer, w_1 <= (8/9)|Y| (round4_q3); 48 Lemma E/C/Obstruction O (round4_q5); 49 Bose six translates (round4_q1); 50 SC => MS (round4_q6).
  - 51 RETRACT 41 (MS replaced, not refuted); 52 OPEN MS' (slack S/100, S >= S_0); 53 OPEN lead from round4_q4.partial (product ceiling 1/sqrt(M)); 54 the m = 23 TSD equality instance.
- round4_q4 was partial twice (only a 1 KB stub). The round4_q1/q6 partials are superseded by their re-runs.

## Checks done this step (scratchpad q5parts/, tsd.py, disj.py, verify23.py; evidence only)
- TSD exact maxima for m = 4..24, exhaustive over disjoint Sidon pairs with a backtracking 2-coloring:
  - deficit of 1-2 for 7 <= m <= 22;
  - EQUALITY (12 = Q+Q) at m = 23 and 24.
- The instance A = {0,1,4,13,15,21}, B = {2,5,7,16,22,23} was verified independently (76 L's, 0 monochromatic).
- Plain disjoint Sidon pairs reach the cap for every m in 5..24 except 7.

## Key insights this step
- Cross-lag collision counting is too weak at the lags Theorem A needs.
  - A cell z_{d+m}(p) lies in about 36 lambda/S lag-structures. Collisions number about lambda^3/S, against C_w of about 6 sqrt(S) lambda.
  - The two are comparable only at lambda ~ S^{3/4}, but at the optimal rank the chain needs lambda up to about S^{5/8}.
  - Raising the rank to reach lambda ~ S makes the needed statement equivalent to the conclusion itself (circular).
- So any deficit must be single-lag and asymptotic, in the coupled structure (W, kappa) of three binary sources.
  - First-moment heuristic for one U_f: about (2·(3/4)^2)^m ≈ 1.1^m colorings, which is borderline.
  - The cross-f couplings W(a), W(b) might push it below 1. MS' may well be false.
- The per-shift (D-a) inequality from MS' needs the named span hypothesis S >= S_1, and it compares to 3K^Pi (the Pi-form certified cap).
  - The only remaining elementary step of the chain is an explicit lower bound K^Pi >= c S^{3/4} (Bose + Bertrand for Q).

## Round 5 wave (6 queries, all "kind: attempt", all on MS')
- q1 = q2 = q3: closing task on MS' (byte-identical, about 54 KB with splices).
  - Splices: round4_q1.md lines 29-194, round4_q6 Part A + Lemma B1, round4_q2 Secs 1-3, round4_q3 Sec 3, round4_q5 Secs 0-5, the Bose statement, the m = 23 data.
- q4: refute MS' exactly as stated (its wording is new this round).
- q5: the single-lag core SL (=> MS'), via TSD or a finite unsatisfiable gadget plus counting; or refute SL/TSD.
- q6: bare query (MS' + the cited statements 9/27/33/42 only; derive the chain; new first move).

## Next round (round 6, the final round)
- If any answer proves MS' (or SL/TSD with the derivation):
  - record PROVED [GOAL] citing entries 9, 27, 33, 42 and the new proof;
  - send two verify queries carrying the whole chain verbatim (P1 Part A, rank inequalities, prefix lemma, Theorem A, the new proof, plus the elementary K^Pi lower-bound step);
  - round 6 is final, so follow the brief's wording on concluding.
- If MS' is refuted by an explicit family:
  - that does not refute (D-a) in general, but it is a strong (D-b)-type result;
  - check whether it meets the goal's (D-b) clause (classes as large as the regime requires); probably record it as a major standing result;
  - verify it with a script (all L's).
- If nothing: the goal was never proved, so there is no goal to come back to.
  - The final document presents the standing results (summary section), with MS' marked open.
  - Up to two queries in the final round may write up standing results.
- Verify any construction by script (both middle orders; atoms below shifts; mirrored L's).
