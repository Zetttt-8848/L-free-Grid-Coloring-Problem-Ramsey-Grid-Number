# A second-moment packing of weak cross-anchor charges

Successor: root's ../NESTED_REFLECTION_HOLE_BUDGET_0041.md retains the
nesting of the same-color tails. The later anchor's difference witness
also lies above the earlier anchor. Consequently every reflected charge
in this note is a hole: the occupied B and C bins are empty. The stronger
result is F<=min(H^+,H^-) and 2F<=n(L+1-n), with exactly
2 binom(mu(r),2) distinct lower/upper holes at each selected output.
The inequalities below remain valid but are superseded by that derivation.

Let

\[
S=B\sqcup C\subseteq[0,L]\cap\mathbb Z
\]

be the diagonal classes of one proper coloring of \(W(S)\).  Both
\(B\) and \(C\) are Golomb.  For \(a\in B\), define

\[
P_a=\{b-a:b\in B,\ b>a\},
\qquad
D_a=\Delta P_a\cap(S-a).
\tag{1}
\]

For \(r\in C\), let

\[
\mathcal A_B(r)=\{a\in B:a<r,\ r-a\in D_a\},
\qquad
m_B(r)=|\mathcal A_B(r)|.
\tag{2}
\]

Each incidence \(a\in\mathcal A_B(r)\) forces the actual cell
\((r,a)\) to have diagonal color \(B\).

