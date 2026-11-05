# A weak-source counterexample and the exact product-span defect

Let
\[
W(S)=\{(v,u):u,v\in S,\ u\le v\}
\]
be colored with two colors.  The proposed inequality for its diagonal
color classes \(B,C\),
\[
\operatorname{span}(S)\ge (|B|-1)(|C|-1),               \tag{1}
\]
is false.  This note turns the saved twelve-mark discovery into a complete
finite construction and then records the corrected exact bookkeeping
identity.  The construction proof uses the displayed coloring rule and a
classification of all possible equal-color endpoint pairs; it does not use
the raw SAT status as a proof premise.

## 1. The twelve-mark coloring

Put
\[
P=\{0,4,7,12,21,23\},\qquad S=P+\{0,1\}.
\]
Every mark of \(S\) has a unique form \(p+\alpha\), with \(p\in P\) and
\(\alpha\in\{0,1\}\).  Color the diagonal cell
\((p+\alpha,p+\alpha)\) by \(\alpha\).  Thus
\[
B=P,\qquad C=P+1.
\]

The cells inside a two-point block are colored by
\[
z(p+1,p)=
\begin{cases}
1,&p\in\{0,4,23\},\\
0,&p\in\{7,12,21\}.
\end{cases}                                             \tag{2}
\]

It remains to specify the four cells between every ordered pair \(p<q\)
in \(P\).  For
\[
(v,u)=(q+\beta,p+\alpha),\qquad \alpha,\beta\in\{0,1\},
\]
use the following four rules:
\[
\begin{array}{c|c|c}
\text{type}&\{(p,q)\}&z(q+\beta,p+\alpha)\\ \hline
A&\{(0,4)\}&1-\beta\\
B&\{(0,7),(0,23),(4,12),(4,23)\}&(1-\alpha)(1-\beta)\\
C&\{(0,12),(0,21),(4,7),(4,21)\}&1-\alpha\beta\\
D&\{(7,12),(7,21),(7,23),(12,21),(12,23),(21,23)\}
 &1-\alpha .
\end{array}                                             \tag{3}
\]
Equations (2)--(3), together with the diagonal colors, specify all
\(\binom{12+1}{2}=78\) cells of \(W(S)\).

## 2. Direct corner classification

Every positive corner has two distinct endpoint cells on one
slope-one diagonal.  Write those cells as
\[
(u+d,u),\qquad (v+d,v),\qquad u<v.
\]
Their completion is \((v+d,u)\).  Therefore it is enough to show that
whenever the two endpoints have equal color, their completion has the
opposite color.

At \(d=0\), the equal-color start sets are \(P\) in color \(0\) and
\(P+1\) in color \(1\).  Rule (3) assigns color \(1\) to every completion
between two distinct marks of \(P\), and color \(0\) to every completion
between the corresponding two marks of \(P+1\).

For \(d>0\), the complete list of equal-color endpoint groups of size at
least two is below.  A start set \(X\) means the endpoints
\(\{(x+d,x):x\in X\}\).  The last column lists all pair completions and
their common color.

\[
\begin{array}{c|c|l|l}
d&\text{endpoint color}&X&\text{completions, all of opposite color}\\ \hline
1&0&\{7,12,21,22\}
 &(13,7),(22,7),(23,7),(22,12),(23,12),(23,21):1\\
1&1&\{0,4,23\}&(5,0),(24,0),(24,4):0\\
2&1&\{5,21\}&(23,5):0\\
3&1&\{1,4,21\}&(7,1),(24,1),(24,4):0\\
4&0&\{1,8\}&(12,1):1\\
4&1&\{0,4\}&(8,0):0\\
5&0&\{0,8\}&(13,0):1\\
7&0&\{1,5\}&(12,1):1\\
8&0&\{0,5,13\}&(13,0),(21,0),(21,5):1\\
9&0&\{4,13\}&(22,4):1\\
11&1&\{1,12\}&(23,1):0\\
12&1&\{0,12\}&(24,0):0\\
16&1&\{5,7\}&(23,5):0\\
17&1&\{4,7\}&(24,4):0 .
\end{array}                                             \tag{4}
\]

At every positive offset omitted from (4), each color occurs at most
once among the endpoint cells, so it cannot support a monochromatic
corner.  The values in (4) follow directly from the four block formulas
(2)--(3).  Thus every equal-color endpoint pair has an opposite-color
completion, proving that this is a proper coloring of \(W(S)\).

