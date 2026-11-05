# The seven-rainbow target on the strict twelve-triangle

This note records a bounded direct attack on the local assertion

\[
  R(T_{12})\ge 7
  \tag{T12-7}
\]

for every proper three-coloring.  It does not prove (T12-7).  It gives two
exact reductions that preserve the directed equal-step geometry and isolates
the remaining finite compatibility gap.  A single bounded construction search
for a coloring with at most six rainbows ended undecided; no negative search
outcome is used below.

## 1. The exact line-square target

Use corner-sum coordinates

\[
  S_{10}=\{(x,y):x,y\ge0,\ x+y\le10\}.
\]

A corner is

\[
  (x,y),\quad (x+d,y),\quad (x,y+d),
  \qquad d>0,quad x+y+d\le10.                 \tag{1}
\]

Let \(n_{\ell,i}\) be the number of cells of color \(i\) on a horizontal,
vertical, or slope-minus-one line \(\ell\), and put

\[
  Q(F)=\sum_{\ell}\sum_{i=0}^2 n_{\ell,i}^2.  \tag{2}
\]

There is one line of each length \(1,\ldots,11\) in each of the three
directions.  Hence

\[
 \sum_{\ell}\frac{|\ell|^2}{3}
 =\sum_{j=1}^{11}j^2=506.                       \tag{3}
\]

The line discrepancy in `TRIANGLE_RAINBOW_ENERGY.md` is therefore

\[
  V(F)=Q(F)-506.
\]

For a proper three-coloring the exact identity \(V+2R=132\) gives

\[
  Q(F)+2R(F)=638.                                \tag{4}
\]

Consequently (T12-7) is exactly the position-sensitive inequality

\[
  Q(F)\le624.                                    \tag{5}
\]

A putative counterexample with \(R\le6\) has \(Q\ge626\).  Thus only two
units of line discrepancy separate the desired statement from the case
\(R=6\); an estimate that rounds individual lines independently is unlikely
to retain enough information.

## 2. Every monochromatic line subset supplies an actual two-color source

The following observation is valid for all three line directions and retains
the positions of the cells.

**Line-source lemma.**  Let \(X\) be the set of positions occupied by one
fixed color on one line of a proper coloring of \(S_{10}\).  The completion
cells of the pairs from \(X\) carry only the other two colors, and their
induced coloring is a proper strict source triangle \(V(X)\).

For example, on the horizontal line \(y=y_0\), write a cell position as its
\(x\)-coordinate.  For \(u<v\) in \(X\), the completion of the equal-colored
pair is

\[
  \Phi(v,u)=(u,y_0+v-u).                         \tag{6}
\]

It is not in the fixed color, by the corner with the two cells
\((u,y_0),(v,y_0)\).  Moreover a source corner

\[
 (v,u),\quad(v+d,u),\quad(v+d,u+d)
\]
is sent by (6) to

\[
 (u,y_0+v-u),\quad
 (u,y_0+v+d-u),\quad
 (u+d,y_0+v-u),                                  \tag{7}
\]

which is precisely a directed corner of step \(d\), with its last two cells
interchanged.  It lies in \(S_{10}\) because \(y_0+v\le10\).  Ambient
properness proves properness of the two-color source.

The vertical case is obtained by interchanging \(x,y\).  On the diagonal
\(x+y=t\), parameterize a cell by \(x\).  The corresponding completion map is

\[
  \Phi(v,u)=(u,t-v),                              \tag{8}
\]

and the same substitution sends every source corner to an ambient corner.
This proves the lemma in all directions.

Thus (5) can be restated without losing arithmetic information: for each of
the 33 lines and each color, its actual position set must admit the induced
proper two-color source supplied by (6) or (8), and all 99 induced source
colorings use the same ambient cells.  The unresolved step is to exploit that
shared-cell compatibility to prove the joint square bound (5).  Bounds based
only on the cardinalities \(|X|\) discard precisely the completion colors
that couple different lines.

## 3. Three overlapping \(T_{11}\) faces

