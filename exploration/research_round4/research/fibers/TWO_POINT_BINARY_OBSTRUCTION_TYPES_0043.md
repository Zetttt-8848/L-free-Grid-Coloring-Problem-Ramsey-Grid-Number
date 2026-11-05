# Complete binary obstruction types for two opposite marks

Let \(B\) be Golomb and let the opposite diagonal class consist of two
marks. Translate them to

\[
 C=\{0,d\},\qquad d>0,                                \tag{1}
\]

with \(B\cap C=\varnothing\). Write

\[
 \rho_x=X_{0,x},\qquad \sigma_x=X_{d,x}.
\]

The fixed \(C\)-to-\(C\) cell \((d,0)\), of color \(B\), produces the
matching \(G_B\). The B-parent binary graph \(G_C\) is the disjoint union
of the \(0\)-column forest \(F_0\) and the \(d\)-column forest \(F_d\).
As in the transversal reduction, an endpoint forced to color \(B\) is
unavailable for the \(C\)-colored transversal.

## 1. Complete matching inventory

There are only the following matching edges.

* If \(-d\in B\), the lower exterior edge is

  \[
  L=\{\rho_{-d},\sigma_{-d}\}.
  \]

* If \(2d\in B\), the upper exterior edge is

  \[
  U=\{\rho_{2d},\sigma_{2d}\}.
  \]

* If \(p<q\) lie in \(B\cap(0,d)\) and \(p+q=d\), the two interior
  edges are

  \[
  I=\{\rho_q,\sigma_p\},\qquad
  J=\{\rho_p,\sigma_q\}.                              \tag{2}
  \]

* If \(p=q=d/2\in B\), there is one midpoint edge

  \[
  K=\{\rho_p,\sigma_p\}.
  \]

The interior unordered pair is unique. Moreover, \(L\) and \(U\) cannot
both coexist with an interior edge, because

\[
 (-d)+2d=d=p+q
\]

would give two unordered \(B\)-pairs of one sum. Therefore

\[
 |E(G_B)|\le3.                                       \tag{3}
\]

## 2. Exact parent witnesses

For two \(B\)-marks \(x,y\) on the same side of \(0\), let \(f\) be the
one farther from \(0\) and \(n\) the nearer. Then

\[
 \rho_x\rho_y\in E(F_0)
 \quad\Longleftrightarrow\quad
 f-n\in B.                                           \tag{4}
\]

For two marks on the same side of \(d\), with \(f\) farther from \(d\)
and \(n\) nearer,

\[
 \sigma_x\sigma_y\in E(F_d)
 \quad\Longleftrightarrow\quad
 d+f-n\in B.                                         \tag{5}
\]

These are the literal B-parent witnesses. For example, when
\(0<x<y\), equation (4) uses the fixed \(B\)-cell
\((y,y-x)\); the corner is

\[
 (x,0),\quad(y,0),\quad(y,y-x).
\]

The remaining orientations follow by reflecting the line.

Apply (4)--(5) to the inventory above. The complete possible
adjacencies are:

\[
\begin{array}{c|c|c}
\text{candidate pair}&F_0\text{ witness}&F_d\text{ witness}\\ \hline
I,J&q-p\in B&2p\in B\\
U,I&d+p\in B&\text{impossible: }U\text{ is right of }d\\
U,J&d+q\in B&\text{impossible: }U\text{ is right of }d\\
L,I&\text{impossible: }L\text{ is left of }0&-p\in B\\
L,J&\text{impossible: }L\text{ is left of }0&-q\in B.
\end{array}                                           \tag{6}
\]

For a midpoint, the corresponding exterior witnesses are
\(3d/2\in B\) for \(U,K\) in \(F_0\), and
\(-d/2\in B\) for \(L,K\) in \(F_d\).

The table has four useful Golomb restrictions.

1. Both \(I,J\) adjacencies can occur, one in each forest, only when
   \(q=2p\). Indeed, their witnesses satisfy

   \[
   (q-p)+2p=p+q=d.
   \]

   Pair-sum uniqueness forces
   \(\{q-p,2p\}=\{p,q\}\), hence \(q=2p\).

2. At most one of \(U,I\) and \(U,J\) is an \(F_0\)-edge. Their two
   witnesses \(d+p,d+q\) would repeat the difference \(q-p\).
   Reflectively, at most one of \(L,I\), \(L,J\) is an \(F_d\)-edge.

3. If \(I,J\) is an \(F_d\)-edge, neither \(U,I\) nor \(U,J\) can be an
   \(F_0\)-edge. For instance, the witnesses \(2p,d+p\), together with
   \(2d\), give two representations of \(d-p=q\); the other case repeats
   the difference \(p\).

4. If \(I,J\) is an \(F_0\)-edge, neither \(L,I\) nor \(L,J\) can be an
   \(F_d\)-edge. With witnesses \(q-p,-p\), the pairs
   \((-d,-p)\) and \((-p,q-p)\) both have difference \(q\); the
   \(-q\) case similarly repeats \(p\).

