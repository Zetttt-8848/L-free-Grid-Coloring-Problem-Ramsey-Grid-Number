# A Gram-matrix band inequality and graph sum models

Root derivation, checkpoint 0022. This extends the single-band analysis
from full weight-two layers to arbitrary graph subsets of pair sums,
including repeated atoms. The resulting theorem is unconditional for
the stated representation class. It is not a theorem about every proper
two-color source and does not change a Ramsey bound.

## 1. A weighted triangle-free inequality

Let F be a triangle-free graph, and let t_i>=0 be weights on its vertices.
Then

    sum_{ij in E(F)} t_i t_j <= (sum_i t_i)^2/4.       (1)

Here is an elementary proof. Preserve the total weight. If two distinct
positive-weight vertices i,j are nonadjacent, let a_i and a_j be their
weighted neighborhood sums. Moving all the weight of whichever has the
smaller a-value onto the other does not decrease the left side: there is
no ij edge, so the a-values exclude both moved weights. The number of
positive-weight vertices decreases. Repeating leaves positive support
on a clique, which has size at most two because F is triangle-free. On
one vertex the objective is zero; on two vertices it is xy<=(x+y)^2/4.
This proves (1). It is the standard weighted triangle-free argument,
not a claim of novelty for that graph inequality.

Let v_i be real vectors, put g_ij=<v_i,v_j>, and D=sum_i ||v_i||^2.
Cauchy--Schwarz gives g_ij^2<=||v_i||^2 ||v_j||^2. Applying (1),

    sum_{ij in E(F)} g_ij^2 <= D^2/4.                 (2)

Suppose also that all g_ij on E(F) are nonnegative integers and D<=2m,
where m is a positive integer. Write S=sum_{ij in E(F)} g_ij and
Q=sum_{ij in E(F)} g_ij^2. We claim

    sum_{ij in E(F)} binom(g_ij,2) <= binom(m,2).      (3)

If S>=m, (2) gives Q-S<=m^2-m, proving (3). If S<m, the elementary
identity

    binom(S,2)-sum_e binom(g_e,2)=sum_{e<f} g_e g_f>=0

gives the result because S is a nonnegative integer below m. Thus both
cases are covered, including S=0 and m=1. Retaining the integer first
moment avoids losing the linear term in binom(m,2).

## 2. Arbitrary subsets of dissociated pair sums

Let w_1,...,w_r be distinct integer atoms with the difference-dissociation
condition

    sum_i c_i w_i=0, integers |c_i|<=4
    implies all c_i=0.                               (4)

The coefficient range four permits the doubled atoms introduced by
loops: comparing two differences of two-atom sums can use one atom four
times. For loop-free graphs, the coefficient range two already suffices.

Let G be any finite undirected graph on these atoms, with loops permitted
and with no multiple edges. Form the integer source

    A_G={w_i+w_j: ij in E(G)},                        (5)

where a loop ii contributes 2w_i. Condition (4) makes all these source
marks distinct, so m=|A_G|=|E(G)|, counting a loop once.

Let B be the symmetric zero-one adjacency matrix of G, with B_ii=1
exactly at a loop. Let v_i be row i of B. The sum of squared row norms is

    D=sum_i ||v_i||^2=2m-l<=2m,                      (6)

where l is the number of loops.

The only source differences that can have more than one representation
are atom exchanges w_j-w_i. For such an exchange, every representation
has the form

    w_i+w_k -> w_j+w_k,

with ik and jk both edges of G, permitting k=i or k=j when the required
loop exists. Its representation count is consequently

    r_A(w_j-w_i)=sum_k B_ik B_jk=<v_i,v_j>.           (7)

To justify that this is the full classification, subtract two source
marks and cancel their common atom multiset. If one atom remains on
each side, the signed coefficient vector is an exchange -e_i+e_j, and
the cancelled atom is exactly k. If two atoms remain on each side,
there is no cancelled atom and that signed coefficient vector fixes
both source marks uniquely, including any repeated atom. Distinct
coefficient vectors cannot give the same integer difference by (4).
Thus every nonexchange positive difference is a singleton and contributes
zero to the band energy.

Fix H>0 and let F_H be the graph on the atoms with

    ij in E(F_H) iff H<=|w_i-w_j|<2H.

F_H is triangle-free by the ordered-distance argument in
WEIGHT_TWO_BAND_GEOMETRY_0021.md. Equations (7) and the singleton
classification give exactly

    T_H(A_G)=sum_{ij in E(F_H)} binom(<v_i,v_j>,2).

Now (3) and (6) prove the model theorem

    T_H(A_G)<=binom(|A_G|,2)                         (8)

for every H>0. This includes arbitrary sparse graph subsets and loops;
it does not require a coloring of A_G. In particular it remains true for
members of the representation class whose source triangles are not
properly two-colorable. A general proper source must not be assumed to
have representation (5).

## 3. An abstract sufficient representation for a general source

The same argument supplies a precise representation target. For a source
A of m marks and one band, suppose its active difference fibers of size
at least two
can be assigned injectively to edges of some triangle-free graph F, with
vectors v_i such that

    r_A(d)<=<v_i,v_j> for its assigned edge ij,
    all these inner products are nonnegative integers,
    sum_i ||v_i||^2<=2m.

Extend unused edge inner products only when they are also nonnegative
integers. Then monotonicity of binom(n,2) for integral n>=0 and (3) imply
T_H(A)<=M(A). An equivalent version simply takes F to consist of the
assigned edges, so no unused-edge assumption is needed.

The assignment and trace budget are substantive requirements. No such
representation has been constructed for arbitrary proper source colors.
The source cells themselves cannot automatically be treated as edges of
an atom graph: that would assume the missing structural conclusion.
The useful new result is the complete theorem (8) for graph sum models
and the explicit Gram budget needed to extend its mechanism. The open
general-source target remains D(7/5), with its previously derived
conditional small-color consequences.

## 4. Two limits on extending the representation

First, a source of the form (5) cannot contain a four-term arithmetic
progression. Such a progression would give four two-atom incidence
vectors p_0,p_1,p_2,p_3 with the same successive difference v, by (4).
Every coordinate of each p_j is in {0,1,2}. If a coordinate of the
nonzero integer vector v is nonzero, the same coordinate of
p_3-p_0=3v has magnitude at least three, impossible in that range.
The inherited properly two-colored five-mark interval does contain a
four-term progression. Thus literal dissociated graph-sum representation
cannot hold for every proper source, even allowing loops.

Second, permitting arbitrary auxiliary vectors without connecting them
to source incidence only rewrites the desired squared-count estimate.
For any list of positive integers r_1,...,r_k, put Q=sum_i r_i^2. A star
with one center and k leaves has a one-dimensional Gram representation

    v_center=Q^(1/4),  v_i=r_i/Q^(1/4).

Its edge inner products are exactly r_i and its total squared norm is
2sqrt(Q). Conversely (2) forces Q<=D^2/4 for any such triangle-free Gram
representation. Hence an unconstrained Gram representation with D<=2m
exists exactly when Q<=m^2. It is not an independently easier premise.
The content of section 2 is that actual atom incidences construct the
vectors and establish their trace bound before using the energy estimate.
Any extension must likewise supply source-derived structure; a freely
chosen Gram matrix does not overcome the current bottleneck.
