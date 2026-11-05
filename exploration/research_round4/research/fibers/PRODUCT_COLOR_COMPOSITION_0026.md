# Product color composition: an exact binary lifting criterion

## 1. No-carry binary product

Let \(B\subset\mathbb Z\) be finite, let \(S=\operatorname{span}(B)\), and
choose \(Q>2S\). Put
\[
A=B+Q\{0,1\}.
\]
Write a source mark as \((b,\varepsilon)\), meaning \(b+Q\varepsilon\).
The no-carry hypothesis has two consequences.

First, the numerical order is lexicographic in \(\varepsilon\). Second, equality
of two source differences implies equality of both coordinate differences:
\[
(b'-b)+Q(\varepsilon'-\varepsilon)
=(c'-c)+Q(\eta'-\eta)
\]
forces
\[
b'-b=c'-c,
\qquad
\varepsilon'-\varepsilon=\eta'-\eta.
\tag{1}
\]
Thus a positive difference has exactly one of two types:
\[
(\delta,0),\quad \delta>0,
\qquad\text{or}\qquad
(\delta,1),\quad \delta\in\mathbb Z.
\]
The signed values \(\delta<0\) in the second type are essential; they are the
inverse-orientation mixed corners that a strict coloring of \(V(B)\) does not
control.

## 2. Exact composition criterion

Let \(\chi_0,\chi_1\) be two proper two-colorings of the strict triangle
\(V(B)\). Let
\[
g:B\times B\longrightarrow\{0,1\}
\]
be a coloring of the full directed cross matrix: \(g(y,x)\) is the color of
the cell from the lower-layer mark \((x,0)\) to the upper-layer mark
\((y,1)\). Define a coloring of \(V(A)\) by
\[
\chi((y,\varepsilon),(x,\varepsilon))=\chi_\varepsilon(y,x)
\quad(x<y),
\qquad
\chi((y,1),(x,0))=g(y,x).
\tag{2}
\]

**Binary lifting criterion.** The coloring (2) is proper if and only if the
following two families of conditions hold.

**Horizontal compatibility.** Whenever \(x,y\in B\), \(\delta>0\), and
\[
x,x+\delta,y,y+\delta\in B,
\]
one has
\[
\operatorname{NAE}\bigl(
\chi_0(x+\delta,x),
g(y+\delta,x),
\chi_1(y+\delta,y)
\bigr).
\tag{H}
\]

**Mixed directed compatibility.** Whenever \(x<y\), \(\delta\in\mathbb Z\),
and
\[
x,x+\delta,y,y+\delta\in B,
\]
one has
\[
\operatorname{NAE}\bigl(
g(x+\delta,x),
g(y+\delta,x),
g(y+\delta,y)
\bigr).
\tag{M}
\]

To prove the criterion, classify a corner by (1). For a difference
\((\delta,0)\), both representations lie in the same layer or one lies in
each layer. In the first case properness is exactly that of \(\chi_0\) or
\(\chi_1\). In the second case numerical order places the lower-layer start
first regardless of the relative order of its base coordinate \(x\) and the
upper-layer base coordinate \(y\); the three cells are precisely those in
(H). Thus (H) genuinely requires all \(x,y\), including \(x=y\) and \(x>y\).
For a difference \((\delta,1)\), both endpoint cells and their completion are
cross-layer cells, and their colors are exactly the three entries in (M).
There are no other corner types. This proves both necessity and sufficiency.

Condition (M) is stronger than a proper strict coloring of \(B\). It includes
\(\delta=0\), positive \(\delta\), and negative \(\delta\), and the completion
\(g(y+\delta,x)\) has no reason to lie in the strict half of the matrix. This
is the precise extra object needed to iterate a no-carry product.

## 3. Exact energy amplification

Let
\[
m=|B|,
\qquad
M=\binom m2,
\qquad
T(B)=\sum_{d>0}\binom{r_B(d)}2.
\]
The difference fibers in the binary product are explicit.