Both diagonal classes have six marks and
\[
\operatorname{span}(S)=24<25=(6-1)^2.                  \tag{5}
\]
This is a direct counterexample to (1).  The weaker numerical expression
\(|B||C|-|B|-|C|=24\) happens to be attained by this example, but no
universal assertion about that expression follows.

## 3. Exact bookkeeping behind the one-unit failure

For a finite integer set \(X\), write
\[
\Delta X=\{y-x:x,y\in X,\ x<y\}.
\]
In any proper two-color weak triangle, each diagonal color class is
Golomb: two same-color diagonal pairs with a repeated positive difference
would force their two off-diagonal cells to the opposite color, and those
cells with their completion would be monochromatic.  Hence
\[
|\Delta B|=\binom b2,\qquad |\Delta C|=\binom c2,
\quad b=|B|,\ c=|C|.                                   \tag{6}
\]

Let
\[
R=|\Delta B\cap\Delta C|,\qquad
U=L-|\Delta B\cup\Delta C|,\qquad L=\operatorname{span}(S).
\]
Here \(R\) counts lengths used in both diagonal colors and \(U\) counts
positive lengths at most \(L\) used in neither.  Inclusion-exclusion gives
the exact identity
\[
\boxed{
L-(b-1)(c-1)
=U+\frac{(b-c)^2+b+c-2}{2}-R .
}                                                       \tag{7}
\]
Thus (1) would be equivalent to
\[
R-U\le\frac{(b-c)^2+b+c-2}{2}.                          \tag{8}
\]

For the construction above,
\[
\Delta P=
\{2,3,4,5,7,8,9,11,12,14,16,17,19,21,23\}.             \tag{9}
\]
Since \(C=B+1\), the two difference sets coincide.  Therefore
\[
R=15,\qquad U=24-15=9,
\qquad \frac{(b-c)^2+b+c-2}{2}=5,
\]
and (7) reads
\[
24-25=9+5-15=-1.                                       \tag{10}
\]
The failure is exactly one excess shared length after unused lengths and
the five-unit balanced allowance are deducted.

## 4. A corrected special-case span lemma

Although (1) is false, there is a clean regime in which it holds.  Let
\[
I_B=[\min B,\max B],\qquad I_C=[\min C,\max C],
\]
and let \(\omega\) be the ordinary length of \(I_B\cap I_C\), with
\(\omega=0\) when the hulls are disjoint.  Golombness and overlap of the
two hulls give
\[
\begin{aligned}
L
&\ge \operatorname{span}(B)+\operatorname{span}(C)-\omega\\
&\ge \binom b2+\binom c2-\omega\\
&=(b-1)(c-1)
  +\frac{(b-c)^2+b+c-2}{2}-\omega.                     \tag{11}
\end{aligned}
\]
Consequently (1) remains valid under the explicit hypothesis
\[
\omega\le\frac{(b-c)^2+b+c-2}{2}.                       \tag{12}
\]
For \(b=c=m\), this means hull overlap at most \(m-1\).  In particular it
covers separated classes and shallowly interlaced classes.  The present
counterexample has hull overlap \(22\), far beyond the allowance \(5\).

There is also an unbalanced regime needing no hull hypothesis:
if \(b\ge c\) and \(b\ge2c-2\), then
\[
L\ge\binom b2\ge(b-1)(c-1),                             \tag{13}
\]
with the color-reversed statement when \(c\ge2b-2\).

## 5. The remaining compatibility gap

For a common length \(h\), Golombness gives unique monochromatic starts
\(p_B(h)\) and \(p_C(h)\).  The six-mark theorem in
MIXED_INTERVALS.md says that if \(p_B<p_C\), no mixed \(h\)-edge can
go from \(C\) back to \(B\) with its start strictly between them; the
color-reversed statement holds if \(p_C<p_B\).  This is genuine ordered
information, but it does not itself charge a common length to a missing
length.

Identity (7) isolates the quantitative statement that would be needed:
all but
\[
\frac{(b-c)^2+b+c-2}{2}
\]
common lengths must be paid for by distinct unused lengths.  The explicit
proper coloring above shows that such a payment can fail by one already
at \(b=c=6\).  Any surviving finite-cap inequality therefore needs either
a larger correction or another completion statistic beyond the sets
\(\Delta B,\Delta C\), their unused lengths, and the six-mark orientation
alone.
