# Two-layer overlap energy identities

## 1. Setup

Translate finite integer sets \(B,C\) so both have minimum zero, place
both in \([0,S]\) with \(S=\max(\operatorname{span}B,\operatorname{span}C)\), and take
\[
A=B\cup(C+Q),
\qquad
Q>2\max(\operatorname{span}B,\operatorname{span}C).
\]
For a signed displacement \(\delta\in\mathbb Z\), define
\[
D_\delta=B\cap(C-\delta)
=\{b\in B:b+\delta\in C\}.
\tag{1}
\]
This is the start set of the cross-layer difference fiber \(Q+\delta\): its
diagonal cells are
\[
p_\delta(b)=z(b+\delta+Q,b),
\qquad b\in D_\delta.
\]
If \(V(A)\) is properly two-colored, these diagonal colors induce a proper
weak triangle on \(D_\delta\). In particular, each color class in
\(D_\delta\) is Golomb. The identities below use the full overlap sets
\(D_\delta\), before discarding this inherited structure.

For any finite integer set \(X\), write
\[
r_X(h)=|X\cap(X-h)|\quad(h>0),
\qquad
\mathcal E(X)=\sum_{h>0}\binom{r_X(h)}2.
\tag{2}
\]
For two finite sets define their common-difference energy
\[
U(X,Y)=\sum_{h>0}r_X(h)r_Y(h).
\tag{3}
\]
Finally, put
\[
X_h=X\cap(X-h),
\tag{4}
\]
the start set of the length-\(h\) pairs in \(X\).

## 2. A general cross-correlation identity

For finite integer sets \(X,Y\), let
\[
n_\delta(X,Y)=|X\cap(Y-\delta)|.
\]
Then
\[
\sum_{\delta\in\mathbb Z}\binom{n_\delta(X,Y)}2
=U(X,Y).
\tag{5}
\]
Indeed, an unordered pair of distinct elements \(x<x'\) in
\(X\cap(Y-\delta)\) corresponds uniquely to the two pairs
\[
x,x'\in X,
\qquad
x+\delta,x'+\delta\in Y,
\]
which have the same positive gap \(x'-x\). Conversely, a gap-\(h\) pair in
\(X\) and a gap-\(h\) pair in \(Y\) determine their common displacement
\(\delta\). Summing over \(h\) proves (5).

Applying (5) first to \(X=B,Y=C\) gives the exact first overlap moment
\[
\boxed{
\sum_{\delta\in\mathbb Z}\binom{|D_\delta|}{2}=U(B,C).
}
\tag{6}
\]
Thus common-difference energy is precisely the total number of unordered
pairs inside the whole cross-fiber start sets.

## 3. Energy of the overlap fibers

For every \(h>0\), equations (1) and (4) give
\[
r_{D_\delta}(h)
=|B_h\cap(C_h-\delta)|.
\tag{7}
\]
Using (5) again, now with \(X=B_h,Y=C_h\), and exchanging the finite sums,
we obtain
\[
\begin{aligned}
\sum_{\delta\in\mathbb Z}\mathcal E(D_\delta)
&=\sum_{h>0}\sum_\delta
  \binom{|B_h\cap(C_h-\delta)|}{2}\\
&=\boxed{\sum_{h>0}U(B_h,C_h)}.
\tag{8}
\end{aligned}
\]
This is the requested second overlap moment. It says that energy inside the
cross fibers counts pairs of congruent additive rectangles: the first side
\(h\) chooses an edge in each layer, while the energy inside its two start
sets matches a second side.

Combining (6) and (8), any uniform implication valid for the inherited weak
triangles,
\[
\mathcal E(D)\le \kappa\binom{|D|}{2},
\tag{9}
\]
immediately transfers to the aggregate statement
\[
\sum_\delta\mathcal E(D_\delta)
\le \kappa U(B,C).
\tag{10}
\]
No independence between fibers is used. Equation (10) is simply the weighted
average of the individual ratios in (9), with weights
\(\binom{|D_\delta|}{2}\).

## 4. Same-side intersection inequality

For arbitrary finite \(X,Y\), Cauchy--Schwarz gives
\[
U(X,Y)
\le
\sqrt{
\left(2\mathcal E(X)+\binom{|X|}{2}\right)
\left(2\mathcal E(Y)+\binom{|Y|}{2}\right)}.
\tag{11}
\]
This follows from
\[
\sum_{g>0}r_X(g)^2
=2\mathcal E(X)+\sum_{g>0}r_X(g)
=2\mathcal E(X)+\binom{|X|}{2}.
\]

Apply one global Cauchy--Schwarz inequality to the double sum in (8). Since
\[
\sum_{h>0}\binom{|B_h|}{2}
=\sum_{h>0}\binom{r_B(h)}2
=\mathcal E(B),
\]
and likewise for \(C\), one obtains
\[
\boxed{
\sum_\delta\mathcal E(D_\delta)
\le
\sqrt{
\left(\mathcal E(B)+2\sum_{h>0}\mathcal E(B_h)\right)
\left(\mathcal E(C)+2\sum_{h>0}\mathcal E(C_h)\right)}.
}
\tag{12}
\]
This inequality retains all same-side intersections. It is exact on the
diagonal \(B=C\): both sides then equal
\[
\mathcal E(B)+2\sum_{h>0}\mathcal E(B_h).
\]
Hence no improvement of (12) is possible from Cauchy--Schwarz alone.

## 5. Remaining quantitative gap

Equations (6) and (8) separate the two quantities that an aggregate argument
must connect:
\[
U(B,C)=\sum_\delta\binom{|D_\delta|}{2},
\qquad
\sum_\delta\mathcal E(D_\delta)
=\sum_hU(B_h,C_h).
\]
The inherited weak coloring acts on each whole \(D_\delta\), so a valid
per-fiber energy bound transfers by (10). By contrast, applying a standalone
Cartesian estimate directly to \(B_h\times C_h\) would discard exactly this
whole-fiber structure and is not justified.

The remaining gap for a sharper cross-energy theorem is therefore explicit:
one needs either a stronger ratio bound in (9) for weakly proper overlap sets,
or a way to couple the Golomb partitions belonging to different
\(\delta\)'s. The purely additive identity (8) does not provide that coupling,
and (12) is already sharp when the two layers coincide.
