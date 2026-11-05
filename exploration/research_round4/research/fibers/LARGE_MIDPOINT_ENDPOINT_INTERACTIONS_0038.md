# Interactions among large endpoint midpoint fibers

Work in the two-distance endpoint setting of
TWO_DISTANCE_ENDPOINT_BUDGET_0038.md.  Translate the image of the
anchored source endpoint to the origin \(p=0\), and scale notation so
that all nonzero squared distances are \(\tau\) or \(2\tau\).

For every far output \(w\), so \(\|w\|^2=2\tau\), let \(q_w\) be the
number of source decompositions
\[
w=x_i+y_i.
\]
Each \(x_i,y_i\) is a near point of squared norm \(\tau\), the pairs are
disjoint for fixed \(w\), and
\[
\|x_i-y_i\|^2=2\tau.
\]
Write
\[
D_w=\{x_i,y_i:1\le i\le q_w\},\qquad |D_w|=2q_w.       \tag{1}
\]
The endpoint deletion cost is \(2\sum_w q_w\).  This note studies the
large outputs
\[
\mathcal H=\{w:q_w\ge6\}.                              \tag{2}
\]
The midpoint fiber at \(w/2\) contains the antipodal pair \(\{0,w\}\)
as well as the \(q_w\) pairs in (1), so its total number of displayed
axes is \(k=q_w+1\).

## 1. Pairwise intersection rule

Fix \(w\in\mathcal H\), put \(c=w/2\), and write its midpoint axes as
\[
\{c\pm p_i:0\le i\le q_w\},
\]
where
\[
p_0=w/2,\qquad \|p_i\|^2=\tau/2,
\qquad \langle p_i,p_j\rangle=0\quad(i\ne j).          \tag{3}
\]
The pair for \(i=0\) is \(\{0,w\}\); the other pairs are the elements
of \(D_w\).

Let \(v\ne w\) be another far output and put \(r=v-c\).  For every axis
\(p_i\), the two squared distances from \(v\) to \(c\pm p_i\) are
\[
\|r\|^2+\tau/2\mp2\langle r,p_i\rangle.                \tag{4}
\]

If \(\|v-w\|^2=2\tau\), then the distances from \(v\) to both \(0\) and
\(w\) are \(2\tau\).  Their average in (4) is \(2\tau\).  Hence
\[
\|r\|^2=3\tau/2,\qquad \langle r,p_i\rangle=0
\]
for every \(i\), and both distances from \(v\) to each endpoint in
\(D_w\) are \(2\tau\).  A decomposition endpoint for \(v\) must be at
distance \(\tau\) from \(v\).  Therefore
\[
\|v-w\|^2=2\tau
\quad\Longrightarrow\quad
D_v\cap D_w=\varnothing.                              \tag{5}
\]

If \(\|v-w\|^2=\tau\), the distances from \(v\) to \(0,w\) are
\(2\tau,\tau\), so their average is \(3\tau/2\).  Equation (4) gives
\[
\|r\|^2=\tau,\qquad
|\langle r,p_i\rangle|=\tau/4
\quad(0\le i\le q_w).                                 \tag{6}
\]
Thus \(v\) is at distance \(\tau\) from exactly one endpoint of every
pair \(c\pm p_i\), and at distance \(2\tau\) from the other.  In
particular, at most one endpoint from each decomposition pair for \(w\)
can also be a decomposition endpoint for \(v\).  Hence
\[
\|v-w\|^2=\tau
\quad\Longrightarrow\quad
|D_v\cap D_w|\le\min(q_v,q_w).                         \tag{7}
\]

Equations (5)--(7) are the basic overlap rule.  They retain the geometry
of the two far outputs; a bare bound \(q_w\le7\) does not.

## 2. Aggregate packing inequality

Let \(N_1\) be the set of near points relative to the root and write
\[
n_1=|N_1|.
\]
For \(u\in N_1\), let
\[
d(u)=|\{w\in\mathcal H:u\in D_w\}|.
\]
Set
\[
I=\sum_{w\in\mathcal H}|D_w|
  =2\sum_{w\in\mathcal H}q_w
  =\sum_{u\in N_1}d(u),                               \tag{8}
\]
and let \(e_\tau(\mathcal H)\) count unordered pairs \(v,w\in\mathcal H\)
at squared distance \(\tau\).

Double-counting intersections and applying (5)--(7) gives
\[
\sum_{u\in N_1}\binom{d(u)}2
=\sum_{\{v,w\}\subset\mathcal H}|D_v\cap D_w|
\le
\sum_{\substack{\{v,w\}\subset\mathcal H\\
                 \|v-w\|^2=\tau}}
\min(q_v,q_w).                                        \tag{9}
\]
In the small-midpoint regime relevant to the coefficient-\(14\) proof,
every \(q_w\le7\), so
\[
\sum_{u\in N_1}\binom{d(u)}2
\le7e_\tau(\mathcal H).                               \tag{10}
\]
On the other hand, Cauchy gives
\[
\sum_{u\in N_1}\binom{d(u)}2
=\frac12\left(\sum_ud(u)^2-I\right)
\ge\frac12\left(\frac{I^2}{n_1}-I\right).             \tag{11}
\]
Combining (10)--(11),
\[
\boxed{\qquad
I^2\le n_1\bigl(I+14e_\tau(\mathcal H)\bigr).
\qquad}                                               \tag{12}
\]

