# Two-sided color identity map (0039)

This is a project-local dependency map of eight directly relevant notes.  It records their stated identities and examples without recomputing coefficients or reviewing their proofs.

## Common source and sign notation

For a finite integer source \(A\), let \(V=T(A)=\{(v,u):u<v,\ u,v\in A\}\), and encode the two strict-source colors by \(z_q\in\{-1,+1\}\).  For an offset \(d>0\), the cells in that offset form the diagonal line \(V_d=\{(u+d,u):u\in F_d\}\), where \(F_d=A\cap(A-d)\), \(r_d=|F_d|\), and \(s_d=\sum_{q\in V_d}z_q\).  The complete corner count is
\[
 T(A)=\sum_{d>0}{r_d\choose2}.
\]
This is the shared input for the completion operator, support correlations, and the three-direction cut budget.

## 1. Completion operator and the signed global matrix identity

`SIGNED_COMPLETION.md` defines, for \(q=(v,u)\), the inner end-cap distances
\[
D_q=\{d:0<d<v-u,\ u+d,v-d\in A\},
\]
and the lower-span operator
\[
(Kz)_q={1\over2}\sum_{d\in D_q}\bigl(z_{(u+d,u)}+z_{(v,v-d)}\bigr).
\]
Ordering cells by span makes \(K\) strictly triangular and nilpotent.  If \(H_q\) counts equal-sign end-cap pairs completing at \(q\), its exact properness identity is
\[
H_q=-z_q(Kz)_q=|(Kz)_q|.
\]
Thus same-sign horizontal/vertical end-cap pairs are retained at their common output, rather than counted separately.

Summing these local identities with signed offset-fiber counts gives
\[
4z^TKz+\sum_d s_d^2=2M-\sum_d r_d^2,\qquad M=|V|.
\]
With \(F\) the offset-line incidence matrix and
\[
Q=F^TF+2(K+K^T),
\]
this becomes \(z^TQz=2M-\sum_d r_d^2\).  Hence the note records the sufficient spectral obstruction
\[
\lambda_{\min}(Q)>2-\frac{\sum_d r_d^2}{M}.
\]

**Closed limitation.** For interval sources \(A=\{0,\ldots,m-1\}\), the note identifies \(Q\) also as the combined offset-diagonal, row, and column incidence form minus \(2I\).  A displayed six-cell alternating vector gives \(\lambda_{\min}(Q)=-2\) for \(m\ge5\).  Therefore the unweighted criterion does not detect the known noncolorable \(m=6\) interval, although it does detect the stated obstruction from \(m=7\).  This limits that unweighted spectral test, not the pointwise identity.

## 2. Signed support correlations and their quadratic cloud form

`SUPPORT_CORRELATIONS.md` splits each \(F_d\) into \(F_d^\epsilon\) and defines sign supports \(U_\epsilon=\{h:F_h^\epsilon\ne\varnothing\}\).  For \(u<v\in F_d^\epsilon\), \(h=v-u\), properness supplies a same-sign supporting cell at offset \(h\) (at start \(u\) or \(u+d\)) and an opposite-sign completion at offset \(d+h\).  Its retained cardinality consequence is
\[
{r_d^\epsilon\choose2}\le
\sum_{h>0}{\bf1}_{h\in U_\epsilon}{\bf1}_{h+d\in U_{-\epsilon}}.
\]
Writing \(s_h={\bf1}_{U_+}(h)+{\bf1}_{U_-}(h)\) and
\(t_h={\bf1}_{U_+}(h)-{\bf1}_{U_-}(h)\), the actual opposite-sign overlap is exactly
\[
\frac12\sum_{h>0}(s_hs_{h+d}-t_ht_{h+d}).
\]
The note explicitly identifies the unresolved step as bounding these *coupled* correlations across all \(d\); optimizing them separately discards the shared signs.

