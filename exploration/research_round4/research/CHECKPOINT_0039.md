# Research checkpoint R4-RESEARCH-0039

Continuation of CHECKPOINT_0038.md. The preceding goal turn was progress:
it completed the two-distance point-deletion theorem and new actual-color
transport. This turn also makes progress through a complementary positive
fan injection, its supported-difference structure, a direct weak-source
formulation, and a sharp finite four-cycle construction. None closes the
uniform quantitative implication required by the goal.

The working bounds remain 21<=R3<=465 and R4<=21991300. The attributed
general growth theorem remains complete and unchanged. EP10, H10,
D(7/5), S21, C46/45(463), and the original superior small-color method
remain open in the required generality. The full goal is active and
incomplete; keep the user's results summary withheld.

All three auxiliary handles are terminal, confirmed in the live agent
listing after their last outputs. There is no live solver or shell
session. One new forced SAT instance was used for discovery and its
signs were converted into a direct finite construction. No old run was
replayed, no separate audit or review pass was assigned, and no reset
credit was used. There is no external blocker. One no-op patch attempt
failed to match its context; the subsequent real edits succeeded.

## 1. Root: the second anchored fan budget

POSITIVE_FAN_DIFFERENCE_BUDGET_0039.md uses the existing notation at min
A=0, B=A\{0}, f(x)=z(x,0). The two actual fan sets are

    P_x={y in B:x+y in B, z(x+y,y)=f(x)},
    Y_x={y in B:x+y in B, f(x+y)=f(x)}.

Let p_x=|P_x|, k_x=|Y_x|, p=sum p_x, s=sum k_x, and let o count
opposite-color J arcs. Thus s counts same-color arcs and e=s+o is the
endpoint deletion cost.

For y<z in P_x, put h=z-y and c=f(x). The two offset-x c-cells force
Q=(x+z,y) to -c; P_x membership also gives f(x+z)=-c. If x+h is a
source mark, the actual corner

    (x+h,0), (x+z,0), (x+z,y)

forces f(x+h)=c. If h also lies in B, this is the same-color arc
x->x+h. The arc fixes x,h and P_x is Golomb, so the map is globally
injective into same-color arcs. With the absent-label/absent-target
defect E_P counted once per pair,

    sum_x binom(p_x,2)<=s+E_P.

Together with the old same-color-fan injection,

    sum_x binom(k_x,2)<=o+E_Y,

and hence for n=|B|>0,

    p^2/(2n)-p/2<=s+E_P,
    s^2/(2n)-s/2<=o+E_Y.

The two charged arc sets are disjoint by actual anchored colors. No
defect has an asserted upper bound.

## 2. Root and auxiliary: supported differences have strong graph structure

Let

    D_x=Delta P_x intersect B intersect (B-x).

The positive-pair injection gives D_x subset Y_x, so D_x is Golomb.
fibers/POSITIVE_FAN_ITERATION_0039.md derives sum-freeness: if h,d,h+d
all lie in D_x, their Y_x cells first force a completion to f(x),
which makes the anchored corner at x+d monochromatic. Equivalently,
the supported-difference graph Gamma_x on P_x is triangle-free.

Root further proves that any pair u<v of vertices has at most two
common neighbors, at most one in (u,v) and at most one outside [u,v].
Two exterior common neighbors would repeat the difference v-u in D_x;
two interior ones would repeat its representation as a sum of two
elements of D_x. Golombness of P_x keeps the edge labels distinct.
Counting common neighbors and applying Cauchy gives, for t=|P_x|>0,

    |D_x|<=t[1+sqrt(8t-7)]/4.

Therefore the local defect is exactly binom(t,2)-|D_x| and has the
corresponding lower bound. This is a LOWER bound on holes, not an
upper bound usable to erase E_P. It says that a large positive fan
requires many missing supports. The same hole can recur for several x.

## 3. Root: direct weak-source formulation

WEAK_SOURCE_SUPPORTED_DIFFERENCES_0039.md removes the external x from
the notation and applies directly to any actually proper W(S). For
a in S, set c=z(a,a) and let P be the positive labels of later diagonal
marks having the same color c. Then

    D=Delta P intersect (S-a)

satisfies, for every h in D,

    z(a+h,a)=c,
    z(a+h,a+h)=-c.

Proof: a same-color diagonal pair at a+p,a+q forces (a+q,a+p)=-c,
the diagonal pair a,a+q forces (a+q,a)=-c, and their supported corner
forces (a+q-p,a)=c. The corner with diagonal a then forces its other
diagonal endpoint to -c. Three supported gaps h,d,h+d produce a
monochromatic first-column corner, so D is sum-free. It lies in one
opposite diagonal class and is Golomb as well.

The same triangle-free and common-neighbor-two graph conclusions hold.
At each a, missing supports number exactly binom(|P|,2)-|D|. Their
overlap across different a remains unbounded. This applies to each
translated weak triangle W(F_d) of an original proper source. It
retains first-column colors in addition to the two diagonal Golomb
classes and is a potential new finite-cap input; it proves no cap yet.

## 4. A direct construction attains two common neighbors

The new single-instance discovery files are

    fibers/POSITIVE_FAN_CYCLE_DISCOVERY_0039.py/json/md.

The instance uses

    x=10000,
    P={1000,1001,1011,1111}, D={1,10,100,111},
    S={0} union P union D,
    A=S union (x+S),

with forced actual P_x and Y_x signs. It includes all strict directed
source corners. The one raw call returned SAT and recorded 18 marks,
153 cells, 144 corners. No rerun or separate checking pass followed.

