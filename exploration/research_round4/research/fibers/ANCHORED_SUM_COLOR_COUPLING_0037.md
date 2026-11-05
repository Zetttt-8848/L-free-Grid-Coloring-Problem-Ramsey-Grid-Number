# Anchored sum colors and an internal fan collision

Let \(A\) be a finite integer source with \(\min A=0\), and suppose the
strict source triangle \(V(A)\) has a proper two-coloring \(z\).  Put
\[
B=A\setminus\{0\},\qquad f(x)=z(x,0)\quad(x\in B).
\]
An additive arc is a relation
\[
x\longrightarrow x+y,\qquad x,y,x+y\in B.             \tag{1}
\]
If the two anchored cells at the ends of (1) have the same color \(c\),
the corner
\[
\{(x,0),(x+y,0),(x+y,y)\}
\]
forces
\[
z(x+y,y)=-c.                                           \tag{2}
\]
The following lemma couples two such anchored arcs through an ordinary
corner entirely inside \(B\).

## 1. Anchored fan-difference lemma

**Lemma.**  Let \(x,y,z\) be positive marks with \(y<z\), and suppose
\[
x,\ y,\ z,\ x+y,\ x+z\in B.                            \tag{3}
\]
If
\[
f(x)=f(x+y)=f(x+z)=c,                                  \tag{4}
\]
then, whenever
\[
a:=x+z-y\in B,                                         \tag{5}
\]
one has
\[
f(a)=-c.                                               \tag{6}
\]

**Proof.**  The two anchored arcs
\[
x\to x+y,\qquad x\to x+z
\]
and (4) force
\[
E_y=(x+y,y),\qquad E_z=(x+z,z)
\]
to color \(-c\).  These cells lie on the same offset-\(x\) diagonal.
Their ordinary completion is
\[
Q=(x+z,y),                                             \tag{7}
\]
so properness forces \(z(Q)=c\).

On the other hand, (5) gives the anchored arc
\[
a\to x+z,\qquad (x+z)-a=y.
\]
If \(f(a)=c=f(x+z)\), its completion is again exactly
\[
(x+z,(x+z)-a)=(x+z,y)=Q,
\]
and (2) would force \(z(Q)=-c\), a contradiction.  Hence \(f(a)=-c\).
\(\square\)

The support marks \(y,z\) need not have prescribed anchored colors.
Only the tail \(x\), the two fan outputs \(x+y,x+z\), and the competing
tail \(x+z-y\) occur in (4) and (6).

Equivalently, the following anchored-color pattern is forbidden:
\[
f(x)=f(x+y)=f(x+z)=f(x+z-y),\qquad 0<y<z,              \tag{8}
\]
whenever all five support marks in (3) and the last mark in (5) belong
to \(B\). This uses four actual positive corners: the two anchored
corners forcing \(E_y,E_z\), their ordinary completion at \(Q\), and
the competing anchored corner which also completes at \(Q\).

## 2. A quantitative local consequence

Fix \(x\in B\), write \(c=f(x)\), and define the same-color anchored fan
in summand coordinates by
\[
Y_x^c
=\{y\in B:x+y\in B,\ f(x+y)=c\}.                       \tag{9}
\]
Its translated output set is
\[
N_x^c=x+Y_x^c
=\{w>x:w,w-x\in B,\ f(w)=f(x)\}.                       \tag{10}
\]
For every \(y\in Y_x^c\), (2) colors the cell \((x+y,y)\) by \(-c\).
All these cells lie in one actual offset-\(x\) fiber.  Consequently
\(Y_x^c\), equivalently \(N_x^c\), is Golomb: two distinct pairs with
the same positive difference would give two equal-color endpoint cells
of one corner and an anchored completion conflict.

Now take \(y<z\) in \(Y_x^c\).  The lemma says
\[
x+(z-y)\notin B_c,                                    \tag{11}
\]
where
\[
B_c=\{v\in B:f(v)=c\}.
\]
Since \(Y_x^c\) is Golomb, all differences \(z-y\) from its unordered
pairs are distinct.  Therefore
\[
\boxed{\qquad
\bigl(x+\Delta Y_x^c\bigr)\cap B_c=\varnothing,
\qquad
|x+\Delta Y_x^c|=\binom{|Y_x^c|}{2}.
\qquad}                                                \tag{12}
\]
This is stronger than the assertion that the fan itself is Golomb:
every pair in the fan produces a distinct anchored location which is
either absent from the source or has the opposite anchored color.

For an explicit interval form, let \(k=|Y_x^c|\).  If \(k\ge2\), put
\[
R_x=\max Y_x^c-\min Y_x^c
\]
and let
\[
H_A(x,R_x)
=|\{n\in[x+1,x+R_x]:n\notin A\}|.
\]
All points in \(x+\Delta Y_x^c\) lie in this interval.  Hence (12) gives
the local density inequality
\[
\boxed{\qquad
\binom{k}{2}
\le
H_A(x,R_x)
+|B_{-c}\cap[x+1,x+R_x]|.
\qquad}                                                \tag{13}
\]
For \(k\le1\), (13) holds with both sides interpreted in the evident
way.

Thus a large same-color anchored out-neighborhood cannot occur in a
dense interval of the same anchored color.  Its quadratic pair count
must be absorbed by actual opposite-color anchors or by missing source
marks.

## 3. A four-term corollary

Taking
\[
y=x,\qquad z=3x
\]
in the lemma gives \(x+y=2x\), \(x+z=4x\), and
\(x+z-y=3x\).  Therefore:

**Corollary.**  If \(x,2x,3x,4x\in B\), their four anchored cells cannot
all have one color:
\[
\{f(x),f(2x),f(3x),f(4x)\}
\quad\text{is not monochromatic}.                      \tag{14}
\]

The coincident summands in the arc \(x+x=2x\) cause no degeneracy.  The
two forced offset-\(x\) cells are \((2x,x)\) and \((4x,3x)\), whose
completion is \((4x,x)\); the anchored pair \(3x,4x\) forces the
opposite color on that same completion.

## 4. Counting scope and remaining gap

The lemma controls only arcs whose output color agrees with the anchored
tail color.  Arcs \(x\to x+y\) with \(f(x+y)\ne f(x)\) do not force
\((x+y,y)\), so they contribute no member to (12).

Even among the controlled fans, summing (13) over \(x\) has genuine
multiplicity.  The same opposite-color anchored mark can equal
\[
x+(z-y)
\]
for many different tails \(x\), and a source hole can be reused in the
same way.  Golombness makes the charges injective within one fixed fan,
not across different tails.  Thus (12) does not by itself imply a
universal bound such as \(|E(J)|\le10|B|\).

Root continuation: `../ANCHORED_FAN_ARC_BUDGET_0037.md` now charges
supported fan pairs to distinct opposite-color addition arcs. It retains
separate missing-step and missing-target defects. This avoids charging
only the target vertex, but a linear arc budget is still open.

The new structural input is the exact collision rule (6) and its
quadratic local budget (13).  To turn it into a global anchored-Schur
edge bound, one still needs either a bounded-multiplicity selection of
tails or a second relation coupling repeated charges from different
tails.  No such global selection claim is made here.
