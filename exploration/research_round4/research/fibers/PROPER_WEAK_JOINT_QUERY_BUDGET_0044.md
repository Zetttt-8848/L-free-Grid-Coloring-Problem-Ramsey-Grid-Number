# The joint query budget in the two-anchor normal form

This note tests the proposed properness-specific inequality

\[
N+Q\le M=\binom{|B|+|C|}{2}
\tag{1}
\]

at the first nontrivial structured boundary, where one diagonal class has
two marks.  In that boundary (1) is true for every disjoint Golomb pair,
whether or not the prescribed diagonal coloring has a proper weak
extension.  Thus the two-anchor binary normal form contains no
counterexample, but properness is not the mechanism that proves the
bound there.  The argument does not extend to two classes of size at least
three.

## 1. Statement

Let \(B,C\subset\mathbb Z\) be finite, disjoint Golomb sets.  For \(j>0\)
write

\[
\beta_j=1_{j\in\Delta B},\qquad
\gamma_j=1_{j\in\Delta C},
\]

\[
x_j=|\{u\in B:u+j\in C\}|,qquad
y_j=|\{u\in C:u+j\in B\}|,
\]

and

\[
N=\sum_j(\beta_j+\gamma_j)(x_j+y_j),qquad
Q=\sum_jx_jy_j.
\tag{2}
\]

Put \(b=|B|,c=|C|\),

\[
U=\binom b2+\binom c2,qquad M=U+bc.
\]

The bounded claim proved here is

\[
\boxed{\min(b,c)\le2\quad\Longrightarrow\quad N+Q\le M.}
\tag{3}
\]

The classes are labeled; exchanging them is allowed and preserves all
quantities.  Translation is also allowed.  No equivalence is used to omit
any mixed pair.

## 2. Derivation scope

The route is an explicit symbolic derivation in the two-anchor normal
form.  No SAT, solver search, enumeration, or probabilistic argument is
used.  The unit and binary extension criterion is retained as context, but
the resulting estimate turns out to follow from the diagonal Golomb
geometry alone.

The supplied \(4+4\) numerical excess configuration is also tested by one
direct mixed-cell implication.  It fails properness by an opposite unit
conflict, as recorded in Section 3.5 below.

## 3. Proof

The following symbolic argument proves (3) throughout the two-anchor class.

### 3.1 Reduction to exactly two anchors

If one class has at most one mark, its positive difference support is
empty, so the shared-difference number is zero.  The disjoint-support
identity already gives \(N+Q\le M\).  It remains to treat a class of
exactly two marks.

By translation and exchange of the classes, write

\[
C=\{0,d\},\qquad d>0,qquad |B|=b.
\tag{4}
\]

There are \(2b\) mixed pairs.  Let

\[
R=|\{(a,c)\in B\times C:|a-c|\notin\Delta B\}|
\tag{5}
\]

be the number of their lengths unsupported by \(B\).  The \(B\)-part of
\(N\) is therefore exactly \(2b-R\).

The only positive \(C\)-difference is \(d\).  A mixed pair has length
\(d\) precisely when its \(B\)-endpoint is \(-d\) or \(2d\): the other
two formal possibilities \(0,d\) are the anchors themselves and are not
in \(B\).  Put

\[
E=1_{-d\in B}+1_{2d\in B}\in\{0,1,2\}.
\tag{6}
\]

Consequently

\[
N=2b-R+E.
\tag{7}
\]

Since now \(U=\binom b2+1\) and \(M=2b+U\), inequality (1) is equivalent
to the sharply reduced budget

\[
E+Q\le \binom b2+1+R.
\tag{8}
\]

### 3.2 Exact pair-sum description of \(Q\)

