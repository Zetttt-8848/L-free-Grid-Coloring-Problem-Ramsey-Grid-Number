# Two-point weak extension as a four-edge forest transversal

Let \(B\) be Golomb and let \(C=\{r,s\}\), \(r<s\), be disjoint from
\(B\). Prescribe diagonal color \(B\) on \(B\) and color \(C\) on \(r,s\).
Use the unit set \(\mathcal U\), the binary graphs \(G_B,G_C\), and the sole
possible ternary corner \(T\) from the repaired two-point reduction.

The fixed cell \((s,r)\) gives pairwise disjoint edges in
\(G_B\): one from a mark below \(r\), one from a mark above \(s\), and two
from the unique distinct interior pair \(p<q\) with \(p+q=r+s\). In the
midpoint case \(p=q\), the two interior edges coincide.

There cannot simultaneously be two exterior marks and an interior pair.
Indeed,

\[
 (2r-s)+(2s-r)=r+s,
\]

so an interior representation \(p+q=r+s\), including \(p=q\), would give
two distinct unordered \(B\)-pairs of one sum. Golombness forbids this.
Consequently

\[
 \boxed{G_B\text{ is a matching of size }m\le3.}       \tag{1}
\]

Every edge has one endpoint in the \(r\)-column and one in the \(s\)-column.
Write it as

