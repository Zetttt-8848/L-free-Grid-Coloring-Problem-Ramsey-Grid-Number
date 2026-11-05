# Endpoint deletion in a two-distance source

Let \(A\) be a finite integer source of size \(m\), and suppose there is
an injective Freiman-2 map
\[
\phi:A\longrightarrow X
\]
into a Euclidean two-distance set: every squared distance between
distinct points of \(X\) is either \(\tau\) or \(2\tau\), with
\(\tau>0\).  Only preservation of additive equalities in \(A\) is used.
Replacing \(X\) by the image of \(A\), assume throughout that
\(X=\phi(A)\).

Fix an extreme mark \(a\in\{\min A,\max A\}\).  After translation or
reflection, take \(a=0=\min A\).  Let \(e_0(A)\) be the number of arcs in
the anchored addition graph,
\[
x\longrightarrow w
\quad\Longleftrightarrow\quad
x,w,w-x\in A\setminus\{0\},\quad 0<x<w.                \tag{1}
\]
By endpoint deletion,
\[
e_0(A)=T(A)-T(A\setminus\{0\}).                        \tag{2}
\]
This note proves a uniform \(14(m-1)\) endpoint budget for the
two-distance representation class and records a sharper distance-degree
form.  The desired constant \(10\) is not obtained without an additional
local degree restriction.

## 1. Endpoint relations are squares through one point

There is no anchored progression \(0,x,2x\) in \(A\).  Otherwise
\[
\phi(0)+\phi(2x)=2\phi(x)
\]
would make three distinct points of \(X\) a Euclidean three-term
progression.  Its outer squared distance would be four times a side
squared distance, which is impossible when all nonzero squared
distances are \(\tau\) or \(2\tau\).

Consequently every anchored relation
\[
0+w=x+y                                                   \tag{3}
\]
has four distinct marks.  Its image is a square.  Relative to
\[
p=\phi(0),
\]
the points \(\phi(x),\phi(y)\) are at squared distance \(\tau\) from
\(p\), are joined to one another by squared distance \(2\tau\), and
\(\phi(w)\) is opposite \(p\), at squared distance \(2\tau\).

For a fixed \(w\), let \(q_w\) be the number of unordered source
decompositions
\[
w=x+y,\qquad 0<x<y,\qquad x,y\in A.                    \tag{4}
\]
There are two arcs in (1) for each decomposition, so
\[
e_0(A)=2\sum_w q_w.                                    \tag{5}
\]

Put
\[
c_w=\frac{\phi(0)+\phi(w)}2.
\]
At this midpoint, \(\{\phi(0),\phi(w)\}\) is one long antipodal pair,
and each decomposition in (4) supplies another long antipodal pair
\(\{\phi(x),\phi(y)\}\).  Distinct decompositions give distinct pairs.
If \(k_{c_w}\) is the total number of long pairs in \(X\) with midpoint
\(c_w\), then
\[
q_w\le k_{c_w}-1.                                      \tag{6}
\]

## 2. Large fibers collapse the endpoint fan

The midpoint-separation lemma for two-distance sets says that if a
midpoint \(c\) has \(k_c\ge9\) long pairs, their \(2k_c\) endpoints form
a set
\[
Y_c=\{c\pm p_i:1\le i\le k_c\}
\]
which participates in no square mixing \(Y_c\) with \(X\setminus Y_c\).
Moreover, the only squares entirely in \(Y_c\) are the
\(\binom{k_c}{2}\) squares obtained by choosing two antipodal pairs at
that same midpoint.

Suppose \(p=\phi(0)\) belongs to such a large fiber.  Any square through
\(p\) must then lie in \(Y_c\), and it pairs the unique antipode of \(p\)
at \(c\) with one of the other \(k_c-1\) antipodal pairs.  Therefore
\[
\sum_w q_w\le k_c-1,
\qquad
e_0(A)\le2(k_c-1)\le |Y_c|-2\le m-2.                  \tag{7}
\]
In particular, a large midpoint fiber is favorable for endpoint
deletion.  It cannot coexist with a second square fan through \(p\)
outside that fiber.

## 3. Uniform endpoint bound

