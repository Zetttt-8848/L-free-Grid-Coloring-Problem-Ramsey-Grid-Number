# Reflected caps for reversed anchored sums

Normalize \(\min A=0\), put \(B=A\setminus\{0\}\), and write

\[
f(t)=z(t,0),\qquad t\in B.
\tag{1}
\]

For an addition \(x+y=w\) in \(B\), retain its two distinct physical
cells

\[
g_x(y)=z(w,y),\qquad g_y(x)=z(w,x).
\tag{2}
\]

The difficult anchored-color type is

\[
f(x)=f(y)=-f(w).
\tag{3}
\]

Neither cell in (2) is forced by either anchored corner separately.
The following two positive-corner lemmas give a disjunctive constraint
and then a one-sided forcing mechanism.

## 1. The double hinge retains both physical cells

**Lemma 1.**  Let \(0<x<y\), let \(w=x+y\), and suppose

\[
x,y,w,2x\in B,\qquad
f(x)=f(2x)=s,\qquad f(w)=-s.
\tag{4}
\]

If also \(f(y)=s\), then

\[
\boxed{g_x(y)=s\quad\hbox{or}\quad g_y(x)=s.}
\tag{5}
\]

**Proof.**  The anchored corner

\[
(x,0),\qquad(2x,0),\qquad(2x,x)
\tag{6}
\]

has its first two cells colored \(s\), so

\[
z(2x,x)=-s.
\tag{7}
\]

Now use the positive corner of step \(y-x>0\)

\[
(2x,x),\qquad(w,x),\qquad(w,y).
\tag{8}
\]

Its last two cells are precisely \(g_y(x)\) and \(g_x(y)\).  They cannot
both have color \(-s\), proving (5).  \(\square\)

In the notation of the anchored fiber partition, (5) says that the
reversed relation must choose at least one of the memberships

\[
y\in P_x,\qquad x\in P_y,
\tag{9}
\]

provided the smaller input has a same-color double.  This is a genuine
constraint on the two physical cells, rather than a recoloring of the
addition relation.

## 2. A reflected cap forces one side of the choice

**Lemma 2 (reflected cap).**  Let \(0<x<y\), suppose

\[
x,y,x+y,2y,2y-x\in B,
\tag{10}
\]

and assume

\[
f(x)=f(y)=f(2y)=f(2y-x)=s.
\tag{11}
\]

Then necessarily

\[
\boxed{
f(x+y)=-s,\qquad g_y(x)=z(x+y,x)=s.
}
\tag{12}

**Proof.**  The two anchored corners

\[
(y,0),(2y,0),(2y,y)
\tag{13}

and

\[
(2y-x,0),(2y,0),(2y,x)
\tag{14}

have same-color anchored cells.  Hence

\[
z(2y,y)=z(2y,x)=-s.
\tag{15}

Because \(x<y\), the three cells

\[
(x+y,x),\qquad(2y,x),\qquad(2y,y)
\tag{16}

form a positive corner of step \(y-x\).  Its last two cells have color
\(-s\), so

\[
z(x+y,x)=s.
\tag{17}

Finally,

\[
(y,0),\qquad(x+y,0),\qquad(x+y,x)
\tag{18}

is the anchored corner belonging to the addition \(y+x=x+y\).  Its
first and third cells have color \(s\), forcing
\(f(x+y)=-s\).  All steps in (13)--(18) are positive.  \(\square\)

Thus the four same-color anchors in (11) do more than constrain an
already identified reversed relation: they create that reversed output
and force the particular incidence

\[
x\in P_y.
\tag{19}

\]

## 3. A two-relation fan obstruction

The smallest direct composition of Lemma 2 uses the sum-free property
of \(P_y\).

**Proposition.**  Let \(r>0\) and \(y>4r\).  Suppose all eight marks

\[
r,\ 2r,\ y,\ y+r,\ y+2r,\ 2y,\ 2y-r,\ 2y-2r
\tag{20}

belong to \(B\).  In a proper coloring it is impossible to have

\[
f(r)=f(2r)=f(y)=f(2y)=f(2y-r)=f(2y-2r)=s.
\tag{21}

**Proof.**  Apply Lemma 2 first with \(x=r\).  It gives

\[
f(y+r)=-s,\qquad g_y(r)=s,\qquad r\in P_y.
\tag{22}

Apply it again with \(x=2r\).  It gives

\[
f(y+2r)=-s,\qquad g_y(2r)=s,\qquad 2r\in P_y.
\tag{23}

But \(P_y\cup\{0\}\) is Golomb.  The two pairs

\[
\{0,r\},\qquad\{r,2r\}
\tag{24}

give two representations of the same positive difference \(r\), a
contradiction.  Equivalently, the sum-free property of \(P_y\) forbids
\(r,r+r\in P_y\).  \(\square\)

The inequality \(y>4r\) merely keeps the displayed marks distinct and
their prescribed roles transparent.  The forcing itself only uses the
positive inequalities stated in Lemma 2; any collision demanding both
colors is already an immediate contradiction.

## 4. What this controls and what remains

Lemma 1 turns a reversed relation into a two-way fan-membership choice
when \(2x\) is present with the required anchored color.  Lemma 2 uses
the reflected support \(2y-x\), together with \(2y\), to choose the
specific membership \(x\in P_y\).  The proposition shows that two such
choices with labels \(r,2r\) cannot accumulate at one anchor.

This does not yet give a linear bound on the total reversed-sum count
\(R\).  A sparse source may omit \(2x\), \(2y\), or \(2y-x\); even when
these marks exist, their anchored colors may fail the hypotheses.  If
the cap is absent, (3) alone still leaves both cells in (2) unforced.
Thus a global use of this mechanism requires a budget for missing or
wrong-color double/reflection supports, or a second forcing motif that
handles those failures.  No bound such as \(R\le2|B|\), EP10, or a main
source inequality follows from the local proposition alone.
