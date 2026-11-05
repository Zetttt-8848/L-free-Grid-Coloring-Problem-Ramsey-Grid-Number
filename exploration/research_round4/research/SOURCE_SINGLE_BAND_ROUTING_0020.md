# Single-band completion routing and strict scale descent (checkpoint 0020)

Let \(A\) be a finite integer source, let
\[
M=\binom{|A|}{2},
\qquad
F_d=\{x:x,x+d\in A\},
\qquad
r_d=|F_d|,
\]
and suppose that \(V(A)\) has a proper coloring
\(z:V(A)\to\{-1,+1\}\). Fix
\[
I_H=\{d:H\le d<2H\}.
\]
The band energy is
\[
T_H=\sum_{d\in I_H}\binom{r_d}{2}. \tag{1}
\]
Write \(F_d^\pm\) for the two actual color classes in the offset-\(d\)
fiber, and set
\[
A_H=
\sum_{d\in I_H}
\left[
\binom{|F_d^+|}{2}+\binom{|F_d^-|}{2}
\right],
\qquad
R_H=\sum_{d\in I_H}r_d. \tag{2}
\]
Thus \(A_H\) counts active-band corners whose two offset-\(d\) endpoint
cells have the same color.

## 1. Reduction to monochromatic completion fans

If \(r_d=a_d+b_d\), where \(a_d=|F_d^+|\) and \(b_d=|F_d^-|\), then
\[
\begin{aligned}
a_db_d-
\left[\binom{a_d}{2}+\binom{b_d}{2}\right]
 &=\frac{r_d-(a_d-b_d)^2}{2}\\
 &\le\frac{r_d}{2}.
\end{aligned}
\]
Since \(\binom{r_d}{2}\) is the sum of the monochromatic and bichromatic
endpoint-pair counts,
\[
\boxed{
T_H\le 2A_H+\frac{R_H}{2}.
} \tag{3}
\]
Also \(R_H\le M\). Hence the coefficient-one goal \(T_H\le M\) would
follow from a sufficiently strong bound on the monochromatic part
\(A_H\); signed-fiber Golombness by itself does not give a constant
bound for its sum over the band.

For an outer cell \(Q=(v,u)\), let \(D_Q\subseteq I_H\) consist of the
offsets \(d\) for which
\[
S_d=(u+d,u),\qquad T_d=(v,v-d) \tag{4}
\]
exist and have the same color. These cells and \(Q\) form an original
corner, so all such endpoint pairs have color \(-z(Q)\). Put
\[
H_Q=|D_Q|.
\]
Every monochromatic pair in an active fiber has a unique completion,
giving the exact identity
\[
A_H=\sum_Q H_Q. \tag{5}
\]
Since there are \(M\) possible outer cells, Cauchy--Schwarz gives
\[
\boxed{
\sum_Q\binom{H_Q}{2}
\ge
\frac12\left(\frac{A_H^2}{M}-A_H\right).
} \tag{6}
\]

## 2. A collision descends below the active scale

Fix \(d<e\) in \(D_Q\) and put
\[
\delta=e-d.
\]
The dyadic geometry gives the strict separation
\[
1\le\delta<H,\qquad d+e\ge2H. \tag{7}
\]
All four cells \(S_d,S_e,T_d,T_e\) have one sign, say \(s=-z(Q)\).

If \(u+\delta\in A\), then
\[
(u+d,u),\qquad (u+e,u),\qquad (u+e,u+\delta) \tag{8}
\]
is an original corner of step \(\delta\). Its first two cells have sign
\(s\), so the last cell has sign \(-s\). The first and last cells in
(8) both have offset \(d\), with starts \(u,u+\delta\). Thus the
completion collision creates a bichromatic pair at gap \(\delta<H\)
inside the active fiber \(F_d\).

If instead \(v-\delta\in A\), the corner
\[
(v-\delta,v-e),\qquad (v,v-e),\qquad (v,v-d) \tag{9}
\]
gives the same conclusion in \(F_d\), with starts \(v-e,v-d\).

This proves the following band-specific forcing rule.

**Strict descent lemma.** Two monochromatic endpoint pairs of active
offsets \(d<e\) that share their completion \(Q=(v,u)\) force a
bichromatic pair in \(F_d\) at the lower gap \(e-d<H\), provided at
least one of
\[
u+(e-d),\qquad v-(e-d) \tag{10}
\]
belongs to \(A\). Every corner used has the original positive
orientation.

## 3. Aggregate second-moment inequality

