# Notes (director, rewritten at the round-6 plan step; round 6 is the final round)

## Status
- Goal: entry 1 (OPEN), never proved, never raised; no goal to come back to. P1 is PROVED (entry 9; round1_q1 Part A is the cleanest chain). Part D open.
- Ledger after the round-6 block: entries 1-68.
  - 55 Lemma F / Corollary F0 (Fejer cap K_F >= sqrt(v_1 S)); 56 Theorem B (Fejer route); 57 Prop C / C1 (MS' => SD => (D-a)).
  - 58 chain audit (step-6 direction flaw fixed); 59 Prop N; 60 Lemma K and Prop P; 61 RETRACT 53.
  - 62 inscribed-pair rule; 63 SL => MS', Theorem T, gadget G1; 64 single-quadruple W lemma.
  - 65 RETRACT 52 (MS' retired, not refuted); 66 OPEN FD (new missing statement); 67 OPEN SCF; 68 PROVED separation lemma (director, round6_plan).
- Round 5: all six answered after a resume (screen_r5 all OK). No proof, no counterexample.

## Key insights this step
- round5_q6 Prop C: MS' implies the plain size deficit, so all the local fibre statements (MS, MS', WE, TSD/SL) are at least as hard as (D-a). The missing statement is now FD: |F_d(D)| <= 3(1-eta) sqrt(v_1 S). The chain is three lines: entry 9, Corollary F0, FD.
- FD is essentially the (D-a) clause itself; the reductions did not make Part D easier.
- Counterexamples to FD need three binary sources of size about sqrt(2) S^{3/4} at one shift. None known; Sidon sets give about sqrt S.
- Separation lemma (mine): at each outer pair of a binary source, agreeing inscribed pairs have only one colour. Under Fejer saturation there are about 2L/sqrt(S) inscribed pairs per outer pair, so random-like colourings fail. Whether structured ones can survive is the core of SCF.
- The consumer caveat: K_F may exceed the consumer's rank cap K by about 1% (heuristic), so a deficit against K_F helps the consumer only beyond that gap.
- SCF touches the binary-source capacity lane (Codex's). Flag this to the orchestrator.

## Round 6 wave (6 queries; 5 "kind: attempt", 1 "kind: verify")
- q1 = q2 = q3: closing task on FD (byte-identical, about 41 KB).
  - Splices: P1 Part A (round1_q1 lines 3, 7-88), round5_q6 lines 10-56 and 187-249, round5_q2 lines 58-78, 102-152 and 156-183, round4_q2 lines 20-81, round5_q1 lines 121-190, the m = 23 datum, and the sketch.
- q4: refute FD (wording new), with round5_q4 Secs 0-6 and the Fejer material.
- q5: SCF cut out, with the separation lemma as first move.
- q6: verify the round2_q1 digit-family theorems (final-round standing-results allowance).

## For the proof-writing steps
- If FD is proved, the goal still needs its audit. No further round exists, so the proof-writing steps must handle it, marking it uncertified unless verified.
- If FD is not settled, the final document presents:
  - P1 (entry 9) in full;
  - the (D-b)-type standing results (digit families, entries 18-22; lifted family, entries 31-32; (D-c+) refutation, entries 34-35);
  - the conversion results (entries 27, 33, 42, 55-57);
  - the necessary conditions for counterexamples (entries 59, 60);
  - FD as the clearly marked open statement.
- Verify any construction by script: both middle orders, atoms below shifts, mirrored L's.
