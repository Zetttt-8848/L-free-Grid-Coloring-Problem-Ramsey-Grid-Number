# A nonlinear proper coloring of every separated four-cube

Let positive integer weights satisfy
\[
w_{i+1}>2\sum_{j\leq i}w_j\qquad(1\leq i<4),       \tag{1}
\]
and put
\[
A=\left\{\sum_{i=1}^4\epsilon_iw_i:
          \epsilon_i\in\{0,1\}\right\}.             \tag{2}
\]
This note gives one fixed subset-label rule that properly two-colors the
strict triangle \(V(A)\) for every choice of weights satisfying (1).
The rule was extracted from the unrestricted four-cube discovery, but the
construction and verification below are symbolic and do not use the
numerical solver status.

## 1. Three-table coloring rule

Identify a subset of \([3]\) with its mask in \(\{0,\ldots,7\}\), with
bits corresponding to \(w_1,w_2,w_3\). Condition (1) orders masks by their
largest differing bit. Split the four-cube into
\[
S=\left\{\sum_{i=1}^3\epsilon_iw_i\right\},
\qquad A=S\sqcup(S+w_4).                            \tag{3}
\]
For two local masks \(u<v\), define the lower- and upper-copy colors
\(L(v,u)\) and \(U(v,u)\) by the following row words. The word on row \(v\)
lists the colors at columns \(u=0,1,\ldots,v-1\):
\[
\begin{array}{c|c|c}
v&L(v,0)\cdots L(v,v-1)&U(v,0)\cdots U(v,v-1)\\ \hline
1&1&0\\
2&10&01\\
3&100&111\\
4&1001&0110\\
5&10110&11001\\
6&110101&101010\\
7&0001111&1000000.
\end{array}                                        \tag{4}
\]
For a cross-copy cell, let \(r\) be its upper local mask and \(c\) its
lower local mask. Define \(X(r,c)\) by
\[
\begin{array}{c|cccccccc}
r\backslash c&0&1&2&3&4&5&6&7\\ \hline
0&1&0&0&1&0&1&1&0\\
1&1&0&1&1&1&1&0&0\\
2&1&1&0&1&1&0&1&0\\
3&0&0&0&1&0&0&0&1\\
4&1&1&1&0&0&1&1&0\\
5&0&0&1&0&0&1&0&0\\
6&0&1&1&0&1&0&0&0\\
7&0&1&1&0&1&0&1&0.
\end{array}                                        \tag{5}
\]
The coloring \(z\) of \(V(A)\) is
\[
\begin{aligned}
z(s_v,s_u)&=L(v,u) &&(u<v),\\
z(w_4+s_v,w_4+s_u)&=U(v,u) &&(u<v),\\
z(w_4+s_r,s_c)&=X(r,c) &&(r,c\in\{0,\ldots,7\}),
\end{aligned}                                      \tag{6}
\]
where \(s_u\) is the subset sum encoded by mask \(u\). Since
\(w_4>2\operatorname{span}(S)\), every cross-copy cell in (6) has the
displayed orientation.

## 2. Signed-support classification

Condition (1) implies 2-dissociation:
\[
\sum_{i=1}^4 a_iw_i=0,\quad a_i\in\{-2,-1,0,1,2\}
\quad\Longrightarrow\quad a_i=0\ \text{for all }i. \tag{7}
\]
Indeed, the contribution of the largest index with \(a_i\ne0\) strictly
dominates the sum of all lower-index contributions.

For a positive difference inside \(S\), its signed support is a vector
\(\delta\in\{-1,0,1\}^3\) whose highest nonzero coordinate is \(+1\).
Write \(t=|\operatorname{supp}\delta|\). Equality of two differences is
equivalent, by (7), to equality of their signed supports. The cells
representing a fixed \(\delta\) are indexed by arbitrary common bits on
the \(3-t\) unused coordinates, so their number is
\[
m_t=2^{3-t}.                                       \tag{8}
\]
The number of positive signed supports of size \(t\) is
\[
n_t=\binom3t2^{t-1},
\qquad (n_1,n_2,n_3)=(3,6,4).                      \tag{9}
\]

This gives an exhaustive weight-independent classification of the corners.
There are
\[
\sum_t n_t\binom{m_t}{2}=3\binom42+6\binom22=24    \tag{10}
\]
strict corners inside each copy. Cross-matrix corners choose one row
representation and one column representation of the same signed support,
and bridge corners independently choose one lower- and one upper-copy
representation. Each family therefore has
\[
\sum_t n_tm_t^2=3\cdot16+6\cdot4+4=76             \tag{11}
\]
corners.

## 3. Exact truth-table certificate

Apply the three tables (4)--(5) to the signed-support classes above. In the
following certificate, a word gives the three colors in corner order and
the parenthesized number is its multiplicity. For \(L,U\), the first two
colors are the equal-difference endpoint cells in increasing-start order
and the third is their outer completion. For \(X\), the word is
\[
X(r,c),\ X(r+h,c),\ X(r+h,c+h).
\]
For a bridge it is
\[
L(u+h,u),\ X(v+h,u),\ U(v+h,v).
\]
Direct substitution by support size gives
\[
\begin{array}{c|c|l}
\text{family}&t&\text{words with multiplicities}\\ \hline
L&1&001(3),010(4),011(2),101(6),110(3)\\
L&2&011(3),100(2),110(1)\\ \hline
U&1&001(3),011(6),100(6),110(3)\\
U&2&100(3),101(3)\\ \hline
X&1&001(7),010(5),011(8),100(15),101(4),110(9)\\
X&2&001(1),010(9),011(2),100(5),101(7)\\
X&3&010(1),011(1),100(2)\\ \hline
\text{bridge}&1&001(6),010(12),011(6),100(8),101(12),110(4)\\
\text{bridge}&2&010(5),011(5),100(6),101(7),110(1)\\
\text{bridge}&3&001(1),100(1),110(2).
\end{array}                                        \tag{12}
\]
The multiplicities in the first two blocks sum to \(24\) each, and those
in the last two blocks sum to \(76\) each, agreeing with the exhaustive
counts (10)--(11). Neither \(000\) nor \(111\) occurs.

## 4. Properness theorem

**Theorem.** For every weight sequence satisfying (1), the rule (4)--(6)
is a proper two-coloring of \(V(A)\).

**Proof.** Use the exact separated-copy compatibility classification with
lower coloring \(L\), upper coloring \(U\), and cross matrix \(X\).
Its internal lower and upper corners are precisely the first two families
of (12), its cross-matrix corners are precisely the third family, and its
bridge corners are precisely the fourth family. Equations (7)--(11) show
that these lists exhaust every actual positive equal-step corner for every
admissible choice of weights. Equation (12) shows that every listed corner
contains both colors. Hence all corners of \(V(A)\) are proper. \(\square\)

For the concrete discovery weights
\[
(w_1,w_2,w_3,w_4)=(1,3,9,27),
\]
the source is
\[
\{0,1,3,4,9,10,12,13,27,28,30,31,36,37,39,40\},
\]
and (4)--(6) reproduces the discovered strict-cell assignment. The theorem
is stronger than that one instance: the same nonlinear mask rule works
unchanged throughout the open separated-weight region (1).
