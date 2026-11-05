# The unique-outer-difference model

## 1. Property \(P\) and rectangles

Let \(A\subset\mathbb Z\) be finite.  For \(d>0\), put

\[
X_d=\{x:x,x+d\in A\},\qquad r_d=|X_d|.
\]

Property \(P\) says that whenever

\[
x,\quad x+d,\quad x+h,\quad x+d+h\in A
\tag{1}
\]

with \(d,h>0\), then

\[
r_{d+h}=1.
\tag{2}
\]

Repeated representations of \(d\) are exactly pairs of starts \(x<y\) in \(X_d\).  Writing \(h=y-x\), they form (1), so their outer pair has difference \(d+h\), which is singleton by (2).

The case \(d=h\) is allowed: a three-term progression \(x,x+d,x+2d\) forces \(r_{2d}=1\).

## 2. Every repeated-difference start fiber is Golomb

**Lemma 1.**  If \(r_d\ge2\), then \(X_d\) is Golomb: no two distinct unordered pairs of elements of \(X_d\) have the same positive difference.

**Proof.**  Suppose two pairs of starts in \(X_d\) have the same positive difference \(h\).  These two \(h\)-intervals form a rectangle inside \(X_d\), possibly the three-point degenerate case in which the intervals share one endpoint.  Let its outer difference be \(s\).  Since \(X_d\subset A\), property \(P\) applied to this rectangle says \(r_s=1\).

But translating both outer endpoints by \(d\) gives a second representation of \(s\), because \(x\in X_d\) implies \(x+d\in A\).  The untranslated and translated endpoint pairs are distinct.  Thus \(r_s\ge2\), a contradiction.  \(\square\)

Consequently, for fixed \(d\), the map

\[
\{x,y\}\subset X_d\longmapsto h=|x-y|
\tag{3}
\]

is injective.  Every image \(h\) is itself a repeated difference: (1) contains the two \(h\)-intervals

\[
(x,x+h),\qquad (x+d,x+d+h).
\tag{4}
\]

Thus every collision at difference \(d\) creates a distinct repeated side difference \(h\) and a singleton outer difference \(d+h\).

## 3. The rectangle graph

Let \(\mathcal D\) be the set of repeated positive differences:

\[
\mathcal D=\{d:r_d\ge2\}.
\]

Build a graph \(\mathcal G_P\) on vertex set \(\mathcal D\).  A rectangle (1) gives an edge between its two side differences \(d,h\).  When \(d=h\), retain a loop.

Lemma 1 gives the following exact structure.

1. **Simplicity.**  For fixed \(d,h\), there is at most one rectangle with side differences \(d,h\).  Otherwise \(X_d\) would contain two pairs of starts of difference \(h\).
2. **Singleton edge sum.**  Every edge \(\{d,h\}\) has
   \[
   r_{d+h}=1.
   \tag{5}
   \]
3. **Matching color classes.**  Color an edge by \(s=d+h\).  Edges of one color form a matching, with a possible loop: once \(s\) and one endpoint \(d\) are fixed, the other endpoint is \(s-d\).
4. **Prescribed degree.**  At a vertex \(d\), its incident rectangle edges are in bijection with the pairs of starts in \(X_d\).  With a loop counted once,
   \[
   \deg_*(d)={r_d\choose2}.
   \tag{6}
   \]

Therefore

\[
T(A)=\sum_{d\in\mathcal D}{r_d\choose2}
=\sum_{d\in\mathcal D}\deg_*(d).
\tag{7}
\]

Equivalently, every nonloop rectangle contributes two units to \(T\), one at each side difference, while a progression loop contributes one.

This is a substantive strengthening of merely mapping collisions to outer pairs.  The collision partners \(h\) are distinct at each fixed \(d\), and repeated outer load is organized as a proper sum-coloring of a simple graph.

## 4. Equal-sum nesting

There is a dual description.  For a fixed integer \(s\), order all distinct-pair representations of \(s\) as

\[
x_1<\cdots<x_k<y_k<\cdots<y_1,\qquad x_i+y_i=s.
\tag{8}
\]

Any two representations form a rectangle.  Property \(P\) says that the difference \(y_i-x_i\) of the outer representation is singleton whenever \(i<k\).  Hence

\[
r_{y_i-x_i}=1\qquad(1\le i<k).
\tag{9}
\]

Only the innermost representation of a sum fiber may have repeated difference.

