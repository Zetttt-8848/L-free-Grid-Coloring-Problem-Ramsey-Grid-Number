# A two-cluster source-band inequality

## 1. Geometry and the active band

Let

\[
A=B\sqcup \widetilde C,\qquad B<\widetilde C,
\]

where \(\widetilde C=C+D\) is a translate of a finite integer set \(C\).  Put

\[
b=|B|,\qquad c=|C|,\qquad
M_B={b\choose2},\qquad M_C={c\choose2},\qquad
M=M_B+bc+M_C.
\]

Assume every internal difference of \(B\) and \(C\) is below \(H\), while every cross difference \(\widetilde c-u\), \(u\in B,\widetilde c\in\widetilde C\), lies in \([H,2H)\).  Let one proper coloring \(z\) be given on the whole strict source \(V(A)\).

Every equal pair of cross differences

\[
\widetilde c-u=\widetilde c'-u'
\]

with \(u<u'\) has \(\widetilde c<\widetilde c'\) and

\[
u'-u=\widetilde c'-\widetilde c.
\]

Conversely, every aligned pair of one internal \(B\)-edge and one internal \(C\)-edge of the same positive length produces such an equality.  Hence the active-band energy is

\[
T_H(A)=U(B,C)=\sum_{d>0}r_B(d)r_C(d).
\tag{1}
\]

The aim in this special geometry is

\[
U(B,C)\le\frac75M.
\tag{2}
\]

## 2. Opposite-colored child pairs

For a fixed internal difference \(d\), split the \(d\)-edges in each child triangle by their actual colors:

\[
r_{B,+}(d)+r_{B,-}(d)=r_B(d),\qquad
r_{C,+}(d)+r_{C,-}(d)=r_C(d).
\]

Let

\[
O_d=r_{B,+}(d)r_{C,-}(d)+r_{B,-}(d)r_{C,+}(d)
\tag{3}
\]

be the number of aligned \(d\)-edge pairs having opposite child colors.  Define the monochromatic equal-difference energies inside the two child triangles by

\[
\begin{aligned}
S_B&=\sum_d\left\{
{r_{B,+}(d)\choose2}+{r_{B,-}(d)\choose2}\right\},\\
S_C&=\sum_d\left\{
{r_{C,+}(d)\choose2}+{r_{C,-}(d)\choose2}\right\}.
\end{aligned}
\tag{4}
\]

Applying \(2xy\le x^2+y^2\) to the two products in (3) gives

\[
O_d\le\frac12\left(
r_{B,+}(d)^2+r_{B,-}(d)^2+
r_{C,+}(d)^2+r_{C,-}(d)^2
\right).
\]

Since

\[
r_{B,+}^2+r_{B,-}^2
=r_B+2\left\{{r_{B,+}\choose2}+{r_{B,-}\choose2}\right\},
\]

and \(\sum_dr_B(d)=M_B\), summing over \(d\) yields the finite child-color bound

\[
\boxed{\quad
O:=\sum_dO_d
\le \frac{M_B+M_C}{2}+S_B+S_C.
\quad}
\tag{5}
\]

This is the first place where the two internal source triangles enter quantitatively.  A standalone Cartesian matrix has no terms \(S_B,S_C\) tied to the same coloring.

## 3. Same-colored child pairs and support incidence

Let \(E_d=r_B(d)r_C(d)-O_d\), and put \(E=\sum_dE_d\).  Thus

\[
U=O+E.
\tag{6}
\]

An event counted by \(E_d\) consists of

\[
a=(u+d,u)\in V(B),\qquad
\gamma=(\widetilde c+d,\widetilde c)\in V(\widetilde C)
\]

with one common color \(\sigma\).  Let

\[
p=(\widetilde c,u),\quad
x=(\widetilde c+d,u),\quad
q=(\widetilde c+d,u+d).
\]

The long corner \(a,x,\gamma\) forces \(z(x)=-\sigma\).  The short corner \(p,x,q\) then forces at least one of \(p,q\) to have color \(\sigma\).

