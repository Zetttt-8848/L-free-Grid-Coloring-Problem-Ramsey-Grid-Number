# Probe of the square source

**Status:** one natural uniform coloring class is excluded by a short
five-mark pattern.  No finite obstruction to arbitrary two-coloring, and
no uniform coloring for all \(m\), is proved here.

## 1. Corner notation and exact fiber count

Let

\[
A_m=\{1^2,2^2,\ldots,m^2\}.
\]

Write \((j,i)\) for the cell \((j^2,i^2)\), where
\(1\le i<j\le m\).  For a positive integer \(d\), define

\[
\mathcal F_m(d)
=
\{(j,i):1\le i<j\le m,\ j^2-i^2=d\},
\qquad
r_m(d)=|\mathcal F_m(d)|.
\tag{1}
\]

If \((j,i),(l,k)\in\mathcal F_m(d)\) and \(i<k\), then necessarily
\(j<l\), and the associated corner is

\[
(j,i),\qquad(l,i),\qquad(l,k).
\tag{2}
\]

Thus

\[
M_m=\binom m2,
\qquad
T_m=\sum_{d>0}\binom{r_m(d)}2.
\tag{3}
\]

The multiplicities in (1) can be obtained without searching over
quadruples.  Factoring

\[
d=j^2-i^2=(j-i)(j+i)=uv
\]

shows that \(r_m(d)\) is exactly the number of factor pairs \(uv=d\)
satisfying

\[
u<v,\qquad u\equiv v\pmod 2,\qquad u+v\le 2m.
\tag{4}
\]

Indeed, the inverse map is

\[
j=\frac{u+v}{2},
\qquad
i=\frac{v-u}{2}.
\]

## 2. A five-mark obstruction to every difference-only coloring

Consider the five source marks indexed by

\[
\{1,7,11,13,17\}.
\]

They contain the following three equal-difference pairs:

\[
\begin{aligned}
11^2-1^2&=13^2-7^2=120,\\
11^2-1^2&=17^2-13^2=120,\\
13^2-1^2&=17^2-11^2=168.
\end{aligned}
\tag{5}
\]

Suppose a cell coloring depends only on its source difference, so that

\[
\chi(j,i)=f(j^2-i^2)
\qquad
\text{for some }f:\mathbb Z_{>0}\to\{0,1\}.
\tag{6}
\]

The first equality in (5) gives the corner

\[
(11,1),\qquad(13,1),\qquad(13,7),
\]

whose colors are

\[
f(120),\qquad f(168),\qquad f(120).
\]

Properness therefore requires

\[
f(120)\ne f(168).
\tag{7}
\]

The second equality in (5) gives

\[
(11,1),\qquad(17,1),\qquad(17,13),
\]

with colors

\[
f(120),\qquad f(288),\qquad f(120),
\]

and hence

\[
f(120)\ne f(288).
\tag{8}
\]

Finally, the third equality in (5) gives

\[
(13,1),\qquad(17,1),\qquad(17,11),
\]

with colors

\[
f(168),\qquad f(288),\qquad f(168),
\]

so

\[
f(168)\ne f(288).
\tag{9}
\]

Equations (7)--(9) demand three pairwise distinct values from a
two-element color set, which is impossible.

Consequently, for every \(m\ge17\), no proper coloring of \(T(A_m)\)
can be a function only of \(j^2-i^2\).  Equivalently, the graph whose
vertices are source differences and whose edges join a corner's
repeated difference to its completion difference already contains the
triangle

\[
120\mathbin{-}168\mathbin{-}288\mathbin{-}120.
\tag{10}
\]

This excludes in one step all difference-only parity, valuation,
factor-count, and fiber-multiplicity rules.  It does not exclude
colorings that distinguish different cells in the same difference
fiber.

## 3. Bounded general-coloring probe

For discovery, assign one Boolean variable \(x_{j,i}\) to every cell.
For every equality

\[
j^2-i^2=l^2-k^2,
\qquad i<k,
\]

impose the two clauses

\[
(x_{j,i}\vee x_{l,i}\vee x_{l,k})
\quad\text{and}\quad
(\neg x_{j,i}\vee\neg x_{l,i}\vee\neg x_{l,k}).
\tag{11}
\]

These are exactly the conditions that the corner (2) is not
monochromatic.

The terminal bounded probe used \(m=200\).  Exact enumeration by
(1)--(4) gives

\[
M_{200}=\binom{200}{2}=19900,
\qquad
T_{200}=17588,
\qquad
\frac{T_{200}}{M_{200}}
=
\frac{4397}{4975}.
\tag{12}
\]

The Boolean instance (11), with 19,900 cell variables and 17,588
corner constraints, returned satisfiable.  This is bounded discovery
evidence only.  In particular, the initial square source through
\(200^2\) supplied no forced monochromatic corner.

## 4. Exact remaining question

The five-mark calculation proves that any uniform construction must
use more information than the numerical source difference.  The
bounded satisfiable instance shows that this obstruction does not
extend directly to unrestricted cell colorings.

What remains unresolved is whether \(T(A_m)\) admits a proper
two-coloring for every \(m\), or whether some larger finite square
source is uncolorable.  No asymptotic estimate for \(T_m/M_m\) is
claimed here, so this probe by itself neither proves nor refutes a
uniform source-energy inequality.
