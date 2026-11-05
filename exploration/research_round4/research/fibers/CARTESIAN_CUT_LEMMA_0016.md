# Cartesian cut lemma: fixed-step routing, its cross-step gap, and a sharp dissociated family

## 1. Setup

Let (B,C\subset \mathbb Z) be finite.  Write

\[
r_B(h)=|B\cap(B-h)|,\qquad r_C(h)=|C\cap(C-h)|
\]

for (h>0), and

\[
U(B,C)=\sum_{h>0}r_B(h)r_C(h).
\]

Thus (U(B,C)) is exactly the number of available corners

\[
L=(b,c),\qquad Q=(b+h,c),\qquad R=(b+h,c+h)
\tag{1}
\]

in (B\times C).  Let (z_{b,c}\in\{\pm1\}) be a proper coloring, so the three signs in (1) are never all equal.

The hoped-for Cartesian estimate is

\[
U(B,C)\le 2|B||C|.
\tag{2}
\]

The argument below obtains an exact fixed-step routing statement, identifies the sole cross-step quantity it leaves uncontrolled, and gives an infinite proper Cartesian family with (U/(|B||C|)\to1).  It does not prove (2).

## 2. Exact routing at one step

Fix (h>0).  Join (p=(b,c)) to (p+(h,h)) whenever both cells belong to (B\times C).  These diagonal (h)-edges form vertex-disjoint directed paths (possibly with gaps when viewed on a whole numerical diagonal).

For a bichromatic diagonal edge (LR), the completion (Q) in (1) has the color of exactly one endpoint.  Route the edge

* to (L) when (z_Q=z_L) (the column pair (LQ) is monochromatic), and
* to (R) when (z_Q=z_R) (the row pair (QR) is monochromatic).

This routing is injective on every (h)-path.  Indeed, the only possible collision is an edge entering a cell (p) routed to its right endpoint followed by an edge leaving (p) routed to its left endpoint.  If

\[
p_-=p-(h,h),\quad q_-=(b,c-h),\quad p=(b,c),\quad
q_+=(b+h,c),\quad p_+=p+(h,h),
\]

then such a collision says

\[
z_{q_-}=z_p=z_{q_+}.
\]

Here the full (3\times3) arithmetic subproduct is essential.  The two original (h)-corners (p_-q_-p) and (pq_+p_+) force (p_-) and (p_+) to have the sign opposite to (p).  Put

\[
s=(b+h,c-h).
\]

The original (2h)-corner (p_-sp_+) then forces (s) to have the sign of (p).  Finally, (q_-sq_+) is an original (h)-corner, and all its cells have the sign of (p), a contradiction.  Hence a cell receives at most one routed bichromatic diagonal (h)-edge.  (A bare (2\times2) rectangle would not justify the reflected constraint; the two consecutive diagonal edges supply the needed three marks in each coordinate.)

Let (X_h) be the number of bichromatic diagonal (h)-edges.  The conclusion is

\[
X_h\le |B||C|.
\tag{3}
\]

The monochromatic diagonal edges have a different exact restriction.  On each numerical diagonal (b-c=\delta), the cells of either fixed sign form a Golomb set: two same-sign pairs on that diagonal cannot have the same positive separation.  Consequently, for a fixed (h), there is at most one monochromatic (h)-edge of each sign on each numerical diagonal.

This is a genuine same-step statement.  It does not sum over (h).

## 3. The cross-step load left by the routing

Route every bichromatic diagonal edge by the preceding rule.  For a cell (p), let

\[
\lambda(p)=\#\{h>0:\text{a bichromatic diagonal (h)-edge is routed to (p)}\}.
\]

Let (S) denote the total number of monochromatic diagonal pairs over all positive steps.  Every corner is represented by exactly one diagonal pair, so

\[
U(B,C)=S+\sum_{p\in B\times C}\lambda(p).
\tag{4}
\]

Writing

\[
P=|\{p:\lambda(p)>0\}|,
\qquad
E=\sum_p(\lambda(p)-1)_+,
\]

gives the exact decomposition

\[
U(B,C)=S+P+E.
\tag{5}
\]

Thus (2) is equivalent, for this routing, to

\[
S+E\le 2|B||C|-P.
\tag{6}
\]

In particular, the clean sufficient inequality

\[
S+E\le |B||C|
\tag{7}
\]

would prove (2).  Here (E) is precisely the excess caused by different offsets charging the same cell.

The reflected-corner argument does not control (E).  To see the obstruction exactly, suppose an incoming edge of step (h_1) and an outgoing edge of step (h_2) collide at (p=(b,c)).  The routing then makes

\[
(b,c-h_1),\quad (b,c),\quad (b+h_2,c)
\tag{8}
\]

