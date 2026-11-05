# The seven-rainbow target on the strict twelve-triangle

This is a bounded direct attack on
\[
R(T_{12})\ge 7. \tag{T12-7}
\]
It does not prove the assertion. It gives two exact reductions preserving
directed equal-step corners and isolates the remaining finite compatibility
gap. One bounded search for a coloring with at most six rainbows ended
undecided; no negative computation is used below.

## 1. Exact line-square target

Use
\[
S_{10}=\{(x,y):x,y\ge0,\ x+y\le10\}.
\]
A corner is
\[
(x,y),\quad(x+d,y),\quad(x,y+d),
\qquad d>0,\qquad x+y+d\le10.                    \tag{1}
\]
Let \(n_{\ell,i}\) count color \(i\) on a horizontal, vertical, or
slope-minus-one line \(\ell\), and set
\[
Q(F)=\sum_{\ell}\sum_{i=0}^2n_{\ell,i}^2.        \tag{2}
\]
There is one line of each length \(1,\ldots,11\) in each direction, so
\[
\sum_{\ell}\frac{|\ell|^2}{3}=\sum_{j=1}^{11}j^2=506. \tag{3}
\]
Thus the discrepancy from TRIANGLE_RAINBOW_ENERGY.md is \(V=Q-506\).
Its proper three-color identity \(V+2R=132\) becomes
\[
Q(F)+2R(F)=638.                                  \tag{4}
\]
Therefore (T12-7) is exactly
\[
Q(F)\le624.                                      \tag{5}
\]
A putative \(R\le6\) coloring has \(Q\ge626\). Only two units of
discrepancy separate the desired result from \(R=6\), so independent
rounding of line estimates is too lossy unless equality is also classified.

## 2. Monochromatic line subsets give actual two-color sources

**Line-source lemma.** Let \(X\) be the positions occupied by one fixed
color on one line of a proper coloring of \(S_{10}\). The completion cells
of pairs from \(X\) use only the other two colors, and their induced coloring
is a proper strict source triangle \(V(X)\).

For a horizontal line \(y=y_0\), parameterized by \(x\), define for
\(u<v\) in \(X\)
\[
\Phi(v,u)=(u,y_0+v-u).                           \tag{6}
\]
This is the completion of the equal-colored cells at \(u,v\), hence it
does not have their color. A source corner
\[
(v,u),\quad(v+d,u),\quad(v+d,u+d)
\]
is mapped to
\[
(u,y_0+v-u),\quad
(u,y_0+v+d-u),\quad
(u+d,y_0+v-u),                                  \tag{7}
\]
an ambient directed corner of step \(d\), with the final two cells
interchanged. All images lie in \(S_{10}\) because \(y_0+v\le10\).
Ambient properness proves the claim.

The vertical case follows by interchanging \(x,y\). On the diagonal
\(x+y=t\), parameterized by \(x\), use
\[
\Phi(v,u)=(u,t-v).                               \tag{8}
\]
Substitution again maps each source corner to an ambient corner. This proves
the lemma in all three directions.

Hence (5) is a joint statement about 99 position sets: each color subset of
each of the 33 lines supplies a proper two-color source by (6) or (8), and
all these source colorings reuse the same ambient cells. A bound using only
the 99 cardinalities discards the completion colors that couple distinct
lines. The missing quantitative step is to use this shared-cell compatibility
to prove (5).

## 3. Three overlapping \(T_{11}\) faces

Give the corner (1) its gap coordinates
\[
(x,y,s),\qquad s=10-x-y-d.                       \tag{9}
\]
The three unit translates of \(S_9\) inside \(S_{10}\) contain this corner
respectively when
\[
x\ge1,\qquad y\ge1,\qquad s\ge1.                 \tag{10}
\]
Let \(R_x,R_y,R_s\) be their rainbow counts. For a rainbow corner \(e\)
put
\[
b(e)={\mathbf 1}_{x=0}+{\mathbf 1}_{y=0}
     +{\mathbf 1}_{s=0},
\qquad
D=\sum_{e\ {\rm rainbow}}b(e).                   \tag{11}
\]
Counting incidences with the three faces gives
\[
R_x+R_y+R_s=3R-D,
\qquad
3R=R_x+R_y+R_s+D.                                \tag{12}
\]
Thus (T12-7) is equivalently
\[
R_x+R_y+R_s+D\ge21.                              \tag{13}
\]
This retains exactly how many barycentric boundary faces each rainbow misses.

## 4. Complete form of a small-rainbow exception

Suppose \(R\le6\). If some \(R_x,R_y,R_s\le4\), the coloring already
contains a proper \(T_{11}\) with at most four rainbows. Otherwise all three
face counts are at least five. Since a face rainbow is also a full-triangle
rainbow, (12) leaves only these cases, up to permuting the faces:

| \(R\) | \(D\) | \(\{R_x,R_y,R_s\}\) |
|---:|---:|:---|
|5|0|\(\{5,5,5\}\)|
|6|0|\(\{6,6,6\}\)|
|6|1|\(\{5,6,6\}\)|
|6|2|\(\{5,5,6\}\)|
|6|3|\(\{5,5,5\}\)|

Indeed, every face count is between five and \(R\), and their sum is
\(3R-D\). In particular \(R\le4\) necessarily produces a
four-rainbow-or-less \(T_{11}\) face.

Consequently the following two statements together would prove (T12-7):

1. every proper \(T_{11}\) has at least five rainbows;
2. under that premise,
   \[
   D+\sum_{j\in\{x,y,s\}}(R_j-5)\ge6.             \tag{14}
   \]

Equation (14) excludes exactly the five tight patterns above. Neither
statement is established here. The known five-rainbow \(T_{11}\) coloring
shows that the first constant would be sharp.

## 5. Precise remaining gap

The bounded attempt reduces the problem to the joint line-square inequality
(5), equivalently the face inequality (13). If the sharp \(T_{11}\) premise
is proved separately, it is enough to exclude the five boundary patterns or
prove (14).

The corner-sum variables \(g_d=D_dF\) from CORNER_SUM_COORDINATES.md express
the missing shared-cell compatibility through
\[
D_e g_d=D_d g_e.
\]
Treating the line-source systems independently omits these equations.
Treating only zero positions of the \(g_d\) omits the condition that a
zero-sum corner is rainbow rather than monochromatic. Both pieces are needed
for (5).

For discovery only, all original corners (1) were encoded, all monochromatic
triples were forbidden, and at most six rainbow indicators were allowed. A
60-second Glucose4 run ended interrupted/undecided and produced no coloring.
This is neither evidence for (T12-7) nor a finite exclusion. The mathematical
output of this attempt is the line-source lemma, identities (4) and (12), and
the five-case structural gap above.