fibers/POSITIVE_FAN_CYCLE_CONSTRUCTION_0039.md converts the discovered
signs into three explicit layer tables specifying all cells. A complete
classification of equal-color signed offset groups gives opposite
colors at all their pair completions, which is the direct construction
proof. The raw SAT status is not a premise of that proof.

At x=10000 its actual P_x=P. The six positive differences of P are
1,10,11,100,110,111, and the supported ones are precisely D. Thus the
graph is the monotone four-cycle whose consecutive increasing gaps
are 1,10,100, with closing gap 111. Opposite vertices have two common
neighbors, one interior and one exterior. This rules out replacing the
proved graph restriction by a forest, by four-cycle-freeness, or by
common-neighbor at most one. Restricting the cross-layer cells to W(S)
gives the same limitation for the weak formulation.

## 5. Reversed outputs feed genuine positive-fan memberships

fibers/REVERSED_OUTPUT_CONCENTRATION_0039.md fixes reversed
decompositions x_i+y_i=w with 0<x_i<y_i and
f(x_i)=f(y_i)=-f(w)=c. Let p_i count which of the two actual row-w
cells at columns x_i,y_i have color c; these are genuine memberships
in P_{y_i} and P_{x_i}.

For two nested decompositions i<j, the same-color source supports
x_i+x_j and x_i+y_j force a four-cycle of forbidden simultaneous
-c pairs among their four retained cells. Hence p_i+p_j>=2. If both
smaller-input doubles 2x_i,2x_j have the same anchored color, the two
remaining pairs are forbidden too and p_i+p_j>=3.

Define G_w by those two cross-sum support conditions. Its zero-payment
indices form an independent set whose neighbors have payment two.
With independent-set expansion defect

    delta_w=max_(I independent)(|I|-|N(I)|)_+,

the derived inequality is sum_i p_i>=q_w-delta_w. A clique of
double-supported indices pays at least two per vertex except one.

Root integrates this without double-counting memberships: a membership
(x,y) determines its output x+y and reversed relation. With
Delta=sum delta_w and r_eq the equal-input reversed count,

    sum_w q_w<=p+Delta,
    R<=2p+2Delta+r_eq,
    o<=s+2p+2Delta+r_eq.

The support graph can be empty when cross-sums are absent or carry
another color. Thus Delta remains real and is not set to zero. This
feeds the reversed sums into the new nonlinear P budget but does not
yet provide a closed bound on e.

## 6. Transport reuse has shared exclusions

fibers/TRANSPORT_REUSE_STRUCTURE_0039.md fixes two incoming anchors
a<a'=a+delta for one earlier opposite arc. All their later reused
targets are parameterized by pairs r<s in

    K={r in A:r-x in A, r-x>a', z(r,a)=z(r,a')=c},

with b=r-x, h=s-r and actual target colors z(r,b)=-c,z(s,b)=c.
The common set K has no pair at distance delta. Each target step h
also excludes a+x+h and a'+x+h from K, by two explicit positive
corners using b>a'.

For distinct target steps H and union V of their anchor endpoints,

    V intersect (V+delta) is empty,
    V intersect (a+H)=V intersect (a'+H)=empty,
    |V|+2|H|-N_delta(H)<=L+1.

Missing shadow rows, absent back-shifts, and wrong-color shadows are
retained. This bounds distinct endpoints and steps, not target edges;
the reuse graph can still have a quadratic edge inventory under these
conditions alone. No injectivity of the earlier-arc charge is asserted.

## 7. Two-endpoint reversal classification and local dependency map

fibers/TWO_ENDPOINT_REVERSAL_LEDGER_0039.md classifies a four-mark
parallelogram by its anchored input signs relative to the outer cell
at both its minimum and reflected maximum. P means both inputs same
as the outer cell, R both opposite, M mixed. The only pairs of types
are RR, RP, PR, RM, MR, MM. RR is exactly the pure rectangle with all
four side cells opposite to its outer cell.

If X counts RR and Z counts RM/MR, the endpoint-type counts satisfy

    mathcal R-mathcal P=2X+Z.

Each pure rectangle injects into both a signed-fiber pair whose gap
exceeds its offset and one whose gap is smaller. The two inventories
have no linear total bound. Equal-input AP3 relations are handled
separately: PR,RP,RR remain possible and R-P=2X_AP. These are relation
type counts; do not confuse them with the two distinct arc incidences
of a four-mark Schur relation.

literature/TWO_SIDED_COLOR_IDENTITY_MAP_0039.md retrieves eight local
inputs, including the existing exact three-direction cut budget,
triangular signed-completion operator, support correlations, pair
potentials, and split-graph reconstruction. No new external theorem
was used and no new web search was needed. The map prevents presenting
those already-completed identities as a new uniform estimate.

## 8. Next root-owned implication

Root remains responsible for uniform EP10/S21 and the R4 breakthrough.
The central endpoint system now simultaneously includes the P and Y
fan injections, a structural theorem for supported P differences, and
positive-fan payment from reversed-output cross-support expansion.
The missing step is a joint budget for E_P,E_Y and Delta, or a span
argument that uses their repeated-support geometry rather than their
raw cardinalities.

The direct weak-source condition offers another concrete interface to
the finite R3 capacity target: impose it at every diagonal anchor of
W(F_d), with the actual first-column colors retained. Missing supports
cannot be summed without controlling overlap. Do not retry the now
closed common-neighbor-one/forest strengthening; the literal four-cycle
construction settles that. General defect bounds, cross-target
multiplicity, and finite source caps remain substantive open work.

Reuse the finished auxiliary handles through followup_task for new
bounded derivation questions. Keep the completed class theorems and
the general growth transfer as inputs, preserve the unchanged Ramsey
status, and continue without a results summary or completion claim.
