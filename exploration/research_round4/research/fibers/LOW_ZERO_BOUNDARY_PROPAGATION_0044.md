# Boundary propagation for low zero-sum signatures on S9

Use the simplex

\[
 S_9=\{(x,y):x,y\ge0, x+y\le9\}
\]

and write

\[
 g_d(x,y)=F(x,y)+F(x+d,y)+F(x,y+d)\in\mathbb F_3
\tag{1}
\]

whenever (x+y+d\le9).  The barycentric base of this corner is

\[
 (x,y,z),\qquad z=9-d-x-y.
\tag{2}
\]

Call the corner a boundary-base corner when (xyz=0).  This note gives
an exact local propagation rule for nonzero corner sums, then an
explicit proper coloring showing that all zero sums can avoid the
entire barycentric boundary.  Consequently a proof for a putative
four-zero signature must use the small zero budget quantitatively; a
bare boundary-puncturing assertion is false.

## 1. A six-sum propagation lemma

For a triple (a,b,c\in\{1,-1\}\subset\mathbb F_3), define its sign
type by

\[
 \mu(a,b,c)=
 \begin{cases}
 0,&a=b=c,\\
 1,&\text{two entries are }1\text{ and one is }-1,\\
 -1,&\text{two entries are }-1\text{ and one is }1.
 \end{cases}
\tag{3}
\]

Then simply

\[
 a+b+c=\mu(a,b,c)\quad\text{in }\mathbb F_3.
\tag{4}
\]

The commuting corner operators give, for every available base and
positive (d,e),

\[
 \begin{aligned}
 &g_d(x,y)+g_d(x+e,y)+g_d(x,y+e)\\
 &\hspace{20mm}=
 g_e(x,y)+g_e(x+d,y)+g_e(x,y+d).
 \end{aligned}
\tag{5}

Therefore:

**Six-sum lemma.**  If all six entries in (5) are nonzero, then

\[
 \boxed{
 \mu\bigl(g_d(x,y),g_d(x+e,y),g_d(x,y+e)\bigr)
 =
 \mu\bigl(g_e(x,y),g_e(x+d,y),g_e(x,y+d)\bigr).}
\tag{6}
\]

Conversely, a mismatch of the two sign types in (6) forces at least one
of those six actual corner sums to vanish.

This gives a direct low-zero consequence.  If (mathcal Q) is any
family of compatibility instances (5) with pairwise disjoint sets of
six corner-sum coordinates, then a signature with at most four zeros
can have sign-type mismatch in at most four members of (mathcal Q).
More generally, mismatches form a hypergraph covered by the zero-sum
coordinates, with each compatibility instance using exactly the six
displayed corners.  A boundary propagation proof can therefore close
the five-zero target if it produces five disjoint forced mismatches.

The lemma is stronger than a formal restatement of the target: it
turns the operator identity into a three-valued deterministic transport
rule on every zero-free compatibility hexagon.

## 2. A proper coloring with no boundary-base zero

The following explicit (F:S_9\to\mathbb F_3) shows that boundary
avoidance alone cannot force a zero.  In row (y), the string lists
(F(0,y),F(1,y),\ldots,F(9-y,y)):

\[
\begin{array}{c|l}
y&\text{values}\ \\ \hline
0&0201121210\\
1&001012210\\
2&12010020\\
3&1200120\\
4&101122\\
5&02201\\
6&0101\\
7&011\\
8&12\\
9&1
\end{array}
\tag{7}
\]

Here is a full corner-sum certificate.  For fixed (d), successive
strings are the rows (y=0,1,\ldots,9-d), and each string lists
(g_d(x,y)) with (x) increasing.  Thus the table contains all 165
actual positive-step corners.

\[
\begin{array}{c|l}
d&\text{rows of }g_d\\ \hline
1&222212211/10120121/1111112/121221/10102/2222/122/21/1\\
2&12112112/2222122/201212/11022/2201/201/11/2\\
3&2222121/111011/21201/1121/201/12/2\\
4&212111/11212/1022/221/11/2\\
5&22122/2021/121/11/1\\
6&1212/222/11/2\\
7&211/22/2\\
8&21/1\\
9&1
\end{array}
\tag{8}
\]

Every nonzero entry of (8) corresponds to a corner using exactly two
colors.  The thirteen zero entries, written with their full
((d,x,y,z)) base data and ordered color triples, are

\[
\begin{array}{c|c}
(d,x,y,z)&(F(x,y),F(x+d,y),F(x,y+d))\\ \hline
(1,1,1,6)&012\\
(1,4,1,3)&120\\
(1,1,4,3)&012\\
(1,3,4,1)&120\\
(2,1,2,4)&210\\
(2,2,3,2)&012\\
(2,2,4,1)&120\\
(2,1,5,1)&201\\
(3,3,1,2)&021\\
(3,3,2,1)&120\\
(3,1,4,1)&021\\
(4,1,2,2)&201\\
(5,1,1,2)&021
\end{array}
\tag{9}
\]

Each zero is visibly rainbow, so (7)--(9) prove properness directly.
Every base in (9) has

\[
 x>0,qquad y>0,qquad z>0.
\]

Thus all boundary-base corners have nonzero sum:

\[
 \boxed{
 \text{a proper coloring of }T_{11}\text{ can have every rainbow
 corner based strictly inside the simplex}.}
\tag{10}
\]

This construction has thirteen rainbow corners.  It is a limitation of
an unconditional boundary argument, not a counterexample to the desired
five-rainbow lower bound.

## 3. Exact remaining low-zero implication

Assume now that a proper coloring has at most four zero sums.  The
six-sum lemma says that every collection of five pairwise disjoint
compatibility hexagons must contain at least one whose two nonzero sign
types agree; equivalently, five forced mismatches would contradict the
zero budget.  If all zeros avoid the barycentric boundary, then every
compatibility instance supported entirely on boundary-base corner sums
obeys the deterministic transport (6).

The construction (7) shows that these boundary transport equations are
jointly consistent with properness.  What remains to prove is a
quantitative interior statement, for example either of the following:

* boundary transport plus affine-slope compatibility forces five
  interior sign-type mismatches; or
* any boundary-zero-free proper signature has at least five interior
  zero sums.

Neither conclusion is derived here.  The precise obstruction is that
an equality of sign types in (6) permits both triples to be monochromatic
as signs, or permits matching majority signs; it does not determine the
six individual signs.  These choices can propagate around the boundary
without a zero, as (8) demonstrates.  A successful continuation must
couple overlapping compatibility hexagons or invoke the three affine
slope exclusions from `T11_FIVE_RAINBOW_LEMMA_0043.md`.