monochromatic.  When (h_1=h_2), (8) is the supported reflected corner used above.  When (h_1\ne h_2), its two legs have unequal lengths, and (8) is not a legal corner.  Full Cartesian availability supplies all three cells but does not change the unequal lengths.  Therefore any proof of (7), or of the exact weaker target (6), needs a further ordered or amortized relation between different offsets; an unequal-step substitution cannot provide it.

This isolates the quantitative gap: pay simultaneously for monochromatic diagonal pairs (S) and for cross-offset routing collisions (E), using at most one additional unit per Cartesian cell on average.

## 4. A parameterized proper family with ratio tending to (1)

The following construction shows that no universal bound (U\le c|B||C|) can have (c<1).

Fix (t\ge3), split a (2t)-element coordinate set as (X\sqcup Y) with (|X|=|Y|=t), and choose weights (w_i) that are dissociated for coefficients in ({-2,-1,0,1,2}); for example, (w_i=5^i).  For a two-element set (S), put

\[
a_S=\sum_{i\in S}w_i.
\]

Define

\[
B=\{a_{\{x,y\}}:x\in X, y\in Y\},
\]

and

\[
C=\{a_S:S\in {X\choose2}\text{ or }S\in {Y\choose2}\}.
\]

Thus (B) is the family of cross pairs, (C) is the family of within-part pairs, and (B\cap C=\varnothing).  Color the Cartesian cell ((a_S,a_T)) by

\[
\chi(a_S,a_T)=
\begin{cases}
1,&S\cap T\ne\varnothing,\\
0,&S\cap T=\varnothing.
\end{cases}
\tag{9}
\]

This coloring is proper.  Suppose

\[
a_{S'}-a_S=a_{T'}-a_T>0.
\tag{10}
\]

Dissociation makes the signed incidence vectors in (10) equal.  Hence there are disjoint nonempty sets (P,Q) and stationary sets (I,J) such that

\[
S=Q\sqcup I,quad S'=P\sqcup I,quad
T=Q\sqcup J,quad T'=P\sqcup J.
\tag{11}
\]

Both (S\cap T) and (S'\cap T') are nonempty, since they contain (Q) and (P), respectively.  On the other hand,

\[
S'\cap T=I\cap J.
\]

If (|P|=2), then (I=J=\varnothing).  If (|P|=1), then (I,J) are singletons; equality (I=J) would give (S=T), contrary to (B\cap C=\varnothing).  Thus (I\cap J=\varnothing) in both cases.  Every corner therefore has color pattern (1,0,1).

It remains to count (U).  A common difference that replaces two coordinates has a unique initial and final two-set, so it cannot occur in both disjoint families (B) and (C).  A common difference that replaces (q) by (p) has one representation ({q,i}\to\{p,i}) for each (i\notin\{p,q}).

If (p,q\in X), there are (t) such representations in (B) (the stationary coordinate lies in (Y)) and (t-2) in (C) (it lies in (X\setminus\{p,q})).  The same holds in (Y).  If (p,q) lie in opposite parts, there is no representation in (B) with both endpoints cross pairs.  Consequently

\[
U(B,C)=2{t\choose2}t(t-2)=t^2(t-1)(t-2).
\tag{12}
\]

Since

\[
|B|=t^2,qquad |C|=2{t\choose2}=t(t-1),
\]

we obtain

\[
\frac{U(B,C)}{|B||C|}=\frac{t-2}{t}\longrightarrow1.
\tag{13}
\]

There is also a useful internal explanation for the coefficient (1) in this family.  Regard (B) and (C) as two edge-disjoint graphs (G,H) on the coordinate set.  Then

\[
U=\sum_{p<q}|N_G(p)\cap N_G(q)|\,|N_H(p)\cap N_H(q)|.
\tag{14}
\]

An object counted in (14) is a four-cycle whose two edges through one center lie in (G) and whose two edges through the other center lie in (H).  Pairing opposite edges gives two incidences with a pair ((e_G,e_H)).  A fixed disjoint pair ((e_G,e_H)) supports at most two such incidences: the two complementary alternatives are mutually exclusive because they would require the same cross-edge to lie in both edge-disjoint graphs.  Hence (2U\le2|E(G)||E(H)|), so (U\le|B||C|) throughout this entire dissociated two-set model.  The balanced two-part construction above asymptotically attains it.

This stronger estimate relies on the single-coordinate exchange representation (11).  General integer sets have no such coordinate centers, so the opposite-edge injection does not extend to arbitrary (B,C).  For arbitrary Cartesian sets, the remaining target is exactly the cross-offset inequality (6), with (7) as a clean sufficient form.
