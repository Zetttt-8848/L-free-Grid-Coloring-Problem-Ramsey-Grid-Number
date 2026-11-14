# Where the current upper-bound arguments lose information

Dated analysis (2026-11-13, checkpoint `dc1cbe6daf7d`). It is a map for
generating candidates, not a list of mandated routes. Revise it when a proof
changes or a loss is closed. Numbers are quoted from the records cited in
`lgrid-research/references/state.md`.

## The three-color chain (`R_3 <= 464`)

```text
proper 3-coloring of [n]^2
 -> diagonal classes A_0, A_1, A_2 (partition of the main diagonal)
 -> for each lag d: six completion classes B_(c,b)(d), pairwise disjoint,
    each a Golomb set inside n-d positions
 -> joint cap R_d <= U(n-d), using G(24) >= 425, G(25) >= 480 and distinct
    minima of 24-mark classes
 -> pointwise Cauchy on f_c * w with sum_c f_c = 1:
    sum_d (n - d - 3 U(n-d)) a_d <= n a_0, contradicted at n = 464
```

| Step | What is kept | What is discarded |
|---|---|---|
| Diagonal classes | The partition of one diagonal | All other diagonals `W_c`, `c != 0`, except through completion colors of same-class pairs |
| Completion classes | Colors of cells `(u+d, u)` with `u, u+d` in one class | Cells whose two diagonal endpoints have different colors (about two thirds of the square), used only in the cross-source request count |
| Golomb cap | Cardinality of each class | Which ruler it is. 24-mark rulers in 426-431 positions are few and rigid; the bound uses only their existence. Near-extremal 23-mark rulers are not classified at all |
| Per-lag cap | One number per lag | Classes at lags `d` and `d'` are fibers of the same set under the same coloring; only adjacent-lag endpoint words are coupled so far |
| Cauchy | A second moment at window scale about 85 | Equality requires all three classes equidistributed in every window; the deficit is used only through integer rounding |
| Single weight `w` | One linear functional | The cone of all valid functionals; scanned families are not optimal duals |

Unresolved bridges at the checkpoint, each a place where retained
information has not yet been summed: cross-source request cost; all-level
two-end matching for one diagonal word; a lower bound on near-extremal
occurrences against the upper budget of 56.

Candidate seeds (unranked, unproved):

- A stability statement for rulers one mark below optimal in about 430
  positions, turning the cap into a cost for every lag, not only for
  saturated ones.
- Exact joint feasibility of the endpoint words over a block of consecutive
  lags, as a finite optimization whose dual is a proof.
- Using a second diagonal `W_c` as a source in its own right and coupling it
  to the main diagonal through the cells they share.

## The four-color chain (`R_4 <= 21991300`)

```text
proper 4-coloring of [n]^2
 -> a diagonal class D (ternary source), n/4 marks or joint Cauchy over four
 -> for each lag h: F_h(D) splits into 3 sets E, each with a binary source
 -> for each lag h': F_h'(E) splits into 2 Golomb sets
 -> three nested capacity bounds with exponents 1/2, 3/4, 7/8
```

| Level | Bound used | Loss |
|---|---|---|
| Golomb | Elementary neighbor/shift count, cap about `sqrt(L) + L^(1/4)` | Negligible at this scale |
| Binary source | Only `r_h(E) <= 2 Q(L - h)` | The whole content of proper two-colorability beyond "fibers are two Golomb sets". This is the same missing statement as S21/H10/G9, but in a different regime |
| Ternary source | Only `r_h(D) <= 3 * cap(binary)` | The three parts at one lag, and parts at different lags, are fibers of one set under one coloring |
| Square | One diagonal, pigeonhole or joint Cauchy | All other diagonals and all mixed cells |

### Sensitivity (exact results in `research/four_color_sensitivity_20261113/`)

- If properly two-colorable strict sources satisfy `M(A) <= q L(A)` on the
  needed span range, then `R_4 <= N(q)`, with `N(q)` between `4614 q` and
  `4745 q` at the twelve tabulated values `10 <= q <= 4500`
  (`N(21) = 98733`).
- The archived unconditional bound corresponds to an effective coefficient
  about 4765 at span `2.2 * 10^7`: **any** proved `q <= 4765` on spans up to
  `21991297` improves `R_4`.
- Heuristic scaling (not a theorem): the bound behaves like the fourth power
  of the binary-level capacity, so a one percent reduction of that capacity
  at large span is worth about four percent of `R_4`.

Consequences for strategy:

- For `R_4`, a **qualitative** improvement at the binary level (any exponent
  below `3/4`, or a linear bound with a constant in the thousands) dominates
  every refinement of weights and profiles. Tools that are useless for `R_3`
  because of poor constants (energy increments, Balog-Szemeredi-Gowers-type
  structure, hypergraph coloring obstructions for fibers) are admissible
  here, provided every constant is made explicit.
- For `R_3`, the same statement is needed with `q <= 25` on spans up to 450:
  sharp constants, small spans.
- The two-Golomb accounting summed over lags reproduces exponent `3/4`
  (second-level cube count); a proof below `3/4` must use more than "every
  fiber is a union of two Golomb sets". Candidates: compatibility of the
  two-class splittings of different fibers, which share completion cells;
  the hypergraph two-coloring problem that each fiber must solve.

## Losses common to both chains

- Only one diagonal of the grid is used at the top level.
- Translation and sub-square structure: every sub-square is itself a proper
  coloring, so every statement holds at every position and scale
  simultaneously; the arguments use one scale.
- Upper triangle versus lower triangle: the configuration is not symmetric
  under transposition for a fixed coloring; arguments stated for the lower
  triangle have counterparts whose joint use is unexplored.
