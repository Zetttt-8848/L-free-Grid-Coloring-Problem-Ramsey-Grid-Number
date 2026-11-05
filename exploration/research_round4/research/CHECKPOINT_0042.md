# Research checkpoint R4-RESEARCH-0042

Continuation of0041. Both the preceding turn and this turn are progress.
Root developed rooted interval forests for the complete weak mixed-cell
system, an exact triple-convolution dictionary, and a new reflected-middle
hole rule. Auxiliary work gives finite-band propagation capacity, exact
ordered Q constraints, and a sharp two-point extension reduction with a
new six-mark binary obstruction. None yet proves the uniform source bound.

The objective file at attachments/1b639c86-e74d-43dc-b451-d0fd3ce53dfc/
goal-objective.md and the research handoff were read. The user requests
in-depth continuation and no results summary until all objectives are
achieved. Working bounds remain 21<=R3<=465 and R4<=21991300. The
attributed general-growth corollary remains complete. S21, H10, EP10,
dyadic D(7/5), the finite R3 caps, and an original superior method with
new small-color bounds remain open. Keep the goal active; there is no
external blocker and no basis for marking it complete or blocked.

No computation, SAT discovery/replay, numerical optimization, separate
audit, review, or formalization was performed in0042. All new examples
and formulas have direct derivations in the notes. No reset credit was
authorized or used. The user will undertake later verification.

All three auxiliary handles are now terminal. No solver or other
research process is live. Reuse the existing Sol derivation and Terra
retrieval handles through followup_task for new bounded work.

## 1. Root: outward implication forests with exact sibling lengths

MIXED_INTERVAL_FORESTS_0042.md starts from disjoint Golomb diagonal
classes B,C and the mixed variables (b,c), with interval
I=[min(b,c),max(b,c)] and weight w=|b-c|.

At fixed c, a supported query w in Delta B has a unique representing
B-pair p<q. If the corresponding positive corner has homogeneous
completion, it is a unit force of color B. Otherwise its completion
is another mixed variable, the B-parent. The parent moves only the
B endpoint strictly away from c. Unsupported queries and B units
are exactly the roots of this B-forest. C has the symmetric forest.

Every parent has zero children, one midpoint child, or two distinct
children. In the last case their B endpoints, or C endpoints in
the other family, are the unique unordered pair whose sum is the
sum of the parent's endpoints. Therefore

    two children: w1+w2=w_parent;
    one child:    2w_child=w_parent.

For an actual proper coloring, a B-colored mixed variable follows
its C-parent and a C-colored variable follows its B-parent. Every
successor has the opposite actual color and larger interval. The
result is a forest with at most two incoming children and total
incoming weight at most the parent's weight. Its sinks are exactly

    color B with w absent from Delta C,
    color C with w absent from Delta B.

For every ancestry antichain U, its total interval weight is at
most the total weight of these unsupported sinks. The theorem
does not make all reflection units an antichain. It also concerns
outward implications only: the full binary system has other logical
implications, including inward N implications and equal-weight Q links.

## 2. Root: exact one-ruler triple dictionary

GOLOMB_TRIPLE_FOREST_DICTIONARY_0042.md writes

    lambda_B(r)=#{(u,v,w) in B^3:u+v-w=r}.

For r outside B it is exactly the supported-query count
sum_(u in B)1_(|r-u| in Delta B), hence at most b. On B it equals
2b-1, and its total mass outside B is b(b-1)^2.

Let mu count internal reflections of distinct triples, nu external
reflections of distinct triples, and delta outputs 2a-c, a!=c.
Then lambda=2mu+2nu+delta. Their total off-B counts are respectively
binom(b,3), 2binom(b,3), and b(b-1). At a fixed output r, the B-forest
has 2mu unit roots, b-lambda unsupported roots, nu two-child
vertices, delta one-child vertices, and 2nu+delta edges.

The weighted supported-query mass Q_B(r) also satisfies

    sum_(r not in B) Q_B(r)
      =2(b-1) sum_(d in Delta B)d.

These are full integer-output identities. Outputs beyond the source
hull must be retained when localizing them. Selecting only C outputs
can discard much of each total, so no lower bound for the selected
reflection or query mass has been inferred.

## 3. Root: a new reflected-middle hole

