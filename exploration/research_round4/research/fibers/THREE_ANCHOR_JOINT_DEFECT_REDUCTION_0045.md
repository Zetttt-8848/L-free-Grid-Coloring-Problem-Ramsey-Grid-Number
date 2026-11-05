# Three-anchor joint-budget reduction to \(b=4,5\)

Let \(B,C\subset\mathbb Z\) be disjoint Golomb sets with

\[
|B|=b,\qquad |C|=3,
\]

and suppose the prescribed diagonal coloring extends to a proper weak
coloring of \(W(B\sqcup C)\).  Retain

\[
N=N_B+N_C,\qquad
N_B=\sum_h\beta_h(x_h+y_h),\qquad
N_C=\sum_h\gamma_h(x_h+y_h),
\]

\[
Q=\sum_hx_hy_h,\qquad
\rho=|\Delta B\cap\Delta C|.
\]

The proposed three-anchor inequality is

\[
N+Q\le \binom{b+3}{2}.
\tag{1}
\]

This derivation proves that (1) is automatic for \(b\ge6\), while the
completed two-anchor and three-by-three lemmas cover \(b\le3\).  It reduces
the unsolved part exactly to two defect inequalities for \(b=4,5\).

## 1. The six anchor sums give \(Q\le9\)

Write \(C=\{c_0<c_1<c_2\}\).  Its unordered pair sums with repetition are

\[
2c_0,\ 2c_1,\ 2c_2,\ c_0+c_1,\ c_0+c_2,\ c_1+c_2.
\tag{2}
\]

They are distinct because \(C\) is Golomb.  The same pair-sum uniqueness
holds in \(B\), with repetitions allowed.

Each contribution to \(Q\) is a coincidence of a \(B\)-pair sum and a
\(C\)-pair sum.  For each of the three repeated sums \(2c_i\), a matching
distinct \(B\)-pair contributes one; a repeated \(B\)-pair is excluded by
disjointness.  For each of the three distinct sums \(c_i+c_j\), a matching
distinct \(B\)-pair contributes two, while a repeated \(B\)-midpoint
contributes one.  Pair-sum uniqueness allows at most one of these
alternatives.  Therefore

\[
\boxed{Q\le 3\cdot1+3\cdot2=9.}
\tag{3}
\]

This is independent of \(b\).

## 2. Anchor-supported mixed queries give \(N_C\le6+\rho\)

For a nonnegative integer \(k\),

\[
k\le 1_{k>0}+\binom{k}{2}.
\tag{4}
\]

Apply (4) to \(x_h\) and \(y_h\) for the three values
\(h\in\Delta C\).  There are only six orientation bins, and the exact
same-orientation collision identity gives

\[
\sum_h\left(\binom{x_h}{2}+\binom{y_h}{2}\right)=\rho.
\]

Consequently

\[
\boxed{N_C
=\sum_{h\in\Delta C}(x_h+y_h)
\le6+\rho\le9.}
\tag{5}
\]

Every one of the \(3b\) mixed pairs contributes at most one to \(N_B\), so

\[
\boxed{N_B\le3b.}
\tag{6}
\]

Combining (3), (5), and (6),

\[
N+Q\le3b+15+\rho\le3b+18.
\tag{7}
\]

For \(b\ge6\),

\[
\binom{b+3}{2}-(3b+18)
=\frac{(b-6)(b+5)}2\ge0.
\tag{8}
\]

Thus (1) holds for every \(b\ge6\).  The completed results
PROPER_WEAK_JOINT_QUERY_BUDGET_0044.md and
THREE_BY_THREE_JOINT_QUERY_0045.md give (1) for \(b\le2\) and \(b=3\),
respectively.  Only \(b=4,5\) remain.

## 3. Exact defect form of the two remaining sizes

Define three nonnegative defects

\[
R_B=3b-N_B,
\qquad
R_C=6+\rho-N_C,
\qquad
R_Q=9-Q.
\tag{9}
\]

Here \(R_B\) counts mixed queries unsupported by \(\Delta B\).
The quantity \(R_C\) is the slack in the six-orientation-bin estimate
(5), including its collision cost, and \(R_Q\) is the unused capacity
among the nine weighted anchor-sum matches.

