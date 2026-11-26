# Refuted statements and what survives them

Each entry names the exact proposition that failed, the evidence, and the
variants it does **not** rule out. A counterexample refutes a statement, not
a direction. Add entries when a formulation fails; cite the record that holds
the witness. Entries marked (summary) were taken from a project summary and
the underlying witness was not reread on 2026-11-13.

| Refuted or blocked statement | Evidence | What failed | What remains open |
|---|---|---|---|
| Local rainbow premises `F_11(5)`, `F_12(7)`, `F_13(17)` (every proper three-coloring of the complete strict triangle on `m` marks has at least `rho` rainbow corners) | `manuscript/main.tex`: `prop:local-rainbows`, `prop:t13`; explicit colorings | The numerical premise, not the weighted arithmetic built on it | Rainbow counts with different thresholds, or on restricted sources, need fresh evidence |
| "No injective five-cube implies a linear energy or corner bound" | `prop:cube-free-energy` (construction with `E >= n^(73/26)/2`) | Cube exclusion is only a necessary condition | Arguments that use proper colorability itself rather than cube exclusion |
| "Per-fiber two-Golomb bounds sum to `T(A) <= 2 M(A)`" | `cor:moments`; summation yields a higher-order cube count | Fibers of different lags share completion cells | A bound that accounts for the shared cells with true multiplicity |
| "Choosing the coloring controls `2T - M`" | `thm:forcing`: `2|E| - sum s_d^2 = 2T - M` depends only on `A` | Forcing edges and imbalance trade off exactly | An independent bound on either term |
| "A globally optimal source potential balances every local three-cube block" | `research/boundary_extension_20261108/upper/README.md` (exact optima 9 and 13 with fixed exterior) (summary) | Local and global optimality are incompatible in a complete source | Amortized or boundary-aware potentials |
| "A fixed boundary can always be repaired by changing one or two cells"; "radius 8 suffices in general" | PR 3 (`origin/codex/three-cube-pair-repair`, not in the checkpoint line) (summary) | Small-step repair has disconnected components | Repairs that may move the boundary and pay for it |
| "A single-defect `21 x 21` candidate is close to a proper coloring" | `research/coupled_budget_20261108/lower/README.md`: no repair within radius 10 (summary) | Monochromatic-L count is not a repair distance | Nothing about `R_3 >= 22` either way |
| "Local forced imbalance adds to the total source cost" | `research/coupled_budget_20261108/structural/README.md` (summary) | External cells of the same fiber can cancel it | Accounting with explicit external terms |
| "The six raw joint capacities can all be attained at consecutive lags" | `research/kernel_compatibility_20261108/geometry/SIX_CLASS_LEMMA.md` | Endpoint words force one common color, contradicting the color-incidence refinement | The weighted deficit this yields is not yet enough for 463 |
| "`C_mix = 0` characterizes extendability"; "the listed H/V requests are all requests" | `research/global_counting_20261108/review/REVIEW.md`, scope findings 1-3 | Parallel-input requests are omitted; the condition is necessary only | A complete request family, or a uniform positive lower bound for the listed one |
| "Scalar autocorrelations `R_d` determine two-end matching capacity" | `research/global_counting_20261108/information_gap.json` (two nine-letter words) | `R_d` discards pairing information | Bounds stated directly on the paired statistic |
| "The first capacity level can be pushed below square root inside one region" | `exploration/research_round3/general/square_root_barrier.md` (Golomb construction) | A Golomb set with monochromatic triangle is proper | Bounds coupling several levels or the full grid |
| "A single diagonal class cannot meet all per-lag caps at `n = 464`" | 155-set, `exploration/research_round3/STATUS.md` (summary) | One-class feasibility is YES | Joint arguments over all three classes and their completions |
| "Hypothetical capacity reductions in the calibration scripts are results" | `origin/codex/recover-claude-calibration-20261113`, `README.md` | They are scenarios over scanned weight families | Each scenario is a target lemma; none is proved |
| "Proper four-colorings of small full squares force positive rainbow counts `rho_m^(4) > 0` in `T_m` (`3 <= m <= 10`, including the `m = 6` consumer bridge `rho_6^(4) > 17.376`)" | `origin/kimi/r4-energy-20261115` (`m=3..5`), `origin/kimi/r4-hybrid-dual-20261116` (`1da352c`), and `research/r4_mcf_minimax_20261126/zero_rainbow_witnesses.json` (`m=6..10`) | Explicit proper 4-colorings of `S_3..S_10` have `rho_m^(4) = 0` in `T_m` (`0` across all of `S_6, S_7`), and the 4-color line identity leaves an asymptotic `(1/4) C(N,3)` rainbow ceiling | Larger orders where `R_3(L)` forces rainbows, or non-rainbow 4-color mechanisms |
| "Unrestricted binary-source energy satisfies `E <= C * R` for an absolute constant `C`" | `origin/codex/r4-binary-compatibility-20261114` (`fb33871`), `THEORY.md` | Reflected-Golomb proper binary sources achieve `E / R = (4r + 2) / 3 -> infinity` | Near-extremal or fixed-window weighted deficit bounds (`SHORT_DEMAND.md`) |
| "Palette-quotient block scaling Q3a or two-diagonal 16-product-class reduction O1 gives a four-color capacity improvement" | `origin/kimi/r4-multiscale-20261115` (`b7d5243`, 6-square witness) and `origin/kimi/r4-off-diagonal-20261115` (`af166bc`, 3-square witness) | Pair-tight count `(n-d)^2` is coloring-independent; off-diagonal completion cells `W_{c+h}[u]` differ from `W_h[u]` | Multi-segment prefix-histogram outer DP and exact multi-bin Farkas duals |
| "A single-diagonal same-class relaxation can prove `R_3 <= 61`" | `origin/claude/r4-grid-compatibility-20261114` (`deb5097`), `round2/MX_STAGE1_RESULT.md` (`n_rel(3) >= 61`) | `[0, 61)` partitions into three proper binary sources | Full-square 2D shifted-triangle and ambient-square coupling (`R_3 <= 138`) |
| "Single-segment 4-count outer matching DP scales monotonically past `S = 35..36`" | `research/r4_mcf_minimax_20261126/README.md` | Balanced single-histogram trajectories approach 12 matches/step at large `S` | Multi-segment (`13 + 13 + 13`) prefix-quadrant KD-tree stratification (`>= 99` missing matches at `S = 39`) |

## Transfers that fail from three colors to four

- The fibers of a ternary source are not Golomb by the three-color proof;
  they are sets with a binary source. Any use of `G(24)`, `G(25)`, or OGR
  uniqueness at the top level of a four-color argument is unjustified.
- Signed completion, forcing graphs, and "balance" have no direct ternary
  analogue: excluding one color leaves a choice of two.
