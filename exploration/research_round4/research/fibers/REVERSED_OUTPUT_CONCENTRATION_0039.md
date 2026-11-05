# Concentration at one reversed anchored output

Normalize \(\min A=0\), put \(B=A\setminus\{0\}\), and write
\[
f(t)=z(t,0).
\]
Fix \(w\in B\) and a color \(s\) with
\[
f(w)=-s.
\]
Consider the reversed decompositions
\[
x_i+y_i=w,\qquad
0<x_i<y_i,\qquad
f(x_i)=f(y_i)=s.                                      \tag{1}
\]
Order them so that
\[
x_1<x_2<\cdots<x_q<w/2,
\qquad
y_1>y_2>\cdots>y_q>w/2.                               \tag{2}
\]
For each decomposition retain both physical cells
\[
A_i=z(w,x_i),\qquad D_i=z(w,y_i).                      \tag{3}
\]
Neither color in (3) is forced by the anchored relation (1) alone.
This note shows that pairs of nested decompositions force a concentration
of the color \(s\) among these cells.

## 1. The nested four-cycle lemma

Fix \(i<j\).  Abbreviate
\[
x=x_i,\quad X=x_j,\quad Y=y_j,\quad y=y_i,
\]
so
\[
x<X<Y<y,\qquad x+y=X+Y=w.                             \tag{4}
\]
Define the two cross-sums
\[
t=x+X,\qquad r=x+Y=w-(X-x).                            \tag{5}
\]

**Lemma 1.**  Suppose
\[
t,r\in B,\qquad f(t)=f(r)=s.                           \tag{6}
\]
Then among the four cells
\[
z(w,x),\ z(w,X),\ z(w,Y),\ z(w,y)                     \tag{7}
\]
at least two have color \(s\).  Equivalently,
\[
\boxed{\qquad
p_i+p_j\ge2,\qquad
p_k=\mathbf1_{A_k=s}+\mathbf1_{D_k=s}.
\qquad}                                                \tag{8}
\]

