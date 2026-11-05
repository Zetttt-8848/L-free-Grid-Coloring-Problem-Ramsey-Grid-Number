# Companion FF parallelograms and open cube slots

In a proper two-color strict source, call a four-mark additive
parallelogram FF when both pairs of parallel side cells are monochromatic.
If its outer completion has color \(-s\), all four side cells then have
the common color \(s\).

This note derives the exact local interaction of two FF parallelograms
that overlap in three marks or occur as adjacent faces of an injective
positive three-cube. The three-cube mixed-corner minimum is used only as
context; the conclusions below are direct local implications.

## 1. Three shared marks

Let \(x<y<z\) be three source marks. The three possible fourth positions
that can complete them to a parallelogram are
\[
\ell=x+y-z,\qquad m=x+z-y,\qquad r=y+z-x.          \tag{1}
\]
The outer positions satisfy \(\ell<x<z<r\). The middle position \(m\)
lies strictly between \(x,z\), unless \(x,y,z\) form a three-term
progression, in which case \(m=y\) and that completion is degenerate.

Denote the corresponding four-mark sets by
\[
P_\ell=\{\ell,x,y,z\},\quad
P_m=\{x,y,m,z\},\quad
P_r=\{x,y,z,r\}.                                   \tag{2}
\]

**Three-mark overlap lemma.**

1. \(P_m\) cannot be FF simultaneously with either \(P_\ell\) or \(P_r\).
2. If \(m\ne y\), the pair \(P_\ell,P_r\) can survive the immediate FF
   constraints. Their common side cell \((z,x)\) fixes a common side
   color \(s\). If \(m=y\), even this exterior pair is impossible.
3. If \(m\ne y\), both \(P_\ell,P_r\) are FF, and the middle mark \(m\)
   is present,
   then
   \[
   z(y,x)=z(z,y)=s,\qquad
   z(z,m)=z(m,x)=-s.                               \tag{3}
   \]
   Hence the two companion corners of \(P_m\), both completing at
   \((z,x)\), are mixed.

To prove the first assertion, \(P_m\) and \(P_r\) share the side cell
\((y,x)\), so their FF side colors agree. But \((z,x)\) is the outer
completion of \(P_m\) and a side cell of \(P_r\), forcing it to have both
colors. The argument for \(P_\ell,P_m\) uses their shared side
\((z,y)\) and the same cell \((z,x)\).

For the exterior pair \(P_\ell,P_r\), the cell \((z,x)\) is a side of
both and has color \(s\). The cells \((y,x)\) and \((z,y)\) are also
sides, one from each exterior parallelogram, so they have color \(s\).
If \(m=y\), then \(x,y,z\) are an arithmetic progression, and these last
two cells have the same offset and complete at \((z,x)\). They would form
a monochromatic corner, proving the exceptional impossibility in item 2.
If \(m\in A\), then
\[
(y,x),\ (z,m),\ (z,x)
\]
form one corner, while
\[
(m,x),\ (z,y),\ (z,x)
\]
form the companion corner. Properness and the already equal colors in
each triple force (3).

Thus the middle position \(m\) is an exact open support slot: it may be
absent, but if it is present the two exterior FF parallelograms pay two
mixed corners.

## 2. Two adjacent faces of a positive three-cube

Let \(d,h,k>0\) have eight distinct subset sums, and suppose the six marks
\[
u,\ u+d,\ u+h,\ u+d+h,\ u+k,\ u+d+k              \tag{4}
\]
belong to \(A\). Assume the two faces
\[
\{u,u+d,u+h,u+d+h\},\qquad
\{u,u+d,u+k,u+d+k\}                               \tag{5}
\]
are FF. They share the side cell \((u+d,u)\), so both faces have the same
side color \(s\). In particular the three available cells of offset \(d\)
are
\[
\begin{aligned}
e_0&=(u+d,u),\\
e_h&=(u+d+h,u+h),\\
e_k&=(u+d+k,u+k),
\end{aligned}
\qquad z(e_0)=z(e_h)=z(e_k)=s.                    \tag{6}
\]
The two unoccupied cube slots not specified in (4) are
\[
v=u+h+k,\qquad w=u+d+h+k.                         \tag{7}
\]

**Adjacent-face slot lemma.** At least one of the following holds:

* one of \(v,w\) is absent from \(A\);
* both are present, the top offset-\(d\) cell
  \[
  e_{hk}=(w,v)
  \]
  has color \(-s\), and its three pairs with \(e_0,e_h,e_k\) are three
  distinct mixed corners.

It remains only to rule out \(z(e_{hk})=s\) when both slots are present.
Assume that equality. The pair \(e_0,e_{hk}\), both of offset \(d\), would
force the main completion
\[
Q=(w,u)
\]
to color \(-s\). On the other hand, the FF \(d,h\)-face makes
\[
q_0=(u+d+h,u)
\]
color \(-s\). The translated pair \(e_k,e_{hk}\) would likewise make
\[
q_k=(w,u+k)
\]
color \(-s\). The two cells \(q_0,q_k\) have the common offset \(d+h\)
and complete at the same cell \(Q\), forcing \(Q\) to color \(s\). This
contradiction proves \(z(e_{hk})=-s\). Equation (6) then gives the three
mixed corners.

The argument is symmetric in \(h,k\); no ordering between those two
generators is used.

## 3. Sharpness of the two open slots

The six-vertex data in (4)--(6) do not distinguish which slot in (7)
should be missing. If only \(v\) is added, the two new primitive side
cells
\[
(v,u+h),\qquad(v,u+k)
\]
may both have color \(s\), while \((v,u)\) has color \(-s\); the two new
companion corners are then forcing and proper.

If only \(w\) is added, the two translated side cells
\[
(w,u+d+h),\qquad(w,u+d+k)
\]
may have color \(s\), forcing \((w,u+d)\) to color \(-s\). The cells
\[
(w,u+k),\qquad(w,u+h)
\]
may have color \(-s\), consistently forcing \((w,u)\) to color \(s\)
against the two lower face diagonals. These assignments satisfy the new
companion corners that directly extend the two FF faces. Other difference
fibers may constrain the remaining cells of the seven-mark source; no full
seven-mark coloring is asserted. Thus the two-face argument itself does
not select one individual slot for absence.

Therefore the exact retained alternative is
\[
\boxed{
\{v,w\}\not\subseteq A
\quad\text{or}\quad
\text{three mixed corners occur in the offset-\(d\) cube fiber}.
}                                                   \tag{8}
\]
This is a local support-or-mixed payment. It gives no global control on
reuse of an absent slot or a mixed corner among different cubes, and no
global energy estimate is claimed.
