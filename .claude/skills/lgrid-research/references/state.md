# Research state snapshot

Snapshot date: 2026-11-13; PR 11 rows added 2026-11-14. Pins: `pins.json`. This file is a dated summary
with pointers; the cited project records are the authority. If
`scripts/refresh_state.py` reports a moved pin, the affected lines below are
unverified until re-derived. Evidence labels follow `lgrid-verify`.

"Reviewed in repository" means an in-repository review by a separate agent
exists. It is not an external referee report and not a formal proof.
"Rerun 2026-11-13" means the named checker was executed in the session that
wrote this snapshot.

## Where the work lives

| Ref | Commit | Content |
|---|---|---|
| `origin/main` | `1231d436d199` | English conversion of the imported manuscript and records. Literature baseline only; none of the research checkpoints below are merged. |
| `origin/codex/global-counting-research-20261108` | `dc1cbe6daf7d` | **Latest research checkpoint.** Contains every `research/` package below. PR 7 (open, stacked on PR 6). |
| `origin/codex/kernel-compatibility-research-20261108` | `5b5db22c3c65` | `R_3 <= 464`. PR 6 (open). |
| `origin/codex/coupled-budget-research-20261108` | `654cc044cad3` | `R_3 <= 465` restored, `466` by endpoint rearrangement. PR 5 (open). |
| `origin/codex/boundary-extension-research-20261108` | `df6e35cfff68` | Boundary obstructions, literature audit. PR 4 (open, base `main`). |
| `origin/codex/three-cube-*` | `d6755b4`, `7f8e8bf`, `a53970c` | Three-cube forcing, boundary budgets, pair-repair refutation. PRs 1-3 (open, stacked on `main`, **not** contained in the checkpoint line). |
| `refs/pull/11/head` (fork `TommyMaHaoKun:research/directed-l-boundary-20261115`) | `b3941b3ad1d6` | `R_3 <= 462`, `R_4 <= 21,987,409`. PR 11 (open, stacked on PR 10). Reviewed in `research/upper_bounds_20261114/pr11_review/` (branch `claude/upper-bounds-20261114`). |
| `origin/codex/recover-claude-calibration-20261113` | `0910ed1f08e3` | Recovered exploratory calibration scripts; based on old `main`. No proof content. |

Pull requests 8 and 9 (merged) are language conversions, not mathematics.
The primary working directory may sit at `080822b` with uncommitted work from
an earlier session; the refresh script reports this.

## Three colors

| Statement | Status | Evidence |
|---|---|---|
| `R_3 >= 21` | PROVED (literature) | Explicit proper `20 x 20` coloring, Canakci et al. 2023; matrix in `.agents/skills/directed-l-grid-research/assets/paper20.json`, checkable with `check_coloring.py`. |
| `R_3 <= 493` | PROVED (literature) | Mammel-Smith-Yerger, Integers 25 (2025) A21, Theorem 6; recorded in `literature/KNOWN_RESULTS.md` (verification date 2026-11-05; paper not reread on 2026-11-13). |
| `R_3 <= 465` | PROVED with external inputs; reviewed in repository | `research/coupled_budget_20261108/numeric_upper/THEOREM.md`. Inputs: `G(24) >= 425`, `G(25) >= 480` (distributed.net OGR-24/25 completion reports; exhaustive searches not replayed). |
| `R_3 <= 464` | PROVED with the same external inputs; reviewed in repository; integer certificate rerun 2026-11-13 (PASS, margin `477965143`) | `research/kernel_compatibility_20261108/geometry/SIX_CLASS_LEMMA.md`, `geometry/audit_464.py`, `review/REVIEW.md`. Proof read in full for this snapshot. Not merged to `main`; not in the manuscript. |
| `R_3 <= 462` | PROVED with the same external inputs; certificate rerun 2026-11-14 (PASS, `3^37` words, margin `23276682`); proof read in full | PR 11 `research/boundary_certificates_20261115/README.md`; review `research/upper_bounds_20261114/pr11_review/REVIEW.md`. Not merged. |
| `R_3 <= 461` | UNDECIDED; the fixed-diagonal prefix family is numerically near exhaustion at 461 (>= 62,547 bad prefix classes; adaptive kernels exclude about 7%) | `research/upper_bounds_20261114/proof.md`, Section 6 |
| Shape-cost certificate at 463 (historical, global counting line) | FAILED (negative margin) | `research/global_counting_20261108/review/REVIEW.md`. The tested shape-cost certificate at `n = 463` has negative margin `-2534488525`. |
| `R_3 <= 379` | CONDITIONAL on S21 | `manuscript/main.tex`, `thm:s21three`. |
| `R_3 <= 361` | CONDITIONAL on existential G9 for spans up to 360 | `cor:g9-three`. |

