# Reflected-hole multiplicity input map (0040)

This is a six-file project-local retrieval map; it does not recompute the cited bounds.

## Positive fan support graph

`POSITIVE_FAN_DIFFERENCE_BUDGET_0039.md` is the direct input. With \(P_x\) the positive anchored fan and \(D_x=\Delta P_x\cap B\cap(B-x)\), it records \(D_x\subseteq Y_x\), so \(D_x\) is Golomb and also sum-free. The support graph \(\Gamma_x\) on \(P_x\), whose edges have gaps in \(D_x\), is triangle-free. Its stronger local statement is codegree at most two: at most one interior and one exterior common neighbor for any two vertices.

For \(t=|P_x|\), \(j=|D_x|=|E(\Gamma_x)|\), the recorded bound is
\[
j\le {t\over4}\bigl(1+\sqrt{8t-7}\bigr).
\]
It yields the stated local defect \({t\choose2}-j\). No globally sharp coefficient is claimed. The note does state that codegree two and a monotone four-cycle occur in a literal proper source: \(P_x=\{1000,1001,1011,1111\}\), \(D_x=\{1,10,100,111\}\), with \(\Gamma_x\) exactly a four-cycle. Thus neither codegree one nor four-cycle-freeness is available universally.

## Reflected triples and fixed-target holes

`fibers/OPEN_REFLECTION_COLLISIONS_0034.md` uses the triple reflection \(w=a+c-b\). At fixed target \(q=(v,u)\) and lower offset \(d\), a column-open transport has the stated hole \(u+d\notin A\), while a row-open transport has \(v-d\notin A\). The Golomb condition gives at most one seed triple for fixed \((q,d)\), and an open transport cannot coexist with an ordinary fan at that same offset.

For column-/row-open offset sets \(C_q,R_q\), ordinary monochromatic fan count \(H_q\), and actual row/column sign counts \(N_v^\pm,N_u^\pm\), its two injections give
\[
{ |C_q|\choose2}H_q\le {N_v^s\choose2}N_v^{-s},\qquad
{ |R_q|\choose2}H_q\le {N_u^s\choose2}N_u^{-s}.
\]
These are the existing shared-reflected-hole collision bounds. They are target-local; they do not sum \(\mu_B(r)=\#\{a<b<c\in B:r=a+c-b\}\) across anchors.

## Two-endpoint ledger

`fibers/TWO_ENDPOINT_REVERSAL_LEDGER_0039.md` classifies a four-mark parallelogram at both endpoints and records the exact identity
\[
\mathcal R-\mathcal P=2X+Z,
\]
with \(X\) pure reversed rectangles and \(Z\) mixed \(R/M\) rectangles. Each pure rectangle injects into two signed-fiber-pair inventories:
\[
X\le\min\{|\mathcal G_>|,|\mathcal G_<|\},\qquad 2X\le|\mathcal G_>|+|\mathcal G_<|.
\]
The note states the remaining gap: aggregate offset-gap labels can still have corner scale, and the \(Z\) term has no analogous two-fiber charge.

## Existing global multiplicity bottleneck

`fibers/SOURCE_CLOUD_SUMMATION_0019.md` turns repeated charge offsets into descending propagation or terminal bichromatic tokens, with exact identity \(R=W+P+H\). Its unresolved terms are the convergence multiplicities \(\nu_P,\nu_H\): many translated parent clouds can reach one descendant event/token. Same-sign predecessors are only Sidon, yielding the recorded \(O(\sqrt L)\) fan-in rather than a constant. This is the closest existing global version of the new multiplicity issue.

## Translate energy, not one-point extension

`PAIRED_SOURCE_ENERGY_0036.md` contains the collision-retaining calculation for a Golomb set and a disjoint translate, \(P=B\cup(B+d)\):
\[
E(P)=6E(B)+8C_d(B)+2C_{2d}(B),\qquad C_h(B)=\sum_t r_B(t)r_B(t+h).
\]
It records \(E(B)=2b^2-b\), \(C_h(B)\le b^2+b-2\), and hence \(E(P)\le22b^2-12b-4\). This permits shifted-difference collisions but concerns two translates, not \(B\cup\{r\}\), and gives no bound for \(\mu_B(r)\).

## Local primary-source availability and scope

No named theorem extending a Sidon/Golomb set by one mark, nor a local primary-source file for such a theorem, appears in the six read files. A project-local filename/text search for “extend Golomb/Sidon” and “one point/add a point” returned no match. Existing inputs therefore give fixed-target uniqueness, local support-graph capacity, two-endpoint injections, and an unresolved convergent-fan bottleneck; they do not yet bound total reflected-hole multiplicity across all anchors.
