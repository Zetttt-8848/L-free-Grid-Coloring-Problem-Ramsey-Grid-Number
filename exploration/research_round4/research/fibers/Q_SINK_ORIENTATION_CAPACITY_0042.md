# Orientation and capacity of Q-edges contracted to N-sinks

Let (B,C) be the two Golomb diagonal classes of an actual proper weak
source.  A mixed vertex has orientation (X) if its (B)-mark is below
its (C)-mark, and orientation (Y) if its (C)-mark is below its
(B)-mark.  Let (sigma(v)) be the unsupported sink reached by following
the actual forward (N)-implications from (v).

## 1. Orientation is invariant along every N-path

An (N)-parent keeps one endpoint fixed and moves the other endpoint
strictly outward.  Its interval properly contains the child interval.
Consequently an (X)-vertex has only (X)-ancestors and a (Y)-vertex
has only (Y)-ancestors:

\[
 \operatorname{or}(v)=\operatorname{or}(\sigma(v)).
\tag{1}
\]

Every (Q)-constraint joins an (X)-vertex and a (Y)-vertex at one
common weight (d).  By (1), its contracted endpoints are sinks of
opposite orientation.  In particular they are distinct.  Hence

\[
 \boxed{\text{the Q-graph contracted along N-paths has no loops and is
 bipartite by sink orientation}.}
\tag{2}
\]

This conclusion concerns physical mixed orientation, independently of
the alternating actual colors and path parities that determine the sign
of the contracted edge.

## 2. Fixed-weight capacity of one sink basin

Fix an unsupported sink (s), write

\[
 W_s=w(s),
\]

and let

\[
 \mathcal B_s(d)=\{v:\sigma(v)=s,\ w(v)=d\},
 \qquad n_s(d)=|\mathcal B_s(d)|.
\tag{3}
\]

All vertices in (mathcal B_s(d)) have the orientation of (s).  No
two are comparable in the (N)-forest, since weights strictly increase
along every nontrivial forward path.  They therefore form an antichain.
The length-conservation inequality gives

\[
 d,n_s(d)\le W_s,
 \qquad
 n_s(d)\le\left\lfloor\frac{W_s}{d}\right\rfloor.
\tag{4}
\]

There is also an endpoint-order improvement.  Every interval belonging
to the basin is contained in the sink interval.  If (s) has orientation
(X), write the vertices of (mathcal B_s(d)) as

\[
 [u,u+d],\qquad u\in B,quad u+d\in C.
\]

Their starts form a subset of the Golomb set (B), and all lie in an
interval of length (W_s-d).  Thus their \(\binom{n_s(d)}2\) positive
pair differences are distinct integers between (1) and (W_s-d):

\[
 \binom{n_s(d)}2\le W_s-d.
\tag{5}
\]

For a (Y)-sink the same argument uses the starts in (C).  Define

\[
 G(W,d)=
 \min\left\{
 \left\lfloor\frac Wd\right\rfloor,
 \left\lfloor\frac{1+\sqrt{1+8(W-d)}}2\right\rfloor
 \right\}
\tag{6}
\]

for (1\le d\le W), and (G(W,d)=0) for (d>W).  Combining (4) and
(5) gives the exact clean capacity

\[
 \boxed{n_s(d)\le G(W_s,d).}
\tag{7}
\]

The first term is strongest when (d) is a substantial fraction of
the sink weight.  The Golomb-start term improves it for small (d).

## 3. Contracted multiplicity between two sinks

Let (s) be an (X)-sink and (t) a (Y)-sink.  At fixed offset
(d), every vertex of (mathcal B_s(d)) and every vertex of
(mathcal B_t(d)) are opposite-orientation endpoint cells at the same
positive offset.  They therefore determine one actual (Q)-corner.
After contraction, the number of (Q)-clauses between (s) and (t)
coming from this offset is exactly

\[
 m_{s,t}(d)=n_s(d)n_t(d).
\tag{8}
\]

Equations (4) and (7) yield

\[
 \boxed{
 m_{s,t}(d)
 \le G(W_s,d)G(W_t,d)
 \le
 \left\lfloor\frac{W_s}{d}\right\rfloor
 \left\lfloor\frac{W_t}{d}\right\rfloor.}
\tag{9}
\]

In particular,

\[
 d^2m_{s,t}(d)\le W_sW_t.
\tag{10}
\]

If only active actual-color implications are counted, subdivide the
two basin fibers by actual color:

\[
 n_{s,B}(d)+n_{s,C}(d)=n_s(d),
 \qquad
 n_{t,B}(d)+n_{t,C}(d)=n_t(d).
\]

The exact active multiplicity is

\[
 m^{\rm act}_{s,t}(d)
 =n_{s,B}(d)n_{t,C}(d)+n_{s,C}(d)n_{t,B}(d)
 \le m_{s,t}(d).
\tag{11}
\]

Summing (8) over all opposite-orientation sink pairs recovers the full
physical (Q)-corner count at that layer:

\[
 |X_d||Y_d|
 =\sum_{s\in\mathcal Z_X}\sum_{t\in\mathcal Z_Y}
 n_s(d)n_t(d).
\tag{12}
\]

## 4. Limit of further sharpening from endpoint order

The ordered (Q)-threshold controls which same-colored opposite-
orientation pairs are permitted, but it does not reduce the worst-case
product in (8).  For fixed basin fibers, assigning every (X)-vertex
color (B) and every (Y)-vertex color (C) makes every one of the
(n_s(d)n_t(d)) cross-pairs an active implication; the two threshold
inequalities impose no relative-order restriction on these two color
categories.  The reversed choice has the analogous property.

Thus interval containment sharpens each factor through the Golomb
estimate (5), but the complete bipartite nature of a (Q)-layer leaves
their product intact.  Any stronger pairwise multiplicity bound must
use information absent from endpoint order alone, such as the path
parities forced by the two sink colors, additional (Q)-layers, or the
three-variable shared-difference clauses.

The theorem is a local contraction-capacity statement.  Summing (9)
over many offsets or sink pairs still requires a global budget for the
unsupported sink weights and their fixed-weight basin profiles.
