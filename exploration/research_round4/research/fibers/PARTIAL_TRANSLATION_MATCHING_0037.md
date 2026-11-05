# Partial translation matchings in a proper source

Let \(A\) be a finite integer source for which \(V(A)\) has a proper
two-coloring.  Fix \(d>0\), and take a maximum matching in the graph
joining marks at distance \(d\).  Write its lower endpoints as \(S\), so
\[
P=S\mathbin{\dot\cup}(S+d),\qquad
A=P\mathbin{\dot\cup}U .
\]
Put
\[
s=|S|,\qquad u=|U|,\qquad m=|A|=2s+u,\qquad
L=\operatorname{span}(A),\qquad M=\binom m2 .
\]
This note gives an energy estimate valid for every such partial matching,
and a simple quantitative matching threshold implying \(M\le21L\).

## 1. The matching classes and the whole step fiber

Color each \(x\in S\) by the actual color of the cell \((x+d,x)\).
This partitions
\[
S=B\mathbin{\dot\cup}C.
\]
Both \(B\) and \(C\) are Golomb sets, since they are subsets of the two
signed classes of
\[
F_d=A\cap(A-d).                                        \tag{1}
\]
This is the same actual-color input used by the perfect-matching theorem;
no colors are assigned artificially.

The whole fiber (1) gives extra information about some unmatched marks.
The step-\(d\) graph is a disjoint union of paths.  A maximum matching
leaves exactly one unmatched vertex in every odd component and none in
an even component.  We may choose the unmatched vertex to be an endpoint
of each odd path.

Let \(i\) be the number of isolated vertices of the step-\(d\) graph.
Thus \(i\le u\), and the other \(u-i\) unmatched vertices lie at endpoints
of nontrivial odd paths.  In each such path, the edge incident with the
unmatched endpoint is a nonmatching edge of \(F_d\).  Component by
component,
\[
|F_d|\ge s+(u-i).                                      \tag{2}
\]
Indeed, an even path on \(2a\) vertices has \(2a-1\ge a\) edges; a
nontrivial odd path on \(2a+1\) vertices has \(2a\ge a+1\) edges; and an
isolated vertex contributes neither a matching edge nor a fiber edge.

The two actual color classes of all of \(F_d\) are Golomb and lie in an
interval of span at most \(L-d\).  Therefore
\[
|F_d|\le
1+\sqrt{\,1+8(L-d)\,}
\le 1+\sqrt{\,8L-7\,}.                                 \tag{3}
\]
Combining (2)--(3) gives
\[
s+u-i\le1+\sqrt{8L-7}.                                 \tag{4}
\]
There is also a useful form independent of the selected matching.  Every
nonisolated path with \(k\) vertices satisfies \(k\le2(k-1)\), while an
isolated path contributes one vertex and no edge.  Hence
\[
m\le2|F_d|+i
\le2+2\sqrt{8L-7}+i.                                   \tag{5}
\]
Thus nonisolated unmatched marks are paid for by the whole signed fiber;
only isolated unmatched marks escape this count.

## 2. Energy with an arbitrary unmatched remainder

For a finite set \(X\), write
\[
r_X(t)=|\{(x,y)\in X^2:x-y=t\}|,\qquad
E(X)=\sum_t r_X(t)^2.
\]
The paired-source calculation applies verbatim to \(P\), because the
matching colors split \(S\) into the two Golomb sets \(B,C\), even though
\(P\ne A\).  A convenient uniform bound is
\[
E(P)\le G(s),                                           \tag{6}
\]
where
\[
G(0)=0,\qquad G(1)=6,
\]
and, for \(s\ge2\),
\[
G(s)=
\min\{\,88s^2-96s-64,\ (2s)^3-(2s)^2+2s\,\}.            \tag{7}
\]
The first expression is the two-Golomb paired bound.  The second is the
elementary bound \(E(X)\le |X|^3-|X|^2+|X|\), included only because it is
smaller for the first few values of \(s\).

For completeness, that elementary inequality follows from
\[
r_X(0)=|X|,\qquad r_X(t)\le|X|-1\quad(t\ne0),
\]
and
\[
\sum_{t>0}r_X(t)=\binom{|X|}{2}.
\]
It also gives
\[
E(U)\le H(u):=u^3-u^2+u,                               \tag{8}
\]
with \(H(0)=0\).  The maximum-matching property additionally gives
\(r_U(d)=0\), but one forbidden difference does not improve (8) by a
uniform amount without another distribution hypothesis.

