# Reflection closure on a completion ladder

This note extracts one parametric consequence of the supported reflected
triangle identities.  It applies to an arbitrary finite integer source and
uses only original positive-step corners.  It is independent of the completed
eight-mark obstruction.

## 1. Completion ladders

Let `A` be a finite subset of the integers, and suppose its strict source
triangle has a proper two-coloring.  For a pair of cells `p,q`, let

\[
X(p,q)=\frac{1+z_pz_q}{2}\in\{0,1\}
\tag{1}
\]

be the indicator that they have the same color.

Fix positive integers `d,h`, and define the set of supported starts

\[
G=\{x:x,x+h,x+d,x+d+h\in A\}.
\tag{2}
\]

Equivalently, if `F_d={x:x,x+d in A}`, then
`G=F_d intersect (F_d-h)`.  For `x in G`, put

\[
L_x=(x+d,x),\qquad
Q_x=(x+d+h,x),\qquad
R_x=(x+d+h,x+h)=L_{x+h}.
\tag{3}
\]

The three cells `L_x,Q_x,L_{x+h}` form the original positive corner at
start `x`, of step `h`.

Decompose `G` into its maximal `h`-runs.  Consider one run

\[
x_k=x_0+kh\in G,\qquad 0\le k<r,
\tag{4}
\]

where neither `x_0-h` nor `x_r=x_0+rh` belongs to `G`.  Membership of
`x_{r-1}` in `G` still guarantees that the cell `L_{x_r}` exists.
Abbreviate

\[
L_k=L_{x_k}\quad(0\le k\le r),
\qquad Q_k=Q_{x_k}\quad(0\le k<r).
\tag{5}
\]

## 2. The reflected triples follow from positive corners

For every `0<=k<r-1`, the six marks

\[
x_k,x_k+h,x_k+2h,
x_k+d,x_k+d+h,x_k+d+2h
\tag{6}
\]

belong to `A`, because both `x_k` and `x_{k+1}` lie in `G`.  The cells

\[
Q_k,quad L_{k+1},quad Q_{k+1}
\tag{7}
\]

are therefore nonmonochromatic.

Here is a derivation using only the original orientation.  If the three
cells in (7) all had sign `s`, then the original corners

\[
(L_k,Q_k,L_{k+1}),qquad
(L_{k+1},Q_{k+1},L_{k+2})
\]

would force `L_k` and `L_{k+2}` to sign `-s`.  These two offset-`d`
cells are the outer cells of the positive corner

\[
L_k,quad Z=(x_k+d+2h,x_k),quad L_{k+2},
\]

whose step is `2h`; hence they force `Z` to sign `s`.  On the other hand,
the same-colored offset-`d+h` cells `Q_k,Q_{k+1}` are the outer cells of
the positive corner

\[
Q_k,quad Z,quad Q_{k+1},
\]

of step `h`, and force `Z` to sign `-s`.  This contradiction proves (7).
Every step used here is a positive integer, and (6) supplies every source
endpoint.

Consequently both families have exact NAE identities:

\[
\begin{aligned}
&X(L_k,Q_k)+X(Q_k,L_{k+1})+X(L_k,L_{k+1})=1,
&&0\le k<r,\\
&X(Q_k,L_{k+1})+X(L_{k+1},Q_{k+1})+X(Q_k,Q_{k+1})=1,
&&0\le k<r-1.
\end{aligned}
\tag{8}
\]

## 3. Exact reflection-closure balance

Define

\[
\begin{array}{ll}
c_k=X(L_k,Q_k),&u_k=X(Q_k,L_{k+1}),\\
a_k=X(L_k,L_{k+1}),&b_k=X(Q_k,Q_{k+1}).
\end{array}
\tag{9}
\]

Summing the first line of (8) over `0<=k<r`, summing the second over
`0<=k<r-1`, and subtracting cancels every internal `c` and `u` term.
This gives the following reusable theorem.

**Reflection-closure balance theorem.**  On every maximal `h`-run (4),

