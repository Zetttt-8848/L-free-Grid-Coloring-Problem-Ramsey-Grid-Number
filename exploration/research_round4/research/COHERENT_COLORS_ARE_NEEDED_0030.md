# Separate Golomb overlaps do not control even one source band

Root derivation, continuation 0030. This strengthens the relaxation
counterexample in GOLOMB_OVERLAPS_DO_NOT_BOUND_ENERGY_0029.md to a
balanced two-cluster setting. No proper source coloring is asserted.

## 1. Starting sets and a balanced cut

The preceding construction supplies finite sets S with every nonzero
overlap S intersect (S-d) Golomb and with T(S)/M(S) arbitrarily large.
We may take |S|=2r even: deleting at most one mark preserves all Golomb
overlap conditions and the lower bound |S|^2/span(S) tending to infinity;
positive-difference Cauchy then again makes T(S)/M(S) tend to infinity.
Translate S into [0,L], where L=span(S).

Choose a uniformly random balanced partition S=B disjoint-union C,
with |B|=|C|=r. Let P3(S) count three-term arithmetic progressions in S.
Among the T(S) unordered pairs of equal positive differences, exactly
P3(S) have a shared endpoint. The other T(S)-P3(S) use four distinct
marks. A shared-endpoint pair cannot put one entire edge into B and
the other entire edge into C. A four-distinct pair does so with probability

    p_r=2 (r)_2^2/(2r)_4
       =r(r-1)/[2(2r-1)(2r-3)] >=1/8,              (1)

for r>=2. The last inequality is equivalent to
4r(r-1)>=(2r-1)(2r-3), whose difference is 4r-3.

Writing U(B,C)=sum_{d>0}r_B(d)r_C(d), linearity of expectation gives

    E[U(B,C)]=p_r[T(S)-P3(S)].                       (2)

Each three-term progression is determined by its outer pair, so
P3(S)<=M(S). Consequently there exists a balanced partition with

    U(B,C)>=[T(S)-M(S)]/8.                          (3)

Both B and C inherit the all-overlaps-Golomb property. Moreover every
signed cross overlap D_delta=B intersect (C-delta) is Golomb. For
delta=0 it is empty; for delta>0 it is a subset of F_delta(S); for
delta<0 it is a subset of a translate of F_{-delta}(S).

Thus even simultaneous Golomb conditions on every same-side and every
cross overlap do not bound U(B,C) by a constant times |B||C|: equations
(2)-(3) and |B||C|=r^2 show that the ratio is unbounded.

## 2. Put every cross difference into a single dyadic band

Take a power of two H>=2L, and set Q=3H/2. For L>0 this is an integer.
Form the separated source

    A=B union (Q+C).

Every internal difference is at most L<H. Every cross difference
Q+c-b belongs to [Q-L,Q+L], contained in [H,2H]. In fact neither
outer endpoint can cause trouble: a difference equal to 2H would
require H=2L and c=L,b=0; replacing H by the next larger power of two
if necessary makes H>2L and puts all cross differences strictly
between H and 2H. We use this latter choice.

All equalities between two cross differences correspond exactly to
an aligned pair of one B difference and one C difference. Therefore

    T_H(A)=U(B,C).                                  (4)

The set has the same cardinality as S, hence M(A)=M(S). By (3)-(4),

    T_H(A)/M(A)>=[T(S)/M(S)-1]/8,                    (5)

which is arbitrarily large. Thus the separate overlap relaxation
does not imply any absolute single-band coefficient, not just 7/5.

## 3. The new source still has Golomb overlaps

Projection pi:A->S defined by pi(b)=b and pi(Q+c)=c is injective,
because B and C partition S. It preserves every equality of source
differences: the fine-coordinate discrepancy has magnitude at most
2L<Q, so a multiple of Q can cancel it only if both discrepancies
vanish.

For clarity, apply this to a putative positive additive cube in A.
Each of its three step directions has a fixed projected increment,
by the difference-preserving property. No projected increment is zero:
the two endpoints of such an edge would be distinct marks with the
same projection, contradicting injectivity. Thus its projection is an
additive cube in S with three nonzero, possibly signed generators.
Changing the base and reversing each negative generator expresses the
same projected point set with three positive generators. Repeated
generators and coinciding subset sums are allowed, as in the preceding
construction. This contradicts the cube-free property of S.

Hence A has no positive additive cube. By the overlap/cube implication
in the preceding note, every F_d(A) is Golomb.

## 4. Exact implication for the research route

We have constructed balanced, separated two-cluster sources with all
of the following properties at once:

* every nonzero overlap of the whole source is Golomb;
* every same-side and signed cross overlap is Golomb;
* every cross difference lies in one dyadic band;
* the energy in that one band divided by M is arbitrarily large.

This does not refute a theorem for an actually proper source. The
construction does not specify compatible colors for the strict triangles
on B and C and their common completion block. It shows that separate
weak-overlap energy estimates, however sharp, cannot supply the missing
general band bound on their own. In particular the two-layer aggregate
identities in fibers/TWO_LAYER_OVERLAP_ENERGY_0029.md need genuine
cross-fiber color compatibility or another stronger premise to close.

The examples are asymptotic and do not establish a counterexample in
the finite span range of S21. The complete and dense-partial product
theorems of checkpoint 0028 remain valid, with their actual structural
hypotheses. The working Ramsey bounds remain unchanged.