**Proof.**  List the cells in (7), in increasing column order, as
\[
A=(w,x),\quad B'=(w,X),\quad C=(w,Y),\quad D=(w,y).
\]
The pairs \(A,B'\) and \(C,D\) have completions
\[
P=(r,x),\qquad Q=(r,Y),                                \tag{9}
\]
respectively.  Since \(x,X,t\) all have anchored color \(s\), the two
anchored corners belonging to \(x+X=t\) force
\[
R=(t,x),\qquad S=(t,X)                                \tag{10}
\]
to color \(-s\).  But \(R,S\) are also the completions of the row-\(w\)
pairs \(A,C\) and \(B',D\), respectively.  Therefore neither
\[
\{A,C\},\qquad\{B',D\}                                \tag{11}
\]
can consist of two cells of color \(-s\).

Likewise, \(x,Y,r\) all have anchored color \(s\), so the two anchored
corners belonging to \(x+Y=r\) force the cells \(P,Q\) in (9) to color
\(-s\).  Hence neither
\[
\{A,B'\},\qquad\{C,D\}                                \tag{12}
\]
can consist of two cells of color \(-s\).

The four forbidden pairs in (11)--(12) form a cycle on the four cells
in (7).  An independent set in this cycle has size at most two, so at
most two of the cells can have color \(-s\).  This proves (8).
\(\square\)

The equality case is rigid.  If exactly two cells in (7) have color
\(-s\), they must be one of the two nonedges of that cycle:
\[
\{A,D\}\quad\text{or}\quad\{B',C\}.                    \tag{13}
\]
Thus one of the two reversed decompositions has both internal cells
\(-s\), and the other has both internal cells \(s\).

## 2. Double supports strengthen two to three

The double-hinge relation from REVERSED_SUM_COUPLING_0038.md says that,
if
\[
2x_i\in B,\qquad f(2x_i)=s,                            \tag{14}
\]
then \(A_i,D_i\) cannot both have color \(-s\).  Indeed, the anchored
pair \(x_i,2x_i\) forces \(z(2x_i,x_i)=-s\), while two \(-s\) cells
\((w,x_i),(w,y_i)\) would force that same completion to color \(s\).

Applying this at both decompositions removes the two remaining nonedges
in (13).

**Lemma 2.**  Under (6), if additionally
\[
2x_i,2x_j\in B,\qquad f(2x_i)=f(2x_j)=s,               \tag{15}
\]
then
\[
\boxed{\qquad p_i+p_j\ge3.\qquad}                      \tag{16}
\]

**Proof.**  Lemma 1 forbids the four pairs in the cycle
(11)--(12).  The two double hinges forbid its two complementary pairs
\(\{A,D\}\) and \(\{B',C\}\).  Thus every pair among the four cells is
forbidden from being simultaneously \(-s\).  At most one cell is
\(-s\), proving (16).  \(\square\)

## 3. Cross-support graph and a concentration bound

For the fixed output \(w\), define a graph \(G_w\) on the decomposition
indices \(\{1,\ldots,q\}\).  Join \(i<j\) when both cross-sums
\[
x_i+x_j,\qquad x_i+y_j                                \tag{17}
\]
belong to \(B\) and both have anchored color \(s\).  Lemma 1 gives
\[
p_i+p_j\ge2\quad\text{on every edge of }G_w.           \tag{18}
\]

Let
\[
Z=\{i:p_i=0\},\qquad T=\{i:p_i=2\}.
\]
Equation (18) implies
\[
Z\text{ is independent in }G_w,\qquad N_{G_w}(Z)\subseteq T. \tag{19}
\]
Since
\[
\sum_i p_i=q-|Z|+|T|,
\]
we obtain
\[
\sum_i p_i
\ge q-|Z|+|N_{G_w}(Z)|.                               \tag{20}
\]
Define the independent-set expansion defect
\[
\delta(G_w)=
\max_{\substack{I\subseteq V(G_w)\\I\ {\rm independent}}}
\bigl(|I|-|N_{G_w}(I)|\bigr)_+ .
\]
Then (20) gives the complete concentration inequality
\[
\boxed{\qquad
\sum_{i=1}^q
\left(\mathbf1_{z(w,x_i)=s}+
      \mathbf1_{z(w,y_i)=s}\right)
\ge q-\delta(G_w).
\qquad}                                                \tag{21}
\]
In particular, if \(G_w\) has the elementary expansion property
\[
|N(I)|\ge|I|
\quad\text{for every independent }I,                  \tag{22}
\]
then at least \(q\) of the \(2q\) retained physical cells have color
\(s\).

The cells counted in (21) are actual anchored-fiber memberships.  Namely,
\[
A_i=s\Longleftrightarrow x_i\in P_{y_i},
\qquad
D_i=s\Longleftrightarrow y_i\in P_{x_i},               \tag{23}
\]
in the notation of ANCHORED_SUM_PEELING_0037.md.  Thus a highly reused
reversed output with a well-supported graph \(G_w\) pays for its
decompositions by memberships in the sum-free Golomb sets \(P_x\);
it is not merely assigned an abstract charge.

There is a stronger dense-double case.  Let
\[
K=\{i:2x_i\in B,\ f(2x_i)=s\}.                         \tag{24}
\]
Lemma 2 says \(p_i+p_j\ge3\) on every edge induced by \(K\).  Hence if
\(G_w[K]\) is a clique, at most one vertex of \(K\) can have \(p_i=1\),
and all others have \(p_i=2\).  Therefore
\[
\sum_{i\in K}p_i\ge2|K|-1.                            \tag{25}
\]
This is near-total concentration of the retained cells into the color
\(s\).

## 4. Exact support gap

The conclusion is intentionally conditional on the two cross-sums in
(17).  For nested decompositions, these marks are
\[
x_i+x_j,\qquad x_i+w-x_j.                              \tag{26}
\]
They need not belong to a sparse source, and when they do belong their
anchored colors need not be \(s\).  If either support fails, the forced
cells \(P,Q,R,S\) used in Lemma 1 are unavailable or have no prescribed
color, so the four-cycle constraint does not follow.

Consequently \(G_w\) can be empty even when \(w\) has many reversed
decompositions.  The present argument gives no absolute cap on \(q\),
as required by the known possibility of large local multiplicity.  Its
new content is a dichotomy:

* a dense cross-support graph forces at least \(q-\delta(G_w)\) genuine
  memberships in the other anchored fan sets, and double support raises
  this toward \(2q\);
* a failure of concentration requires a large independent collection of
  decompositions whose pairwise cross-sums are absent or have the wrong
  anchored color.

A global endpoint bound would still need to pay that second alternative
by missing marks, wrong-color anchored fans, or a bounded-multiplicity
selection across different outputs \(w\).  No universal bound on
\(q_w\), the total reversed count, EP10, or the main source energy is
asserted here.