`fibers/DERIVATIONS.md` gives the endpoint-cloud version.  For each outer cell \(q\), let \(P_q,M_q\) count its all-\(+\) and all-\(-\) decompositions, and \(S_q=P_q-M_q\).  Properness gives
\[
P_qM_q=0,\qquad H_q=P_q+M_q=|S_q|,
\qquad \|H\|_2^2=\|S\|_2^2.
\]
The same note gives ordered opposite-cloud separation and a two-shift correlation inequality.  It also fixes two sharp local limits: its explicit proper six-mark region \(A=\{1,4,8,14,18,21\}\) shows the \(+1\) in the two-shift overlap bound cannot be removed; at its outer cell \((21,1)\), four same-sign decompositions give \(H_q=|D_q|=4\).  Thus a universal per-output multiplicity deficit is false.

## 3. Exact horizontal/vertical/offset-diagonal budget

`COMPLETION_CUT_BUDGET.md` replaces every proper corner by its three cell pairs.  Unique completion partitions these pair edges into: complete offset-diagonal graphs \(D_d\), and generally incomplete row graphs \(R_v\) and column graphs \(C_u\).  If \(\tau(H)\) is the minimum same-color-edge count in a two-coloring of \(H\), then every proper source obeys exactly the necessary budget
\[
\sum_d\phi(r_d)+\sum_v\tau(R_v)+\sum_u\tau(C_u)\le T(A),
\quad \phi(r)=\left\lfloor{(r-1)^2\over4}\right\rfloor.
\]
Equivalently, the row-plus-column deficit is at most \(\sum_d\lfloor r_d^2/4\rfloor\).  This is the existing literal three-direction identity for the proposed two-sided endpoint budget.  Clique/odd-cycle packings provide lower bounds for individual \(\tau\)'s, but separate minima are expressly a relaxation because the line colorings must arise from one cell matrix.

**Closed example.** On \(A=\{0,1,2,3,4,5\}\), all three line directions are cliques of sizes \(1,\ldots,5\); their integer lower total is \(21>T=20\).  This excludes that source and supplies strength missing from the unweighted spectral test.  The note does not give an all-source row/column lower bound.

## 4. Shared-color matrices: line/block potentials and one closed finite obstruction

`ORDERED_COMPLETION_DUAL_0014.md` refines the preceding budget by including exact line factors and completion blocks simultaneously.  Edge prices split as \(a_f+b_f\le w_{e(f)}\); pair potentials on repeated physical-cell pairs cancel across factor copies.  The stated joint inequality is
\[
\sum_H L_H+\sum_{d<e}K_{d,e}\le\sum_e w_e,
\]
where \(L_H\) and \(K_{d,e}\) are minima over, respectively, one actual line assignment and an allowed proper block assignment with the added pair-product potentials.  Unary cancelling potentials cannot improve this lower bound because of global sign reversal; even pair products are the first retained shared-color coordinates.

The same note gives an exact pair-marginal alternative: either factor distributions have consistent expectations of every repeated physical pair-product, or cancelling pair potentials have positive summed local minimum.  It warns that a solver feasibility/infeasibility status alone is only a development test.

`fibers/PAIR_BLOCK_DERIVATIONS_0014.md` supplies algebraic local bounds for three two-start blocks, including the displayed pair potentials and targets \(B_{1,6}\ge5\), \(B_{1,7}\ge3\), \(B_{2,6}\ge5\).  `EIGHT_MARK_PAIR_OBSTRUCTION_0014.md`, using these and its companion line derivations, closes one finite shared-pair calculation: for \(A=\{0,1,2,3,4,6,7,8\}\), cancelling factor polynomials sum identically to zero while line factors total at least \(-68\) and blocks at least \(72\).  This proves that literal source noncolorable, but is explicitly not an S11-scale estimate.

Finally, `COMPLETION_PROFILE_RIGIDITY_0033.md` gives the descending-offset compatibility formulation: once greater-offset output colors are fixed, an offset fiber must split as a clique plus an independent set, with at most \(r_d+1\) possible partitions.  This preserves the fact that row/column/end-cap constraints reuse the same cell colors; it gives no quantitative nonexistence bound by itself.

## Remaining dependency

The notes do not already derive a uniform two-sided endpoint inequality.  The precise open move is to turn the shared signs in the support correlations, or shared pair products in the line/block factors, into a source-uniform lower bound on the combined row/column (and offset) same-color budget.  The stated counterexamples rule out obtaining that gain from independent offset correlations, a per-output loss, or independently optimized line factors.
