# Research checkpoint R4-RESEARCH-0045

Continuation of0044, including the work before and after context compaction.
The objective file and current handoff were retained as authoritative;
historical document workflows do not override the user's invention-first
instructions. The goal is active and incomplete, with results withheld.

Unconditional bounds remain 21<=R3<=465 and R4<=21991300. The general
polynomial-exponent literature corollary is complete and unchanged.
S21/H10/EP10, the dyadic D(7/5) target, F11(5), and F12(7) remain open.
No original method with an unconditional small-color improvement is yet
established. There is no external blocker and the goal must not be marked
complete or blocked merely because this checkpoint is being saved.

## 1. Root: two pair capacities and a sharp full-cube dimension boundary

CUBE_PAIR_CAPACITY_0045.md is a complete new elementary derivation. For
an injective Boolean d-cube and a Golomb subset B, let e_J count its pairs
whose endpoint labels differ exactly on J, j=|J|. Signed difference types
and pair-sum records give respectively

    e_J<=2^(j-1),       e_J<=2^(d-j).

These bounds require only distinct subset sums, not dissociation of all
differences. Numeric coincidences between symbolic types only strengthen
them. Summing their minimum over J gives

    binom(|B|,2)<=sum_j binom(d,j)min(2^(j-1),2^(d-j)).

At d=4 the right side is 4+12+8+1=25, so |B|<=7. Thus two Golomb
classes occupy at most14 of a Boolean four-cube's16 marks. Actual proper
weak sources satisfy this restriction because their diagonal classes are
Golomb. Applying it to the actual weak coloring

    w_d(v,u)=z(d+v,u) on W(F_d)

shows that a proper strict source contains no injective positive five-cube.
More precisely it occupies at most30 of a five-cube's32 marks: at most14
of its16 paired four-face starts can have both endpoints present.

The companion positive result is
fibers/FOUR_CUBE_NONLINEAR_CONSTRUCTION_0045.md. It gives fixed lower and
upper strict three-cube color tables L,U and a full8-by8 cross matrix X.
For w_(i+1)>2sum_(j<=i)w_j these tables are independent of the actual
weights. Two-dissociation classifies every corner by signed support;
the exact separated-copy compatibility theorem gives24 lower,24 upper,
76 cross and76 bridge corners. The displayed color-word inventory has
only the six nonmonochromatic words. This is a symbolic construction for
the whole separated-weight family, not an inference from SAT status.

Consequently the largest full cube dimension admitting a proper strict
coloring in the separated family is exactly4. This does not imply S21.
Generic cube avoidance remains quantitatively insufficient at the desired
source density, and the actual proper weak three-cube from0044 remains
an important positive example.

The precursor fibers/FULL_FOUR_CUBE_DISCOVERY_0045.py/json/md made one
materially changed query: all120 strict cells at weights1,3,9,27 were
independent variables, with200 actual corners and400 NAE clauses. It
returned a complete assignment. The old binary m=2 typed=true experiment
had only92 identified variables; its raw negative was not unrestricted
four-cube noncolorability. Do not revive that interpretation. The symbolic
construction supersedes the discovery status as the existence evidence.

## 2. Root: global forcing-load moment attack and its exact obstruction

Root pursued the actual shared-color identity

    H_q=|(Kz)_q|,
    sum H_q=(2T-M+sum_d s_d^2)/4.

A proposed bound sum H_q^2<=C M would give
T<=(2sqrt(C)+1/2)M by Cauchy; C<=361/16 would imply H10. This was a new
global-moment attempt, not the already refuted pointwise load cap.

REFLECTED_GOLOMB_LOAD_SATURATION_0045.md supplies a complete new
counterexample family to that stronger route. Let

    P={p_0<...<p_(r-1)}, p_0=0, P Golomb,
    D>4span(P), A=P disjoint union (D-P).

Color all within-copy cells0, and cross cell (D-p_j,p_i) by1 exactly
when i=j, otherwise0. Every internal difference p_j-p_i and every
nontrivial cross difference D-p_i-p_j has exactly two representations.
Both corner types have colors(0,1,0) and complete at
Q_i=(D-p_i,p_i). Thus the full load profile is

    H_(Q_i)=2(r-1-i), all other H=0,
    M=r(2r-1), T=r(r-1),
    sum H_q^2=2r(r-1)(2r-1)/3,
    (sum H_q^2)/M=2(r-1)/3,
    sum binom(H_q,2)=r(r-1)(4r-5)/6.

