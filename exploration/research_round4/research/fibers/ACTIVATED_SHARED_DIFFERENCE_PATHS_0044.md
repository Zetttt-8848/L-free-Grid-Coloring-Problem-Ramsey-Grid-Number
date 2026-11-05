# Overlap descent for activated shared differences

Let \(W(S)\) be a proper weak two-color triangle with diagonal partition
\(S=B\sqcup C\). For a shared positive difference \(h\), write its unique
\(B\)- and \(C\)-pairs as
\[
[b_h,b_h+h],\qquad [c_h,c_h+h],
\]
and put \(\sigma_h=b_h-c_h\). The pair is interlaced exactly when
\(0<|\sigma_h|<h\). This note records the one canonical descent supplied
by an occupied outer position, and the precise obstruction to turning that
descent into a bounded-reuse charge to
\[
\delta=(U-2\rho)+(2|B||C|-N)+(U-Q).
\]

The exclusive-continuation theorem from
`INTERLACED_SHARED_PAIR_COMPLETION_0044.md` is used as input. In
particular, an interlaced shared difference has at most one occupied outer
position, so it supports at most one activated seed across both class
roles.

## 1. The canonical overlap successor

Define the overlap length
\[
\tau(h)=h-|\sigma_h|.                              \tag{1}
\]
Thus \(1\leq\tau(h)<h\). If, after exchanging \(B,C\), the pairs are
normalized as
\[
C:\{r,r+h\},\qquad B:\{r+p,r+h+p\},
\qquad 0<p<h,                                      \tag{2}
\]
then \(\tau(h)=h-p\). The two possible activations have the following
side resources:
\[
\begin{array}{c|c|c}
\text{occupied outer mark}&\text{forced same-class side pair}
  &\text{its length}\\ \hline
r+2h\in B&\{r+h+p,r+2h\}\subset B&h-p\\
r+p-h\in C&\{r+p-h,r\}\subset C&h-p.
\end{array}                                         \tag{3}
\]
This gives a canonical successor resource for every activated shared
difference; no choice of a missing position or of an alternative pair-sum
match is involved.

**Overlap-descent lemma.** Form a directed graph whose vertices are the
activated shared differences. From \(h\), draw an edge to \(\tau(h)\) when
\(\tau(h)\) is itself activated. Then:

1. every vertex has outdegree at most one;
2. every edge strictly decreases the positive integer label;
3. the graph is acyclic, and every directed path starting at \(h\) has at
   most \(h-1\) edges;
4. if \(\tau(h)\) is not shared, the pair displayed in (3) is one specific
   resource counted by \(U-2\rho\);
5. if \(\tau(h)\) is shared but inactive, the descent stops at a shared
   difference and none of the three summands of \(\delta\) receives an
   automatic unit from (1)--(3).

The first three assertions follow from (1) and from the one-seed-per-shared-
difference theorem. For the fourth, (3) is a pair resource in one class
whose difference is absent from the other class, which is exactly one unit
of \(U-2\rho\). The fifth is a statement about the limit of this argument:
sharedness uses both same-class difference resources, while inactivity by
itself asserts neither a deficient mixed query nor an unused pair-sum
resource.

Thus pair-start displacement does orient all compatible activated chains,
and span makes them terminate. It does not yet make them terminate
injectively in the defect: paths may merge before termination, and they may
stop at an inactive shared difference.

## 2. Arbitrarily large merging is allowed by the diagonal geometry

The failure of a reuse bound is not merely that (1) forgot a convenient
parameter. The Golomb conditions and all of the local occupied/absent
positions from exclusive continuation allow arbitrarily many activated
predecessors to have the same overlap successor resource.

Fix integers \(M\geq5\) and \(m\geq1\), put
\[
H=\{M,M^2,\ldots,M^m\},
\]
and define the disjoint diagonal sets
\[
B=\{0,1\}\cup\{-h:h\in H\},\qquad
C=\bigcup_{h\in H}\{1-2h,1-h\}.                  \tag{4}
\]
Both sets are Golomb. For \(B\), its positive differences are of the four
forms
\[
1,\quad h,\quad h+1,\quad h_j-h_i\quad(i<j).       \tag{5}
\]
The numbers \(h+1\) are the only nonunit entries congruent to
\(1\pmod M\). Among the remaining entries, \(M\)-adic valuation separates
a power from a difference of two powers and uniquely recovers the lower
and upper exponents of a difference. Hence (5) has no repetition.

After the affine change \(x\mapsto1-x\), the set \(C\) becomes
\[
D=\{M^i,2M^i:1\leq i\leq m\}.                    \tag{6}
\]
This is Golomb as well. A cross-exponent difference has the unique form
\(aM^j-bM^i\), where \(j>i\) and \(a,b\in\{1,2\}\). Its \(M\)-adic
valuation gives \(i\), its reduced residue modulo \(M\) gives \(b\), and
then the remaining equality gives \(a,j\). A same-exponent difference is
\(M^i\) and cannot equal a cross-exponent difference because the latter's
reduced residue is \(-1\) or \(-2\pmod M\). Finally, (4) is disjoint
because all elements of \(C\) are \(1\pmod M\), whereas the only such
element of \(B\) is \(1\), which is larger than every element of \(C\).

For every \(h\in H\), normalize a shared \(h\)-pair by
\[
r=1-2h,\qquad p=h-1.
\]
Then
\[
C:\{1-2h,1-h\},\qquad B:\{-h,0\},               \tag{7}
\]
are interlaced \(h\)-pairs, and their right outer candidate is the occupied
mark \(1\in B\). Their left outer candidate and forced reflected middle
are respectively
\[
q_-=-2h,\qquad v_+=2-2h.                          \tag{8}
\]
Both are absent from \(B\cup C\): the first has residue \(0\pmod M\) but
is neither \(0\) nor a negative power of \(M\), while the second has
residue \(2\pmod M\). Thus the construction respects the two distinct
holes required by exclusive continuation. Nevertheless every one of these
\(m\) activated configurations has
\[
\sigma_h=h-1,\qquad \tau(h)=1,
\]
and (3) is always the same \(B\)-pair \(\{0,1\}\). Its length \(1\) is
not a \(C\)-difference, since every \(C\)-difference is divisible by \(M\).
Consequently the overlap descent would charge all \(m\) activations to the
same single resource of \(U-2\rho\).

This family is a diagonal Golomb configuration satisfying the local seed
occupancies and the two forced holes. No proper coloring of its full weak
triangle is asserted. Its role is exact: Golomb uniqueness, pair-start
displacement, decreasing span, and the local exclusive-continuation
consequences do not imply bounded terminal reuse. Any proof that rules out
this fan in a proper weak triangle must use additional mixed-cell colors or
another global compatibility condition.

## 3. The remaining path gap

The overlap-successor construction therefore reduces a path argument to
two concrete missing statements. One would need either

* a constant bound, using actual weak-cell colors, on the number of
  activated \(h\) whose side pair in (3) is a fixed same-class resource; or
* a secondary injective charge for all but constantly many arrivals at
  that resource, and for a descent that stops at an inactive shared
  difference.

The three defect totals alone do not supply either statement. The fan
(4)--(8) shows unbounded merging into one \(U-2\rho\) unit at the exact
place where the decreasing-span argument terminates. It does not refute a
bound \(K_{\rm seed}\leq c\delta\), because the same configuration may pay
through other defect resources, and properness may impose further
constraints. It identifies the additional theorem a successful activated-
path proof must establish.
