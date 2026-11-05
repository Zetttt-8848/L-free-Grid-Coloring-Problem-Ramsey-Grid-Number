# Additive interval transfer through equal-sum fibers

## 1. Sum-fiber form of the proposed transfer

Let

\[
A=\{a_1<\cdots<a_m\},\qquad M={m\choose2}.
\]

For an integer \(s\), let

\[
\mathcal R_s
=\{\{x,y\}\subset A:x<y,\ x+y=s\},
\qquad k_s=|\mathcal R_s|.
\]

The distinct-pair sum fibers partition the \(M\) unordered pairs, so

\[
\sum_s k_s=M.
\tag{1}
\]

Two distinct representations of the same sum use four distinct marks and are necessarily nested.  Therefore

\[
D=\sum_s{k_s\choose2}.
\tag{2}
\]

Put

\[
q_s=\mathbf1_{\{s\text{ is even and }s/2\in A\}}.
\]

Every pair in \(\mathcal R_s\) gives a three-term progression precisely when \(q_s=1\).  Hence

\[
P_3=\sum_s q_sk_s.
\tag{3}
\]

Using \(T=2D+P_3\), equations (1)-(3) give

\[
T-(1+2\Lambda)M
=
\sum_s k_s(k_s-2+q_s)-2\Lambda M.
\tag{4}
\]

Consequently the desired transfer

\[
T\le(1+2\Lambda)M
\tag{5}
\]

is exactly

\[
\boxed{\quad
\sum_s k_s(k_s-2+q_s)\le2\Lambda M.
\quad}
\tag{6}
\]

This identifies the boundary allowance precisely.  A sum fiber with no midpoint mark (\(q_s=0\)) uses its first two representations for free; a sum fiber with a midpoint mark uses only its first representation for free.

There is only one negative case in (6): \(q_s=0,k_s=1\), which contributes \(-1\).  Let

\[
Z_0=|\{s:q_s=0,\ k_s=1\}|
\]

and define

\[
H=
\sum_{\substack{s:q_s=1}}k_s(k_s-1)
+
\sum_{\substack{s:q_s=0\\k_s\ge3}}k_s(k_s-2).
\tag{7}
\]

Then (6) is equivalently

\[
H-Z_0\le2\Lambda M.
\tag{8}
\]

Thus singleton non-AP sum fibers provide an exact boundary credit; all other work is concentrated in heavy sum fibers.

## 2. Residual clique interpretation

For each \(s\), regard the representations in \(\mathcal R_s\) as the vertices of a clique.  An edge of this clique is exactly one additive quadruple.

If \(q_s=1\), give every clique edge weight \(1\).  Its total weight is

\[
{k_s\choose2}=\frac{k_s(k_s-1)}2.
\]

If \(q_s=0\) and \(k_s\ge3\), give every clique edge weight

\[
\frac{k_s-2}{k_s-1}.
\]

Its total weight is

\[
{k_s\choose2}\frac{k_s-2}{k_s-1}
=\frac{k_s(k_s-2)}2.
\]

Equivalently, the base \(M\)-budget removes a fractional one-factor of total weight \(k_s/2\) from a non-AP clique and removes nothing from an AP clique, since its base allowance is already consumed by \(P_3\).

Let \(\mathcal Q_{\rm res}\) denote this weighted family of residual additive quadruples.  Then

\[
w(\mathcal Q_{\rm res})=\frac H2.
\tag{9}
\]

In this language, (8) asks for

\[
w(\mathcal Q_{\rm res})
\le \Lambda M+\frac{Z_0}{2}.
\tag{10}
\]

The advantage of (10) is that it specifies which part of each dense additive fiber must be seen by interval cuts; it does not ask a cut argument to pay again for the first one or two representations.

If \(\Lambda=0\), every \(k_s\le1\): two representations of one sum would themselves be visible in the cut between their two left and two right endpoints.  Then \(D=0\) and \(T=P_3\le M\).  Hence the remaining discussion may assume \(\Lambda>0\).

## 3. One heavy sum fiber produces a nested cut

Fix \(s\) with \(k=k_s\), and order its representations as

\[
x_1<x_2<\cdots<x_k<y_k<\cdots<y_2<y_1,
\qquad x_i+y_i=s.
\tag{11}
\]

Take the smallest contiguous source-index interval containing \(x_1,y_1\), and split it at any source-index gap between \(x_k\) and \(y_k\).  Call the resulting adjacent blocks \(B_s<C_s\).  Every \(x_i\) lies in \(B_s\), and every \(y_i\) lies in \(C_s\).

