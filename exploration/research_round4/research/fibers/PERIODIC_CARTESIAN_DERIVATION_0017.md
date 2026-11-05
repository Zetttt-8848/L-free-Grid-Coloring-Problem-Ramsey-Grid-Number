# An explicit periodic Cartesian construction

## 1. The column set and coloring

For an integer (m\ge1), define

\[
C_m=\{c_i=2^i-1:0\le i<m\}.
\tag{1}
\]

On the infinite strip (mathbb Z\times C_m), color column (c_i) by

\[
\chi(x,c_i)=\left\lfloor\frac{x}{2^i}\right\rfloor\pmod 2.
\tag{2}
\]

Column (c_i) has period (2^{i+1}), so the whole coloring is periodic in (x) with period (2^m).

## 2. Direct proof of properness

Consider any available corner

\[
(x,c_i),\qquad (x+h,c_i),\qquad (x+h,c_j),
\tag{3}
\]

where (j>i) and (h=c_j-c_i>0).  From (1),

\[
h=2^j-2^i=2^i(2^{j-i}-1).
\tag{4}
\]

The quotient (h/2^i=2^{j-i}-1) is odd.  Since it is an integer,

\[
\left\lfloor\frac{x+h}{2^i}\right\rfloor
=
\left\lfloor\frac{x}{2^i}\right\rfloor+rac{h}{2^i}.
\tag{5}
\]

Equations (2), (4), and (5) give

\[
\chi(x+h,c_i)=1-\chi(x,c_i).
\tag{6}
\]

Thus the first two cells in (3) always have opposite colors.  The third cell may have either color, and the corner is still nonmonochromatic.  This proves properness on the full infinite strip.  Restricting (x) to any finite row set preserves properness.

The mechanism can be stated more generally.  If a sorted column set (C=\{c_0<\cdots<c_{m-1}\}) has the property that, for each (i), all later differences (c_j-c_i) have the same 2-adic valuation (v_i), then

\[
\chi(x,c_i)=\left\lfloor x/2^{v_i}\right\rfloor\pmod2
\]

is proper.  The set (1) realizes this with (v_i=i).

## 3. Exact finite corner count

Let

\[
B_n=\{0,1,\ldots,n-1\}.
\]

The positive differences in (C_m) are all distinct.  Indeed,

\[
2^j-2^i=2^i(2^{j-i}-1)
\]

has 2-adic valuation (i), which determines (i), and its remaining odd factor then determines (j-i).  Hence (r_{C_m}(h)=1) for every represented positive difference (h).

Assume (n>2^{m-1}-1), so every column difference is also represented in (B_n).  Then

\[
\begin{aligned}
U(B_n,C_m)
&=\sum_{0\le i<j<m}\bigl(n-(2^j-2^i)\bigr)\\
&={m\choose2}n-D_m,
\end{aligned}
\tag{7}
\]

where

\[
\begin{aligned}
D_m
&=\sum_{0\le i<j<m}(2^j-2^i)\\
&=\sum_{k=0}^{m-1}(2k-m+1)2^k\\
&=(m-3)2^m+m+3.
\end{aligned}
\tag{8}
\]

Since (|B_n||C_m|=mn), (7) yields

\[
\frac{U(B_n,C_m)}{|B_n||C_m|}
=
\frac{m-1}{2}-\frac{(m-3)2^m+m+3}{mn}.
\tag{9}
\]

For fixed (m), the ratio tends to

\[
\frac{m-1}{2}
\tag{10}
\]

as (n\to\infty).

## 4. Explicit consequences

With six columns,

\[
C_6=\{0,1,3,7,15,31\},\qquad D_6=201,
\]

and therefore

\[
U(B_n,C_6)=15n-201.
\tag{11}
\]

Two concrete restrictions of the periodic coloring are:

* (n=34): (U=309), (|B_n||C_6|=204), and
  \[
  \frac{U}{|B_n||C_6|}=\frac{103}{68}>\frac32.
  \]
* (n=68): (U=819), (|B_n||C_6|=408), and
  \[
  \frac{U}{|B_n||C_6|}=\frac{273}{136}>2.
  \]

More strongly, (10) is unbounded as (m\to\infty).  Given any fixed constant (c), choose (m>2c+1) and then take (n) sufficiently large.  The finite product (B_n\times C_m), with the restriction of (2), is properly two-colored and satisfies

