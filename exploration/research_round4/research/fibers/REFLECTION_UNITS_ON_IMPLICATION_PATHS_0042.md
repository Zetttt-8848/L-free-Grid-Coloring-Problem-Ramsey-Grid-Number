# Reflection units can be consecutive on an implication path

Let (S=B\sqcup C) be a proper weak source with the prescribed
diagonal colors named (B) and (C).  I use the actual-color successor
map from `MIXED_INTERVAL_FORESTS_0042.md`: a (B)-colored mixed vertex
follows its (C)-parent, and a (C)-colored mixed vertex follows its
(B)-parent.  This note gives an explicit proper family in which two
reflection units are consecutive on one such path.  Their lengths can
have ratio arbitrarily close to one, so neither antichainhood nor a
fixed multiplicative separation of unit vertices is available.

## 1. General path bookkeeping

Write a forward path as

\[
 v_i=(b_i,c_i),\qquad w_i=|b_i-c_i|.
\]

The parent theorem gives (w_{i+1}>w_i).  More precisely, one endpoint
is fixed at every step.  If the (C)-endpoint moves, then

\[
 w_{i+1}-w_i=|c_{i+1}-c_i|\in\Delta C,
\tag{1}
\]

and if the (B)-endpoint moves, then

\[
 w_{i+1}-w_i=|b_{i+1}-b_i|\in\Delta B.
\tag{2}
\]

Because the parent interval strictly contains the child interval, the
relative order of the two classes stays fixed along the path.  The
(B)-endpoints move monotonically in one direction and the
(C)-endpoints monotonically in the other.  Thus the increments in
(1) and (2) telescope separately.  In a source contained in an
interval of length (L),

\[
 \sum_{i:\,C\text{ moves}}(w_{i+1}-w_i)\le L,
 \qquad
 \sum_{i:\,B\text{ moves}}(w_{i+1}-w_i)\le L.
\tag{3}
\]

The actual colors alternate along the path.  Consequently consecutive
reflection units, if they occur, must alternate their forcing classes.
Equations (1)--(3) are the unconditional path packing presently
available.  For integer marks they imply only the coarse bound that a
path has at most (H+1) vertices, hence at most (H+1) unit vertices,
whose weights lie in one band ([H,2H)).

## 2. A proper family with two consecutive units

Fix an integer (N\ge 8), and put

\[
 B=\{0,10N,11N\},
 \qquad
 C=\{-1,3,N,N+2,N+3\}.
\tag{4}
\]

Both classes are Golomb.  Indeed,

\[
 \Delta B=\{N,10N,11N\},
\tag{5}
\]

while

\[
 \Delta C=
 \{1,2,3,4,N-3,N-1,N,N+1,N+3,N+4\};
\tag{6}
\]

the ten values in (6) are distinct for (N\ge8).  Their only common
difference is (N).

Color every (B)-(B) strict cell (C), and every (C)-(C) strict
cell (B), as the diagonal rule requires.  Among the mixed cells set

\[
 \begin{aligned}
 z(0,-1)&=C,\\
 z(N+3,0)&=C,\\
 z(11N,3)&=C,
 \end{aligned}
\tag{7}
\]

and color every other mixed cell (B).

Here is a direct exhaustion of the nonautomatic corner constraints.
The mixed distances, listed by their (B)-endpoint, are

\[
\begin{array}{c|ccccc}
 b & c=-1&3&N&N+2&N+3\\ \hline
 0   &1&3&N&N+2&N+3\\
 10N &10N+1&10N-3&9N&9N-2&9N-3\\
 11N &11N+1&11N-3&10N&10N-2&10N-3.
\end{array}
\tag{8}
\]

Comparing (8) with (5)--(6), the only mixed endpoint lengths supported
by a within-class difference are

\[
 1,3,N,N+3,10N.
\tag{9}
\]

They give precisely the following unit and binary conditions.

* The (C)-reflection
  (-1<N+2<N+3), whose reflected output is (0), forces
  (z(0,-1)=z(N+3,0)=C).
* The (B)-reflection
  (0<10N<11N), whose reflected output is (N), forces
  (z(N,0)=z(11N,N)=B).
* At length (3), the fixed (C)-edge ((N+3,N)) gives the binary
  corner on (z(3,0)) and (z(N+3,0)); it is proper because the
  latter is (C).
* At length (N), the fixed (C)-edge ((N+3,3)) gives the binary
  corner on (z(N,0)) and (z(N+3,0)); these have colors (B,C).

There is no opposite-orientation pair of equal mixed distances.  The
only repeated mixed distance is (10N-3), attained at

\[
 (10N,3),\qquad (11N,N+3).
\]

It corresponds to the sole shared difference (N) and gives the sole
three-mixed-cell corner

\[
 (10N,3),\quad(11N,3),\quad(11N,N+3).
\tag{10}
\]

Under (7) its colors are (B,C,B).  The complete mixed-cell
classification therefore shows that (7) is a proper coloring of
(W(B\cup C)).

Now consider

\[
 v_0=(0,N),\qquad v_1=(0,N+3).
\tag{11}
\]

The first vertex has color (B) and is the (B)-reflection unit from
(0<10N<11N).  The (C)-pair (3<N+3) has length (N), so it makes
(v_1) the (C)-parent of (v_0).  The binary corner just listed
indeed transports the actual color (B) at (v_0) to the actual color
(C) at (v_1).  Finally, (v_1) is itself the (C)-reflection unit
from (-1<N+2<N+3).  Thus one forward implication path contains two
consecutive reflection-unit vertices, of weights

\[
 w(v_0)=N,\qquad w(v_1)=N+3.
\tag{12}
\]

Taking (N) through powers of two puts both weights in the same dyadic
band ([N,2N)), while

\[
 \frac{w(v_1)}{w(v_0)}=1+\frac3N\longrightarrow1.
\tag{13}
\]

Hence no bound based on a factor (1+\varepsilon) of growth between
unit occurrences can hold, for any fixed (arepsilon>0).

## 3. Exact remaining condition for longer paths

The local arithmetic needed to continue a path is explicit.  Suppose
(b<c), a (B)-colored vertex ((b,c)) has length (d=c-b), and its
(C)-parent is to have length (d+k).  The parent relation requires
the two (C)-marks

\[
 b+k,\qquad c+k,
\tag{14}
\]

and the parent is ((b,c+k)).  To make this parent a (C)-reflection
unit, it is enough to add, for some (ell>0), the (C)-pair

\[
 b-\ell,\qquad c+k-\ell,
\tag{15}
\]

of length (d+k).  Exchanging (B) and (C) and reflecting the order
gives the next step.  Thus the parent/unit equations themselves can be
iterated formally for any prescribed number of alternating steps.

What is not settled by those equations is whether the auxiliary marks
from all stages can simultaneously keep both classes Golomb and admit
a proper coloring of every induced mixed constraint.  Besides avoiding
opposite unit forces, one must control the new opposite-orientation
equal mixed distances and the three-variable clauses created by every
new shared class difference.  The two-unit family above handles that
inventory exactly, but it does not prove that arbitrarily many unit
vertices occur on one actual path.  Accordingly, the supported outcome
is:

\[
 \boxed{\text{two consecutive units occur, even at asymptotically equal
 weights; arbitrary path multiplicity remains open.}}
\]

The only unconditional quantitative replacement obtained here is the
additive endpoint-displacement budget (3), not a constant bound on unit
occurrences.
