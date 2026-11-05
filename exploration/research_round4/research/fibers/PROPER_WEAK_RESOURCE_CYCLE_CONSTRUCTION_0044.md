# A proper weak cube with alternating difference--sum resource cycles

This note gives an explicit proper weak coloring whose diagonal pair-resource
graph contains alternating four-cycles. It closes the existence gap left by
the symbolic rectangle calculation in
`DIFFERENCE_SUM_RESOURCE_CYCLES_0044.md`.

## 1. The weak three-cube coloring

Let \(w_1,w_2,w_3\) be positive and 2-dissociated, meaning that
\[
\sum_{i=1}^3\epsilon_iw_i=0,\qquad
\epsilon_i\in\{-2,-1,0,1,2\}
\quad\Longrightarrow\quad
\epsilon_1=\epsilon_2=\epsilon_3=0.                \tag{1}
\]
For \(X\subseteq[3]\), put
\[
s_X=\sum_{i\in X}w_i,\qquad
S=\{s_X:X\subseteq[3]\}.                           \tag{2}
\]
Condition (1) makes all eight subset sums distinct. Identify a cell of
\(W(S)\) with the unordered pair of its endpoint subsets \(\{X,Y\}\).
Define its color \(z(X,Y)\in\{0,1\}\) as follows:

* on the diagonal, \(z(X,X)=|X|\pmod2\);
* if \(X\ne Y\) have the same parity, then
  \(z(X,Y)=1-(|X|\pmod2)\);
* if \(|X\mathbin{\triangle}Y|=1\), then \(z(X,Y)=1\) exactly when one
  of \(X,Y\) is \([3]\);
* if \(|X\mathbin{\triangle}Y|=3\), so \(X,Y\) are complementary, then
  \(z(X,Y)=1\) for a singleton--doubleton pair and \(z(X,Y)=0\) for
  the empty--full pair.

Distinct opposite-parity subsets have odd symmetric-difference size, so
the last two rules exhaust that case.

**Proper weak cube theorem.** The preceding rule is a proper two-coloring
of \(W(S)\).

For offset zero, two diagonal cells of the same color come from subsets of
the same parity, and their strict completion has the opposite color by the
second rule. Diagonal cells of opposite colors are already nonmonochromatic.

For a positive offset, equality of two numerical differences gives a
relation with coefficients in \(\{-2,-1,0,1,2\}\). By (1), the signed
generator supports agree coordinatewise. Thus every corner is obtained
from disjoint signed supports, and after removing coordinates common to all
three cells its active support has size two or three. The complete color
table, in the order (first equal-offset cell, outer completion, last
equal-offset cell), is
\[
\begin{array}{c|c}
\text{support type}&\text{color words}\\ \hline
\text{two-bit face, remaining bit }0&010\\
\text{two-bit face, remaining bit }1&001\\
\text{three-bit split }1+2,\ \text{both positive}&001,\ 100\\
\text{three-bit split }1+2,\ \text{mixed signs}&010,\ 011.
\end{array}                                        \tag{3}
\]
Swapping the two equal-offset cells only reverses the first and third entries and
does not change whether the word is monochromatic. The support reduction
exhausts all positive corners, and every word in (3) contains both colors.
This proves the theorem.

## 2. The two diagonal Golomb classes

Let
\[
B=\{s_X:|X|\ \text{is even}\},\qquad
C=\{s_X:|X|\ \text{is odd}\}.                     \tag{4}
\]
These are the two diagonal color classes of the proper coloring above.
Put
\[
a=w_1+w_2,\qquad b=w_1+w_3,\qquad
c=w_2+w_3,\qquad W=w_1+w_2+w_3.
\]
Then
\[
B=\{0,a,b,c\},\qquad C=\{w_1,w_2,w_3,W\}.          \tag{5}
\]
The 2-dissociation condition makes both classes Golomb. More precisely,
their common positive-difference set is
\[
\Delta B=\Delta C
=\{w_2-w_1,w_3-w_1,w_3-w_2,a,b,c\},               \tag{6}
\]
after relabeling the weights so that \(w_1<w_2<w_3\).
Their sets of sums of distinct pairs also agree:
\[
\Sigma_2(B)=\Sigma_2(C)
=\{a,b,c,W+w_1,W+w_2,W+w_3\}.                     \tag{7}
\]
All six entries in each display are distinct by (1). Hence every distinct
pair resource has both a \(D\)-edge and an \(S\)-edge.

