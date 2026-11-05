# Reflected-middle seeds versus the mixed-energy defect

Let \(S=B\sqcup C\) be the diagonal partition of a proper two-color weak
triangle. Thus \(B,C\) are Golomb. Write
\[
U=\binom{|B|}{2}+\binom{|C|}{2},
\qquad
\delta=(U-2\rho)+(2|B||C|-N)+(U-Q).
\tag{1}
\]
The three summands have exact resource meanings:

* \(U-2\rho\) is the number of same-class pair resources whose difference
  is not represented in the other class.
* \(2|B||C|-N\) is the sum, over mixed pairs of length \(j\), of
  \(2-\beta_j-\gamma_j\). It counts the missing same-class difference
  supports for each mixed query.
* \(U-Q\) is the number of distinct same-class pair resources not used in
  an equal-sum match with the other class. A distinct-distinct match uses
  two resources and contributes two to \(Q\); a repeated-distinct match
  uses the one distinct resource and contributes one.

This note identifies the resources immediately exposed by a
reflected-middle seed. It also gives a proper weak example showing that the
most natural \(U-Q\) charge is not automatic. No inequality
\(K_{\rm seed}\le c\delta\) with absolute \(c\) is proved.

## 1. The local saturation dichotomy

Normalize an upper seed to
\[
C\supseteq\{0,h\},\qquad
B\supseteq\{p,h+p,2h\},
\qquad 0<p<h,
\tag{2}
\]
and put
\[
t=h-p.
\tag{3}
\]
Proper weak coloring forces the reflected middle \(t\) to be absent from
all of \(S\). In particular \(p\ne t\), since \(p\in B\).

The seed supplies three distinct \(B\)-pair resources:
\[
\begin{array}{c|c}
\text{pair}&\text{difference}\\ \hline
\{p,h+p\}&h\\
\{h+p,2h\}&t\\
\{p,2h\}&h+t .
\end{array}
\tag{4}
\]
The first difference is shared with the \(C\)-pair \(\{0,h\}\).

It also supplies two mixed pairs of length \(p\):
\[
\{0,p\},\qquad \{h,h+p\}.                         \tag{5}
\]
Hence their combined contribution to the middle defect is
\[
2(2-\beta_p-\gamma_p).                            \tag{6}
\]
There is a further mixed pair \(\{p,h\}\) of length \(t\), while the
\(B\)-pair of length \(t\) is already present.

Finally, the opposite-class pair \(\{0,h\}\) has sum \(h\). Its natural
\(B\)-match would be
\[
\{p,h-p\}=\{p,t\},                                \tag{7}
\]
and the second endpoint is exactly the forced hole. Pair-sum uniqueness
does not, however, prohibit a different \(B\)-pair of sum \(h\).

These observations prove the following exact dichotomy.

**Saturation lemma.** Every upper seed has at least one of the following
features:

1. the \(C\)-pair \(\{0,h\}\) is unused by \(Q\), giving one unit of
   \(U-Q\);
2. \(t\notin\Delta C\) or \(h+t\notin\Delta C\), so one of the last two
   resources in (4) gives a unit of \(U-2\rho\);
3. \(p\notin\Delta B\cap\Delta C\), in which case the two mixed queries
   in (5) give at least two units of \(2|B||C|-N\);
4. all of the following saturation conditions hold:
   \[
   p,t,h,h+t\in\Delta B\cap\Delta C
   \quad\text{and}\quad
   h\in B+B
   \text{ through a \(B\)-pair distinct from \(\{p,t\}\)}.
   \tag{8}
   \]

Here the last condition means precisely that the \(C\)-pair \(\{0,h\}\)
is used by the \(Q\)-charging match. The proof is just exhaustion of the
negations of items 1--3, using (4)--(7). Translation gives the general
upper seed. Direction-preserving reversal gives the same statement for a
lower seed, and exchanging \(B,C\) gives the opposite class role.

Thus a seed which is invisible to all three immediate charges is not a bare
five-mark configuration. It requires the four distinct shared positive
differences in (8), including the additive pattern
\[
p+t=h,\qquad h+t=2h-p,                            \tag{9}
\]
and an additional opposite-class pair-sum match.

## 2. The one charge that is injective

Restrict to seeds for which the opposite-class \(h\)-pair is unused by
\(Q\). Charge the seed to that unused pair resource. This map is injective.

