# The proper weak joint-query budget for three-by-three diagonal classes

Let \(S=B\sqcup C\) be the diagonal partition of a proper two-color weak
triangle, with

\[
|B|=|C|=3.
\]

This note proves the proposed joint budget

\[
\boxed{N+Q\le M=15.}
\tag{1}
\]

The proof first gives a sharp six-mark difference-energy gap.  Any
numerical violation of (1) must then be a six-term arithmetic progression
with one of two diagonal color patterns.  Direct weak-corner implications
rule out both patterns.

## 1. Definitions and claim

Let \(B=\{b_0<b_1<b_2\}\) and \(C=\{c_0<c_1<c_2\}\) be disjoint integer
Golomb sets.  For \(h>0\), put

\[
\beta_h=1_{h\in\Delta B},\qquad
\gamma_h=1_{h\in\Delta C},
\]

\[
x_h=|\{u\in B:u+h\in C\}|,\qquad
y_h=|\{u\in C:u+h\in B\}|,
\]

and

\[
N=\sum_h(\beta_h+\gamma_h)(x_h+y_h),\qquad
Q=\sum_hx_hy_h.
\tag{2}
\]

Here

\[
U=\binom32+\binom32=6,\qquad |B||C|=9,\qquad M=U+9=15.
\tag{3}
\]

The predicate is that the prescribed diagonal colors extend to a proper
coloring of every cell of \(W(S)\).  Translation, positive integral
scaling, reflection, and exchange of \(B,C\) preserve the statement.

## 2. The six-sum inventory for \(Q\)

For a three-mark Golomb set \(D=\{d_0<d_1<d_2\}\), its six unordered
pair sums with repetitions allowed are

\[
2d_0, 2d_1, 2d_2, d_0+d_1, d_0+d_2, d_1+d_2.
\tag{4}
\]

They are all distinct.  Indeed, two different unordered representations
of one sum give two different pairs with the same positive difference;
a distinct representation \(a+b=2m\) gives the repeated difference
\(m-a=b-m\).

Every term counted by \(Q=\sum_hx_hy_h\) is exactly a coincidence of one
\(B\)-sum and one \(C\)-sum.  A distinct-distinct coincidence contributes
two to \(Q\), a distinct-repeated coincidence contributes one, and a
repeated-repeated coincidence would give a common mark and is excluded by
disjointness.  Thus

\[
Q\le6.
\tag{5}
\]

Equivalently, \(Q\) is the number of the six distinct same-class pair
resources used by these sum coincidences: two resources for a
distinct-distinct match and one for a distinct-repeated match.

## 3. A sharp energy gap for six marks

For an arbitrary six-mark integer set \(A=\{a_0<\cdots<a_5\}\), let

\[
r_A(h)=|\{u:u,u+h\in A\}|,\qquad
T(A)=\sum_{h>0}\binom{r_A(h)}2.
\tag{6}
\]

An unordered pair of distinct representations

\[
(u,u+h),\qquad(v,v+h),\qquad u<v,
\]

maps injectively to the three-mark subset

\[
\{u,v,v+h\}.
\tag{7}
\]

The triple recovers \(h=(v+h)-v\) and the omitted endpoint \(u+h\).
Therefore

\[
T(A)\le\binom63=20.
\tag{8}
\]

Equality means that every triple \(u<v<w\) has

\[
u+w-v\in A.
\tag{9}
\]

Taking \(u=a_0,v=a_1,w=a_i\) shows that

\[
a_i-(a_1-a_0)\in A\qquad(1\le i\le5).
\]

Predecessor closure from the minimum now gives

\[
A=\{a_0,a_0+g,\ldots,a_0+5g\},\qquad g=a_1-a_0.
\tag{10}
\]

So equality in (8) occurs exactly for a six-term arithmetic progression.

We also need the strict gap below equality.  Order the nonzero difference
multiplicities as

\[
m_1\ge m_2\ge\cdots.
\]

For any selected set \(D\) of \(k\le5\) positive differences, count its
representations by lower endpoint.  The point \(a_i\) has at most

\[
\min(k,5-i)
\]

selected-difference successors.  Hence

\[
\sum_{j=1}^k m_j
\le\sum_{i=0}^5\min(k,5-i)
=6k-\frac{k(k+1)}2.
\tag{11}
\]

If \(A\) is not an arithmetic progression, these partial-sum bounds
sharpen to

\[
\sum_{j=1}^k m_j\le4,8,11,13,14
\quad\text{for }k=1,2,3,4,5.
\tag{12}
\]

