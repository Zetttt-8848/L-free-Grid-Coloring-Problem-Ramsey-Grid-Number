# Notes (director, rewritten at the proof-draft step; rounds are over)

## Status
- Goal: entry 1 OPEN; never proved, never raised; there is no earlier proved goal. P1 PROVED (entry 9). Part D open; its core is FD (entry 66). SCF/SCD (entry 67) implies FD.
- Round 6: five queries answered (q1, q2, q3, q4, q6); q5 (SCF) not run because it is Codex's lane. No proof and no counterexample of FD.
- The round-6 results are NOT yet in the ledger (the ledger ends at entry 68). New proved items, all used in proof.md:
  - Lemma A / S0: K_F <= (1 + 3.83 S^{-3/8}) c(S);
  - Prop 1 (q2) and Prop S (q3): every class of an FD-violator is near the cap, with saturated fibres;
  - Prop 3 / 4 (q2) and R3 (q4): FD holds for translation-invariant colourings and for difference-coloured classes (factor 1/sqrt2);
  - band lemma (q1);
  - R1 (q4): BD => FD, and the doubling reduction of the converse;
  - q6 verification: the digit family needs hypothesis (H) (atoms below their copy's shift); explicit failure D = {-9900,0,100,10000} without it; side asides corrected (the B=9 aside is false; restrict "no member" to the families actually used).

## proof.md (written this step)
- Sections:
  - 1. P1 in full, plus the collision lemma, the inscribed-pair rule and the separation lemma.
  - 2. Energy reduction, forced energy; digit family with (H) (Lemma 2.3 L-list, Theorem 2.4, Lemma 2.5, Theorem 2.6 many-shift refutation); lifted family (Lemmas 2.7-2.8, Theorems 2.9-2.10, Corollary 2.11).
  - 3. (D-c): Prop 3.1, abstract obstruction, Theorem 3.2 (round3_q2 family), Prop 3.3 (under near-extremality, imbalance = fibre deficit).
  - 4. Q bounds, Lemma F, Fejer cap, Lemma 4.4, Theorem 4.5 (per-shift (D-a) vs Fejer caps <=> FD up to xi), Prop 4.6 (SCD => FD; violator structure), Prop 4.7 (saturation), Prop 4.8 (structured cases).
  - 5. Conditional R_4 implication.
  - 6. Other routes.
  - 7. Open core.
- Script checks this step (scratchpad, evidence only), all with 0 monochromatic L's:
  - digit family: cyclic k = 2, 3, 4; a two-shift Theorem-D instance (r=1, k'=2, s=1, role-1 padding under the general table) with counts as predicted;
  - (H)-violating example: monochromatic, as predicted;
  - lifted family: (p,r,k,m') = (5,1,2,2), (7,2,2,2), (5,1,3,1), with counts and fibre multiplicity as predicted;
  - (D-c+) family: k = 1, 2, 3, with A = G'' and B = G' confirmed;
  - TSD m = 23 datum: both sets Sidon; proper colouring exists (76 L's);
  - Lemma F identity on random sets; K_F/c - 1 ≈ 0.0021 at S = 2.2e7.
- First attempt at the Theorem-D check failed because atom exponents collided with shift exponents (my implementation error, not a flaw in the theorem). The distinct-exponent condition is essential.
- No extra_q files were written: nothing load-bearing is in doubt, and FD cannot be settled by a targeted query.

## If invoked again
- Possible polish: the ledger lacks the round-6 entries. proof.md is self-contained.
- Keep the honesty points:
  - FD open;
  - c(S) <= K(S) uncertified (margin about 0.7%, heuristic);
  - no R_4 bound;
  - B = 9 embedding open;
  - interval averaging not refuted.
