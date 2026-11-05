# Research checkpoint R4-RESEARCH-0022

Continuation of CHECKPOINT_0018.md, preserving work through 0022. The
user requests sustained invention, no separate audits, and no results
summary until all objectives are achieved. The substantive goal remains
active. No small-color objective has been achieved in this continuation.

Working bounds remain 21<=R3<=465 and R4<=21991300. The attributed general
growth bound remains complete in GENERAL_BOUND.md and was not replayed.
The completed eight-mark proof from 0015 was not revisited. No reset
credit was authorized. All bounded agents and research executions listed
below are terminal at this checkpoint.

## 1. Root's current sufficient implication

FINITE_SOURCE_SIZE_TARGET_0018.md proves that the open S21 statement

    V(A) properly two-colored, span(A)<=99994
       => binom(|A|,2)<=21 span(A)

would imply R3<=379 and R4<=99996. The latter uses the inherited finite
shift-count inequality a^2 t<=(L+t)[a+W(t-1)], with a=24999, L=99995,
W=6153, t=550. These are conditional numbers, not improved bounds.

The new root route is in DYADIC_SOURCE_SIZE_TARGET_0019.md. Put

    T_H=sum_{H<=h<2H} binom(r_A(h),2), M=binom(|A|,2).

The open single-band hypothesis

    D(7/5): T_H<=7M/5 for every dyadic H

already implies M<21 span(A), and hence both conditional thresholds.
It does not require constant total energy H10. For band lengths n_j and
masses X_j, retain X_j in

    X_j^2<=n_j[(14/5)M+X_j].

The geometric band sum satisfies (sum sqrt(n_j))^2<7L. Assuming M>=21L,
the root's explicit quadratic-root calculation gives

    M < L/2+sqrt((119/6)ML)
      <= M[1/42+sqrt(17/18)] < M.

The exact sharper band-length constant is 4+2sqrt(2). The simpler D1
implication is also derived in the note, but 7/5 is the current more
generous sufficient budget. D(7/5) is unproved. Do not spend another turn
recomputing this completed transfer; work on the source inequality.

## 2. Complete positive model results

WEIGHT_TWO_BAND_GEOMETRY_0021.md uses the inherited proper weight-two
construction. Its active atom exchanges form a triangle-free graph:
three ordered atom values cannot have all three distances in [H,2H).
The elementary edge bound gives D1 throughout this full-layer model.

For 2n atoms split into two widely separated groups, with every
cross-group atom difference in one dyadic band, the exact ratio is

    T_H/M = 2n(2n-3)/[(2n-1)(2n+1)] -> 1.

Thus a universal single-band coefficient below one is false. The
construction uses w_i=5^i in the first group and w_i=D+5^i in the second,
with S=sum5^i, a power of two H>8S, and D=3H/2. Difference dissociation
and the concentrated band are derived in the note. D(7/5) is not refuted.

GRAM_BAND_SOURCE_MODELS_0022.md extends the model theorem to arbitrary
subsets of pair sums of dissociated atoms, including doubled atoms via
graph loops. For loops it requires no integer atom relation with
coefficients of magnitude at most four; loop-free graphs need only two.

For the atom graph G, source size m=e(G), and adjacency row vectors v_i,
the repeated exchange multiplicity is <v_i,v_j> and

    sum_i ||v_i||^2=2m-number_of_loops<=2m.

The elementary weighted triangle-free inequality and vector Cauchy give
sum_{ij in F_H}<v_i,v_j>^2<=m^2. Retaining the integer first moment gives
sum_{ij in F_H}binom(<v_i,v_j>,2)<=binom(m,2). All nonexchange differences
are singletons. Thus D1 holds for every member of this graph-sum class,
even uncolorable members. This is not a general-source theorem.

Two limitations are explicit. These dissociated pair-sum sources contain
no four-term progression, whereas proper source triangles can. Also an
arbitrary triangle-free Gram representation with trace at most 2m is
equivalent to the squared-count bound itself: a one-dimensional star
realizes any list r_i with trace 2sqrt(sum r_i^2). An extension must build
vectors from actual source structure; free Gram variables add no new
strength. No original-method completion or novelty priority is asserted.

## 3. Source-compatible aggregate derivations and exact gaps

fibers/SOURCE_CLOUD_SUMMATION_0019.md replaces all-pairs cloud payment by
consecutive offsets in each translated-color list. Exact local identity:

    (k(p)-1)_+=W(p)+P(p)+H(p).

Every repeated link either propagates to a smaller-offset actual charge
event or terminates at an aligned bichromatic child pair. Within a band,
propagation goes to a strictly lower band. The remaining issue is
convergent fan-in: many parent anchors may reach one child event. Splitting
predecessors by sign gives only O(sqrt L) or O(sqrt H) multiplicity, not a
constant aggregate bound. No global cloud budget was proved.

SOURCE_FAN_AGGREGATE_0019.md and SOURCE_SINGLE_BAND_ROUTING_0020.md turn
two monochromatic fan pairs at offset gap delta into a bichromatic target
when a boundary translate exists. The safe combined multiplicity for
left and right closures is 2r_A(delta), not r_A(delta). This factor was
repaired during integration and propagated through both notes. No union
injection or cancellation is claimed. The band inequality has the form

    (A_H^2/M-A_H)/2
      <=2 B_H^{<H}+sum_{delta<H} r_delta(m-r_delta)^2.

