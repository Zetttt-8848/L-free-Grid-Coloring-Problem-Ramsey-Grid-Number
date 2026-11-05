# Forced reflection in a full Cartesian source

This note concerns an arbitrary finite Cartesian set `B x C` in the integer
plane.  It derives a reflected-corner restriction using only original
positive-step corners, then converts it into a count inequality.  The full
Cartesian hypothesis is used to supply mixed cells; no strict-source closure
is assumed.

## 1. Orientations and notation

Let

\[
\mathcal G=B\times C,
\]

and suppose `z:mathcal G->{-1,+1}` has no monochromatic positive corner

\[
K^+(b,c;h)=
\{(b,c),(b+h,c),(b+h,c+h)\},\qquad h>0.
\tag{1}
\]

The inverse-orientation, or reflected, corner in the same square is

\[
K^-(b,c;h)=
\{(b,c),(b,c+h),(b+h,c+h)\}.
\tag{2}
\]

It exists when `b,b+h in B` and `c,c+h in C`.  Unlike (1), it is not
automatically covered by the properness hypothesis.

For a finite integer set `S`, define

\[
\begin{aligned}
r_S(h)&=|\{s:s,s+h\in S\}|,\\
p_S(h)&=|\{s:s,s+h,s+2h\in S\}|.
\end{aligned}
\tag{3}
\]

Thus `r_S(h)` counts step-`h` pairs and `p_S(h)` counts step-`h`
three-term progressions by their first mark.  Reindexing by the middle mark
does not change `p_S(h)`.

## 2. Cartesian reflection-switch theorem

**Theorem.**  Fix `b,c` and `h>0`.  Assume

\[
b-h,b,b+h\in B,
\qquad
c,c+h,c+2h\in C.
\tag{4}
\]

Then the reflected corner `K^-(b,c;h)` is nonmonochromatic.

**Proof.**  Name the relevant cells

\[
\begin{array}{lll}
A=(b,c),&P=(b+h,c),&D=(b+h,c+h),\\
S=(b,c+h),&E=(b+h,c+2h),&Z=(b-h,c).
\end{array}
\tag{5}
\]

All six cells belong to `B x C` by (4).  Suppose for a contradiction that
the reflected triple `A,S,D` has one sign `sigma`.

The positive corner `A,P,D`, of step `h`, forces `P` to sign `-sigma`.
The positive corner `S,D,E`, also of step `h`, forces `E` to sign
`-sigma`.  Now `Z,P,E` is a positive corner of step `2h`; its two cells
`P,E` force `Z` to sign `sigma`.  Finally `Z,A,S` is a positive corner of
step `h`; its two cells `A,S` force the same `Z` to sign `-sigma`.  This is
a contradiction.  Every corner used has the original orientation (1) and a
positive integer step.  This proves the theorem.

The extra coordinate requirements in (4) have a simple geometric meaning:
the row pair `b,b+h` must extend one step backward, while the column pair
`c,c+h` must extend one step forward.  The full product then supplies the
two mixed completion cells `Z` and `E` automatically.

## 3. A no-cancellation count inequality

Let `M_h^-` be the number of monochromatic reflected corners (2) of step
`h`.  There are exactly

\[
U_h=r_B(h)r_C(h)
\tag{6}
\]

reflected corners of that step before colors are considered.  The theorem
excludes every anchor in the Cartesian product

\[
\{b:b-h,b,b+h\in B\}
\times
\{c:c,c+h,c+2h\in C\}.
\]

The two factors have cardinalities `p_B(h)` and `p_C(h)`, respectively.
Therefore

\[
\boxed{
M_h^-\le r_B(h)r_C(h)-p_B(h)p_C(h).}
\tag{7}
\]

This subtraction has no multiplicity ambiguity: an anchor `(b,c,h)` has a
unique step, and the two extension conditions are independent coordinate
conditions in the full product.

Summing over positive steps, put

\[
U=\sum_{h>0}r_B(h)r_C(h),
\qquad
M^-=\sum_{h>0}M_h^-.
\]

Then

\[
\boxed{
M^-\le
U-\sum_{h>0}p_B(h)p_C(h).}
\tag{8}
\]

There is also a version involving only pair representation counts and the
set sizes.  In the graph on `S` joining `s` to `s+h`, every component is an
arithmetic-progression run.  If a nontrivial run has `m` vertices, it
contributes `m-1` to `r_S(h)` and `m-2` to `p_S(h)`.  Isolated vertices can
only weaken the resulting lower bound, so

\[
p_S(h)\ge \bigl(2r_S(h)-|S|\bigr)_+,
\tag{9}
\]

where `t_+=max(t,0)`.  Combining (8) and (9) gives the analytic inequality

\[
\boxed{
M^-\le U-
\sum_{h>0}
\bigl(2r_B(h)-|B|\bigr)_+
\bigl(2r_C(h)-|C|\bigr)_+.}
\tag{10}
\]

Thus a step represented by more than half of each coordinate set forces a
positive Cartesian block of inverse-orientation corners to be
nonmonochromatic.  The correction is a product, not a sum of separate
Golomb caps.

## 4. The extra support cannot be dropped automatically

Properness of the positive orientation alone does not make all reflected
corners proper.  Take `h=1`, `B=C={0,1}`, and color

\[
z(0,0)=z(0,1)=z(1,1)=+1,
\qquad z(1,0)=-1.
\tag{11}
\]

The only positive corner is nonmonochromatic, while the reflected corner
`{(0,0),(0,1),(1,1)}` is monochromatic.

Neither one-sided extension in (4) suffices by itself.  If
`B={-1,0,1}`, `C={0,1}`, the row array

\[
\begin{array}{c|cc}
 &0&1\\ \hline
-1&-&+\\
0&+&+\\
1&-&+
\end{array}
\tag{12}
\]

is positive-corner-free but has the reflected corner at `(0,0)`
monochromatic; here the backward row extension exists and the forward
column extension does not.  Conversely, for `B={0,1}`, `C={0,1,2}`,

\[
\begin{array}{c|ccc}
 &0&1&2\\ \hline
0&+&+&+\\
1&-&+&-
\end{array}
\tag{13}
\]

has the same behavior; now the forward column extension exists and the
backward row extension does not.  These examples do not claim that (4) is
the only possible forcing configuration.  They show that the full Cartesian
product, or either single extension, does not justify automatic reflection.

## 5. Scope of the relation

Inequalities (7)--(10) are a reusable relation between positive properness,
inverse-orientation monochromatic corners, and the common-difference energy
`U`.  They do not by themselves upper-bound `U`, because no independent
lower bound for `M^-` is supplied.  A global Cartesian-source argument would
need either such a lower bound or a way to charge the progression-product
term in (8) against its source decomposition.  The local theorem identifies
the exact term available for that purpose without assuming unsupported
reflected corners.