Since \(A=P\mathbin{\dot\cup}U\), the Fourier \(L^4\) triangle inequality
now yields the complete partial-matching estimate
\[
\boxed{\quad
E(A)^{1/4}\le G(s)^{1/4}+H(u)^{1/4}.
\quad}                                                  \tag{9}
\]
Equivalently,
\[
T(A)\le
\frac{\bigl(G(s)^{1/4}+H(u)^{1/4}\bigr)^4-2m^2+m}{4},   \tag{10}
\]
using \(E(A)=2m^2-m+4T(A)\).

Combining (9) with ordinary difference Cauchy gives a direct source-size
inequality:
\[
\boxed{\quad
M^2\le
\frac L2\left[
\bigl(G(s)^{1/4}+H(u)^{1/4}\bigr)^4-m^2
\right].
\quad}                                                  \tag{11}
\]
Indeed,
\[
\sum_{t>0}r_A(t)^2=\frac{E(A)-m^2}{2}
\]
and \(\sum_{t>0}r_A(t)=M\).

Formula (9) is clean but loses too much in the interaction between \(P\)
and even a small \(U\): the fourth-root triangle inequality permits all
cross terms to align.  Thus it is not the best way to obtain a constant
fraction threshold.  The signed-Golomb cardinality count is stronger for
that purpose.

## 3. Exact and uniform thresholds for \(M\le21L\)

The two matching classes \(B,C\) separately satisfy
\[
\binom{|B|}{2},\binom{|C|}{2}\le L-d\le L-1.
\]
Consequently
\[
s\le1+\sqrt{8L-7}.                                     \tag{12}
\]
For the actual values \(s,u,L\), the exact elementary sufficient
condition is
\[
2s+u\le\frac{1+\sqrt{1+168L}}2,                        \tag{13}
\]
because the right side is the positive solution of
\(\binom m2=21L\).

A scale-free version follows.

**Partial-matching threshold.**  If
\[
u\le\frac{s}{5},                                       \tag{14}
\]
then
\[
M\le21L.                                               \tag{15}
\]

Thus it is sufficient that the maximum translation matching cover at
least \(10/11\) of the source marks.

To prove the assertion, put \(x=\sqrt{8L-7}\).  Since \(L\) is a positive
integer, \(x\ge1\).  Equations (12) and (14) give
\[
m=2s+u\le\frac{11}{5}(1+x).                            \tag{16}
\]
The desired comparison
\[
\binom{\frac{11}{5}(1+x)}2\le21L
=\frac{21}{8}(x^2+7)                                  \tag{17}
\]
is equivalent, after multiplying by \(200\), to
\[
41x^2-748x+3411
=41(x-9)\left(x-\frac{379}{41}\right)\ge0.             \tag{18}
\]
If \(L\le11\), then \(x\le9\), so both factors in (18) are nonpositive.
If \(L\ge12\), then
\[
x\ge\sqrt{89}>\frac{379}{41},
\]
so both are positive.  These are all integer spans, proving (17) and
hence (15).

The whole-fiber refinement gives a stronger variant in sources with few
isolated marks.  If
\[
i\le\frac{|F_d|}{5},                                   \tag{19}
\]
then (5) sharpens to
\[
m\le\frac{11}{5}|F_d|
\le\frac{11}{5}(1+\sqrt{8L-7}),
\]
and the same calculation proves \(M\le21L\).  Condition (19) places no
limit on unmatched endpoints of nontrivial odd components; their
nonmatching incident edges are already included in \(F_d\).

## 4. Precise remaining gap

The result reduces this partial-matching route to a covering statement.
It is enough to find one step \(d\) for which either
\[
|U|\le |S|/5
\]
or, more flexibly, the isolated step-\(d\) marks satisfy
\[
i\le |F_d|/5.
\]
Neither condition follows from maximality of the matching alone.  A
source may have many marks isolated at a chosen displacement \(d\), and
those marks supply no cell on the signed fiber whose two Golomb classes
drive (3).

The unmatched energy inequality (9) remains valid in that case, but its
generic \(L^4\) interaction term is too loose to recover the \(21L\)
constant from a positive density of uncontrolled isolated marks.
Progress beyond the thresholds above therefore requires either a
source-color argument attaching isolated marks to other signed fibers,
or a covering theorem selecting a displacement with sufficiently few
isolates.  No such global selection statement is asserted here.