The second term counts unsupported shifts and remains too large. The
proper four-mark family {0,H,2H-1,3H-1} shows that sum/difference scale
separation alone cannot supply the missing boundary marks.

SOURCE_BAND_BOUNDARY_COUPLING_0021.md retains actual completion colors in
an incidence graph with two output-to-endpoint edges per band corner.
Its actual color-cut size is C_H=T_H+A_H, and

    T_H<=2C_H/3+R_H/6.

Thus C_H<=21M/10-R_H/4, or uniformly C_H<=37M/20, would suffice for
D(7/5). These are open cut budgets, not proved improvements; rewriting
them as a Laplacian form does not prove them.

fibers/TWO_CLUSTER_SOURCE_BAND_0021.md handles the separated two-cluster
geometry, where all cross differences lie in one band and T_H=U(B,C).
With M_B=binom(b,2), M_C=binom(c,2), S_B,S_C the actual monochromatic
child energies, and R_* an exact cross-support Hall matching deficiency,

    U<=bc+(M_B+M_C)/2+S_B+S_C+R_*.

The coefficient-7/5 target follows from the unproved closure
S_B+S_C+R_*<=9(M_B+M_C)/10+2bc/5. Source compatibility is retained, but
Hall-deficient clouds can converge. Standalone Cartesian constants remain
false and cannot replace this missing step.

## 4. A pure-additive model and another transfer formulation

fibers/UNIQUE_OUTER_DIFFERENCE_MODEL_0022.md studies property P:

    x,x+d,x+h,x+d+h in A, d,h>0 => r_A(d+h)=1.

P itself gives a proper source coloring: repeated-difference cells have
one color and singleton-difference cells the other. For P, every repeated
difference's start fiber is Golomb. Rectangle incidences form a simple
graph on repeated differences (with loop bookkeeping when d=h), and
each edge sum is a singleton difference; equal-sum classes are matchings.
Its degree at d, counting a loop once, is binom(r_d,2). In a nested
equal-sum fiber every representation except the innermost has singleton
difference. Simultaneous realization of all these fibers is still missing
from an aggregate graph bound. Abstract graph data are not enough.

The explicit P-family A_n={+5^i,-5^i:1<=i<=n} has unbounded load at one
outer diameter but T=n(n-1), M=n(2n-1). It again rules out pointwise
output caps, without refuting a global or single-band bound.

fibers/ADDITIVE_INTERVAL_TRANSFER_0020.md retains the separate open
pure-additive target T<=(1+2Lambda)M. With k_s the number of distinct
unordered pairs summing to s and q_s the midpoint indicator, the exact
remaining inequality is

    sum_s k_s(k_s-2+q_s)<=2Lambda M.

Heavy sum fibers admit a residual-clique interpretation and each nested
segment is captured by an interval cut. The missing fractional cover
budget is average-one control of central filler pairs across different
sums. A plain dyadic cover leaves logarithmic overlap. No actual Lambda
transfer proof or counterfamily was obtained.

## 5. New discovery inputs, all terminal

fibers/SOURCE_DYADIC_PROFILE_0019.py/json: 100 stored proper-source records,
new band statistic only, no new solves or checking of old colorings. A
window13 candidate {0,1,2,5,6,7,8,11,12} has raw T_4/M=29/36, disproving
the proposed 3/5 coefficient within those inputs. No candidate exceeded
one. Root's new explicit family approaching one supersedes reliance on
this finite calibration for the asymptotic lower constraint.

fibers/SOURCE_SINGLE_BAND_DISCOVERY_0020.py/json: 120 new cluster/rank-layer
sources, at most 28 marks and span 400; 54 had T_H>M and each received
one bounded SAT call. All 54 returned raw UNSAT. There was no SAT or
UNKNOWN candidate. These bounded negatives do not prove D1 or D(7/5).
No solver remains live and no separate verification run was made.

## 6. Primary-source searches in this continuation

literature/SOURCE_ENERGY_INPUTS_0019.md records anti-Ramsey vertex Sidon,
rainbow edge-color, and vertex additive-configuration near-matches. None
provides the actual two-edge-color source theorem or coefficient 21.

literature/ALTERNATING_SOURCE_GRAPH_INPUTS_0021.md records the lonesum /
Ferrers / chain-graph characterization requiring every alternating 2x2
rectangle to be absent. Source properness controls only supported additive
parallelograms, so the full characterization cannot be imported.

literature/UNIQUE_OUTER_SOURCE_INPUTS_0022.md records Freiman-2 equivalence,
a unique-difference theorem for small symmetric finite-field sets, and
standard energy facts. None gives the needed graph-sum representation for
P or a general-source energy estimate. These were bounded new questions;
their negative retrieval outcome does not establish novelty.

## 7. Continuation

Root retains original method design, D(7/5)/S21, and the R4 integration.
The next useful step must prove a general-source band budget, derive a
source-controlled incidence structure with a real trace/capacity bound,
or materially change the sufficient source hypothesis. Do not replay
completed model proofs, band-to-size calculations, or operator reformulations.
Reuse the three completed agent handles with followup_task for concrete
independent auxiliary derivations; send_message alone will not activate
them. Continue substantive research and keep the goal active. Do not
present any conditional number as an achieved upper bound.
