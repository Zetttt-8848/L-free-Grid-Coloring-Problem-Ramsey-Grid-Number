# Short progression factors: an unconditional single-band bound

## Setup and result

Let \(B\subset\mathbb Z\) be a finite Golomb set, put \(m=|B|\), and write
\[
S=\max B-\min B.
\]
Fix \(h>2S\), let \(q\in\{2,3,4\}\), put \(n=q+1\), and form
\[
A=B+\{0,h,2h,\ldots,qh\}.
\]
For \(d>0\), write
\[
r_A(d)=|\{a\in A:a+d\in A\}|,
\qquad
T_K(A)=\sum_{K\le d<2K}\binom{r_A(d)}2.
\]

**Proposition.** For every integer \(K\ge1\),
\[
T_K(A)\le \frac75\binom{|A|}{2}.
\]
Thus the desired \(D(7/5)\) band inequality holds for every such short-progression extension, whether or not its source triangle admits a proper two-coloring. In particular it holds throughout the properly colorable subclass.

The proof retains the pure-progression fibers (the loops from the \(B\)-coordinate viewpoint) and all mixed fibers. The useful point is that no carry separates their supports into short clusters, while one dyadic interval can meet only a tightly prescribed part of those clusters.

## Complete difference-fiber classification

Translate \(B\) so that \(B\subset[0,S]\). Every ordered difference in \(A\) has the form
\[
d=kh+\delta,
\qquad -q\le k\le q,
\qquad \delta=b'-b,quad b,b'\in B.
\]
Because \(|\delta|\le S<h/2\), this representation is unique once \(d>0\) is put in the following types.

1. **Fine fibers:** \(k=0\), \(\delta>0\). Since \(B\) is Golomb, \(\delta\) comes from one unordered pair of marks. That pair may be placed in any of the \(n\) layers, so
   \[
   r_A(\delta)=n.
   \]
   There are \(\binom m2\) such difference values.

2. **Pure progression fibers:** \(1\le k\le q\), \(\delta=0\). One chooses a mark of \(B\) and a starting layer among \(n-k\) possibilities, hence
   \[
   r_A(kh)=m(n-k).
   \]

3. **Mixed fibers:** \(1\le k\le q\), \(\delta\ne0\). The signed difference \(\delta\) determines a unique ordered pair of distinct marks of \(B\). Its layer start has \(n-k\) choices, so
   \[
   r_A(kh+\delta)=n-k.
   \]
   At each fixed \(k\) there are \(m(m-1)\) signed values of \(\delta\).

These are all fibers. In corner language, choosing two representations of the same difference gives all corner types: fine/fine corners inside two layers; pure/pure corners along one vertical progression over two base marks or two layer starts; and mixed/mixed corners joining the same ordered base pair at two layer starts. Uniqueness of the decomposition forbids a corner whose two legs come from different listed types.

It is convenient to record the total energy of each complete block:
\[
F=\binom m2\binom n2,
\qquad
P_k=\binom{m(n-k)}2,
\qquad
X_k=m(m-1)\binom{n-k}{2}.
\]
Here \(F\) is the contribution of all fine fibers, \(P_k\) that of the single pure fiber \(kh\), and \(X_k\) that of all mixed fibers at level \(k\). We set \(P_k=X_k=0\) for \(k>q\).

## What one dyadic band can contain

The fine differences lie in \((0,S]\). The level-\(k\) mixed and pure differences lie in the cluster
\[
J_k=[kh-S,kh+S].
\]
Let \(I_K=[K,2K)\). If \(I_K\) contains no pure multiple \(kh\), then the coarse bound
\[
T_K(A)\le F+\sum_{k=1}^q X_k
\tag{1}
\]
is enough.

Otherwise let \(ph\) be the least pure multiple in \(I_K\). Since \(K\le ph<2K\), the following support restrictions are immediate from \(h>2S\).

- If \(p=1\), then \(h/2<K\le h\). Fine differences are excluded; clusters \(J_k\), \(k\ge3\), lie above \(2K\); and at level \(2\) only the negative signed differences \(2h+\delta\), \(\delta<0\), can enter. The two signs occur in equal numbers and have equal fiber sizes. Therefore
  \[
  T_K(A)\le P_1+X_1+\frac12X_2.
  \tag{2}
  \]

- If \(p=2\), then \(h<K\le2h\). Fine differences are excluded, at level \(1\) only positive signed differences can enter, and the pure level \(4\) is excluded by the open upper endpoint. Hence
  \[
  T_K(A)\le P_2+P_3+\frac12X_1+X_2+X_3.
  \tag{3}
  \]

- If \(p=3\), then \(K>2h\), so levels \(0\) and \(1\) are excluded. Also \(6h\notin I_K\), and the only potentially present complete levels are \(2,3,4\). Thus
  \[
  T_K(A)\le P_3+P_4+X_2+X_3.
  \tag{4}
  \]

- If \(p=4\), then \(K>3h\). Only the upper side of level \(3\) can accompany the pure level \(4\), giving the safe bound
  \[
  T_K(A)\le P_4+X_3.
  \tag{5}
  \]

The estimates deliberately allow more of a cluster than a given interval may actually contain. They are therefore uniform in the internal placement of the signed differences of \(B\).

## Evaluation for \(q=2,3,4\)

Substitution into (1)--(5) gives the following upper bounds. Empty cases and terms with index greater than \(q\) are omitted.

\[
\begin{array}{c|c|c}
q & \text{position of the least pure multiple} & \text{upper bound for }T_K(A)\\ \hline
2 & \text{none} & \frac52m(m-1)\\
  & h & 3m^2-2m\\
  & 2h & m^2-m\\ \hline
3 & \text{none} & 7m(m-1)\\
  & h & 8m^2-5m\\
  & 2h & 5m^2-4m\\
  & 3h & \frac32m(m-1)\\ \hline
4 & \text{none} & 15m(m-1)\\
  & h & \frac{31m^2-19m}{2}\\
  & 2h & \frac{27m^2-19m}{2}\\
  & 3h & \frac{13m^2-11m}{2}\\
  & 4h & \frac32m(m-1)
\end{array}
\]

Since \(|A|=mn\), the target is
\[
\frac75\binom{mn}{2}=\frac7{10}(m^2n^2-mn).
\]
Every entry in the table is below this target. The largest table entry in each row is the \(p=1\) entry, and the respective target margins are
\[
\begin{array}{c|c}
q & \frac75\binom{m(q+1)}2-\text{the }p=1\text{ bound}\\ \hline
2 & \frac{33m^2-m}{10}\\
3 & \frac{16m^2+11m}{5}\\
4 & 2m^2+6m.
\end{array}
\]
They are positive for every \(m\ge1\), proving the proposition.

## Scope

The short arithmetic factor does not create a new obstruction at lengths three through five once its step is more than twice the base span. More strongly, its complete additive energy already obeys the \(7/5\) single-band bound before any source colors or proper-corner identities are imposed. The result makes no assertion that these sources are properly colorable, and it does not address shorter-step extensions where neighboring clusters overlap and the no-carry classification fails.

