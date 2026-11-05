# Iterating a positive fan through its supported differences

Normalize the physical anchor to \(0\), put
\(B=A\setminus\{0\}\), and write

\[
f(t)=z(t,0).
\tag{1}
\]

Fix \(x\in B\), put \(s=f(x)\), and define the actual positive fiber
class

\[
P_x=\{y\in B:x+y\in B,\ z(x+y,y)=s\}.
\tag{2}
\]

The anchored corner at \(0\) shows that

\[
f(x+y)=-s\qquad(y\in P_x).
\tag{3}
\]

Also, \(P_x\cup\{0\}\) is Golomb.  The issue here is what happens when
differences between labels of \(P_x\) are themselves supported addition
labels at \(x\).

## 1. One supported \(P_x\)-pair

We use the following stated positive-pair transport, including its
physical cells.

Let \(p<q\) lie in \(P_x\), and put \(h=q-p\).  Suppose

\[
h\in B,\qquad x+h\in B.
\tag{4}
\]

The two offset-\(x\) cells

\[
(x+p,p),\qquad(x+q,q)
\]

have color \(s\).  Their positive corner forces

\[
z(x+q,p)=-s.
\tag{5}
\]

Since \(q\in P_x\), equation (3) gives \(f(x+q)=-s\).  Now

\[
(x+h,0),\qquad(x+q,0),\qquad(x+q,p)
\tag{6}
\]

is a positive corner of step \(p\), because
\(x+q-(x+h)=p\).  Its last two cells have color \(-s\), and hence

\[
\boxed{f(x+h)=s.}
\tag{7}
\]

Thus every supported difference of \(P_x\) belongs to the same-color
anchored fan

\[
Y_x=\{h\in B:x+h\in B,\ f(x+h)=f(x)\}.
\tag{8}
\]

## 2. The supported differences are sum-free

Define

\[
D_x=\Delta P_x\cap B\cap(B-x)
   =\{h\in\Delta P_x:h,x+h\in B\}.
\tag{9}
\]

Here \(B-x=\{h:x+h\in B\}\).

**Theorem.**  The set \(D_x\) is sum-free:

\[
\boxed{h,d\in D_x\quad\Longrightarrow\quad h+d\notin D_x.}
\tag{10}
\]

The statement includes \(h=d\), so \(h,2h\) cannot both lie in \(D_x\).

**Proof.**  Suppose instead that

\[
h,d,h+d\in D_x.
\tag{11}
\]

Applying (7) to the \(P_x\)-pairs realizing these three differences
gives

\[
f(x+h)=f(x+d)=f(x+h+d)=s.
\tag{12}
\]

The two labels \(h<h+d\) therefore lie in \(Y_x\).  The anchored
corners

\[
(x,0),(x+h,0),(x+h,h)
\]

and

\[
(x,0),(x+h+d,0),(x+h+d,h+d)
\]

force

\[
z(x+h,h)=z(x+h+d,h+d)=-s.
\tag{13}
\]

These are two cells on offset \(x\).  Their positive corner of step
\(d\) forces

\[
z(x+h+d,h)=s.
\tag{14}
\]

Finally,

\[
(x+d,0),\qquad(x+h+d,0),\qquad(x+h+d,h)
\tag{15}
\]

is a positive corner of step \(h\).  Its last two cells have color
\(s\), by (12) and (14), so it forces

\[
f(x+d)=-s.
\tag{16}
\]

This contradicts the middle equality in (12).  Every cited row and
column is supported by (9) and the relevant \(P_x\)-pairs, and every
step is positive.  \(\square\)

This is the desired difference-of-differences cancellation.  If
\(h<h'\) are supported \(P_x\)-differences, then \(h'-h\) cannot also
be a supported \(P_x\)-difference.

## 3. A three-label version

There is a particularly short forbidden motif.  Let

\[
p<q<r,\qquad p,q,r\in P_x,
\]

and suppose all three pairwise gaps

\[
q-p,\qquad r-q,\qquad r-p
\tag{17}
\]

belong to \(B\cap(B-x)\).  Set

\[
h=q-p,\qquad d=r-q.
\]

Then (17) says \(h,d,h+d\in D_x\), contrary to (10).  Equivalently,
the graph on \(P_x\) joining two labels when their difference belongs
to \(B\cap(B-x)\) is triangle-free.

This uses only three \(P_x\)-labels.  A four-label configuration gives
the same contradiction whenever two of its supported pair differences
are \(h<h'\) and another supported pair difference is \(h'-h\).

## 4. Exact scope and remaining gap

The theorem constrains precisely

\[
\Delta P_x\cap B\cap(B-x).
\]

A difference escapes the iteration if the difference label itself is
absent from \(B\), or if its addition target \(x+h\) is absent.  Even
when every difference is supported, sum-free subsets of an interval can
still have size proportional to the span, and the sets \(D_x\) for
different \(x\) may overlap without any injectivity asserted here.

Thus (10) is a new actual-color restriction on the supported part of a
positive fan, but it does not by itself give a linear global arc budget.
Such a budget would still require paying the two support defects or
coupling the sum-free sets belonging to different anchors.