If \(h=|\mathcal H|\) and
\[
E_{\rm exc}=\sum_{w\in\mathcal H}(q_w-5),
\]
then \(I=10h+2E_{\rm exc}\), so (12) becomes
\[
\boxed{\qquad
(10h+2E_{\rm exc})^2
\le n_1\bigl(10h+2E_{\rm exc}
             +14e_\tau(\mathcal H)\bigr).
\qquad}                                               \tag{13}
\]
This is a direct quantitative restriction on the positive excess over
five decompositions per far output.  Large excess requires the high
outputs themselves to span many near pairs.  Far-separated high outputs
have disjoint endpoint resources.

## 3. The binary code at \(q_w=7\)

Suppose \(q_w=7\).  Then (3) supplies eight orthogonal axes.  For any
other far output \(v\) with \(\|v-w\|^2=\tau\), equation (6) uses exactly
the full norm:
\[
\sum_{i=0}^7
\frac{\langle r,p_i\rangle^2}{\|p_i\|^2}
=8\cdot\frac{\tau}{8}
=\tau
=\|r\|^2.                                              \tag{14}
\]
Thus \(r\) has no component perpendicular to these axes.  Its sign on
\(p_0\) is fixed by the ordered distances
\(\|v\|^2=2\tau\), \(\|v-w\|^2=\tau\).  The remaining seven projection
signs encode \(v\) by a word
\[
\sigma(v)\in\{\pm1\}^7.                               \tag{15}
\]
The encoding is injective.

For two such outputs \(v,v'\), their squared distance is
\[
\|v-v'\|^2=\frac{\tau}{2}
d_H(\sigma(v),\sigma(v')),                            \tag{16}
\]
where \(d_H\) is Hamming distance.  Since the left side is \(\tau\) or
\(2\tau\), distinct codewords have Hamming distance \(2\) or \(4\).
In particular all words have the same parity and no two are at Hamming
distance \(6\).

There is a short numerical bound for such a code.  On one parity class
of the seven-cube, join two words when their distance is \(6\).  This is
a \(7\)-regular graph on \(64\) vertices.  Its characters have
eigenvalues
\[
7,\quad 3,\quad -1,\quad -5.
\]
Indeed, the seven generators are the weight-six words
\(\mathbf1+e_i\); a character represented by a word of weight
\(r\le3\) has eigenvalue \(7-2r\) for even \(r\), and \(2r-7\) for odd
\(r\).  The least eigenvalue is \(-5\).  The elementary ratio bound for
an independent set gives
\[
\alpha\le
\frac{64\cdot5}{7+5}
=\frac{80}{3},
\]
and hence
\[
\boxed{\qquad
|\{v:\|v\|^2=2\tau,\ \|v-w\|^2=\tau\}|\le26
\quad\text{when }q_w=7.
\qquad}                                               \tag{17}
\]
For completeness, the ratio bound follows by applying the least
eigenvalue inequality to the centered indicator of the independent
set.  No classification of binary codes is used.

## 4. The remaining \(q_w=6\) gap

When \(q_w=6\), there are seven displayed axes.  Equation (6) accounts
for \(7\tau/8\) of \(\|r\|^2=\tau\), leaving
\[
\|r_\perp\|^2=\tau/8.                                 \tag{18}
\]
The signs on the seven axes still determine which endpoint of every
pair in \(D_w\) can be shared, but the residual vectors \(r_\perp\) live
in an uncontrolled orthogonal complement.  Pairwise distances among
other high outputs depend on both their Hamming signs and
\(\|r_\perp-r'_\perp\|^2\).  Therefore the finite code argument in
Section 3 does not extend directly to \(q_w=6\).

The aggregate inequality (13) is the complete new count available
without resolving that residual geometry.  It shows that a violation of
the desired excess budget must concentrate on a dense near-distance
graph among outputs with \(q_w=6\) or \(7\).  The \(q_w=7\) vertices have
the finite local bound (17); the unresolved configuration is a large
collection of \(q_w=6\) outputs whose residual vectors on the
\(\tau/8\)-sphere maintain all two-distance constraints while their
decomposition endpoint sets overlap according to (7).


## Root continuation

The endpoint coefficient-ten gap and the q=6 residual issue are now closed for this representation class in ../TWO_DISTANCE_POINT_DELETION_0038.md. The residuals are forced into one antipodal pair, a seven-bit quadratic function-space bound gives at most 29 far near-neighbors, and bounded decomposition overlap proves deletion cost at most 10(m-1) for every source mark. This is still a class theorem, not a general proper-source result.