Equations (8)-(9) explain the unbounded-load obstruction: one singleton outer pair \((x_i,y_i)\) may contain every later representation \(j>i\), so property \(P\) does not bound the number of rectangles mapped to that singleton output.

## 5. An explicit \(P\)-family with unbounded output load

Let

\[
A_n=\{-5^i,5^i:0\le i<n\}.
\tag{10}
\]

Balanced base-\(5\) uniqueness for coefficients in \(\{-2,-1,0,1,2\}\) implies that two unordered pairs from \(A_n\) have the same sum only when they are the same pair, except that all \(n\) central pairs

\[
\{-5^i,5^i\}
\]

have sum \(0\).  Thus every nontrivial rectangle comes from two central pairs.

The same coefficient uniqueness excludes a three-term progression in \(A_n\): an equation \(x+z=2y\) would be a nontrivial balanced base-\(5\) relation (and the central alternative would require \(y=0\notin A_n\)).

For \(i<j\), the corresponding rectangle has outer pair

\[
(-5^j,5^j)
\]

of difference \(2\cdot5^j\).  This difference has no other representation in \(A_n\): an equality

\[
y-x=2\cdot5^j
\]

would give a second balanced base-\(5\) coefficient expansion unless \((x,y)=(-5^j,5^j)\).  Therefore \(A_n\) satisfies property \(P\).

The outer pair \((-5^j,5^j)\) supports \(j\) nested rectangles, so its output load is unbounded with \(j\).  Nevertheless the total energy remains small.  For each \(i<j\),

\[
5^j-5^i
\]

has exactly the two same-sign representations

\[
(-5^j,-5^i),\qquad(5^i,5^j),
\]

and

\[
5^j+5^i
\]

has exactly the two cross-sign representations

\[
(-5^j,5^i),\qquad(-5^i,5^j).
\]

All these difference values are distinct by the same balanced base-\(5\) uniqueness, while each \(2\cdot5^i\) is singleton.  Hence

\[
T(A_n)=2{n\choose2}=n(n-1),
\qquad
M(A_n)={2n\choose2}=n(2n-1),
\tag{11}
\]

so

\[
\frac{T(A_n)}{M(A_n)}
=\frac{n-1}{2n-1}<\frac12.
\tag{12}
\]

This family shows directly why a proof cannot cap the load of one singleton outer difference.  Its many nested rectangles are paid globally by many distinct repeated side differences.

## 6. The remaining graph inequality

Let \(R=|\mathcal D|\), and let \(K\) be the number of singleton positive differences.  Since every repeated difference has at least two representations and every singleton difference has one,

\[
M\ge 2R+K.
\tag{13}
\]

If \(t_d=\deg_*(d)\), equation (6) determines

\[
r_d=\frac{1+\sqrt{1+8t_d}}2
\tag{14}
\]

as an integer.  A proof of \(T\le2M\) from the rectangle graph would follow from

\[
\sum_{d\in\mathcal D}t_d
\le
2K+2\sum_{d\in\mathcal D}
\frac{1+\sqrt{1+8t_d}}2.
\tag{15}
\]

The graph properties proved above do not imply (15) abstractly.  A dense graph on repeated-difference labels chosen from one high interval can have only linearly many distinct edge sums; each sum class is automatically a matching, while the degree sum is quadratic.  Choosing a regular degree that is triangular can also meet the formal constraint (14).  Such an abstract graph need not be realizable by one integer set \(A\), but it shows exactly what is missing from the current structure theorem.

The unresolved implication is therefore a **rectangle-graph realizability inequality**: use the fact that all edges arise simultaneously from translated interval fibers \(X_d\subset A\), not merely from a simple graph whose sum colors are singleton labels.  Property \(P\) has already forced every \(X_d\) to be Golomb; a constant energy bound requires an additional global restriction on how these Golomb fibers can share their spawned differences.

The same obstruction remains in a single band.  Restricting (7) to \(H\le d<2H\) selects the degree contribution of band vertices, but their collision partners \(h\) and singleton colors \(d+h\) may lie outside the band and may be shared by many band vertices.  No injection proving \(T_H\le M\) follows from the local graph properties alone.

## 7. Scope

The completed result is the rectangle-graph structure (3)-(7), together with the equal-sum nesting rule (9).  The family (10) is a direct property-\(P\) construction demonstrating unbounded singleton-output load while satisfying \(T<M/2\).

No counterexample to \(T_H\le M\) or \(T\le2M\) is obtained, and neither inequality is claimed.  Their remaining content is the global realizability constraint described after (15).