\[
\boxed{
\sum_{k=0}^{r-1}a_k-
\sum_{k=0}^{r-2}b_k
=1-c_0-u_{r-1}.}
\tag{10}
\]

In particular,

\[
\left|
\sum_{k=0}^{r-1}X(L_k,L_{k+1})-
\sum_{k=0}^{r-2}X(Q_k,Q_{k+1})
\right|\le1.
\tag{11}
\]

Thus the numbers of equal-color `h`-neighbor pairs on the two parallel
cell lines of offsets `d` and `d+h` cannot vary independently.  Their
discrepancy is exactly a two-ended boundary term.

The equivalent sign-product identity is

\[
\sum_{k=0}^{r-1}z_{L_k}z_{L_{k+1}}
-\sum_{k=0}^{r-2}z_{Q_k}z_{Q_{k+1}}
+z_{L_0}z_{Q_0}+z_{Q_{r-1}}z_{L_r}=-1.
\tag{12}
\]

For the whole supported-start set `G`, let `rho_h(G)` be its number of
maximal `h`-runs.  Summing (10) over the runs gives the immediate global
form

\[
\left|A_{d,h}(G)-B_{d+h,h}(G)\right|\le \rho_h(G),
\tag{13}
\]

where

\[
\begin{aligned}
A_{d,h}(G)
 &=\sum_{x\in G}X\bigl((x+d,x),(x+d+h,x+h)\bigr),\\
B_{d+h,h}(G)
 &=\sum_{\substack{x\in G\\x+h\in G}}
 X\bigl((x+d+h,x),(x+d+2h,x+h)\bigr).
\end{aligned}
\tag{14}
\]

This is a coupling between two source-difference fibers.  Separate Golomb
caps bound the two quantities individually; (10)--(13) retain their relative
position and force their counts to track one another along every supported
run.

## 4. Exact weighted path closure

There is a second, weighted form of the same closure.  The first identity in
(8) gives

\[
c_k+u_k\le1,
\]

and the reflected identity gives

\[
u_k+c_{k+1}\le1.
\]

Therefore

\[
(c_0,u_0,c_1,u_1,\ldots,c_{r-1},u_{r-1})
\tag{15}
\]

is the incidence vector of an independent set in the path on `2r` vertices.
For arbitrary nonnegative weights `alpha_k,beta_k`, it follows that

\[
\boxed{
\sum_{k=0}^{r-1}(\alpha_kc_k+\beta_ku_k)
\le
\operatorname{MWIS}
 (\alpha_0,\beta_0,\alpha_1,\beta_1,\ldots,
   \alpha_{r-1},\beta_{r-1}),}
\tag{16}
\]

where `MWIS` is the maximum-weight independent-set value of the path in
the displayed order.  It has the elementary recurrence

\[
D_0=0,\qquad D_1=w_0,\qquad
D_{j+1}=\max(D_j,D_{j-1}+w_j),
\tag{17}
\]

for the path weights `w_0,...,w_{2r-1}`.

This path bound is exact for the abstract subsystem consisting of the original and
supported reflected ladder triangles.  Given any independent set in (15),
choose a sign for `L_0` and move through the alternating cell sequence

\[
L_0,Q_0,L_1,Q_1,\ldots,Q_{r-1},L_r,
\]

making consecutive signs equal exactly at the selected path vertices.
No two selected vertices are adjacent, so no consecutive triple is
monochromatic.  Hence every identity in (8) holds.

The weighted closure can be strictly stronger than minimizing the original
corners independently.  For example, give weight one to `u_{2j}` and
`c_{2j+1}` for every `j` with `2j+1<r`, and zero to the other variables.
Independent original-corner bounds permit both selected terms at every such
boundary.  Reflection closure gives

\[
u_{2j}+c_{2j+1}\le1,
\]

losing one unit at each of the `floor(r/2)` disjoint boundaries.  This shows
exactly what the reflected edges add to the independent-block relaxation.
Such a formal run occupies two parallel progressions and necessarily
satisfies

