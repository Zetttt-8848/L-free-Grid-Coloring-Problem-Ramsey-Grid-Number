# Corners frontier: source dictionary (R4-RESEARCH-0001)

**Scope checked 2026-09-11.** This note records external, primary-source
results relevant to the positive-step directed grid L
\[
 H(x,y;d)=\{(x,y),(x+d,y),(x+d,y+d)\},\qquad d>0.
\]
It is a source map, not a claim that any of the research-round constructions
proved these theorems.  The April-2025 theorem below supersedes the former
inverse-iterated-log density frontier for the present general-growth question.

## 1. The current quantitative theorem

**Jaber--Liu--Lovett--Ostuni--Sawhney (JLL0S), _Quasipolynomial bounds for
the corners theorem_, arXiv:2504.07006 (2025), Theorem 1.1, pp. 1--2;
ECCC TR25-047.**  This is the primary current source checked.  Its theorem is:

> There is an absolute \(c>0\) such that, for every finite abelian group
> \(G\), if \(A\subseteq G^2\) contains no
> \((x,y),(x+d,y),(x,y+d)\) with \(d\ne0\), then
> \[
> |A|\le |G|^2\exp\{-c(\log |G|)^{1/600}\}.
> \]

The displayed exponent \(1/600\), rather than merely an unspecified
\(\Omega(1)\), is in Theorem 1.1.  The authors immediately state that an
embedding into \(\mathbb Z/(4N)\mathbb Z\) gives the analogous integer-grid
statement and that Green's trick (cited there as Shkredov, Lemma 6.2) gives an
essentially identical bound while avoiding only \(d>0\).  Thus this is a
source-stated consequence, not a new transfer asserted here.

### Translation to this project's L and its Ramsey consequence

Put \(P(a,b;d)=\{(a,b),(a+d,b),(a,b+d)\}\).  The integral unimodular
shear
\[
 T(x,y)=(x-y,y)
\]
sends \(H(x,y;d)\) exactly to \(P(x-y,y;d)\).  Hence it preserves the
step and takes the finite-group version of the directed L problem to the
JLL0S pattern.  In particular, for a \(k\)-coloring of \(G^2\), the largest
color class and Theorem 1.1 give
\[
 \frac1k\le \exp\{-c(\log|G|)^{1/600}\}
\]
whenever it has no directed L.  Therefore a directed L is forced once
\[
 |G|\ge \exp\!\bigl(C(\log k)^{600}\bigr)                 \tag{FF/group}
\]
for an absolute \(C\).  This is a formal corollary of the theorem plus the
displayed shear.

