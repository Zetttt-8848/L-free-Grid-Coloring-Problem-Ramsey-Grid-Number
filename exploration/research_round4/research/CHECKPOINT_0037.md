# Research checkpoint R4-RESEARCH-0037

Continuation of CHECKPOINT_0036.md. The full goal is active and incomplete.
The working bounds remain 21<=R3<=465 and R4<=21991300. The general
literature-based growth estimate is complete and unchanged. No original
method has yet demonstrated the required small-color improvements.
S21, D(7/5), H10, and the exact finite R3 cap remain open.

New work changes the research state through an endpoint-addition
reduction, an actual-color fan transport with a global injection into
opposite-color arcs, a quantitative partial-matching theorem, an ordered
weak-source collision budget, and two explicit square-source mechanism
limitations. No new solver computation was run. All three auxiliary
agents are terminal, as confirmed by the live agent listing. No reset
credit was used and no external blocker is present.

The user requests continued mathematical invention and full derivations,
not separate audits or repeated checking, and withholds a results summary
until all objectives are met. Those instructions remain active. Ordinary
integration repaired a few apparent notation/counting descriptions in the
new notes; no separate review campaign was conducted.

## 1. Root: endpoint addition graphs

ANCHORED_SUM_PEELING_0037.md normalizes min A=0, sets B=A\{0}, and defines
the directed mark graph J with arcs x->w when x,w,w-x belong to B and
x<w. Its exact corner-deletion identity is

    e(J)=T(A)-T(B).

The arc x->w corresponds to the positive equal-step corner
(x,0),(w,0),(w,w-x). Distinct summands in x+y=w give two arcs; equal
summands give one. Reflection across the anti-diagonal gives the maximum-
endpoint counterpart without changing the directed-corner convention.

The new open sufficient target EP10 says that every proper source with
m>=2 has at least one endpoint whose deletion loses at most 10(m-1)
corners. Successive endpoint deletions would telescope to T<=10M and
M<=21 span. Restriction to the S21 finite-span range suffices, since
deletion decreases span. EP10 is not proved and is not asserted equivalent
to H10. A minimal H10 counterexample would lose more than 10(m-1) corners
on deletion of every mark, hence at both endpoints.

The actual anchored colors are f(x)=z(x,0). For an arc x->x+y, let
g_x(y)=z(x+y,y). If f(x+y)=f(x), then g_x(y)=-f(x). With

    P_x={y:g_x(y)=f(x)}, Q_x={y:g_x(y)=-f(x)},

over its positive addition labels, P_x union {0} and Q_x are Golomb,
P_x is sum-free, and every output x+y from P_x has anchored color
-f(x). These are constraints from one actual source coloring, not
independent vertex and edge color choices.

## 2. New auxiliary forcing and root's global arc injection

fibers/ANCHORED_SUM_COLOR_COUPLING_0037.md proves the following rule.
Assume x,y,z,x+y,x+z are positive source marks with y<z and
f(x)=f(x+y)=f(x+z)=c. If a=x+z-y is a source mark, then f(a)=-c.
Two anchored corners force (x+y,y),(x+z,z) to -c; their ordinary
completion Q=(x+z,y) is c. The anchored corner from a to x+z would
force Q to -c if f(a)=c. The derivation uses four actual corners.

For Y_x={y:x+y is a positive source mark and f(x+y)=f(x)}, all pair
differences are distinct and

    (x+Delta Y_x) intersect B_(f(x)) is empty.

Thus the pairs in a fixed fan inject into opposite-color anchored
positions or source holes. The special anchored set x,2x,3x,4x cannot
have one color. A charge only to a position has cross-tail reuse.

Root's ANCHORED_FAN_ARC_BUDGET_0037.md retains the tail, resolving that
particular reuse by charging an arc. Write n=|B|, e_s/e_o for same/
opposite-color arcs of J, and W=sum_x binom(|Y_x|,2). For y<z in Y_x
put h=z-y,a=x+h. Partition the pairs into:

    D_step: h missing from B;
    D_target: h present, a missing;
    I: h,a both present.

Every pair in I maps to the opposite-color arc x->a. It is globally
injective: the arc fixes x,h and Golombness fixes the pair in Y_x.
With D=D_step+D_target,

    W=I+D, I<=e_o,
    e_s^2/(2n)-e_s/2 <=e_o+D,
    e_s^2/(2n)+e_s/2 <=e(J)+D.

The latter also holds with e_s replaced by the graph cut deficit tau(J).
The defects may not be dropped. They refer to actual missing labels and
targets, not arbitrary filler cells.

Let R count the arc incidences of Schur relations whose two inputs have
one anchored color and whose sum has the other. Let P count incidences
of wholly monochromatic Schur relations. Exact type counting gives

    e_o-e_s=R-P, P>=0,
    e(J)<=3n+sqrt(9n^2+8n(R+D))+R.

The local extra hypothesis R+D<=2n would imply e(J)<=10n, but it is
explicitly NOT a universal target. The inherited proper weight-two
source, rooted at w_1+w_2, has

    n=binom(q,2)-1,
    e_s=D=0,
    R=e(J)=4 binom(q-2,2).

For q>=8, R>2n, with difference (q-7)(q-2). All its additions are of
the reversed-sum type, while its actual arc count is less than 4n.
This does not refute EP10; it shows that a bound losing the tradeoff
between R and e_s is insufficient. The next root task is to control
opposite-color additions jointly with fan degrees and the two defects.