\[
U(B_n,C_m)>c|B_n||C_m|.
\]

Consequently there is no universal constant (c) in an estimate (U(B,C)\le c|B||C|) for arbitrary finite Cartesian sets with a proper coloring.

## 5. Relation to the finite discovery pattern

The recorded (12\times6) assignment on (C=\{0,2,3,5,7,9\}) supplied evidence that the coefficient (3/2) was too small, but its row pattern is not needed here and no assertion about extending that particular assignment is made.  Construction (1)-(2) gives a separate analytic periodic strip, proves its properness directly, and yields ratios above both (3/2) and (2).

The construction also identifies the obstruction to any Cartesian argument based only on the number of cells: a column (c_i) can independently alternate on its own dyadic scale, and every forward column difference flips that column before the third corner cell is consulted.  Increasing the number of dyadic scales raises the corner density by approximately one half per added column.

## 6. Where the routed load diverges

The fixed-offset routing has a particularly transparent form here.  Consider the corner from column (c_i) to column (c_j), (i<j), and write its upper row coordinate as (y=x+h).  The lower-column cells at rows (x) and (y) have opposite colors by (6).  Therefore exactly one of the following occurs:

* the two diagonal endpoints have the same color, contributing to (S); or
* the upper diagonal endpoint ((y,c_j)) has the color of the completion ((y,c_i)), so the bichromatic diagonal pair is routed to ((y,c_j)).

No routed pair points to its lower diagonal endpoint.  Away from the two row boundaries, the load at ((y,c_j)) is consequently

\[
\lambda(y,c_j)
=
|\{i<j:\operatorname{bit}_i(y)=\operatorname{bit}_j(y)\}|.
\tag{12}
\]

Over a common binary period, each comparison in (12) is an equality for half the rows.  Hence, for fixed (m) and (n\to\infty),

\[
S=\frac{n}{2}{m\choose2}+O_m(1),
\qquad
P+E=\frac{n}{2}{m\choose2}+O_m(1).
\tag{13}
\]

The load is zero in column (c_0).  For (j\ge1), it is zero exactly when every lower bit is the complement of bit (j), an event occupying the fraction (2^{-j}) of a binary period.  Thus

\[
\begin{aligned}
P&=n\bigl(m-2+2^{-(m-1)}\bigr)+O_m(1),\\
Z&=n\bigl(2-2^{-(m-1)}\bigr)+O_m(1),\\
E&=n\left(\frac{m(m-1)}4-m+2-2^{-(m-1)}\right)+O_m(1).
\end{aligned}
\tag{14}
\]

Thus both (S) and the repeated-load term (E) have order (nm^2), while the unused-cell credit (Z) has order (n).  In the capacity form from `CARTESIAN_THREE_HALVES_0017.md`,

\[
S+E\le \frac{nm}{2}+Z,
\]

the failure comes mainly from the accumulation of about (j/2) distinct lower-column offsets at a typical cell in column (j).  The collision-forest lemma correctly converts this excess into monochromatic-pair incidences, but their congestion is unbounded with (m).

## 7. The source constraint absent from the strip

The Cartesian strip lets the row marks and column marks play permanently different roles.  A strict source does not: every mark belongs to one set (A), and every ordered pair of its marks supplies a cell.  If one places a translate of the dense interval (B_n) above (C_m), the strip is only the rectangular cross block.  A source extension must additionally color the whole triangular blocks (V(B_n)) and (V(C_m)), with the same cell colors participating in all cross-block corners.

The dyadic rule works because, from a fixed (c_i), every later selected column difference has exactly the same 2-adic valuation (i).  Inside the dense interval (B_n), a fixed lower mark has forward differences of several valuations (already (1) and (2)).  No single column bit can flip on all of them.  More invariantly, the source restriction to (V(B_n)) is a proper weak-triangle coloring problem on the row set itself; this self-interaction is entirely absent from (mathbb Z\times C_m).

Therefore the periodic example rejects every standalone Cartesian constant, but it does not transfer to a source construction.  Any source-level use of Cartesian cuts must retain a term measuring the triangular self-cost of the row and column mark sets, or a compatibility potential shared between the cut and (V(B)\cup V(C)).  Dropping that compatibility is exactly what permits the divergent load (12).
