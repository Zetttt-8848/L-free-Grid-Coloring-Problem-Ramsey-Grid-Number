# The cross-mass bound with at most two diagonal anchors

Let \(S=B\sqcup C\) be the diagonal partition of a proper weak two-color
source. Thus \(B,C\) are disjoint Golomb sets. Write
\[
b=|B|,\qquad c=|C|,
\]
and use the exact weak-energy decomposition
\[
T(S)=2\rho+N+Q,                                    \tag{1}
\]
where \(\rho=|\Delta B\cap\Delta C|\).

This note proves the bounded cross-mass statement
\[
\boxed{
\min(b,c)\leq2\quad\Longrightarrow\quad
T(S)\leq2bc.
}                                                   \tag{2}
\]
The proof uses only the diagonal Golomb geometry and the completed
two-anchor joint-query budget. Proper weak extendibility adds no further
step in this range.

## 1. Zero or one anchor

The case \(\min(b,c)=0\) is empty. By exchanging the classes, suppose
\(C=\{r\}\). Then \(\rho=0\).

There are \(b\) mixed pairs. Each contributes at most one to \(N\), since
\(\Delta C\) is empty, so
\[
N\leq b.                                           \tag{3}
\]
A contribution to \(Q\) consists of two \(B\)-marks symmetric about the
single anchor \(r\). Distinct contributions use distinct \(B\)-marks;
in particular
\[
Q\leq b.                                           \tag{4}
\]
Equations (1), (3), and (4) give
\[
T(S)=N+Q\leq2b=2bc.                                \tag{5}
\]

## 2. Exact two-anchor form

It remains to take \(c=2\) and \(b\geq2\). Translate so that
\[
C=\{0,d\},\qquad d>0.
\]
For the \(2b\) mixed pairs, let
\[
R=|\{(a,c)\in B\times C:|a-c|\notin\Delta B\}|     \tag{6}
\]
be the number of lengths unsupported by \(B\), and put
\[
E=1_{-d\in B}+1_{2d\in B}.                         \tag{7}
\]
The \(B\)-supported part of \(N\) is \(2b-R\). The only \(C\)-difference
is \(d\), and a mixed pair has length \(d\) only through one of the two
possible exterior marks \(-d,2d\). Hence
\[
\boxed{N=2b-R+E.}                                  \tag{8}
\]
Also
\[
\rho\leq1,\qquad E\leq2.                           \tag{9}
\]

The three unordered anchor multisets have sums \(0,d,2d\). Pair-sum
uniqueness in the Golomb class \(B\) gives
\[
Q\leq1+2+1=4:                                      \tag{10}
\]
the repeated anchor pairs at sums \(0,2d\) contribute at most one each,
and the distinct anchor pair at sum \(d\) contributes at most two.

Substituting (8) into (1) gives the exact reduced target
\[
T(S)=2\rho+2b-R+E+Q.                               \tag{11}
\]

## 3. Four or more marks in the other class

For \(b\geq4\), equations (9)--(11) immediately yield
\[
T(S)\leq2+2b+2+4=2b+8\leq4b=2bc.                  \tag{12}
\]
No relation among the three crude maxima is needed.

## 4. The two small joint cases

The completed two-anchor joint-query theorem gives, in the notation
(6)--(7),
\[
E+Q\leq\binom b2+1+R.                              \tag{13}
\]
For \(b=2\), (13) is \(E+Q\leq2+R\). Therefore
\[
T(S)\leq2+4-R+(2+R)=8=4b.                         \tag{14}
\]
For \(b=3\), (13) is \(E+Q\leq4+R\), and similarly
\[
T(S)\leq2+6-R+(4+R)=12=4b.                        \tag{15}
\]
Together with (12), this proves the two-anchor case for every \(b\geq2\).
If the other class has one mark, Section 1 applies after exchanging the
class names.

## 5. Scope

Combining (5), (12), (14), and (15) proves (2). The result is a theorem
for every disjoint Golomb pair with one class of size at most two; the
existence of a proper weak extension is not used beyond supplying that
diagonal setting.

The argument is specific to two anchors. Its decisive inputs are the
three available anchor pair sums, which give the absolute bound \(Q\leq4\),
and the exact joint estimate (13) for the two small values \(b=2,3\).
For two classes of size at least three, neither bound has a corresponding
constant form, and no general claim \(T(S)\leq2bc\) follows from this note.
