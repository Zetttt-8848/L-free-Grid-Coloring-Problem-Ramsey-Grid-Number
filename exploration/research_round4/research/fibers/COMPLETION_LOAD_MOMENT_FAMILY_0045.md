# Completion-load moment of the reflected Golomb family

Let \(C\) be a nonnegative Golomb set containing \(0\), write
\[
r=|C|,\qquad L=\max C,
\]
choose \(s>4L\), and put
\[
A=C\sqcup(s-C).
\]
Use the proper coloring constructed in
`UNBOUNDED_COMPLETION_LOAD.md`. This note computes its
entire completion-load profile. The completed properness argument is used
as input.

For a cell \(p\in V(A)\), let \(H_p\) be the number of corners whose outer
completion is \(p\) and whose two parallel endpoint cells have equal
color.

## 1. The complete load profile

Every positive difference fiber of \(A\) has size at most two. The coloring
has equal colors on exactly the following size-two fibers:
\[
\{(a,0),(s,s-a)\},
\qquad a\in A\setminus\{0,s\}.                    \tag{1}
\]
Both cells in (1) have color \(0\). Their outer completion is always
\[
Q=(s,0),                                          \tag{2}
\]
since the starts are \(0<s-a\), the corresponding endpoints are \(a<s\),
and the outer cell joins the left start to the right endpoint.

There are
\[
|A|-2=2r-2                                        \tag{3}
\]
fibers in (1). Every other size-two fiber has its two cells colored
differently, and a singleton fiber supplies no pair of parallel endpoint
cells. Therefore neither kind contributes to any \(H_p\).

This proves the exact profile
\[
\boxed{
H_Q=2r-2,\qquad H_p=0\quad(p\ne Q).
}                                                   \tag{4}
\]
Thus there are no secondary loaded outputs hidden outside the distinguished
spanning cell.

## 2. Exact first and second moments

The first moment and second moment are consequently
\[
\sum_{p\in V(A)}H_p=2r-2,                          \tag{5}
\]
\[
\boxed{
\sum_{p\in V(A)}H_p^2=(2r-2)^2=4(r-1)^2.
}                                                   \tag{6}
\]
The source has
\[
M(A)=\binom{2r}{2}=r(2r-1)                        \tag{7}
\]
cells and
\[
T(A)=r(r-1)                                       \tag{8}
\]
corners. Hence
\[
\boxed{
\frac{\sum_pH_p^2}{M(A)}
=\frac{4(r-1)^2}{r(2r-1)}
=2-\frac{6r-4}{r(2r-1)}
<2,
}                                                   \tag{9}
\]
and
\[
\frac{\sum_pH_p^2}{T(A)}
=\frac{4(r-1)}r<4.                                \tag{10}
\]
As \(r\to\infty\), the two ratios tend to \(2\) and \(4\), respectively.

## 3. Consequence for a global moment bound

The absolute second moment grows quadratically because one output carries
linear load. It does not grow faster than the cell count:
\[
\frac{\sum_pH_p^2}{M(A)}\longrightarrow2.          \tag{11}
\]
Thus this family does not obstruct an estimate of the form
\(\sum_pH_p^2\leq K M(A)\) with a universal \(K\). It does show that any
such inequality valid for all proper two-color sources must have
\[
K\geq2                                             \tag{12}
\]
in the asymptotic sense.

The responsible output type is unique: the hull-spanning completion
\(Q=(s,0)\). Its contributing fibers are precisely the \(2r-2\) symmetric
representations whose numerical difference is itself a nonextreme mark of
\(A\). The remaining \(r(r-1)-(2r-2)=(r-1)(r-2)\) size-two fibers carry
opposite endpoint colors and contribute zero to every completion load.