The normalized second moment is unbounded despite actual properness.
All loaded outputs have the same endpoint sum D, and the loads are
spread over nested cells rather than concentrated at the hull output.

There is an explicit instance inside the S21 span range. For odd prime p,
P_i=2p i+(i^2 mod p), 0<=i<p, is Golomb by the displayed index-difference
and modular argument. Taking p101 gives span(P)20201 and D80805:

    |A|202, M20301, T10100, sum H^2=1353400=(200/3)M.

Thus even the finite cap25M, and therefore361M/16, is false on the
required span range. This source has small T/M and is not an S21/H10
counterexample.

A dyadic version is also false: choose D a power of two above4span(P).
In the band[D/2,D), the forcing loads are r-1-i and their squared sum
divided by M is (r-1)/6, unbounded, although the actual band corner
count is only binom(r,2)<M/4. Do not substitute a squared-load cap for
the still-open dyadic energy budget.

The completed auxiliary
fibers/COMPLETION_LOAD_MOMENT_FAMILY_0045.md analyzes the OLD high-load
coloring as a different input. It has only H_Q=2r-2 nonzero, so its
normalized global moment tends to2. This did not refute the new moment
proposal; root's different nested coloring does. Keep these two profiles
distinct even when their underlying reflected source geometry agrees.

## 3. Auxiliary pair-of-forcing-offset geometry

fibers/PAIRED_FORCING_OFFSETS_0045.md derives all first consequences of
two forcing offsets0<d<e<v-u at q=(v,u). Write

    a=u+d, b=u+e, c=v-e, f=v-d, g=e-d.

The six source marks u,v,a,b,c,f are present, four physical cells have
color-z(q), and [a,b],[c,f] are equal-gap pairs. They coincide exactly
when d+e=v-u; they share b=c when2e=v-u and a=f when2d=v-u.

The two closure alternatives are

    u+g absent, or z(u+e,u+g)=z(q);
    v-g absent, or z(v-g,v-e)=z(q).

If both closure marks are present, the new length-d cells force an
opposite-color completion, except when they are the same cell at
2e=v-u+d. The complementary and AP4-type coincidences are explicit.

The map(q;d,e)->(u,u+d,u+e,v) is injective, giving
sum_q binom(H_q,2)<=binom(|A|,4). Noncomplementary pairs map to an
ordered repeated-difference resource with its exact reuse nu(Gamma)
retained. Root's nested construction shows why that reuse cannot simply
be replaced by an absolute constant. The quartic bound does not meet the
source target.

literature/COMPLETION_SECOND_MOMENT_INPUTS_0045.md maps the earlier
exact norm identity and the fan bounds with their bichromatic and
boundary-open terms. Those terms were not already bounded by a constant
multiple of M. It distinguishes arbitrary signs, uncolored incidence,
and actual proper forcing.

## 4. Auxiliary joint weak budget: a completed size and two remaining sizes

fibers/THREE_BY_THREE_JOINT_QUERY_0045.md completes

    |B|=|C|=3, actual proper weak W(B union C)
       implies N+Q<=15=M.

Its six-mark energy argument gives T<=16 unless the marks form an AP6,
where T20. Together with T=2rho+N+Q and the zero-shared-support identity,
any violation reduces to one of two progression diagonal patterns:

    B{0,1,4}, C{2,3,5}, (N,Q)=(12,4);
    B{0,2,5}, C{1,3,4}, (N,Q)=(10,6).

The note gives direct five/six-corner implication chains excluding both.
It is an ordinary derivation; the inherited audit-template headings
were removed without opening a separate checking project. Combined with
the completed min(b,c)<=2 result, all proper weak sources of at most6
marks satisfy the joint budget.

fibers/THREE_ANCHOR_JOINT_DEFECT_REDUCTION_0045.md extends the bounded
question to c3 and arbitrary b. The six anchor sums imply Q<=9, the six
orientation bins imply N_C<=6+rho<=9, and N_B<=3b. Therefore
N+Q<=3b+18, so b>=6 is automatic. Only b4,5 remain after prior results.
With R_B=3b-N_B, R_C=6+rho-N_C, R_Q=9-Q, the exact missing inequalities are

    b4: R_B+R_C+R_Q>=6+rho;
    b5: R_B+R_C+R_Q>=2+rho.

