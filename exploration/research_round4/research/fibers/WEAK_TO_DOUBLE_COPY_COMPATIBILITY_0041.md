# Compatibility of a weak triangle with two separated strict copies

Let \(S\subset\mathbb Z\) be finite, let
\(\ell=\operatorname{span}(S)\), and choose

\[
d>2\ell.
\tag{1}
\]

Put

\[
A=S\sqcup(S+d).
\tag{2}
\]

Every cross-copy pair is positively oriented: \(d+v>u\) for all
\(u,v\in S\).

Suppose first that a coloring of \(V(A)\) is given.  Separate its cells
into

\[
L(v,u)=z(v,u),\qquad u<v,\quad u,v\in S,
\tag{3}
\]

\[
U(v,u)=z(d+v,d+u),\qquad u<v,\quad u,v\in S,
\tag{4}
\]

and the full cross matrix

\[
X(v,u)=z(d+v,u),\qquad u,v\in S.
\tag{5}
\]

Thus \(L,U\) are strict triangular colorings on \(S\), while \(X\) is
defined on every ordered pair in \(S\times S\), including its diagonal
and lower triangle.

## 1. Exact corner classification

**Compatibility theorem.**  The coloring \(z\) is proper on \(V(A)\)
if and only if all three conditions below hold.

1. \(L\) and \(U\) are each proper strict colorings of \(V(S)\).

2. For every \(h>0\) and
   \(r,r+h,c,c+h\in S\), the cross-matrix triple

   \[
   X(r,c),\qquad X(r+h,c),\qquad X(r+h,c+h)
   \tag{6}
   \]

   is not monochromatic.

3. For every \(h>0\) and
   \(u,u+h,v,v+h\in S\), the bridge triple

   \[
   L(u+h,u),\qquad X(v+h,u),\qquad U(v+h,v)
   \tag{7}
   \]

   is not monochromatic.

**Proof.**  Every internal positive difference is at most \(\ell\).
Every cross-copy difference has the form

\[
d+v-u\ge d-\ell>\ell.
\tag{8}
\]

Thus two equal-difference endpoint cells are either both internal or
both cross-copy.

For an internal difference \(h\), two endpoint cells can both lie in
the lower copy, both lie in the upper copy, or lie one in each copy.
The first two alternatives give condition 1.  In the mixed alternative,
the lower endpoint has start \(u\), the upper endpoint has start
\(d+v\), and their completion is

\[
(d+v+h,u),
\]

which is \(X(v+h,u)\).  This is exactly (7).

Two cross cells \(X(r,c)\) and \(X(r',c')\) have equal positive
difference precisely when

\[
r-c=r'-c'.
\tag{9}
\]

