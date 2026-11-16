# Contract: incidence erratum and multiscale quotient consumer

Date: 2026-11-15. Author: Kimi.
Branch: `kimi/r4-multiscale-20261115`.
Base: `kimi/r4-off-diagonal-20261115` at
`af166bc27aaa3f22b4f62907d983fbecb20f4aec`.

## Frontier refresh and nonduplication

GitHub authentication, all 19 repository branches, and all 12 open pull
requests were refreshed before this contract. The Codex lane remains at
`14647e607c2525b0cd12081b03899827d306a030` for round 3 and occupies binary
source capacities, hereditary rank transfer, collisions, short requests, and
exact windows. Claude's grid-compatibility branch is
`8c2308fd48a7cdcb07dbf6afe8b50a37362e59b1`; its upper-bound branch is
`4517f60d7c9d9284cb0b60428f7cb362d59d02c4` and occupies ternary sources, MS*,
prefix certificates, and local triangle refutations.

PR 11, from fork branch `research/directed-l-boundary-20261115` at
`98af36bdb368609f38bc350b664310d7a5b45877`, now reports `R_3<=144` and
`R_4<=21,947,877`. Its `THREE_COLOR_WEIGHTED.md`, `FOUR_COLOR_DOUBLE_WINDOW.md`,
and `FOUR_COLOR_EDGE_VARIANCE.md` were read. These newest claims have not been
independently audited here and are not inputs to this package. PR 12 reviews an
older PR 11 head, not these newest claims. This round does not enter weighted
rainbow catalogs, diagonal capacities, or prefix search.

Read in full for this lane: the governing skills and state refresh, the dated
information-loss and obstruction maps, Kimi's round-1 theorem, report, handoff,
and averaging scripts, and manuscript Lemma `lem:variance` through Lemma
`lem:weighted`. The state refresh reports old pins stale; no stale numerical
bound is promoted.

## Object and coordinates

Use zero-based cells `(x,y)` in the full `[n]^2` square. An L is
`L(x,y;d)={(x,y),(x+d,y),(x+d,y+d)}`, with integer `d>0`. A proper coloring has
no monochromatic L. The seven palette quotients are the nontrivial bipartitions
of four colors, up to interchanging the two sides. An L is pair-tight for a
quotient when all its at most three original colors lie in one side.

For a contiguous 5 by 5 block `B`, let `q(B)` be its number of distinct
pair-tight Ls. Let `P_d` be the number of pair-tight Ls of step `d` in the host.
For a scale `s>=1`, a geometry-preserving copy is
`{(a+s*i,b+s*j):0<=i,j<5}` inside the host. No arbitrary unequal row and column
selection is allowed.

## Exact statements to test

E1 (audit of the published Q3a). The old statement was

```text
sum_(d=1)^4 P_d/(5-d)^2 >= 3(n-4)^2.
```

Test its proof and its numerical validity. In particular, independently check a
6 by 6 crop of the stored proper 20 by 20 coloring, enumerate all 55 Ls, and
evaluate the exact rational left side. A left side below `12` is a complete
counterexample. Also test the claimed position-independent multiplicity
`(5-d)^2` by literal block enumeration.

M1 (signature trichotomy). For every three-cell color word in four colors, the
signature size is respectively 7, 3, or 1 when the word uses 1, 2, or 3 colors.
Consequently every geometric L in every four-coloring is pair-tight for some
quotient, and `P_d=(n-d)^2`. Exhaust all `4^3=64` words independently.

M2 (exact multiscale replacement). For each copy family at scale `s`, compute
the literal copy multiplicity `m(L;s)` of every L, including all boundary and
cross-scale incidences. Determine whether the quotient-cover lower bound gives
any inequality beyond the exact geometric incidence count. Also test the
quotient-incidence version obtained by summing signature sizes.

## Information retained that the incumbent loses

The proposed objects retain all palette bipartitions, all cell positions, and
all geometry-preserving scales rather than only one main diagonal. The audit
must nevertheless distinguish retained labels from a count that is actually
independent of the coloring.

## Cheapest discriminating test and stop condition

Use only the 64 color words, the stored finite witness, and direct enumeration
of all copies and Ls at sides 5, 6, 9, and 10 with authorized scales. No random
sampling or capacity run is needed. Stop the quotient-count route if E1 fails,
if the corrected copy count is identical for proper and improper colorings, or
if the seven-quotient lower bound is dominated by the trivial nonempty signature
of every L. Do not enlarge the same search after any such outcome.

## Consumer chain if successful

A Ramsey improvement would require a new inequality involving actual coloring
data, followed by a proved upper estimate and a contradiction for an arbitrary
proper four-coloring of a specified full square. If the object is a geometric
identity for all colorings, there is no such consumer. A structural statement
without that chain will be labelled accordingly.

## Nearest known obstruction

Round 1 already refuted arbitrary combinatorial subselection and universal
three-L cover sufficiency. Round 2 refuted two-diagonal product-class fiber
reduction. The present test must not revive either premise. Manuscript weighted
triangle embeddings and PR 11's weighted catalogs are separate occupied routes.

## Status and evidence required

Preserve the original Q3a record with an explicit SUPERSEDED/REFUTED pointer if
it fails. Supply the complete witness, a standalone definition-level checker,
raw output, exact commands, interpreter version, and hashes. Q1 and Q2 require
separate statements; an error in Q3a must not be misreported as refuting them.
State "No new Ramsey bound" unless every full-square reduction closes. Internal
verification is not external review or formalization.