Indeed, a Golomb class has only one pair of difference \(h\). Once the two
opposite-class endpoints and the unique other-class \(h\)-pair are fixed,
their relative displacement determines \(p\) and whether the possible seed
is upper or lower. The upper and lower seeds cannot coexist: they would
produce two distinct \(h\)-pairs in the other Golomb class, as in
BINARY_CORE_FIBER_TRANSFER_0044.md. Therefore
\[
K_{\rm unused\ opposite\ pair}\le U-Q.            \tag{10}
\]

The analogous maps to the other two defect terms do not yet have constant
multiplicity. A fixed unshared side pair of length \(t\) can be the
\(t\)-side of seeds with several larger shared lengths \(h\). Likewise the
two queries in (5) belong to a same-orientation mixed fiber: if that fiber
has \(k\) starts, one query participates in \(k-1\) start pairs, while the
middle defect charges the query only once per missing support class.
Golombness makes the resulting shared lengths distinct but does not bound
\(k\) absolutely.

## 3. A proper weak example defeating the canonical \(Q\)-charge

Take
\[
B=\{-100,2,9,14,107\},\qquad C=\{0,7\}.           \tag{11}
\]
The positive \(B\)-differences are
\[
102,109,114,207,7,12,105,5,98,93,
\tag{12}
\]
all distinct, and \(C\) has the single difference \(7\). Thus both classes
are Golomb.

The marks
\[
C:\ 0,7,\qquad B:\ 2,9,14                        \tag{13}
\]
form the upper seed with \(h=7,p=2\); its forced reflected middle is
\(5\notin S\). Nevertheless the opposite pair \(\{0,7\}\) is not unused:
\[
0+7=(-100)+107.                                  \tag{14}
\]
The distinct-distinct match (14) uses that \(C\)-pair resource in \(Q\).

Here is a direct proper coloring of \(W(S)\). Color the \(B\)-diagonal
zero and the \(C\)-diagonal one. Color every strict \(B\)-\(B\) cell one
and the strict \(C\)-\(C\) cell zero. The only positive differences with
more than one representation are
\[
\begin{array}{c|c}
2&(2,0),(9,7)\\
5&(7,2),(14,9)\\
7&(7,0),(9,2),(14,7)\\
100&(0,-100),(107,7)\\
107&(7,-100),(107,0).
\end{array}
\tag{15}
\]
At differences \(2,100,107\), give the two displayed cells opposite
colors. At difference \(5\), the cell \((14,9)\) is the fixed
\(B\)-\(B\) color one, so color \((7,2)\) zero. At difference \(7\), the
three displayed colors are
\[
0,\ 1,\ 0.                                        \tag{16}
\]
The unique equal-color endpoint pair in (16) has completion \((14,0)\);
color that cell one. Every other positive-difference fiber is a singleton,
and its mixed cells may be colored arbitrarily.

All positive corners are now proper: a two-cell fiber has opposite endpoint
colors, while the sole equal pair in the three-cell fiber has its completion
opposite by construction. Offset-zero corners are proper because every
same-class strict cell was assigned the color opposite its diagonal class.
This proves properness of the full weak coloring without a search.

For reference, this example has
\[
U=11,\qquad \rho=1,\qquad N=3,\qquad Q=2,
\qquad \delta=9+17+9=35.                          \tag{17}
\]
Thus it does not refute an absolute inequality \(K_{\rm seed}\le c\delta\).
It refutes the proposed canonical rule “charge every seed to its
opposite-class pair in \(U-Q\).”

## 4. Precise remaining geometric gap

Equation (10) disposes of every seed whose opposite pair-sum resource is
unused. The saturation lemma reduces the rest to two issues:

* control seeds satisfying the full package (8); and
* control reuse of an unshared side-pair resource or a deficient mixed query
  by seeds that fail only one part of (8).

A constant \(K_{\rm seed}\le c\delta\) would follow from a constant-reuse
map for those two classes. The present identities do not provide it. In
particular, pair-sum uniqueness replaces the missing natural match (7) by
at most one alternative match, but it does not constrain where the two
endpoints of that alternative pair lie. Difference Golombness similarly
makes the larger seed lengths distinct while allowing a fixed side resource
or mixed query to participate at many lengths.

Therefore the exact unresolved implication is a compatibility theorem for
the saturated packages (8), using their actual weak-cell colors or an
ordered bound on the resulting chains of shared differences. The three
nonnegative defect totals alone do not identify such a bounded-multiplicity
charge in this derivation.
