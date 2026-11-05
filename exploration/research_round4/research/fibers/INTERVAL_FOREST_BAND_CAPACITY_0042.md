# Band capacity of an actual interval implication forest

Let an actual proper weak coloring and its forward (N)-implication
forest be as in `MIXED_INTERVAL_FORESTS_0042.md`.  A mixed vertex
(v=(b,c)) has integer weight

\[
 w(v)=|b-c|.
\]

Every forward edge strictly enlarges the interval, actual colors
alternate, every vertex has at most two incoming children, and the sum
of the child weights is at most the parent weight.  This note combines
the Golomb property of the moved endpoints with that length-conserving
branching.

## 1. Exact path height in one dyadic band

Fix an integer (H\ge1), and consider the vertices of one forward path
whose weights lie in

\[
 [H,2H).
\tag{1}
\]

They form a contiguous path segment because weights strictly increase.
Suppose this segment has (n) vertices and hence (k=n-1) forward
edges.  Along it, let (k_B) edges move the (B)-endpoint and (k_C)
edges move the (C)-endpoint.  Actual colors alternate, so the parent
families alternate and

\[
 k_B+k_C=k,qquad |k_B-k_C|\le1.
\tag{2}
\]

The moved (B)-endpoints form a monotone subsequence of (B), with
(k_B+1) terms if (k_B>0); likewise for (C).  Each subsequence is
Golomb.  If their total displacements are (D_B,D_C), respectively,
then all pairwise positive differences inside the (B)-subsequence are
distinct integers in ([1,D_B]).  Therefore

\[
 \binom{k_B+1}{2}\le D_B,
 \qquad
 \binom{k_C+1}{2}\le D_C.
\tag{3}
\]

The two endpoints move outward, so their displacements add exactly to
the increase in interval length across the segment:

\[
 D_B+D_C=w_{\rm last}-w_{\rm first}\le H-1.
\tag{4}
\]

For fixed (k), (2) minimizes the left side of the sum of (3) when the
two move counts are as equal as possible.  Thus

\[
 H-1\ge
 \begin{cases}
 t(t+1),&k=2t,\\
 (t+1)^2,&k=2t+1.
 \end{cases}
\tag{5}
\]

In terms of the number (n=k+1) of band vertices, the right side is
exactly (lfloor n^2/4\rfloor).  Hence

\[
 \left\lfloor\frac{n^2}{4}\right\rfloor\le H-1,
 \qquad n^2<4H,
\]

and therefore

\[
 \boxed{n\le K_H:=\left\lfloor\sqrt{4H-1}\right\rfloor.}
\tag{6}
\]

This uses both color switches: each class pays for roughly half of the
moves through its own Golomb difference inventory.  It is the strongest
bound obtained solely from monotonicity, integrality, and Golombness of
the two moved endpoint subsequences.

The same calculation applies to every subband ([H,H+R]) with integer
weights after replacing (H-1) in (4) by (R).  If (n) is the number
of path vertices in that subband, then

\[
 \left\lfloor\frac{n^2}{4}\right\rfloor\le R.
\tag{7}
\]

## 2. Lifting the path bound through all branches

Let (mathcal V_H) be all mixed vertices in the entire actual forest
with weights in (1).  Let (mathcal Z_H) be the unsupported sinks whose
components meet (mathcal V_H), and put

\[
 R_H=\sum_{z\in\mathcal Z_H}w(z).
\tag{8}
\]

The induced ancestor poset on (mathcal V_H) has height at most (K_H)
by (6).  Partition it into at most (K_H) antichains, for example by
the length of a longest chain in (mathcal V_H) ending at each vertex.
The weighted-antichain inequality of the interval-forest theorem gives,
for every such antichain (mathcal A),

\[
 \sum_{v\in\mathcal A}w(v)\le R_H.
\tag{9}
\]

Summing (9) over the antichain partition yields the forest-wide bound

\[
 \boxed{
 \sum_{v\in\mathcal V_H}w(v)
 \le K_H R_H.}
\tag{10}
\]

Since every band vertex has weight at least (H), this also gives

\[
 \boxed{
 |\mathcal V_H|
 \le \frac{K_H}{H}R_H
 <\frac{2}{\sqrt H}R_H.}
\tag{11}
\]

Both conclusions remain true with (mathcal V_H) replaced by any
subset, in particular the reflection-unit vertices in the band:

\[
 |\mathcal U_H|
 \le \frac{K_H}{H}R_H.
\tag{12}
\]

No multiplicity of paths ending at one sink is hidden here.  The local
law that the sum of child weights is at most the parent weight is
exactly what proves (9), while the Golomb path estimate supplies the
number (K_H) of necessary antichain layers.

One can localize (10) componentwise.  If (T_z) is the component rooted
at one unsupported sink (z), then

\[
 \sum_{v\in T_z:\ H\le w(v)<2H}w(v)\le K_Hw(z),
\qquad
 |T_z\cap\mathcal V_H|\le \frac{K_H}{H}w(z).
\tag{13}
\]

## 3. What reflection pairing does and does not add

An internal reflection (a<p<q) produces two unit vertices.  Their
weights are the two adjacent gaps

\[
 d_1=p-a,qquad d_2=q-p,
\tag{14}
\]

and the outer same-class difference is (d_1+d_2).  Thus reflection
unit occurrences are naturally paired, but the mate of a band unit
need not lie in the same band or in the same implication component.
The two-consecutive-unit family in
`REFLECTION_UNITS_ON_IMPLICATION_PATHS_0042.md` already exhibits both
types of escape for the band ([N,2N)): one relevant mate is below the
band and the other is above it.  Consequently reflection pairing alone
does not divide the factor (K_H) in (12).

This can be recorded by an exact defect.  For reflection events (R),
write their adjacent gaps as (d_1(R),d_2(R)), and define

\[
 E_H=\#\left\{R:
   \big|\{d_1(R),d_2(R)\}\cap[H,2H)\big|=1
 \right\}.
\tag{15}
\]

If (P_H) counts reflection events with both gaps in the band, then the
number of unit occurrences in the band is exactly

\[
 |\mathcal U_H|=2P_H+E_H.
\tag{16}
\]

The paired term (2P_H) retains two actual unit vertices, but the
one-sided term (E_H) has no band-local mate.  Any improvement of
(12) based on reflection pairing must therefore control (E_H) across
scales or couple the escaped mate to another finite resource.  Neither
the interval-parent law nor Golombness of the moved path endpoints
provides such a bound.

## 4. Remaining finite-capacity gap

The quantity on the right of (10)--(12) is the actual unsupported sink
mass

\[
 R_H=
 \sum_{(b,c)\in\mathcal Z_H}|b-c|,
\]

with the sink color selecting which diagonal-class difference is
unsupported.  It may be much larger than the number of source marks or
the number of holes at the relevant scale.  The factor

\[
 K_H\sim2\sqrt H
\]

also remains because the forest can place band vertices in that many
successive antichain layers before the endpoint Golomb inventories are
exhausted.

Thus the complete consequence of the present route is the
sink-weighted band estimate (10), with the exact height (6).  A useful
finite-source capacity theorem still needs at least one further input:
either a sharper bound on (R_H), a bound on the one-sided reflection
defect (E_H), or an actual-color argument showing that reflection
units occupy substantially fewer than (K_H) ranks in each component.