Every contribution to \(x_jy_j\) pairs one mixed interval in each
orientation.  If their \(B\)-endpoints are \(a,a'\) and their
\(C\)-endpoints are \(c,c'\), equality of their positive lengths is
equivalent to

\[
a+a'=c+c'.
\tag{9}
\]

The unordered \(C\)-multiset \(\{c,c'\}\) has only the three possible
sums

\[
0,\qquad d,\qquad 2d.
\tag{10}
\]

A Golomb set has at most one unordered pair with repetitions allowed of
any prescribed sum.  Indeed, two distinct representations of one sum,
after ordering and cancelling a common endpoint if present, give two
distinct pairs with the same positive difference.  A representation
\(a+a'=2m\) distinct from \(m+m\) likewise gives
\(m-a=a'-m>0\) twice.

For sums \(0\) and \(2d\), the \(C\)-multiset is repeated, so a matching
distinct \(B\)-pair contributes one to \(Q\).  For sum \(d\), the
\(C\)-pair \(\{0,d\}\) is distinct.  A distinct matching \(B\)-pair
contributes two, while the repeated midpoint \(\{d/2,d/2\}\), when
integral and contained in \(B\), contributes one.  Pair-sum uniqueness
prevents the distinct and midpoint alternatives from coexisting.  Hence

\[
Q\le1+2+1=4.
\tag{11}
\]

### 3.3 The range \(b\ge4\)

By (6) and (11),

\[
E+Q\le6.
\]

For \(b\ge4\),

\[
\binom b2+1+R\ge\binom42+1=7.
\]

Thus (8) holds, with at least one unit of slack, throughout this range.

### 3.4 The three small values of \(b\)

For \(b=1\), \(\Delta B\) is empty and hence \(R=2\).  Also \(E\le1\)
and \(Q\le1\), so (8) holds.

For \(b=2\), there is only one distinct \(B\)-pair.  It can match at
most one of the three sums (10).  It contributes at most two, and a
midpoint contribution cannot coexist with a distinct sum-\(d\) match.
Thus \(Q\le2\).  A violation of (8) can only have one of the following
forms.

* If \(R=0\), it needs \(E+Q\ge3\).  The case \(E=2\) forces
  \(B=\{-d,2d\}\), whose sole difference is \(3d\); all four mixed
  queries have length \(d\) or \(2d\), so in fact \(R=4\).  If \(E=1\),
  then \(Q=2\) would require either a distinct \(B\)-pair of sum \(d\),
  which supplies the other exterior point, or a midpoint together with a
  pair of sum \(0\) or \(2d\).  With exterior point \(-d\), these latter
  sums require the other point to be \(d\) or \(3d\), neither a midpoint;
  the case of exterior point \(2d\) is the reflection.  Hence this form is
  impossible.

* If \(R=1\), a violation needs \(E=Q=2\).  Again \(E=2\) forces
  \(B=\{-d,2d\}\) and therefore \(R=4\), a contradiction.

For \(R\ge2\), the right side of (8) is at least four, while
\(E+Q\le4\).  This proves the case \(b=2\).

For \(b=3\), first note that \(Q\le3\).  The only way the crude maximum
four in (11) could occur would use distinct \(B\)-pairs of all three sums
\(0,d,2d\).  These would be the three pair sums of the three \(B\)-marks.
Recovering the marks from those sums gives, in some order,

\[
-\frac d2,\qquad \frac d2,\qquad \frac{3d}2,
\]

which is a three-term progression and hence is not Golomb.  A midpoint
sum-\(d\) match cannot coexist with a distinct sum-\(d\) match, so it
does not create another four-unit case.

Now (8) can fail only if \(R=0,E=2,Q=3\).  The condition \(E=2\) places
\(-d,2d\) in \(B\), and this pair already has sum \(d\), contributing
two to \(Q\).  To reach \(Q=3\), the third mark \(t\) must make a pair
of sum \(0\) or \(2d\).  Disjointness excludes the solutions \(t=d\)
and \(t=0\), leaving

\[
t=-2d\quad\hbox{or}\quad t=3d.
\tag{12}
\]

If \(t=-2d\), the mixed query from \(t\) to the anchor \(0\) has length
\(2d\), whereas

\[
\Delta B=\{d,3d,4d\}.
\]

If \(t=3d\), the mixed query from \(t\) to the anchor \(d\) again has
length \(2d\), with the same difference set.  In either case \(R\ge1\),
contrary to the only possible failure.  This completes the proof of (8)
and hence of (3).

### 3.5 Why the supplied \(4+4\) numerical excess is not proper

For

\[
B=\{0,2,5,6\},\qquad C=\{1,3,4,8\},
\tag{13}
\]

the mixed-length inventory is

\[
\begin{array}{c|rrrrrrrr}
j&1&2&3&4&5&6&7&8\\ \hline
x_j&2&2&2&1&0&1&0&1\\
y_j&2&2&1&1&1&0&0&0
\end{array}
\]

and the two within-class difference supports are respectively
\(\{1,2,3,4,5,6\}\) and \(\{1,2,3,4,5,7\}\).  Therefore

\[
N=29,\qquad Q=11,\qquad M=28,
\]

so the proposed budget fails numerically by twelve.

However, the \(B\)-triple

\[
0<5<6,\qquad 0+6-5=1\in C,
\]

forces the mixed cell \(z(6,1)\) to color \(B\).  The \(C\)-triple

\[
1<3<8,\qquad 1+8-3=6\in B,
\]

forces the same cell \(z(6,1)\) to color \(C\).  These are opposite unit
constraints in the complete mixed-cell system.  Hence (13) has no proper
weak extension.

This explains this particular excess through actual constraints, but it
does not give an aggregate charge for all excess configurations.

## 4. Scope and remaining gap

| Scope | Joint budget status | Role of properness | Evidence |
|---|---:|---|---|
| \(\min(|B|,|C|)\le2\) | proved | not needed | Sections 3.1--3.4 |
| supplied \(4+4\) excess pair | numerical inequality fails, but no extension | opposite units collide at \(z(6,1)\) | Section 3.5 |
| \(|B|,|C|\ge3\) with an actual proper weak extension | undecided | a global unit/binary/ternary charge is still missing | no claim |

The first diagonal sizes in which properness could be essential to (1)
are therefore \(3+3\).  The two-anchor normal form cannot supply that
properness-specific mechanism because it satisfies (1) before its coloring
constraints are imposed.

The bounded inequality is proved when \(\min(|B|,|C|)\le2\). The case
of arbitrary actual proper weak triangles remains open; no general
weak-source theorem or new Ramsey consequence is asserted.
