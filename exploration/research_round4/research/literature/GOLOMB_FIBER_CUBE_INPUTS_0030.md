# Three-generator additive-cube avoidance: bounded source inputs

## Target convention

The requested condition excludes every positive cube

\[
 x+\{0,u\}+\{0,v\}+\{0,w\}\subset A\qquad(u,v,w>0),
\]

**including coincident generators**.  In the intended formulation this is
equivalent to requiring each nonzero difference fibre to be Golomb.  This is
stronger than the convention in much of the Hilbert-cube literature where a
``3-cube'' means eight *distinct* vertices (often called a proper or
non-degenerate Hilbert cube).  Results using that latter convention cannot
by themselves control cubes with, for example, two equal generators.

The three bounded leads below give terminology or comparison constructions;
none yields an energy bound for the repeated-generator fibre condition.

## 1. Hilbert cubes are the standard named object, but usual extremal results are for non-degenerate cubes

**C. Dietmann and C. Elsholtz, [*Hilbert cubes in progression-free sets and
in the set of squares II*](https://arxiv.org/abs/1207.1461).**  The paper uses
the additive Hilbert-cube form

\[
 a_0+\{0,a_1\}+\cdots+\{0,a_d\}.
\]

Its quantitative theorems bound the possible dimension of cubes contained
in special ambient sets (notably the squares, and progression-free ambient
sets).  Thus it is a primary source for the terminology and for the fact that
cube containment can be quantitatively rigid in a prescribed host set.

**Mismatch.**  It is not a density theorem for arbitrary subsets of
\([N]\) avoiding the displayed three-generator configuration.  More
importantly here, its Hilbert-cube arguments are about cubes of a stated
dimension/properness type; they do not state that every generator collision
is forbidden.  The repeated-generator/fibre-Golomb hypothesis must therefore
be supplied separately before importing any such result.

## 2. Sidon sets give a rigorous stronger comparison class, at square-root scale

**P. Erd\H{o}s and P. Tur\'an, [*On a problem of Sidon in additive number
theory, and on some related problems*](https://doi.org/10.1112/jlms/s1-16.4.212),
Journal of the London Mathematical Society 16 (1941), 212--215.**  This is
the classical source for the quantitative Sidon problem: a Sidon subset of
an interval of length \(N\) has size at most \(\sqrt N+O(N^{1/4})\), and the
paper gives the foundational near-square-root construction framework.

A Sidon set has every nonzero difference fibre of cardinality at most one,
so it is a sufficient (strictly stronger) instance of the requested
all-fibres-Golomb condition.  It supplies a named, quantitative baseline of
order \(N^{1/2}\).

**Mismatch.**  The target permits an entire Golomb difference fibre, rather
than insisting that a fibre have one ordered pair.  Consequently Sidon theory
does not bound this larger class and cannot improve the stated \(N^{5/9}\)
deletion construction; it only records one familiar subfamily.

## 3. Existing Hilbert-cube work is host-set incidence theory, not an extremal theorem for this fibre class

**C. Dietmann, C. Elsholtz and I. E. Shparlinski, [*On additive and
multiplicative Hilbert cubes*](https://arxiv.org/abs/1107.4541).**  This work
studies the intersection/containment of additive Hilbert cubes with structured
arithmetic sets and with multiplicative restrictions.  Its hypotheses start
from a given Hilbert cube and then constrain the ambient arithmetic set.

**Mismatch.**  The requested problem starts from an arbitrary finite
integer set and excludes cubes, including degenerate-generator cubes.  There
is no stated estimate there for the largest subset of \([N]\) satisfying the
all-fibres-Golomb condition, nor a conclusion controlling its additive
energy.  It is therefore a useful terminology/nearby-incidence lead, but not
a finite-range improvement for the root construction.

## Bounded-search conclusion

Across these focused primary leads, the only directly quantitative comparison
class is Sidon, at the weaker square-root scale.  The standard Hilbert-cube
literature must be read with its explicit distinct-vertex/non-degeneracy
convention before it can bear on the repeated-generator condition.  This is
a bounded source-search observation, not an absence or novelty claim.
