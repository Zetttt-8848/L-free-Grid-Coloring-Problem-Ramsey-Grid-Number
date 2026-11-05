# Research checkpoint R4-RESEARCH-0041

Continuation of0040. The preceding turn was progress through the new
two-Golomb energy theorem and its class consequences. This turn is also
progress: root strengthened reflection charges to actual missing marks,
derived the complete mixed-cell constraint system and its exact inventory,
and summed the weak-fiber energy theorem into a cube balance. Auxiliary
derivations clarify double-copy compatibility and shifted-ruler run energy.

The full objective remains active and incomplete. Working bounds remain
21<=R3<=465 and R4<=21991300. The attributed general-growth corollary is
complete and unchanged. S21, EP10, H10, dyadic D(7/5), the finite R3
capacities, and the original method with new small-color bounds are open.
Withhold a results summary until every objective is achieved. There is no
external blocker and no reason to mark the goal blocked or complete.

All three auxiliary handles are terminal. No SAT, numerical experiment,
old solver replay, separate audit, review, or formalization was performed
in this turn. No reset credit was authorized or used. The user will
undertake later verification; the files below contain the derivations.

## 1. Root: nested tails eliminate the occupied charge bins

NESTED_REFLECTION_HOLE_BUDGET_0041.md is the central new input. Let
W(S), S=B disjoint union C subset[0,L], be actually properly two-colored,
with these Golomb diagonal classes. For r outside B let

    R_B(r)={(a,p,q):a<p<q in B, r=a+q-p},
    mu_B(r)=|R_B(r)|,
    A_B(r)={left extremes a}, Q_B(r)={right extremes q}.

Both endpoint sets have size mu_B(r), by Golomb difference uniqueness.
For r in C, reflection forcing gives z(r,a)=B and z(q,r)=B.