\[
d+rh\le \operatorname{span}(A).
\tag{18}
\]

For an actual properly colored source, the inherited weak-triangle AP5
exclusion is stronger: the run supplies the `r+1`-term progression
`x_0,...,x_r` inside `F_d`, so `r+1<=4`, or `r<=3`.  Hence the displayed
linear growth cannot occur within one actual run.  Any quantitative gain
must come from aggregating the boundary effects of many short runs.

## 5. Summation over all starts and all offsets

For fixed `d,h`, set

\[
\begin{aligned}
\operatorname{Beg}_{d,h}
 &=\{x\in G:x-h\notin G\},\\
\operatorname{End}_{d,h}
 &=\{x\in G:x+h\notin G\}.
\end{aligned}
\tag{19}
\]

The maximal runs partition `G`, with one beginning and one end per run.
Therefore (10) sums without loss to the exact boundary functional

\[
\boxed{
A_{d,h}(G)-B_{d+h,h}(G)
=|\operatorname{Beg}_{d,h}|
-\sum_{x\in\operatorname{Beg}_{d,h}}X(L_x,Q_x)
-\sum_{x\in\operatorname{End}_{d,h}}X(Q_x,L_{x+h}).}
\tag{20}
\]

This answers the first summation question: all interior switch terms cancel,
and only the two exposed switch pairs of each run remain.

There is also an exact sum over the offset `d`.  Write

\[
G_d=\{x:x,x+h,x+d,x+d+h\in A\},
\]

and let `mathcal B_{d,h}` denote the right side of (20).  Then

\[
\sum_{d>0}\left(A_{d,h}(G_d)-B_{d+h,h}(G_d)\right)
=\sum_{d>0}\mathcal B_{d,h}.
\tag{21}
\]

To see exactly whether the left side telescopes, define the physical
offset-`t` pair

\[
E_{t,h}(x)=X\bigl((x+t,x),(x+t+h,x+h)\bigr).
\]

Reindexing the negative sum in (21) from `d+h` to `t` gives

\[
\sum_{t>0}\sum_x
\left(
 \mathbf 1_{\{x\in G_t\}}
 -\mathbf 1_{\{t>h\}}
  \mathbf 1_{\{x,x+h\in G_{t-h}\}}
\right)E_{t,h}(x)
=\sum_{d>0}\mathcal B_{d,h}.
\tag{22}
\]

Thus there is no unconditional telescope across `d`.  The positive copy of
`E_{t,h}(x)` needs the four-mark rectangle

\[
x,x+h,x+t,x+t+h\in A,
\]

whereas its negative copy needs the six-mark support

\[
x,x+h,x+2h,x+t-h,x+t,x+t+h\in A.
\]

Neither support condition implies the other for an arbitrary source.  Formula
(22) isolates the residual coefficients that any source-wide summation must
control; replacing them by a formal cancellation would silently add missing
source marks.

## 6. Quantitative limitation and remaining implication

With unit weights on every `c_k,u_k`, the path in (16) has independence
number `r`.  This is exactly the sum of the independent original-corner
bounds `c_k+u_k<=1`; there is no unweighted gain.  The abstract ladder
subsystem admits arbitrary path lengths, but the actual source has `r<=3`
by the inherited AP5 exclusion noted after (18).  Reflection closure thus
gives a balance law for many short components, rather than a new long-run
cap or a source-size inequality in terms of span.

To obtain a span bound, one must combine (10) or (16) with the fact that the
same-color starts on each offset line are Golomb, and must account for the
reuse of physical cell pairs when different choices of `d,h` overlap.  The
precise missing quantitative step is a source-wide choice of nonnegative or
cancelling pair weights for which the accumulated boundary terms in (20),
with the unmatched supports in (22), or the path deficit in (16)
dominates the independent line/block budget by a function of
`|A|` and `span(A)`.  Equations (10)--(18) supply the exact local closure
available for that step; they do not assert that such a source-wide weighting
already exists.
