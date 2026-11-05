# Paired forcing offsets at one strict-source cell

Let \(A\subset\mathbb Z\) carry a proper two-color strict-source
coloring \(z\).  Fix a cell

\[
q=(v,u),\qquad u<v,\qquad L=v-u,
\]

and write

\[
t=z(q),\qquad s=-t.
\]

A forcing offset \(d\) at \(q\) means

\[
0<d<L,\qquad u+d,v-d\in A,
\]

\[
z(u+d,u)=z(v,v-d)=s.
\tag{1}
\]

Take two distinct forcing offsets

\[
0<d<e<L
\tag{2}
\]

at this same \(q\).  This note records the complete first consequences of
that pair, including the complementary case \(d+e=L\), and gives two
exact resource maps.

## 1. Exact support and the four forced cells

Put

\[
a=u+d,\qquad b=u+e,\qquad
c=v-e,\qquad f=v-d,\qquad g=e-d.
\tag{3}
\]

The complete source support supplied directly by the two offsets is

\[
u,v,a,b,c,f\in A.
\tag{4}
\]

The four forcing cells are

\[
z(a,u)=z(b,u)=z(v,c)=z(v,f)=s.
\tag{5}
\]

They are four distinct physical cells even when some of the source marks
in (4) coincide: the two left cells have different rows, the two right
cells have different columns, and a left cell cannot equal a right cell
under (2).

The inner marks satisfy

\[
b-a=f-c=g,
\tag{6}
\]

and the reflection identities

\[
a+f=b+c=u+v.
\tag{7}
\]

Thus the pair of offsets always produces two source pairs of the same
positive difference \(g\):

\[
[a,b],\qquad[c,f].
\tag{8}
\]

Their possible coincidences are exact:

\[
\begin{array}{c|c}
\text{coincidence}&\text{arithmetic condition}\\ \hline
a=c\ \text{and}\ b=f&d+e=L,\\
b=c&2e=L,\\
a=f&2d=L.
\end{array}
\tag{9}
\]

There are no other cross-coincidences among \(a,b,c,f\).  In particular,
the two gap-\(g\) pairs in (8) are identical exactly in the complementary
case

\[
e=L-d.
\tag{10}
\]

The cases \(2e=L\) and \(2d=L\) give adjacent gap pairs sharing one
endpoint, but the pairs remain distinct.

## 2. The two closure dichotomies

The two left forcing cells \(z(a,u),z(b,u)\) have the same color \(s\)
and their row separation is \(g\).  Define

\[
\lambda=u+g.
\tag{11}
\]

If \(\lambda\notin A\), the offset pair supplies the explicit missing
source position \(u+g\).  If \(\lambda\in A\), the strict corner

\[
z(a,u),\qquad z(b,u),\qquad z(b,\lambda)
\]

forces

\[
z(b,\lambda)=t.
\tag{12}
\]

Here \(b-\lambda=e-g=d>0\), so the third cell is valid.

Reflecting at the right end, define

\[
\mu=v-g.
\tag{13}
\]

If \(\mu\notin A\), the offset pair supplies the explicit missing source
position \(v-g\).  If \(\mu\in A\), the strict corner

\[
z(\mu,c),\qquad z(v,c),\qquad z(v,f)
\]

forces

\[
z(\mu,c)=t.
\tag{14}
\]

Again \(\mu-c=e-g=d>0\).

Therefore every forcing-offset pair has the exact alternative

\[
\boxed{
\begin{array}{l}
u+g\notin A\quad\text{or}\quad z(u+e,u+g)=t,\\[2mm]
v-g\notin A\quad\text{or}\quad z(v-g,v-e)=t.
\end{array}}
\tag{15}
\]

The two missing positions in (15) need not be distinct.  They coincide
exactly when

\[
u+g=v-g,\qquad 2g=L.
\tag{16}
\]

No missing position is asserted when the relevant closure mark belongs to
\(A\).

## 3. When both closure marks are present

Assume \(\lambda,\mu\in A\).  The two cells forced in (12) and (14) both
have length \(d\) and color \(t\):

\[
p=z(b,\lambda)=t,\qquad r=z(\mu,c)=t.
\tag{17}
\]

Their starts are \(\lambda\) and \(c\).

If \(\lambda<c\), they form a strict corner whose completion is

\[
z(\mu,\lambda)=s.
\tag{18}
\]

If \(c<\lambda\), their completion is

\[
z(b,c)=s.
\tag{19}
\]

If \(\lambda=c\), then automatically \(b=\mu\), so \(p=r\) is one
physical cell and there is no pair of distinct length-\(d\) cells to
complete.  The coincidence condition is

\[
\lambda=c
\quad\Longleftrightarrow\quad
2e=L+d.
\tag{20}
\]