- A horizontal difference \((d,0)\), \(d>0\), has size \(2r_B(d)\).
- The mixed difference \((0,1)\) has size \(m\).
- For every \(d>0\), the two mixed differences \((d,1)\) and \((-d,1)\)
  each have size \(r_B(d)\).

Therefore
\[
\begin{aligned}
T(A)
&=\sum_{d>0}\binom{2r_B(d)}2
  +\binom m2
  +2\sum_{d>0}\binom{r_B(d)}2\\
&=6T(B)+2M,
\tag{3}
\end{aligned}
\]
while
\[
|A|=2m,
\qquad
\binom{|A|}{2}=4M+m.
\tag{4}
\]
Thus an indefinitely iterable solution of (H)--(M) would make normalized
energy grow roughly by the recurrence
\[
\frac{T(A)}{\binom{|A|}{2}}
\sim \frac32\frac{T(B)}{M}+\frac12.
\]
Repeated binary products would consequently give unbounded normalized energy.
The issue is entirely whether the directed cross-matrix extensions continue
to exist.

## 4. The affine Boolean rule and its dimension-three ceiling

The separated Boolean cube gives a clean test of the criterion. Let
\[
B_r=\left\{\sum_{i=1}^r x_iw_i:x\in\{0,1\}^r\right\},
\]
with coordinatewise uniqueness of differences. Consider the endpoint-linear
color rule
\[
\chi(y,x)=\alpha\mathbin{\cdot}x+\beta\mathbin{\cdot}y
\pmod2,
\qquad \alpha,\beta\in\mathbb F_2^r.
\tag{5}
\]

For a corner, let \(s\in\mathbb F_2^r\) be the support vector of its common
signed coordinate step. If its three colors are \(C_0,C_1,C_2\), direct
cancellation gives
\[
C_0+C_1=\beta\cdot s,
\qquad
C_1+C_2=\alpha\cdot s.
\tag{6}
\]
Every nonzero support except \({\bf1}=(1,\ldots,1)\) occurs in a corner: a
coordinate outside the support may be changed to obtain two distinct starts,
and the signs on the support may be chosen so the common numerical step is
positive. The full support \({\bf1}\) has only one possible start for each
choice of signs and therefore produces no corner.

It follows that (5) is proper exactly when
\[
\ker\alpha\cap\ker\beta\subseteq\{0,{\bf1}\}.
\tag{7}
\]
For \(r=3\), one may take
\[
\alpha=(1,0,1),
\qquad
\beta=(1,1,0),
\]
whose common kernel is \(\{000,111\}\). This recovers the explicit proper
three-factor rule
\[
\chi(y,x)=x_1+x_3+y_1+y_2\pmod2.
\]

For \(r\ge4\), the common kernel of two linear forms has dimension at least
\(r-2\ge2\). It contains at least three nonzero vectors, while only one vector
has full support. Hence it contains a nonzero proper-support vector \(s\), and
(6) gives a monochromatic corner. Therefore no endpoint-linear rule of the
form (5) can color a separated Boolean product in four or more dimensions.

This is an obstruction to the natural affine product composition, not an
obstruction to every nonlinear coloring of the four-dimensional cube. In the
language of the lifting criterion, two affine parity checks can distinguish
all realizable step supports through dimension three, but from dimension four
onward some proper support is invisible to both. A nonlinear solution of
(H)--(M), if one exists, would need to use more than the support parities that
make the three-factor construction work.

## 5. Scope

Equations (H) and (M) give a complete color-composition rule for adjoining one
binary no-carry factor, and (3) gives its exact energy effect. They identify a
route to unbounded energy and the precise additional matrix coloring it
requires. The affine specialization proves that the simplest iterated rule
stops after three binary factors. No conclusion here rules out a nonlinear
four-factor coloring or a product rule using a larger factor and additional
state.
