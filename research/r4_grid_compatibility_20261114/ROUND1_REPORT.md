# Lane B, round 1: interim report (R4-PAIR-20261114-v2)

**Status:** INTERIM. The proof attack in `siege/` has finished four of six rounds; round 5 was in progress at this checkpoint. Nothing here is a new bound on `R_4`.

- **Branch:** `claude/r4-grid-compatibility-20261114`
- **Base commit:** `726998b9` (PR #11 head as pinned in the agreement). Later PR #11 commits (for example `98af36bd`) touch only three-color files.
- **Owner:** Claude (lane B).

## B0: sensitivity (HYPOTHETICAL; computed exactly)

**Hypothesis H(delta).** `X_d <= (1-delta) U_d` holds for every shift `d` in the outer window.

**First pass: `b0/b0_sensitivity.py`.** Caps are held at their certified table values.
- The original verifiers are imported read-only. Both reproduce their stated margins (rerun 2026-11-14 with Python 3.13.5).
- **Elementary chain:** delta = 1/100 gives an excluded side of 21,748,312 (gain 239,097).
- **Window chain:** delta = 1/100 gives 21,708,379.
- These gains understate the effect, because the caps are not lowered at the smaller spans.

**Second pass: `b0/b0_recertified.py`.** Binary-source caps are re-proved at the spans each target side needs, using the same rank inequality.
- The reproduction check against the certified table is exact at three indices.
- A side reduction of about 3.9·delta needs delta:

| Target side | Required delta |
|---|---|
| 21.9M | 0.00101 |
| 21.5M | 0.00565 |
| 21.0M | 0.01154 |
| 20.0M | 0.02364 |

**Comparison with the existing correction.** The twenty-shift correction of the window chain is equivalent to delta ≈ 1.2·10^-7. An additive saving of about 63 starts at every shift moves the side by about 1,000.

**Results:** `b0/b0_results.json` and `b0/b0_recertified_results.json`.

## D1: pre-registered candidates (bounded search)

- **Pre-registration:** `D1_PREREGISTRATION.md`, committed before any search was run.
- **Search:** `d1/d1_search.py`, seed 20261114, 600 s, 1 worker, 8,425 proper colorings.
- **Witness check:** `d1/check_witness.py`, which shares no code with the search, re-checks every L of each witness.
- **Status:**
  - **U1, REFUTED.** Witness: `D = [0,14)`, `h = 5`, `sum m^2 = 16 > 26/3`.
  - **UW(1), REFUTED.** Witness: `D = [0,18)`, `h = 15`, `N_e = (5,5,5)`, `|F_h| = 3`.

## P1 and Part D: proof attack (`siege/`, 4 rounds so far)

The ledger is in `siege/ledger.md`, and the latest summary in `siege/summary.md` / `siege/round4_summary.md`. Answer files are `siege/roundK_qJ.answer.md`. None of the statements below has had an independent audit yet.

**P1 (i)–(v): proved by several independent workers (rounds 1 and 2).**
- (i) is an exact reformulation: every L in `V(D)` is `L(u,d,h)`, with corner `(u+h,u)` and arms `(u+d,u)` and `(u+h,u+h-d)`.
- (iii) is the double cover: each start is requested by at most two of the three colors, and a start requested twice is forced to the third color.
- (iv) is forced Golomb membership inside a class.
- (v): the PR #11 chain uses only the same-class, same-shift case.

**Refuted for arbitrary ternary sources.** Explicit digit and Sidon-lift families, proved proper by hand, refute:
- union growth;
- every energy bound `sum m^2 <= C(N + N^2/|F|)`;
- UW(lambda) for every lambda, on any number of shifts;
- the forced-color imbalance D-c+, by an explicit balanced family.

All of these families are sparse and cannot be diagonal classes of four-colored squares. See rounds 1–3: `round1_q2`, `round2_q1`, `round3_q2`, `round3_q3`.

**Reduction (round 4).** The consumer needs only a prefix-averaged joint fiber deficit, MS* (ledger entry 41 and later):

`sum_{l<=lambda} sum_e r_{S_e(d)}(l) <= (1-delta) sum_{l<=lambda} 3 v_l + E`, required only for `lambda` below a threshold set by the certificate rank. At this scale that is about `3*10^4`–`3.5*10^5`.

- MS* would give a proportional saving `delta' ≈ delta/2`, through the summed rank inequality: rounds 4 q1, q3, q6.
- Per-lag additive facts alone give no positive delta, because translates of a Bose set give six disjoint near-maximal Sidon pieces.
- Large density is excluded by the corners theorem, but only beyond a non-explicit scale.

**Open (main line).** MS* with an explicit delta for ternary sources at regime scale, or a counterexample. A proof would need an anti-correlation statement between the row and column words on the two non-corner colors.

## Exports to Codex (interface fields)

| ID | Domain | Statement | Evidence | Consumer and missing bridge | Near-extremality used |
|---|---|---|---|---|---|
| B-P1 | Ternary source `V(D)`, palette {0,1,2} | P1 (i)–(iv) as stated in `siege/problem.md` | PROVED by several worker answers; no separate audit yet | Structural only | None |
| B-MSstar | Ternary source, shift `d` | MS* implies `sum_e |S_e(d)| <= (1-delta') 3K`, with `delta' ≈ delta/2` | PROVED implication (round 4); the conversion constant is an estimate | U_d in the outer inequality; missing MS* itself | None in the implication |
| B-B0 | Outer inequality | Exact hypothetical response to `(1-delta) U_d` | Computed exactly; HYPOTHETICAL | — | — |

**Composition with lane A.** An improved `v_l` or `K` from lane A enters B's statements only as parameters. MS* is stated relative to `v_l`, so the two results compose and do not add.

## Next step (pending completion of the attack)

- Finish rounds 5–6 and the proof tail.
- Then audit P1 and the MS* implication independently.
- Recommendation so far: **continue on MS* only under a named near-extremality hypothesis.** The unconditional union and energy routes are closed by the counterexample families.