Define the lower-gap bichromatic energy in the active fibers by
\[
\mathcal B_H^{<H}
=
\sum_{d\in I_H}
\ \sum_{\substack{\{x,y\}\subset F_d\\
                   z(x+d,x)\ne z(y+d,y)\\
                   |x-y|<H}}
r_A(|x-y|). \tag{11}
\]
Charge a supported pair \(d<e\) in one completion fan through the left
corner (8) when possible, and otherwise through (9).

A fixed bichromatic target pair at gap \(\delta\) receives at most
\(r_A(\delta)\) left charges. In the left case its two starts determine
\(u,d,e\), while the remaining reflected source pair
\(v-e,v-d\) is one of the \(r_A(\delta)\) pairs of gap \(\delta\).
The right case is symmetric and contributes at most another
\(r_A(\delta)\) charges. No disjointness between the two source-fan
orientations is asserted, so the safe combined multiplicity is
\(2r_A(\delta)\).

If neither mark in (10) belongs to \(A\), then \(u\) is one of the
\(|A|-r_A(\delta)\) marks lacking a forward \(\delta\)-translate, and
\(v\) is one of the same number lacking a backward translate. Once
\(u,v\) and the pair \(u+d,u+e\) are chosen, the fan collision is
determined. Dropping the remaining restrictions gives at most
\[
r_A(\delta)\bigl(|A|-r_A(\delta)\bigr)^2 \tag{12}
\]
unsupported collisions of gap \(\delta\).

Summing the supported and unsupported cases, then using (6), yields
\[
\boxed{
\frac12\left(\frac{A_H^2}{M}-A_H\right)
\le
2\mathcal B_H^{<H}
+
\sum_{1\le\delta<H}
r_A(\delta)\bigl(|A|-r_A(\delta)\bigr)^2.
} \tag{13}
\]
This is a genuine scale descent: the left side measures crowded
monochromatic completions from offsets in \([H,2H)\), while every
color-sensitive term on the right has pair gap below \(H\).

For a scalar version, let
\[
R_{<H}^{\max}=\max_{1\le\delta<H}r_A(\delta).
\]
The number of bichromatic pairs in the active fibers is \(T_H-A_H\), so
\[
\mathcal B_H^{<H}
\le R_{<H}^{\max}(T_H-A_H). \tag{14}
\]
Consequently
\[
\boxed{
\frac12\left(\frac{A_H^2}{M}-A_H\right)
\le
2R_{<H}^{\max}(T_H-A_H)
+
\sum_{\delta<H}r_\delta(|A|-r_\delta)^2.
} \tag{15}
\]
Equations (3) and (13) are an explicit route by which lower-scale
information could control one active band.

## 4. Why sum/difference separation alone is insufficient

When four source marks have the parallelogram form
\[
x,\qquad x+d,\qquad x+e,\qquad x+d+e,
\qquad d<e,
\]
the two source corners have active offsets \(d,e\). Their common outer
cell has offset \(d+e\ge2H\), while the inner cross cell has offset
\(e-d<H\). Thus both auxiliary cells lie outside the active band.

However, the inner cell occurs in neither of the two mandatory corner
constraints. This is not merely a formal concern. For every \(H\ge2\),
take
\[
A_H^{(4)}=\{0,H,2H-1,3H-1\}. \tag{16}
\]
Its only repeated positive differences are
\[
H\quad\text{and}\quad 2H-1,
\]
both in \(I_H\). Color the four side cells
\[
(H,0),\quad(2H-1,0),\quad
(3H-1,H),\quad(3H-1,2H-1)
\]
with \(+1\), color the common outer cell
\[
(3H-1,0)
\]
with \(-1\), and color the remaining inner cell
\[
(2H-1,H)
\]
arbitrarily. The two repeated-difference corners are both
nonmonochromatic, and there are no others, so this is a proper coloring
of the full source triangle.

Here
\[
\delta=H-1,\qquad
0+\delta=H-1\notin A_H^{(4)},\qquad
(3H-1)-\delta=2H\notin A_H^{(4)}. \tag{17}
\]
Both active corners have monochromatic endpoint pairs and collide at the
same outer completion, yet neither descent corner (8)--(9) is supported.
The inner cell of offset \(H-1\) remains completely free.

This four-mark family shows the exact limitation of a bare
sum/difference charge. The strict separation (7) localizes every
supported collision outside the active scale, but it does not supply the
missing translated marks needed to invoke properness. Inequality (13)
therefore stops at the explicit unsupported-shift term. Eliminating or
amortizing that term requires a further whole-source argument; the
single-band route here does not prove \(T_H\le M\).

The factor \(2\) in (13) and (15) is deliberate: the left-closure and
right-closure charge families have separate \(r_A(\delta)\) multiplicity
bounds, and a fixed unordered bichromatic target may receive charges from
both families.
