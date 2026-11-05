# The five-rainbow T11 target: exact reductions and remaining gap

Let

\[
 T_{11}=\{(v,u):0\le u<v<11\},
\]

with its 165 positive directed corners

\[
 (v,u),\quad(v+d,u),\quad(v+d,u+d),
 \qquad d>0, v+d<11.
\tag{1}
\]

This note records two exact reductions of the desired statement

\[
 \text{proper three-coloring of }T_{11}
 \quad\Longrightarrow\quad R\ge5,
\tag{2}
\]

and isolates the remaining finite implication.  It does not prove
(2).  In particular, cells are retained as the actual directed-L
vertices in (1); they are not identified with the edges of an ordinary
graph triangle.

## 1. Singleton-load form of the target

Every cell of (T_{11}) belongs to exactly nine corners.  Indeed, for
(p=(v,u)), its numbers of appearances in the three positions in (1)
are

\[
 10-v,qquad v-u-1,qquad u,
\]

whose sum is (9).

In a proper three-coloring, every non-rainbow corner has a two-plus-one
color pattern and therefore has a unique singleton-colored cell.  For
a cell (p), let (lambda(p)) be the number of incident corners in
which (p) is this singleton.  The 165 corners partition into rainbow
corners and corners charged to their unique singleton, so

\[
 \boxed{R+\sum_{p\in T_{11}}\lambda(p)=165.}
\tag{3}
\]

Equivalently, let (n_{\ell,i}) be the number of cells of color (i)
on a row, column, or slope-one diagonal (ell).  The equal pair on a
two-colored corner is its repeated-color pair, and each same-line pair
has one actual completion.  Thus

\[
 \sum_p\lambda(p)
 =\sum_{\ell,i}\binom{n_{\ell,i}}2.
\tag{4}
\]

The five-rainbow statement is exactly either of the inequalities

\[
 \sum_p\lambda(p)\le160,
 \qquad
 \sum_{\ell,i}\binom{n_{\ell,i}}2\le160.
\tag{5}
\]

Using the line-discrepancy notation of
`TRIANGLE_RAINBOW_ENERGY.md`, it is also exactly

\[
 V\le100.
\tag{6}
\]

These formulations show what a local charging proof must supply: five
of the 165 corner incidences must remain uncharged by repeated-color
line pairs.  The fact that every cell has corner degree nine does not
itself limit (lambda(p)) enough to prove (5); different roles and
steps can charge the same singleton.

## 2. Exact corner-sum reduction

Identify the colors with (mathbb F_3), and use triangular coordinates

\[
 S_9=\{(x,y):x,y\ge0, x+y\le9\},
 \qquad F(x,y)=z(x+y+1,y).
\]

For every available base and positive step put

\[
 g_d(x,y)=F(x,y)+F(x+d,y)+F(x,y+d).
\tag{7}
\]

A proper corner has (g_d=0) exactly when it is rainbow.  Hence (2)
is equivalent to saying that every proper lift has at least five zero
coordinates among the 165 values in (7).

The reconstruction theorem in `CORNER_SUM_COORDINATES.md` gives a
particularly precise finite form.  Take as basis coordinates

\[
 \mathcal G=
 \{g_1(x,y):(x,y)\in S_8\}
 \cup
 \{g_2(x,0):0\le x\le7\}.
\tag{8}
\]

There are (45+8=53=|T_{11}|-2) coordinates.  Every assignment to
(mathcal G) occurs, and it determines all 165 corner sums.  The nine
cell labelings above one signature differ by

\[
 F(x,y)\longmapsto F(x,y)+\alpha+\beta(x-y).
\tag{9}
\]

All corner sums, and hence their number of zeros, are invariant under
(9).

For the canonical lift (F_0), form the excluded-slope set

\[
 \mathcal H(F_0)=
 \left\{-\frac{F_0(x+d,y)-F_0(x,y)}d:
   g_d(x,y)=0, 3\nmid d\right\}\subseteq\mathbb F_3.
\tag{10}
\]

The lift criterion gives the following exact restatement.

**Proposition.**  A counterexample to (2) exists if and only if there
is a signature on the 53 coordinates (8) such that:

1. after reconstruction, at most four of all 165 values (g_d(x,y))
   vanish;
2. every zero-sum corner whose step is divisible by three is rainbow
   in the canonical lift;
3. (mathcal H(F_0)\ne\mathbb F_3).

**Proof.**  Conditions 2 and 3 are precisely the necessary and
sufficient criterion for at least one affine lift (9) to be proper.
Condition 1 then says that this proper lift has at most four rainbow
corners.  Conversely, the signature of any proper counterexample has
the same zero set, satisfies the divisible-step condition, and leaves
its own value of (eta) outside (10).  \(\square\)

Thus no choice of the two affine seed values remains in the problem.
The missing implication is the finite statement

\[
 \#\{g_d=0\}\le4
 \quad\Longrightarrow\quad
 \bigl(\text{a divisible-step zero is monochromatic}igr)
 \ \text{or}\ 
 \mathcal H(F_0)=\mathbb F_3.
\tag{11}
\]

A proof of (11) would establish (2).  Proving instead that every
(mathbb F_3)-labeling has five zero sums would be stronger: it would
discard both alternatives on the right of (11), without using
properness.

## 3. The simplest linear blocking certificate cannot occur

There is a tempting way to prove the stronger statement.  Regard each
corner as its incidence vector

\[
 q_e\in\mathbb F_3^{55},
\]

with three entries equal to one.  A labeling (F) has zero corner sum
at (e) exactly when (F\cdot q_e=0).  If four actual corner vectors
formed all four points of a projective line over (mathbb F_3), then
every linear functional would vanish on at least one of them.  Five
disjoint such lines would immediately give five zero corners.

No projective line is contained in the actual corner-vector set.
Indeed, take two distinct corner supports (A,B), each of size three.
The other two projective points in their span are represented by

\[
 1_A+1_B,qquad 1_A-1_B.
\]

For the sum, disjoint supports give weight six.  If the supports
overlap nontrivially, the intersection has coefficient two and the
symmetric difference coefficient one, so the vector is not a scalar
multiple of a (0)-(1) vector of weight three.  For the difference,
the intersection cancels while the two nonempty sides of the symmetric
difference have coefficients one and two.  Again it is not projectively
a corner incidence vector.  Therefore

\[
 \boxed{\{[q_e]:e\text{ an actual corner of }T_{11}\}
 \text{ is a projective cap}.}
\tag{12}
\]

This rules out the smallest independent linear blocking argument.  A
corner-sum proof must combine several compatibility relations, such as

\[
 D_e g_d=D_d g_e,
\tag{13}
\]

rather than partitioning the coordinates into projective lines.

## 4. Bounded outcome

The supplied coloring with five rainbow corners proves that the target
constant, if (2) is established, is sharp.  The derivations above do
not exclude a proper coloring with at most four rainbows.  A bounded
constraint attempt at the stronger arbitrary-labeling statement was
stopped without a result and supplies no premise.

The exact unresolved task is (11), or equivalently the singleton-load
inequality (5).  The reconstruction proposition reduces it to 53 free
corner-sum coordinates and an explicit three-slope obstruction, while
the cap lemma (12) explains why a direct five-block linear certificate
does not close it.  No (R_3\le464) conclusion follows from this note
without a proof of (11).
