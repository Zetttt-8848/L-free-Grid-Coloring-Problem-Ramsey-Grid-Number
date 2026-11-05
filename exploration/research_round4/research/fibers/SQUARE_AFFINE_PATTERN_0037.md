# Why an unconstrained Gallai copy does not force a square corner

## 1. Root-pair formulation

Write the square-source cell \((J^2,I^2)\) as the lattice point
\((J,I)\), where \(J>I>0\).  Three root-pair points form a positive
corner only if, after naming them

\[
u=(b,a),\qquad v=(d,a),\qquad w=(d,c),
\tag{1}
\]

they satisfy

\[
a<c,qquad b<d,qquad b^2-a^2=d^2-c^2.
\tag{2}
\]

The first two coordinate coincidences in (1) are preserved by a common
translation and homothety.  The quadratic equality in (2) is not.

## 2. The compatibility line for one fixed L

Let the three points in (1) belong to a fixed lattice pattern.  Under
the homothety with positive integer scale \(q\) and translation
\((s,t)\), they become

\[
u'=(s+qb,t+qa),\quad
v'=(s+qd,t+qa),\quad
w'=(s+qd,t+qc).
\tag{3}
\]

The required square-difference equality is

\[
(s+qb)^2-(t+qa)^2
=(s+qd)^2-(t+qc)^2.
\tag{4}
\]

After expansion and division by \(q>0\), this is exactly

\[
2s(b-d)+2t(c-a)
+q\bigl[(b^2-a^2)-(d^2-c^2)\bigr]=0.
\tag{5}
\]

For fixed \(q\), equation (5) is one affine line in the translation
plane.  It is a genuine line because a positive L has \(b-d<0\) and
\(c-a>0\).  Even when the original L already satisfies (2), its
translates remain square corners only on the line

\[
s(d-b)=t(c-a).
\tag{6}
\]

Thus being a square corner is not a translation-invariant property of
a root-pair L.

## 3. No finite pattern can repair the translation defect

**Lemma.**  Let \(P\subset\mathbb Z^2\) be finite.  There are infinitely
many integer translations \((s,t)\) for which

\[
(s,t)+P\subset\{(J,I):J>I>0\}
\tag{7}
\]

but the translated copy contains no square corner whose three points
come from \(P\).

**Proof.**  Only triples of points in \(P\) already having the two
coordinate coincidences in (1) can become corners after translation.
There are finitely many such positive L triples.  By (5), with \(q=1\),
each one can satisfy the square equality only when \((s,t)\) lies on
one particular affine line.

For a completely explicit avoidance, put

\[
s=n^2+S,qquad t=n+T,
\tag{8}
\]

where \(S,T\) are fixed integers.  Substitution into (5) gives, for
each candidate L, a polynomial in \(n\) whose leading coefficient is

\[
2(b-d)\ne0.
\tag{9}
\]

It therefore vanishes for at most two values of \(n\).  Since there
are only finitely many candidate triples, every sufficiently large
integer \(n\), apart from a finite exceptional set, avoids all their
compatibility lines.  For sufficiently large \(n\), (8) also makes
both coordinates positive and makes \(J-I>0\) uniformly for every
\((J,I)\in(s,t)+P\), because \(s-t\to\infty\).  This proves the lemma.
\(\square\)

The same proof applies to a finite collection of finite patterns: a
finite union of compatibility lines still misses infinitely many
admissible integer translations.

## 4. Consequence for the direct Gallai strategy

Gallai's lattice theorem can give a monochromatic copy

\[
(s,t)+qP
\tag{10}
\]

of a prescribed finite pattern, but it does not prescribe \((s,t)\).
For every fixed scale \(q\), the square-corner translations of (10)
lie in the finite union of the lines (5), one line per positive L in
\(P\).  Section 3 shows that admissible translations outside this
union are abundant.  Consequently, the mere existence of a
monochromatic homothetic copy of \(P\) gives no square corner.

This is not just a defect of choosing a pattern whose original L was
slightly wrong.  If an L is already a square corner, translation
reduces its preservation to the homogeneous line (6).  No
nondegenerate L is valid under every common translation.

## 5. Polynomial versions with a free common translate

The same obstruction persists if the three entries of the L depend on
an auxiliary parameter \(r\).  Let

\[
u_r=(B(r),A(r)),\quad
v_r=(D(r),A(r)),\quad
w_r=(D(r),C(r)).
\tag{11}
\]

After a free common translation \((s,t)\), the square identity expands
to

\[
2s(B-D)+2t(C-A)
+B^2-A^2-D^2+C^2=0,
\tag{12}
\]

where all four letters on the right are evaluated at \(r\).  If (12)
is to hold identically for all \(s,t\), its two linear coefficients
force

\[
B(r)=D(r),\qquad A(r)=C(r),
\tag{13}
\]

so the L degenerates.  Hence allowing polynomial coordinates does not
make a nonzero square corner compatible with an uncontrolled common
translation.

## 6. Exact remaining gap

This argument excludes the direct scheme

\[
\text{finite root-pair pattern}
\;\xrightarrow{\text{Gallai}}\;
\text{monochromatic homothetic copy}
\;\Longrightarrow\;
\text{square corner}.
\]

It does not prove that the infinite square source is two-colorable.
A Ramsey-based obstruction would need an additional mechanism that
forces the translation and scale onto one of the compatibility loci
(5), or a different finite coloring theorem formulated directly on a
polynomially constrained family of cells.  Standard unrestricted
translation is precisely the unsupported step.
