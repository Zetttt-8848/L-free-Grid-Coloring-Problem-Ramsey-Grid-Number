# Edge-colored source inputs: bounded literature search

## Question and scope

Let (A\subset\mathbb Z) be finite and ordered.  The source problem colors
the edges ({a,b}), (a<b), of (K_A) in two colors and forbids one color
on all three edges


    ab, ce, ae

whenever (a<b, c<e, a<c), and (b-a=e-c>0).  Equivalently, it is a
proper two-coloring of the strict source triangle (V(A)).  The desired
external input would be a span-sensitive theorem for this exact edge-color
condition, for example (|A|=O(\sqrt{L\log L})) or an explicit bound when
(L=\max A-\min A).

This note first reused `FRONTIER.md` and `CHECKPOINT_0015.md`.  Thus it does
not repeat the general corners theorem, its grid transfer, or the already
excluded vertex-Sidon route.  The bounded web search used the three query
families “edge coloring + (a+d=b+c),” “Ramsey Sidon + edge coloring,” and
“equal differences + edge coloring.”  The closest primary sources are below.
No source in this bounded search states the requested span estimate.

## 1. Locally additive edge colorings: edge-colored, but an extra axiom

**Adi Jarden and Ziv Shami, [*A Note on Edge Colorings and Trees*](https://arxiv.org/abs/2204.06874), 2022, Definitions 2.3--2.4 and Theorems 3.1, 7.7.**

For a linearly ordered set, the source defines an edge coloring
(C:[A]^2\to D) to be *additive* when a binary operation (s:D^2\to D)
satisfies


    C(a,c)=s(C(a,b),C(b,c))       for a<b<c,

and *locally additive* when


    C(b,c)=C(b,d) => C(a,c)=C(a,d)       for a<b<c<d.

Their Theorem 3.1 transfers suitable Ramsey relations for additive colorings
to locally additive ones.  Their Theorem 7.7 gives an infinite-cardinal
homogeneity statement: if (kappa) is regular and (mu^+<kappa), then
every locally additive (C:[kappa]^2\tomu) has a homogeneous subset of
size (kappa).

**Translation and mismatch.** This is genuinely an ordered complete-graph
edge-coloring theorem.  But the source triangle only forbids the same color
on (ab,ce,ae) for an equal-gap completion.  It does not impose the displayed
local-additivity implication for every ordered quadruple, nor does the paper
derive local additivity from this weaker condition.  The cited results are
infinite-cardinal partition relations, with no finite interval/span estimate.
They therefore supply neither (|A|=O(\sqrt{L\log L})) nor a direct finite
input for S11.

## 2. Grid Ramsey edge colorings: a different four-edge rectangle pattern

**David Conlon, Jacob Fox, Choongbum Lee, and Benny Sudakov,
[*On the Grid Ramsey Problem and Related Questions*](https://arxiv.org/abs/1405.6587), IMRN 2015, Theorems 1.2--1.3.**

The paper studies (r)-edge-colorings of the Cartesian-product grid graph
(Gamma_{m,n}): vertices are ([m]\times[n]), and graph edges join pairs in
a common row or column.  Its basic forbidden configuration is an
*alternating rectangle*: both pairs of opposite graph edges receive the same
color.  If (G(r)) is the least (n) forcing such a rectangle in every
(r)-coloring of (Gamma_{n,n}), the paper records Shelah's upper bound


    G(r) <= r^{binom(r+1,2)}+1,

and proves the lower bound


    G(r) > 2^{c (log r)^(5/2)/sqrt(log log r)}

for an absolute (c>0).

**Translation and mismatch.** This is also an edge-color Ramsey problem and
the paper represents it through multiple colorings of complete graphs.  Its
rectangle uses four graph edges and pairs of opposite edges; it neither
requires the three colors in an L-completion to coincide nor singles out
equal integer gaps (b-a=e-c).  The host is a two-dimensional graph rather
than the ordered integer vertex set (A).  Its bounds vary with the number
of colors (r), not with (operatorname{span}(A)), and do not yield a
source-size inequality.

## 3. Sidon--Ramsey: additive equation, but colors are on vertices

**Manuel A. Espinosa-García, Amanda Montejano, Edgardo Roldán-Pensado, and
J. David Suárez, [*Sidon--Ramsey and (B_h)-Ramsey numbers*](https://arxiv.org/abs/2111.08076), Theorem 1; published 2024.**

For (mathrm{SR}(k)), the least (n) such that ([n]) cannot be partitioned
into (k) Sidon **vertex sets**, their theorem gives


    k^2-O(k^c) <= SR(k) <= k^2+Ck^(3/2)+O(k),

with (c\le1.525) and (C) close to (1.996).  A color class is Sidon
when (x+y=z+w) inside that one vertex class has only trivial solutions.

**Translation and mismatch.** The source equality (b-a=e-c) is the Sidon
equation (a+e=b+c), but the colors in this theorem label the four integers,
not the edges (ab,ce,ae).  A two-edge-coloring of (K_A) does not partition
(A) into two Sidon sets, and the three-edge constraint does not rule out all
monochromatic four-vertex Sidon solutions.  Thus the theorem cannot be
applied without a new reduction, and it is recorded only to prevent that
vertex/edge conflation.

## Conclusion

Within this bounded source search, no primary theorem was located for the
ordered same-step three-edge completion condition itself, nor for a bounded
decomposition of such an edge coloring into Sidon vertex sets.  The first
source is the nearest general ordered-edge-color framework, but it assumes
local additivity; the second is the nearest finite edge-Ramsey rectangle
framework, but its geometry is different; the third shares the additive
equation but has vertex colors.  Any use of these sources for a source-span
bound would require a new theorem establishing the missing implication.
