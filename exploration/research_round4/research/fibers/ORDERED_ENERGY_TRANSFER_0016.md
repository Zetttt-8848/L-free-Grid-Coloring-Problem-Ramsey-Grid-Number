# Ordered energy transfer through interval split trees (checkpoint 0016)

Let
\[
A=\{a_1<\cdots<a_m\},\qquad M=\binom m2,
\]
and, for (d>0), let
\[
r_A(d)=|\{x:x,x+d\in A\}|,
\qquad
T=\sum_{d>0}\binom{r_A(d)}2.
\]
Write (P_3) for the number of three-term arithmetic progressions in (A), and write (D) for the number of quadruples
\[
u<b<c<v,\qquad u+v=b+c.
\]
The standard separation of two equal-difference pairs according to whether they use three or four marks gives
\[
T=2D+P_3. \tag{1}
\]
Also (P_3\le M), since a three-term progression is determined by its two endpoints.

For two disjoint consecutive source blocks (B<C), put
\[
U(B,C)=\sum_{d>0}r_B(d)r_C(d).
\]
Every summand selects (u<b) in (B) and (c<v) in (C) with (b-u=v-c). Consequently
\[
U(B,C)=|\{(u,b,c,v)\in D:u,b\in B, c,v\in C\}|. \tag{2}
\]
Thus the parameter in the proposed transfer can be written
\[
\lambda(A)=\max_{B<C}\frac{U(B,C)}{|B||C|}, \tag{3}
\]
where the maximum runs over all nonempty consecutive subinterval blocks, not merely prefixes and suffixes of all of (A).

## Interval-tree decomposition

An **interval split tree** on (A) is a rooted binary tree whose leaves, from left to right, are (a_1,\ldots,a_m), and in which every internal node is a consecutive block (I) split into two nonempty consecutive children (L_I<R_I).

There is an exact pair-budget identity
\[
\sum_{I\text{ internal}} |L_I||R_I|=M. \tag{4}
\]
Indeed, every unordered pair of leaves is separated at exactly one node, its least common ancestor.

Now assign each additive quadruple (e=(u,b,c,v)) to the least tree node containing all four of its marks. At that node the four marks are distributed between the two children in one of the patterns
\[
1+3,\qquad 2+2,\qquad 3+1.
\]
In the (2+2) case, order forces (u,b\in L_I) and (c,v\in R_I), so (e) is counted by (U(L_I,R_I)). It cannot be counted at any other node. Conversely, every quadruple counted by (U(L_I,R_I)) has (I) as its least containing node and is of this (2+2) type.

Let (E_{\mathcal T}) be the number of quadruples whose least containing node splits them (1+3) or (3+1). Then
\[
D=E_{\mathcal T}+\sum_{I\text{ internal}}U(L_I,R_I). \tag{5}
\]
Equations (3)--(5) yield the following complete transfer with an explicit defect.

**Interval-tree transfer.** For every interval split tree (\mathcal T),
\[
D\le \lambda(A)M+E_{\mathcal T}, \tag{6}
\]
and hence
\[
T\le 2\lambda(A)M+2E_{\mathcal T}+P_3. \tag{7}
\]

The proof is just
\[
\sum_I U(L_I,R_I)
\le \lambda(A)\sum_I|L_I||R_I|
=\lambda(A)M
\]
inserted into (5) and then (1). Notice that this uses the full subinterval definition of (\lambda(A)): every sibling pair in the tree is an admissible pair of blocks.

Define the intrinsic ordered splitting defect
\[
\varepsilon(A)=\min_{\mathcal T}E_{\mathcal T}. \tag{8}
\]
Then (7) gives the reusable bound
\[
T\le 2\lambda(A)M+2\varepsilon(A)+P_3. \tag{9}
\]
In particular, the proposed inequality
\[
T\le (1+2\lambda(A))M \tag{10}
\]
follows from the purely ordered condition
\[
2\varepsilon(A)\le M-P_3. \tag{11}
\]
The stronger, simpler sufficient condition (\varepsilon(A)=0) says that (A) admits a recursive consecutive splitting in which every additive quadruple is first split (2+2).

## Exact scope of the remaining issue

This decomposition identifies why averaging only over a global cut loses the small-middle-gap configurations. Such a quadruple is visible to a cut exactly when the cut lies between its two middle marks. In a recursive cut scheme, it disappears permanently when an earlier split peels off only one of its four marks; this is exactly a (1+3) or (3+1) contribution to (E_{\mathcal T}).

Therefore the proposed transfer is reduced to a precise additive ordering problem: prove (11), or find a source set for which every interval split tree has
\[
2E_{\mathcal T}>M-P_3.
\]
The local rectangle estimates alone control the (2+2) term in (5) and give no charge for the other two orientations. A proof must exploit additive compatibility among the lost quadruples to build a lower-defect tree, or charge those losses to the unused endpoint-pair budget (M-P_3). No such general charging rule was obtained in this bounded attempt.

