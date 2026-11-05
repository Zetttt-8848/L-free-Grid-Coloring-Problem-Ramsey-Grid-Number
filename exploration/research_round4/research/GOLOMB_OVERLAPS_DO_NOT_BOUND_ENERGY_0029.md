# Golomb overlaps alone do not bound source energy

Root probabilistic construction, continuation 0029. This identifies a
limitation of extending the overlap-array mechanism using only separate
properties of the sets F_d. No proper two-coloring of the constructed
source is asserted. The finite-span target S21 remains open.

## 1. The stronger local relaxation

For a finite integer set A and d>0, let F_d=A intersect (A-d).
Consider the local property

    every F_d is itself Golomb.                      (G)

This is stronger than the existence of a two-Golomb partition of each
F_d, which is forced by a properly two-colored strict source triangle.
Nevertheless, (G) does not imply T(A)<=K M(A) for any absolute K,
nor M(A)<=K span(A) for any absolute K.

The reason is a sparse random construction with all three-generator
additive cubes deleted. The argument below includes cubes with repeated
generators and other coincidences; those degeneracies cannot be ignored.

## 2. Cubes and their possible numbers of distinct marks

A positive additive cube is the set

    P(x;u,v,w)={x+epsilon_1 u+epsilon_2 v+epsilon_3 w:
                         epsilon_i in {0,1}},

where u,v,w are positive integers and all marks lie in [1,N]. Repeated
generators are permitted. A cube can have four through eight distinct
marks. The following counts of parameter tuples suffice:

    eight distinct marks:       at most N^4 tuples;
    six or seven distinct:      at most 6N^3 tuples;
    four or five distinct:      at most 4N^2 tuples.  (1)

To derive the exceptional counts, cancel the common generators in two
equal subset sums. Positivity shows that every collision of subset sums
requires either equality of two generators or equality of one generator
with the sum of the other two. There are three choices of the first
kind and three of the second. Each such relation determines one
generator from the other two, leaving at most N^3 choices including x.

If the generators are pairwise distinct, their only possible collision
is that the largest equals the sum of the other two. Exactly one pair
of subset sums coincides, leaving seven marks. If exactly two generators
equal a, and the other is b, the sums are

    {0,a,2a} union {b,b+a,b+2a}.

They have six marks unless b=a or b=2a. The former is the all-equal
case and has four marks; the latter has five. Thus fewer than six marks
occurs only with three equal generators, or with two equal generators
and the third twice their value. There is one all-equal family and
three choices for the doubled generator, each with at most N^2 tuples.
This proves (1). Additional relations among a six-mark family do not
invalidate its upper count.

## 3. Random selection and deletion

Let q>=5 be an integer, choose

    N=q^9,    p=q^(-4),

and select each integer in [1,N] independently with probability p.
Let S be the selected set and let Z count parameterized positive cubes
all of whose distinct marks are selected. Counting parameter tuples
rather than distinct cubes only enlarges the deletion allowance.

By (1) and independence,

    E[|S|]=Np=q^5,
    E[Z]<=N^4 p^8+6N^3 p^6+4N^2 p^4
          =q^4+6q^3+4q^2.                           (2)

Consequently some selection satisfies

    |S|-Z>=q^5-q^4-6q^3-4q^2>=q^5/2.               (3)

For the last inequality, after division by q^2/2, the relevant
polynomial is

    q^3-2q^2-12q-8
      =(q-5)(q^2+3q+3)+7>0.

Starting with this selection, delete a mark from each remaining cube
until none remains. At most Z marks are deleted: every cube which can
be encountered was already present in S, and deletion creates no cube.
The resulting set A has

    |A|>=q^5/2,   span(A)<=q^9-1,                    (4)

and contains no positive additive cube, including a degenerate one.

## 4. Every nonzero overlap is Golomb

Suppose F_d were not Golomb. Two different pairs in F_d would have
the same positive difference u. Write their distinct starts as x<x+v,
where v>0. Then

    x, x+u, x+v, x+u+v belong to F_d.

By the definition of F_d, the same four marks translated by d also
belong to A. Thus A contains P(x;u,v,d), contrary to its construction.
This remains a contradiction when some generators or marks coincide.
Therefore A satisfies (G).

## 5. Unbounded normalized energy and source density

Put m=|A|, M=binom(m,2), and L=span(A). From (4),

    M/L >= M/q^9 >= q/8-1/(4q^4).                   (5)

The quadratic m(m-1)/2 is increasing for m>=1, so substituting the
real lower bound q^5/2 in (4) is legitimate. The right side of (5)
tends to infinity.

Also sum_{d>0}r_A(d)=M. Cauchy over the L possible positive differences
gives

    M+2T(A)=sum_d r_A(d)^2>=M^2/L,

and hence

    T(A)/M >= M/(2L)-1/2
             >=q/16-1/(8q^4)-1/2.                  (6)

This proves the claimed failure of every absolute energy or source-size
constant under (G). For example every q>=169 makes the right side of
(5) greater than 21: q-168>=1>2/q^4. It then follows from (6), or
directly from M>21L, that T(A)>10M.

The completed band-to-size implication also shows that (G) cannot imply
D(7/5) at every scale: otherwise it would imply M<21L for the same
examples. No new band-to-size calculation is needed for this conclusion.

These examples have spans allowed up to q^9-1, far beyond the finite
range in S21. Neither S21 in its stated range nor a proper-source
energy conjecture is refuted: no common proper coloring is supplied.

## 6. Consequence for the research route

The complete and dense-partial product theorems remain valid. They use
product structure to turn separate overlap restrictions into factor
energy bounds. This construction shows that one cannot simply remove
that structural hypothesis and infer a uniform bound from all overlap
partitions, even after strengthening each partition to a single Golomb
set.

A general argument must use more than the unlabeled collection of
overlap properties. The actual colors of shared completion cells, a
quantitative finite-span restriction, or another genuinely stronger
condition has to enter. In particular, proving better separate energy
caps for each F_d cannot by itself close a universal constant-energy
theorem: in this construction every F_d already has the minimum Golomb
energy 2|F_d|^2-|F_d|.
