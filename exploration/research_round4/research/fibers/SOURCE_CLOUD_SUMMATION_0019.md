# Summing source-compatible clouds: descent and convergence

## 1. Charge events

Retain the separated source \(A=B\sqcup C\), \(B<C\), and its one proper coloring \(z\).  For a cross support

\[
p=(c,u)\in C\times B,\qquad \sigma=z(p),
\]

call \((p,d)\) a **charge event** when

\[
u+d\in B,\quad c+d\in C,\quad
z(u+d,u)=z(c+d,c)=\sigma.
\tag{1}
\]

As in SOURCE_COMPATIBLE_CLOUD_0018.md, put

\[
q_d=(c+d,u+d).
\]

The two child edges in (1) force the outer cross cell \((c+d,u)\) to have color \(-\sigma\), so the corner of step \(d\) is supported by \(p\).  Let

\[
G_\tau(p)=\{d:(p,d)\text{ is a charge event and }z(q_d)=\tau\}.
\]

The total number of charge events is at most

\[
\sum_d r_B(d)r_C(d)=U(B,C),
\tag{2}
\]

because an event is a color-restricted aligned pair of one \(B\)-edge and one \(C\)-edge of the same length.

## 2. Consecutive-pair descent

For each nonempty \(G_\tau(p)\), list its offsets increasingly,

\[
d_1<d_2<\cdots<d_k.
\]

Use only consecutive pairs.  For \(d_i<d_{i+1}\), set

\[
g=d_{i+1}-d_i,\qquad p'=q_{d_i}=(c+d_i,u+d_i).
\tag{3}
\]

The local pairwise child lemma says that at least one of

\[
e_B=(u+d_{i+1},u+d_i)\in V(B),
\qquad
e_C=(c+d_{i+1},c+d_i)\in V(C)
\tag{4}
\]

