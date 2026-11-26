# Research state snapshot

Snapshot date: 2026-11-26. Pins: `pins.json`. This file is a dated summary
with pointers; the cited project records are the authority. If
`scripts/refresh_state.py` reports a moved pin, the affected lines below are
unverified until re-derived. Evidence labels follow `lgrid-verify`.

"Reviewed in repository" means an in-repository audit by an independent
verification agent exists. It is not an external referee report and not a
formal proof. "Rerun 2026-11-26" means the named checker was executed in the
session that wrote this snapshot.

## Where the work lives

| Ref | Commit | Content |
|---|---|---|
| `codex/swarm-r3-r4-20261126` | `b3bff4112585` | **Latest research checkpoint.** Certifies `R_3 <= 138` (`research/r3_side138_20261126/`), `R_4 <= 21,947,741` (`research/r4_mcf_minimax_20261126/`), exact strict binary-source minimum spans `e_1..e_16` and `C(1)..C(27)` (`research/binary_source_spans_20261126/`), and `S_6..S_10` four-color zero-rainbow square witnesses. |
| `codex/antigravity-r3-r4-20261123` | `d18a9650826e` (remote `c5a6394fcb9a`) | `R_3 <= 139` (`research/weak_triangle_20261123/SIDE_139.md`), `R_4 <= 21,947,830` (`research/r4_stratified_farkas_20261124/`), `r_14 >= 15` (`ORDER14_MIN15.md`). Contained in `b3bff4112585`. |
| `codex/weak-triangle-certificates-20261123` | `98af36bdb368` | PR 11 head: `R_3 <= 144`, `R_4 <= 21,947,877`, local rainbow catalogs (`research/boundary_certificates_20261115/`). Contained in `b3bff4112585`. |
| `origin/codex/r4-local-capacity-round3-20261114` | `14647e607c25` | Codex Lane A Rounds 1-3 (`R_4 <= 21,947,865`, short-request duals, reflected-Golomb obstruction). Sibling branch from `726998b`; finite-seed and window inputs superseded in-tree by `b3bff4112585`. |
| `origin/kimi/r4-hybrid-dual-20261116` | `1da352c4cb1f` | Kimi Rounds 1-5 (`k`-color strict-triangle line identity, `S_3..S_5` zero-rainbow 4-color witnesses, nonuniform `m=6` scale duals, Q3a and O1 refutations). Sibling stack atop `14647e607c25`. |
| `origin/claude/r4-grid-compatibility-20261114` | `deb509763d43` | Claude Lane B Rounds 1-2 (P1 request/double-cover calculus, G1+/Theorem W `t`-peak width bijection, `C(20)=13`, `n_rel(3) >= 61`, outer-kernel optimality check). Sibling branch from `726998b`. |
| `origin/claude/upper-bounds-20261114` | `4517f60d7c9d` | Early PR 11 review, word-adaptive prefix tests at 461, partition relaxation `P_3(n)` SAT for `n <= 62`. |
| `origin/codex/global-counting-research-20261108` | `dc1cbe6daf7d` | Earlier 2026-11-13 checkpoint (`R_3 <= 464` in `5b5db22c3c65`, `465` in `654cc044cad3`, boundary obstructions in `df6e35cfff68`). Contained in `b3bff4112585`. |
| `origin/codex/three-cube-*` | `d6755b4`, `7f8e8bf`, `a53970c` | Three-cube forcing, boundary budgets, pair-repair refutation (open PRs 1-3 on old `main`, not in checkpoint). |
| `origin/main` | `1231d436d199` | English conversion of the imported manuscript and records. Literature baseline only. |

## Three colors

| Statement | Status | Evidence |
|---|---|---|
| `R_3 >= 21` | PROVED (literature) | Explicit proper `20 x 20` coloring, Canakci et al. 2023; `.agents/skills/directed-l-grid-research/assets/paper20.json` (`check_coloring.py`). Proper `20 x 21` rectangle in `research/boundary_certificates_20261115/RECTANGLE_20_21.md`. |
| `R_3 <= 493` | PROVED (literature) | Mammel-Smith-Yerger, Integers 25 (2025) A21, Theorem 6; `literature/KNOWN_RESULTS.md`. |
| `R_3 <= 465`, `464`, `462`, `461` | PROVED with external inputs (`G(24) >= 425`, `G(25) >= 480`) | `research/coupled_budget_20261108/`, `research/kernel_compatibility_20261108/`, `research/boundary_certificates_20261115/THREE_COLOR_461.md`. |
| `R_3 <= 144`, `143`, `141`, `140`, `139` | PROVED, computer-assisted, self-contained in repository; rerun 2026-11-26 (PASS) | `research/boundary_certificates_20261115/THREE_COLOR_WEIGHTED.md` (`144`) and `research/weak_triangle_20261123/SIDE_139.md` (`139`, margin `384,370,061`, `r_14 >= 15`). Zero external OGR assumptions. |
| **`R_3 <= 138`** | **PROVED, computer-assisted, self-contained in repository; reviewed in repository; integer certificate rerun 2026-11-26 (PASS, margin `1,659,966,634`)** | `research/r3_side138_20261126/README.md`, `verify.py`, `certificate.json.xz`. Asymmetric physical-corner pricing on `S_138`, `T_13` 16/17/18-square survivor intersections, 19 directional subtriangle rays on `T_14..T_18`, and upgraded local packings (`r_19..r_40`). Zero external OGR assumptions. |
| Any bound below 138 | UNDECIDED | Exploratory dual LP at `N = 137` reaches `W_LB = 1.049678 > 1` (`research/r3_side138_20261126/README.md`). |
| `R_3 <= 379` (under S21), `R_3 <= 361` (under existential G9) | CONDITIONAL (manuscript, numerically superseded by unconditional `138`) | `manuscript/main.tex`, `thm:s21three`, `cor:g9-three`. S21 and G9 themselves remain open. |