Equations (18)--(20) exhaust the second-generation possibilities.  All
endpoints of the completion cell in (18) or (19) are already source marks,
so no additional source membership is needed.

## 4. Complementary offsets

Suppose

\[
d+e=L.
\tag{21}
\]

Then

\[
c=a,\qquad f=b,
\]

and the direct support reduces to the four distinct marks

\[
u<a<b<v.
\tag{22}
\]

Their consecutive gaps are

\[
d,\quad g=e-d,\quad d,
\]

and they satisfy the nested pair-sum identity

\[
u+v=a+b.
\tag{23}
\]

Thus the two gap pairs in (8) have coalesced, but the offset pair supplies
one distinct-distinct equal-sum resource: the outer pair \(\{u,v\}\) and
the inner pair \(\{a,b\}\).

The closure positions become

\[
\lambda=u+e-d,\qquad \mu=u+2d.
\tag{24}
\]

There is one further exact coincidence inside this case:

\[
e=2d
\quad\Longleftrightarrow\quad
L=3d
\quad\Longleftrightarrow\quad
\lambda=a,\ \mu=b.
\tag{25}
\]

When (25) holds, the two propagated cells in (12) and (14) coincide as

\[
z(b,a)=t.
\tag{26}
\]

When \(e<2d\) and both closure marks are present, (18) applies and forces
the outer completion \(z(\mu,\lambda)=s\).  When \(e>2d\), (19) applies
and forces the inner cell

\[
z(b,a)=s.
\tag{27}
\]

There is no contradiction at \(e=2d\): equation (26) is then the sole
propagated cell, while the two-cell completion used for (27) has
coalesced.

## 5. Two exact resource maps

Every unordered pair of forcing offsets at \(q\) maps to

\[
\Phi(q;\{d,e\})=(u,u+d,u+e,v).
\tag{28}
\]

The four entries are strictly increasing.  Conversely, the image
recovers

\[
q=(v,u),\qquad d=(u+d)-u,\qquad e=(u+e)-u.
\]

Hence \(\Phi\) is injective.  If \(H_q\) denotes the number of forcing
offsets at \(q\), then

\[
\boxed{
\sum_q\binom{H_q}{2}\le\binom{|A|}{4}.
}
\tag{29}
\]

This is a quartic source-support bound.  It does not give or assume a
pointwise bound on \(H_q\).

There is also a more geometric resource split.

* If \(d+e=L\), map the pair to the nested equal-sum resource

  \[
  \{\{u,v\},\{a,b\}\},\qquad u<a<b<v,\quad u+v=a+b.
  \tag{30}
  \]

  This map is injective because the ordered four marks recover \(d,e\).

* If \(d+e\ne L\), map the pair to the ordered equal-difference resource

  \[
  \Gamma=(g;[a,b],[c,f]),
  \qquad b-a=f-c=g,
  \tag{31}
  \]

  where the two pairs are distinct, possibly sharing one endpoint as in
  (9).

The second map need not have constant multiplicity.  For a fixed ordered
resource \(\Gamma=(g;[a,a+g],[c,c+g])\), its preimages are exactly the
integers \(d\) for which

\[
u=a-d\in A,\qquad
e=d+g,\qquad
v=c+e=c+d+g\in A,
\tag{32}
\]

together with

\[
0<d<d+g<L=c-a+2d+g,\qquad 2d+g\ne L,
\]

and the four color equalities (5), after retaining the chosen left/right
orientation.  Thus its reuse is the explicit count

\[
\nu(\Gamma)=
\left|
\left\{
d>0:
a-d,c+d+g\in A,\ 
d+g<c-a+2d+g,\ 
2d+g\ne c-a+2d+g,\ 
z(a,a-d)=z(a+g,a-d)
=z(c+d+g,c)=z(c+d+g,c+g)
\right\}
\right|,
\tag{33}
\]

with the common color required to be opposite the recovered completion
cell \(z(c+d+g,a-d)\).

No constant bound on \(\nu(\Gamma)\) follows from this derivation.  The
four-mark injection (28) retains every such reuse separately.

## 6. Scope

Two forcing offsets at one cell produce:

1. the six-mark reflected support (4), with all endpoint coincidences
   classified by (9);
2. four distinct forced-\(s\) cells (5);
3. the two exact hole-or-opposite-color alternatives (15);
4. a second forced-\(s\) completion when both closures exist and remain
   distinct, as in (18)--(20);
5. either a distinct repeated-difference resource (31), or, for
   complementary offsets, the nested equal-sum resource (30);
6. the injective ordered quadruple (28).

The result supports a moment analysis of
\(\sum_q\binom{H_q}{2}\), but (29) is not a linear source budget and no
pointwise \(H_q\) deficit is claimed.
