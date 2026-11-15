# Running summary after round 4 (written at the round-5 plan step)

## Goal (ledger entry 1, OPEN; unchanged)
P1 (i)-(v) exactly as posed, plus Part D settled at level (D-a) or (D-b).
- (D-a): an explicit-delta proportional-loss inequality sum_e |S_e(h)| <= (1-delta)(sum of separate binary-source caps), per h or a_h-averaged, every hypothesis named.
- (D-b): an explicit, L-by-L checkable family of proper ternary sources showing that no request-based inequality of that kind can hold, with classes as large as the regime requires.
- (D-c) is a separate line (entries 6, 35, 39), not part of the goal.
- No complete written proof of the goal is in hand; the audit rule is not triggered. Escalation applies. Round 6 is the last round.

## Standing results (never dropped)
1. **P1 (i)-(v), complete (entry 9; round1_q1 Part A is the cleanest chain; round1_q3, round1_q4 agree).**
   - Lemma 0: every L in V(D) is L(u,d,h), 1<=d<h, cells (u+d,u), corner (u+h,u), (u+h,u+h-d), arm length h-d; it lies in V(D) iff u, u+d, u+h-d, u+h in D.
   - (i) L(u,d,h) is monochromatic of color e iff u in F_{h-d}(S_e(d)) ∩ S_e(h). (ii) R_e(h) ⊆ F_h(D). (iii) double cover, sharp identity sum_e |R_e| = 2|F_h| - 2#{k=0} - #{k=1}. (iv) shifted source avoids e; F_l(X) ⊆ R_e(h); four-L Golomb split; F_l(X) ∩ R_{e'} ⊆ G_{e''}; F_l(X) ∩ R_{e'} ∩ R_{e''} = ∅. (v) accounting.