**Working interval: `21 <= R_3 <= 138`** (unconditional, self-contained in repository).

Open source-level assertions (manuscript labels): G9, existential G9, S21, EP10, H10. Exact order-14 triangle rainbow minimum narrowed to `15 <= r_min(T_14) <= 17` (`research/weak_triangle_20261123/ORDER14_MIN15.md`).

## Four colors

| Statement | Status | Evidence |
|---|---|---|
| `R_4 >= 21` | PROVED (trivial from `R_3 >= 21`) | A three-coloring is a coloring with at most four colors. |
| `R_4 <= 22,049,225` and `R_4 <= 21,987,409` | PROVED, elementary and self-contained | `research/four_color_sensitivity_20261113/README.md` (`22,049,225`) and `research/boundary_certificates_20261115/FOUR_COLOR.md` (`21,987,409`; recursive span bounds without external window tables). |
| `R_4 <= 21,947,877` .. `21,947,830` | PROVED, computer-assisted; rerun 2026-11-26 (PASS) | `research/boundary_certificates_20261115/FOUR_COLOR_EDGE_VARIANCE.md` (`21,947,877`), `research/r4_disjoint_edge_bins_20261123/` (`21,947,855`), `research/r4_subadditive_farkas_20261124/` (`21,947,834`), `research/r4_stratified_farkas_20261124/` (`21,947,830`). |
| **`R_4 <= 21,947,741`** | **PROVED, computer-assisted, self-contained in repository; reviewed in repository; exact certificate rerun 2026-11-26 (PASS, margin `+67,076,013,380,690,640,788,136,578,854,518,589,429,308,720`)** | `research/r4_mcf_minimax_20261126/README.md`, `verify.py`, `certificate.json.xz`. Exact-integer 200-bin min-cost-flow Farkas duals (`window_tables/` vendored in-tree with SHA-256 verification), triple-checker-verified `e_2..e_16` finite seeds, multiset-monotone nonuniform binary spans through `22,000` marks, and 3-segment (`S = 39 = 13+13+13`) KD-tree outer matching DP proving `>= 99` missing matches across 562 disjoint blocks (negative margin at `21,947,740`). |
| Exact binary-source spans `e_1..e_16` and `C(1)..C(27)` | PROVED, computer-assisted, self-contained in repository; reviewed in repository; rerun 2026-11-26 (PASS) | `research/binary_source_spans_20261126/README.md`, `verify.py`, `seed_trees_k16.bin.xz`, `witnesses_k2_k16.json`. Exact `e_1..e_16 = (0,1,2,3,4,6,7,9,10,12,14,17,19,21,24,27)` and `C(6)=5..C(27)=15`. |
| `R_4 <= 98,777` | CONDITIONAL on S21 (spans up to 98,775) | `manuscript/main.tex`, `thm:s21four`. **Not** an established bound. |
| `R_4 <= 4.62 * 10^3 * q` (table) | CONDITIONAL on binary-source `M <= q*L` | `research/four_color_sensitivity_20261113/`. |

**Working interval: `21 <= R_4 <= 21,947,741`** (unconditional, self-contained in repository).

## Known structural facts that shape strategy

- The 1D main-diagonal capacity recursion has exponents `1/2, 3/4, 7/8`. For `R_3`, full-square 2D cross-diagonal shifted-triangle coupling bypasses the 1-diagonal same-class relaxation floor (`n_rel(3) >= 61`, `origin/claude/r4-grid-compatibility-20261114`) to reach `138`.
- For `R_4`, by contrast, the 4-color strict-triangle line identity leaves an `~ (1/4) C(N,3)` rainbow ceiling (`origin/kimi/r4-energy-20261115`) and explicit proper 4-colorings of `S_3..S_10` have zero rainbow Ls in `T_m` (`research/r4_mcf_minimax_20261126/zero_rainbow_witnesses.json`), blocking direct 4-color local rainbow scaling.

See `obstructions.md` for refuted statements.
