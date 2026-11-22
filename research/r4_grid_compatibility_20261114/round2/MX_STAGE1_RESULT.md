# MX stage 1: result

The pre-registration is in `NEXT_TARGETS.md` §2, committed at ddefa7a before this run.

**Outcome.**
- **n_rel(3) ≥ 61.** [0, n) splits into three binary sources for every n ≤ 61.
- **The exact value is not reached:** n = 62 was not decided within the budget.
- **Pre-registered rule (b) fires** (n_rel(3) ≥ 28), so MX proceeds to stage 2, subject to the caveat below.
- **No claim about R_3 or R_4.**

## Run

- **Script:** `mx_stage1.py`, with CaDiCaL 1.5.3.
- **Scan:** every n from 5 to 61 is SAT.
- **Interruption:** the first run was stopped by the outer time limit while solving n = 62, before its results file was written. The script now writes after every row. The n = 61 row was then recomputed (40 s) and stored in `mx_stage1_results.json`.
- **Witness checks:** every witness was re-checked against every L, and each class was re-decided colorable by the independent backtracking solver of `../review_codex_r3/check_finite_caps.py`.
- **The n = 61 witness:** class sizes 20, 20, 21:
  - D_1 = {0,2,12,15,16,21,22,25,26,28,29,30,36,41,47,48,50,51,56,59}
  - D_2 = {1,4,6,10,11,14,18,20,31,32,33,34,35,40,42,44,49,52,53,58}
  - D_3 = {3,5,7,8,9,13,17,19,23,24,27,37,38,39,43,45,46,54,55,57,60}
- **Upper bound for context:** n_rel(3) is at most the 3-color chain bound minus 1. The chain bounds exactly this relaxation, since every L it uses lies inside one diagonal class.

## Caveat (the rule's comparison is with a lower bound)

Rule (b) compares n_rel(3) with 21. That number comes from the known proper 20 × 20 three-colored square, so R_3 ≥ 21.
- The true full maximum, R_3 − 1, is unknown. The repo's searches at n = 21–23 are UNDECIDED.
- So "the outside cells carry information at k = 3" follows only if R_3 ≤ 61, and that is not known.
- At k = 2 the comparison is exact (`relaxation_k2.py`): n_rel(2) = 7 against a full value of 4.

## Follow-up probe (not pre-registered)

`mx_extension_probe.py` takes relaxed-feasible diagonals at n = 21 and asks whether each extends to a proper 3-coloring of the full 21 × 21 square, with only the diagonal fixed (`mx_extension_probe.json`).

| Diagonal | Full extension |
|---|---|
| trial 0 | UNKNOWN (200k conflicts) |
| trial 1 | UNKNOWN (200k conflicts) |
| trial 2 | **none**: UNSAT by CaDiCaL, and UNSAT by Glucose 4 |

- So same-class feasibility does not imply full feasibility, even at n = 21.
- Even fixed-diagonal extension is hard at this size. That is consistent with n = 21–23 being the frontier of full 3-color searches.
- The probe was not enlarged. It is undecided for the other diagonals.
- The UNSAT answers are confirmed by two solvers. No DRAT check was done.

## Reading

1. **There is a measurable gap at k = 2.** The relaxation that the whole chain bounds admits n = 7, while the full square fails at 5.
2. **The relaxation is weak at k = 3.** It admits n ≥ 61, while every known full construction stops at 20. Whether the true full maximum is far below 61 is open.
3. **What the chain loses.** Since the chain bounds only the relaxation, its 3-color bound can never fall below n_rel(3) + 1 ≥ 62. The same holds at k = 4 with n_rel(4) + 1. Any method that stays inside same-class information has this floor; outside-cell information is the only way below it.

## Stage 2 entry point (proposed)

Start where everything is exact, at k = 2.
- For each relaxed-feasible diagonal with n = 5, 6, 7, extract a minimal set of outside-cell L's that refutes its full extension (an UNSAT core).
- Classify the gadgets in the language of Lemma C1 and the type I/II conflicts.
- Then look for the same gadgets on k = 3 relaxed witnesses, starting with the UNSAT diagonal above.

These are small exact computations. They aim at a forcing lemma, not a bound. Any R_4 consumer still needs the bridge named in `NEXT_TARGETS.md` §2.
