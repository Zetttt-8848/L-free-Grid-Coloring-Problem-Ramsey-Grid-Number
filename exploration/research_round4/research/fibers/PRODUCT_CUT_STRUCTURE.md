# Product sources and the completion cut budget

Base: R4-RESEARCH-0008. Bounded auxiliary construction analysis integrated
at R4-RESEARCH-0009.

**Status:** proved for the product source below. This note only analyzes that
construction; it does not claim a new Ramsey bound.

## Setup

Let $B,G\subset \mathbb Z$ be finite nonempty Golomb sets, put

\[
S=\max B-\min B,
\qquad H>2S,
\qquad A=B+HG,
\]

and write $m=|B|$, $n=|G|$.  We use the row and column graphs from
`COMPLETION_CUT_BUDGET.md`: the vertices of $R_v$ are the cells
$(v,u)$, $u<v$, and two are adjacent when they occur together in a
corner whose top row is $v$.  The vertices of $C_u$ are the cells
$(v,u)$, $v>u$, and two are adjacent when they occur together in a
corner whose left column is $u$.

Recall the product coloring

\[
\chi(Hg'+b',Hg+b)=1
\quad\Longleftrightarrow\quad
g'>g\ \text{and}\ b'>b.
\tag{1}
\]

All other cells have color $0$.  The product-construction proof shows
that every corner is obtained from a choice $g<g'$ in $G$ and
$b<b'$ in $B$.  If

\[
P=Hg+b,
\quad Q=Hg+b',
\quad R=Hg'+b,
\quad S=Hg'+b',
\]

the two associated corners are

\[
\{(Q,P),(S,P),(S,R)\},
\qquad
\{(R,P),(S,P),(S,Q)\}.
\tag{2}
\]

Both have color pattern $(0,1,0)$, with the shared completion cell
$(S,P)$ having color $1$.

## Exact difference-fiber profile

Let

