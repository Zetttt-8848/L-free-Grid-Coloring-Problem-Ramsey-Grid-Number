# Four-cycles in the difference--sum resource graph

Let \(S=B\sqcup C\) be the diagonal partition of a proper weak two-color
triangle. The vertices considered here are the distinct unordered pairs
inside \(B\) and inside \(C\). A \(D\)-edge joins the unique two pair
resources of a shared positive difference, and an \(S\)-edge joins two
distinct pair resources of equal sum, one in each class. Each edge family
is a matching. Pair-sum matches involving a repeated pair \(\{x,x\}\) are
regarded as tagged terminals rather than vertices of this graph.

This note analyzes one alternating four-cycle. It gives a complete
coordinate closure for that cycle and identifies why the four cycle edges
alone do not contradict proper weak coloring. It does not assert that
longer alternating cycles exist or that all such cycles are allowed.

## 1. Normal form and parity

Suppose an alternating four-cycle uses the pair resources
\[
\begin{array}{c|cc}
 &\text{sum}&\text{positive difference}\\ \hline
P\subset B&s_1&d_1\\
Q\subset B&s_2&d_2\\
R\subset C&s_1&d_2\\
T\subset C&s_2&d_1.
\end{array}                                        \tag{1}
\]
Thus \(P\)--\(R\) and \(Q\)--\(T\) are \(S\)-edges, while
\(P\)--\(T\) and \(Q\)--\(R\) are \(D\)-edges. Necessarily
\[
s_1\ne s_2,\qquad d_1\ne d_2,\qquad d_1,d_2>0,     \tag{2}
\]
because pair sums and positive differences are unique inside each Golomb
class.

Writing a pair of sum \(s\) and difference \(d\) as
\[
\left\{\frac{s-d}{2},\frac{s+d}{2}\right\},         \tag{3}
\]
shows that
\[
s_1\equiv s_2\equiv d_1\equiv d_2\pmod 2.          \tag{4}
\]
Conversely, (4) is the complete integrality condition for the four pairs
in (1). Translate if desired, take \(s_2>s_1\), and put
\(\Delta=s_2-s_1\).

For signs \(\epsilon,\eta\in\{-1,1\}\), denote the endpoints by
\[
\begin{array}{ll}
P_\epsilon=(s_1+\epsilon d_1)/2,&
Q_\eta=(s_2+\eta d_2)/2,\\
R_\eta=(s_1+\eta d_2)/2,&
T_\epsilon=(s_2+\epsilon d_1)/2.
\end{array}                                        \tag{5}
\]
The equal-sum pairs in (1) have no shared endpoint across classes: two
pairs with the same sum and one common endpoint would be identical,
contrary to \(d_1\ne d_2\). The equal-difference pairs across the two
centers share an endpoint exactly when
\[
\Delta=2d_1\quad\hbox{or}\quad \Delta=2d_2.         \tag{6}
\]
Both cases are excluded by \(B\cap C=\varnothing\).

The two \(B\)-resources \(P,Q\) share an endpoint exactly when
\[
\Delta=d_1+d_2\quad\hbox{or}\quad
\Delta=|d_1-d_2|.                                  \tag{7}
\]
The same alternative then makes \(R,T\) share an endpoint. These are the
only repeated-endpoint degeneracies internal to the four-cycle data.

## 2. Rectangle-closure lemma

**Rectangle-closure lemma.** In addition to the two shared differences
\(d_1,d_2\) and the two matched sums \(s_1,s_2\), every cross pair
\(\{P_\epsilon,Q_\eta\}\) has
\[
\left|\;Q_\eta-P_\epsilon\;\right|
 =\frac{|\Delta+\eta d_2-\epsilon d_1|}{2}
 =\left|\;T_{-\epsilon}-R_{-\eta}\;\right|.         \tag{8}
\]
Hence it has a same-difference partner in \(C\), unless the displayed pair
degenerates to a repeated endpoint. It also has sum
\[
P_\epsilon+Q_\eta
 =\frac{s_1+s_2+\epsilon d_1+\eta d_2}{2}
 =R_\eta+T_\epsilon,                               \tag{9}
\]
so it has an equal-sum partner in \(C\), again with repeated pairs treated
as terminals.