For \(i<j\),

\[
x_j-x_i=y_i-y_j.
\]

Thus the \(B_s\)-edge \((x_i,x_j)\) and the \(C_s\)-edge \((y_j,y_i)\) have the same positive difference.  Every pair of representations in (11) is counted by \(U(B_s,C_s)\), and hence

\[
{k_s\choose2}
\le U(B_s,C_s)
\le \Lambda |B_s||C_s|.
\tag{12}
\]

More locally, (12) applies to any consecutive subfamily of the nested list (11), using the minimal outer interval and a split through that subfamily's central gap.  This is the basic Whitney rectangle supplied by a heavy sum fiber.

The local estimate is quadratic in \(k_s\), as required by (7).  The difficulty is entirely in summing its block capacities.

## 4. Fractional Whitney cover that would complete the proof

Let \(\mathscr C\) be the family of all adjacent-block cuts of all contiguous source-index intervals.  A cut \(C=(B_C,C_C)\) sees a residual quadruple when its two left endpoints lie in \(B_C\) and its two right endpoints lie in \(C_C\).

Suppose one can choose nonnegative cut weights \(\theta_C\) such that

\[
\sum_{\substack{C\in\mathscr C\\C\text{ sees }Q}}\theta_C
\ge w(Q)
\qquad(Q\in\mathcal Q_{\rm res})
\tag{13}
\]

and

\[
\sum_{C\in\mathscr C}\theta_C|B_C||C_C|
\le M+\frac{Z_0}{2\Lambda}.
\tag{14}
\]

Then

\[
\begin{aligned}
\frac H2
&=\sum_Qw(Q)\\
&\le\sum_C\theta_CU(B_C,C_C)\\
&\le\Lambda\sum_C\theta_C|B_C||C_C|\\
&\le\Lambda M+\frac{Z_0}{2},
\end{aligned}
\]

which is (10) and proves the transfer.

Therefore (13)-(14) are a complete fractional interval-weighting target.  They retain the exact \(M\)-boundary allowance rather than using a slack-free split-tree defect.

## 5. The central-filler obstruction

Applying (12) once per heavy sum does not establish (14).  The blocks \(B_s,C_s\) contain not only the endpoints from \(\mathcal R_s\), but every source mark between the outermost representation and the chosen central split.  These **central fillers** contribute to \(|B_s||C_s|\) even though they need not represent the sum \(s\).

The same physical pair of filler marks can lie in the product \(B_s\times C_s\) for many different sums \(s\).  Consequently

\[
\sum_s|B_s||C_s|
\]

has no evident \(O(M)\) bound.  Passing to consecutive subfamilies in (11) shrinks the outer interval, but cross-edges between two such subfamilies then require a larger cut that restores the intervening fillers.  This is the precise Whitney overlap that remains.

The obstruction can be recorded as a pair multiplicity.  For a proposed weighted cover, define

\[
\Omega(a_i,a_j)
=
\sum_{\substack{C\in\mathscr C\\a_i\in B_C,\ a_j\in C_C}}\theta_C.
\tag{15}
\]

Then the left side of (14) is exactly

\[
\sum_{i<j}\Omega(a_i,a_j).
\tag{16}
\]

Condition (14) needs average multiplicity at most \(1\), apart from the explicit singleton-sum credit.  The local nested-clique estimate (12) controls how much residual quadruple weight a cut sees, but it does not control the multiplicities (15) generated by cuts chosen for other sum fibers.

A standard dyadic choice limits the number of scales at which one pair is used, but only gives logarithmic overlap in this formulation.  Since the required coefficient in (14) is \(1\), a logarithmic Whitney cover is insufficient for (5), even under the more generous downstream target \(\Lambda\le4.5\).

## 6. Scope

The completed new reduction is (6)-(10): the \(M\) and \(P_3\) terms remove an exact fractional boundary layer from every equal-sum clique, leaving only the residual heavy-fiber weight \(H/2\) for interval cuts.  Every consecutive part of a heavy fiber supplies the concrete nested cut (12).

The remaining pure-additive statement is the fractional capacity bound (14), equivalently an average-one bound for the pair multiplicities (15), while satisfying the residual coverage (13).  Central fillers shared by cuts for different sums are the explicit obstruction.  No complete proof of the transfer and no counterfamily to it is obtained here.