REFLECTED_MIDDLE_HOLE_RULE_0042.md proves the following. Let
a<p<q belong to B and r=a+q-p belong to C. If r<p and 2r-p is in B,
then 2r-q is absent from the entire source. If p<r and 2r-p is in B,
then 2r-a is absent instead.

For the upper-middle case put x=2r-q and y=2r-p. Golombness already
excludes x from B, because the B-pairs (x,y) and (p,q) would have
equal differences. If x is in C, the one reflection event forces
z(r,a)=z(q,r)=B. The C-C cell z(r,x) is B. Two binary corners then
force z(y,x)=z(q,x)=C, giving the all-C corner

    (y,x), (q,x), (q,p).

The lower-middle case is its positive-direction-preserving reversal.
This uses one reflection plus an extra reflected middle mark; it is
different from0041's two-reflection common-output shadow theorem.

At most two triples trigger this rule at a fixed r: the unordered
B-pair {p,2r-p} is unique, and for each middle p the extreme pair
has unique sum r+p. If there are two holes, they lie on opposite
sides of r. Some generated holes can be outside [0,L]. Counting
only interior holes gives J_in<=min(n(L+1-n),2n), using ordered
output-hole pairs. These charges may coincide with old shadow
charges and may not simply be added to them.

## 4. Auxiliary: sharp two-point mixed extension geometry

fibers/TWO_POINT_WEAK_EXTENSION_0042.md takes C={r,s}. There are
only B-unit forces and at most one three-variable constraint, since
Delta C has one length. All binary clauses forbidding two B colors
form a matching G_B. The corrected complete inventory is:

* an edge if 2r-s belongs to B;
* an edge if 2s-r belongs to B;
* two edges for a distinct interior pair p<q in B with p+q=r+s,
  or one edge for its midpoint case.

Although this list superficially has four slots, Golombness gives
the sharp bound |G_B|<=3. Both exterior marks have sum r+s and
cannot coexist with an interior pair of that sum. The earlier
omission of the second interior edge was repaired during derivation;
retain both edges and the arithmetic reason for the final bound.

fibers/TWO_POINT_TRANSVERSAL_GEOMETRY_0042.md chooses one C-colored
endpoint of each matching edge. The remaining N constraints give
two forest graphs R,S on at most three Boolean choices; their
clauses are z_i or z_j for R and not-z_i or not-z_j for S. The
unit-free binary system always extends. An abstract crossed pair
of P4s would obstruct four choices, but four choices have no integer
realization here. With units the implication system remains exact,
and the note gives a complete one-vertex augmentation criterion for
the sole three-variable constraint.

The new uniform longer binary obstruction is

    C={0,d}, B={p,d-p,d+p,2d},
    0<p<d/2, p!=d/4,d/3.

These B sets are Golomb. The one reflection (p,d+p,2d) outputs d.
Its two B units force, through two different matching clauses,
z(d-p,0)=z(2d,0)=C, producing a C corner with fixed cell
(2d,d+p). Neither used matching edge has two directly forced unit
endpoints. The concrete choice d=7,p=2 gives B={2,5,9,14}.
Root's reflected-middle hole theorem generalizes this mechanism.

## 5. Auxiliary: ordered Q layers and finite-band propagation

fibers/ORDERED_MIXED_OFFSET_CONSTRAINTS_0042.md defines

    X_d={u in B:u+d in C}, Y_d={v in C:v+d in B}.

Every cross pair u,v gives a binary clause forbidding (C,C) when
u<v and forbidding (B,B) when v<u. A full assignment is valid
exactly when max Y_C<min X_C and max X_B<min Y_B. Equivalently
two real cuts specify the allowed left/right rays for each color
and orientation. The same cuts give an exact extension test after
arbitrary partial colors from units or N propagation.

Active actual Q implications are precisely opposite-color pairs,
with count sum_d(|X_B||Y_C|+|X_C||Y_B|). If sigma(v) is the
outward N sink and p(v) its path parity, an active Q link vw
gives the exact signed equation

    col(sigma(v)) xor col(sigma(w))
      =1 xor p(v) xor p(w).