Ordering the column starts as \(c<c'\) gives
\(r<r'\) and a common step \(h=c'-c=r'-r\).  Their completion is
\(X(r',c)\), giving exactly the triple in (6).  These alternatives
exhaust every corner of \(V(A)\), proving necessity and sufficiency.
\(\square\)

## 2. What an inherited weak coloring prescribes

Let \(w\) be a proper coloring of

\[
W(S)=\{(v,u):u,v\in S,\ u\le v\}.
\]

For \(W(S)\) to be the weak triangle inherited from the offset-\(d\)
fiber of \(A\), compatibility requires

\[
\boxed{X(v,u)=w(v,u)\qquad(u\le v).}
\tag{10}
\]

Condition 2 restricted to \(r\ge c\) is already exactly a corner of
\(W(S)\), so it follows from the properness of \(w\).  The new
cross-matrix clauses are those with \(r<c\): their first and third
cells lie below the prescribed triangle, while their middle cell can
lie on either side.

Condition 3 is independent additional information.  It couples the
two strict-copy colorings to one physical cross cell.  When
\(v+h\ge u\), this cross cell is already prescribed by \(w\); when
\(v+h<u\), it is one of the new lower-triangular cross entries.

Consequently, extending \(w\) is exactly the problem of choosing two
proper strict colorings \(L,U\) and the lower-triangular entries of
\(X\) so that (6)--(7) hold.  There are no further corner types hidden
by the separation hypothesis.

## 3. Every weak coloring extends when \(S\) is Golomb

**Proposition.**  If \(S\) is Golomb, every proper coloring \(w\) of
\(W(S)\) extends to a proper coloring of \(V(S\sqcup(S+d))\).

**Construction.**  Set

\[
L(v,u)=0,\qquad U(v,u)=1
\tag{11}
\]

on all strict cells in the two copies.  Use (10) on the upper triangle
of \(X\), and assign arbitrary colors, for example \(0\), to its lower
triangle.

Because \(S\) is Golomb, neither strict copy has a corner, so the
constant colorings in (11) satisfy condition 1.  Every bridge in (7)
has endpoint colors \(0\) and \(1\), so condition 3 is automatic.

Finally, for a fixed \(h>0\), \(S\) has at most one pair
\(\{r,r+h\}\).  If a cross corner (6) exists, its row pair and column
pair must therefore be that same unique pair.  Hence \(r=c\), and
(6) is

\[
w(r,r),\qquad w(r+h,r),\qquad w(r+h,r+h),
\]

which is a diagonal corner of the proper weak coloring \(w\).
No lower-triangular entry of \(X\) occurs in a cross corner.  The
compatibility theorem completes the proof.

Thus any failure of weak-to-double-copy extension requires a repeated
difference in \(S\).

## 4. An exact two-bridge conflict mechanism

Repeated differences permit two different internal offsets to demand
opposite colors at one lower-triangular cross cell.

Fix \(r<c\) in \(S\), and let \(h,k>0\) satisfy

\[
r-h,r-k,c+h,c+k\in S.
\tag{12}
\]

The bridge at internal offset \(h\) uses the positive corner

\[
(c+h,c),\qquad(d+r,c),\qquad(d+r,d+r-h).
\tag{13}
\]

Its endpoint cells have colors

\[
L(c+h,c),\qquad U(r,r-h),
\]

and its shared completion is the lower cross entry

\[
X(r,c)=z(d+r,c).
\tag{14}
\]

The offset-\(k\) bridge is the distinct positive corner

\[
(c+k,c),\qquad(d+r,c),\qquad(d+r,d+r-k),
\tag{15}
\]

with the same completion.

Therefore, if

\[
L(c+h,c)=U(r,r-h)=\varepsilon
\tag{16}
\]

and

\[
L(c+k,c)=U(r,r-k)=1-\varepsilon,
\tag{17}
\]

then (13) forces \(X(r,c)=1-\varepsilon\), whereas (15) forces
\(X(r,c)=\varepsilon\).  No extension exists.  All cells in
(13)--(15) belong to the actual separated source \(A\), and both corner
steps are positive:

\[
d+r-c-h>0,\qquad d+r-c-k>0,
\]

by \(d>2\ell\).

There is also an immediate prescribed-entry obstruction.  If
\(v+h\ge u\) and

\[
L(u+h,u)=U(v+h,v)=w(v+h,u),
\tag{18}
\]

then the bridge (7) is already monochromatic; no choice of a lower
cross entry can repair it.

## 5. Exact remaining extension question

The proposition proves extension for every Golomb \(S\).  For a general
source with repeated differences, the compatibility theorem and the
two mechanisms above do not decide whether every proper \(w\) admits
some suitable choices of \(L,U\).  The copy colorings are not fixed by
\(w\), so a conflict such as (16)--(17) is an obstruction only after
those endpoint colors are forced by their own strict-copy corners or
by other bridge clauses.

A general extension theorem would therefore need a simultaneous choice
of two proper strict colorings that avoids all prescribed upper-bridge
conflicts (18) and makes the lower-cross demands consistent with
condition 2.  A counterexample would need to force opposite demands at
one cell as in (13)--(17), independently of the remaining choices.
Neither conclusion follows from weak properness alone in this
derivation.
