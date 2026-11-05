# A minimal cross-direction overlap of forcing blocks

Let \(z\) be a proper two-coloring of the strict source triangle \(V(A)\).
This note considers one \(2\times2\) one-column forcing block and one
reflected \(2\times2\) one-row forcing block.  Their common physical cell
is an output of the column block and an input of the row block.

The result is a four-slot source-mark alternative.  Each cross slot is
either an explicit missing mark or a cell forced to the common input
color.  If all four marks are present, properness makes them distinct.
No general forcing-graph edge bound or constant reuse statement is
inferred.

## 1. The two blocks and their common cell

Fix source marks ordered as

\[
r_1<r_2<u<a_1<a_2<v<w,
\qquad
u<x<v.
\tag{1}
\]

Put

\[
q=(v,u),\qquad z(q)=t,\qquad s=-t.
\tag{2}
\]

The one-column block anchored at \(u\) has input cells

\[
X_i=(a_i,u),\qquad z(X_i)=s,\qquad i=1,2,
\tag{3}
\]

and output cells

\[
Q_0=(v,u)=q,\qquad Q_1=(w,u),
\qquad z(Q_0)=z(Q_1)=t.
\tag{4}
\]

For \(b_0=v,b_1=w\), completeness of this forcing biclique supplies

\[
c_{\ell i}=u+b_\ell-a_i\in A,
\]

\[
R_{\ell i}=(b_\ell,c_{\ell i}),\qquad
z(R_{\ell i})=s
\qquad(\ell=0,1,\ i=1,2).
\tag{5}
\]

These are the third cells of the four column-direction forcing corners.
The source-cost lemma makes the four marks \(c_{\ell i}\) distinct.

The reflected one-row block anchored at \(v\) has input cells

\[
J_0=(v,u)=q,\qquad J_1=(v,x),
\qquad z(J_0)=z(J_1)=t,
\tag{6}
\]

and output cells

\[
P_j=(v,r_j),\qquad z(P_j)=s,\qquad j=1,2.
\tag{7}
\]

For \(\alpha_0=u,\alpha_1=x\), its four supporting marks and cells are

\[
p_{\ell j}=v+r_j-\alpha_\ell\in A,
\]

\[
S_{\ell j}=(p_{\ell j},r_j),\qquad
z(S_{\ell j})=t
\qquad(\ell=0,1,\ j=1,2).
\tag{8}
\]

Equations (5) and (8) are the complete direct source support of the two
blocks.  The shared cell \(q\) has compatible colors because it is a
column output of color \(t\) and a row input of the same color.

There is one immediate forbidden extra physical overlap.  At the shared
row \(v\),

\[
R_{0i}=(v,c_{0i})\ \text{has color }s,
\qquad
J_1=(v,x)\ \text{has color }t.
\]

Therefore an actual compatible pair of blocks must satisfy

\[
x\ne c_{01},c_{02}.
\tag{9}
\]

No other input/output cell coincidence follows from the order in (1).

## 2. The four cross slots

For the shared column output \(q\), abbreviate

\[
c_i=c_{0i}=u+v-a_i.
\tag{10}
\]

Since \(a_i<v\), one has

\[
r_j<u<c_i<v.
\tag{11}
\]

The two cells

\[
R_{0i}=(v,c_i),\qquad P_j=(v,r_j)
\]

lie in the same row and both have color \(s\).  Their column gap is
\(c_i-r_j\).  The third source position required by this strict corner is

\[
k_{ij}=v-(c_i-r_j)
=r_j+(a_i-u).
\tag{12}
\]

Put

\[
d_i=a_i-u>0.
\tag{13}
\]

Then \(k_{ij}=r_j+d_i\), and (1) gives

\[
r_j<k_{ij}<v.
\]

Properness gives the exact alternative

\[
\boxed{
k_{ij}\notin A
\quad\text{or}\quad
z(k_{ij},r_j)=t
}
\qquad(i,j\in\{1,2\}).
\tag{14}
\]

Thus the overlap of the two forcing blocks creates the additive product

\[
\{r_1,r_2\}+\{d_1,d_2\}
\tag{15}
\]

as four tagged candidate source marks.  Presence of a candidate forces
the corresponding cell to the color of the shared cell \(q\); absence is
an actual source hole.

## 3. Present cross slots are injective

Assume all four marks in (12) belong to \(A\).  Equalities with a common
row or common column index are trivial:

\[
k_{i1}\ne k_{i2},\qquad k_{1j}\ne k_{2j}.
\]

The only possible nontrivial collision is

\[
k_{21}=k_{12},
\tag{16}
\]

equivalently

\[
d_2-d_1=r_2-r_1=:h>0.
\tag{17}
\]

Under (16), the three cells

\[
z(k_{11},r_1),\qquad
z(k_{21},r_1),\qquad
z(k_{12},r_2)
\tag{18}
\]

are all forced to color \(t\) by (14).  They form a strict step-\(h\)
corner: the first two share column \(r_1\), their row difference is \(h\),
and the third cell has row \(k_{21}=k_{12}\) and column
\(r_1+h=r_2\).  This is monochromatic, contradicting properness.

Therefore

\[
\boxed{
\text{if all four }k_{ij}\text{ are present, they are pairwise distinct.}
}
\tag{19}
\]

Equivalently, the smallest overlapping pair of \(2\times2\) blocks has
the source-cost alternative

\[
\boxed{
\text{some }k_{ij}\notin A
\quad\text{or}\quad
\{k_{11},k_{12},k_{21},k_{22}\}\subset A
\text{ has size }4.
}
\tag{20}
\]

In the second branch, the four cells \(z(k_{ij},r_j)\) are all color
\(t\).  This is an exact injection of the four cross incidences into
source marks.

If a missing position is used as the charge instead, multiplicity must be
retained.  For this \(2\times2\) block a position can represent two tagged
slots only in the collision pattern (16); the correct missing-mark
multiplicity is

\[
\nu(k)=
|\{(i,j)\in\{1,2\}^2:r_j+d_i=k,\ k\notin A\}|.
\tag{21}
\]

It is not legitimate to replace the tagged holes by distinct bare marks.

## 4. Further colors when the four marks are present

Suppose the four \(k_{ij}\) are present and therefore distinct.  For each
fixed \(i\), the cells

\[
K_{i1}=(k_{i1},r_1),\qquad
K_{i2}=(k_{i2},r_2)
\]

have the same length \(d_i\) and color \(t\).  Their completion is

\[
O_i=(k_{i2},r_1),
\qquad z(O_i)=s.
\tag{22}
\]

The two cells \(O_1,O_2\) share column \(r_1\), have color \(s\), and
their row difference is

\[
\delta=d_2-d_1.
\tag{23}
\]

Hence one more exact support alternative is

\[
\boxed{
r_1+\delta\notin A
\quad\text{or}\quad
z(k_{22},r_1+\delta)=t.
}
\tag{24}
\]

At the same time, the two cells \(K_{11},K_{21}\) share column \(r_1\),
have color \(t\), and have the same row difference \(\delta\).  If
\(r_1+\delta\in A\), they force

\[
z(k_{21},r_1+\delta)=s.
\tag{25}
\]

The cells in (24) and (25) are distinct because
\(k_{22}-k_{21}=r_2-r_1>0\).  Thus this additional support creates two
oppositely colored cells in one column, not an immediate contradiction.

When

\[
\delta=r_2-r_1,
\tag{26}
\]

the extra mark in (24) is the already present mark \(r_2\).  In that
case (25) is exactly the third cell in (18), and the monochromatic
contradiction occurs before (22) can be formed.  This recovers the
collision exclusion (19).

For unequal gaps, the marks in (20) alone remain locally compatible.
The precise additional support exposed at the next step is
\(r_1+\delta\): its absence is a hole, while its presence forces the two
cells (24)--(25) with opposite colors.  A further contradiction would
need another block cell or source translation to identify one of these
cells with a previously forced cell of the other color, or to complete a
new monochromatic pair.  No such extra support is assumed here.

## 5. Source tuple and scope

The bounded overlap is determined by the ordered source tuple

\[
(r_1,r_2,u,a_1,a_2,v,w,x)
\tag{27}
\]

together with the direct support marks in (5) and (8).  The four cross
slots are then fixed by (12).  In the present branch, each present slot
injects into its source mark; missing slots retain the tagged multiplicity
(21).

This derivation treats one cross-role overlap in which \(q\) is a column
output and a row input.  Reflection and color exchange give the reversed
orientation.  It does not classify output-output or input-input block
overlaps, does not bound reuse between many blocks, and does not imply a
universal forcing-graph edge estimate.
