# Notes (director, rewritten at refine_2; rounds are over)

## Status
- Goal: entry 1 OPEN; never proved, never raised. P1 PROVED (entry 9). Part D open; its core is FD (entry 66). SCF/SCD (entry 67) implies FD.
- Round 6: q1, q2, q3, q4, q6 answered; q5 (SCF) not run (Codex lane). No proof and no counterexample of FD.
- The ledger still lacks the round-6 entries (it ends at entry 68). proof.md is self-contained.

## refine_2 (this step)
- Saved the incoming draft as judge/refine_2_previous_proof.md, then edited proof.md in place (structure unchanged).
- Re-audited by hand:
  - P1 incl. the four-L Golomb split and the per-fibre cap;
  - Lemma 2.3 cases; Lemma 2.5; Lemma 2.7; Lemma 2.8 / Theorem 2.9 table;
  - Lemmas 4.1-4.4, Theorem 4.5, Props 4.6-4.8, the difference-colored remark.
  - No mathematical error found.
- Fixes made:
  - Q-low: Bertrand is now applied to the integer n = floor(x), so a prime lies in (x, 2x]; the bound max G_0 < 2p^2 <= m is made explicit.
  - Prop 4.7(a): the case theta >= 1/2 is trivial; the step s^2 >= (1-2theta) v_1 S is justified for theta < 1/2.
  - Heuristic reading after Prop 4.7 was numerically wrong: it said 3.7% / 8%; correct is theta ≈ 3.4% and Dbar ≤ 8.9% (with numerical K_F), or 4.4% / 10.7% with the proved xi.
  - Prop 4.6(c): sqrt2·S^{3/4} is now marked as asymptotic (CITED Q ~ sqrt m); the proved bound is c >= S^{3/4}/sqrt2.
  - Bose six-translates: a one-line proof was added.
  - TSD m=23 datum: now marked as a computer-checked finite fact.
  - Labels paragraph: lists exactly which instances were checked.
- New HEURISTIC remark (Section 5, plus a Section 7 bullet): with the problem's rounded figures, K_F ≈ 4.557e5 < K ≈ 4.58e5, about 0.5% lower. If that survives recertification with the same Q-bound, min(K, K_F) would already be a proportional single-class saving. This is in Codex's lane A; hand it off, do not claim it. The rounding is about ±0.3%.
- Script checks (scratchpad common.py, digit.py, lifted.py, dc.py, misc.py; evidence only), all passed:
  - Theorem 2.6 two-shift instance: 40 points, 60 L's, 0 mono; F=4, N=4, R=1, E=16.
  - Cyclic family with random f, k = 2, 3, 4: 0 mono.
  - (H)-failure example: mono, as stated.
  - Lifted family (5,1,1,2), (5,1,2,2), (7,2,1,2): 0 mono; counts as in Theorem 2.10.
  - Theorem 3.2 family, k = 1, 2, 3: 0 mono; A = G2, B = G1, X = F_d.
  - TSD datum: 76 L's; proper coloring found; Q(23) = 6.
  - Bose q = 7: six disjoint translates.
  - K_F/c - 1 = 0.0021; xi(2.2e7) = 0.0068; xi(2700) = 0.198, so eta = 0.6 is OK.
- Implementation slip of mine (not a math issue): a dead loop over range(h) with h = 100^13 hung the first run; removed.
- No extra_q files written: FD is the only load-bearing gap, and no single query settles it. Earlier rounds tried MS, MS', TSD, SL and FD directly, all without result.

## If invoked again
- Keep the honesty points:
  - FD open;
  - c(S) <= K(S) uncertified;
  - the K_F-vs-K remark is heuristic only;
  - no R_4 bound;
  - B = 9 embedding open;
  - interval averaging not refuted.
- Possible polish: add the round-6 items to the ledger.
