# round3_q4 answer: arm-agreement deficit (AD)

## 1. Verification of identities 1-2 (PROVED)

L(u,d,h), 1 <= d < h, has the horizontal end (u+d,u), the corner (u+h,u) and the vertical end (u+h,u+h-d), with arm length h-d. It lies in V(D) iff u, u+d, u+h-d, u+h are all in D (Lemma 0).
Put l = h-d. Then u ∈ F_l(S_e(d)) iff u, u+l ∈ F_d(D) (which is the same as all four points being in D), chi(u+d,u) = e, and chi(u+l+d,u+l) = chi(u+h,u+h-d) = e. So u ∈ F_l(S_e(d)) iff L(u,d,h) exists and both of its arms have color e. Summing over e and d < h:

    sum_e N_e(h) = #{(u,d) : L(u,d,h) ⊆ V(D), arms agree} <= Lambda(h).

Since z_d(u+l) is the vertical-end color, sum_e r_{S_e(d)}(l) = #{u : u, u+l ∈ F_d(D), z_d(u) = z_d(u+l)}. Both identities are verified.

## 2. Consumer link, with the exact averaged deficit that suffices (PROVED)

**Lemma (prefix form of P).** Take a multiset with w_l copies of each lag l >= 1, and suppose H <= sum_l w_l. Write C_w(λ) = sum_{l<=λ} w_l. Then

    P(H; w) = sum_{λ>=0} max(0, H - C_w(λ)).

*Proof.* Let the H cheapest terms be t_1 <= ... <= t_H. Then sum_k t_k = sum_k #{λ >= 0 : λ < t_k} = sum_{λ>=0} #{k : t_k > λ}. Exactly min(H, C_w(λ)) of the cheapest H terms are <= λ. Hence #{k : t_k > λ} = max(0, H - C_w(λ)). ∎

**Corollary (what suffices).** Suppose that for every λ up to the largest lag used,

    C_w(λ) <= C_{w'}(λ),   with w'_l = (1-δ)·3v_l.

Then P(H_tot; w) >= P(H_tot; w'), because max(0, H - C) is decreasing in C. So the summed rank-neighbour inequality 2P(H_tot;w) + 12Σ_i(c-i)e_{i+1} <= 3L'c(c+1) holds with w replaced by w'. The conclusion is a cap on Σ_e s_e at that main colour and shift.

The hypothesis needed is therefore weaker than a per-lag deficit. It is only a **prefix-averaged deficit**: for every λ,

    Σ_{l<=λ} Σ_e r_{S_e(d)}(l) <= (1-δ) Σ_{l<=λ} 3v_l.

This is a deficit in the lag-l agreement counts of the word z_d, summed over l <= λ. For each fixed d it is a statement about sums over h = d+l of agreement counts. A window-weighted (AD) in the a_h form does **not** directly give prefix domination. One would additionally need (AD) on every initial segment of lags, uniformly in d. The value of δ' (the loss in U_d) as a function of δ is still not computed.

## 3. Density hypotheses cannot yield a counter-family, and give only non-explicit (AD) (PROVED, modulo a cited theorem)

**Cited from memory.** This is the corners theorem (Ajtai–Szemerédi 1974; quantitative versions by Shkredov and others). For every ε > 0 there is N(ε) such that every subset of [0,N)^2 with N >= N(ε) and at least εN^2 elements contains a configuration (x,y), (x+t,y), (x,y+t) with t > 0. The map (x,y) ↦ (x, x+y-?)... More simply, use (x,y) ↦ (x+y, y). It sends {(x,y),(x+t,y),(x,y+t)} to {(x+y,y),(x+y+t,y),(x+y+t,y+t)}, which is a directed L with arm t. So the theorem also holds for directed L's, after rescaling [0,N)^2 into [0,2N)^2, at the cost of a constant factor in ε.

**Proposition.** Fix ρ > 0. Then there is S(ρ) such that no proper ternary source has a D with |D ∩ I| >= ρ|I| on an interval I of length >= S(ρ).

*Proof.* Take D' = D ∩ I with |I| = N. The cells (v,u) with u < v in D' number at least C(ρN, 2) ≈ ρ²N²/2, and they all lie in V(D) ∩ I². One of the three colors covers at least ρ²N²/7 of them once N is large. Apply the corners theorem in its directed-L form to that color class, which is a subset of I² of density >= ρ²/7. For N >= S(ρ) this gives a monochromatic L. Its three cells lie in the color class, hence in V(D), so chi is not proper. ∎

**Consequences.**

- **(a) Task item 3's refutation route is closed.** No family with a fixed density ρ and arbitrarily large spans exists. A counter-family can only be exhibited at bounded span, below S(ρ).
- **(b) (AD) holds vacuously beyond S(ρ).** This is non-explicit (S is of tower or at best quasi-polynomial type) and useless at span 2.2·10^7.
- **(c) The real target is quantitative at a fixed finite scale.** The regime has density 1/4 at span about 2.2·10^7, and proper sources there do exist. Any useful (AD) must exploit near-cap structure, not density alone. The hypothesis to name is near-extremality: r_{S_e(d)}(l) >= (1-η)v_l for the relevant l.

## 4. Attempt at (AD) via the corner-exclusion heuristic (OPEN; partial)

For each pair u < v in D with h = v-u, agreements w_u(d) = c_v(d) occur only in the two non-corner colors. The independent-word heuristic then gives an agreement rate of 2/9. To turn this into a proof one must bound the correlation of the row word w_u with the column word c_v on the non-corner colors.

I found no argument that does this using only the stated inequalities on class sizes and fibers. Line (a) gives per pair only A(u,v) <= |M(u,v)|. Lines (b) and (c) give energy lower bounds for one color, but no deficit for Σ_e N_e. The sparse digit families show that the corner exclusion alone permits agreement rate 1. So any proof must use density or near-cap hypotheses quantitatively.

## Summary

**Proved**
- Identities 1-2.
- The prefix formula for P, and that prefix-averaged agreement deficits suffice for the consumer.
- The density obstruction: there are no proper ternary sources of fixed density at large span. This uses the corners theorem, cited from memory.

**Refuted / closed**
- Item 3's route of a counter-family at fixed density and unbounded span.

**Open**
- (AD) with an explicit δ under a near-cap hypothesis at the finite scale.
- The conversion δ → δ'.
- Whether window-weighted (AD) implies prefix domination.

No claim about R_4 is made.

=== END OF ANSWER round3_q4 ===
