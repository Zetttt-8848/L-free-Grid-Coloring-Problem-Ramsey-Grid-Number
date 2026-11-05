# Binary-strip proper colorings with unbounded Cartesian energy (checkpoint 0017)

For a finite integer set \(S\), write
\[
r_S(h)=|\{s\in S:s+h\in S\}|,\qquad h>0,
\]
and for finite \(B,C\) put
\[
U(B,C)=\sum_{h>0}r_B(h)r_C(h).
\]
An original positive corner in \(B\times C\) has the form
\[
(x,c),\qquad (x+h,c),\qquad (x+h,c+h),
\qquad h>0.
\]

## Infinite proper binary strip

For \(m\ge1\), let
\[
C_m=\{c_j=2^j-1:0\le j<m\}.
\]
For every integer \(x\), define its \(j\)-th binary digit by
\[
\beta_j(x)=\left\lfloor\frac{x}{2^j}\right\rfloor\pmod 2.
\]
This definition works uniformly for positive and negative integers.

Color the infinite strip \(\mathbb Z\times C_m\) by
\[
z(x,c_j)=\beta_j(x). \tag{1}
\]
More generally, (1) is needed only for \(0\le j<m-1\); the last column \(c_{m-1}\) may be colored arbitrarily.

**Binary-strip theorem.** The coloring (1), with an arbitrary last column if desired, has no monochromatic original positive corner.

To prove this, take columns \(c_j<c_k\). Their gap is
\[
h=c_k-c_j=2^k-2^j
  =2^j(2^{k-j}-1). \tag{2}
\]
The multiplier \(2^{k-j}-1\) is odd. Since \(h/2^j\) is an integer,
\[
\left\lfloor\frac{x+h}{2^j}\right\rfloor
=\left\lfloor\frac{x}{2^j}\right\rfloor+\frac{h}{2^j},
\]
and reduction modulo \(2\) gives
\[
\beta_j(x+h)=1-\beta_j(x). \tag{3}
\]
Thus the first two cells of every possible corner, \((x,c_j)\) and \((x+h,c_j)\), already have opposite colors. The color at \((x+h,c_k)\) is irrelevant. This also explains why the last column can be arbitrary: it is never the lower-index column of a pair.

Restricting the row coordinate to any \(B\subset\mathbb Z\) preserves properness.

## Exact Cartesian energy on an interval

Take
\[
B_N=\{0,1,\ldots,N-1\},\qquad
N>2^{m-1}-1.
\]
Every positive difference of \(C_m\) is smaller than \(N\). Moreover, all these differences are distinct: in (2), the \(2\)-adic valuation determines \(j\), and then the odd part \(2^{k-j}-1\) determines \(k-j\). Hence
\[
r_{C_m}(2^k-2^j)=1\qquad(0\le j<k<m)
\]
and there are no other positive differences. Since
\[
r_{B_N}(h)=N-h\qquad(0<h<N),
\]
we obtain
\[
U(B_N,C_m)
=\binom m2N-\sum_{0\le j<k<m}(2^k-2^j). \tag{4}
\]

The remaining sum has the closed form
\[
\begin{aligned}
\sum_{j<k}(2^k-2^j)
 &=\sum_{k=1}^{m-1}k2^k
   -\sum_{j=0}^{m-2}(m-1-j)2^j\\
 &=\bigl((m-2)2^m+2\bigr)
   -\bigl(2^m-m-1\bigr)\\
 &=(m-3)2^m+m+3. \tag{5}
\end{aligned}
\]
Therefore
\[
\boxed{
U(B_N,C_m)
=\binom m2N-\bigl((m-3)2^m+m+3\bigr).
} \tag{6}
\]
After normalizing by the number \(Nm\) of cells,
\[
\frac{U(B_N,C_m)}{Nm}
=\frac{m-1}{2}
 -\frac{(m-3)2^m+m+3}{Nm}. \tag{7}
\]
For each fixed \(m\), the right side tends to \((m-1)/2\) as \(N\to\infty\). Letting \(m\) grow shows that no absolute bound
\[
U(B,C)\le K|B||C|
\]
can hold for all standalone properly two-colored Cartesian rectangles.

## Equal-cardinality extension

The same conclusion holds with \(|B|=|C|\). Choose \(N\) divisible by \(m\), put
\[
q=N/m,
\]
and choose an integer
\[
H>\operatorname{span}(B_N)+\operatorname{span}(C_m)
  =(N-1)+(2^{m-1}-1).
\]
Form \(q\) translated column blocks
\[
C'=\bigcup_{t=0}^{q-1}(tH+C_m). \tag{8}
\]
They are disjoint and
\[
|C'|=qm=N=|B_N|.
\]

Repeat the strip coloring on every block:
\[
z(x,tH+c_j)=\beta_j(x), \tag{9}
\]
again allowing each last column \(tH+c_{m-1}\) to be arbitrary. Corners whose columns lie in one block are nonmonochromatic by (3). If two columns lie in different blocks, their positive gap is at least
\[
H-\operatorname{span}(C_m)>\operatorname{span}(B_N),
\]
so it cannot equal a row difference of \(B_N\). Hence no cross-block corner exists, and (9) is proper on \(B_N\times C'\).

Only within-block column differences can contribute to \(U(B_N,C')\). Each difference of \(C_m\) occurs once in each of the \(q\) blocks, so
\[
U(B_N,C')=q\,U(B_N,C_m). \tag{10}
\]
Using \(q=N/m\) and (6),
\[
\boxed{
\frac{U(B_N,C')}{|B_N||C'|}
=\frac{m-1}{2}
 -\frac{(m-3)2^m+m+3}{Nm}.
} \tag{11}
\]
Thus the normalized energy remains unbounded even among proper Cartesian rectangles with equal row and column cardinalities.

This construction concerns standalone Cartesian properness. The interval \(B_N\) contains long arithmetic configurations and does not itself supply a properly colored strict source triangle. Consequently, the construction does not refute the \(S_{11}\) source statement; it shows that any useful Cartesian energy bound must exploit additional source-specific structure.