For the integer square, the same conclusion holds after the standard
boundary/direction transfer.  One fully elementary way to keep the sign issue
visible is to color a point by its color together with the color of its
half-turn, use the finite cyclic model \(\mathbb Z/(2N)\mathbb Z\), and
reflect one coordinate to interchange the project L with \(P\).  A
same-product-color modular corner has a common signed increment; a negative
increment reflects to a positive project L.  On \([N]^2\), increments in
\([-(N-1),N-1]\) that agree modulo \(2N\) agree as integers.  The selected
product class has density at least \(1/(4k^2)\) in the cyclic square.  JLL0S
then yields, with absolute constants and after absorbing the small-size range,
\[
 R_k(L)\le \exp\!\bigl(C(\log(8k^2))^{600}\bigr).          \tag{integer}
\]
This is **far stronger than the requested** \(\exp(\operatorname{poly}(k))\)
form (for example it is at most \(\exp(C'k^{600})\) for \(k\ge2\)).  The
constants are not numerically specified in the cited theorem (this does not
mean they are ineffective), so this does **not** supply a
numerical bound for \(R_3(L)\).

The direction and boundary transfer above is an application of the theorem,
not wording claimed verbatim by JLL0S.  The only source-level input needed is
the signed finite-abelian theorem; the color-pair/reflection argument records
why it applies to this project's one positive orientation.

### Finite-field specialization

**JLL0S, Theorem 1.5 in arXiv:2504.07006v1, p. 2.** For
\(A\subseteq\mathbb F_2^n\times\mathbb F_2^n\) avoiding
the same standard corners and \(Q=2^n\),
\[
 |A|\le Q^2\exp\{-c(\log Q)^{1/178}\}.
\]
Here \(-d=d\), so there is no positive-versus-negative distinction; the shear
above applies verbatim.  A \(k\)-coloring of
\(\mathbb F_2^n\times\mathbb F_2^n\) therefore forces a directed L when
\[
 n\ge C(\log k)^{178},\quad\text{equivalently}\quad
 Q\ge\exp\{C(\log k)^{178}\}.
\]
This is a model result.  It does not by itself give the integer-square result
without a separate transfer, for which the general finite-abelian theorem above
is the appropriate source.

## 2. Earlier references and comparison baselines

**Graham--Solymosi, _Monochromatic equilateral right triangles on the integer
grid_, Topics in Discrete Mathematics 26 (2006), pp. 129--132, Theorem 1 and
Lemma 3.**  The source proves that an \(r\)-coloring of an \(N\times N\)
grid has a monochromatic standard positive corner for
\(N=(2r)^{2^r}\) (and gives a harmless strict-inequality formulation in its
theorem statement).  Coordinate reflection changes its standard orientation
to the project L.  Thus it gives the historical double-exponential
\(R_k(L)\le (2k)^{2^k}\)-type upper bound.  It is superseded for growth by
JLL0S.

**Shkredov, _On a generalization of Szemerédi's theorem_, Proc. London Math.
Soc. (3) 93 (2006), 723--760.**  JLL0S records this as the prior best corners
estimate: \(|A|\le N^2(\log\log N)^{-c}\), with every \(c<1/73\)
admissible for the standard integer corners problem.  Solving this density
inequality against \(1/k\) produces a much weaker (double-exponential-type)
coloring consequence.  It must not be confused with the new quasipolynomial
density estimate.

**Green, _Lower bounds for corner-free sets_, New Zealand J. Math. 51 (2021),
1--2; arXiv:2102.11702.**  For infinitely many \(N\), there are standard
corner-free \(A\subset[N]^2\) of density
\(2^{-(c+o(1))\sqrt{\log_2N}}\), where
\(c=2\sqrt{2\log_2(4/3)}\approx1.822\).  This shows the JLL0S upper bound
is not close to the known construction scale; it does not obstruct the Ramsey
upper bound above.

**Mammel--Smith--Yerger, _Ramsey Theory on the Integer Grid: The “L” Problem_,
supplied v1 `mammel_v1_complete.txt`, Theorem 8; final publication
Integers 25 (2025), A21, https://math.colgate.edu/~integers/z21/z21.pdf.** Their
anti-diagonal coloring turns a \(k\)-color 3-AP-free interval into an L-free
grid and proves
\[
 R_k(L)\ge \lfloor W(k,3)/2\rfloor+1
\]
(their \(W(k,3)\) is the \(k\)-color, length-three van der Waerden number).
This is a **lower-bound construction**, not an upper-bound reduction.

## 3. Schur / one-dimensional-Ramsey reductions: what is and is not supplied

No checked source identifies the project L Ramsey number with a multicolor
Schur number, nor does a standard Schur bound give the needed upper bound by a
black-box reduction.  The usual diagonal coloring is one-way: if a 1D coloring
is 3-AP-free, coloring the anti-diagonals of the grid produces an L-free square
(the Mammel--Smith--Yerger Theorem 8 construction above).  It therefore proves
a lower bound on \(R_k(L)\), not an upper bound.

The obstruction is structural, not a missing numerical estimate.  A general
grid coloring has \(N^2\) independent color choices.  Restricting to colors
constant on anti-diagonals leaves only \(2N-1\) choices; within that special
family an L reads as a 3-term progression of diagonal indices.  Such a
restriction cannot turn an arbitrary L-free grid coloring into a 1D
Schur- or AP-free coloring.  Conversely, the map based on the difference
\(x-y\) is especially degenerate for this L: its first and third vertices have
the same difference, so monochromaticity only asks for equality of two
1D colors, not a Schur triple.  These direct calculations explain why known
multicolor Schur/van der Waerden estimates are not the relevant route to the
new upper bound.

## Source status and limitations

* Checked primary theorem text: JLL0S arXiv PDF, pp. 1--3 and references;
  Graham--Solymosi PDF, pp. 1--4; the supplied Mammel--Smith--Yerger v1 text.
* The source dictionary is current only through the search date above.  It makes
  no claim that the named exponents or constants are optimal, and no claim of a
  numerical small-\(k\) improvement.
* “Quasipolynomial” describes the density threshold / the logarithm of the
  Ramsey scale; it should not be misreported as a polynomial bound for
  \(R_k(L)\).