has color \(\tau=z(p')\).

There are now exactly two cases.

1. **Propagation.**  If both cells in (4) have color \(\tau\), then \((p',g)\) is itself a charge event.  Thus one repeated charge in the parent cloud becomes a charge event based at a translated cross support.
2. **Termination.**  If exactly one cell in (4) has color \(\tau\), then the pair \((e_B,e_C)\) is bichromatic.  Record this aligned opposite-child pair as a terminal token.

The forbidden third case, in which both cells have color \(-\tau\), is exactly what the local source corner excludes.

This produces an exact linear version of the earlier quadratic cloud estimate.  If

\[
k(p)=|G_+(p)|+|G_-(p)|
\]

and

\[
W(p)=\mathbf1_{\{G_+(p)\ne\varnothing\text{ and }G_-(p)\ne\varnothing\}},
\]

then the number of consecutive links over the two color lists is

\[
(k(p)-1)_+-W(p).
\tag{5}
\]

Every one of these links propagates or terminates.  Therefore

\[
(k(p)-1)_+
=W(p)+P(p)+H(p),
\tag{6}
\]

where \(P(p)\) and \(H(p)\) count propagation and terminal occurrences from this anchored cloud.  Unlike the all-pairs inequality, (6) spends only one child relation per unit of repeated load.

The propagation has genuine offset descent:

\[
0<g=d_{i+1}-d_i<d_{i+1}.
\tag{7}
\]

Thus iterating a single occurrence cannot cycle while its offset strictly decreases.

## 3. Global summation and the convergence multiplicity

Let

\[
R=\sum_{p\in C\times B}(k(p)-1)_+,
\qquad W=\sum_pW(p).
\]

Summing (6) gives

\[
R=W+P+H,
\tag{8}
\]

where \(P,H\) count occurrences, not distinct descendant events or distinct terminal tokens.

For a charge event \(\eta=(p',g)\), let \(\nu_P(\eta)\) be the number of parent consecutive links that propagate to it.  For a physical aligned bichromatic child pair \(\xi=(e_B,e_C)\), let \(\nu_H(\xi)\) be the number that terminate at it.  Then

\[
P=\sum_{\eta}\nu_P(\eta),
\qquad
H=\sum_{\xi}\nu_H(\xi).
\tag{9}
\]

These multiplicities are the remaining global issue.  Offset descent prevents directed cycles, but it does not prevent many parent links from converging to one smaller event.

The fan-in can be described exactly.  Fix a descendant event

\[
\eta=(q,g),\qquad q=(c',u').
\]

A parent at backward distance \(d\) must be

\[
p_d=q-(d,d)=(c'-d,u'-d),
\tag{10}
\]

and the two translated supports in its consecutive link are the fixed cells

\[
q,\qquad q+(g,g).
\]

The value of \(d\) is not determined by \(\eta\).  Distinct anchors \(p_d\) can therefore produce the same descendant charge event.

There is a finite Sidon restriction on this fan-in.  Split the predecessor distances according to the color of \(p_d\).  For either fixed sign, the cells \(p_d\) lie in one signed color class on the numerical diagonal of \(q\).  Hence their distance set is Sidon: all positive differences between predecessor distances are distinct.  If all marks lie in an interval of span \(L\), the elementary Sidon pair count gives

\[
{s\choose2}\le L-1
\]

for \(s\) predecessor anchors of one sign, and therefore

\[
\nu_P(\eta)\le 2\left(\frac{1+\sqrt{1+8(L-1)}}2\right)
<2\sqrt{2L}+2.
\tag{11}
\]

The same statement on a dyadic distance band of width \(H\) gives only \(O(\sqrt H)\) same-sign predecessors.  This is a real restriction supplied by the one source coloring, but at \(L\le99994\) it is far too large to yield a coefficient \(10\).

Terminal tokens have an analogous convergence issue.  A fixed pair of gap-\(g\) child cells in \(V(B)\times V(C)\) can arise from several backward anchors \(p_d\); the same signed-diagonal argument controls each sign class of anchors only by a Sidon-size bound, again of square-root rather than constant order.

## 4. A scale-local form

The descent can be made quantitative without claiming a constant.  For an integer \(s\ge0\), restrict a parent color list to offsets

\[
2^s\le d<2^{s+1}.
\]

Put

\[
K_{p,\tau,s}=|G_\tau(p)\cap[2^s,2^{s+1})|,
\qquad
R_s=\sum_{p,\tau}(K_{p,\tau,s}-1)_+.
\]

Consecutive offsets in each restricted list produce a descendant gap \(g<2^s\), so every propagated occurrence moves to a strictly lower dyadic scale.  If \(P_s,H_s\) count the resulting propagation and terminal occurrences, the same dichotomy gives the exact identity

\[
R_s=P_s+H_s
=\sum_{t<s}\sum_{\eta\text{ at scale }t}\nu_{s\to t}(\eta)
+\sum_\xi\nu^H_s(\xi).
\tag{12}
\]

The omitted part of the original load is explicit: one free event for each nonempty signed cloud in each scale.  Formula (12) supplies a triangular scale recursion for all within-scale repetitions; there is no upward or same-scale propagation.

What it does not supply is a bounded column sum for the transition multiplicities \(\nu_{s\to t}\).  Estimate (11) permits a lower-scale event to receive \(O(2^{s/2})\) parents from scale \(s\).  Summing this loss, even with \(L\le99994\), does not approach a universal factor \(10\).

## 5. Exact obstruction to an H10 aggregate from this route

The completed mechanism has three favorable features:

* it uses the actual common source coloring on \(V(B)\), \(V(C)\), and the cross block;
* every repeated support charge uses exactly one consecutive child relation;
* every propagation strictly decreases the offset, and every nonpropagating relation ends at an actual bichromatic aligned child pair.

To turn it into a bound such as \(T(A)\le10M(A)\), one still needs an amortized convergence estimate of the form

\[
\sum_\eta(\nu_P(\eta)-1)_+
+\sum_\xi(\nu_H(\xi)-1)_+
\le \text{a linear budget in physical source cells or corners}.
\tag{13}
\]

Neither signed-Golomb uniqueness nor dyadic descent proves (13): they bound the set of predecessors to one target by \(O(\sqrt L)\), and different targets may realize their bounds independently.  The obstruction is not a cycle or an unequal-step substitution; it is a convergent fan of translated parent clouds onto the same smaller child event.

Thus (6)-(12) are a usable weighted framework for a later global potential, but the present approach stops at the explicit fan-in term (13).  No bound on \(U\), \(2U+V\), or \(T(A)\) is claimed.