Thus (9) is a complete parametric auxiliary theorem, while (11) is the isolated missing quantitative implication needed to recover (10) from interval cuts alone.

## Addendum: the slack-free defect condition fails for intervals

The condition (11) is not available for arbitrary ordered sets. Take
\[
A=[n]=\{1,\ldots,n\}.
\]
For consecutive blocks of lengths \(b\le c\), translation invariance gives
\[
\begin{aligned}
U_{b,c}
  &=\sum_{d=1}^{b-1}(b-d)(c-d)\\
  &=\frac{b(b-1)(3c-b-1)}6. \tag{12}
\end{aligned}
\]
This cross term fits inside a cubic telescoping budget:
\[
U_{b,c}\le \frac{(b+c)^3-b^3-c^3}{18}. \tag{13}
\]
Indeed, the right side is \(bc(b+c)/6\), while
\[
U_{b,c}\le \frac{b^2(3c-b)}6,
\]
and
\[
b^2(3c-b)\le bc(b+c)
\quad\Longleftrightarrow\quad
0\le(c-b)^2.
\]

Let
\[
G_{\mathcal T}([n])
   =\sum_{I\text{ internal}}U(L_I,R_I)
\]
be the number of quadruples captured \(2+2\) by a particular interval split tree, and let \(G(n)\) be its maximum over all such trees. Then
\[
G(n)\le \frac{n^3}{18}. \tag{14}
\]
This follows by induction on \(n\). If the root splits \([n]\) into intervals of lengths \(b,c\), then the two subtrees and (13) give
\[
\begin{aligned}
G_{\mathcal T}([n])
 &\le \frac{b^3}{18}+\frac{c^3}{18}+U_{b,c}\\
 &\le \frac{(b+c)^3}{18}
  =\frac{n^3}{18}.
\end{aligned}
\]
The one-point base case is immediate.

For even \(n\),
\[
T([n])=\sum_{d=1}^{n-1}\binom{n-d}{2}=\binom n3
\]
and
\[
P_3([n])
 =2\binom{n/2}{2}
 =\frac{n^2}{4}-\frac n2.
\]
Using (1),
\[
D([n])
 =\frac12\left(\binom n3-P_3([n])\right)
 =\frac{n^3}{12}-\frac{3n^2}{8}+\frac{5n}{12}. \tag{15}
\]
Since \(E_{\mathcal T}=D-G_{\mathcal T}\), equations (14)--(15) imply
\[
\varepsilon([n])
\ge
\frac{n^3}{36}-\frac{3n^2}{8}+\frac{5n}{12}. \tag{16}
\]
At \(n=32\), the right side of (16) is \(4856/9\), whereas
\[
\frac{M-P_3}{2}
=\frac{496-240}{2}
=128.
\]
Thus every interval split tree on \([32]\) violates (11). The obstruction is already cubic: a split tree necessarily loses many \(1+3\) and \(3+1\) quadruples even after optimizing all its cuts.

This closes the stronger, slack-free uncolored tree-defect route. It does not disprove the proposed inequality (10): in deriving (7), all unused room in the node bounds \(U(L_I,R_I)\le\lambda(A)|L_I||R_I|\) was discarded. It also does not rule out a source class constrained by the existence of a proper coloring.

## Correct bookkeeping with node slack

Set \(\Lambda=\lambda(A)\), and for a tree \(\mathcal T\) define its accumulated block slack by
\[
S_{\mathcal T}
 =\sum_{I\text{ internal}}
   \bigl(\Lambda|L_I||R_I|-U(L_I,R_I)\bigr). \tag{17}
\]
Every summand is nonnegative because each sibling pair is among the subinterval cuts in the definition of \(\Lambda\). From (4),
\[
\sum_I U(L_I,R_I)=\Lambda M-S_{\mathcal T}. \tag{18}
\]
Combining (1), (5), and (18) gives the exact identity
\[
T
 =2\Lambda M+2(E_{\mathcal T}-S_{\mathcal T})+P_3. \tag{19}
\]
Consequently, for any interval split tree, the desired transfer (10) is equivalent to
\[
2\bigl(E_{\mathcal T}-S_{\mathcal T}\bigr)
\le M-P_3, \tag{20}
\]
or, in charging form,
\[
E_{\mathcal T}
\le S_{\mathcal T}+\frac{M-P_3}{2}. \tag{21}
\]
The difference \(E_{\mathcal T}-S_{\mathcal T}=D-\Lambda M\) is independent of the chosen tree. Thus changing the tree can redistribute lost quadruples against unused block slack, but cannot by itself improve the final difference.

The interval calculation shows that a bound on \(E_{\mathcal T}\) alone cannot prove the universal transfer. A viable cut proof must retain \(S_{\mathcal T}\), or use additional restrictions from a proper source coloring. Those variants remain open here.
