# Product-core geometry: a translated weak triangle and its last-pattern obstruction

Base: `handoff_20260912/RESEARCH_HANDOFF.md`, SHA-256
`614A721B10ADEE968767A51D2F3CFB30A877BB9DD1BE57919D68E3F63E11754F`,
checkpoint R4-RESEARCH-0013 plus the terminal product experiments.  This note
uses the saved negative core only to discover geometry.  It does not promote a
SAT answer to a paper proof.

## 1. Setting and statements

For a finite ordered integer set `S`, write

\[
W(S)=\{(v,u):u,v\in S, u\le v\}.
\]

A positive-step corner is

\[
K(y,x;s)=\{(y,x),(y+s,x),(y+s,x+s)\},\qquad s>0,
\tag{1}
\]

when all three cells belong to `W(S)`.  A two-coloring of `W(S)` is
proper when no set (1) is monochromatic.

Let `G = {g_0<g_1<g_2}` have distinct positive differences, put
`D = g_2-g_0`, and choose

\[
P>2D,\qquad Q>2(D+P).
\tag{2}
\]

Define the separated product

\[
C=G+P\{0,1\}+Q\{0,1\}.
\tag{3}
\]

The desired full auxiliary statement would be that `W(C)` is not properly
two-colorable for every choice satisfying (2).  This note proves the exact
geometric reduction of the saved core to (3), and proves a parameterized
obstruction for the one diagonal pattern singled out by finite propagation.
It does not complete the reduction from an arbitrary diagonal coloring to
that pattern.

Colors below are named blue and green.  Exchanging their names changes no
claim.  Objects are labeled, so no quotient by reflection or factor
permutation is being taken.

## 2. Geometric reduction and conditional obstruction

### 3.1 The four-factor core is a weak-triangle core

The four-factor experiment uses

\[
E(b,\varepsilon,i,j)=b+H(\varepsilon+3i+9j),
\qquad G=\{0,1,3\},\quad H=7.
\tag{4}
\]

Every saved core vertex is a cell whose row endpoint has `epsilon=1` and
whose column endpoint has `epsilon=0`.  On this
slice define

\[
\pi(b,\varepsilon,i,j)=b+3Hi+9Hj.
\tag{5}
\]

Then, for every slice cell from `x` to `y`,

\[
E(y)-E(x)=H+\pi(y)-\pi(x).
\tag{6}
\]

Consequently two slice cells represent the same source difference exactly
when their projected cells have the same difference.  If the two
representations have lower endpoints `x<u`, their source corner projects
to

\[
(\pi(y),\pi(x)),\quad(\pi(v),\pi(x)),\quad(\pi(v),\pi(u)),
\]

which is (1), with

\[
s=\pi(u)-\pi(x)=\pi(v)-\pi(y)>0.
\]

All 56 saved projected cells satisfy `pi(y) >= pi(x)`.  They therefore lie
in the ordinary weak triangle on