\[
 e_i=\{\rho_i,\sigma_i\},
 \qquad
 \rho_i=X_{r,b_i},\quad \sigma_i=X_{s,b_i'},
 \qquad 1\le i\le m.                                  \tag{2}
\]

## 1. The two inherited forests

All edges of \(G_C\) come from a fixed \(B\)-to-\(B\) cell and two mixed
variables. Such an edge keeps the opposite-class endpoint fixed. Therefore

\[
 G_C=F_r\sqcup F_s,                                   \tag{3}
\]

where \(F_r\) is the B-parent forest on the variables \(X_{r,b}\), and
\(F_s\) is the corresponding forest on the variables \(X_{s,b}\). Parent
edges strictly enlarge the interval from \(r\), respectively from \(s\).

Restrict these forests to the matching endpoints. Define two graphs on the
index set \([m]\):

\[
 ij\in R\iff \rho_i\rho_j\in E(F_r),
 \qquad
 ij\in S\iff \sigma_i\sigma_j\in E(F_s).              \tag{4}
\]

Both \(R\) and \(S\) are forests.

For each matching edge it is enough to choose exactly one endpoint to receive
color \(C\). Indeed, any independent set meeting every \(G_B\)-edge can be
reduced to one endpoint per edge; deleting \(C\)-vertices preserves
\(G_C\)-independence and avoids all units. Let

\[
 z_i=0\quad\Longleftrightarrow\quad \rho_i\text{ is chosen},
 \qquad
 z_i=1\quad\Longleftrightarrow\quad \sigma_i\text{ is chosen}. \tag{5}
\]

The complete binary problem on the matching endpoints is then

\[
\begin{array}{rll}
ij\in R&\Longrightarrow& z_i\lor z_j,\\
ij\in S&\Longrightarrow& \neg z_i\lor\neg z_j,\\
\rho_i\in\mathcal U&\Longrightarrow&z_i=1,\\
\sigma_i\in\mathcal U&\Longrightarrow&z_i=0.
\end{array}                                           \tag{6}
\]

If both endpoints of one \(e_i\) lie in \(\mathcal U\), (6) is immediately
inconsistent. Conversely, every solution of (6) selects a non-unit endpoint
of each \(G_B\)-edge and those selected endpoints form an independent set in
\(G_C\). Coloring them \(C\) and all other mixed variables \(B\) satisfies
every unit and binary corner. Thus (6) is an exact binary extension theorem,
not merely a necessary condition.

It is also a literal integer-geometric reduction: the clauses in \(R,S\)
are precisely the parent-child relations in the two interval forests, and
there are at most three Boolean variables.

## 2. Unit-free extension and the excluded four-edge obstruction

There is a useful closed classification when no matching endpoint is a unit.

**Lemma.** Let \(R,S\) be forests on a set of at most four indices. There is
an assignment satisfying the first two lines of (6), except in the following
case. There are four indices \(a,u,v,b\) for which

\[
 R=\{au,uv,vb\},
 \qquad
 S=\{av,uv,ub\},                                     \tag{7}
\]

after possibly exchanging \(R,S\). In words, both are four-vertex paths,
they share their central edge \(uv\), and their two leaf attachments are
crossed.

**Proof.** An assignment is the same as a set

\[
 I=\{i:z_i=0\}
\]

that is independent in \(R\) and meets every edge of \(S\). Equivalently,
\(I\) is an \(R\)-independent vertex cover of \(S\).

If \(S\) has at most two adjacent edges, their common vertex covers all of
them and is independent in \(R\). If its at most two edges are disjoint,
choose one endpoint of each. All four cross choices could fail to be
independent in \(R\) only if \(R\) contained the full \(K_{2,2}\), impossible
for a forest. If \(S\) has three edges and is a star, its center is again a
one-vertex cover. Hence a failure requires \(S\) to be a three-edge spanning
tree with no one-vertex cover, so \(S\) is a four-vertex path. By the
symmetric argument, \(R\) is also a four-vertex path.

Write \(R=a-u-v-b\). Its three minimal vertex covers are

\[
 \{u,v\},\qquad\{a,v\},\qquad\{u,b\}.                 \tag{8}
\]

For none to be independent in \(S\), the forest \(S\), which has exactly
three edges, must contain respectively

\[
 uv,\qquad av,\qquad ub.
\]

This is exactly the crossed path in (7). Conversely, those three edges of
\(S\) meet every cover in (8), so no \(R\)-independent cover exists.
\(\square\)

The obstruction is transparent at the color level. The shared edge \(uv\)
forces \(z_u\ne z_v\). If \(z_u=0,z_v=1\), the \(R\)-edge \(au\) and the
\(S\)-edge \(av\) force contradictory colors at \(a\). If
\(z_u=1,z_v=0\), the edges \(vb\in R\) and \(ub\in S\) force contradictory
colors at \(b\).

The arithmetic bound \(m\le3\) excludes (7). Consequently:

\[
\boxed{\text{If no endpoint of }G_B\text{ is a unit, the binary system
always extends.}}                                    \tag{8a}
\]

The crossed-\(P_4\) is the sole abstract unit-free obstruction at four
matching edges, but pair-sum uniqueness prevents the two-point integer
geometry from ever reaching four edges.

With units present, (6) remains the complete finite characterization. A
failure may be smaller: forced choices can put both selected endpoints on
one parent edge. Equivalently, after unit clauses are included, the directed
implication graph of the at most three variables in (6) has a literal and its
negation in one strongly connected component. This is the exact remaining
finite unit-transversal configuration after the immediate two-unit edge
obstruction is removed.

## 3. A genuine longer unit-implication obstruction

A matching edge with two unit endpoints is not the only integer-geometric
unit obstruction. Fix integers \(d,p\) with

\[
 0<p<\frac d2,\qquad p\ne\frac d4,\qquad p\ne\frac d3,
\]

and put

\[
 C=\{0,d\},\qquad
 B=\{p,d-p,d+p,2d\}.                                 \tag{8b}
\]

The four \(B\)-marks are strictly ordered as displayed. Their six positive
differences are

\[
 d-2p,\quad d,\quad2d-p,\quad2p,\quad d+p,\quad d-p.
\]

The stated exclusions make these six values distinct, so \(B\) is Golomb
and is disjoint from \(C\).

The interior pair \(p+(d-p)=d\) supplies the matching edge

\[
 \{X_{0,d-p},X_{d,p}\}.                              \tag{8c}
\]

The upper exterior mark \(2d=2s-r\) supplies

\[
 \{X_{0,2d},X_{d,2d}\}.                              \tag{8d}
\]

Now

\[
 (p,d+p,2d)
\]

is an internal \(B\)-reflection triple with output \(d\), since
\(p+2d-(d+p)=d\). Its two reflection units force

\[
 X_{d,p}=X_{d,2d}=B.                                 \tag{8e}
\]

The edge in (8c) and the edge in (8d), using the fixed \(B\)-colored
\(C\)-to-\(C\) cell \((d,0)\), therefore force

\[
 X_{0,d-p}=X_{0,2d}=C.                               \tag{8f}
\]

But the three physical cells

\[
 (d-p,0),\qquad(2d,0),\qquad(2d,d+p)
\]

form a positive corner of step \(d+p\). Its first two cells are precisely
\(X_{0,d-p},X_{0,2d}\), while \((2d,d+p)\) is a fixed
\(B\)-to-\(B\) cell and therefore also has color \(C\). This is a
monochromatic corner. Every step used here is positive.

Neither matching edge used in (8f) has two unit endpoints: the unit
endpoints are \(X_{d,p}\) and \(X_{d,2d}\), on two different matching
edges. The contradiction is the length-two implication pattern

\[
 X_{d,p}=B
 \Longrightarrow X_{0,d-p}=C
 \mathrel{-_{G_C}}
 X_{0,2d}=C
 \Longleftarrow X_{d,2d}=B.                          \tag{8g}
\]

Thus the answer to the unit question is negative: absence of a
double-unit \(G_B\)-edge does not suffice. A single reflection triple can
place units on two different matching edges, whose opposite endpoints are
joined by one actual B-parent edge.

The construction is binary-obstructed before the possible ternary clause is
used. It is therefore a direct source obstruction, not merely an abstract
transversal pattern. Taking \(d=7,p=2\) gives the concrete ruler
\(B=\{2,5,9,14\}\). The family establishes only this six-mark binary-chain
obstruction, with one reflection event; it is not a source-capacity bound.

## 4. Incorporating the sole ternary corner

Let \(\mathfrak T\) be the family of endpoint sets \(Z_0\) obtained from all
solutions of (6), with exactly one selected endpoint from every nonempty
\(G_B\)-edge. Each \(Z_0\) is disjoint from \(\mathcal U\), independent in
\(G_C\), and meets every edge of \(G_B\).

If the common-difference ternary corner \(T\) is absent, any
\(Z_0\in\mathfrak T\) gives a full weak extension.

Suppose \(T\) exists. For \(Z_0\in\mathfrak T\), define

\[
 A_T(Z_0)
 =T\setminus\bigl(\mathcal U\cup N_{G_C}[Z_0]\bigr),  \tag{9}
\]

where the closed neighborhood includes \(Z_0\) itself. Then the prescribed
diagonal coloring extends if and only if some \(Z_0\in\mathfrak T\) satisfies
one of

\[
 1\le |Z_0\cap T|\le2,                               \tag{10}
\]

or

\[
 Z_0\cap T=\varnothing
 \quad\text{and}\quad
 A_T(Z_0)\ne\varnothing.                             \tag{11}
\]

For (10), use \(Z=Z_0\). For (11), choose \(t\in A_T(Z_0)\) and use
\(Z=Z_0\cup\{t\}\). This remains unit-free and \(G_C\)-independent, still
meets every \(G_B\)-edge, and meets but does not contain the three-set \(T\).

Conversely, start with any full feasible \(C\)-colored set \(Z\). Select one
member of \(Z\) from each \(G_B\)-edge to form \(Z_0\subseteq Z\). If
\(Z_0\) already meets \(T\), it cannot contain all of \(T\), because then
\(Z\) would do so; hence (10) holds. If it misses \(T\), the original set
\(Z\) contains some \(t\in T\), and independence and the unit conditions
place that \(t\) in \(A_T(Z_0)\), giving (11). This proves necessity.

Equations (6) and (9)--(11) are a complete constructive theorem for the
two-point extension problem. The unit-free binary system always extends.
Once a binary transversal is chosen, the ternary corner has the explicit
one-vertex augmentation test (9).
