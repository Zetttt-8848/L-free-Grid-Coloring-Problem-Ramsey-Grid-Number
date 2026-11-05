# A two-endpoint ledger for one additive parallelogram

Let
\[
a,\quad b=a+x,\quad c=a+y,\quad d=a+x+y,
\qquad 0<x<y,                                         \tag{1}
\]
be four source marks.  The equality
\[
a+d=b+c
\]
supports two directed positive corners.  Write the five physical cell
signs as
\[
u=z(b,a),\qquad v=z(c,a),\qquad q=z(d,a),
\]
\[
r=z(d,b),\qquad s=z(d,c).                              \tag{2}
\]
The four side cells are \(u,v,r,s\), and \(q\) is the outer cell.  The
two corners are
\[
\{u,q,s\},\qquad \{v,q,r\}.                            \tag{3}
\]

At the minimum endpoint \(a\), classify the anchored relation by comparing
\((u,v)\) with \(q\):

* \(P\): \(u=v=q\);
* \(R\): \(u=v=-q\);
* \(M\): \(u=-v\).

At the maximum endpoint \(d\), reflect the source and make the same
classification using the side pair \((r,s)\) and the same outer cell
\(q\).  Thus one four-mark relation contributes one type at each
endpoint.

## 1. Complete five-sign classification

Normalize \(q=+\).  Properness of the two corners (3) is exactly
\[
\neg(u=+\ \&\ s=+),\qquad
\neg(v=+\ \&\ r=+).                                   \tag{4}
\]
The two prohibited pairs are disjoint, so there are \(3\cdot3=9\)
allowed assignments of the four side signs.  Grouping them by endpoint
type gives the complete table
\[
\begin{array}{c|c|c|c}
\text{minimum type}&\text{maximum type}
 &\text{side signs }(u,v;r,s)&\text{number}\\ \hline
R&R&(--;--)&1\\
R&P&(--;++)&1\\
P&R&(++;--)&1\\
R&M&(--;+-),\ (--;-+)&2\\
M&R&(+-;--),\ (-+;--)&2\\
M&M&(-+;-+),\ (+-;+-)&2 .
\end{array}                                            \tag{5}
\]
No other endpoint-type pair is possible.  In particular,
\[
P\text{ at one endpoint forces }R\text{ at the other}. \tag{6}
\]
The unique \(R/R\) assignment has
\[
u=v=r=s=-q.                                            \tag{7}
\]
Call such a relation a **pure reversed rectangle**.

## 2. Exact two-end counting identity

For any collection of four-distinct-mark additive parallelograms, let
\[
X=N_{RR},
\]
\[
Y=N_{RP}+N_{PR},\qquad
Z=N_{RM}+N_{MR},\qquad
W=N_{MM}.                                              \tag{8}
\]
Let \(\mathcal R,\mathcal P,\mathcal M\) count endpoint incidences of
types \(R,P,M\), respectively, over both ends of all these relations.
Table (5) gives
\[
\mathcal R=2X+Y+Z,\qquad
\mathcal P=Y,\qquad
\mathcal M=Z+2W.                                      \tag{9}
\]
Consequently
\[
\boxed{\qquad
\mathcal R-\mathcal P=2X+Z.
\qquad}                                                \tag{10}
\]
Also
\[
\mathcal R+\mathcal P+\mathcal M
=2(X+Y+Z+W),                                          \tag{11}
\]
as every parallelogram has two endpoint classifications.

Thus the excess of reversed over positive endpoint types has two exact
sources:

* two units from every pure reversed rectangle;
* one unit from every rectangle of type \(R/M\) or \(M/R\).

The \(R/P\) and \(P/R\) relations cancel in the difference, while \(M/M\)
contributes to neither side.  No inequality has been used in
(9)--(11); this is a partition of all allowed five-sign assignments.

## 3. Pure rectangles inject into two signed-fiber inventories