Here are the equality exclusions required for (12).

* \(m_1=5\) makes the five edges of one difference a connected chain on
  all six marks, hence an arithmetic progression.  Thus \(m_1\le4\),
  giving the first two bounds.

* Equality \(m_1+m_2+m_3=12\) forces three multiplicities equal to four
  and equality in (11).  Write \(g_i=a_i-a_{i-1}\).  Equality by lower
  endpoints \(a_2,a_3,a_4\) gives

  \[
  D=\{g_3,g_3+g_4,g_3+g_4+g_5\},
  \]

  while \(g_4,g_5,g_4+g_5\in D\).  If \(g_4\ne g_5\), the latter are
  three distinct elements whose largest is strictly below the largest
  element in the first display, impossible.  Thus \(g_4=g_5=g\), and
  comparison forces \(g_3=g\) and \(D=\{g,2g,3g\}\).  Equality at
  \(a_1\) and then \(a_0\) forces \(g_2=g_1=g\).  Thus this equality case
  is again an arithmetic progression, proving the third bound in (12).

* Equality in (11) for \(k=4\) makes every difference among
  \(a_1,\ldots,a_5\) one of the four selected differences.  A five-mark
  set has at least four positive differences, and equality in that
  elementary bound forces an arithmetic progression: after translating
  its minimum to zero, its four distances from the minimum exhaust the
  difference set, and subtraction by the least positive mark gives
  predecessor closure.  Thus \(a_1,\ldots,a_5\) have a common gap \(g\),
  and their four differences are \(g,2g,3g,4g\).  Equality at \(a_0\)
  requires four of its five forward differences to be exactly these four
  values, forcing \(a_1-a_0=g\).  This proves the fourth bound in (12).

* Equality in (11) for \(k=5\) says that all fifteen pairs use only five
  positive differences.  The same minimum-difference argument makes all
  six marks an arithmetic progression.  This proves the fifth bound.

The total multiplicity is

\[
\sum_jm_j=\binom62=15.
\]

Thus (12) says that the multiplicity sequence of a nonprogression is
majorized by

\[
\((4,4,3,2,1,1)\).
\]

Moving one unit toward an earlier, no-smaller entry can only increase
\(\binom{x}{2}\).  Therefore

\[
T(A)\le2\binom42+\binom32+\binom22=16
\qquad\text{if \(A\) is not an arithmetic progression.}
\tag{13}
\]

Combining (8), (10), and (13) gives the sharp dichotomy

\[
\boxed{T(A)=20\text{ for a six-term progression, and }T(A)\le16
\text{ otherwise}.}
\tag{14}
\]

## 4. Reduction of every possible violation to a progression

Put

\[
\rho=|\Delta B\cap\Delta C|.
\]

The exact mixed-energy decomposition is

\[
T(S)=2\rho+N+Q.
\tag{15}
\]

If \(\rho=0\), the exact supported-query identity gives

\[
N=9-Z
\]

for the number \(Z\ge0\) of mixed queries whose length is in neither
difference support.  Together with \(Q\le U=6\), this gives

\[
N+Q\le15.
\tag{16}
\]

If \(\rho=1\) and \(N+Q\ge16\), then (15) gives \(T(S)\ge18\).  By
(14), \(S\) must be a six-term arithmetic progression.  Section 3.4 below
shows that every partition of such a progression into two Golomb triples
has \(\rho=2\) or \(3\), a contradiction.

If \(\rho=3\), equations (8) and (15) give

\[
N+Q\le20-6=14.
\tag{17}
\]

The only remaining possible violation has \(\rho=2\).  Then
\(N+Q\ge16\) and (15) force

\[
T(S)=20,\qquad N+Q=16.
\tag{18}
\]

Thus \(S\) is a six-term arithmetic progression.

## 5. Complete progression color inventory

Normalize the progression to \(S=\{0,1,2,3,4,5\}\).  Exchange the
classes so that \(0\in B\).  Choosing the other two \(B\)-positions gives
the following complete ten-row table.

\[
\begin{array}{c|c|c}
B&C&\text{status or }\rho\\ \hline
\{0,1,2\}&\{3,4,5\}&B,C\text{ not Golomb}\\
\{0,1,3\}&\{2,4,5\}&3\\
\{0,1,4\}&\{2,3,5\}&2\\
\{0,1,5\}&\{2,3,4\}&C\text{ not Golomb}\\
\{0,2,3\}&\{1,4,5\}&2\\
\{0,2,4\}&\{1,3,5\}&B,C\text{ not Golomb}\\
\{0,2,5\}&\{1,3,4\}&2\\
\{0,3,4\}&\{1,2,5\}&3\\
\{0,3,5\}&\{1,2,4\}&2\\
\{0,4,5\}&\{1,2,3\}&C\text{ not Golomb}
\end{array}
\tag{19}
\]

