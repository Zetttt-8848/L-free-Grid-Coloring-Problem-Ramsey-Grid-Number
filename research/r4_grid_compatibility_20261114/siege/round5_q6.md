kind: attempt

Open question attempted (flagged OPEN by this run, ledger entry 52): the missing statement MS' below. You are given only the statement and the statements (not the proofs) of the results the intended chain uses. Do two things, in order.

**Task 1 (derive the chain yourself).** Show, from the cited statements below (you may re-prove any of them, and should say if one looks false), that MS' implies Part D of the problem at level (D-a): an inequality sum_e |S_e(d)| <= (1-delta')·(sum of the three separate binary-source caps) with explicit delta' > 0, for every proper ternary source and every shift d whose span S = span F_d(D) is at least an explicit S_1. If the derivation does not go through, say exactly where; if MS' looks implausible, say why. Either is a result.

**Task 2 (attack MS').** Prove MS' with explicit constants, or refute it by an explicit family checkable L by L. Your first move must be one that none of the attempts listed below used; name it. Attempts already used (names only): pattern classification of mixed additive quadruples and forbidding patterns (AABA/ABAA); corner exclusion with a row/column independence heuristic; near-extremality hypotheses on class sizes and fibers; request-energy bounds; Fourier uniformity / equidistribution of the individual Golomb pieces; color Cauchy-Schwarz; six disjoint Sidon pieces lag by lag; the lag-l start set as a 3-colored source and the two-Sidon binary-source reduction (TSD); hereditary window induction on the capacity K; shear to corners and box (4-point) counts; digit-product and Sidon-block lifting constructions. Candidate untried first moves include (you may choose another): an entropy or container-type count of proper colorings of saturated configurations; a density-increment argument within the shifted triangle; an argument through the rows d' > d (the request sets R_e(h) of the problem and the double cover); a linear-programming or flag-algebra style relaxation of the local constraints; an algebraic construction for the refutation.

A proof of MS' for only some sources or some parameter ranges does not answer the question, though it should be reported if it is all you found.

**Missing statement (MS'; ledger entry 52, OPEN, locator round5_plan).**
Let Q(m), m >= 0, be the largest size of a Sidon set (all positive differences distinct; 3-term progressions excluded) contained in m+1 consecutive integers; Q(m) = 0 for m < 0. MS' asserts: there are explicit constants delta in (0,1) and S_0 >= 1 such that for every proper ternary source (D, chi) — a finite D ⊂ Z with a coloring chi of V(D) = {(v,u) : u < v; u, v in D} by P = {0,1,2} with no monochromatic directed L (x,y),(x+t,y),(x+t,y+t), t > 0, all three cells in V(D) — and every d >= 1 with F_d(D) = {u : u, u+d in D} nonempty and S := max F_d(D) - min F_d(D) >= S_0, writing v_l = Q(S-l) + Q(S-l-1), S_e(d) = {u in F_d(D) : chi(u+d,u) = e}, r_X(l) = #{u in X : u+l in X}, one has for every integer lambda with 1 <= lambda <= S:

    sum_{l=1}^{lambda} sum_{e in P} r_{S_e(d)}(l)  <=  (1-delta) · sum_{l=1}^{lambda} 3 v_l  +  S/100.

- It is universal (no hypothesis besides S >= S_0). It is weaker than MS (entry 41): the slack S/100 absorbs complete saturation of all lags up to about sqrt(S)/600, and moderate spans are exempt. It is implied by MS, by SC(delta), and (for large S) by TSD.


## Cited statements (proved earlier in this run; statements only)

Notation as in the problem; P = {0,1,2}; C(p,q) and kappa are not needed here. For a lag weight w = (w_l)_{l>=1}, C_w(lambda) = sum_{l<=lambda} w_l, and P(H; w) is the sum of the H smallest elements of the multiset with w_l copies of l.

1. **P1 (i)-(v) hold as posed.** In particular: every L in V(D) is L(u,d,h) = {(u+d,u), (u+h,u), (u+h,u+h-d)}, 1 <= d < h, and lies in V(D) iff u, u+d, u+h-d, u+h are in D; for each class X = S_e(d), the cells (b+d, a), a < b in X, avoid color e (so X is a binary source); each fiber F_l(X) is the disjoint union of two Sidon sets (its Golomb classes, split by the color of (u+d+l, u)), so r_{S_e(d)}(l) <= v_l := Q(S-l) + Q(S-l-1) where S bounds the span of X.
2. **Heredity.** Every subset of a binary source is a binary source.
3. **Rank-neighbor inequality (single class).** For a hereditary family in which a member with j marks has span at least e_j: a member of size s and span L, with 1 <= c < s, H = cs - c(c+1)/2, and difference multiplicities bounded by v_l, satisfies 2P(H; v) + 4 sum_{i=0}^{c-1}(c-i)e_{i+1} <= L c(c+1). The certified capacity K(L) is the largest s for which this is not violated (at the chosen rank).
4. **Summed rank-neighbor inequality.** If the three classes S_e(d) have sizes s_e and spans <= S, and 1 <= c < min_e s_e, then with w_l = sum_e r_{S_e(d)}(l) and H_tot = sum_e (c s_e - c(c+1)/2): 2P(H_tot; w) + 12 sum_{i=0}^{c-1}(c-i)e_{i+1} <= 3 S c(c+1).
5. **Prefix formula.** If H <= sum_l w_l then P(H; w) = sum_{lambda>=0} max(0, H - C_w(lambda)); hence C_w <= C_{w'} pointwise implies P(H; w) >= P(H; w').
6. **Theorem A (conversion).** Let C~ be the piecewise-linear interpolation of C_v and Pi(H) = integral_0^infinity (H - C~(x))_+ dx. Fix a proper ternary source and a shift d with span S. Let 0 < alpha <= 1, E_0 >= 0, rho >= 1, and an integer s* > rho satisfy the Pi-certificate 2Pi(H*) + 4 sum_{i<rho}(rho-i)e_{i+1} > S rho(rho+1), H* = rho s* - rho(rho+1)/2, with every class of size <= s*-1. Let Lambda_0 be the least lambda with 3 alpha C_v(lambda) >= 3 rho s* + E_0 (or S if none). If C_w(lambda) <= 3 alpha C_v(lambda) + E_0 for 1 <= lambda <= Lambda_0, then sum_e |S_e(d)| <= max{ 2(s*-1) + rho, 3 sqrt(alpha) s* + E_0/rho + 3(1 - sqrt(alpha))(rho+1)/2 }.

## Scale (heuristic, for orientation only)
At the problem's scale S ≈ 2.2*10^7: K ≈ 4.58*10^5, v_l ≈ 9.4*10^3, optimal rank about sqrt(K) ≈ 675 (estimate).

## What to return
1. Task 1: the derivation MS' => (D-a) with delta' explicit, or the exact point where it fails.
2. Task 2: a complete proof of MS' with explicit constants, or an explicit counterexample with complete L-by-L properness proof; otherwise the strongest rigorous partial result, clearly labelled, and the obstruction met. Name your first move.
Rules: every proof complete; finite computations are evidence only for what they check; do not import three-color facts; no claim about R_4 except as an implication from stated hypotheses.