There is a second exact reduction.  Give a corner (1) its three nonnegative
gap coordinates

\[
  (x,y,s),\qquad s=10-x-y-d.                     \tag{9}
\]

The three unit translates of \(S_9\) inside \(S_{10}\) are obtained by
requiring respectively \(x\ge1\), \(y\ge1\), or the third barycentric
coordinate to be at least one.  A corner belongs to these three copies of
\(T_{11}\) respectively when

\[
  x\ge1,\qquad y\ge1,\qquad s\ge1.               \tag{10}
\]

Let \(R_x,R_y,R_s\) be the rainbow counts in the three restrictions, and for
a rainbow corner \(e\) define its boundary defect

\[
 b(e)={\bf1}_{x=0}+{\bf1}_{y=0}+{\bf1}_{s=0},
 \qquad D=\sum_{e\ {
m rainbow}}b(e).            \tag{11}
\]

Counting incidences of rainbow corners with the three faces gives the exact
identity

\[
  R_x+R_y+R_s=3R-D,
  \qquad
  3R=R_x+R_y+R_s+D.                              \tag{12}
\]

In particular, (T12-7) is equivalent to

\[
  R_x+R_y+R_s+D\ge21.                            \tag{13}
\]

This is stronger information than merely restricting to one consecutive
\(T_{11}\): it charges a rainbow according to exactly how many of the three
barycentric boundary faces it misses.

## 4. Complete form of any small-rainbow exception

Identity (12) gives a short exhaustive alternative.  Suppose \(R\le6\).
If one of \(R_x,R_y,R_s\) is at most four, the coloring already contains a
proper \(T_{11}\) with at most four rainbows.  Otherwise all three face counts
are at least five.  Since each face rainbow is also a rainbow of the full
triangle, (12) leaves only the following cases, up to permuting the faces:

| full count \(R\) | defect \(D\) | face counts \(\{R_x,R_y,R_s\}\) |
|---:|---:|:---|
|5|0|\(\{5,5,5\}\)|
|6|0|\(\{6,6,6\}\)|
|6|1|\(\{5,6,6\}\)|
|6|2|\(\{5,5,6\}\)|
|6|3|\(\{5,5,5\}\)|

Indeed, all face counts lie between five and \(R\), and their sum is
\(3R-D\).  This also shows that \(R\le4\) necessarily yields a
four-rainbow-or-less \(T_{11}\) face.

Consequently a two-part route would suffice:

1. prove that every proper \(T_{11}\) has at least five rainbows; and
2. under that premise prove the boundary-excess inequality
   \[
     D+\sum_{j\in\{x,y,s\}}(R_j-5)\ge6.           \tag{14}
   \]

Equation (14) excludes exactly the five tight patterns in the table.  Neither
part is proved here.  The existing five-rainbow \(T_{11}\) coloring shows that
the constant in the first part would be sharp.

## 5. Exact remaining gap and bounded discovery status

The useful unresolved implication is now narrow:

> Prove the joint line-square bound (5), using the common ambient colors in
> the 99 line-source systems of Section 2; equivalently, prove that every
> proper coloring satisfies (13).  If the sharp \(T_{11}\) lower bound is
> established separately, it is enough to exclude the five boundary patterns
> in Section 4, or to prove (14) directly.

The corner-sum variables \(g_d=D_dF\) from
`CORNER_SUM_COORDINATES.md` express the same missing compatibility through
\(D_e g_d=D_d g_e\).  Treating the line-source systems independently omits
these shared-cell equations; treating only the zero positions of the \(g_d\)
omits the requirement that a zero-sum corner be rainbow rather than
monochromatic.  Both pieces must be retained in a proof of (5).

For discovery only, the original directed corners (1) were encoded with all
monochromatic triples forbidden and at most six rainbow indicators.  A
60-second Glucose4 run returned interrupted/undecided and produced no
coloring.  This is neither evidence for (T12-7) nor a finite exclusion.  The
complete mathematical output of the bounded attempt is therefore the
line-source lemma, identities (4) and (12), and the five-case structural gap
above.
