# Higher-fiber / span dependency map (0045)

This compact local map records the strongest already-derived ingredients for a
proper two-colored strict source \(V(A)\), with \(A\subseteq[0,L]\),
\(L\le99994\). It is a dependency map only; no derivation is recomputed.

## 1. Actual fibers and the higher-cube identities

For \(d>0\), set
\[
 F_d=A\cap(A-d),\qquad r_d=|F_d|,
 \qquad T(A)=\sum_d {r_d\choose2}.
\]
The inherited weak coloring of \(F_d\) has its **actual** signed diagonal
partition \(F_d=B_d\sqcup C_d\), with both classes Golomb. The positive
cube counts satisfy
\[
 K_2(A)=T(A),\qquad K_3(A)=\sum_{d>0}T(F_d),
 \tag{1}
\]
where, explicitly,
\[
 T(F_d)=\sum_{h>0}{|F_d\cap(F_d-h)|\choose2}.
 \tag{2}
\]
Thus an upper bound on the actual higher-fiber overlaps
\(q_{d,h}=|F_d\cap(F_d-h)|\) directly bounds the corresponding contribution
to \(K_3\) through (2); it is not interchangeable with a bound only on
\(r_d\).

The universal two-Golomb consequence is
\[
 K_3(A)\le2T(A).
 \tag{3}
\]
Writing \(\rho_d=|\Delta B_d\cap\Delta C_d|\) and \(R(A)=\sum_d\rho_d\),
the stronger color-retaining defect identity from
`LOW_SHARED_SUPPORT_WEAK_ENERGY_0044.md` is
\[
 K_3(A)=T(A)+4R(A)+\sum_d\nu_d-\sum_d H_d,
 \qquad 0\le\nu_d\le\rho_d,\quad H_d\ge0,
 \tag{4}
\]
and hence
\[
 K_3(A)\le\min\{2T(A),\ T(A)+5R(A)\}.
 \tag{5}
\]
The actual proper three-cube construction with \(\rho_d=0\) but
\(K_3>0\) remains the recorded reason that \(R=0\) cannot be treated as
cube avoidance.

## 2. Span-sensitive inequalities already available

Since \(\operatorname{span}(F_d)\le L-d\), the saved fourth-fiber-moment
inequality is
\[
 \sum_{d=1}^{L}\frac{r_d^4}{2(L-d)+1}
 \le\sum_d E(F_d)
 \le 6\sum_d r_d^2-5\sum_d r_d
 =M+12T(A),\qquad M={|A|\choose2}.
 \tag{6}
\]
This is the strongest existing decreasing-span aggregate bound on the full
actual fibers. It can be paired with an overlap cap through (2), but neither
(2) nor (6) supplies such a cap.

For a whole-source window length \(t\),
\[
 K_j^{(t)}(A)=\sum_u K_j(A\cap[u,u+t-1])
\]
weights each positive \(j\)-cube by \((t-\sum h_i)_+\). The existing local
relations are
\[
 K_3^{(t)}(A)\le2K_2^{(t)}(A),
 \qquad
 K_3^{(t)}(A)\le K_2^{(t)}(A)+5R^{(t)}(A).
 \tag{7}
\]
Here \(R^{(t)}\) is not an unweighted multiple of \(R\): it counts actual
colored shared-pair incidences with their whole source-span weight
\((t-d-h-p)_+\).

## 3. Short-window signed variance: retained term and exact gap

For the restrictions \(A_u=A\cap[u,u+t-1]\), let
\(s_{u,d}=|B_{u,d}|-|C_{u,d}|\) be the signed size imbalance of the
**restricted actual fiber**. If the interlaced reflected-middle seeds have
fiber step \(d\) and internal separation \(h\), their exact window inequality
is
\[
 8\sum_{\rm seeds}(t-d-2h)_+
 +\sum_u\sum_d s_{u,d}^{,2}
 \le2K_2^{(t)}(A)+K_1^{(t)}(A),
 \tag{8}
\]
and
\[
 2\sum_{\rm seeds}(t-d-2h)_+\le K_3^{(t)}(A).
 \tag{9}
\]
The term that remains unbounded is precisely
\[
 \boxed{\ \sum_u\sum_d s_{u,d}^{,2}\ },
 \tag{10}
\]
the short-window variance of the signed *actual* fiber color classes.
It cannot be replaced by an arbitrarily direction-weighted copy of the
full-fiber \(\sum_d(|B_d|-|C_d|)^2\). In the complementary small-shared
support branch, the likewise unbounded retained color resource is
\(R^{(t)}(A)\) in (7); no local note bounds it from \(L\le99994\), \(r_d\),
or the uncolored overlaps alone.

## 4. Exact dependency for a finite-span attack

An upper estimate on \(q_{d,h}\) could enter only through (2), hence control
\(K_3\) or its windowed form. To turn that into a source-size conclusion at
\(L\le99994\), the saved route still needs a simultaneous estimate involving
the actual colors: either an upper bound on (10), a bound on \(R^{(t)}\), or a
mechanism forcing enough interlaced seeds for (8) to pay. The current
higher-fiber moment and span formulas alone do not provide that missing
color-sensitive estimate; generic cube-free density is therefore not a
sufficient replacement.

