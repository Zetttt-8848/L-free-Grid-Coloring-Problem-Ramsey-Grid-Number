# Exact mixed-cell criterion for two opposite diagonal marks

Let \(B\) be Golomb and let

\[
C=\{r,s\},\qquad r<s,\qquad B\cap C=\varnothing.
\tag{1}
\]

Prescribe diagonal color \(B\) on \(B\) and diagonal color \(C\) on
\(r,s\).  The fixed strict cells are

\[
z(q,p)=C\quad(p<q\text{ in }B),
\qquad
z(s,r)=B.
\tag{2}
\]

For \(c\in\{r,s\}\) and \(b\in B\), denote the mixed variable on the
unordered pair \(\{b,c\}\) by

\[
X_{c,b}=z(\max\{b,c\},\min\{b,c\}).
\tag{3}
\]

There are \(2|B|\) such variables.  All remaining extension conditions
can be stated on them.

## 1. Units and the two binary graphs

Every internal reflection

\[
a<p<q\quad\text{in }B,\qquad c=a+q-p\in\{r,s\}
\tag{4}
\]

forces

\[
X_{c,a}=X_{c,q}=B.
\tag{5}
\]

Let \(\mathcal U\) be the set of variables forced to \(B\) by all such
reflection units.  Since the opposite diagonal class has only two
marks, it contains no reflection triple.  Thus there are no unit forces
to color \(C\).  In particular, an opposite-unit conflict is impossible
in this two-point setting.

Define two graphs on the mixed variables.

* Put \(\{x,y\}\) in \(G_B\) when \(x,y\), together with a fixed
  \(B\)-colored cell, form an actual positive corner.  Its constraint is
  that \(x,y\) are not both \(B\).

* Put \(\{x,y\}\) in \(G_C\) when \(x,y\), together with a fixed
  \(C\)-colored \(B\)-\(B\) cell, form an actual positive corner.  Its
  constraint is that \(x,y\) are not both \(C\).

These definitions retain the physical cells and positive orientation;
they are precisely the binary cases in the complete mixed-cell
classification.

The graph \(G_B\) is especially small.  Put \(\delta=s-r\).  Its only
possible edges are:

\[
\{X_{r,\,2r-s},X_{s,\,2r-s}\}
\quad\text{if }2r-s\in B,
\tag{6}
\]

\[
\{X_{r,\,2s-r},X_{s,\,2s-r}\}
\quad\text{if }2s-r\in B,
\tag{7}
\]

and, for the unique unordered pair \(p\le q\) in \(B\cap(r,s)\) with
\(p+q=r+s\),

\[
\{X_{r,q},X_{s,p}\}
\quad\text{and}\quad
\{X_{r,p},X_{s,q}\}
\quad\text{if }p<q,
\tag{8}
\]

while for \(p=q\) these two displayed edges coincide and occur only once.
For (6), the positive corner is

\[
(r,2r-s),\quad(s,2r-s),\quad(s,r).
\]

For (7), it is

\[
(s,r),\quad(2s-r,r),\quad(2s-r,s).
\]

For the first edge in (8), it is

\[
(q,r),\quad(s,r),\quad(s,p).
\]

The second edge comes from

\[
(p,r),\quad(s,r),\quad(s,q).
\]

In every case the fixed cell is \((s,r)\), of color \(B\).
Golombness makes the unordered pair \(\{p,q\}\) in (8) unique, since
it has the prescribed sum \(r+s\). The two interior edges are disjoint
when \(p<q\), and the midpoint case \(p=q\) gives one edge. The lower,
upper, and interior alternatives use disjoint \(B\)-marks.

The apparent four-edge case cannot occur. If both exterior marks
\(2r-s\) and \(2s-r\) belong to \(B\), their sum is \(r+s\). Any interior
pair \(p+q=r+s\), including a doubled midpoint pair, would be a second
unordered \(B\)-pair of that sum, contrary to Golombness. Thus either the
two exterior edges occur, or at most one exterior edge occurs together
with at most two interior edges. Hence

\[
\boxed{G_B\text{ is a matching with at most three edges}.}
\tag{9}
\]

The graph \(G_C\) can be larger.  Its edges are exactly the mixed pairs
whose positive corner has a fixed \(B\)-\(B\) cell as its third member.
No independent recoloring or omitted corner type is hidden in this
definition.

## 2. The sole possible three-variable clause

There is a three-variable mixed corner exactly when

\[
\delta=s-r\in\Delta B.
\tag{10}
\]

