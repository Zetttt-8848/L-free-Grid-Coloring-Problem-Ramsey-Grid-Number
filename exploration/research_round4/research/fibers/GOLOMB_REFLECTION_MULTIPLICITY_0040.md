# Golomb reflection multiplicity

Let (B\subset\mathbb Z) be Golomb: every positive difference between two
elements of (B) has a unique representation. Fix (r\notin B), and put

\[
 \mathcal T_r(B)=\{(a,b,c)\in B^3:a<b<c,\ r=a+c-b\},
 \qquad \mu_B(r)=|\mathcal T_r(B)|.
\]

Every such triple has (a<r<c). Indeed, writing

\[
 p=r-a>0,\qquad q=c-r>0,
\]

gives the useful normal form

\[
 (a,b,c)=(r-p,\ r+q-p,\ r+q),                 \tag{1}
\]

whose consecutive differences are (q,p).

## Sharp extremal-mark bound

Write

\[
 B_-=B\cap(-\infty,r),\qquad B_+=B\cap(r,\infty),
 \qquad \ell=|B_-|,\quad u=|B_+|.
\]

Then

\[
 \boxed{\ \mu_B(r)\le \min(\ell,u)\le
          \left\lfloor\frac{|B|}{2}\right\rfloor.\ }       \tag{2}
\]

For a fixed lower extreme (a), the equation (r=a+c-b) says

\[
 c-b=r-a.
\]

Golombness permits at most one ordered pair (b<c) with this difference.
Thus the map ((a,b,c)\mapsto a) is injective into (B_-). Similarly, for a
fixed upper extreme (c),

\[
 b-a=c-r,
\]

so ((a,b,c)\mapsto c) is injective into (B_+). This proves (2). The same
argument with (a+c=b+r) shows that a fixed middle (b) also occurs in at
most one triple: two representations would give an equality of nonzero
differences.

Consequently the outer pairs ({a,c}) form a matching between (B_-) and
(B_+). The triples themselves need not form a matching, because the middle
of one triple can be an extreme of another. A mark below (r) can occur only
as a lower extreme or a middle, and a mark above (r) only as an upper
extreme or a middle. Hence every mark has triple-degree at most two.

One convenient quotient records each outer matching edge as a vertex and
draws an arrow from a triple's outer edge to the outer edge containing its
middle, when such an edge exists. Its outdegree is at most one and its
indegree at most two. It can contain cycles. For example, with (r=0),

\[
 B=\{-101,-100,-9,1,10,110\}
\]

is Golomb: its fifteen positive differences are

\[
 1,9,10,19,91,92,100,101,102,109,110,111,119,210,211.
\]

It has the three reflection triples

\[
 (-9,1,10),\qquad (-100,10,110),\qquad (-101,-100,1).
\]

Their middle marks (1,10,-100) lie successively on the other outer edges,
giving a directed (3)-cycle. Here equality holds in (2).

## An infinite equality family

The coefficient (1/2) in (2) is sharp for arbitrarily large sets. Fix
(k\ge1), take an integer (M\ge10), and set

\[
 p_i=M^{k+1-i}\quad(1\le i\le k+1),
\]

\[
 B_k=\{-p_i:1\le i\le k+1\}
      \ \cup\
      \{p_i-p_{i+1}:1\le i\le k\}.                 \tag{3}
\]

Then (0\notin B_k), (|B_k|=2k+1), and for every (i\le k)

\[
 (-p_i,-p_{i+1},p_i-p_{i+1})\in\mathcal T_0(B_k).   \tag{4}
\]

Thus (2) gives (mu_{B_k}(0)=k=\lfloor |B_k|/2\rfloor).

For completeness, (B_k) is Golomb. Before substituting powers of (M),
write its formal elements as

\[
 L_i=-e_i\quad(1\le i\le k+1),\qquad
 R_i=e_i-e_{i+1}\quad(1\le i\le k)
\]

in the free abelian group on (e_1,\ldots,e_{k+1}). The differences of two
distinct formal elements are unique up to reversing their ordered pair. This
is read directly from their coefficient patterns:

* (L_i-L_j) has two unit coefficients of opposite signs;
* (R_i-R_j) has four unit coefficients when the two path edges are
  disjoint, and the consecutive pattern ((1,-2,1)) when they are adjacent;
* (R_i-L_j=e_i-e_{i+1}+e_j) has respectively one, two, or three support
  positions according as (j=i+1), (j=i), or neither. In the last case its
  unique negative position and its immediately preceding positive position
  recover (i), and the remaining positive position recovers (j).

These cases are mutually distinguished by support size and the occurrence of
a coefficient of magnitude two, and within each case the indices are
recovered from the displayed pattern. Now substitute
(e_i\mapsto p_i=M^{k+1-i}). If two resulting integer differences were equal,
subtracting their formal coefficient vectors would give a relation

\[
 \sum_j d_jM^j=0,\qquad |d_j|\le4.
\]

At its highest nonzero position, the leading term has magnitude at least
(M^j), whereas all lower terms have total magnitude at most
(4(M^j-1)/(M-1)<M^j). This is impossible. Hence no formal differences
collapse numerically, proving that (3) is Golomb.

The triples in (4) form a path: the middle (-p_{i+1}) of one is the lower
extreme of the next. Thus both paths and cycles genuinely occur, while the
outer extremes always retain their matching structure.

## What a weak-triangle coloring adds

Suppose now that (B\cup C) supports a proper two-color weak triangle,
that all diagonal marks of (B) have sign (s), and that (r\in C) has
sign (-s). For one reflection triple (a<b<c) in (B), the three internal
cells

\[
 (b,a),\quad(c,a),\quad(c,b)
\]

all have sign (-s), since each completes a corner whose two diagonal inputs
have sign (s). The two reflected corners then force

\[
 \boxed{\ z(r,a)=z(c,r)=s.\ }                       \tag{5}
\]

Indeed, ((b,a),(c,a),(c,r)) is a corner because
(r-a=c-b), and ((r,a),(c,a),(c,b)) is a corner because
(c-r=b-a). In each, the first two cells have sign (-s), so properness
forces the third to have sign (s).

Over all (mu_B(r)) triples, (5) produces (mu_B(r)) distinct (s)-cells
in row (r), indexed by the distinct lower extremes, and (mu_B(r))
distinct (s)-cells in column (r), indexed by the distinct upper extremes.
This is the exact additional color-sensitive conclusion.

It does not by itself improve (2). Pairing two forced cells in row (r)
requires a further row mark of the form

\[
 r-(a_j-a_i),
\]

and pairing two forced cells in column (r) requires the analogous translated
support on the upper side. Those marks are not supplied by the definition of
a reflection triple or by Golombness. If present, properness forces the
corresponding completion to sign (-s); if absent, the weak triangle contains
no such corner. Therefore an improvement over the sharp half-size bound needs
a quantitative hypothesis on these secondary translated supports. The mere
presence and opposite diagonal color of (r) yields the two fans (5), but no
closed numerical decrement from the present local data.

Root continuation: WEAK_REFLECTION_POSITION_BUDGET_0040.md, Section 4,
now gives a proper weak coloring of B union {r} for every Golomb B
and every r outside it: B diagonals +, the r diagonal -, strict B
cells -, and all strict r-incident cells +. Its direct corner proof
shows the half-size equality families remain attainable under actual
proper weak coloring. Section 2 of that root note also uses the
positional form of (2), over both classes together, to prove the
supported internal-reflection count at most floor(bc/2).
