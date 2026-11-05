# Coupling two top-half sink chains

Let (s) be an (X)-oriented unsupported (N)-sink of weight (W_s),
and let (t) be a (Y)-oriented unsupported sink of weight (W_t).
Write (T_s,T_t) for their actual outward implication basins.  Every
vertex in (T_s) of weight (>W_s/2) lies on one ancestry chain: two
incomparable such vertices would have total weight greater than the
sink weight.  The same holds for (t).

Put

\[
 D=\{d:\ d>\max(W_s,W_t)/2,
       \ T_s\text{ and }T_t\text{ both contain a vertex of weight }d\}.
\tag{1}
\]

There is at most one vertex from either basin at each (d\in D), hence
exactly one physical (Q)-corner between the two basin vertices.  This
note records the exact parity law for its activity and a sharper
consequence when the two chains advance synchronously by one edge.

## 1. Size of each top-half chain

For a sink of integer weight (W), the possible top-half weights range
from

\[
 \lfloor W/2\rfloor+1\quad\text{to}\quad W.
\]

Their total variation is

\[
 R_W=\left\lceil\frac W2\right\rceil-1.
\tag{2}
\]

If the top-half chain contains (n) vertices, its alternating moved
(B)- and (C)-endpoint subsequences are Golomb.  The path calculation
from `INTERVAL_FOREST_BAND_CAPACITY_0042.md` gives

\[
 \left\lfloor\frac{n^2}{4}\right\rfloor\le R_W,
\]

so

\[
 n\le K^{\rm top}(W)
 :=\left\lfloor\sqrt{4\lceil W/2\rceil-1}\right\rfloor.
\tag{3}
\]

Consequently

\[
 |D|\le \min\{K^{\rm top}(W_s),K^{\rm top}(W_t)}.
\tag{4}
\]

This is the baseline square-root height bound before using the (Q)
colors.

## 2. Exact activity parity law

List the common offsets as

\[
 d_1<d_2<\cdots<d_m.
\]

Let (x_i\in T_s) and (y_i\in T_t) be the unique vertices of weight
(d_i).  For (i<m), let

\[
 a_i=\text{number of N-edges from }x_i\text{ to }x_{i+1},
 \qquad
 b_i=\text{number of N-edges from }y_i\text{ to }y_{i+1}.
\tag{5}
\]

The paths may contain weights not in (D), so (a_i,b_i) need not be
one.  Let (A_i=1) when the (Q)-link at (d_i) is active, meaning
that its two endpoint cells have opposite actual colors.  Each (N)-edge
reverses color, and therefore

\[
 \boxed{A_{i+1}=A_i\oplus(a_i+b_i\bmod2).}
\tag{6}
\]

Equivalently, activity persists between successive common offsets
exactly when (a_i,b_i) have the same parity.  In terms of sink colors
and path parities (p_s(d),p_t(d)), the pointwise form is

\[
 A(d)=1\oplus\operatorname{col}(s)
          \oplus\operatorname{col}(t)
          \oplus p_s(d)\oplus p_t(d).
\tag{7}
\]

This is the full restriction supplied by alternating path colors alone.
In particular, synchronization of the two path parities permits every
common-offset link to be active.

## 3. Synchronous one-edge transitions create shared differences

Assume (A_i=A_{i+1}=1) and

\[
 a_i=b_i=1.
\tag{8}
\]

Put (h_i=d_{i+1}-d_i>0).  Because the colors of (x_i,y_i) are
opposite, their successors use opposite parent classes.  If (x_i)
has color (B), its single edge moves its (C)-endpoint by (h_i),
while (y_i), of color (C), moves its (B)-endpoint by (h_i).
If the two colors are reversed, the roles of (B,C) are reversed.
In either case the two moved endpoint pairs prove

\[
 \boxed{h_i\in\Delta B\cap\Delta C.}
\tag{9}
\]

These are the unique (B)- and (C)-pairs of difference (h_i), by
Golombness.  They therefore generate the unique rotated
three-mixed-cell corner associated with that shared difference.

