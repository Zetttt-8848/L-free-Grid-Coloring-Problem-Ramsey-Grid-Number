# Notes (director, rewritten at select / commit wave)

## Status
- Goal: entry 1 OPEN; never proved, never raised. P1 PROVED (entry 9). Part D open; its core is FD (entry 66). SCF/SCD (entry 67) implies FD; SCD is Codex lane A.
- Round 6: q1-q4 and q6 answered; q5 (SCF) not run (Codex lane). No proof and no counterexample of FD.
- Ledger still ends at entry 68 (round-6 items not added). proof.md is self-contained. It was not changed at this step.
- No extra_q files exist.

## select step (this step): commit wave written
- Route chosen: NTSD (near-maximal two-layer unsatisfiability). This is in Claude's lane: it couples two different completion classes at one shift, not single-class capacity.
  - NTSD(β, m_0): no TSD instance of span m ≥ m_0 with |A|, |B| ≥ (1−β)Q(m).
  - A TSD instance: disjoint Sidon A, B; pairs coloured 0 on A-pairs, 1 on B-pairs, proper on V(A∪B).
  - Key observation: NTSD ⇒ FD needs only ONE contradiction in ONE near-maximal pair. Earlier rounds wanted a density of gadgets. The chain:
    1. Prop 4.6(b): an FD-violator has three near-cap classes.
    2. Prop 4.7(b), union bound over classes: one lag l ≤ εS is good for all classes.
    3. Prop 4.7(c): all Golomb pieces at that lag are near-maximal.
    4. Corollary U: U_f(l) is a TSD instance, which NTSD forbids.
  - Expected η ≈ β/200.
- Director computations (scratchpad tsd*.py; evidence only):
  - DPLL TSD solver, validated on the m = 23 datum (SAT).
  - Bose-type near-maximal pairs: q = 7, 11, 13, 17, with B = uA + s; 240 pairs, all UNSAT.
  - Bose translates by j(q+1): all UNSAT.
  - C-collisions (first-generation clash at one mixed cell) in random Bose pairs: minimum counts 1, 2, 4, 8, 10 for q = 7..19.
  - Trimmed small translates (B = A+t, no differences ≤ 2t):
    - 0 C-collisions, as Prop O predicts;
    - UNSAT for q ≥ 13 except one case;
    - G1 gadgets present except in two UNSAT cases with t = 3 and |A|/q ≈ 0.7.
  - Below near-max, SAT is easy: a SAT-preserving greedy matches unconstrained greedy at about 0.77-0.87 of v. So β < about 0.2.
  - First-generation forcing for a mixed cell (a, a+g), derived and checked:
    - AB cell: forced 1 if α_A(g) > a; forced 0 if α_B(g) < a.
    - BA cell: forced 0 if α_B(g) > b; forced 1 if α_A(g) < b.
    - Collision iff the left end lies strictly between the starts on the forbidden side.
    - A spanning-position mixed cell is never first-generation forced.
- Files written:
  - r3_q1: full NTSD via the collision/gadget dichotomy.
  - r3_q2: non-aligned half; C-collision under an explicit alignment parameter τ.
  - r3_q3: aligned half; translates via Theorem T/G1, then partial translates.
  - r3_q4: rigorous reduction NTSD ⇒ FD ⇒ per-shift (D-a), explicit η(β), S_0. This one is the most likely to succeed. If proved, add it to proof.md as a conditional theorem, an implication only.
  - r3_verify: full proof.md, cat-spliced, with a step-by-step check request.
- Context blocks: C1-C3 = Lemma 0, (iv), Lemma W/Cor U, spliced. C5 = proof.md §4 lines 475-549, spliced. C6 = Lemma S, C7 = Theorem T + G1 (round5_q5.answer), spliced. C4/C8/C9 were written by hand (Lemma C1 with proofs, Prop O, NTSD, evidence).

## If invoked again (integration)
- If r3_q4 proves Theorem R: add it to proof.md §4 or §7 as PROVED (conditional on NTSD). Then the open core can be restated as NTSD, which is a sharper and in-lane statement than FD. Keep FD as the equivalent per-shift form.
- If r3_q1/q2/q3 claim NTSD or one half: check hard. Points to check:
  - the order arguments;
  - that the statement covers ALL near-max Sidon pairs, Bose/Singer included;
  - that the alignment parameter in q2 really complements q3.
  - Re-test any claimed gadget on the solver instances (scratchpad tsd.py has solve, clashes, g1).
- Even full NTSD gives an R_4 consequence only after the consumer certification: c(S) ≤ K(S) is uncertified and fragile, and S_0 must be ≤ about 6e5·η.
- Keep the honesty points:
  - FD open;
  - c(S) ≤ K(S) uncertified;
  - the K_F-vs-K remark is heuristic;
  - no R_4 bound;
  - B = 9 embedding open;
  - interval averaging not refuted;
  - the lifted family is limited to C < 3 and f > 1/3.
- Possible polish: add the round-6 items and the commit-wave outcome to the ledger.