\[
C=\{0,1,3\}+21\{0,1\}+63\{0,1\}
 =\{0,1,3,21,22,24,63,64,66,84,85,87\}.
\tag{7}

Every one of the 75 saved triples is a positive-step corner in `W(C)`.
Thus the four-factor obstruction is not intrinsically four-dimensional: it
lives in the translated weak triangle on the three factors left after the
fixed binary slice is removed.

The same projection works for `G x {0,1}^3` with arbitrary separated
weights.  Fixing one binary coordinate to be 1 at every row endpoint and 0
at every column endpoint cancels its constant gap from equality of
differences and leaves `W(G+P{0,1}+Q{0,1})`.  Conditions (2) make the
coordinate representation unique and preserve the lexicographic order used
by every displayed corner.

### 3.2 A parameterized obstruction for the last diagonal pattern

Denote a cell by `[y,x]`.  The only forcing rule used below is

> If two cells of a corner have the same color, its third cell has the
> opposite color.

In particular, equal-colored diagonal cells `[x,x]` and `[y,y]` force
`[y,x]` to the opposite color.

The numerical labels in the next lemma are symbolic shorthand.  Apply the
substitution

\[
\begin{array}{lll}
0\mapsto g_0,&1\mapsto g_1,&3\mapsto g_2,\\
21\mapsto g_0+P,&22\mapsto g_1+P,&24\mapsto g_2+P,\\
63\mapsto g_0+Q,&64\mapsto g_1+Q,&66\mapsto g_2+Q,\\
84\mapsto g_0+P+Q,&85\mapsto g_1+P+Q,&87\mapsto g_2+P+Q.
\end{array}
\tag{8}
\]

Every equality of steps below is an identity in the five symbols
`g_0,g_1,g_2,P,Q`, and every step is positive by (2).

**Last-pattern lemma.**  A proper two-coloring of `W(C)` cannot have the
following diagonal colors:

\[
\begin{array}{c|ccc}
\text{translate}&g_0&g_1&g_2\\ \hline
0&B&G&B\\
P&G&B&B\\
Q&G&B&G\\
P+Q&B&G&G
\end{array}
\tag{9}
\]

The color-reversed pattern is impossible as well.

**Proof.**  Branch on the color of `[63,0]`.

If `[63,0]` is green, repeated application of the forcing rule gives

\[
\begin{array}{c|c|c}
&\text{same-colored cells}&\text{forced cell}\\ \hline
1 &[0,0],[84,84]\ (B)&[84,0]\ (G)\\
2 &[63,0],[84,0]\ (G)&[84,21]\ (B)\\
3 &[21,21],[85,85]\ (G)&[85,21]\ (B)\\
4 &[84,21],[85,21]\ (B)&[85,22]\ (G)\\
5 &[1,1],[66,66]\ (G)&[66,1]\ (B)\\
6 &[1,1],[87,87]\ (G)&[87,1]\ (B)\\
7 &[66,1],[87,1]\ (B)&[87,22]\ (G)\\
8 &[21,21],[87,87]\ (G)&[87,21]\ (B)\\
9 &[84,21],[87,21]\ (B)&[87,24]\ (G).
\end{array}
\tag{10}
\]

Now `[85,22],[87,22],[87,24]` are a monochromatic green corner, of
step `g_2-g_1>0`.

If `[63,0]` is blue, the corresponding forcing chain is

\[
\begin{array}{c|c|c}
&\text{same-colored cells}&\text{forced cell}\\ \hline
1 &[1,1],[85,85]\ (G)&[85,1]\ (B)\\
2 &[1,1],[87,87]\ (G)&[87,1]\ (B)\\
3 &[85,1],[87,1]\ (B)&[87,3]\ (G)\\
4 &[0,0],[84,84]\ (B)&[84,0]\ (G)\\
5 &[84,0],[87,3]\ (G)&[87,0]\ (B)\\
6 &[63,0],[87,0]\ (B)&[87,24]\ (G)\\
7 &[87,3],[87,24]\ (G)&[66,3]\ (B)\\
8 &[3,3],[24,24]\ (B)&[24,3]\ (G)\\
9 &[3,3],[84,84]\ (B)&[84,3]\ (G)\\
10&[24,3],[84,3]\ (G)&[84,63]\ (B)\\
11&[63,63],[85,85]\ (G)&[85,63]\ (B)\\
12&[84,63],[85,63]\ (B)&[85,64]\ (G)\\
13&[24,3],[85,64]\ (G)&[85,3]\ (B)\\
14&[1,1],[66,66]\ (G)&[66,1]\ (B)\\
15&[66,1],[87,1]\ (B)&[87,22]\ (G)\\
16&[87,22],[87,24]\ (G)&[85,22]\ (B).
\end{array}
\tag{11}
\]

The cells `[66,3],[85,3],[85,22]` are now a monochromatic blue corner;
its step is `P-(g_2-g_1)>0`.  Both colors of `[63,0]` contradict
properness.  This proves (9), and exchanging blue and green proves its
complement.  \(\square\)

All cells in (10) and (11), including the two final corners, occur among the
saved 56 vertices, and all used triples occur among the saved 75 corners.
The proof therefore explains a genuine geometric submechanism inside the
saved core, rather than filling unspecified cells of `W(C)`.

### 3.3 Exact remaining gap

The diagonal of a hypothetical coloring is an arbitrary coloring of the 12
marks in (7).  The usual diagonal-completion argument first forces each
diagonal color class to be Golomb.  The ordered mixed-interval lemma and the
branched forcing lemma remove many further patterns, but they do not by
themselves force (9).

Finite NAE propagation from the diagonal cells singled out (9), up to color
exchange, as the last surviving diagonal pattern and then found the branch
above.  That first statement is still a finite discovery result.  A short
case-free derivation, or a compact hand-checkable case partition proving that
every other diagonal pattern already fails, was not obtained in this bounded
attempt.  Therefore the proposed universal non-two-colorability of `W(C)`
is not asserted as a paper theorem here.

This isolates the missing implication precisely:

\[
\boxed{\text{proper coloring of }W(C)
\quad\Longrightarrow\quad
\text{diagonal pattern (9), up to exchanging colors}.}
\tag{12}
\]

The conclusion of (12) is now symbolically impossible by the last-pattern
lemma.  Proving (12) would turn the saved negative core into a complete
parameterized weak-triangle obstruction for every separated three-point
Golomb factor times two binary factors, and hence explain the corresponding
fixed slice of the four-factor product.

## 4. Scope of the result

The projection and the conditional diagonal-pattern obstruction are the mathematical results of this note. The reduction of arbitrary diagonal colors to pattern (9) remains open. No general source-size inequality or Ramsey improvement follows.

The generated auxiliary script is retained as a local artifact. Its execution status is not a premise of either derivation and supplies no missing arbitrary-diagonal argument.