Moreover, two different transitions satisfying (8) cannot have the
same gap.  Equality (h_i=h_j=h) would make both transitions use the
same unique (B)-pair (p,p+h) and the same unique (C)-pair
(q,q+h).  If the two transitions assign each class-pair to the same
basin, one monotone chain would move the same endpoint pair twice,
which is impossible.  The pairs cannot swap basins either.  For
example, suppose the earlier transition moves (q,q+h) on the
(X)-chain and (p,p+h) on the (Y)-chain.  Its fixed opposite
endpoints give (b<q) on the (X)-side and (c<p) on the (Y)-side.
If a later transition swapped the pairs, nesting of the later (X)
interval around the earlier one would require (p+h\le b), while
nesting on the (Y)-side would require (q+h\le c).  Hence

\[
 p+h\le b<q,
 \qquad
 q+h\le c<p,
\]

which is contradictory.  The other initial assignment is symmetric.
Thus the gaps from all synchronous one-edge active transitions are
distinct positive integers.

If (J\subseteq\{1,\ldots,m-1\}) is the set of indices satisfying
(8), then their successive common-offset intervals are disjoint, so

\[
 \sum_{i\in J}h_i\le d_m-d_1.
\tag{10}
\]

Writing (r=|J|), distinctness and (10) give

\[
 \frac{r(r+1)}2\le d_m-d_1,
\]

or

\[
 \boxed{
 r\le
 \left\lfloor
 \frac{\sqrt{1+8(d_m-d_1)}-1}{2}
 \right\rfloor.}
\tag{11}
\]

Since every common offset is greater than
(max(W_s,W_t)/2) and at most (min(W_s,W_t)), one may further use

\[
 d_m-d_1
 \le \min(W_s,W_t)-\left\lfloor\frac{\max(W_s,W_t)}2\right\rfloor-1.
\tag{12}
\]

Thus a run in which consecutive common levels are adjacent in both
chains and all (Q)-links are active has length at most one plus the
right side of (11).  Each step of such a run spends a distinct shared
difference and has its own associated ternary corner.

## 4. Why the ternary corners do not yet bound all active links

The conclusion (9) fails once either intervening chain segment contains
more than one edge.  To see the exact arithmetic issue, write the total
outward endpoint motions between weights (d_i) and (d_{i+1}) as

\[
 \alpha_B+\alpha_C=h_i
 \quad\text{on the }X\text{-chain},
 \qquad
 \beta_B+\beta_C=h_i
 \quad\text{on the }Y\text{-chain}.
\tag{13}
\]

Here each nonzero term is a sum of consecutive, class-specific Golomb
endpoint increments.  If (a_i,b_i) have the same parity, (6) permits
activity at both ends, but (13) asserts only

\[
 \alpha_B+\alpha_C=\beta_B+\beta_C.
\tag{14}
\]

It need not identify a single (B)-difference with a single
(C)-difference.  For example, the local decomposition

\[
 1+4=3+2
\tag{15}
\]

uses distinct (B)-motions (1,3) and distinct (C)-motions (4,2),
while producing no shared moved-endpoint difference.  Equation (15) is
only a local arithmetic obstruction to the proposed inference; it does
not assert a separately constructed weak source.  The actual N-parent
witnesses would have to be included to realize a full example.

Even in the one-edge case, the ternary corner from (9) consists of the
three cross cells obtained by rotating the moved (B)- and (C)-pairs.
None is one of the two chain vertices at either common offset.  Its
properness only says that those three additional mixed cells are not
monochromatic.  Without an N- or Q-route fixing their colors, it does
not change the activity parity law (6).

The ordered Q threshold also gives no inequality at an active link:
opposite endpoint colors satisfy the Q-clause in either start order.
Order becomes restrictive only at an inactive, same-color link.

Accordingly, (6) and (11) are the complete coupling obtained here.
A better bound than the individual square-root height (4) requires one
of two additional facts not yet derived: either many successive common
levels must be adjacent in both chains, or the rotated ternary cells
created in (9) must feed back into the two basins with controlled
multiplicity.  Multi-edge synchronized segments are the explicit
remaining obstruction.
