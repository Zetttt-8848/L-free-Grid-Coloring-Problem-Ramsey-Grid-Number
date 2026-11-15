# round4_q1 answer: the prefix-averaged joint fiber deficit (MS)

## Plan / current statement attempted
- Goal: prove MS with explicit delta, or refute it by an explicit, L-by-L checkable source.
- Strategy as it stands: (1) audit the chain MS => (D-a), and work out step 5 exactly; (2) find out which part of MS the chain actually needs; (3) test the weakest point of MS, which is lambda = 1; (4) give a structural reduction.

## Status summary (filled in at the end)
(see the final section)

## 1. Audit of the chain MS => (D-a), and step 5 made exact (PROVED)

Notation. For a nonnegative lag weight u = (u_l)_{l>=1}, put C_u(lambda) = sum_{l<=lambda} u_l and
P_u(x) = sum_{lambda>=0} max(0, x - C_u(lambda)) for real x >= 0. By the prefix lemma (quoted, and correct), when x = H is an integer not exceeding the total mass, P_u(H) is the sum of the H cheapest lags of the multiset with u_l copies of l.

**Lemma 1.1 (scaling identities).** For 0 <= delta < 1 and every x >= 0:
(a) P_{(1-delta)u}(x) = (1-delta) P_u(x/(1-delta));
(b) P_{3u}(3x) = 3 P_u(x).
*Proof.* (a): max(0, x - (1-delta)C) = (1-delta) max(0, x/(1-delta) - C). (b): max(0, 3x - 3C) = 3 max(0, x - C). Sum over lambda. ∎

**Proposition 1.2 (exact form of steps 2-5).** Fix d and the three classes X_e = S_e(d), with sizes s_e and spans <= S. Let e_j be any valid lower bound for the span of a binary source with j marks (the same one the single-class certificate uses). Let c be an integer with 1 <= c < min_e s_e, and put s̄ = (s_0+s_1+s_2)/3 and H̄ = c s̄ - c(c+1)/2. If the domination C_w(lambda) <= (1-delta) C_{3v}(lambda) holds for all lambda >= 0, with w_l = sum_e r_{X_e}(l), then
   2 P_{(1-delta)v}(H̄) + 4 sum_{i=0}^{c-1} (c-i) e_{i+1} <= S c(c+1).          (1.2)
That is, the **mean** class size s̄ satisfies exactly the single-class rank-neighbour certificate, with the per-fiber caps v_l replaced by (1-delta) v_l and everything else unchanged.

*Proof.* The summed inequality (quoted, valid for unequal sizes) gives 2 P_w(H_tot) + 12 sum(c-i)e_{i+1} <= 3 S c(c+1), with H_tot = 3H̄. Domination and the prefix formula give P_w(H_tot) >= P_{(1-delta)3v}(H_tot), because max(0, H - C) decreases in C. (For lambda > S, C_w(lambda) = C_w(S) since r_X(l) = 0 for l > S, so domination for lambda <= S, i.e. MS, already gives it for all lambda.) By Lemma 1.1, P_{(1-delta)3v}(3H̄) = 3 P_{(1-delta)v}(H̄). Divide by 3. ∎

**Consequence.** Let K^{(delta)}(S) be the capacity produced by the single-class certificate when v_l is replaced by (1-delta)v_l, i.e. the largest real s for which some admissible rank c makes (1.2) hold with s̄ = s (or, in the actual certificate, the largest s surviving the chosen c; P is increasing, so the feasible set of s is an interval). Then, under MS, every shift d of every proper ternary source satisfies
   sum_e |S_e(d)| <= 3 K^{(delta)}(S),
provided the chosen c is < min_e s_e. **Small classes.** If some s_e <= c, then sum_e s_e <= 2K(S) + c, which is already far below 3K(S) when c is much smaller than K(S). So the side condition costs nothing in the regime of interest; it must be stated, though.

**Audit verdict.** Steps 1-4 are correct as written. Step 5 is correct with two precisions: (i) the common rank c < min s_e needs the small-class case split above; (ii) in the square, the triple at main colour c gets the cap 3K^{(delta)}(n-d-1) instead of the staggered sum_j K(n-d-j-1). The staggering offsets j <= 11 are absorbed with an additive loss of at most 3 sum_{j<=11} (K(n-d-1) - K(n-d-1-j)). This is negligible at n ~ 2.2*10^7, but it has to be computed. Neither point is a flaw.

**On delta'.** By (1.2), delta' := 1 - K^{(delta)}(S)/K(S) is obtained by rerunning the existing elementary certificate with caps (1-delta)v_l. It is not a universal function of delta, because it depends on how the P-term and the e-term share the budget S c(c+1). Two rigorous comparisons:
- Convexity alone gives no gain: P_u is convex with P_u(0) = 0, so (1-delta)P_u(x/(1-delta)) >= P_u(x), with equality possible when C_u jumps.
- In the smooth regime P_v(x) ≈ x^2/(2 v̄) (v roughly constant over the lags used), P_{(1-delta)v} ≈ P_v/(1-delta). If the e-term were negligible, s̄ would scale by sqrt(1-delta), so delta' ≈ delta/2. With the e-term present, delta' < delta/2 (heuristic).
I cannot run the numerical recertification here, so delta' is not computed. It is elementary once MS, or the weaker statement of Section 2, is available.

