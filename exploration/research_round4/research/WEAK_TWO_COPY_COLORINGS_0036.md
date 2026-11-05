# Arbitrary diagonal choices on two separated Golomb copies

Root construction, checkpoint 0036. This gives proper weak triangles
with quadratically many repeated absolute mixed-color differences. It
rules out a proposed linear loss budget for those differences, while
leaving the finite-span weak-source cap questions open.

Let P={0=p_1<...<p_q} be Golomb, of span D, and choose Q>2D.
Put

    S=P disjoint union (Q+P).

For each i choose an arbitrary bit e_i. Color the weak diagonal cell
at p_i by e_i and that at Q+p_i by 1-e_i. Thus each diagonal color
class has exactly q marks, independently of the choices of bits.

## 1. Complete cell rule

For i<j, assign the within-copy cells

    z(p_j,p_i)=1-e_j,
    z(Q+p_j,Q+p_i)=e_j.

Assign the cross-copy cells as follows:

    z(Q+p_i,p_i)=e_i;
    z(Q+p_j,p_i)=1-e_i  for i<j;
    z(Q+p_i,p_j)=e_i    for i<j.                       (1)

All cross-copy cells are strictly above the diagonal in the source
convention because Q>D. The rules cover every weak cell exactly once.

## 2. Complete corner classification and properness

First consider a corner whose parallel endpoints are diagonal cells.
These endpoints correspond to any two marks of S. If their assigned
diagonal colors agree, (1) and the within-copy rules give the opposite
color to their completion:

* Within P, equality e_i=e_j makes 1-e_j opposite.
* Within Q+P, equality 1-e_i=1-e_j makes e_j opposite.
* Matching cross-copy marks have opposite diagonal colors already.
* For i<j, the diagonals at p_i and Q+p_j agree only if
  e_i=1-e_j; their completion is 1-e_i.
* The diagonals at p_j and Q+p_i agree only if e_j=1-e_i;
  their completion is e_i.

Thus all corners of this first type are proper.

For the remaining corners, classify the positive difference fibers.
Golombness of P and Q>2D imply:

* Each internal difference h=p_j-p_i has precisely two starts,
  p_i and Q+p_i.
* The cross difference Q has all q starts p_i.
* Each cross difference Q+h or Q-h for i<j has one start.

There are no collisions between these categories: internal differences
are at most D, while Q-D>D, and the positive base differences are
distinct. Therefore every strict corner is one of the following two
for some i<j:

    {(p_j,p_i), (Q+p_j,p_i), (Q+p_j,Q+p_i)},
    {(Q+p_i,p_i), (Q+p_j,p_i), (Q+p_j,p_j)}.            (2)

In the first corner the parallel endpoint colors are 1-e_j and e_j,
so they differ. In the second, its first cell has color e_i and its
completion has color 1-e_i, so these differ. Every corner in (2) is
therefore proper. Together with the diagonal case this proves that
the entire weak source W(S) is properly colored.

The rule allows arbitrary choices of the q bits. It is not an
independent recoloring assertion for a larger source: it is a complete
coloring of this specific constructed source.

## 3. Loss of distinct absolute mixed differences

Let B,C be the two diagonal color classes, and let p count indices
with e_i=1. Let Delta_mix be the set of positive absolute differences
|b-c| with b in B and c in C. There are |B||C|=q^2 such pairs with
multiplicity. Their distinct values can be counted directly.

The q matching cross-copy pairs all have the mixed difference Q,
contributing one distinct value. For each base pair i<j:

* If e_i=e_j, the two mixed pairs are cross-copy pairs, of distinct
  lengths Q+(p_j-p_i) and Q-(p_j-p_i).
* If e_i differs from e_j, the two mixed pairs lie within the two
  copies, and both have length p_j-p_i.

There are p(q-p) base pairs of the second kind. Separation and
Golombness again ensure that the listed values from different base
pairs do not coincide. Hence

    |Delta_mix|=1+2[binom(q,2)-p(q-p)]+p(q-p)
               =q(q-1)+1-p(q-p),
    |B||C|-|Delta_mix|=q-1+p(q-p).                    (3)

Balanced choices of the bits make the last term quadratic in q.
For example, taking p=floor(q/2) gives p(q-p)=floor(q^2/4).
Consequently there is no absolute constant K such that

    |B||C|-|Delta_mix|<=K(|B|+|C|)

for every properly colored weak source and its diagonal color classes.
The full weak coloring above, rather than separate Golomb partitions,
is part of this counterexample.

Arbitrarily large instances need no existence assumption about optimal
rulers: P={2^i-1:0<=i<q} is Golomb, since the two-adic valuation of a
positive difference identifies its smaller exponent and then its
larger exponent. Q may be any integer exceeding twice its span.

## 4. Scope for the finite-cap route

The construction has separated copies and span Q+D. It does not
refute a sharp inequality that also retains the actual span or the
unused difference values. In particular it is not a counterexample
to a proposed finite cap at span 462 merely because (3) is large.

Its precise implication is that a proof based on making almost all
absolute mixed differences distinct, with only linearly many losses,
cannot hold uniformly even under the actual proper weak coloring.
A finite-span argument must account for the losses together with
their geometry or their unused-length budget. No general weak-span
formula or unconditional Ramsey improvement follows from this note.