2. Single-shift satisfiability iff R_0 ∩ R_1 ∩ R_2 = ∅; single-shift counting bounds |F_h| only from below (entry 12, round1_q3).
3. Conditional energy reduction (entry 13, round1_q4). 4. Forced energy (entry 25, round2_q3). 5. Collision lemma (entry 15). 6. Single-L coupling lemma (entry 24, round2_q2).
7. Lemma F; AABA forcing (entry 26, round2_q4); ABAA forcing and r = s impossible (entry 30, round3_q1).
8. Summed rank-neighbor inequality 2P(H_tot;w) + 12 sum_i (c-i)e_{i+1} <= 3L'c(c+1), w_l = sum_e r_{S_e(d)}(l), common rank c < min_e s_e (entry 27, round2_q4).
9. Prefix formula P(H;w) = sum_{lambda>=0} max(0, H - C_w(lambda)) and prefix-dominated sufficiency (entry 33, round3_q4).
10. Digit families (entries 18-22, round2_q1): proper for every role/arm-color choice; over arbitrary sources they refute UW(lambda) for every lambda, U1-type energy for every C, union growth with positive liminf, simultaneously on any finite set of shifts. Not embeddable.
11. Lifted digit family (entries 31, 32, round3_q3): proper; min_e N_e(H) >= lambda|F_H|, sum_e |R_e(H)| = |F_H|, classes and fibers of size >= span^{1/2-o(1)}. Not embeddable. (Director's script check, evidence only.)
12. (D-c+) refuted for arbitrary sources (entries 34, 35, round3_q2).
13. Density obstruction modulo the corners theorem (entry 36, round3_q4); non-explicit.
14. Color Cauchy-Schwarz (entry 37, round4_plan): sum_k a_k r_Y(k) <= 3 sum_e sum_k a_k r_{S_e(d)}(k). Gives no saving by itself (round4_q5 Sec. 6: it is a uniformity statement, translation-blind).
15. **NEW. Theorem A, the conversion MS' => (D-a) (round4_q6 Part A; director re-checked every step this round).** With Pi(H) = int_0^inf (H - C~(x))_+ dx (C~ the piecewise-linear interpolation of C_v), Lemma A1: P(H;v) - H <= Pi(H) <= P(H;v); Pi(tH) >= t^2 Pi(H) for t >= 1; sum_{lambda>=0}(H' - beta C_v(lambda))_+ >= beta Pi(H'/beta). Theorem A: if 0 < alpha <= 1, E_0 >= 0, rho >= 1, integer s* > rho with Pi-certificate 2Pi(H*) + 4E_rho > S rho(rho+1) (H* = rho s* - rho(rho+1)/2), every class s_e <= s*-1, and C_w(lambda) <= 3 alpha C_v(lambda) + E_0 for 1 <= lambda <= Lambda_0 (Lambda_0 the least lambda with 3alpha C_v(lambda) >= 3rho s* + E_0, else S), then sum_e s_e <= max{2(s*-1)+rho, 3 sqrt(alpha) s* + E_0/rho + 3(1-sqrt alpha)(rho+1)/2}. Corollary A2: with s* = K^Pi(S)+1 (K^Pi the Pi-form certified cap, K <= K^Pi), delta' = (1-sqrt(1-delta))(1-(rho+1)/(2K)) - small terms, about delta/2. The factor 1/2 is intrinsic. Entry 42.
   - Same conversion independently in round4_q3 Theorem 2.1 (sigma <= 3 sqrt((1-delta) V S (1+1/c)) + 3(c+1)/2) and round4_q5 Lemma P; all three agree. Numerically (estimates): delta ≈ 0.023 in MS' is needed for delta' ≈ 0.0115 (the hypothetical 21.0M figure).
16. **NEW. Lag-l start set structure (round4_q2 Sec. 1, Lemma W / Corollary U; entry 43).** W = union of the three fibers F_l(S_e(d)), kappa(p,q) = chi(q+h,p) for p <= q: (a) kappa is proper on the "L's" (p,p+x),(p,p+y),(p+y-x,p+y); (b) kappa(p,q) != e for p <= q in the same fiber A^e. Each diagonal class U_f = {kappa(p,p) = f} = G_e^f ⊔ G_{e'}^f is a binary source whose coloring is constant e' on pairs inside G_e^f and constant e on pairs inside G_{e'}^f. Lemma F, Golomb split and the AABA/ABAA forcings are special cases. Also (round4_q5 Lemma B) for every m, r_{U_f}(m) <= 2Q.
17. **NEW. No single mixed quadruple pattern is forbidden in the U-structure (round4_q2 Sec. 2; entry 44).** Only AAAA/BBBB are; so any proof of MS-type statements must be global (counting/density), not pattern-by-pattern. (The realizability of AABA in an actual ternary source remains open, entry 28.)
18. **NEW. TSD reduction (round4_q2 Sec. 3; entry 45).** TSD(m0,delta): U = A ⊔ B, A,B Sidon in m+1 consecutive integers, m >= m0, with a proper 2-coloring of V(U) constant alpha on A-pairs and beta != alpha on B-pairs, implies |U| <= (1-delta)(Q(m)+Q(m-1)). TSD(m0,delta) implies the per-lag bound |U_f(l)| <= (1-delta)v_l for S-l >= m0, hence MS up to an additive error depending only on m0, hence MS' for large S. TSD itself OPEN (entry 46).
    - Director's finite check this round (scratchpad tsd.py, verify23.py; evidence only for what it checks): the exact maximum of |U| under the TSD hypotheses is cap-1 or cap-2 for 7 <= m <= 22, but EQUALS the cap Q(m)+Q(m-1) = 12 at m = 23 and m = 24. Explicit instance at m = 23: A = {0,1,4,13,15,21}, B = {2,5,7,16,22,23}, with an explicit coloring of the 36 mixed pairs checked against all 76 L's of V(U) (entry 54). So TSD has no deficit at small m; it can hold only asymptotically, if at all. Plain disjointness (no coloring) reaches the cap for every m in 5..24 except m = 7.
19. **NEW. Near-extremality transfer and lag-1 facts (round4_q3 Sec. 3; entry 47).** If C_w(lambda) > (1-delta)C_{3v}(lambda) then each class has prefix ratio > 1-3delta and each of the six pieces sum_{l<=lambda}|G_e^f(l)| > (1/2-3delta)C_v(lambda) - lambda/2. w_1 <= (8/9)|F_d(D)| (runs of constant z_d have length <= 9); lag-1 equality needs S >= 67 (Golomb table cited from memory). Also (round4_q6; entry 50) SC(delta) (single-class prefix deficit) implies MS(delta).
20. **NEW. Uniformity obstructions (round4_q5 Secs. 2, 4, 5; round4_q1 Sec. 4; entries 48, 49).** Lemma E: Sidon sets are equidistributed in windows (sum_x (a(x)-abar)^2 <= T(k+T-1-Tk^2/(N+T))). Lemma C: complete first-generation no-collision consequence of Lemma F + AABA/ABAA. Obstruction O: for A Sidon without differences in {1..4}, the pair (A, A+2) has zero Lemma-C collisions although both are near-maximal and Fourier-uniform; so uniformity of individual pieces plus first-generation forcing cannot give a positive rate of contradictions. Bose translates (round4_q1 Prop 4.2): six pairwise disjoint Sidon sets of size q in [0,q^2-2], so lag-by-lag disjoint-Sidon constraints give no delta.
21. **NEW. Chain refinements (round4_q1 Sec. 2, round4_q3 Sec. 1).** Only lambda < Lambda (about S^{5/8} with the optimal rank c ≈ sqrt K ≈ 675 at the regime scale; estimate) and an additive slack E (costing E/c in the cap) matter; a failure of MS at bounded lambda or at moderate S does not hurt the consumer. Small-class case split: if min_e s_e <= c then sum_e s_e <= 2K + c. Staggering inside a triple is lost additively (negligible).

## Dead ends (each a REFUTED statement with its refuting file)
- U1 (entry 3), UW(1) (entry 4): d1 witnesses.
- round1_q2's original digit family proper (entry 10, round1_q2).
- UW(lambda) for every lambda (entry 20, round2_q1). U1-type energy for every C; union growth with positive liminf (entry 21, round2_q1).
- Union of same-corner pieces is Sidon (entry 16).
- (D-b)-type variants refuted by the lifted family (entry 32, round3_q3): fiber multiplicity >= m at request lags; class sizes >= c·span^alpha, alpha < 1/2.
- (D-c+) without near-extremality hypotheses (entry 35, round3_q2).
- Fixed-density counter-families at unbounded span (entry 36, modulo corners theorem).
- MS (entry 41) is NOT refuted; it is retracted as missing statement only because the weaker MS' (entry 52) suffices.

## Open gaps (set aside, not refuted)
- (D-b) at regime size (entry 38): explicit constructions look out of reach; round4_q4.partial claims (proof not in hand) that digit-product sources M·B+R have lag-1 ratio <= (1+o(1))/sqrt(M), so product/lift constructions cannot refute MS (entry 53, OPEN lead).
- AABA/ABAA forbiddenness (entry 28); deprioritized (entry 44 shows pattern-forbidding is not the mechanism).
- (D-c) under (H1)-(H3) (entry 39).
- Union growth / anti-collision under saturation (entry 7).
- TSD (entry 46); OQ2 of round4_q5 (is the full Lemma-B(c) system on A ∪ (A+2) satisfiable for near-maximal A?); the row/column anti-correlation lemma (round4_q3 Sec. 4.1); cross-uniformity of same-corner pieces (round4_q5 OQ3).
- SC(delta), single-class prefix deficit (round4_q6 O2): stronger than MS; would improve K itself.
- The extension question (round4_q1 Sec. 5): is every proper 3-coloring of the shifted triangle T_d(F_d(D)) a restriction of a ternary source?

## The chain and the missing statement

**Chain.**
1. Entry 9 settles P1 (i)-(v) as posed. It remains to settle Part D at (D-a).
2. Fix a proper ternary source and a shift d with S = span F_d(D) >= S_0. The three classes S_e(d) are binary sources of span <= S (entry 9 (iv.0); heredity, round4_q6 Lemma B1). Let K^Pi(S) be the Pi-form rank-certificate cap at a chosen rank rho (entry 42): every binary source of span <= S has size <= K^Pi(S), and K^Pi >= K.
3. Entry 27 (summed rank-neighbor inequality) and entry 33 (prefix formula) feed Theorem A (entry 42).
4. MS' (below, entry 52) gives the hypothesis of Theorem A with alpha = 1-delta, E_0 = S/100, Lambda_0 <= S.
5. Theorem A with s* = K^Pi(S)+1 gives sum_e |S_e(d)| <= max{2K^Pi(S) + rho, 3 sqrt(1-delta)(K^Pi(S)+1) + S/(100 rho) + 3(1-sqrt(1-delta))(rho+1)/2}. Hence sum_e |S_e(d)| <= (1-delta')·3K^Pi(S) with the explicit
   delta' = min{ 1/3 - rho/(3K^Pi), (1-sqrt(1-delta))(1-(rho+1)/(2K^Pi)) - sqrt(1-delta)/K^Pi - S/(300 rho K^Pi) }.
6. Elementary remaining step (to be written out in the final document, not structural): an explicit lower bound K^Pi(S) >= c_1 S^{3/4} (from v_l <= 2Q(S) <= 2(sqrt S + S^{1/4} + 1) and the definition of the certificate), and the choice rho = floor(K^Pi(S)^{1/2}), make delta' >= delta/2 - O(S^{-1/8}) explicitly, so delta' >= delta/4 for all S >= S_1 with S_1 explicit. At the regime scale (estimates: K ≈ 4.58e5, rho ≈ 675) delta' >= 0.4996 delta - 2.5e-4. This is the (D-a) inequality per shift, with the named span hypothesis S >= S_1, compared to the sum of the three separate (Pi-form certified) binary-source caps.
   - If step 6's lower bound on K^Pi were not available, the inequality still holds at each S with the displayed delta'(S), explicit in terms of the certificate value.

**Missing statement (MS'; ledger entry 52, OPEN, locator round5_plan).**
Let Q(m), m >= 0, be the largest size of a Sidon set (all positive differences distinct; 3-term progressions excluded) contained in m+1 consecutive integers; Q(m) = 0 for m < 0. MS' asserts: there are explicit constants delta in (0,1) and S_0 >= 1 such that for every proper ternary source (D, chi) — a finite D ⊂ Z with a coloring chi of V(D) = {(v,u) : u < v; u, v in D} by P = {0,1,2} with no monochromatic directed L (x,y),(x+t,y),(x+t,y+t), t > 0, all three cells in V(D) — and every d >= 1 with F_d(D) = {u : u, u+d in D} nonempty and S := max F_d(D) - min F_d(D) >= S_0, writing v_l = Q(S-l) + Q(S-l-1), S_e(d) = {u in F_d(D) : chi(u+d,u) = e}, r_X(l) = #{u in X : u+l in X}, one has for every integer lambda with 1 <= lambda <= S:

    sum_{l=1}^{lambda} sum_{e in P} r_{S_e(d)}(l)  <=  (1-delta) · sum_{l=1}^{lambda} 3 v_l  +  S/100.

- It is universal (no hypothesis besides S >= S_0). It is weaker than MS (entry 41): the slack S/100 absorbs complete saturation of all lags up to about sqrt(S)/600, and moderate spans are exempt. It is implied by MS, by SC(delta), and (for large S) by TSD.

**Why it should hold (director's sketch; candid).**
- If MS' fails, entry 47 makes all six pieces G_e^f(l), l <= lambda, near-maximal Sidon sets on average, and Corollary U (entry 43) makes each U_f(l) = G_e^f(l) ⊔ G_{e'}^f(l) a binary source of size about 2Q(S-l) whose coloring kappa_l(p,q) = chi(q+d+l,p) is constant on each piece. The m = 23 instance (entry 54) shows one U_f at one lag can be saturated, so no deficit comes from a single small (f, l).
- Cross-lag collisions are too rare at the lags the chain needs: kappa_l(p,p+j) is the cell z_{d+l+j}(p) (z_m(p) = chi(p+m,p)), shared by the structures of all lags l' <= l+j; but a cell lies in about 36 lambda/S of them, so forced-value collisions number about lambda^3/S, negligible against C_w ≈ 6 sqrt(S) lambda unless lambda >~ S^{3/4}, while Theorem A at the optimal rank needs lambda up to about S^{5/8} (estimates). Raising the rank to push Lambda_0 to order S makes the needed statement equivalent to the conclusion itself, so it does not help.
- So the deficit must come from a single lag, asymptotically: the three binary sources U_0, U_1, U_2 of one lag, coupled by Lemma W(a) with mixed diagonal colors and by Lemma W(b). Single-lag first moment (heuristic): U_f has about 2m L-constraints on about m free mixed cells, each forbidding about 1/4 of assignments (units forbid 1/2), so the count of colorings is about (2·(3/4)^2)^m ≈ 1.1^m — borderline. The cross-f constraints of W(a) (cells kappa(p,q) with p in U_f, q in U_{f'}, f != f', constrained by triples mixing three diagonal colors) and W(b) are what could push it below 1.
- Candidate mechanism: a finite gadget — a configuration of O(1) points of W in prescribed pieces with prescribed additive relations — whose W(a)/W(b) constraints are jointly unsatisfiable, plus a counting lemma that six near-maximal Sidon pieces in an interval contain such a configuration at a rate proportional to sqrt(S) per lag (near-maximal Sidon sets realize almost half of all differences, so configurations defined by few difference coincidences occur at a predictable rate; Lemma E gives the needed equidistribution). Each gadget forces one point deleted, and the rate gives delta.
- Risk: the borderline first moment means MS' may be false; a refutation needs a full proper ternary source, not just a lag structure.

**Tried so far (on MS', MS, or earlier wordings: entry 17 joint per-lag bound, entry 29 AD).**
- round2_q4: pattern classification of mixed quadruples; gave Lemma F, AABA forcing, Sidon-union refutation; no bound.
- round3_q1: AABA/ABAA forbiddenness; only forcing found.
- round3_q4: AD via corner exclusion with independence; gave the prefix lemma and density obstruction; correlation step not achieved.
- round2_q3: near-extremality hypotheses H_avg, H_fib; no deficit. round1_q4: energy route; conditional reduction only.
- round4_q1 (closing task on MS, re-run): chain audit, MS* reduction, Bose six-translate obstruction (additive lag-by-lag info gives no delta), MS is a statement about the shifted triangle; no proof.
- round4_q2 (closing task copy): Lemma W/Corollary U (lag-l start set as a 3-colored source), no single pattern forbidden, TSD reduction; no proof.
- round4_q3 (closing task copy): chain audit, MS* and Theorem 2.1 with explicit constants, near-extremality transfer, lag-1 exclusions; row/column anti-correlation named as the missing lemma; no proof.
- round4_q4 (refute MS; partial only, cut off twice): claims a digit-product lemma, a positive-ratio family and a 1/sqrt(M) ceiling for products (proofs not in hand); no counterexample.
- round4_q5 (Fourier/uniformity route): Lemma E, Lemma B, Lemma C, Obstruction O (translate pairs defeat uniformity); no proof.
- round4_q6 (bare query): Theorem A; window induction (dead, estimate); shear to corners and box symmetry (4-point counts consistent with saturation); decoupling remark (inter-class content lives in rows d' > d, i.e. requests); no proof.

## Where the next round should concentrate

**Progress test.** Rounds 3-4 produced progress on the chain in the counted sense: a new PROVED universal result shortening the chain — Theorem A (entry 42, round4_q6; also round4_q3 Theorem 2.1), which turns the former step "compute delta' from delta" (an open step of the round-4 chain) into a proved explicit conversion; and in round 3 the prefix lemma (entry 33). The missing statement itself is not proved. MS is replaced by the weaker MS' (entry 52); this is a weakening that the chain re-derived via Theorem A supports, not a simplification.
- What differs from last round's sketch: the round-4 sketch was uniformity of the individual pieces plus corner exclusion, which round4_q5 (Obstruction O) and round4_q1 (Bose translates) show cannot work. The new sketch locates the deficit at one lag in the coupled three-source structure (W, kappa) of entry 43, via an unsatisfiable finite gadget forced at a positive rate; cross-lag collisions are shown (heuristically) to be too rare at the needed lags.

**Round 5 wave (escalation; six attempt queries, all on MS').**
- q1-q3: identical closing task on MS' (P1 key lemmas, Lemma F/AABA/ABAA, rank-neighbor + summed inequality + prefix lemma, Theorem A with proof, Corollary U, TSD reduction, Lemma 3.1, Obstruction O, the m = 23 instance, the chain, the cross-lag sketch).
- q4: refute MS' exactly as stated (wording changed this round): an explicit family with S -> infinity and prefix ratio -> 1 beyond the slack, or a derivation of something false.
- q5: the single-lag core, continued from round4_q2's TSD reduction with its partial results spliced: prove a single-lag deficit for the coupled structure (W, kappa) (or TSD itself) for large m, or refute TSD by an explicit family of saturated two-Sidon binary sources; the m = 23 equality instance is supplied.
- q6: bare query (MS' and the cited statements only): derive the chain, then attack MS' by a first move none of the listed attempts used.
- Round 6 (final): if MS' is proved, record PROVED [GOAL] and send two verify queries carrying P1, entries 27/33/42 and the MS' proof; otherwise come back to nothing (the goal was never proved) and let the final document present the standing results, with MS' as the clearly marked open statement.