Assume now that \(p\) belongs to no midpoint fiber with nine or more
long pairs.  Every \(w\) occurring in (4) then has
\[
k_{c_w}\le8,
\qquad q_w\le7                                          \tag{8}
\]
by (6).  There are at most \(m-1\) choices of \(w\).  Equations
(5) and (8) give
\[
e_0(A)\le14(m-1).                                      \tag{9}
\]
Together with (7), this proves:

**Two-distance endpoint theorem.**  Every extreme mark \(a\) of an
integer source admitting an injective Freiman-2 map to a Euclidean
two-distance set satisfies
\[
\boxed{\qquad
T(A)-T(A\setminus\{a\})\le14(|A|-1).
\qquad}                                                \tag{10}
\]
The assertion holds for both endpoints because reflection preserves
the source corners and the Freiman-2 relations.

This proof does not deduce an endpoint statement from the global
\(T(A)\le7\binom m2\) theorem.  It counts only squares incident with the
chosen endpoint and applies the large-fiber separation at that endpoint.

## 4. Near/long degree refinement

The endpoint geometry gives a more informative bound than (9).  Let
\[
n_1=|\{x\in A\setminus\{0\}:
       \|\phi(x)-p\|^2=\tau\}|,
\]
\[
n_2=|\{x\in A\setminus\{0\}:
       \|\phi(x)-p\|^2=2\tau\}|,
\qquad n_1+n_2=m-1.                                    \tag{11}
\]
Every decomposition in (4) uses an unordered pair of near points and
has a long point \(w\) as its output.  In the small-fiber case,
\[
\sum_w q_w
\le \min\left\{\binom{n_1}{2},\,7n_2\right\}.
\]
Hence
\[
\boxed{\qquad
e_0(A)\le
\min\{\,n_1(n_1-1),\,14n_2\,\}.
\qquad}                                                \tag{12}
\]
In the large-fiber case, the stronger estimate (7) applies.

Formula (12) reaches the desired endpoint constant \(10\) under either
of the explicit conditions
\[
n_1(n_1-1)\le10(m-1)                                   \tag{13}
\]
or
\[
n_2\le\frac57(m-1).                                    \tag{14}
\]
Condition (14) says that at least \(2/7\) of the other source marks map
to near neighbors of the endpoint.  These are sufficient conditions,
not properties proved for an arbitrary extreme source mark.

There is also a per-output version useful when midpoint multiplicities
are known:
\[
e_0(A)\le
2\sum_{\substack{w:\,\|\phi(w)-p\|^2=2\tau}}
\bigl(k_{c_w}-1\bigr).                                 \tag{15}
\]
If all endpoint midpoint fibers have size at most \(r+1\), then
\[
e_0(A)\le2r\,n_2.                                      \tag{16}
\]

## 5. Exact gap at constant ten

The separation argument has a sharp internal threshold at
\(k_c=9\): for \(k_c\ge9\), orthogonal projection excludes every square
mixing the fiber with outside points.  Below that threshold it only gives
\(q_w\le7\), producing the coefficient \(14\) in (9).

To improve (10) to \(10(m-1)\) by this route, one must show that an
extreme source image cannot simultaneously have too many long outputs
and average more than five decompositions per such output.  Equivalently,
one needs a compatibility relation among several distinct midpoint
fibers \(c_w=(p+\phi(w))/2\) through the same root \(p\).  The existing
large-fiber projection treats one midpoint at a time and supplies no
such relation for fibers of sizes \(2,\ldots,8\).

Thus the complete class result is the endpoint constant \(14\), with the
degree-sensitive improvement (12).  No two-distance counterexample to
constant \(10\) is constructed here, and no universal endpoint claim is
made beyond the representation class.


## Root continuation

The endpoint coefficient-ten gap and the q=6 residual issue are now closed for this representation class in ../TWO_DISTANCE_POINT_DELETION_0038.md. The residuals are forced into one antipodal pair, a seven-bit quadratic function-space bound gives at most 29 far near-neighbors, and bounded decomposition overlap proves deletion cost at most 10(m-1) for every source mark. This is still a class theorem, not a general proper-source result.
