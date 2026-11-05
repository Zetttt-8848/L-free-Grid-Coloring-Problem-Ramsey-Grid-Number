# A joint input/output sparsity target for actual forcing corners

The raw squared-load target is false by
REFLECTED_GOLOMB_LOAD_SATURATION_0045.md. This note changes the object:
it retains both endpoints and outputs as vertices of one graph. It gives
an exact graph dictionary and a sufficient conditional source bound.
The global graph sparsity premise is open. The stronger constant-
degeneracy proposal below is refuted by the subsequently derived
ANCHORED_REFLECTED_PRODUCT_FORCING_0045.md; that note replaces it with
an actual source-mark cost for a complete forcing biclique.

## 1. The actual forcing graph

Let z be a proper two-coloring of V(A). A forcing corner has parallel
endpoint cells p,r of the same color and outer completion q of the
opposite color. Put two edges pq and rq into a graph Gamma on all
M=binom(|A|,2) physical source cells. No diagonal endpoint edge pr is
included. An edge lies in a row or column, and its two cells determine
the remaining corner cell uniquely. Thus edges from different corners
never coincide and Gamma is a simple graph. It is bipartite under z.

Write H_q for the number of forcing corners completed at q and
H=sum_q H_q. Then

    |E(Gamma)|=2H.                                  (1)

For p=(u+d,u), let b(p) be the number of cells of its own color on the
actual difference fiber F_d, including p. As a parallel endpoint p
belongs to exactly b(p)-1 forcing corners; as an outer completion it
belongs to exactly H_p forcing corners and receives two edges for each.
These incidences are distinct, since outputs have strictly greater
span than their parallel endpoints. Hence

    deg_Gamma(p)=b(p)-1+2H_p.                        (2)

Equation (2) keeps the two sources of high degree together. Controlling
H_p alone or b(p) alone would discard one side of the incidence pattern.

## 2. The source-energy transfer

Let b_d,c_d be the two actual fiber class sizes and s_d=b_d-c_d.
Counting same-color parallel pairs gives

    H=sum_d[binom(b_d,2)+binom(c_d,2)]
      =(2T-M+sum_d s_d^2)/4.                        (3)

Combining (1) and (3),

    2T=M+2|E(Gamma)|-sum_d s_d^2.                  (4)

Therefore a bound |E(Gamma)|<=aM would imply

    T<=(a+1/2)M,
    sum_d r_d^2=2T+M<=(2a+2)M.                    (5)

Positive-difference Cauchy then gives

    M<= (2a+2)span(A).                              (6)

In particular the open sparsity statement

    |E(Gamma)|<=9M                                 (G9)

would imply H(19/2), hence the sufficient S21 bound. It is enough to
prove (G9) for source spans at most99994. The complete existing S21
transfers then apply to both requested small-color thresholds. No new
unconditional Ramsey number is asserted here.

A stronger proposed local premise was that Gamma is
9-degenerate: every nonempty induced subgraph has a vertex of degree at
most9. Repeatedly remove such a vertex; charging an edge when its first
endpoint is removed gives |E(Gamma)|<=9M and proves (G9). This implication
is valid, but the stronger premise is false by the anchored reflected
product construction. It is not an open route to (G9).

An argument about one low-degree cell in Gamma is insufficient for this
deduction. After arbitrary physical cells are removed, the survivors
need not form V(B) for a source subset B. A degeneracy proof must apply
to every induced subgraph of the original forcing graph, retaining
whatever supporting third cells its edges use in the original source.

## 3. The new reflected family is sparse in this graph

For the reflected Golomb coloring of
REFLECTED_GOLOMB_LOAD_SATURATION_0045.md, each nontrivial difference has
two cells, both of color0. Its two endpoint cells each participate in
exactly one forcing corner and are never a loaded output. The matched
cross outputs Q_i have singleton difference fibers and have no outgoing
forcing incidence. Thus Gamma is a disjoint union of stars and isolated
vertices. It is1-degenerate despite its unbounded sum H_q^2/M.

This is a material change in hypotheses from the failed moment target:
high output degree is permitted and is attached to degree-one inputs.

## 4. The weight-two family has a complementary sparse side

Let w_1,...,w_n be positive 2-dissociated weights, and let A consist of
all pair sums w_i+w_j, i<j. Label a mark by its two-element index set.
Color a strict cell0 when its endpoint labels intersect and1 when they
are disjoint. This is the established proper weight-two construction;
the following argument derives its new forcing-graph property.

An intersecting endpoint pair has difference +/- (w_i-w_j). All its
representations vary only in their one common index, so there may be
arbitrarily many same-color parallel cells. A difference between
disjoint labels has a signed support of size4 and has only one
representation. These are exhaustive by 2-dissociation.

Every repeated-difference corner therefore has color0 on both parallel
endpoints. Their distinct common indices make the outer endpoint
labels disjoint, so the output has color1. Thus all edges of Gamma run
from intersecting-label input cells to disjoint-label output cells.

If the endpoint labels of q intersect, their multiset union contains
one index twice and two indices once. There is no different partition
of that multiset into two distinct two-element subsets, so q has no
nontrivial end-cap decomposition and H_q=0.

If the endpoint labels of q are disjoint, their union has four indices.
There are exactly three unordered partitions into two two-element
subsets. One is q's own pair. Each of the other two partitions gives
at most two end-cap offsets, and only if its two marks lie strictly
inside q's interval. Hence H_q<=4. This q also has a singleton
difference fiber, so (2) gives deg_Gamma(q)<=8.

Remove the disjoint-label vertices first. Each has degree at most8,
and the remaining intersecting-label vertices have no edges. Therefore
Gamma is8-degenerate throughout the weight-two family. Large parallel
fiber degree is permitted here and meets outputs of degree at most8.
No assertion that8 is the exact degeneracy in every instance is needed.

## 5. The unresolved geometric implication

The two constructions above calibrate opposite sides of (2): reflected Golomb
copies have unbounded output degree with degree-one inputs; weight-two
sources have unbounded input degree with bounded-degree outputs. Neither
contradicts (G9). The subsequent anchored reflected product does allow
an induced K_(p,q) with p,q arbitrarily large, but needs (p+1)(q+1)
source marks and has T/M<1.

The next required theorem must bound the global edges by charging those
dense incidence blocks to their underlying source-mark cost, including
reuse between blocks. Bipartiteness alone cannot do this. The existing
two-forcing-offset closures describe one high-output star and retain
common-sum reuse; the new source-cost lemma instead couples distinct
stars through shared physical input cells. No general edge bound is
proved in this note, and no low-degree assumption is being inserted as
a premise of an unconditional bound.