The example B{0,1,5,7}, C{2,3,6} has N_B10,N_C6,Q6,rho2 and total22>21,
while all its3+3 scalar totals are at most12. Two B-reflection units
force z(7,6)=z(7,2)=B, and the fixed z(3,2)=B gives a monochromatic
step-one corner. Thus averaging the scalar3+3 theorem alone is not enough;
the actual mixed-cell interactions still matter. No general joint theorem
or finite-span source conclusion was obtained.

## 5. Local R3: cross-scale sign types and the exact remaining gap

fibers/FROBENIUS_SIGN_STENCILS_0045.md retains all domains for
g_d=D_dF, D_d=1+X^d+Y^d on S9 over F3:

    g3=D1^2g1 on S6, g6=D2^2g2 on S3,
    g9=D3^2g3 only at0.

Top commutation gives

    g9(0)=g6(0)+g6(3ex)+g6(3ey)
           -g3(3ex)-g3(3ey)-g3(3ex+3ey).

The displayed nonzero-sign pattern satisfies both separate Frobenius
chains and their top coupling. It need not arise from a common F;
D2g1=D1g2 on S6 is the missing lower cross-scale constraint.

fibers/CROSS_SCALE_SIGN_TYPE_COUPLING_0045.md additionally uses
D2g3=D3g2 on every base in S4. Nonzero triads on its two sides have the
same ternary majority type. Subtracting overlapping packets cancels their
shared g3 value: equal g2 types would force the two exterior g3 pairs to
have the same number of plus signs. Horizontal, vertical and transverse
packets reach all three inner values of the top stencil. However the
paired g2 types may differ; no coincidence or inconsistent closed cycle
has been forced from D2g1=D1g2. Neither F11(5) nor a counterexample follows.

The complete divisor-weighted implications in0043 remain the R3 route;
do not recompute their already sufficient integer weights.

literature/BIHYPERGRAPH_CORNER_INPUTS_0045.md records one targeted
primary-source pass on Zhang-Dong-Zhang arXiv2310.06464. T11 is the actual
55-vertex165-edge linear corner hypergraph. The source's colorability
results do not give the five-rainbow defect theorem in a prescribed
three-coloring; its linear-uniform unrestricted-colorability question is
itself posed as open. No ordinary K_N graph substitution was made.

## 6. Main finite-span dependencies and next research choice

literature/HIGHER_FIBER_SPAN_MAP_0045.md retains the strongest currently
derived higher-fiber input

    sum_d r_d^4/[2(L-d)+1]<=M+12T,
    K3<=min(2T,T+5R), R=sum_d rho_d,

and the window inequality with the actual restricted-fiber variance

    8 sum_seeds(t-d-2h)_+ +sum_(u,d)s_(u,d)^2
       <=2K2^(t)+K1^(t).

Replacing those restricted variances by weighted whole-fiber variances
would be invalid. Neither R^(t) nor the retained variance has the needed
new global payment. Arbitrarily sharp isolated Golomb-overlap bounds
still cannot imply S21, by the earlier coherent-color counterexamples.

The root-owned unresolved implication is still a finite-span estimate
M(A)<=21span(A), or another comparably sufficient formula. The new cube
boundary is a structural input, not that formula. The new load family
means that another attempt at moment control must explicitly handle
many nested outputs at one pair-sum center; rerunning the false raw L2
proposal, globally or in one band, would repeat a closed route.

A possible changed question is an exact decomposition separating those
common-sum nested concentrations from interactions between distinct sum
centers. No estimate for that decomposition is asserted here. Root must
own that design and the R4 inference; auxiliary local weak cases and
sign stencils remain secondary support.

One fresh narrow web search on additive-energy edge-coloring terminology
returned primary color-energy/linear-pattern papers but no theorem was
selected or used as a new source premise. It does not support any absence
or novelty claim and should not become a repeated broad literature pass.

## 7. Root: forcing incidence graph and source cost of dense blocks