The cross-anchor lemma says that for
\(a<a'\) in \(\mathcal A_B(r)\), with

\[
\delta=a'-a,\qquad h=r-a',\qquad t=r-\delta=a+h,
\tag{3}
\]

one has

\[
h\notin D_a.
\tag{4}
\]

If \(t\in S\), the physical corner

\[
(t,a),\qquad(r,a),\qquad(r,a')
\tag{5}
\]

also forces \(z(t,a)\) to have diagonal color \(C\).  If \(t\notin S\),
the same anchor pair exposes an actual source hole.

## 1. Three globally injective charge bins

Let

\[
\Omega_B=
\{(r;a,a'):r\in C,\ a<a'\text{ in }\mathcal A_B(r)\}.
\tag{6}
\]

Thus

\[
|\Omega_B|=\sum_{r\in C}\binom{m_B(r)}2.
\tag{7}
\]

Partition a charge \(\omega=(r;a,a')\) according to whether the
reflected position \(t\) in (3) belongs to \(B\), belongs to \(C\), or
is absent from \(S\).

### Bin B: charge to a mixed pair

If \(t\in B\), send

\[
\omega\longmapsto(t,r)\in B\times C,\qquad t<r.
\tag{8}
\]

This map is injective.  The image determines
\(\delta=r-t\); since \(B\) is Golomb, \(\delta\) determines the unique
ordered \(B\)-pair \(a<a'\) with \(a'-a=\delta\).  It then determines
the original charge.

### Bin C: charge to a shared positive length

If \(t\in C\), then

\[
r-t=\delta=a'-a
\tag{9}
\]

is represented once in \(B\) and once in \(C\).  Send the charge to
\(\delta\in\Delta B\cap\Delta C\).  This map is injective because
Golombness of both classes recovers the two ordered pairs
\((a,a')\) and \((t,r)\).

### Hole bin

Let

\[
\mathcal H=([0,L]\cap\mathbb Z)\setminus S.
\tag{10}
\]

If \(t\in\mathcal H\), send

\[
\omega\longmapsto(t,r),\qquad t<r,\quad r\in C.
\tag{11}
\]

This map is injective for the same reason as (8): the pair gives
\(\delta=r-t\), and Golombness of \(B\) gives the unique anchors
\(a<a'\).

The three image classes are disjoint.  Define their exact capacities

\[
M_{BC}^{<}=|\{(t,r)\in B\times C:t<r\}|,
\tag{12}
\]

\[
R=|\Delta B\cap\Delta C|,
\tag{13}
\]

and

\[
H_C^{<}=|\{(t,r)\in\mathcal H\times C:t<r\}|.
\tag{14}
\]

The three injections prove the second-moment inequality

\[
\boxed{
\sum_{r\in C}\binom{m_B(r)}2
\le M_{BC}^{<}+R+H_C^{<}.
}
\tag{15}
\]

This is not based on disjointness of the missing positions themselves.
A single hole may appear with many outputs, but the ordered
hole-output pairs in (14) remain distinct.

## 2. The symmetric two-color inequality

Define \(\mathcal A_C(r)\) and \(m_C(r)\) for \(r\in B\) by exchanging
\(B\) and \(C\).  The same proof gives

\[
\sum_{r\in B}\binom{m_C(r)}2
\le M_{CB}^{<}+R+H_B^{<},
\tag{16}
\]

where

\[
M_{CB}^{<}=|\{(t,r)\in C\times B:t<r\}|,
\qquad
H_B^{<}=|\{(t,r)\in\mathcal H\times B:t<r\}|.
\]

Every mixed \(B\)-\(C\) pair occurs in exactly one of the two
orientations, so

\[
M_{BC}^{<}+M_{CB}^{<}=bc.
\tag{17}
\]

Also put

\[
H^+=H_B^{<}+H_C^{<}
=\sum_{t\in\mathcal H}|S\cap(t,L]|.
\tag{18}
\]

Adding (15) and (16) yields

\[
\boxed{
\sum_{r\in C}\binom{m_B(r)}2
+\sum_{r\in B}\binom{m_C(r)}2
\le bc+2R+H^+.
}
\tag{19}
\]

The hole term retains its position.  The coarse consequence

\[
H^+\le |\mathcal H|(b+c)
=\bigl(L+1-b-c\bigr)(b+c)
\tag{20}
\]

is available but can lose most of the information in (18).

## 3. Span and unused-length form

Let

\[
U=L-|\Delta B\cup\Delta C|
\tag{21}
\]

be the number of positive lengths used by neither diagonal class.
Golombness and inclusion-exclusion give

\[
R=\binom b2+\binom c2-L+U.
\tag{22}
\]

Therefore (19) has the equivalent finite-span form

\[
\boxed{
\sum_{r\in C}\binom{m_B(r)}2
+\sum_{r\in B}\binom{m_C(r)}2
\le
bc+2\binom b2+2\binom c2-2L+2U+H^+.
}
\tag{23}
\]

For example, for any integer \(k\ge2\), (15) immediately bounds the
number of opposite-color outputs with at least \(k\) supported anchors:

\[
|\{r\in C:m_B(r)\ge k\}|
\le
\frac{M_{BC}^{<}+R+H_C^{<}}{\binom k2},
\tag{24}
\]

with the color-reversed analogue.  This permits the known sharp large
multiplicity at an individual output; it charges its quadratic anchor
pairs to finite global resources.

## 4. Why this is genuinely cross-anchor, and the remaining term

An incidence \(a\in\mathcal A_B(r)\) is a supported reflection of one
same-color triple.  Inequality (15) begins only after two different
anchors hit the same output.  Their two already forced cells
\((r,a),(r,a')\) create the additional corner (5).  The reflected
position \(t\), together with Golomb uniqueness of the anchor pair,
makes the three charge maps injective.

The resulting estimate is quantitative but does not prove a uniform
weak-source capacity bound.  In a sparse source, \(H^+\) can have order
\(|\mathcal H||S|\).  Even with no holes, the mixed-pair term \(bc\)
and the two copies of the shared-length term \(R\) can be quadratic in
the class sizes.  Improving (19) would require a further restriction on
which charged mixed pairs \((t,r)\) can coexist with the forced color
\(z(t,a)=C\), or a new way to amortize the ordered hole-output pairs.
No constant output multiplicity or disjoint-hole assumption is used.

## Successor

NESTED_REFLECTION_HOLE_BUDGET_0041.md strengthens this packing after
using the nesting of the reflection witnesses.  For two common anchors
\(a<a'\) at \(r\), the smaller step \(r-a'\) is automatically in
\(\Delta P_a\); the cross-anchor exclusion therefore forces the
reflected position to be a genuine source hole.  Consequently the two
occupied bins used above are empty in this setting, and the successor
note gives the sharper lower- and upper-hole budget.