Build a bipartite incidence graph \(\mathcal G\):

* its left vertices are the \(E\) same-colored aligned child events;
* its right vertices are the \(bc\) cross cells \(\widetilde C\times B\);
* an event of color \(\sigma\) is adjacent to \(p\) and/or \(q\) exactly when that support cell has color \(\sigma\).

Every left vertex has at least one neighbor.  Assigning each event to one valid support is precisely a matching-with-reuse problem.  Let \(\nu(\mathcal G)\) be the maximum matching size.  The least possible repeated support load is

\[
R_*=E-\nu(\mathcal G).
\tag{7}
\]

Indeed, a matching of size \(\nu\) assigns \(\nu\) events to distinct supports; all remaining events create one unit of excess somewhere.  Conversely, from any support assignment, selecting one event at every used support gives a matching whose size is the number of used supports.

Equivalently, by the deficiency form of Hall's theorem,

\[
R_*=
\max_{\mathcal F\subseteq V_{\rm left}(\mathcal G)}
\bigl(|\mathcal F|-|N(\mathcal F)|\bigr).
\tag{8}
\]

Since \(\nu(\mathcal G)\le bc\), equations (7) and (6) give

\[
E=\nu(\mathcal G)+R_*\le bc+R_*.
\tag{9}
\]

## 4. Master inequality

Combining (5), (6), and (9) gives

\[
\boxed{\quad
U(B,C)
\le
bc+\frac{M_B+M_C}{2}
+S_B+S_C+R_*.
\quad}
\tag{10}
\]

Writing \(I=M_B+M_C\), the desired estimate (2) follows from the concrete source-compatible closure

\[
\boxed{\quad
S_B+S_C+R_*
\le
\frac9{10}I+\frac25bc.
\quad}
\tag{11}
\]

Indeed, the right side of (10) would then be

\[
bc+\frac12I+\frac9{10}I+\frac25bc
=\frac75(I+bc)=\frac75M.
\]

Thus the \(7/5\) problem for the two-cluster band has been reduced to two quantities that retain the one-source colors:

1. \(S_B+S_C\), the monochromatic repeated-difference energy in the child triangles;
2. \(R_*\), the Hall deficiency of the actual cross-support incidence graph.

Neither quantity appears in the false standalone Cartesian estimate.

## 5. How the support-cloud lemma enters \(R_*\)

For a fixed cross support, events assigned to it have the support's color.  The source-compatible cloud lemma from checkpoint 0018 says that repeated offsets of one translated-support color force actual child cells of that color at their pairwise difference.  Using consecutive offsets gives the descent mechanism from checkpoint 0019.

In the present formulation, those facts constrain subsets \(\mathcal F\) with large Hall deficiency in (8): if many same-colored events have a small support neighborhood, their repeated offsets create many forced monochromatic child relations, which add to \(S_B+S_C\).  This is exactly the tradeoff requested in (11).

The remaining obstruction is that one forced child relation can be generated by several deficient support clouds.  The convergence multiplicity identified in SOURCE_CLOUD_SUMMATION_0019.md therefore reappears as overlap between certificates for different Hall-deficient subsets.  Equations (10)-(11) show the coefficient that an amortization must meet: after the elementary matrix bound, the combined child-correlation and Hall-deficiency cost has allowance

\[
\frac9{10}(M_B+M_C)+\frac25bc.
\tag{12}
\]

This allowance is substantially larger than the half-cell capacities required by the discarded standalone \(3/2\) Cartesian route, but no bounded-overlap proof is obtained here.

## 6. Exact scope

Inequality (10) is the completed special-case lemma.  It is finite, uses the actual shared colors on both child triangles and the cross rectangle, and makes no standalone Cartesian assumption.  The exact remaining implication for the \(7/5\) target is (11).

A counterexample to (11) would not automatically refute (2), because (5) can have slack.  A counterexample to (2) would require a full proper source coloring of both clusters and their cross block.  No such construction is produced here.
