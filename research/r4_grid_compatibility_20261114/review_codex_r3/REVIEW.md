# Independent review: Codex round 3, `R_4 <= 21,947,865`

- **Reviewer:** Claude (lane B), under R4-PAIR-20261114-v2 ("you will review Codex's new mathematical contribution").
- **Date:** 2026-11-22.
- **Reviewed revision:** `codex/r4-local-capacity-round3-20261114` at `14647e607c2525b0cd12081b03899827d306a030`, in a detached review worktree.
- **Files read in full:** `research/r4_local_capacity_round3_20261114/THEOREM.md`, `ROUND3_REPORT.md` and `TOOLS.md`.
- **Files read in part:** `verify_numeric.py`, its span audit and discrepancy routine.
- **Not read:** `ENCODING_REVIEW.md` and `NUMERIC_REVIEW.md`.

## Verdict

**The claimed chain reproduces exactly.** Every quantitative input was recomputed by code written for this review. The only shared components are the inherited, previously reviewed verifiers of `research/boundary_certificates_20261115`, and they are unmodified on the reviewed branch (`git diff 726998b9..14647e6` is empty there).

I confirm the status **PROVED, computer-assisted**. The external inputs are:
- the Carter–O'Bryant–Tao rational window data inherited from the window chain. This data was not audited in this review; its audit is Codex's baseline task.
- the inherited window and twenty-shift lemmas.

The finite caps are confirmed by complete enumeration instead of the DRAT traces. That is a second, independent evidence path for them.

## What was checked

| Step (THEOREM.md section) | Independent check | Result |
|---|---|---|
| §1: C(4)=4, C(8)=7, C(12)=9, C(16)=11, C(20) ≤ 14 | `check_finite_caps.py`: every k-subset containing 0 is decided by a complete backtracking search on the NAE-L constraints of V(A). Lower bounds have explicit colorings, re-checked against every L. The solver agrees with brute force on 400 random small sets. | All confirmed (`finite_caps_check.json`). The 11,628 subsets of size 15 in 20 positions take 38 s. |
| §2: hereditary spans e_s, s ≤ 600, with the seeds e_8 ≥ 8, e_10 ≥ 12, e_12 ≥ 16, e_15 ≥ 20 | `check_transfer_and_consumer.py` recomputes the nonuniform rank recursion from scratch. It does not audit a stored list. | Identical to Codex's stored spans at every s. |
| §3: endpoint discrepancy D | Exact rational recomputation with the improved local cap | D = 219.441282528684… ≥ 1097/5 |
| §3: 566 binary interval rows at saving 1097/5 | Inherited `verify_profile`, plus a domain check on every row | All pass |
| §4: full-square contradiction at n = 21,947,865 | Inherited `outer_twenty` with the quartic window | 561 blocks, loss 41. Margin = 667767862929561436134957406955093129954012400, positive, equal to Codex's value |

Codex's own `verify_numeric.py` was also rerun and passes all six variants.

**What this review did not do:**
- It did not replay the DRAT traces. I did not download or build DRAT-trim; the exhaustive enumeration replaces that evidence path for the same finite statements.
- It did not audit the external window data.
- It did not check the 15 complete source witnesses separately. My own witnesses cover the lower bounds.

## New finding for lane A (hand-off, not adopted into any bound)

**C(20) = 13 exactly**, by the same exhaustive method:
- every one of the 27,132 subsets of size 14 containing 0 in 20 positions is uncolorable;
- a 13-subset is colorable: A = {0,1,2,3,5,6,8,9,11,15,17,18,19}, with its coloring stored and re-checked against every L in `c20_exact_check.json`.

So the seed **e_14 ≥ 20** holds, which is stronger than e_15 ≥ 20. Effect on the discrepancy: D rises from 219.4413 to **219.4961**. The spans change at 117 sizes.

Codex measured about one position for the jump from D ≈ 219.00 to D ≈ 219.44. An extra +0.055 is therefore unlikely to move the side by more than one position. Turning it into a certificate requires rerunning Codex's consumer, which is lane A. The exhaustive search, rather than DRAT, is the evidence for C(20) = 13.

The finite caps C(24) and C(32), undecided in Codex's run, look within reach of the same exhaustive method if lane A wants them. Their consumer value should be priced first, as Codex's report recommends.

## Integration note

The round-1 results of lane B (`../ROUND1_REPORT.md`) do not touch this chain. Lane B's open statements (FD, NTSD) bound the joint size of the three classes at one shift. If proved, they would compose with the improved binary caps as a separate factor on U_d. They must not be added to the 41-match twenty-shift saving or to the endpoint discrepancy, which charge the same cells.
