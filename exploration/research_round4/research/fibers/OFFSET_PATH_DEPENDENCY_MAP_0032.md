# Offset-path dependency map (checkpoint 0032)

For a properly colored strict source, write \(M=\binom{|A|}{2}\),
\(F_d=\{x\in A:x+d\in A\}\), and
\(T_H=\sum_{H\le d<2H}\binom{|F_d|}{2}\). These existing notes are band
or selected-fan statements; none states a global logarithmic energy theorem.

## Decreasing cloud paths

[SOURCE_CLOUD_SUMMATION_0019.md](../SOURCE_CLOUD_SUMMATION_0019.md),
Sections 1--2, defines a charge event \((p,d)\) as an aligned,
same-colored pair of child edges, equation (1). Consecutive signed-cloud
offsets \(d_i<d_{i+1}\) have \(g=d_{i+1}-d_i<d_{i+1}\), equation (7).
Each link propagates to \((q_{d_i},g)\), or terminates at a physical
bichromatic aligned child pair, with exact accounting
\[
(k(p)-1)_+=W(p)+P(p)+H(p).\tag{6}
\]
On parent scale \(s\), all propagated occurrences land at scale \(t<s\),
equation (12).

The global obstruction is convergence. In Section 3,
\(P=\sum_\eta\nu_P(\eta)\) and \(H=\sum_\xi\nu_H(\xi)\), equation (9).
A fixed descendant \(\eta=(q,g)\) may have parents
\(p_d=q-(d,d)\), with backward distance \(d\) undetermined, equation (10).
Same-sign predecessor anchors are Sidon, but this gives only
\[
\nu_P(\eta)<2\sqrt{2L}+2,\tag{11}
\]
and \(O(\sqrt H)\) on a width-\(H\) band. The stated unresolved inequality
is (13):
\[
\sum_\eta(\nu_P(\eta)-1)_++\sum_\xi(\nu_H(\xi)-1)_+
\le \text{a linear budget in physical cells or corners}.
\]
Descent prevents cycles but not many higher-scale anchors converging on one
smaller event or terminal token.

## Active-band completion routing

[SOURCE_SINGLE_BAND_ROUTING_0020.md](../SOURCE_SINGLE_BAND_ROUTING_0020.md),
Sections 1--3, proves \(T_H\le2A_H+R_H/2\), equation (3), and
\(A_H=\sum_QH_Q\), equation (5). A collision of active offsets \(d<e\)
has \(\delta=e-d<H\), equation (7), and forces a lower-gap bichromatic
fiber pair only when \(u+\delta\in A\) or \(v-\delta\in A\), equations
(8)--(10). The exact aggregate bound is
\[
\tfrac12(A_H^2/M-A_H)
\le2\mathcal B_H^{<H}+\sum_{\delta<H}r_A(\delta)(|A|-r_A(\delta))^2.
\tag{13}
\]
A target has safe multiplicity \(2r_A(\delta)\), not one, because left and
right closure charges can overlap.

Section 4 gives \(\{0,H,2H-1,3H-1\}\): two repeated active differences
share a completion while both closure translates are absent, equations
(16)--(17). The lower-offset inner cell is in neither required source
corner. Thus one charge per collision leaves exactly the final summand in
(13).

## Two-corner completion support and its cut target

[SOURCE_BAND_BOUNDARY_COUPLING_0021.md](../SOURCE_BAND_BOUNDARY_COUPLING_0021.md),
Sections 1--2, retains the shared completion sign:
\[
(\mathcal K_Hz)_Q=-z(Q)H_Q.\tag{5}
\]
The completion-incidence graph has exactly \(2T_H\) distinct physical
edges, equation (9), and its actual-color cut obeys
\[
C_H=T_H+A_H,\qquad2T_H-C_H=T_H-A_H.\tag{10}
\]
Its edges orient from a larger-offset completion to a smaller-offset active
endpoint (Section 4). Section 5 records why this is not a per-cell budget:
an ordered acyclic graph may have a high-degree completion star, all of
whose boundary neighbors have the opposite color. Pair-edge uniqueness and
no-alternating boundaries do not bound this star. The exact missing target
for \(T_H\le7M/5\) is
\[
C_H\le\frac{21}{10}M-\frac14R_H,\tag{16}
\]
or the stronger uniform \(C_H\le37M/20\), equation (17).

## Status of a logarithmic energy proposal

The notes read here do **not** contain an attempted or refuted theorem
\[
T\le\frac{\log_2L}{2}M.
\]
CHECKPOINT_0017, Section 1, records a relevant calibration from
`fibers/DYADIC_CHARGING_0016.md`: a properly colored dilated five-mark
interval has \(T_H=3M/5\). This refutes the stronger raw per-band target
\(T_H\le M/2\), but does not refute the displayed global logarithmic form,
which needs a separate aggregation argument.

The exact recorded obstacle to a one-charge-per-cell-per-scale proof is
twofold: convergent parent fans have only square-root, not constant, fan-in;
and boundary-open completion collisions need not create a forced lower-scale
corner. No universal conclusion is asserted.
