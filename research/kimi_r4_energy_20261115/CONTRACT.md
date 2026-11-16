# Contract: four-color line energy and full-square finite kernels

Date: 2026-11-15. Author: Kimi.
Branch: `kimi/r4-energy-20261115`.
Base: `b7d52434061f7cb15395d50edc949e2700356926`.

## Governing objective and nonduplication

The only objective is a rigorous improvement of a Ramsey upper bound, with
`R_4` prioritized. A finite result is supporting evidence only; it is not an
upper bound unless it enters a proved argument starting from an arbitrary
coloring of a full square.

GitHub authentication, all 19 pre-existing branches, and all 12 open pull
requests were refreshed before this experiment. No remote research head had
moved since round 3. Codex remains at
`14647e607c2525b0cd12081b03899827d306a030`; Claude's two research heads remain
`8c2308fd48a7cdcb07dbf6afe8b50a37362e59b1` and
`4517f60d7c9d9284cb0b60428f7cb362d59d02c4`. PR 11 remains at
`98af36bdb368609f38bc350b664310d7a5b45877`. No collaborator bound is adopted
without an independent audit.

Read for this lane: the governing skills, state refresh, information-loss and
obstruction maps; manuscript Lemmas `lem:variance` and `lem:weighted`; PR 11's
`THREE_COLOR_WEIGHTED.md`, `FOUR_COLOR_DOUBLE_WINDOW.md`, and
`FOUR_COLOR_EDGE_VARIANCE.md`; Codex's round-3 theorem and report; Claude's D1
preregistration, grid-compatibility report, and upper-bound proof. The stale
state snapshot is not used as evidence for a moved numerical bound.

This package does not enter binary-source capacities, hereditary rank transfer,
request multiplicities, ternary MS*, prefix certificates, or three-color local
triangle catalogs. The proposed finite objects are complete four-colored
squares, not sparse sources or partially colored triangles.

## Object and coordinates

Use zero-based cells `(x,y)`. An L is
`L(x,y;d)={(x,y),(x+d,y),(x+d,y+d)}`, with integer `d>0`. Define the complete
strict triangle

```text
T_N={(x,y):0<=y<x<N}.
```

Its horizontal, vertical, and slope-one lines each have one line of every
length `1,...,N-1`. Every unordered pair on such a line has its unique directed
L completion inside `T_N`. Every L contained in `T_N` has the form
`(u+d,u),(v+d,u),(v+d,v)` for `u<v`, `d>0`, and `v+d<N`.

For a coloring with palette `[k]`, let `n_(lambda,i)` count color `i` on line
`lambda`, and define

```text
M=C(N,2), C=C(N,3), S=N(N-1)(2N-1)/2,
D_k=sum_(lambda,i) (n_(lambda,i)-|lambda|/k)^2.
```

Let `P_k` be the total number of equal-color pairs on all three line families,
and let `R_k` count Ls using three distinct colors.

## Route N: exact proposition and cheapest consumer test

N1. Prove or refute, for every proper `k`-coloring of `T_N`,

```text
P_k+R_k=C,
D_k+2R_k=2C-S/k+3M.
```

For `k=3`, the second identity must reduce exactly to manuscript
`D_3+2R_3=N(N-1)`.

N2. For `k=4`, derive the exact line-balanced lower bound on `P_4` and the
resulting upper bound on `R_4`. Test the proposed pure-energy Ramsey consumer:
a contradiction would require the line-balanced equal-pair lower bound to
exceed `C`, or equivalently the derived rainbow upper bound to be negative.

The predicted leading coefficient check is `P_4/C -> 3/4`, not a constant
above one. This prediction is not assumed in the proof. Compute exact rational
values at small `N`, including boundary and integrality terms, and determine
the asymptotic gap from the formulas rather than a numerical scan.

### Stop condition for Route N

Stop the pure second-order energy route if the identity is only the general
four-color form of the existing line identity or if its leading coefficient
cannot contradict properness at any `N`. Do not run a large energy scan and do
not add higher-order statistics without a new stated consumer.

## Route F: full-square finite kernels with an upper-bound consumer

If Route N has no contradiction, test the following distinct fallback. For a
proper four-coloring `chi` of a complete `m by m` square, let `r_m(chi)` count
rainbow Ls contained in its strict lower triangle. Define

```text
rho_m=min_chi r_m(chi),
```

where the minimum is over every proper coloring using at most four colors.
The square supplies cells outside the triangle as part of the finite kernel;
this is not a minimum over arbitrary partial triangle colorings.

F1. Determine `rho_m` exactly for the preregistered small orders `m=3,4`, and
attempt `m=5` only if the same complete enumeration stays within its explicit
budget. Use first-appearance color renaming only after proving that every
coloring has exactly one such representative. Store the complete enumeration
tree counts, all minimizers up to that renaming, and an independent literal
checker. A timeout or incomplete branch coverage is UNDECIDED.

F2. Before using any positive `rho_m`, prove the full-square embedding chain.
A geometry-preserving square copy has cells
`{(a+s*i,b+s*j):0<=i,j<m}` with integer `s>0`. With nonnegative finitely
supported scale weights `a_s`,

```text
J=sum_s a_s*(N-s*(m-1))^2,
Lambda_h=sum_(j|h, 1<=j<=m-2) a_(h/j)*C(m-j,2).
```

The intended implication is
`rho_m*J <= sum_L Lambda_(step(L))*indicator(L is rainbow)` in every proper
four-color `T_N` arising as the strict lower triangle of an arbitrary proper
full square. Every boundary truncation and overlapping copy must be included.
If `Lambda_h<=K` for all `h`, combine this with the Route N upper estimate on
the total rainbow count. A strict positive exact-arithmetic margin at a stated
`N` would prove `R_4<=N`; otherwise it is not a bound.

### Stop condition for Route F

Stop if `rho_m=0` throughout the completed test range, if enumeration is not
complete, or if the best preregistered uniform-incidence consumer has no chance
to overcome the exact rainbow ceiling. Do not enlarge the same search merely
because it is inconclusive. Any positive local minimum without a closed
full-square consumer is reported as a finite lemma only, not as progress on a
numerical bound.

## Information retained that the incumbent loses

Route N retains all three line directions and all four color indicators on the
full strict triangle. Route F additionally retains the surrounding square and
all scale-labelled copies, rather than discarding every off-diagonal cell after
a main-diagonal capacity reduction. The test must distinguish this retained
information from a coloring-independent identity.

## Nearest known obstruction

The three-color line identity is already in the manuscript. PR 11 already uses
weighted local rainbow catalogs for three colors; this round must not claim
that mechanism as new. Four colors permit a positive cubic rainbow ceiling, so
an arbitrary positive local minimum need not yield a contradiction. Round 3's
quotient identities are coloring-independent and supply no lower bound here.
No conditional S21/G9 statement may be used.

## Status and evidence required

Supply exact formulas, standalone generators and independent verifiers, raw
JSON output, all finite witnesses or complete coverage data, commands,
interpreter version, and hashes. Validate any enumerator on known small cases
and test both properness and rainbow counts literally. State `No new Ramsey
bound` unless the arbitrary-full-square chain and exact final inequality are
both closed. Internal checks are not external peer review or Lean
formalization.