Equations (3), (5), and (6) give the exact identity

\[
N+Q=3b+15+\rho-(R_B+R_C+R_Q).
\tag{10}
\]

Hence the desired bound (1) is equivalent to

\[
R_B+R_C+R_Q
\ge
\rho+\frac{-b^2+b+24}{2}.
\tag{11}
\]

At the two remaining sizes this is precisely

\[
\boxed{
\begin{aligned}
b=4:&\qquad R_B+R_C+R_Q\ge6+\rho,\\
b=5:&\qquad R_B+R_C+R_Q\ge2+\rho.
\end{aligned}}
\tag{12}
\]

Thus no unbounded-\(b\) argument remains in the three-anchor route.  The
missing statement is a properness charge in two fixed finite diagonal
sizes.

## 4. A one-unit \(4+3\) excess invisible to all \(3+3\) numerical bounds

The following configuration shows that applying the completed
three-by-three inequality separately to all \(B\)-triples does not by
itself prove the \(b=4\) line of (12):

\[
B=\{0,1,5,7\},\qquad C=\{2,3,6\}.
\tag{13}
\]

Its difference supports are

\[
\Delta B=\{1,2,4,5,6,7\},\qquad
\Delta C=\{1,3,4\},
\qquad \rho=2.
\]

The mixed orientation inventory is

\[
\begin{array}{c|rrrrrr}
h&1&2&3&4&5&6\\ \hline
x_h&2&2&1&0&1&1\\
y_h&1&1&1&1&1&0
\end{array}
\tag{14}
\]

and therefore

\[
N_B=10,\qquad N_C=6,\qquad Q=6.
\tag{15}
\]

Thus

\[
N+Q=22>\binom72=21,
\]

with

\[
(R_B,R_C,R_Q)=(2,2,3),\qquad
R_B+R_C+R_Q=7<8=6+\rho.
\tag{16}
\]

Nevertheless, for the four choices of a \(B\)-triple, the corresponding
local values against the same \(C\) are

\[
\begin{array}{c|c}
B'&N(B',C)+Q(B',C)\\ \hline
\{0,1,5\}&10\\
\{0,1,7\}&9\\
\{0,5,7\}&11\\
\{1,5,7\}&12.
\end{array}
\tag{17}
\]

Every local value is below \(15\).  Hence neither a maximum argument nor a
sum of the four scalar \(3+3\) budgets detects the global excess.

The actual weak constraints do detect it.  The \(B\)-reflection

\[
0<1<7,\qquad 0+7-1=6\in C
\]

forces

\[
z(7,6)=B.
\tag{18}
\]

The second \(B\)-reflection

\[
0<5<7,\qquad 0+7-5=2\in C
\]

forces

\[
z(7,2)=B.
\tag{19}
\]

Now the step-one corner on intervals \([2,3]\) and \([6,7]\) has cells

\[
z(3,2)=B,\qquad z(7,6)=B,\qquad z(7,2)=B.
\]

The first cell joins two \(C\)-marks and is fixed to color \(B\), so the
corner is monochromatic.  Configuration (13) therefore has no proper weak
extension.

This is a genuine four-mark interaction on the \(B\)-side: deleting any
one of the four marks destroys either one of the two reflection units or
the final corner, even though every surviving \(3+3\) restriction obeys
its scalar joint budget.

## 5. Exact remaining implication

The three-anchor target is reduced to proving the two inequalities in
(12) from the actual unit, binary, and ternary mixed-cell constraints.
Example (13) shows one way a one-unit defect shortfall is repaired: two
\(B\)-reflection units land on the endpoints of a \(C\)-supported corner
and make it monochromatic.

What is not proved here is that every \(b=4\) configuration with

\[
R_B+R_C+R_Q\le5+\rho
\]

or every \(b=5\) configuration with

\[
R_B+R_C+R_Q\le1+\rho
\]

must contain either this reflection-shadow mechanism or one of the two
forbidden \(3+3\) progression cores from
THREE_BY_THREE_JOINT_QUERY_0045.md.  That is the exact finite properness
implication left by this attempt.

No claim is made for larger \(C\), for arbitrary class sizes, or for an
all-source bound.
