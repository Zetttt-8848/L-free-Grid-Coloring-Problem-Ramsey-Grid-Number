# R4-RESEARCH-0015: a complete local pair-polynomial obstruction

This checkpoint extends CHECKPOINT_0014.md. The controlling continuation
objective is the already-read attachment
`1b639c86-e74d-43dc-b451-d0fd3ce53dfc/goal-objective.md`. No Git repository
or .mathbox ledger is present. The root continues to own the all-source
derivation; the finite local theorem here does not complete the campaign.

## Bound status

The working bounds remain

    21<=R_3(L)<=465,       R_4(L)<=21991300.

S11 remains open: no proof yet shows M(A)<=11 span(A) for every properly
two-colored strict source triangle with span at most 91998. Its inherited
conditional R3<=201 and R4<=92000 implications stay conditional. The
requested superior method and numerical small-color improvements have
not been established.

The general growth bound in GENERAL_BOUND.md is unchanged and attributed
to the cited Jaber--Liu--Lovett--Ostuni--Sawhney theorem. Its orientation
and boundary transfer are reused, not repeated.

## Completed mathematical derivations

`EIGHT_MARK_PAIR_OBSTRUCTION_0014.md` now proves that the strict source
triangle on A={0,1,2,3,4,6,7,8} has no proper two-coloring. It also excludes
every source containing a translation and positive integer dilation of
that set. This local obstruction was already present in the inherited
catalog; the new result is its explicit algebraic derivation through
ordered completion duality.

The exact integer definitions and cancelling transfers are in
`PAIR_POLYNOMIAL_TABLE_0014.md`. Each line polynomial has a derived lower
bound, totaling -68. The completion-block bounds total 72. All terms
cancel by their defining transfers, giving 0>=4. The proof contains the
full summation and local block derivations. Four longer line inequalities
are supplied with full algebra in `fibers/PAIR_LINE_DERIVATIONS_0014.md`.
No optimization status is a mathematical premise.

The proof uses three specific types of sign-product identity: original
positive corners; equally spaced triples within a source difference
fiber; and reflected corners only when their six supporting source marks
are present. `ORDERED_SWITCH_INEQUALITY_0014.md` derives the last rule and
the more general quadratic three-pair inequality. It does not declare
arbitrary reflected corners forbidden or change the original orientation.

`ORDERED_COMPLETION_DUAL_0014.md` gives the general joint inequality and,
in Section 7, a direct convex-geometric alternative: consistent local pair
marginals exist, or cancelling shared-pair potentials strictly separate
the local state families. A nearest-point argument proves this alternative.
The sign-reversal argument proves that unary and, more generally, odd
potentials cannot improve a fixed even-potential local lower bound.

These results establish a reusable framework and one complete local
application. They do not establish its requested superiority on R3 and R4.

## Discovery provenance and closed local work

The earlier independent-line discovery reported 41 against 44 corners on
the eight-mark source. A single global maximal-clique packing LP returned
44.0. A subsequent single pair-marginal LP reported infeasible, and one
Phase-I discovery supplied potentials with displayed fifth denominators.
These outputs guided the algebra. The final proof fixes exact integer
coefficients and derives the inequalities explicitly; it does not infer
a theorem from those statuses.

Relevant discovery files are
`fibers/PAIR_MARGINAL_DISCOVERY_0014.py/json` and
`fibers/PAIR_POTENTIAL_CANDIDATE_0014.py/json`, together with the earlier
ROUTING_DUAL_DISCOVERY and GLOBAL_CLIQUE_DISCOVERY files. The table-writing
script only formats polynomial definitions and does not run a solver or
evaluate the local inequalities.

`fibers/EIGHT_MARK_ROUTING_0014.md` retains the earlier eleven-word partial
route. Its finite obstruction gap is superseded by the complete pair proof;
there is no need to finish those eleven cases. The auxiliary
`fibers/PAIR_BLOCK_DERIVATIONS_0014.md` contains a complete small case table
for three blocks; the root proof replaces that table with shorter clique
decompositions. Do not restart a separate review or checking phase.

The product auxiliary remains unchanged: its weak-triangle projection and
one diagonal-pattern obstruction are derived, but the arbitrary-diagonal
classification is still open. It is secondary to the root source-size goal.

All Sol auxiliary derivations and Terra retrieval/discovery tasks are
terminal. No solver or child handle needs waiting. No usage reset was used.

## Next root implication

Produce an explicit source-dependent weighted combination of the three
identity families and line-polynomial lower bounds that is uniform over
sources satisfying M(A)>11 span(A), span(A)<=91998, or obtain another
source-size formula sufficient for the small-color transfers.

The completed eight-mark proof supplies actual algebraic building blocks,
not a reason to repeat its searches. Uniform residual weights per corner
and unary-potential scans are known unproductive choices for this dual.
Any new reflected-corner term must retain its six-mark support condition.
Any claimed Ramsey improvement must include the all-source estimate and
its quantitative transfer; the local theorem alone supplies neither.