## 3. The three alternating four-cycles

The resource graph decomposes into the following three cycles:
\[
\begin{aligned}
\{0,a\}_B
&\xleftrightarrow{\ S\ }\{w_1,w_2\}_C
\xleftrightarrow{\ D\ }\{b,c\}_B
\xleftrightarrow{\ S\ }\{w_3,W\}_C
\xleftrightarrow{\ D\ }\{0,a\}_B,\\
\{0,b\}_B
&\xleftrightarrow{\ S\ }\{w_1,w_3\}_C
\xleftrightarrow{\ D\ }\{a,c\}_B
\xleftrightarrow{\ S\ }\{w_2,W\}_C
\xleftrightarrow{\ D\ }\{0,b\}_B,\\
\{0,c\}_B
&\xleftrightarrow{\ S\ }\{w_2,w_3\}_C
\xleftrightarrow{\ D\ }\{a,b\}_B
\xleftrightarrow{\ S\ }\{w_1,W\}_C
\xleftrightarrow{\ D\ }\{0,c\}_B.
\end{aligned}                                      \tag{8}
\]
For example, the first \(S\)-edge uses the common sum \(a\), the next
\(D\)-edge uses the common difference \(w_2-w_1=c-b\), the second
\(S\)-edge uses the common sum \(b+c=W+w_3\), and the closing \(D\)-edge
uses the common difference \(W-w_3=a\). The other two lines follow by
permuting the omitted generator.

There are twelve distinct pair vertices in (8), exactly all six distinct
pairs from each class. Thus (8) is the complete distinct-pair resource
graph for the construction, not merely three cycles contained in a larger
resource graph. No repeated-pair terminal occurs in these cycles.

## 4. Concrete instance

Take
\[
(w_1,w_2,w_3)=(1,4,16).
\]
The dominance inequalities \(4>2\) and \(16>2(1+4)\) verify (1). The
source and its diagonal classes are
\[
\begin{aligned}
S&=\{0,1,4,5,16,17,20,21\},\\
B&=\{0,5,17,20\},\\
C&=\{1,4,16,21\}.
\end{aligned}                                      \tag{9}
\]
Their common difference set and common distinct-pair-sum set are
\[
\Delta B=\Delta C=\{3,5,12,15,17,20\},             \tag{10}
\]
\[
\Sigma_2(B)=\Sigma_2(C)=\{5,17,20,22,25,37\}.       \tag{11}
\]
The three cycles become
\[
\begin{aligned}
\{0,5\}_B&-_{S}\{1,4\}_C-_{D}\{17,20\}_B
           -_{S}\{16,21\}_C-_{D}\{0,5\}_B,\\
\{0,17\}_B&-_{S}\{1,16\}_C-_{D}\{5,20\}_B
           -_{S}\{4,21\}_C-_{D}\{0,17\}_B,\\
\{0,20\}_B&-_{S}\{4,16\}_C-_{D}\{5,17\}_B
           -_{S}\{1,21\}_C-_{D}\{0,20\}_B.
\end{aligned}                                      \tag{12}
\]
Together with the coloring rule in Section 1, this is an explicit proper
weak example containing alternating \(D\)--\(S\) cycles. Therefore actual
proper weak coloring does not make the two-matching resource graph
acyclic. Any use of that graph in an energy argument must accommodate its
alternating cycle components rather than charge only to path terminals.
