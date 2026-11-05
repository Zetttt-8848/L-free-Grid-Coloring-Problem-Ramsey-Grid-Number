# A root-arithmetic obstruction for the square source

## Scope

For a square-source cell \((J^2,I^2)\), with \(1\le I<J\), the two
natural root factors are

\[
J-I,\qquad J+I.
\]

The construction below rules out every coloring obtained from a fixed
finite package of residue information about \(I,J,J-I,J+I\), together
with exact valuations of \(J-I,J+I\) at any fixed finite set of primes.
In particular, no arbitrary Boolean function of

\[
\bigl(v_2(J-I),v_2(J+I)\bigr)
\]

can properly color all square sources.  This is a cell-dependent
obstruction: it does not assume that the color is constant on a
numerical-difference fiber.

## The four-root corner

Let \(R\) be a positive integer and set

\[
\alpha=8R+3,\qquad
\beta=72R+7,\qquad
\gamma=64R+3,\qquad
\delta=96R+7.
\tag{1}
\]

Then

\[
\alpha<\gamma<\beta<\delta.
\tag{2}
\]

The root factors of the two endpoint cells are

\[
\begin{array}{c|cc}
\text{cell}&J-I&J+I\\ \hline
(\beta^2,\alpha^2)&64R+4&80R+10\\
(\delta^2,\gamma^2)&32R+4&160R+10.
\end{array}
\tag{3}
\]

Consequently

\[
\begin{aligned}
\beta^2-\alpha^2
 &= (64R+4)(80R+10)\\
 &=40(16R+1)(8R+1)\\
 &= (32R+4)(160R+10)\\
 &=\delta^2-\gamma^2.
\end{aligned}
\tag{4}
\]

Thus the three cells

\[
(\beta^2,\alpha^2),\qquad
(\delta^2,\alpha^2),\qquad
(\delta^2,\gamma^2)
\tag{5}
\]

form a positive corner in the square source through \(\delta^2\).  The
root factors of its completion cell are

\[
\delta-\alpha=88R+4,
\qquad
\delta+\alpha=104R+10.
\tag{6}
\]

Equations (3) and (6) have the decisive feature

\[
J-I\equiv4\pmod R,
\qquad
J+I\equiv10\pmod R
\tag{7}
\]

for every one of the three cells in (5).  Their higher roots are all
\(7\pmod R\), and their lower roots are all \(3\pmod R\).

## Exact obstruction theorem

Fix a modulus \(Q\ge1\) and a finite set of primes \(P\).  Consider any
coloring rule whose value on \((J^2,I^2)\) is an arbitrary function of

\[
\begin{split}
&I\bmod Q,\quad J\bmod Q,\quad
(J-I)\bmod Q,\quad(J+I)\bmod Q,\\
&\bigl(v_p(J-I),v_p(J+I)\bigr)_{p\in P}.
\end{split}
\tag{8}
\]

No such rule properly colors \(V(\{1^2,\ldots,m^2\})\) for every
\(m\).

To prove this, choose \(R\) divisible by \(Q\) and, for every \(p\in P\),
by

\[
p^{1+\max\{v_p(4),v_p(10)\}}.
\tag{9}
\]

The congruences in (7) then imply, for each \(p\in P\),

\[
v_p(J-I)=v_p(4),
\qquad
v_p(J+I)=v_p(10)
\tag{10}
\]

on all three cells in (5).  Indeed, a number congruent to \(4\) modulo
a power of \(p\) strictly larger than \(v_p(4)\) has valuation
\(v_p(4)\), and similarly for \(10\).  Since \(Q\mid R\), the four
residue entries in (8) are also identical on the three cells.  Hence
all three cells receive the same color, contradicting properness.

The same argument also covers residues modulo \(Q\) of the
\(p\)-free parts of the two factors.  Choose \(R\) with the additional
factor \(Q\) after the powers in (9).  Dividing the differences between
corresponding factors by their common exact power of \(p\) still leaves
a multiple of \(Q\).  For the most natural dyadic version this is
visible directly:

\[
\begin{array}{c|cc}
& (J-I)/4&(J+I)/2\\ \hline
(\beta,\alpha)&16R+1&40R+5\\
(\delta,\alpha)&22R+1&52R+5\\
(\delta,\gamma)&8R+1&80R+5,
\end{array}
\tag{11}
\]

so the reduced odd parts are respectively \(1\) and \(5\) modulo every
divisor of \(R\).

As a small instance, \(R=1\) gives

\[
(\alpha,\gamma,\beta,\delta)=(11,67,79,103).
\tag{12}
\]

For each cell in the corner

\[
(79^2,11^2),\qquad(103^2,11^2),\qquad(103^2,67^2),
\tag{13}
\]

the exact pair of dyadic valuations is

\[
\bigl(v_2(J-I),v_2(J+I)\bigr)=(2,1).
\tag{14}
\]

Thus even an unrestricted lookup table on the two exact dyadic
valuations is monochromatic on this corner.

## What remains open

The obstruction applies to fixed finite local arithmetic signatures.
It does not exclude a rule that uses unbounded magnitude information,
a modulus depending on \(I\) or \(J\), the position of a representation
inside its full equal-difference fiber, or colors defined recursively
from interactions among several cells.  Therefore it supplies no
non-two-colorability result for the square source itself.  It isolates
the remaining requirement: a uniform square-source coloring, if one
exists, must distinguish the three cells in (5) despite their agreement
on every prescribed finite package of root residues and valuations.