Equations (8)--(9) prove the claim directly. In the nondegenerate case
\[
\Delta\notin\{d_1+d_2,|d_1-d_2|\},                 \tag{10}
\]
all four cross pairs in each class are distinct resources. Together with
the four original resources, they give twelve pair vertices. On the eight
cross-pair vertices, following an \(S\)-edge and then a \(D\)-edge sends
\[
(\epsilon,\eta)\longmapsto(-\epsilon,-\eta).        \tag{11}
\]
Therefore those eight vertices form two further alternating four-cycles.
The closure of the original cycle is consequently a disjoint union of
three alternating four-cycles on these twelve resources.

If (7) holds, one cross pair in each class is repeated. Formulae (8)--(9)
still give the exact closure, but the affected incidences terminate at
repeated-pair tags after the repeated resources are removed from the
distinct-pair graph. Thus repeated endpoints break part of the companion
cycle structure; they do not invalidate the original four-cycle.

The closure has a familiar additive interpretation: the four endpoint
sets in (1) are obtained by swapping the two radii \(d_1,d_2\) around the
two centers \(s_1/2,s_2/2\). In the nondegenerate case the two classes have
the same full six-element difference set and the same full six-element
set of distinct-pair sums.

## 3. The four core weak constraints do not conflict

There is no parity contradiction in the four original resource edges.
This can be seen without assigning the rest of the weak triangle.
Assume for clarity that
\[
\Delta>d_1+d_2,\qquad d_2>d_1.                    \tag{12}
\]
Then \(R\) is the outer interval in the sum match at \(s_1\), while \(Q\)
is the outer interval in the sum match at \(s_2\). The first \(S\)-edge
gives a binary clause saying that its two mixed endpoint cells are not both
color \(B\), and the second says that its two mixed endpoint cells are not
both color \(C\).

The \(D\)-edge of length \(d_1\) joins the left pair \(P\) to the right
pair \(T\). It gives a three-variable not-all-equal clause on the two
parallel mixed cells and their outer mixed completion. The \(D\)-edge of
length \(d_2\) similarly joins \(R\) to \(Q\) and gives a second
three-variable clause.

Under (12), the four variables from the two sum clauses lie inside the two
separate center clusters, whereas the six variables from the two
difference clauses cross between the clusters. All ten physical mixed
cells are distinct. Consequently the two binary clauses and two
three-variable clauses are jointly satisfiable: color both cells of the
first sum clause \(C\), both cells of the second sum clause \(B\), and use
both colors in each of the two difference triples.

This is only a local assignment to the four core clauses. The companion
edges forced by the rectangle-closure lemma, and any further
representations of their mixed-cell offsets, impose additional clauses.
Those are the first places where actual weak properness can obstruct the
cycle.

## 4. A concrete Golomb rectangle and the exact gap

For example, take
\[
s_1=0,\qquad s_2=30,\qquad d_1=2,\qquad d_2=6.
\]
Then
\[
B=\{-1,1,12,18\},\qquad
C=\{-3,3,14,16\}.                                  \tag{13}
\]
The two sets are disjoint Golomb rulers. Their common difference set is
\[
\{2,6,11,13,17,19\},                               \tag{14}
\]
and their distinct-pair sum sets are also equal:
\[
\{0,11,13,17,19,30\}.                              \tag{15}
\]
Thus their distinct-pair resource graph is exactly the three four-cycles
predicted above. No proper coloring of the complete \(W(B\sqcup C)\) is
claimed here.

The bounded conclusion is therefore an exact dependency gap. Difference
and sum uniqueness do not exclude an alternating four-cycle; rather, one
cycle forces a twelve-resource rectangle closure. The four original weak
constraints themselves are variable-disjoint and satisfiable in the
separated regime. To prove that a four-cycle is impossible under actual
proper weak coloring, one must propagate through the two companion cycles
and the remaining mixed-offset constraints. Conversely, a proper weak
counterexample must color that entire closure, not just the four clauses
of the chosen cycle. No conclusion about longer alternating cycles follows
from this four-cycle calculation.
