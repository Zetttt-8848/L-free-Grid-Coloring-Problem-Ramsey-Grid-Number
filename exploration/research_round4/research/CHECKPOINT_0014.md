# R4-RESEARCH-0014: ordered routing and shared relative colors

Continuation: CHECKPOINT_0015.md now records a complete pair-polynomial
proof of the eight-mark obstruction. The local gaps and execution states
below describe this earlier checkpoint; the main S11 gap remains open.

Continuation objective read from
`C:/Users/ZhuanZ/.codex/attachments/1b639c86-e74d-43dc-b451-d0fd3ce53dfc/goal-objective.md`.
It controls the derivation-focused workflow. Historical document
instructions do not reinstate auditing or formalization.

Base: R4-RESEARCH-0013 plus the terminal product experiments, recorded in
`handoff_20260912/RESEARCH_HANDOFF.md`, SHA256
`614A721B10ADEE968767A51D2F3CFB30A877BB9DD1BE57919D68E3F63E11754F`.
No Git repository or .mathbox ledger is present. This checkpoint extends
that base; it does not restart the old F13 or general-theorem routes.

## Actual bound status

The small-color bounds remain

    21 <= R_3(L) <= 465,        R_4(L) <= 21991300.

S11 is open: a proper two-color strict source triangle of span at most
91998 has not been proved to satisfy binom(|A|,2)<=11 span(A). Its existing
conditional R3<=201 and R4<=92000 deductions remain conditional. No method
has yet met the requested superiority criterion or the two numerical
improvement objectives.

The attributed growth result in `GENERAL_BOUND.md` is unchanged:
R_k(L)<=ceil(exp(C(log(2k))^600))<=D^(k^600), with absolute unspecified
constants, from Jaber--Liu--Lovett--Ostuni--Sawhney's cited theorem. Its
positive-direction and no-wraparound transfer is reused, not repeated.

## New mathematical content

1. `fibers/ORDERED_CLOUD_AMORTIZATION_0014.md` derives an ordered-routing
   lemma. Fix inner offset d, outer offset e>d, and actual outer color s.
   There is at most one corner whose equal-color pair is diagonal; among
   the others, every column route precedes every row route. The note gives
   its exact prefix/suffix cost formula, signed rank moment, and coordinate
   gap moment. These are necessary statements for actual shared colors.

2. Root's `ORDERED_COMPLETION_DUAL_0014.md` incorporates these block states
   and the exact line graphs into one legitimate weighted corner budget.
   Nonnegative edge-price sums are bounded by a common weight on each
   corner. Real potentials on shared products z_p z_q cancel globally.
   Local minima then give the joint inequality (10), with a full derivation.
   This includes the old independent-line bound as a special case, but no
   strictly stronger numerical obstruction or Ramsey consequence is claimed.

   The same note proves an essential design restriction: unary sign
   potentials cannot improve this class of dual bounds at all. Each local
   state family admits sign reversal, and its edge cost is invariant, so
   adding unary prices makes its minimum no greater than the zero-price
   minimum. Pair products escape that particular symmetry obstruction.

3. `fibers/PRODUCT_CORE_GEOMETRY_0014.md` identifies the saved product
   core's fixed binary slice as a translated weak triangle on
   G+P{0,1}+Q{0,1}. It gives explicit two-branch forcing chains excluding
   one parameterized diagonal pattern and its color complement. The
   reduction of arbitrary diagonal colors to that pattern remains open;
   the full product obstruction is not asserted as a theorem.

## Bounded discovery inputs

The Terra task examined twelve of at most one hundred allowed saved small
supports and stopped at A={0,1,2,3,4,6,7,8}. Its tiny line-pattern enumeration
reported diagonal/row/column minima 16,12,13 against 44 corners; the one
full-triangle solver call reported UNSAT. These are discovery outputs in
`fibers/ROUTING_DUAL_DISCOVERY_0014.py/json`. They are not an all-source
result or a paper proof of the literal source's obstruction.

A separate single-source maximal-clique packing LP on that same source
returned floating objective 44.0, with the displayed support consisting of
the corner triangles. This supplied no strict contradiction. Its scope is
only the reported LP in `fibers/GLOBAL_CLIQUE_DISCOVERY_0014.py/json`;
it does not close the ordered-block or shared-pair-potential route.

`fibers/EIGHT_MARK_ROUTING_0014.md` records the bounded auxiliary reduction
on this source. Using the reported line-minimum inputs, a proper coloring
has only three units of excess over those minima. Its first fiber reduces
to eleven normalized signed-Golomb words, and nested completion blocks
give explicit shared-product inversion constraints. No contradiction or
four-unit lower bound was obtained; the finite case remains a development
gap, not a completed proof.

The assigned Sol routing and product tasks and the Terra retrieval and
bounded discovery tasks are terminal. There is no live solver or child
research run to resume at this checkpoint. No usage reset was requested.

## Limited source comparison

A bounded Terra retrieval first consulted the existing local literature
map, then examined three query families. The nearest primary sources were
the Sidon--Ramsey vertex-partition paper (arXiv:2111.08076 / published DOI
10.1007/s40590-024-00676-7) and rainbow Sidon solutions (arXiv:2010.04127).
Neither supplies the two-edge-color, directed-outer-edge theorem needed
here. They are not premises of the new inequality. This is a scoped
comparison, not an exhaustive novelty conclusion.

## Exact next root implication

Find a source-dependent choice of prices, shared-pair potentials, and
explicit local lower derivations in the joint inequality such that

    binom(|A|,2)>11 span(A), span(A)<=91998
       implies joint lower cost > total corner weight.

A comparably sufficient source-size formula is also acceptable. Giving all
three directions of each corner the same residual price is a known trivial
choice. Unary-potential scans are now ruled out by the symmetry lemma and
should not be launched. Any proposed improvement must retain a legitimate
global budget and agreement of relative colors, rather than independently
choosing the best sign for each offset.

The small eight-mark example is only a bounded development case. An
explicit local obstruction there would not establish the uniform estimate
above. The product diagonal-classification gap is secondary to that main
source-size implication. The goal remains active and incomplete.