For two left anchors a<a' at r, write delta=a'-a and h=r-a'. The
later witness p',q'>a' also lies above a. Thus h is automatically a
difference of the same-color tail above a. If t=r-delta=a+h belonged
to S, its supported-difference rule would force z(t,a)=B. But the
actual corner (t,a),(r,a),(r,a') forces it C. Therefore t is a hole.
The opposite order gives upper holes. Precisely,

    r-Delta A_B(r) and r+Delta Q_B(r) are disjoint from S,
    their union has exactly 2 binom(mu_B(r),2) positions.

Each shadow is itself an internal reflection output of B, and lies
inside its witness hull. The same statements hold with colors swapped.
The individual hole count can be localized to
I_r=[r-span A_B(r), r+span Q_B(r)], which is strictly inside the
hull of the used B extremes.

Put

    F=sum_(r in C) binom(mu_B(r),2)
       +sum_(r in B) binom(mu_C(r),2),
    H=L+1-|S|,
    H^+=sum_(hole t)|S intersect(t,L]|,
    H^-=sum_(hole t)|S intersect[0,t)|.

Each lower/upper charge injects into its ordered hole-output pair:
the output and difference recover the anchor pair by Golombness.
Consequently

    F<=min(H^+,H^-),  2F<=|S|H.

If K is the corresponding reflection first moment and n=|S|>0,
Cauchy gives K^2-nK<=n^2H. The earlier K<=floor(bc/2) remains an
independent input. Neither is a lower bound on K, so neither proves
capacity by itself.

The auxiliary WEAK_CROSS_ANCHOR_PACKING_0041.md initially retained
mixed-pair and shared-length bins and obtained F<=bc+2rho+H^+.
Those bins are actually empty by the root nesting argument. The old
inequality is true but superseded; a successor pointer was prepended.
Do not revert to treating an occupied opposite-color shadow as possible.

## 2. Root: the reflection-output graph and the exact weak system

For a fixed Golomb B, let Z_B be all its internal reflection outputs.
The root note defines directed edges from r to its lower and upper
shadows, without first choosing an opposite class. All targets stay
in Z_B and outdegree(r)=2 binom(mu_B(r),2). If B,C are the diagonal
classes of an actual proper weak source, no edge can go from a selected
vertex of C to another selected vertex of C; all its outgoing neighbors
are holes of the full source. A finite-span expansion or independent-
set estimate for this specific graph is a new possible capacity route.
No such graph theorem has been proved, and generic graph/Sidon
incidence theorems do not supply it automatically.

WEAK_MIXED_CELL_REDUCTION_0041.md gives the complete accompanying
constraint system. Given disjoint Golomb B,C, diagonal corners force
all B-B strict cells to color C and all C-C cells to color B. The bc
mixed cells are the only variables. At every positive offset, use
beta,gamma for the within-class length indicators and x,y for the
two orientations of mixed pairs. Put

    rho=|Delta B intersect Delta C|,
    N=sum(beta+gamma)(x+y), Q=sum xy,
    K=sum_C mu_B+sum_B mu_C.

Every positive-offset corner is exactly one of:

    rho automatically proper corners (opposite fixed endpoints),
    rho three-variable not-all-equal constraints,
    2K unit corner constraints,
    N+Q-2K binary corner constraints.

The sum is T(S)=2rho+N+Q. The same-orientation mixed-pair collision
bijection gives exactly one three-variable corner per shared length;
its rotated corner has the two opposite fixed within-class colors.
Each internal reflection supplies its two unit constraints, with an
explicit converse. Three-term progressions belong to the binary
inventory and require no separate distinct-four-mark assumption.

The system is necessary and sufficient for extending the prescribed
diagonal coloring. It is not asserted that the binary part always has
a solution, or that such a solution extends over the three-variable
constraints. In a proper source, the 2K unit occurrences concern
distinct mixed variables: a variable has at most one force of each
color, and opposite forces conflict. This recovers 2K<=bc while
identifying the actual cells.

The new shadow exclusion is specifically a three-variable shared-length
corner whose three variables would all be forced alike. It must not
be misdescribed as a mere binary constraint. This links tail nesting,
reflection units, and the rotated parallelogram clauses concretely.

## 3. Root: simultaneous weak-fiber cube balance

WEAK_FIBER_CUBE_BALANCE_0041.md defines K_j(A) as the number of positive
ordered j-generator cubes, permitting equal generators and coincident
subset sums. Then

    K1=M, K2=T(A), K3=sum_d T(F_d)<=2T(A).

For the full integer signed cube count C3, including zero generators,

    C3=m+6M+12T+8K3
      <=7E(A)-11m^2+5m.

The sign/zero coefficients have a direct bijection proof; no finite-
field encoding or external Gowers result is invoked.

For each actual signed fiber define U_d=binom(b_d,2)+binom(c_d,2).
The exact nonnegative defect is

    delta_d=(U_d-2rho_d)+(2b_dc_d-N_d)+(U_d-Q_d),
    2T(A)-K3(A)=sum_d delta_d.

The three terms are the unused resources in the completed H2 proof.
No disjointness across d is assumed. Window localization gives
K3^(t)<=2K2^(t), weighting each positive cube by
(t-sum of generators)_+. The finite support moment also gives

    sum_(d=1)^L r_d^4/[2(L-d)+1] <= M+12T(A).

These are complete universal profile conditions. They do not prove
S21. In particular the older all-overlaps-Golomb counterexample family
has K3=0 and satisfies the cube upper bound; do not claim that it has
been excluded by these formulas. Shared color defects or genuinely
finite-span information still need a further estimate.

## 4. Auxiliary: an actual fiber contains more than one weak triangle

fibers/WEAK_TO_DOUBLE_COPY_COMPATIBILITY_0041.md takes
A=S disjoint union(S+d), d>2span(S). Write L,U for its two strict-copy
colorings and X(v,u)=z(d+v,u) for the full cross matrix. The exact
necessary and sufficient conditions are:

* L,U are proper on V(S).
* Every equal-step matrix triple X(r,c),X(r+h,c),X(r+h,c+h), with
  r,r+h,c,c+h in S, is nonmonochromatic.
* Every bridge L(u+h,u),X(v+h,u),U(v+h,v), with
  u,u+h,v,v+h in S, is nonmonochromatic.

Separation makes internal and cross-copy difference ranges disjoint,
so this classification exhausts all corners. A given weak coloring
w prescribes X(v,u)=w(v,u) for u<=v, but not its lower triangle or
the two strict-copy colorings.

Every w extends when S is Golomb: take L constant0, U constant1,
use w above the cross diagonal and any colors below it. A cross
corner then has its identical row/column pair and is a diagonal
corner of w; bridges have opposite endpoint colors.

For general S, two actual bridge offsets can demand opposite colors
at the same lower cross cell. The note gives the coordinates and
positive steps. This is a conditional obstruction when the relevant
L,U endpoint colors are fixed, not an explicit nonextendable w.
Whether every weak w admits some choice of L,U remains open. Do not
assume an arbitrary proper weak source can be doubled into a strict
source, or silently identify the two premises.

## 5. Auxiliary: adjacent and distance-two run energy

The following results are secondary and have the prescribed class
S=P disjoint union(P+1), P Golomb, 1 not in Delta P, and a proper weak
coloring with these copies as diagonal classes where the valley law
is used. They do not concern arbitrary weak partitions.

fibers/ADJACENT_DIFFERENCE_RUN_BUDGET_0041.md writes n=|P|,
M=binom(n,2), Sigma={a+b:a<=b in P}, N=M+n, and r_D,r_Sigma for the
numbers of consecutive runs. Every adjacent represented-sum pair has
two adjacent-difference preimages, except one if its inner pair is
doubled. With Z1 the number of those exceptions,

    M-r_D=2(N-r_Sigma)-Z1,
    2r_Sigma-r_D=M+2n-Z1,
    0<=Z1<=2n-2.

The actual weak coloring gives one valley per sum run, so outer-cell
charges from distinct sum-run edges are distinct. Packing the runs
in their integer ranges gives

    L>=M+r_D,
    4L+4>=3M+4n+r_D-Z1,

where L=span(P). A difference run does not map to a sum run: if its
successive ruler intervals start at a_i, the corresponding successive
sum locations differ by a_(i+2)-a_i+1. No individual run cap follows.

fibers/SHIFTED_RULER_ENERGY_GEOMETRY_0041.md includes root's complete
convolution derivation

    T(S)=n(n-1)+4A1+A2+n epsilon2,

where Aj counts pairs d,d+j in Delta P and epsilon2 indicates
difference2. If Ej counts pairs t,t+j in Sigma and Zj their doubled
inner intervals, the exact distance-two correspondence gives

    A1=2E1-Z1,
    A2=2E2-Z2-n epsilon2.

The final shared-endpoint term has exactly n epsilon2 incidences and
cancels the corresponding energy term. Let s_Sigma count singleton
sum runs and g_Sigma one-hole gaps between runs. Then

    E2=N-2r_Sigma+s_Sigma+g_Sigma,
    E2=Z1+s_Sigma+g_Sigma-n-r_D,
    T(S)=6M-6r_D-2n+2(Z1+s_Sigma+g_Sigma)-Z2.

The unresolved terms are singleton runs and one-hole gaps, or a new
constraint linking distinct sum runs. Do not infer a coefficient
bound from the valley law alone. Root supplied Section0 so the first
energy formula is derived in the note, not left as an unproved input.

## 6. Retrieval and next root-owned implication

literature/FINITE_SPAN_FIBER_MOMENT_INPUTS_0041.md maps at most six
local inputs: the weak H2 theorem, shifted-window counting, supported
differences, reflection moments, and the inherited conditional R3
profile. It found no existing local sum of weak H2 cube moments;
the root derivation above supplies that missing input now.

literature/REFLECTION_SHADOW_GRAPH_INPUTS_0041.md makes a bounded new
primary-source comparison. Eberhard--Manners' Sidon development is a
partial linear space under the stated finite-group hypotheses, but
does not give the ordered triple-output shadow graph or the second-
Golomb-class avoidance theorem. The other retrieved Cayley-graph
embedding result also does not transfer. No applicable expansion
or independent-set theorem was found in that bounded search. This
is a scoped mismatch, not a claim of novelty or universal absence.

The next root attack should use the precise mixed-cell/forced-unit
system together with the shadow graph at finite span, or derive a
joint compatibility budget for actual fibers beyond one arbitrary
weak coloring. Keep the graph's holes and all shared-variable
constraints explicit. The cube balance is an input, not an already
successful finite-density estimate. The prior endpoint P/Y/Delta
system remains available with all its missing-support defects.

Earlier uniform/class bounds and all scope restrictions remain as
recorded in0040. Do not reopen the completed H2 proof, isolated N
deficit counterexample, sharp one-point reflection coefficient, or
four-cycle-free positive-fan proposal. All auxiliary handles are
terminal and may be activated for fresh bounded derivations using
followup_task. Continue the full goal without a results summary.
