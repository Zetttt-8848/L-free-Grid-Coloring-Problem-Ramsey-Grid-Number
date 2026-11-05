# A uniform coloring of the weight-two layer

**Status:** proved under the stated coordinatewise dissociation hypothesis.
This note treats only the weight-two layer.

## Statement

Let

\[
W(X)=\sum_{i\in X}w_i
\qquad
\left(X\in\binom{[r]}2\right),
\]

where \(r\ge3\),

\[
0<w_1<w_2<\cdots<w_r
\]

and assume the following dissociation property:

\[
W(Y)-W(X)=W(Y')-W(X')
\quad\Longrightarrow\quad
\mathbf 1_Y-\mathbf 1_X
=
\mathbf 1_{Y'}-\mathbf 1_{X'}
\tag{D}
\]

for all weight-two sets \(X,Y,X',Y'\).  The choice \(w_i=5^i\)
satisfies (D).  Put

\[
A=\left\{W(X):X\in\binom{[r]}2\right\}.
\]

Property (D) also makes \(W\) injective: compare a zero difference
\(W(Y)-W(X)=0\) with \(W(X)-W(X)\).  Thus every cell has a unique
pair of set labels, and \(|A|=\binom r2\).

For a cell \((W(Y),W(X))\in V(A)\), color it by

\[
\boxed{
\chi(W(Y),W(X))
=
\begin{cases}
0,&X\cap Y\ne\varnothing,\\
1,&X\cap Y=\varnothing.
\end{cases}}
\tag{1}
\]

Then \(\chi\) is a proper two-coloring of the strict source triangle
\(V(A)=\{(v,u):u,v\in A,\ u<v\}\).

## Classification of the difference fibers

Consider a positive source difference

\[
d=W(Y)-W(X)>0.
\]

Write

\[
P=Y\setminus X,
\qquad
N=X\setminus Y.
\]

Because \(X\) and \(Y\) both have size two,

\[
|P|=|N|\in\{1,2\}.
\tag{2}
\]

Property (D) says that every other representation of \(d\) has exactly
the same positive support \(P\) and negative support \(N\).

If \(|P|=|N|=2\), then \(X=N\) and \(Y=P\).  Thus the difference has
one representation and its fiber has size one.  It cannot produce a
corner.

Suppose instead that

\[
P=\{p\},
\qquad
N=\{n\}.
\]

Every representation must then have the form

\[
X_t=\{n,t\},
\qquad
Y_t=\{p,t\},
\qquad
t\in[r]\setminus\{n,p\}.
\tag{3}
\]

Conversely, every \(t\) in (3) gives a representation of the same
difference

\[
d=w_p-w_n.
\]

Since the weights are strictly increasing, positivity is equivalent to
\(n<p\).  Therefore, for every \(n<p\), the difference \(w_p-w_n\)
has the exact fiber

\[
F_{n,p}
=
\left\{
\bigl(W(Y_t),W(X_t)\bigr):
t\in[r]\setminus\{n,p\}
\right\},
\qquad
|F_{n,p}|=r-2.
\tag{4}
\]

These \(\binom r2\) exchange fibers include all the repeated fibers
(their size is one when \(r=3\)).  The
differences arising from disjoint \(X,Y\) are singleton fibers; there
are \(3\binom r4\) of them.  In particular, the exact number of corners
is

\[
T
=
\binom r2\binom{r-2}{2}
=
6\binom r4.
\tag{5}
\]

## Color of every corner

Fix \(n<p\), and take two distinct representations from (4), indexed
by \(t\) and \(s\).  Relabel them so that \(t<s\).  Since the two lower
marks have the common summand \(w_n\),

\[
W(X_t)<W(X_s),
\]

and the corresponding upper marks have the common summand \(w_p\), so
also

\[
W(Y_t)<W(Y_s).
\]

The corner determined by these two representations consists of

\[
\bigl(W(Y_t),W(X_t)\bigr),
\qquad
\bigl(W(Y_s),W(X_t)\bigr),
\qquad
\bigl(W(Y_s),W(X_s)\bigr).
\tag{6}
\]

The first and third cells in (6) join

\[
X_t=\{n,t\}\ \text{to}\ Y_t=\{p,t\},
\qquad
X_s=\{n,s\}\ \text{to}\ Y_s=\{p,s\}.
\]

Each pair has a common coordinate, so both cells have color \(0\).
The completion cell joins

\[
X_t=\{n,t\}
\quad\text{to}\quad
Y_s=\{p,s\}.
\]

The four indices \(n,p,t,s\) are distinct, hence
\(X_t\cap Y_s=\varnothing\), and this cell has color \(1\).  Every
corner consequently has the pattern

\[
(0,1,0).
\tag{7}
\]

It is therefore nonmonochromatic.  The fiber classification proves
that (6) exhausts all corners, which proves the claim.

## Why powers of five meet the hypothesis

For \(w_i=5^i\), equality of two source differences gives

\[
\sum_i c_i5^i=0
\qquad\text{with}\qquad
c_i\in\{-2,-1,0,1,2\},
\]

where \(c_i\) is the difference between the two signed incidence
vectors.  If \(k\) were the largest index with \(c_k\ne0\), then

\[
|c_k|5^k
\ge 5^k
>
2\sum_{i<k}5^i,
\]

which is impossible.  Hence all \(c_i\) vanish, proving (D).

## Scope

Write \(m=\binom r2\) and \(M=\binom m2\).  From (5),

\[
\frac{T}{M}
=\frac{(r-2)(r-3)}{\binom r2-1}
=\frac{2(r-3)}{r+1}
=2-\frac8{r+1}.
\tag{8}
\]

The cancellation uses
\(\binom r2-1=(r-2)(r+1)/2\), and \(r\ge3\) keeps the
denominator positive.  The ratio tends to two from below.
Consequently, any constant \(\kappa\) valid in the universal
two-color source-energy hypothesis
\(T(A)\le\kappa\binom{|A|}{2}\) must satisfy \(\kappa\ge2\).
For every \(\kappa<2\), choosing \(r+1>8/(2-\kappa)\) gives
an explicit counterexample.  This strengthens the earlier finite
lower constraint \(\kappa\ge26/15\).  It does not prove the
upper hypothesis at \(\kappa=2\) or at \(\kappa=5\).

The construction uses only the weight-two representation and the
coordinatewise uniqueness in (D).  It gives a uniform proper coloring
for arbitrary \(r\), but makes no assertion about higher weight layers
or arbitrary nondissociated weights.
