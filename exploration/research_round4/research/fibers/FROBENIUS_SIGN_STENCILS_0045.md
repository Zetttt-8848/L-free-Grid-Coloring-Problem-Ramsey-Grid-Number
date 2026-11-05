# Frobenius sign stencils on \(S_9\)

Let
\[
S_m=\{(x,y)\in\mathbb Z_{\geq0}^2:x+y\leq m\},
\qquad
g_d=(1+X^d+Y^d)F=D_dF,
\]
where \(g_d\) is defined on \(S_{9-d}\). Work over \(\mathbb F_3\).
For a proper coloring, every nonzero corner sum is one of the two signs
\(\{1,-1\}\); a zero corner is rainbow. This note records the exact
consequence of the Frobenius stencils at scales \(1,3,9\) and \(2,6\).

## 1. Exact stencil domains

Freshman's dream gives
\[
D_d^3=1+X^{3d}+Y^{3d}=D_{3d},
\]
and hence
\[
\boxed{g_{3d}=D_d^2g_d.}                           \tag{1}
\]
Since
\[
D_d^2
=1+X^{2d}+Y^{2d}-X^d-Y^d-X^dY^d,                 \tag{2}
\]
equation (1) is the six-point signed stencil
\[
\begin{aligned}
g_{3d}(p)={}&g_d(p)+g_d(p+2de_x)+g_d(p+2de_y)\\
&-g_d(p+de_x)-g_d(p+de_y)-g_d(p+d(e_x+e_y)).
\end{aligned}                                      \tag{3}
\]
Every term in (3) exists exactly when \(p\in S_{9-3d}\). Thus the
available instances relevant here are
\[
\begin{array}{c|c|c}
d&\text{output}&\text{base domain}\\ \hline
1&g_3=D_1^2g_1&S_6\\
2&g_6=D_2^2g_2&S_3\\
3&g_9=D_3^2g_3&S_0.
\end{array}                                        \tag{4}
\]
In particular, the \(3\)-to-\(9\) stencil exists only at the origin.
Iterating the first and third lines also gives
\[
g_9(0)=D_1^8g_1(0),                               \tag{5}
\]
with all required \(g_1\)-bases lying in \(S_8\).

## 2. A boundary coupling between the two chains

The two chains meet through operator commutation:
\[
D_6g_3=D_3g_6
\]
on \(S_0\). Explicitly,
\[
g_3(0,0)+g_3(6,0)+g_3(0,6)
=g_6(0,0)+g_6(3,0)+g_6(0,3).                     \tag{6}
\]
On the other hand, (2) at \(d=3\) says
\[
\begin{aligned}
g_9(0,0)={}&g_3(0,0)+g_3(6,0)+g_3(0,6)\\
&-g_3(3,0)-g_3(0,3)-g_3(3,3).
\end{aligned}                                      \tag{7}
\]
Combining (6)--(7) proves the following exact comparison.

**Boundary Frobenius lemma.**
\[
\boxed{
g_9(0,0)
=g_6(0,0)+g_6(3,0)+g_6(0,3)
-g_3(3,0)-g_3(0,3)-g_3(3,3).
}                                                   \tag{8}
\]
All six terms on the right are actual corner sums in \(S_9\). The
asymmetry is forced by the boundary: \(g_6\) has base domain \(S_3\), so
the three displayed values exhaust the \(D_3g_6(0)\) stencil, and there is
no available translate based at \((3,3)\).

For three nonzero signs define
\[
\theta(a,b,c)=a+b+c\in\mathbb F_3.
\]
Then
\[
\theta=0\quad\Longleftrightarrow\quad
\text{the three signs are unanimous},              \tag{9}
\]
while \(\theta=1\) and \(\theta=-1\) distinguish the two majority signs.
Consequently, if all six right-hand entries in (8) are nonzero, then
\[
g_9(0)=0
\quad\Longleftrightarrow\quad
\theta(g_6(0),g_6(3e_x),g_6(3e_y))
=\theta(g_3(3e_x),g_3(3e_y),g_3(3e_x+3e_y)).
                                                            \tag{10}
\]
If \(g_9(0)\ne0\), the two types in (10) are merely required to differ.
Thus the top Frobenius comparison imposes a sign-type condition; it does
not force a zero among its seven corner sums.

## 3. A zero-free sign realization of the available stencils

The lack of a forced zero can be made exact at the stencil level. Assign
\[
\begin{array}{c|ccc}
&\text{first position}&\text{second position}&\text{third position}\\ \hline
(g_3(0),g_3(6e_x),g_3(6e_y))&1&1&1\\
(g_3(3e_x),g_3(3e_y),g_3(3e_x+3e_y))&1&1&-1\\
(g_6(0),g_6(3e_x),g_6(3e_y))&1&1&1.
\end{array}                                        \tag{11}
\]
The two sides of (6) both sum to zero, and (8) gives
\[
g_9(0)=-1.                                         \tag{12}
\]
Thus every displayed \(g_3,g_6,g_9\) value is nonzero.

Moreover, all values in (11) can be realized by their lower Frobenius
stencils without introducing a zero among the stencil inputs. In (3), an
output \(1\) is obtained by taking the positive-coefficient triad
\((1,1,1)\) and the negative-coefficient triad \((1,-1,-1)\). An output
\(-1\) is obtained by using \((1,1,1)\) and \((1,1,-1)\). The six
\(D_1^2\)-blocks based at
\[
(0,0),(6,0),(0,6),(3,0),(0,3),(3,3)
\]
are pairwise disjoint subsets of the \(g_1\)-domain \(S_8\). Likewise the
three \(D_2^2\)-blocks based at
\[
(0,0),(3,0),(0,3)
\]
are pairwise disjoint subsets of the \(g_2\)-domain \(S_7\). Hence the
required nonzero inputs can be assigned independently within each scale.

This is a sign realization of the Frobenius equations (3), the top
commutation equation (6), and the boundary identity (8). It is not asserted
to arise from one common labeling \(F\).

## 4. Exact remaining compatibility gap

The missing information is the cross-scale relation
\[
\boxed{D_2g_1=D_1g_2}                              \tag{13}
\]
on its full base domain \(S_6\), together with its translates and
consequences such as
\[
D_2g_3=D_3g_2\qquad\text{on }S_4.                 \tag{14}
\]
These equations hold because all \(g_d\) come from the same \(F\). The
zero-free construction in Section 3 deliberately treats the disjoint
\(g_1\)- and \(g_2\)-blocks independently and therefore does not certify
(13)--(14).

The bounded conclusion is that the two Frobenius chains
\[
1\longrightarrow3\longrightarrow9,
\qquad
2\longrightarrow6
\]
and their only top boundary coupling do not themselves force even one zero
corner sum. They reduce the top constraint to the majority-type comparison
(10), for which the zero-free pattern (11)--(12) is an explicit local
model. A successful five-zero argument along this route must use the
full-domain cross-scale compatibility (13), or an equivalent consequence
that prevents these independently chosen sign blocks. Properness alone
adds no local restriction to the model in Section 3, since every displayed
corner sum is nonzero.