**Working interval: `21 <= R_3 <= 462`** (PR 11, reviewed 2026-11-14; previously 464), the upper end resting on two
external computational theorems and an in-repository review.

Open bridges recorded at the checkpoint (all three are proof gaps, none is a
bound): (1) a uniform positive lower bound for the cross-source request cost
`sum_q min(V^a, H^b, H^e + V^e)`; (2) uniform control, for one long diagonal
word, of truncated autocorrelation and two-end matching capacity across all
levels at once; (3) a lower estimate on the number of near-extremal ruler
occurrences to play against the proved upper budget of 56 span-425 classes.
Savings from (2), (3) and the colored-boundary count constrain the same
24-mark classes and must be intersected, not added.

Open source-level assertions (manuscript labels): G9, existential G9, S21,
EP10, H10. Whether any finite uniform coefficient `T <= C*M` holds for
properly two-colored sources is open.

## Four colors

| Statement | Status | Evidence |
|---|---|---|
| `R_4 >= 21` | PROVED (trivial from `R_3 >= 21`) | A three-coloring is a coloring with at most four colors. No dedicated four-color lower bound was found in the records read. |
| `R_4 <= 22049225` | PROVED, elementary and self-contained; exact check rerun 2026-11-13 | `research/four_color_sensitivity_20261113/README.md`, section 3. Three nested applications of the manuscript shift count (`lem:shift`); no external input. Not independently reviewed. |
| `R_4 <= 21991300` | PROVED per repository history; reviewed in repository; certificate arithmetic rerun 2026-11-13 (PASS) | `exploration/research_round3/four/R3_R4_REPORT.md`, certificate `r4_profile_endpoint_21991300.json`, review `exploration/research_round3/audits/fresh_astra/REVIEW.md`. Depends on Round-2 lemmas FM1, FM2-4, FM3 under `exploration/research_round2/`, which were **not** re-audited on 2026-11-13. Absent from `README.md`, `docs/RESULTS_INDEX.md`, and `literature/KNOWN_RESULTS.md` at the checkpoint. |
| `R_4 <= 21987409` | PROVED, elementary and self-contained; rerun 2026-11-14 by PR 11's verifier and by an independent re-implementation (identical margin) | PR 11 `research/boundary_certificates_20261115/FOUR_COLOR.md`; `research/upper_bounds_20261114/pr11_review/`. Not merged. |
| `R_4 <= 98777` | CONDITIONAL on S21 (spans up to 98775) | `manuscript/main.tex`, `thm:s21four`. Not an established bound. |
| `R_4 <= 4.62 * 10^3 * q` (table) | CONDITIONAL on a binary-source bound `M <= q*L` | `research/four_color_sensitivity_20261113/`. Any proved `q <= 4765` on spans up to `21991297` would beat `21991300`. |

**Working bound: `R_4 <= 21987409`** (PR 11, elementary, independently re-executed 2026-11-14); earlier figures `21991300` and `22049225` are superseded.

Literature: `manuscript/main.tex` (`thm:general`) derives
`R_k <= exp(O((log 2k)^600))` from the quasipolynomial corners theorem with
an unspecified constant, hence no number for `k = 4`. A limited web search
on 2026-11-13 found no published explicit four-color bound for this
configuration (Graham-Solymosi give a general-`k` bound). This is absence of
a discovered match within one search, not a proof that none exists.

Other general-`k` claims in history (`exploration/research_round3/general/`):
`R_5 <= 15^16`, `R_k <= [k(k-2)-1]^(2^(k-1))` for `k >= 6`; inventoried, not
read.

## Known structural facts that shape strategy

- The capacity recursion has exponents `1/2, 3/4, 7/8`: Golomb sets, sets
  with a binary source, sets with a ternary source. `R_3` uses two levels,
  `R_4` three.
- A Golomb set with monochromatic strict triangle is a proper source, so the
  first level cannot be improved inside a single completion-closed region
  (`exploration/research_round3/general/square_root_barrier.md`). Improvement
  must couple levels, lags, sources, or the full grid.
- A single diagonal class can satisfy every per-lag cap at `n = 464` (the
  155-set recorded in `exploration/research_round3/STATUS.md`; inventoried).
  One-class arguments alone are therefore near exhaustion for `R_3`.

See `obstructions.md` for refuted statements.
