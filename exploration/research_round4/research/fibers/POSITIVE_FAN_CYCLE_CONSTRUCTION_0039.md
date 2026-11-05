# A proper source realizing the supported positive-fan four-cycle

Let
\[
D=\{1,10,100,111\},\qquad
P=\{1000,1001,1011,1111\},
\]
\[
S=\{0\}\cup D\cup P,\qquad x=10000,
\qquad A=S\cup(x+S).                                   \tag{1}
\]
This note gives a direct coloring of the strict source triangle \(V(A)\).
The saved raw model was used only to find the signs.  Properness follows
from the explicit tables and the offset classification below.

## 1. Compact specification of all cells

Order the nine elements of \(S\) as
\[
(s_0,\ldots,s_8)
=(0,1,10,100,111,1000,1001,1011,1111).                \tag{2}
\]
There are three kinds of strict cells.

For a lower-layer cell \((s_i,s_j)\), \(i>j\), its signs in increasing
column order are:
\[
\begin{array}{c|l}
s_i&z(s_i,s_0)\cdots z(s_i,s_{i-1})\\ \hline
1&-\\
10&--\\
100&+--\\
111&+---\\
1000&+-++-\\
1001&+-++-+\\
1011&++---++\\
1111&-++--+++
\end{array}                                             \tag{3}
\]

For an upper-layer cell \((x+s_i,x+s_j)\), \(i>j\), use:
\[
\begin{array}{c|l}
s_i&z(x+s_i,x+s_0)\cdots z(x+s_i,x+s_{i-1})\\ \hline
1&-\\
10&--\\
100&---\\
111&----\\
1000&---+-\\
1001&+----+\\
1011&-----++\\
1111&++-++-+-
\end{array}                                             \tag{4}
\]

Every cross-layer cell exists because \(x>\operatorname{span}(S)\).
For fixed row \(x+s_i\), list its nine signs in the column order (2):
\[
\begin{array}{c|c}
s_i&(z(x+s_i,s_0),\ldots,z(x+s_i,s_8))\\ \hline
0&+-+--+++-\\
1&+-----+--\\
10&++-------\\
100&+++--+---\\
111&++++-----\\
1000&-+--++---\\
1001&-+--+-+--\\
1011&--+++--+-\\
1111&---++---+
\end{array}                                             \tag{5}
\]
The two triangular lists (3)--(4) contain \(36\) signs each and (5)
contains \(81\), so these tables specify all
\(\binom{18}{2}=153\) strict cells.

## 2. Offset proof of properness

For an offset \(d>0\), a start \(u\) denotes the cell
\[
(u+d,u).
\]
If two starts \(u<v\) at the same offset have equal sign \(c\), their
unique corner completion is
\[
(v+d,u).                                               \tag{6}
\]
It is therefore enough to show that every such completion has sign
\(-c\).

The following is the complete list of signed offset groups containing at
least two starts.  In the last column, the displayed sign is the sign of
every completion (6) obtained from a pair of starts in that row.
\[
\begin{array}{r|c|l|c}
d&c&\text{starts}&\text{all completions}\\ \hline
1&+&1000,11000&-\\
1&-&0,10000&+\\
9&-&1,10001&+\\
10&+&1001,11001&-\\
10&-&0,10000&+\\
11&+&1000,11000&-\\
11&-&100,10100&+\\
90&-&10,10010&+\\
99&-&1,10001&+\\
100&+&0,1011&-\\
100&-&10000,11011&+\\
101&-&10,10010&+\\
110&+&1001,11001&-\\
110&-&1,10001&+\\
111&+&0,1000&-\\
111&-&10000,11000&+\\
889&-&111,10111&+\\
890&-&111,10111&+\\
900&+&100,10100&-\\
900&-&111,10111&+\\
911&-&100,10100&+\\
999&-&1,10001&+\\
1000&+&0,10111&-\\
1000&-&1,111,10000,10001&+\\
1001&+&0,10000&-\\
1001&-&10,10010&+\\
1011&+&0,10100&-\\
1011&-&100,10000&+\\
1110&+&1,10001&-\\
9000&+&1000,1001&-\\
9889&-&111,1111&+\\
9890&-&111,1111&+\\
9900&-&100,1111&+\\
9989&-&111,1011&+\\
9999&-&1,1001&+\\
10000&+&0,1000,1001,1011,1111&-\\
10000&-&1,10,100,111&+\\
11000&+&1,111&-
\end{array}                                             \tag{7}
\]

The start sets in (7) are obtained directly by subtracting pairs of
marks in (1) and reading the corresponding signs from (3)--(5).
Substitution of every unordered start pair into (6) gives the last
column from the same three tables.  At every offset omitted from (7),
each sign occurs at most once, so that offset cannot supply equal-color
corner endpoints.

Thus every equal-color endpoint pair has an opposite-color completion.
Every positive corner in \(V(A)\) is represented by exactly one such
pair, proving that (3)--(5) give a proper two-coloring.

## 3. The positive fan at \(x=10000\)

The anchored cell at \(x\) has sign
\[
f(x)=z(10000,0)=+.
\]
At offset \(x\), the cells based at the four starts in \(P\) have signs
\[
z(x+p,p)=+\qquad(p\in P),                              \tag{8}
\]
while the cells based at \(D\) have sign \(-\).  Also
\[
f(x+p)=z(x+p,0)=-\qquad(p\in P).                       \tag{9}
\]
Consequently the actual positive-fan set in the notation of
POSITIVE_FAN_DIFFERENCE_BUDGET_0039.md is exactly
\[
P_x=P.                                                 \tag{10}
\]

Its six pair differences are
\[
\Delta P=\{1,10,11,100,110,111\}.                      \tag{11}
\]
The supported differences are those \(h\) for which both \(h\) and
\(x+h\) are source marks.  Equations (1) and (11) give
\[
D_x=\{1,10,100,111\}=D.                                \tag{12}
\]

Write the vertices of \(P\) in increasing order as
\[
p_0=1000,\quad p_1=1001,\quad p_2=1011,\quad p_3=1111.
\]
The supported-difference graph has precisely the edges
\[
p_0p_1\ (1),\qquad
p_1p_2\ (10),\qquad
p_2p_3\ (100),\qquad
p_0p_3\ (111).                                        \tag{13}
\]
The two missing chords have gaps \(11\) and \(110\), neither of which is
supported in (12).  Hence
\[
\Gamma_x=C_4.                                         \tag{14}
\]
The opposite vertices \(p_0,p_2\) have the two common neighbors
\(p_1,p_3\): \(p_1\) lies between them and \(p_3\) lies outside their
closed interval.  Thus the common-neighbor upper bound \(2\) from the
positive-fan lemma is attained by an actual properly colored source.

## 4. Scope

This is one literal two-layer construction.  The tables prove its
properness without using the raw SAT verdict as a premise.  No compact
parameterized rule for replacing the decimal scales
\(1,10,100,1000,10000\) is derived here; the signs in (3)--(5) do not
reduce to a single difference color or a single layer parity.

The construction establishes that a universal strengthening of the
supported-difference graph from triangle-free to forest, or from
common-neighbor at most two to common-neighbor at most one, is false.
It does not classify all possible cycles and does not imply a global
endpoint or source-energy bound.
