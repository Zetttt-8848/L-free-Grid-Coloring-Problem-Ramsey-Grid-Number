# Adjacent-difference runs and pair-sum valleys

Let (P\subset\mathbb Z) be Golomb, let (n=|P|\ge2), and suppose
(1\notin\Delta P). Put

\[
 D=\Delta P,\qquad M=|D|=\binom n2,
\]

and let

\[
 \Sigma=\{a+b:a,b\in P,\ a\le b\}.
\]

Golombness makes every sum in (Sigma) uniquely represented by an unordered
pair, including doubled pairs. Hence

\[
 N:=|\Sigma|=\binom{n+1}{2}=M+n.
\]

Assume in addition that (W(P\sqcup(P+1))) is properly colored with diagonal
classes (P) and (P+1). The orientation law and pair-sum valley theorem from
the adjacent-translate argument are retained below.

Write (r_D) and (r_\Sigma) for the numbers of maximal consecutive-integer
runs in (D) and (Sigma), respectively. Thus the numbers of internal run
edges are

\[
 A=M-r_D,
 \qquad
 E=N-r_\Sigma.                                      \tag{1}
\]

Here (A) is exactly the number of pairs (d,d+1\in D).

## 1. The exact two-to-one correspondence

Take adjacent represented sums (t,t+1\in\Sigma). Their representing pairs
cannot share a mark: otherwise the two other marks would differ by one.
Their interval lengths have opposite parity, so they are unequal. The
endpoint formulas

\[
 \left(\frac{t-\ell}{2},\frac{t+\ell}{2}\right)
\]

then show that the shorter representing interval lies strictly inside the
longer one. Write the outer interval as ([u,v]) and the inner interval as
([x,y]), where

\[
 u<x\le y<v.                                         \tag{2}
\]

If the outer sum is one greater than the inner sum, the two cross pairings
give

\[
 (v-y)-(x-u)=1,
 \qquad
 (v-x)-(y-u)=1.                                     \tag{3}
\]

If the outer sum is one smaller, the same identities hold with the two sides
reversed. Thus an adjacent pair of represented sums produces two pairs of
consecutive represented differences. They are distinct when (x<y), and
coincide when (x=y).

Conversely, let ([p,q]) and ([r,s]) be the unique ruler intervals of
lengths (d) and (d+1). Then

\[
 (p+s)-(q+r)=1,                                     \tag{4}
\]

so the complementary endpoint pairs represent adjacent sums. Equations
(3)--(4) are inverse constructions. Therefore every edge of the pair-sum
run graph has exactly two preimages among adjacent differences, except when
its inner pair is doubled, in which case it has one.

Define the **double-valley defect**

\[
 Z=|\{t:\ t,t+1\in\Sigma
       \text{ and the inner representing pair is }\{p,p\}\}|. \tag{5}
\]

The correspondence gives the exact ledger

\[
 \boxed{\ M-r_D=2(N-r_\Sigma)-Z.\ }                 \tag{6}
\]

Equivalently,

\[
 \boxed{\ 2r_\Sigma-r_D=M+2n-Z.\ }                 \tag{7}
\]

## 2. What proper coloring contributes

For an interval ([a,b]) representing a sum, denote its cross-copy cell by

\[
 \chi[a,b]=(b+1,a).
\]

The adjacent-difference orientation law says that an edge of the pair-sum
run charges the cell belonging to its outer representing interval. If the
interval length increases as the sum increases, that cell is forced to the
(P+1) diagonal color; if the length decreases, it is forced to the (P)
diagonal color.

Were one representation outer relative to both of its neighbors, the same
cell would be forced to both colors. Hence a proper coloring excludes a
strict local maximum. Since adjacent lengths are unequal, every pair-sum run
has a unique valley: its lengths strictly decrease and then strictly
increase.

It follows that distinct edges of the pair-sum run graph charge distinct
physical cells. On the decreasing arm, each representation except the valley
is charged once in the (P) color; on the increasing arm, each representation
except the valley is charged once in the (P+1) color. Equations (3) and (6)
now refine the previous multiplicity-two statement exactly:

* a charged cell normally receives two adjacent-difference charges;
* it receives one precisely when the inner interval across that run edge is
  the doubled valley pair.

A doubled pair has length zero and can only be the valley of its run. Thus
(Z) is the sum of the run-graph degrees of doubled valleys. Each of the
(n-2) nonextreme doubled sums has degree at most two, while the doubled sums
at (min P) and (max P) have degree at most one. Consequently

\[
 0\le Z\le2n-2.                                      \tag{8}
\]

In particular, (7) yields the completely explicit run-count window

\[
 M+2\le2r_\Sigma-r_D\le M+2n.                       \tag{9}
\]

## 3. Finite-interval packing with the explicit defect

Translate (P) so that (min P=0), and put (L=\operatorname{span}(P)).
Since (1\notin D), packing the (M) differences and the (r_D-1) gaps
between their runs into ({2,\ldots,L\}) gives

\[
 L\ge M+r_D.                                        \tag{10}
\]

Likewise, (Sigma\subseteq[0,2L]). Packing its (N) sums and its
(r_\Sigma-1) inter-run gaps gives

\[
 r_\Sigma\le2L+2-N.                                \tag{11}
\]

Combining (7) and (11) gives the new defect-sensitive inequality

\[
 \boxed{\ 4L+4\ge3M+4n+r_D-Z.\ }                   \tag{12}
\]

Thus one convenient complete form of the interval budget is

\[
 L\ge
 \max\left\{
 M+r_D,
 \left\lceil\frac{3M+4n+r_D-Z-4}{4}\right\rceil
 \right\},                                         \tag{13}
\]

with (0\le Z\le2n-2). Eliminating the defect gives, more coarsely,

\[
 4L\ge3M+2n+r_D-2\ge3M+2n-1.                       \tag{14}
\]

Formula (12), rather than (14), is the useful finite statement: it retains
exactly the exceptional adjacent sums centered at source marks.

## 4. Exact remaining limitation

This ledger controls the **total** internal length of all adjacent-difference
runs, namely (M-r_D), by distinct valley-side cells. It does not bound the
length of each individual difference run. The reason is that the
correspondence does not preserve run incidence.

Indeed, suppose the interval representing (d+i) starts at (a_i). The
adjacency between the intervals for (d+i) and (d+i+1) maps to the
pair-sum edge beginning at

\[
 t_i=a_i+a_{i+1}+d+i.
\]

For successive adjacencies in the same difference run,

\[
 t_{i+1}-t_i=a_{i+2}-a_i+1,                         \tag{15}
\]

which can be large. Hence consecutive edges of one difference run may land
in unrelated pair-sum runs. The valley theorem constrains every image edge
and makes the physical-cell charge injective at the pair-sum-edge level, but
it supplies no chain connecting the images in (15).

Any uniform cap on an individual adjacent-difference run therefore needs a
new relation among three successive ruler intervals, or an estimate forcing
many of the values in (15) to be small. Equations (6), (12), and the explicit
defect (Z) are the complete consequence of the present two-edge
correspondence and valley structure.
