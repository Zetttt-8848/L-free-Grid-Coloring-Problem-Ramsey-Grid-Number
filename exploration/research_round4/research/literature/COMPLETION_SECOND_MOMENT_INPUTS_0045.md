# Completion second-moment inputs (0045)

This is a local dependency map for a properly two-colored strict source
\(V(A)\). For an outer cell \(q=(v,u)\), let \(D_q\) be the set of
positive equal-step end-cap decompositions
\[
((u+d,u),(v,v-d))\quad(d\in D_q),
\]
and let \(H_q\) count those whose two endpoint cells have one common color.

## 1. Three distinct levels of completion counting

### Uncolored geometry

Every source corner has one such endpoint pair and one outer completion.
Consequently the uncolored total is
\[
\sum_q |D_q|=T(A)=\sum_{d>0}{r_d\choose2}.
\tag{1}
\]
This counts all completion decompositions, without signs and without
properness.

### Arbitrary sign assignment

For any assigned signs, write \(P_q\) and \(M_q\) for the counts of
all-\(+\) and all-\(-\) endpoint decompositions, and set
\[
H_q=P_q+M_q,\qquad S_q=P_q-M_q.
\]
The algebraic identity
\[
H_q^2-S_q^2=4P_qM_q
\tag{2}
\]
is unconditional. The first moment is also a fiber count:
\[
\sum_q H_q=
\sum_d\left[{|F_d^+|\choose2}+{|F_d^-|\choose2}\right]
={1\over4}\sum_d(r_d^2+s_d^2-2r_d).
\tag{3}
\]
Equation (3) only counts equal-sign endpoint pairs; it does not impose the
color required at their completion. Thus arbitrary-sign data do not make
\(H_q=|S_q|\), and their second moment is not identified with an operator
norm by the saved identities.

### Proper source coloring

Properness forces an all-\(+\) pair and an all-\(-\) pair at the same
completion to demand opposite colors of that completion. Hence
\[
P_qM_q=0,\qquad H_q=|S_q|,
\qquad H_q^2=S_q^2.
\tag{4}
\]
Equivalently, with the triangular completion operator
\[
(Kz)_q={1\over2}\sum_{d\in D_q}
  \bigl(z(u+d,u)+z(v,v-d)\bigr),
\]
the exact proper-only pointwise identity is
\[
H_q=-z_q(Kz)_q=|(Kz)_q|.
\tag{5}
\]
The existing global second-moment identity is therefore
\[
\boxed{\ \sum_q H_q^2=\sum_q S_q^2=\|Kz\|_2^2\ }.
\tag{6}
\]
Together with (3), it gives the exact binomial moment expression
\[
\sum_q{H_q\choose2}
={1\over2}\left[
 \|Kz\|_2^2-
 {1\over4}\sum_d(r_d^2+s_d^2-2r_d)
\right].
\tag{7}
\]
The saved notes do not provide a general span- or source-size upper bound
for the right side of (6) or (7).

## 2. Existing aggregate second-moment inequalities

For any selected proper completion-fan family with
\(H=\sum_qH_q\) and \(M=|V(A)|\), Cauchy gives
\[
\sum_q{H_q\choose2}\ge {1\over2}\left({H^2\over M}-H\right).
\tag{8}
\]
For a dyadic band \(I_H=\{d:H\le d<2H\}\), the notation
\(A_H=\sum_QH_Q\) gives the same lower bound with \(H=A_H\).
The saved strict-descent bound is
\[
{1\over2}\left({A_H^2\over M}-A_H\right)
\le2\mathcal B_H^{<H}
 +\sum_{1\le\delta<H}r_A(\delta)
      (|A|-r_A(\delta))^2.
\tag{9}
\]
Its right side keeps both the lower-gap bichromatic color term and the
unsupported-boundary-shift term.

For all same-colored endpoint pairs (rather than a selected fan), the
saved aggregate version is
\[
\sum_Q{H_Q\choose2}
\le2\mathcal B(A,z)+
 \sum_{\delta>0}r_A(\delta)(|A|-r_A(\delta))^2,
\tag{10}
\]
where
\[
\mathcal B(A,z)=
\sum_{d>0}\sum_{\substack{\{x,y\}\subset F_d\\
 z(x+d,x)\ne z(y+d,y)}}r_A(|x-y|).
\tag{11}
\]
The same note records
\[
\mathcal B(A,z)\le
\bigl(1+\sqrt{1+8L}\bigr)(T-H_{\rm all}),
\quad
H_{\rm all}=\sum_d\left[{|F_d^+|\choose2}+{|F_d^-|\choose2}\right],
\tag{12}
\]
using signed-fiber Golombness and span \(L\). These bounds are proper-only:
their fan closures use the forced output color. Their unresolved term is the
explicit boundary-open profile in (9)--(10), not an omitted constant.

## 3. Recorded sharp limitations

The file **fibers/DERIVATIONS.md** gives a proper six-mark source
\(A=\{1,4,8,14,18,21\}\) with an output \(q=(21,1)\) for which
\[
P_q=4,\quad M_q=0,\quad H_q=|D_q|=4.
\tag{13}
\]
Thus no universal nontrivial pointwise deficit
\(H_q\le|D_q|-1\) is available.

The file **UNBOUNDED_COMPLETION_LOAD.md** gives a proper family
\(A=C\cup(s-C)\), \(|C|=q\), whose positive difference fibers all have
size at most two, yet at \(Q=(s,0)\)
\[
H_Q=|A|-2=2q-2.
\tag{14}
\]
It records \(T(A)=q(q-1)\), \(M(A)=q(2q-1)\), and
\(T(A)/M(A)<1/2\). This rules out a proof route based on a uniform
per-completion load cap; it is not a bound on the global moments (6)--(7).

The distinction is material: (1) is uncolored incidence, (2)--(3) apply
to arbitrary signs, while (4)--(12) use one actual proper coloring and
retain its forced completion colors.