Let \(p,p+\delta\) be the unique \(B\)-pair of difference \(\delta\).
If \(p<r\), its three actual cells are

\[
T=\{X_{r,p},X_{s,p},X_{s,p+\delta}\}.
\tag{11}
\]

They form the positive corner

\[
(r,p),\quad(s,p),\quad(s,p+\delta).
\]

If \(r<p\), the three cells are

\[
T=\{X_{r,p},X_{r,p+\delta},X_{s,p+\delta}\},
\tag{12}
\]

forming

\[
(p,r),\quad(p+\delta,r),\quad(p+\delta,s).
\]

These are the two orientations of the same rotated parallelogram.
There is no other three-variable clause because
\(\Delta C=\{\delta\}\) and \(B\) is Golomb.

## 3. Necessary and sufficient extension criterion

Let \(Z\) be the set of mixed variables assigned color \(C\); every
mixed variable outside \(Z\) is assigned color \(B\).

**Theorem.**  The prescribed diagonal coloring extends to a proper
coloring of \(W(B\cup\{r,s\})\) if and only if there is a set \(Z\)
satisfying all of the following:

\[
Z\cap\mathcal U=\varnothing;
\tag{13}
\]

\[
Z\text{ meets every edge of }G_B;
\tag{14}
\]

\[
Z\text{ is an independent set in }G_C;
\tag{15}
\]

and, when the triple \(T\) in (11) or (12) exists,

\[
1\le |Z\cap T|\le2.
\tag{16}
\]

**Proof.**  Condition (13) is exactly the family of reflection units
(5).  A corner defining an edge of \(G_B\) already contains one fixed
\(B\)-cell, so it is proper exactly when at least one endpoint lies in
\(Z\); this is (14).  A corner defining an edge of \(G_C\) contains one
fixed \(C\)-cell, so it is proper exactly when its two endpoints do not
both lie in \(Z\); this is (15).  The sole all-mixed corner is proper
exactly when its three variables are not all \(B\) and not all \(C\),
which is (16).

The diagonal corners and fixed-only corners are already proper, and
the complete mixed-cell classification has no further cases.  Hence
the conditions are both necessary and sufficient.  \(\square\)

The theorem turns extension into an independent-transversal problem
for a matching of size at most three, with at most one additional
three-variable condition.

## 4. Why unit and shadow checks are not the whole criterion

A reflection-shadow edge between \(r\) and \(s\) is an immediate
obstruction: its nested reflection units make one of the relevant
mixed corners monochromatic.  In the criterion above, this appears as
a failure of (13)--(14), or as an already fixed violation of (16).
Its absence is necessary.

It is not, by itself, a sufficient logical condition.  The remaining
binary corners can obstruct every independent transversal.  The
smallest transparent pattern is the following conditional actual-cell
motif.  Suppose \(G_B\) contains two edges

\[
e_1=\{x_1,x_2\},\qquad e_2=\{y_1,y_2\},
\tag{17}
\]

none of whose vertices is a reflection unit, while \(G_C\) contains
all four edges

\[
\{x_i,y_j\},\qquad i,j\in\{1,2\}.
\tag{18}
\]

The two actual positive corners defining (17) require \(Z\) to contain
some \(x_i\) and some \(y_j\).  The actual positive corner defining
that pair in (18) then forbids both from lying in \(Z\), a
contradiction.  This motif has no opposite unit force and need not use
a shadow edge between \(r,s\).  It records an additional obstruction
that any sufficiency proof must exclude using the integer geometry.

Likewise, when \(T\) exists, a transversal satisfying the binary
conditions must still meet \(T\) without containing all of \(T\).
This is independent of merely checking for opposite units.

## 5. A sharply sufficient usable form

Because \(G_B\) is a matching, the criterion has the following direct
sufficient form.  Choose one non-unit endpoint from every edge of
\(G_B\).  If the chosen endpoints form an independent set in \(G_C\),
and they can be augmented or adjusted so that (16) holds, then color
those selected variables \(C\) and every remaining mixed variable
\(B\).  The theorem proves this is a full proper weak extension.

The unresolved arithmetic implication is whether the special graphs
arising from one Golomb set \(B\) prohibit the independent-transversal
obstruction (17)--(18), and always permit the adjustment for \(T\), once
reflection-shadow edges are absent.  No such geometric theorem is
proved here.  Thus absence of unit and shadow conflicts is not promoted
to an extension theorem without this remaining condition.
