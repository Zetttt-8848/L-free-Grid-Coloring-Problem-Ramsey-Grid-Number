# Low-rainbow proper colorings of \(T_{11},T_{12},T_{13}\)

Checkpoint-0013 update: the T_13 construction here remains valid but
its rainbow count is superseded by the proper fourteen-rainbow
construction in ../THIRTEEN_TRIANGLE_FOURTEEN_RAINBOW.md. The older
array is retained because the fixed-class packing theorem uses it.

**Status:** literal constructions from bounded discovery.  The displayed
rainbow counts are upper bounds; no minimum or impossibility claim is
made.

For

\[
T_N=\{(v,u):0\le u<v<N\},
\]

the string in row \(v\) lists the colors of

\[
(v,0),(v,1),\ldots,(v,v-1)
\]

in that order.  A corner is recorded compactly as \((x,y;d)\), meaning

\[
\{(x,y),(x+d,y),(x+d,y+d)\}.
\tag{1}
\]

For each displayed array, the accompanying endpoint-group table is an
exhaustive no-monochromatic-corner certificate.  At offset \(d\), the
endpoint cells are \((u+d,u)\); the `starts` entry lists all starts of
one color when that color occurs at least twice.  The completion colors
are listed in the lexicographic order of pairs of starts.  Every
completion color in the tables differs from its endpoint color.
Groups of size at most one cannot supply a monochromatic corner, so the
tables prove properness directly.

## 1. A \(T_{11}\) coloring with five rainbow corners

| row \(v\) | colors |
|---:|:---|
| 1 | `0` |
| 2 | `10` |
| 3 | `001` |
| 4 | `2222` |
| 5 | `12000` |
| 6 | `000111` |
| 7 | `2020012` |
| 8 | `12001120` |
| 9 | `012202211` |
| 10 | `0102102101` |

The complete endpoint-group certificate is:

| offset \(d\) | endpoint color | starts | completion colors |
|---:|---:|:---|:---|
| 1 | 0 | 0,1,4,7 | 1,1,1,2,2,1 |
| 1 | 1 | 2,5,8,9 | 0,2,0,2,0,0 |
| 1 | 2 | 3,6 | 0 |
| 2 | 0 | 1,3,8 | 2,1,2 |
| 2 | 1 | 0,4,5,7 | 0,2,0,0,0,2 |
| 2 | 2 | 2,6 | 0 |
| 3 | 0 | 0,2,4 | 1,2,2 |
| 3 | 1 | 3,5,7 | 0,2,0 |
| 3 | 2 | 1,6 | 1 |
| 4 | 0 | 2,3 | 2 |
| 4 | 2 | 0,1,5,6 | 1,0,0,1,1,0 |
| 5 | 0 | 1,3,4,5 | 2,1,1,2,2,1 |
| 6 | 0 | 0,1,2 | 2,1,2 |
| 7 | 2 | 0,1,2,3 | 1,0,0,1,1,0 |
| 8 | 1 | 0,1 | 0 |

The sums of squared color counts on the row, column, and offset-diagonal
line families are, respectively,

\[
159,\qquad165,\qquad161.
\]

Each line family has lengths \(1,\ldots,10\), so

\[
V=159+165+161-\sum_{j=1}^{10}j^2
=485-385=100.
\tag{2}
\]

Here \(M=\binom{11}{2}=55\).  The proper three-color identity
\(V+2R=2M\) therefore gives

\[
R=\frac{110-100}{2}=5.
\tag{3}
\]

The five rainbow corners are

\[
\begin{gathered}
(4,1;2),\quad
(4,2;2),\quad
(5,3;4),\\
(7,1;2),\quad
(8,4;1).
\end{gathered}
\tag{4}
\]

Thus this proper coloring has

\[
R=5<10.
\tag{5}
\]

## 2. A \(T_{12}\) coloring with ten rainbow corners

| row \(v\) | colors |
|---:|:---|
| 1 | `0` |
| 2 | `10` |
| 3 | `011` |
| 4 | `2012` |
| 5 | `11120` |
| 6 | `010101` |
| 7 | `2211022` |
| 8 | `11002000` |
| 9 | `002100211` |
| 10 | `1102102100` |
| 11 | `12102121020` |

The complete endpoint-group certificate is:

| offset \(d\) | endpoint color | starts | completion colors |
|---:|---:|:---|:---|
| 1 | 0 | 0,1,4,7,9,10 | 1,1,1,1,1,1,1,1,2,2,1,2,1,1,2 |
| 1 | 1 | 2,5,8 | 0,2,0 |
| 1 | 2 | 3,6 | 1 |
| 2 | 0 | 4,6,8 | 2,1,2 |
| 2 | 1 | 0,1,2,7 | 0,2,0,0,0,2 |
| 2 | 2 | 3,5,9 | 1,0,1 |
| 3 | 0 | 0,1,4,5,8 | 2,2,1,1,2,1,2,2,2,1 |
| 3 | 1 | 2,3,7 | 0,0,2 |
| 4 | 0 | 2,5 | 2 |
| 4 | 1 | 1,3,7 | 2,2,0 |
| 4 | 2 | 0,4,6 | 1,1,1 |
| 5 | 0 | 3,4,5 | 1,2,1 |
| 5 | 1 | 0,1,2 | 0,2,2 |
| 6 | 0 | 0,2 | 1 |
| 6 | 1 | 3,4,5 | 2,0,2 |
| 7 | 2 | 0,2,3,4 | 0,1,1,0,1,0 |
| 8 | 0 | 1,2,3 | 1,2,1 |
| 9 | 1 | 1,2 | 2 |

