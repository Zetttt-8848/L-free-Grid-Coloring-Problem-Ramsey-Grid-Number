# Notes (director; rewritten at finalize)

## Final status
- Goal (ledger entry 1) is OPEN. It was never proved and never raised, so there is no earlier PROVED [GOAL] to fall back on. The main claim of proof.md is the posed goal: P1 complete plus Part D settled. Verdict: NOT PROVED.
- P1 (i)-(v) is PROVED (entry 9). The verify report confirmed it step by step.
- Part D is open. Its per-shift core is FD. Sufficient conditions: SCD (Codex lane A) and NTSD (Claude lane; new at finalize).

## Commit wave outcome
- r3_q4 answered: Theorem R, NTSD(beta, m_0) => FD(beta/48, S_0) with S_0 = max((1471/beta)^{8/3}, (96/95)m_0). Theorem R' is the parametrised version. Checked by hand; constants checked by python. Integrated as proof.md Section 4.9, together with Lemma W, Corollary U, the TSD definition and Lemmas A, B, C', D, all written out.
  - Vacuous at the R4 scale: S_0 > 1.7e9.
  - Heuristic: Theorem R' at S = 2.2e7 needs beta > 0.046.
- r3_q1 answered: Theorem P (Sigma_1 is satisfiable iff there is no C-collision), Corollary P1, Proposition 2G (type I/II conflicts), Lemma M, and the split-graph lemma for the translate model. NTSD is not proved.
  - Theorem P was checked by python on 2990 random instances, with full agreement. Integrated in Section 4.10.
  - Lemma M and the split-graph lemma were recorded under "Other routes" only.
- r3_q2 and r3_q3 got no answer (API safeguards).
- r3_verify answered: no fatal errors.
  - One serious item, S1: the Status overclaimed embedding exclusion for small lifted members. Fixed.
  - Minor items m1-m9: m1, m2, m3, m7, m8 and m9 fixed in the text. m4 and m5 were fixed by rewording the Status. m6 was fixed by marking "earlier work, not proved here" in Other routes.
- The m = 23 TSD datum was rechecked by python: Sidon, Q(22) = Q(23) = 6, 76 L's, colorable. So NTSD needs m_0 > 23.

## proof.md structure (final)
- Answer in brief.
- Sections 0-4.8 from the draft, with repairs.
- 4.9 NTSD => FD.
- 4.10 known facts about NTSD.
- 5 consumer implication.
- Status.
- Other routes.
- The old Sections 6 and 7 were merged into Status and Other routes.

## If anything continues
- The best in-lane target is NTSD at large m, or NTSD* (only the instances that arise from saturated fibres).
- A proof must use L's with mixed spanning cells (Corollary P1).
- Open finite check: do the two non-colorable C9 instances without G1 (q=17, t=3, |A|=12; q=19, t=3, |A|=14) contain a type I or type II conflict?
- Any R4 use needs certified xi* and K_F/v_1 at spans of about 2.2e7, plus the comparison of 12c(n-1-d) against U_d.
- The ledger has not been updated with round-6 or commit-wave items. Candidate PROVED lines:
  - Theorem R;
  - Theorem P;
  - Proposition 2G.
- Honesty points to keep:
  - FD and NTSD are open;
  - no R_4 bound;
  - the B = 9 and small lifted embeddings are unsettled;
  - interval averaging is not refuted.