This proves the assertion used in the \(\rho=1\) case.  Under reflection
and class exchange, the four \(\rho=2\) rows reduce to exactly two normal
forms:

\[
\begin{array}{c|c|c|c}
&B&C&(N,Q)\\ \hline
\mathrm A&\{0,1,4\}&\{2,3,5\}&(12,4)\\
\mathrm B&\{0,2,5\}&\{1,3,4\}&(10,6).
\end{array}
\tag{20}
\]

For completeness, the \(Q\)-matches in form A are

\[
0+4=2+2,\qquad 1+4=2+3,\qquad 3+5=4+4,
\]

with weights \(1,2,1\).  In form B they are

\[
0+2=1+1,quad 0+5=1+4,quad 2+5=3+4,quad 1+3=2+2,
\]

with weights \(1,2,2,1\).  Equation (18) then gives the displayed values
of \(N\).

## 6. Form A contradicts properness

Use the diagonal class names also for their colors.  A strict cell joining
two \(B\)-marks has color \(C\), while one joining two \(C\)-marks has
color \(B\).

In form A, the step-two corner on intervals \([2,4]\) and \([3,5]\) has
its endpoint \([3,5]\) and completion \([2,5]\) both fixed to color \(B\).
It forces

\[
z(4,2)=C.
\tag{21}
\]

The step-two corner on \([0,2]\) and \([2,4]\), whose completion
\([0,4]\) is fixed to \(C\), then forces

\[
z(2,0)=B.
\tag{22}
\]

Similarly, the step-one corner on \([2,3]\) and \([4,5]\) has the first
endpoint and completion \([2,5]\) fixed to \(B\), so

\[
z(5,4)=C.
\tag{23}
\]

The step-one corner on \([0,1]\) and \([4,5]\), with \([0,1]\) fixed to
\(C\), now forces

\[
z(5,0)=B.
\tag{24}
\]

Finally, the step-two corner on \([0,2]\) and \([3,5]\) has colors

\[
z(2,0)=B,\qquad z(5,3)=B,\qquad z(5,0)=B,
\]

where the middle cell joins two \(C\)-marks.  It is monochromatic.  Hence
form A has no proper weak extension.

## 7. Form B contradicts properness

In form B, the step-one corner on \([1,2]\) and \([3,4]\) has its second
endpoint and completion \([1,4]\) fixed to \(B\), and therefore forces

\[
z(2,1)=C.
\tag{25}
\]

The step-one corner on \([0,1]\) and \([1,2]\), with completion
\([0,2]\) fixed to \(C\), forces \(z(1,0)=B\).  The step-one corner on
\([0,1]\) and \([3,4]\), whose second endpoint is fixed to \(B\), then
forces

\[
z(4,0)=C.
\tag{26}
\]

The step-four corner on \([0,4]\) and \([1,5]\), with completion
\([0,5]\) fixed to \(C\), forces

\[
z(5,1)=B.
\tag{27}
\]

Separately, the step-two corner on \([0,2]\) and \([3,5]\) has its first
endpoint and completion \([0,5]\) fixed to \(C\), forcing

\[
z(5,3)=B.
\tag{28}
\]

The step-two corner on \([1,3]\) and \([3,5]\) now consists of

\[
z(3,1)=B,\qquad z(5,3)=B,\qquad z(5,1)=B,
\]

where the first cell joins two \(C\)-marks.  It is monochromatic.  Hence
form B also has no proper weak extension.

Equations (16)--(20) show that these two forms exhaust every numerical
violation, and Sections 3.5--3.6 eliminate both by actual weak-cell
constraints.  This proves (1).

## 8. Scope

The derivation proves that if \(B,C\) are disjoint Golomb triples and
their prescribed diagonal coloring extends to a proper weak coloring of
\(W(B\sqcup C)\), then

\[
N+Q\le15=M.
\]

The uncolored maximum is \(16\), and Sections 6--7 remove its two equality
patterns under properness.  No example attaining \(15\) is claimed here.
This is a weak-fiber result only; it does not assert the joint budget for
larger diagonal classes, an all-source inequality, or a new Ramsey bound.
