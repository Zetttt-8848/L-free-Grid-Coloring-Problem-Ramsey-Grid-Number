# Almost monochromatic anchors in an all-forcing source

Let (A\subset\mathbb Z) be finite, translate its minimum to (0), and put

\[
B=A\setminus\{0\},\qquad n=|B|.
\]

Assume that a proper coloring of the strict source on (A) is
all-forcing: the two parallel endpoint cells of every actual corner have
the same color. Consequently every non-singleton difference fiber is
monochromatic; assign its color to that difference and write

\[
z(v,u)=f(v-u).
\]

The same notation may be assigned arbitrarily to singleton fibers, using
the color of their unique cell. This note counts additions at the minimum
endpoint under two special hypotheses on the actual anchor colors
(f(a)=z(a,0)), (a\in B).

## 1. The anchored additive-corner rule

Suppose (x,y,x+y\in B). The three cells

\[
(x,0),\qquad (x+y,y),\qquad (x+y,0)
\]

form a positive corner. The first two lie in the difference-(x) fiber,
so their common color is (f(x)), while the third has color (f(x+y)).
Properness therefore gives

\[
f(x+y)=-f(x).                                      \tag{1}
\]

If (x\ne y), the same source support also gives the corner with the
roles of (x) and (y) exchanged. Hence

\[
f(x)=f(y)=-f(x+y).                                  \tag{2}
\]

For (x=y), equation (1) reads (f(2x)=-f(x)). These statements use the
all-forcing hypothesis to identify the internal cell color with the
anchor color of its numerical difference. They do not follow merely from
the three anchor cells.

Let (J_0(A)) be the endpoint addition graph: it has vertex set (B) and
an arc (x\to w) when (0<x<w) and (w-x\in B). Its arc count is the
exact minimum-endpoint deletion cost

\[
e_0(A)=T(A)-T(A\setminus\{0\}).                     \tag{3}
\]

Thus (1) says that every arc of (J_0(A)) changes anchor color.

## 2. One anchor color

Assume first that (f(a)=s) for every (a\in B). If positive
(x,y,x+y\in A) existed, (1) would say (s=-s). Therefore

\[
\#\{\{x,y\}:x,y>0, x,y,x+y\in A\}=0,
\qquad e_0(A)=0.                                    \tag{4}
\]

This is sharp and stronger than a constant linear estimate. By (3),
deleting the minimum loses no corners at all.

The conclusion is a one-step endpoint statement. The surviving source is
still all-forcing, but after translating its new minimum, its new anchor
colors are colors of differences between old marks and need not all equal
(s). Thus (4) cannot be iterated without an additional hereditary
hypothesis.

## 3. Exactly one exceptional anchor mark

Now assume that there is exactly one (r\in B) with

\[
f(r)=-s,qquad f(a)=s\quad(a\in B\setminus\{r\}).   \tag{5}
\]

Equations (1)-(2) classify every positive addition in (A).

If (x\ne y) and (x+y=w), then the two input colors agree and are
opposite to the output color. Under (5), the output must therefore be the
unique exceptional mark:

\[
x+y=r,qquad x,y\ne r.                              \tag{6}
\]

If (x=y), equation (1) permits precisely

\[
2x=r\quad(x\ne r),
\qquad\text{or}\qquad
x=r, 2r\in A.                                     \tag{7}
\]

Conversely, (5) presents no anchored-corner obstruction to the relations
in (6)-(7). Hence all additions at zero consist of decompositions of (r),
together with the possible self-doubling (r+r=2r).

The involution (x\mapsto r-x) pairs the regular marks participating in
(6), with the possible fixed point (r/2). Each participating regular
mark supplies exactly one directed arc into (r). If (2r\notin A), at
most the (n-1) regular marks can participate. If (2r\in A), that mark
cannot participate in a positive decomposition of (r), so at most
(n-2) arcs enter (r), and the single arc (r\to2r) restores at most
one. In both cases

\[
e_0(A)\le n-1=|A|-2.                                \tag{8}
\]

Equivalently, if additive triples are counted with unordered summands,
their number is at most

\[
\left\lceil\frac n2\right\rceil.                   \tag{9}
\]

The directed count (8), rather than (9), is the quantity in the endpoint
deletion identity.

## 4. A family attaining the directed bound

The coefficient and additive constant in (8) are sharp. Fix (m\ge1),
choose an integer base (R\ge5), and set

\[
x_0=0,\qquad x_i=R^i\ (1\le i\le m),\qquad
r=R^{m+2},
\]

\[
A=\{x_i,r-x_i:0\le i\le m\}.
\tag{10}
\]

Thus (0,r\in A), all (x_i) lie below (r/2), and

\[
n=2m+1.
\]

Uniqueness of balanced base-(R) expansions with coefficients of
absolute value at most (2) shows that the only repeated positive
differences are, for (0\le i<j\le m),

\[
\delta_{ij}=x_j-x_i,qquad
H_{ij}=r-x_i-x_j.                                   \tag{11}
\]

The two representations of (delta_{ij}) are

\[
(x_j,x_i),\qquad(r-x_i,r-x_j),
\]

and the two representations of (H_{ij}) are

\[
(r-x_j,x_i),\qquad(r-x_i,x_j).
\]

The central differences

\[
H_{ii}=r-2x_i                                      \tag{12}
\]

have one representation each. Color difference fibers by

\[
f(\delta_{ij})=f(H_{ij})=s\quad(i<j),
\qquad f(H_{ii})=-s.                                \tag{13}
\]

These formulas cover every repeated fiber and every completion used by
one. Give all remaining singleton fibers either color, subject to (13)
where they are the central fibers.

For a (delta_{ij})-corner, the two endpoint cells have color (s) and
their outer completion has difference (H_{ii}), hence color (-s).
The same is true for the (H_{ij})-corner. These are all actual corners,
so the coloring is proper and all-forcing.

At the anchor, (x_i=\delta_{0i}) and
(r-x_i=H_{0i}) have color (s) for (i>0), while
(r=H_{00}) has color (-s). Thus (r) is the unique exceptional
anchor mark. The positive additions at zero are exactly

\[
x_i+(r-x_i)=r\qquad(1\le i\le m),                  \tag{14}
\]

each with two directed arcs. Therefore

\[
e_0(A)=2m=n-1,                                     \tag{15}
\]

which attains (8) for arbitrarily large sources.

## 5. Scope

For an all-forcing source, a monochromatic nonzero anchor is sum-free and
has zero minimum-endpoint cost. With one exceptional anchor mark, the
complete addition classification (6)-(7) gives the sharp bound
(e_0(A)\le |A|-2). The construction (10)-(15) shows that no sublinear
improvement follows in this class. These are single-endpoint statements;
they do not assert that the anchor hypothesis survives deletion and do
not give a bound for unrestricted all-forcing sources.