Root continued the main source attack after the moment obstruction,
changing the object to a graph that retains both inputs and outputs.
FORCING_INCIDENCE_DEGENERACY_TARGET_0045.md defines Gamma on the actual
M source cells: each equal-endpoint forcing corner supplies its two
row/column edges from its outer completion to its parallel endpoints.
Unique corner completion makes Gamma simple; it is bipartite under the
actual coloring. It includes no diagonal endpoint edge. Exactly

    |E(Gamma)|=2H,
    deg_Gamma(p)=b(p)-1+2H_p,
    2T=M+2|E(Gamma)|-sum_d s_d^2.

Here b(p) is the size of p's own color class in its actual difference
fiber. Thus the still-open global budget G9, |E(Gamma)|<=9M, would imply
H(19/2), M<=20span(A), and hence the existing S21 transfers. Root has
not proved G9 or treated it as a premise of a Ramsey theorem.

The two high-degree calibration families behave differently in Gamma.
Root's reflected-Golomb load-saturation graph is a star forest. For the
proper weight-two layer, an intersecting-label cell has H=0; a disjoint-
label cell has a singleton difference fiber and H<=4, since the four
indices have only two alternative pair partitions. Removing all disjoint
cells first proves8-degeneracy for that family. These class facts are
fully derived; they are not a universal graph theorem.

The next stronger proposal, universal9-degeneracy, was then refuted by
root's new ANCHORED_REFLECTED_PRODUCT_FORCING_0045.md. Take4-dissociated
positive a_1,...,a_p,b_1,...,b_q, each successive weight greater than4
times the sum of its predecessors; a_0=0. The source consists of

    row0: P={a_0,...,a_p};
    row j>0: {b_j-a_i:0<=i<=p}.

Color within-row cells0; between two positive rows use1 exactly when
column indices differ; between row0 and a positive row use1 exactly
when the two indices agree. The exhaustive four difference types prove
that every actual corner is(0,1,0). Its source size and energy are

    m=(p+1)(q+1),
    T=2binom(p+1,2)binom(q+1,2), T/M<1.

The p cells(a_i,0), i>0, and q cells(b_j,0) induce K_(p,q) in Gamma,
with their third cells(b_j,b_j-a_i). Thus Gamma has unbounded degeneracy
and arboricity, although the full source remains low-energy. Do not
restart constant induced-cell degeneracy as the main implication. The
graph-target note was updated to state this correction prominently.

The same note derives a new properness-specific source cost, now the
most concrete next input. In ANY proper strict source, suppose a complete
one-column forcing biclique has input cells(a_i,u) of color s and outer
cells(b_j,u) of the opposite color, with all u<a_i<b_j. Its forced third
cells are(b_j,c_ji), c_ji=u+b_j-a_i, all color s. Then ALL pq marks c_ji
are distinct. If c_ji=c_lk and b_j<b_l, set h=b_l-b_j=a_k-a_i. The cross
edge also supplies(b_l,c_ji+h), and

    (b_j,c_ji),(b_l,c_ji),(b_l,c_ji+h)

is a monochromatic positive step-h corner. This proves |A|>=pq with
no unproved reuse assumption. The anchored product's (p+1)(q+1) marks
show why its dense induced cell core has a substantial underlying source
cost. A global decomposition must pay for overlapping blocks, row blocks,
mixed orders and reuse; no such global payment has been derived yet.

One new bounded graph-invariant discovery on the saved four-cube model
is in fibers/FORCING_GRAPH_CORE_DISCOVERY_0045.py/json/md. It builds Gamma
from that saved coloring, without a new coloring solver or a properness
recheck. The model has120 vertices,75 active forcing corners and150
edges. Its maximum degree is12 and maximum core is3. This is one finite
graph observation, not a universal sparsity certificate; the anchored
product is the symbolic counterexample to universal degeneracy.

The most recent root-owned question is therefore the GLOBAL forcing-edge
budget using source-mark costs of interacting incidence blocks. This is
more specific than simply proposing a corrected second moment. It still
requires new mathematics before any small-color upper bound can change.

## 8. Execution and continuity

All three current auxiliary handles are terminal and reusable:
/root/shared_difference_paths (Sol high), /root/weak_joint_budget (Sol
high), and /root/bihypergraph_sources (Terra medium). No solver or root
shell process is live. The earlier unrestricted four-cube discovery is
terminal; do not wait on it or restart it. No usage reset was authorized
or performed. No separate proof audit or formalization was undertaken.

The full goal remains active. Preserve the complete conditional transfers,
the unchanged bound status and the user's instruction to withhold the
results report until all objectives have complete derivations.