Root's integration refinement is complete: N paths preserve mixed
orientation whereas Q edges reverse it. Thus contracted Q edges
cannot be loops; their sink graph is bipartite by orientation. The
earlier paragraph allowing loops has been replaced by this geometric
conclusion. fibers/Q_SINK_ORIENTATION_CAPACITY_0042.md gives, for
a sink s of interval weight W_s and fixed offset d,

    n_s(d)<=floor(W_s/d),
    binom(n_s(d),2)<=W_s-d.

The first bound is antichain mass. The second uses that all these
intervals lie inside the sink interval and their starts form a
Golomb subset of the appropriate diagonal class. Use their minimum
G(W_s,d) as the exact displayed upper capacity. Between opposite
sink basins, the number of Q clauses at d is n_s(d)n_t(d); active
clauses use just the opposite-color subproducts. Thus active
multiplicity is at most G(W_s,d)G(W_t,d), and its d^2-weight is
at most W_s W_t. No global useful bound on sink weights follows.

fibers/INTERVAL_FOREST_BAND_CAPACITY_0042.md gives the exact path
bound n<=K_H=floor(sqrt(4H-1)) for vertices with weights in [H,2H).
The two monotone endpoint subsequences are Golomb. Their positive
pair differences give floor(n^2/4)<=H-1. Partitioning the band's
vertices into K_H ancestry antichains gives total weight<=K_H R_H
and number<=K_H R_H/H, where R_H is the sink mass in components
meeting the band. This applies to all vertices, hence to units.
The missing estimate is a useful bound for R_H or for the unit
ranks; an arbitrary sink of long length has not been paid for.

fibers/REFLECTION_UNITS_ON_IMPLICATION_PATHS_0042.md constructs
proper weak sources

    B={0,10N,11N}, C={-1,3,N,N+2,N+3}, N>=8,

with two consecutive reflection units of weights N,N+3. Its full
coloring and direct corner inventory are supplied. Units need not
form an antichain and have no fixed multiplicative length gap.
It does not establish arbitrary unit-path multiplicity. Paired
reflection mates may leave a band in either direction.

## 6. Auxiliary: bare reflection-hole reuse and literature scope

fibers/REFLECTION_SHADOW_REUSE_0042.md gives a proper weak symbolic
family with arbitrarily many selected outputs sharing the same
bare lower hole 0. For N>=10, h_i=N^(2i), k_i=N^(2i+1), its
gadgets are {-h_i,k_i-h_i,k_i,2k_i,2k_i+h_i}. The middle k_i is
in C and the other four marks in B. Base-N separation excludes
unintended relations, and a full coloring is described. At k_i
there are two B reflections whose lower shadow is 0. Ordered
hole-output pairs remain distinct. This closes a constant bare-
hole reuse bound even for actual weak colorings; it does not
refute a finite-span source theorem.

literature/COOPERATIVE_FOREST_COLORING_INPUTS_0042.md records the
primary cooperative-coloring comparison: two paths can fail to
admit a cooperative two-coloring. The precise arithmetic interval
structure therefore cannot be discarded. It cites Aharoni et al.
arXiv:1806.06267 and Bradshaw's Cooperative Colorings of Forests.
No located theorem handles the complete ordered mixed system.

literature/FINITE_GOLOMB_REFLECTION_INPUTS_0042.md maps the existing
finite-span inputs without supplying a new ruler-span theorem.
literature/CUBE_DENSITY_INPUTS_0042.md likewise finds no saved
applicable lower cube/energy estimate that closes S21. Reuse0041's
K3<=2T, defect, window localization and finite fiber moment; do
not redo the general corners transfer or infer that the separate
Golomb-overlap counterexample family has been excluded.

## 7. Next root-owned bottleneck

The finite source inequality still needs a lower count of actual
forced structures combined with a controlled finite-span resource.
The forest antichain capacity retains shared colors but its sink
mass is unpaid. The new binary reflected-middle holes strengthen
the available local pattern system, but their selected incidence
count has no useful lower bound. The two-point theorem narrows a
whole slice of the weak system to three choices and finite unit
chains; it does not classify arbitrary many-color-class outputs.

Continue a concrete derivation on that interface or on actual-fiber
compatibility beyond arbitrary weak extension. Keep root ownership
of S21/H10 or a comparably sufficient formula and the R4 transfer.
Use completed notes as inputs, not subjects of new audits. All
earlier counterexample scopes and conditional-bound restrictions
remain in force. Save any new versioned experiment only if it
materially informs a fresh derivation; none is currently running.
