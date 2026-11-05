# Large forcing bicliques and their source-mark cost

This note completes a new construction for the forcing graph Gamma of
FORCING_INCIDENCE_DEGENERACY_TARGET_0045.md. It refutes constant cell-graph
degeneracy, while deriving an actual source-mark cost for the dense
bicliques. The global edge budget (G9) remains open.

## 1. An anchored reflected product

Fix integers p,q>=1. Choose positive integer weights

    a_1<...<a_p<b_1<...<b_q

so strongly separated that each weight exceeds four times the sum of all
previous weights. Put a_0=0, P={a_0,...,a_p}, and define

    c_(j,i)=b_j-a_i,  1<=j<=q, 0<=i<=p,
    A=P disjoint union {c_(j,i):1<=j<=q,0<=i<=p}.    (1)

The marks in each positive row j are a reflected copy of P; row0 is P
itself. These rows are separated and ordered by j. The total number of
source marks is m=(p+1)(q+1).

The separation gives absence of any nonzero coefficient relation with
coefficients in[-4,4]: inspect its largest nonzero coordinate. In
particular P is Golomb with unique unordered pair sums, and different
B-coordinate patterns in differences of marks in (1) cannot coincide.

Define a two-coloring of every actual strict source cell as follows:

* two marks in the same row: color0;
* marks c_(j,i),c_(l,k) in different positive rows: color1 exactly when
  i!=k, and color0 when i=k;
* marks a_i in row0 and c_(j,k) in row j>0: color1 exactly when i=k,
  and color0 when i!=k.                              (2)

The reversed comparison in the last rule is intentional and accounts for
the reflected geometry of the positive rows relative to the anchor row.

## 2. Exhaustive difference classification

There are four types of positive differences.

**P differences.** For i<k, h=a_k-a_i has one representation in P and
one in each positive row:

    a_i -> a_k,
    c_(j,k) -> c_(j,i),  1<=j<=q.

All q+1 endpoint cells have color0. Pairing the anchor representation
with a row representation completes at (c_(j,i),a_i), of color1.
Pairing row j with row l>j completes at (c_(l,i),c_(j,k)), also of color1
because i!=k. Hence every corner from this fiber is proper.

**Row differences.** For j<l, h=b_l-b_j has p+1 representations

    c_(j,i) -> c_(l,i),  0<=i<=p.

Their cells have color0. A pair with two different column indices has
an outer completion in rows j,l with those different indices, of color1.
Every such corner is proper.

**Different-row, different-column differences.** A difference
(b_l-b_j)+(a_i-a_k) with j<l and i!=k has just one representation, by
the B-coordinate pattern and Golomb difference uniqueness of P. It
creates no corner.

**Anchor-to-row differences.** A difference b_j-a_i-a_k has two
representations for i<k:

    a_i -> c_(j,k),
    a_k -> c_(j,i).

Both cells have color0, and they complete at (c_(j,i),a_i), of color1.
When i=k the representation is unique and creates no corner. Uniqueness
of unordered P pair sums makes this list exhaustive within the type.

The B-coordinate patterns distinguish these types, and the separation
ensures every indicated cross-row or anchor-to-row difference is
positive. Thus the classification exhausts every corner of V(A) and
proves that (2) is proper. Every corner has colors(0,1,0), so every
corner is a forcing corner.

As a useful scale check derived from the same classification, putting
r=p+1 gives

    T=binom(r,2)binom(q+1,2)
       +binom(q,2)binom(r,2)+q binom(r,2)
     =2 binom(r,2)binom(q+1,2).                    (3)

No numerical coloring solver is a premise of this family.

## 3. An arbitrarily large induced biclique in Gamma

Take the p anchor input cells and q row output cells

    I_i=(a_i,0), 1<=i<=p,       Q_j=(b_j,0), 1<=j<=q.

By (2), I_i has color0 and Q_j has color1. The actual corner

    (a_i,0), (b_j,0), (b_j,b_j-a_i)

has equal parallel endpoint colors0, because its third cell lies within
row j. Therefore Gamma contains every edge I_i Q_j. There are no
same-color edges among the I_i or among the Q_j, so their induced
subgraph is exactly K_(p,q).

Choosing p=q arbitrarily large shows that Gamma need not have bounded
degeneracy or bounded arboricity. In particular the stronger
9-degeneracy proposal in FORCING_INCIDENCE_DEGENERACY_TARGET_0045.md is
false. Formula (3) gives T/M<1, so this is not a counterexample to the
global source edge budget G9 or to H10/S21.

The distinction is essential: the small induced biclique omits most of
the physical cells forced by the complete source in (1). An argument
using source completeness must retain the cost of those marks and cells.

## 4. A source cost for every separated one-column forcing biclique

The following statement uses arbitrary actual proper sources, not the
special construction. Suppose Gamma contains all edges between

    I_i=(a_i,u), 1<=i<=p,
    Q_j=(b_j,u), 1<=j<=q,

where u<min_i a_i<=max_i a_i<min_j b_j, all I_i have one color s and
all Q_j the other color. The rows a_i are distinct and the rows b_j
are distinct. Since Q_j has greater span, every edge is a forcing
incidence whose third cell is

    R_(j,i)=(b_j,c_(j,i)),
    c_(j,i)=u+b_j-a_i in A,
    z(R_(j,i))=s.                                  (4)

**Source-cost lemma.** The pq marks c_(j,i) in (4) are all distinct.
Consequently |A|>=pq.

To prove it, suppose c_(j,i)=c_(l,k). Equal row indices would imply
equal column indices, and conversely, so a nontrivial coincidence has
both indices different. Relabel so b_j<b_l and put h=b_l-b_j>0.
The equality forces a_k-a_i=h. Write c for the common mark. The
complete biclique also supplies R_(l,i) with column

    u+b_l-a_i=c+h.

The three actual cells

    (b_j,c), (b_l,c), (b_l,c+h)

are all color s by (4), and form the original positive step-h corner.
Their strict validity follows from b_j-c=a_i-u>0. This contradicts
properness and proves the lemma.

The family (1) has m=(p+1)(q+1), so its source-mark cost is close to pq
when p and q are large. The lemma explains why its arbitrarily dense
cell subgraph is compatible with a small global T/M: each biclique
forces a multiplicative supply of distinct source marks.

## 5. Remaining global counting question

The exact identity 2T=M+2|E(Gamma)|-sum_d s_d^2 remains available, and
G9 would still suffice for the source target. A proof cannot proceed by
constant degeneracy of arbitrary induced cell subgraphs. The source-cost
lemma supplies a different kind of payment for one complete, separated,
one-column incidence block. It has no unproved per-mark constant-reuse
claim. Overlapping blocks, row-direction blocks, mixed input/output
orders and their shared source marks still need a global treatment.

Thus this note changes the local sparsity question to a cost in the
underlying source. It does not yet give a decomposition or an edge bound
for all forcing graphs, and does not change a Ramsey number.