## 3. Quantitative partial translation matchings

fibers/PARTIAL_TRANSLATION_MATCHING_0037.md fixes a step-d maximum
matching with s edges and u unmatched marks, m=2s+u. The two actual
matching-start color classes are Golomb. The complete derivation proves

    u<=s/5  implies  M<=21L

for every integer span L. Thus coverage of at least 10/11 suffices.
It uses s<=1+sqrt(8L-7), m<=11(1+sqrt(8L-7))/5, and the exact factor
41(x-9)(x-379/41)>=0 for x=sqrt(8L-7). The narrow negative real
interval contains no such x for integer L.

A stronger version counts isolated vertices i in the step-d path graph.
The whole fiber satisfies m<=2|F_d|+i, so i<=|F_d|/5 also suffices,
regardless of unmatched endpoints in nontrivial odd components.

The same note gives

    E(A)^(1/4)<=G(s)^(1/4)+(u^3-u^2+u)^(1/4),

where G is the paired-source estimate capped by the elementary finite-
set cubic bound. The generic fourth-root interaction loses too much
to close the unmatched case. Neither a highly covering displacement
nor few isolates has been proved for arbitrary proper sources.

## 4. Ordered weak-source collision accounting

fibers/ORDERED_WEAK_TRANSITION_BUDGET_0037.md retains the actual proper
weak triangle W(B union C), with Golomb diagonal classes. Let rho be
the number of shared positive differences. For a mixed length k, let
X_k be starts of B-to-C pairs and Y_k starts of C-to-B pairs. The
complete rectangle bijection gives

    rho=sum_k [binom(|X_k|,2)+binom(|Y_k|,2)].

For each shared h, the unique internal B and C pairs begin a distance
k_h apart. The inherited six-mark ordered rule forces every fully
occupied interior h-edge to have the same lower-to-upper mixed color
orientation as the two mixed k_h edges. All other interior starts
miss at least one required source mark. Hence

    k_h-1=a_h+d_h,
    sum_k(k-1)[binom(|X_k|,2)+binom(|Y_k|,2)]
       =A+D <=P_shared+D <=bc+D.

This yields a parameterized tail-collision/span inequality, with
short k, especially k=1, and missing-pair defect D explicit. No useful
uniform charge of those costs to unused lengths has been found. The
previous twelve-mark counterexample to L>=(b-1)(c-1) remains decisive;
the unproved correction bc-b-c is not a premise.

## 5. Bounded square-source secondary route

fibers/SQUARE_ROOT_COLOR_MECHANISM_0037.md gives the explicit roots

    alpha=8R+3, beta=72R+7,
    gamma=64R+3, delta=96R+7,

with beta^2-alpha^2=delta^2-gamma^2. The three corner cells have root
differences congruent to 4 and root sums congruent to 10 modulo R;
their lower and upper roots are respectively 3 and 7 modulo R.
Choosing R divisible by any prescribed modulus and sufficient powers
of finitely many primes makes all corresponding exact factor
valuations and prescribed reduced-part residues agree. Thus no
uniform coloring based on any such finite arithmetic signature can
properly color all square sources. At R=1 all three cells have the
dyadic signature (2,1). This is not a noncolorability theorem for
the square source under arbitrary edge colors.

fibers/SQUARE_AFFINE_PATTERN_0037.md shows that a fixed root L under
scale q and translation (s,t) is a square corner only on the affine
compatibility line

    2s(b-d)+2t(c-a)+q[(b^2-a^2)-(d^2-c^2)]=0.

A finite pattern supplies finitely many such lines. Admissible
translations can avoid all of them. Requiring a nondegenerate
polynomial L identity under every free common translation likewise
fails by coefficient comparison. Thus an unrestricted Gallai copy
does not directly force a square corner. A constrained arithmetic
Ramsey theorem or another coloring mechanism would be required.

The earlier square energy growth theorem and the old m=200 raw SAT
record are unchanged. A square source has M/span<1/2, so this route
does not threaten finite S21. A uniform proper coloring for arbitrarily
large square sources would refute a constant global H-kappa, but no
such coloring has been obtained.

## 6. Narrow primary-source inputs and next work

literature/SQUARE_ROOT_COLOR_INPUTS_0037.md compares the vertex-colored
Boolean Pythagorean and x+y=z^2 theorems with the edge-colored source
problem. Their objects and relations do not transfer. It records three
query batches and two primary-source reads, not a novelty claim.

literature/STRICT_SOURCE_EXTREMAL_INPUTS_0037.md records a separate
three-batch search. The quoted monotone ordered-path Ramsey theorem
does not impose the required integer equal-gap condition, nor has it
the same ordered path type. No usable span-sensitive theorem was
located in that bounded search. The completed general-corners transfer
was not repeated.

The new root-owned implication is EP10 or another sufficient finite-
span estimate using the anchored fan arc injection. The unresolved
costs are opposite-color additions and the missing-label/target defect,
with the weight-two example retained before imposing a uniform R cap.
The earlier dyadic, completion-profile, and reflection constraints
remain available at their stated scopes. Reuse completed data and
derivations; do not restart solver calls as checks. Keep the full goal
active and withhold a results summary.