The row, column, and offset-diagonal squared-count sums are

\[
200,\qquad210,\qquad208.
\]

Since \(\sum_{j=1}^{11}j^2=506\),

\[
V=200+210+208-506=112.
\tag{6}
\]

Here \(M=\binom{12}{2}=66\), so

\[
R=\frac{132-112}{2}=10.
\tag{7}
\]

The ten rainbow corners are

\[
\begin{gathered}
(5,3;1),\quad
(7,1;1),\quad
(7,1;2),\quad
(7,2;2),\quad
(7,3;1),\\
(7,5;2),\quad
(8,1;1),\quad
(8,2;1),\quad
(8,6;1),\quad
(10,5;1).
\end{gathered}
\tag{8}
\]

Thus this proper coloring has

\[
R=10<12.
\tag{9}
\]

## 3. A \(T_{13}\) coloring with twenty-one rainbow corners

| row \(v\) | colors |
|---:|:---|
| 1 | `0` |
| 2 | `11` |
| 3 | `101` |
| 4 | `2112` |
| 5 | `20120` |
| 6 | `020101` |
| 7 | `2211222` |
| 8 | `11022000` |
| 9 | `000202111` |
| 10 | `2220010122` |
| 11 | `11002121000` |
| 12 | `101021021020` |

The complete endpoint-group certificate is:

| offset \(d\) | endpoint color | starts | completion colors |
|---:|---:|:---|:---|
| 1 | 0 | 0,4,7,10,11 | 2,1,1,1,2,2,2,1,2,2 |
| 1 | 1 | 1,2,5,8 | 0,2,0,0,0,2 |
| 1 | 2 | 3,6,9 | 1,0,0 |
| 2 | 0 | 1,4,6,9 | 2,1,1,2,2,2 |
| 2 | 1 | 0,2,7 | 2,0,0 |
| 2 | 2 | 3,5,8,10 | 1,0,0,1,1,1 |
| 3 | 0 | 5,8,9 | 1,1,1 |
| 3 | 1 | 0,1,2,3,6,7 | 2,2,0,0,2,0,2,0,2,0,0,2,2,0,0 |
| 4 | 0 | 1,2,6 | 2,2,2 |
| 4 | 1 | 3,7,8 | 0,0,2 |
| 4 | 2 | 0,4,5 | 1,0,0 |
| 5 | 1 | 2,5 | 2 |
| 5 | 2 | 0,1,3,6,7 | 0,1,1,1,1,1,0,0,0,0 |
| 6 | 0 | 0,2,4,6 | 1,2,1,2,1,2 |
| 6 | 2 | 1,3 | 0 |
| 7 | 0 | 2,3 | 2 |
| 7 | 1 | 1,5 | 0 |
| 7 | 2 | 0,4 | 1 |
| 8 | 0 | 1,3 | 1 |
| 8 | 2 | 2,4 | 1 |
| 9 | 0 | 0,2,3 | 1,1,1 |
| 10 | 1 | 1,2 | 0 |

The row, column, and offset-diagonal squared-count sums are

\[
256,\qquad254,\qquad254.
\]

Since \(\sum_{j=1}^{12}j^2=650\),

\[
V=256+254+254-650=114.
\tag{10}
\]

Here \(M=\binom{13}{2}=78\), and hence

\[
R=\frac{156-114}{2}=21.
\tag{11}
\]

The twenty-one rainbow corners are

\[
\begin{gathered}
(5,1;2),\quad
(5,1;3),\quad
(5,3;1),\quad
(6,3;2),\\
(7,1;1),\quad
(7,2;1),\quad
(7,2;4),\quad
(7,4;2),\\
(7,4;3),\quad
(7,5;4),\quad
(8,1;2),\quad
(8,3;2),\\
(8,5;1),\quad
(8,7;2),\quad
(9,3;2),\quad
(9,5;1),\\
(9,6;2),\quad
(10,1;1),\quad
(10,4;1),\quad
(10,6;1),\\
(10,7;2).
\end{gathered}
\tag{12}
\]

Thus this proper coloring has

\[
R=21<22.
\tag{13}
\]

## 4. Consequence for the whole-triangle density test

At host size \(464\), the coarse whole-corner calculation using the
factor \(\binom m3\) requires every proper coloring to have at least
\(10\), \(15\), and \(22\) rainbow corners for local sizes \(11\),
\(12\), and \(13\), respectively.  Equations (5), (9), and (13) give a
counterexample below each coarse threshold.

Retaining the maximum allowed dilation lowers the sufficient thresholds
at local sizes \(12\) and \(13\) to \(13\) and \(18\); exact boundary
multiplicities may lower them further to \(12\) and \(17\).  The
\(T_{12}\) witness has \(R=10\), so it remains below both refined
\(T_{12}\) thresholds.  The displayed \(T_{13}\) witness has \(R=21\);
it refutes only the coarse threshold \(22\) and gives no conclusion
about the refined thresholds \(18\) or \(17\).

The constructions do not determine the minimum number of rainbow
corners at any size.  The bounded \(T_{13}\) search at \(R\le16\) was
undecided, and no conclusion is drawn from that solver output.
