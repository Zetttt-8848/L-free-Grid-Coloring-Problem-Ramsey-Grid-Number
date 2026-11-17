# Notes (director, rewritten at refine_3; rounds are over)

## Status
- Goal: entry 1 OPEN; never proved, never raised. P1 PROVED (entry 9). Part D open; its core is FD (entry 66). SCF/SCD (entry 67) implies FD; SCD is Codex lane A.
- Round 6: q1-q4 and q6 answered; q5 (SCF) not run (Codex lane). No proof and no counterexample of FD.
- Ledger still ends at entry 68 (round-6 items not added). proof.md is self-contained.
- No extra_q files exist (none written at refine_2 or refine_3).

## refine_3 (this step)
- Saved the incoming draft as judge/refine_3_previous_proof.md; edited proof.md in place (structure unchanged).
- Re-audited by hand: Lemma 0, (i)-(iv) including the four-L Golomb split, per-fibre cap, Lemma 1.1, Props 2.1/2.2, Thm 2.6 counts, Lemma 2.5, Q-bounds, Lemmas 4.2/4.4, Cor 4.3, Thm 4.5, Props 4.6-4.8, the difference-colored remark, and Bose. No error in these.
- REAL OVERCLAIM FIXED: the lifted family (Thm 2.10) has |R_e| = |F_H|/3 and energy ratio 6k/(3+2k) < 3. So it refutes UW(λ) for all λ, but the energy bound only for C < 3 and union growth only for liminf f > 1/3. The earlier status line and Cor 2.11 said "every constant". Fixed in the status, Cor 2.11 (with proof and a limitation paragraph) and Section 7. Padding cannot be added naively: equal base shifts give an (X2) base L with all three cells cross cells, monochromatic color 1 under χ_B.
- Section 5: added the additive term 4S_0 for colors whose F_d(D_c) has span < S_0. FD helps the consumer only with S_0 ≤ about 6e5·η, giving δ ≥ η/2.
- Added K_F^♯ (exact quadratic root keeping λ/Λ), PROVED; numerically 0.15% above c vs 0.21% for K_F.
- Corrected the K_F-vs-K remark (fragile sign). At S = 2.1987e7, with v_1 = 9350/9400/9450 K_F is −0.8/−0.5/−0.3% vs 4.58e5. With the Lindström-type Q ≤ sqrt m + m^{1/4} + 1 (v_1 ≈ 9517), K_F is +0.1% and K_F^♯ +0.03%. The earlier "±0.3% rounding" understated this. The c-vs-K margin goes 0.7% → 0.1% under the same change.
- Script rechecks (scratchpad t32.py, kf.py; evidence only):
  - Thm 3.2, k = 1, 2, 3: 32/144/336 L's, 0 mono, X = F_d, A = G2, B = G1. Passed.
  - Fejér numerics as above; ξ(2700) = 0.198; ξ(2.2e7) = 0.0068.

## If invoked again
- Keep the honesty points:
  - FD open;
  - c(S) ≤ K(S) uncertified and fragile;
  - the K_F-vs-K remark is heuristic, and its sign depends on the Q-bound;
  - no R_4 bound;
  - B = 9 embedding open;
  - interval averaging not refuted;
  - the lifted family is limited to C < 3 and f > 1/3.
- An extra query is possible only on in-lane questions, e.g. a padded lifted family, or FD ⇒ SCD via a sparse-square 3-coloring. Neither is load-bearing for a bound.
- Possible polish: add the round-6 items to the ledger.