\[
\Delta^+B=\{b'-b:b,b'\in B, b<b'\},
\qquad
\Delta^+G=\{g'-g:g,g'\in G, g<g'\}.
\]

Every positive difference between two marks of $A$ has the form

\[
d=Hp+q,
\qquad p=g'-g\ge 0,
\qquad q=b'-b,
\tag{3}
\]

where $p=0$ forces $q>0$.  If
$Hp+q=Hp'+q'$, then

\[
H(p-p')=q'-q,
\qquad |q'-q|\le 2S<H,
\]

so $p=p'$ and $q=q'$.  Thus there is no carry or collision between
the two difference digits.  The Golomb property then gives the complete
fiber list:

1. For each $q\in\Delta^+B$, the difference $d=q$ has
   
   \[
   F_q=\{Hg+b:g\in G\},
   \qquad r_q=n,
   \tag{4}
   \]
   
   where $b<b'$ is the unique pair with $b'-b=q$.

2. For each $p\in\Delta^+G$, the difference $d=Hp$ has
   
   \[
   F_{Hp}=\{Hg+b:b\in B\},
   \qquad r_{Hp}=m,
   \tag{5}
   \]
   
   where $g<g'$ is the unique pair with $g'-g=p$.

3. For each $p\in\Delta^+G$ and each nonzero signed difference
   $q\in(B-B)\setminus\{0\}$, the difference $d=Hp+q$ is positive
   and has exactly one representation, hence
   
   \[
   r_{Hp+q}=1.
   \tag{6}
   \]

All other positive fibers are empty.  Consequently there are

\[
\binom m2\text{ fibers of size }n,
\qquad
\binom n2\text{ fibers of size }m,
\qquad
\binom n2m(m-1)\text{ singleton fibers}.
\tag{7}
\]

Only the first two types contain corners, and therefore

\[
T=\sum_d\binom{r_d}{2}
=2\binom m2\binom n2.
\tag{8}
\]

## Exact row graphs

Fix $v=H\gamma+\beta\in A$, and set

\[
p=|\{g\in G:g<\gamma\}|,
\qquad
q=|\{b\in B:b<\beta\}|.
\tag{9}
\]

Identify a vertex $(v,u)$ of $R_v$ with its lower mark $u$.  The
lower marks split into four types:

\[
\begin{array}{lll}
P_{g,b}=Hg+b, & g<\gamma,\ b<\beta, & pq\text{ vertices},\\
X_g=Hg+\beta, & g<\gamma, & p\text{ vertices},\\
Y_b=H\gamma+b, & b<\beta, & q\text{ vertices},\\
I_{g,b}=Hg+b, & g<\gamma,\ b>\beta,
  & p(m-q-1)\text{ vertices}.
\end{array}
\tag{10}
\]

For every $g<\gamma$ and $b<\beta$, formula (2), with $S=v$,
gives exactly the two row edges

\[
P_{g,b}X_g,
\qquad
P_{g,b}Y_b.
\tag{11}
\]

Conversely, every row edge belongs to a corner, and the complete corner
classification (2) forces it to be one of (11).  Thus the $I_{g,b}$
are isolated and there are no further edges.

Let $\operatorname{Sub}(K_{p,q})$ denote the graph obtained by
subdividing every edge of $K_{p,q}$ once.  Its original vertices are
the $X_g,Y_b$, and its subdivision vertex on $X_gY_b$ is
$P_{g,b}$.  Hence

\[
\boxed{
R_{H\gamma+\beta}
\cong
\operatorname{Sub}(K_{p,q})
\sqcup I_{p(m-q-1)}.}
\tag{12}
\]

In particular,

\[
|E(R_{H\gamma+\beta})|=2pq.
\tag{13}
\]

Under (1), every $P_{g,b}$ has color $1$, whereas every $X_g$,
$Y_b$, and isolated vertex has color $0$.  This is an explicit cut
containing every row edge, so

\[
\tau(R_v)=0
\qquad(v\in A).
\tag{14}
\]

## Exact column graphs

Fix $u=Hg+b\in A$, and set

\[
p^+=|\{g'\in G:g'>g\}|,
\qquad
q^+=|\{b'\in B:b'>b\}|,
\qquad
j=|\{b_0\in B:b_0<b\}|.
\tag{15}
\]

Identify a vertex $(v,u)$ of $C_u$ with its upper mark $v$.  Its
vertices split into

\[
\begin{array}{lll}
S_{g',b'}=Hg'+b', & g'>g,\ b'>b, & p^+q^+\text{ vertices},\\
X_{g'}=Hg'+b, & g'>g, & p^+\text{ vertices},\\
Y_{b'}=Hg+b', & b'>b, & q^+\text{ vertices},\\
I_{g',b_0}=Hg'+b_0, & g'>g,\ b_0<b,
  & p^+j\text{ vertices}.
\end{array}
\tag{16}
\]

For every $g'>g$ and $b'>b$, the two corners in (2), now with
$P=u$, give exactly the column edges

\[
S_{g',b'}X_{g'},
\qquad
S_{g',b'}Y_{b'}.
\tag{17}
\]

The corner classification again excludes all further edges.  Therefore

\[
\boxed{
C_{Hg+b}
\cong
\operatorname{Sub}(K_{p^+,q^+})
\sqcup I_{p^+j},}
\tag{18}
\]

and

\[
|E(C_{Hg+b})|=2p^+q^+.
\tag{19}
\]

The subdivision vertices $S_{g',b'}$ have color $1$, while all
boundary and isolated vertices have color $0$.  Hence

\[
\tau(C_u)=0
\qquad(u\in A).
\tag{20}
\]

Summing (13) and (19) also gives the consistency identities

\[
\sum_{v\in A}|E(R_v)|
=\sum_{u\in A}|E(C_u)|
=2\binom m2\binom n2=T.
\tag{21}
\]

## Exact cut-budget slack

Write

\[
\phi(r)=\binom r2-\left\lfloor\frac{r^2}{4}\right\rfloor.
\]

By (7), the diagonal term in the completion cut criterion is

\[
L_D
=\sum_d\phi(r_d)
=\binom m2\phi(n)+\binom n2\phi(m).
\tag{22}
\]

Equations (14) and (20) show that the entire row-column contribution
vanishes.  The slack in

\[
\sum_d\phi(r_d)+\sum_v\tau(R_v)+\sum_u\tau(C_u)\le T
\]

is therefore exactly

\[
\boxed{
T-L_D
=\binom m2\left\lfloor\frac{n^2}{4}\right\rfloor
 +\binom n2\left\lfloor\frac{m^2}{4}\right\rfloor.}
\tag{23}
\]

This gives an explicit family with unbounded cut-budget slack.  When
$m,n\to\infty$, the slack is $\Theta(m^2n^2)$.  For example, if
$m=n=r$, its ratio to $T$ tends to $1/2$.  If a fixed three-mark
Golomb set $B$ is used and $n=|G|\to\infty$, then

\[
T=6\binom n2,
\qquad
T-L_D=3\left\lfloor\frac{n^2}{4}\right\rfloor+2\binom n2,
\tag{24}
\]

whose ratio tends to $7/12$.

For the particular coloring (1), every vertex in every repeated
difference fiber has color $0$, so the actual equal-color diagonal
edge count is all of $T$, while the actual row and column equal-color
edge counts are zero.  The criterion minimizes the three graph families
separately; (23) measures the resulting relaxation gap on this product
source.

## A further consequence for constant spectral bounds

The following root consequence was added at integration. Let Gamma(A)
be the graph containing all three pairs of every source corner, as in
COMPLETION_CUT_BUDGET.md. Choose |B|=2 and |G|=h^2+1, where h is any
positive integer. At the largest source mark, (12) gives a row graph
Sub(K_(h^2,1)). Its single vertex in the second original part and its
h^2 adjacent subdivision vertices induce a star K_(1,h^2).

All selected cells are on one row, so their induced graph in Gamma(A)
is that same star: another pair type cannot create an additional edge
between them. Put value h at its center, value -1 on each of its h^2
leaves, and zero on every other cell. If J is the adjacency matrix of
Gamma(A), this vector x satisfies

    x^T x=2h^2,     x^T Jx=-2h^3.

Hence lambda_min(J)<=-h. These sources all have the proper product
two-coloring. There is consequently no absolute lower bound on their
least adjacency eigenvalues, even after restricting to properly
two-colored sources.

For a proper two-coloring encoded by z in {-1,1}, the corner identity
is z^T Jz=-2T(A) and z^T z=M(A). A constant spectral lower bound
lambda_min(J)>=-2kappa would imply T(A)<=kappa M(A), but the star
construction disproves every such constant spectral premise. This
does not refute an energy bound specific to actual sign assignments;
the vector above has zero entries and a center of magnitude h.

## Scope of the construction

The fiber profile, graph isomorphisms, and slack formula above are proved
only for $A=B+HG$ with $B,G$ Golomb and $H>2\operatorname{span}(B)$.
They show that the row and column graph terms alone do not detect this
corner-free product coloring.  No assertion is made here about general
sumsets or about an upper bound for arbitrary sources.