Consequently an \(F_0\)-edge and an \(F_d\)-edge on different matching
index pairs never form an alternating path. The only pair that may carry
both kinds is the same interior pair \(I,J\), in the special ratio
\(q=2p\). This is the complete adjacency-pattern restriction on the at
most three matching choices.

## 3. Why at most two unit seeds suffice

With no units, the binary transversal system is satisfiable because the
matching has size at most three. Add the unit forces as unavailable
matching endpoints. If the resulting implication closure is
inconsistent, it contains some choice and its negation. Trace the two
implication paths backward to their initial unit occurrences. At most two
unit occurrences are needed: they are either the same matching choice
forced both ways, one seed whose closure reaches both choices, or two
seeds whose closures collide.

The adjacency restrictions above rule out a one-seed alternating cycle
and every alternating path using two distinct parent edges. Therefore a
binary failure has one of only two logical forms:

* both endpoints of one \(G_B\)-edge are B-units;
* opposite endpoints on two matching edges are B-units, while the two
  remaining endpoints are joined by one edge of \(F_0\) or \(F_d\).

There is no genuinely longer third type in the two-point integer geometry.
It remains to identify when the second logical form is arithmetically
possible.

## 4. Interior-to-interior collisions are impossible

Suppose \(I,J\) is an \(F_0\)-edge, so \(q-p\in B\). The unique
\(B\)-representation of the difference \(p=d-q\) is then

\[
 q-(q-p)=p,
\]

and its lower endpoint lies below \(q\). For \(\sigma_q\) to be a B-unit,
\(q\) would have to be the lower extreme of a reflection at \(d\), requiring
the unique representation of \(d-q=p\) to lie entirely above \(q\).
This is impossible. Hence the two opposite endpoints \(\sigma_p,\sigma_q\)
cannot both be units.

Reflectively, if \(I,J\) is an \(F_d\)-edge, its witness \(2p\in B\)
makes \((p,2p)\) the unique representation of the difference \(p\).
That representation does not lie entirely below \(p\), so \(\rho_p\)
cannot be an upper reflection unit at output \(0\). Again, the two
opposite endpoints cannot both be units.

Thus no parent edge between the two interior matching choices can support
the second obstruction type.

## 5. Exterior-to-interior edges are exactly the longer obstruction

Suppose \(U\) occurs and one interior edge has the form

\[
 E_x=\{\rho_y,\sigma_x\},
 \qquad x+y=d.                                       \tag{7}
\]

By (6), \(U,E_x\) is an \(F_0\)-edge exactly when

\[
 d+x\in B.                                           \tag{8}
\]

But then

\[
 (x,d+x,2d)
\]

is a \(B\)-reflection triple with output \(d\). Its two extreme units are

\[
 \sigma_x=\sigma_{2d}=B.                             \tag{9}
\]

The matching edges \(E_x,U\) force
\(\rho_y=\rho_{2d}=C\), while their \(F_0\)-edge, witnessed by the fixed
\(B\)-cell \((2d,d+x)\) of color \(C\), forbids both values. Hence every
such exterior-to-interior parent edge is already a binary obstruction.

Its complete forced core is

\[
 B\supseteq\{x,d-x,d+x,2d\},\qquad C=\{0,d\}.         \tag{10}
\]

Here the general parent witness is the displayed mark \(d+x\), so the
parameter must be retained in its actual range \(0<x<d\); replacing \(x\)
by \(d-x\) changes that witness and need not preserve the core. As a concrete
Golomb subfamily one may impose \(0<x<d/2\) and
\(x\ne d/4,d/3\). For example \(d=7,x=2\) gives
\(B=\{2,5,9,14\}\). The midpoint version \(x=d/2\) is also valid when
integral, with the three distinct \(B\)-marks

\[
 \{d/2,3d/2,2d\}.
\]

The reflected lower obstruction occurs exactly when \(L\) and \(E_x\)
are joined in \(F_d\), equivalently when \(-x\in B\). Its reflection
triple is

\[
 (-d,-x,d-x),
\]

with output \(0\), and its forced core is

\[
 B\supseteq\{-d,-x,x,d-x\}.                          \tag{11}
\]

It forces the two \(\rho\)-endpoints on \(L,E_x\) to color \(B\), after
which the matching edges and their \(F_d\)-edge give the mirrored
monochromatic corner.

## 6. Complete binary characterization

The prescribed two-point diagonal coloring satisfies all unit and binary
corners if and only if both conditions hold:

1. no matching edge has both endpoints among the reflection units;
2. no exterior matching edge is parent-adjacent to an interior matching
   edge in the only forest where they lie on the same side of its anchor.

Condition 2 is equivalently the absence of the upper core (10) and lower
core (11), including their midpoint forms. Necessity was proved in
Section 5. For sufficiency, Sections 2--4 show that the implication system
has no alternating chain on distinct parent edges, that an
interior-to-interior parent edge cannot have both opposite endpoints forced,
and that every remaining direct forced collision is one of (10)--(11).
The unit-free residual system has at most three matching choices and is
satisfiable.

This theorem classifies the binary subsystem only. The sole ternary
all-mixed corner, when \(d\in\Delta B\), still requires the separate
one-vertex augmentation condition from the two-point transversal theorem.
No global source-capacity estimate is inferred.