For a pure rectangle, (7) says that the two offset-\(x\) cells
\[
(a+x,a),\qquad (a+x+y,a+y)                             \tag{12}
\]
have the common sign \(-q\).  Their starts differ by \(y\).  Likewise,
the two offset-\(y\) cells
\[
(a+y,a),\qquad (a+x+y,a+x)                             \tag{13}
\]
have sign \(-q\), and their starts differ by \(x\).

Therefore a pure rectangle supplies two actual monochromatic signed-fiber
pairs:
\[
(\text{fiber offset }x,\ \text{pair gap }y,\ \text{sign }-q),
\]
\[
(\text{fiber offset }y,\ \text{pair gap }x,\ \text{sign }-q). \tag{14}
\]
Each entry in either line of (14) determines the rectangle uniquely.
For example, the offset-\(x\) pair in (12) gives its smaller start \(a\),
its start gap \(y\), and hence all four marks in (1).  Thus both maps in
(14) are injective over the collection of pure rectangles.

Because \(x<y\), the first map lands among signed-fiber pairs whose pair
gap exceeds their fiber offset, while the second lands among those whose
pair gap is smaller.  If \(\mathcal G_>\) and \(\mathcal G_<\) denote
these two inventories, then
\[
\boxed{\qquad
X\le\min\{|\mathcal G_>|,|\mathcal G_<|\},
\qquad
2X\le|\mathcal G_>|+|\mathcal G_<|.
\qquad}                                                \tag{15}
\]

Signed-fiber Golombness says that, for fixed fiber offset and fixed sign,
each positive pair gap occurs at most once.  Hence the labels in (14)
are already collision-free.  This makes (15) a genuine injection, but
does not turn it into a linear source bound: the number of available
\((\text{offset},\text{gap})\) labels can itself be large.

## 4. Equal-input progressions

If \(x=y\), the four-mark parallelogram collapses to the three marks
\[
a,\quad a+x,\quad a+2x
\]
and only one directed corner remains.  Write
\[
u=z(a+x,a),\qquad q=z(a+2x,a),\qquad
r=z(a+2x,a+x).
\]
There is one input at each reflected endpoint.  Classify it as \(P\) if
the side sign equals \(q\), and \(R\) if it equals \(-q\).  The NAE
condition on \(\{u,q,r\}\) permits exactly
\[
(P,R),\qquad(R,P),\qquad(R,R),                         \tag{16}
\]
where the last case is the collapsed pure rectangle \(u=r=-q\).
For a collection of these progressions,
\[
\mathcal R-\mathcal P=2X_{\rm AP},                     \tag{17}
\]
with \(X_{\rm AP}\) the number having both side cells opposite the outer
cell.  The mixed type is absent because an equal-input relation has only
one side incidence at each endpoint.

## 5. Exact limitation of the local ledger

The injections (14)--(15) account cleanly for the \(2X\) term in
(10).  They charge each pure rectangle to two different physical
same-sign fiber pairs, and neither charge can collide with that of a
second pure rectangle.

There are two remaining obstacles to a nontrivial local endpoint bound.
First, signed-fiber Golombness controls repetition of a gap inside one
fixed offset and sign, but it does not bound the total number of
offset-gap labels across the source.  The charge inventory in (15) is
therefore of the same general scale as the source-corner count one is
trying to control.

Second, the \(Z\) term in (10) comes from \(R/M\) rectangles.  Such a
rectangle has only one endpoint with two sides opposite the outer sign;
its other side pair is bichromatic.  It supplies no second
monochromatic parallel pair analogous to (13), so the symmetric
two-fiber charge for a pure rectangle is unavailable.

Accordingly, the exact reusable statements are the ledger (10) and the
pure-rectangle injections (15).  A global endpoint estimate would still
need either a capacity bound coupling different signed offsets, or a
separate charge for the \(R/M\) term \(Z\).  No uniform endpoint or source
bound is asserted from the five-sign classification alone.
