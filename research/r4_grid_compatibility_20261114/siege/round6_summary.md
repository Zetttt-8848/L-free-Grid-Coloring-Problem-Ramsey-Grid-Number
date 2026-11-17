# Running summary after round 5 (written at the round-6 plan step; round 6 is the final round)

## Goal (ledger entry 1, OPEN; unchanged, never proved, never raised)
P1 (i)-(v) exactly as posed, plus Part D settled at level (D-a) or (D-b).
- (D-a): an explicit-delta proportional-loss inequality sum_e |S_e(h)| <= (1-delta)(sum of separate binary-source caps), per h or a_h-averaged, every hypothesis named.
- (D-b): an explicit, L-by-L checkable family of proper ternary sources showing that no inequality of that kind can hold, with classes as large as the regime requires.
- P1 is PROVED (entry 9). Part D is not settled. No complete written proof or refutation of the goal is in hand; the audit rule is not triggered; the escalation rule applies. There is no proved goal to come back to.

## Standing results (never dropped)
1. **P1 (i)-(v), complete (entry 9; round1_q1 Part A is the cleanest chain; round1_q3, round1_q4 give independent agreeing proofs).**
   - Lemma 0: every L in V(D) is L(u,d,h), 1<=d<h, cells (u+d,u), corner (u+h,u), (u+h,u+h-d), arm length h-d; it lies in V(D) iff u, u+d, u+h-d, u+h in D.
   - (i) L(u,d,h) is monochromatic of color e iff u in F_{h-d}(S_e(d)) ∩ S_e(h). (ii) R_e(h) ⊆ F_h(D). (iii) double cover, sharp identity sum_e |R_e| = 2|F_h| - 2#{k=0} - #{k=1}. (iv) shifted source avoids e; F_l(X) ⊆ R_e(h); four-L Golomb split; F_l(X) ∩ R_{e'} ⊆ G_{e''}; F_l(X) ∩ R_{e'} ∩ R_{e''} = ∅. (v) accounting.
2. Single-shift satisfiability iff R_0 ∩ R_1 ∩ R_2 = ∅; single-shift counting bounds |F_h| only from below (entry 12, round1_q3).
3. Conditional energy reduction (entry 13, round1_q4). 4. Forced energy (entry 25, round2_q3). 5. Collision lemma (entry 15). 6. Single-L coupling lemma (entry 24, round2_q2).
7. Lemma F (same-corner pairs); AABA forcing (entry 26, round2_q4); ABAA forcing and r = s impossible (entry 30, round3_q1).
8. Summed rank-neighbor inequality (entry 27, round2_q4). 9. Prefix formula (entry 33, round3_q4).
10. Digit families (entries 18-22, round2_q1): proper for every role/arm-color choice; over arbitrary sources they refute UW(lambda) for every lambda, U1-type energy for every C, union growth with positive liminf, simultaneously on any finite set of shifts. No member is a diagonal class of a properly four-colored square (every member has span above 21,987,408; entry 22).
11. Lifted digit family (entries 31, 32, round3_q3): proper; min_e N_e(H) >= lambda|F_H|, sum_e |R_e(H)| = |F_H|, classes and fibers of size >= span^{1/2-o(1)}. Not embeddable.
12. (D-c+) refuted for arbitrary sources (entries 34, 35, round3_q2).
13. Density obstruction modulo the corners theorem (entry 36, round3_q4); non-explicit.
14. Color Cauchy-Schwarz (entry 37). No saving by itself.
15. Theorem A, conversion MS' => (D-a) against the Pi-form rank cap (entry 42, round4_q6; re-checked by round5_q1, q2, q3, q6). Round5 audits: steps 1-5 correct; the step-6 asymptotic lower bound K^Pi >= c S^{3/4} was justified in the wrong direction (needs a LOWER bound on Q); corrected in round5_q1 (Q(m) >= sqrt(m/8), m >= 72, via Erdos-Turan + Bertrand; e_j <= 8j^2; K^flat(S) >= S^{3/4}/3 for S >= 1490, rho = floor(S^{3/8}/12)) and round5_q3 Lemma 1.2; the comparison cap must be certified at the rank actually used (round5_q2 A2, round5_q3 1.3); monotonicity of K^Pi in S proved (round5_q2 A3).
16. Lemma W / Corollary U (entry 43, round4_q2). 17. No single mixed quadruple pattern forbidden (entry 44); round5_q1 Lemma G extends: a single additive quadruple's two W(a) constraints plus unary domains are unsatisfiable iff all four points have the same type.
18. TSD reduction (entry 45) and the m = 23 saturated TSD instance (entry 54). Round5_q5: SL(m0,delta) => MS' with S_0 = max(1, 300 delta m0^2); TSD => SL.
19. Near-extremality transfer, w_1 <= (8/9)|F_d(D)| (entry 47); SC => MS (entry 50).
20. Uniformity obstructions: Lemma E, Lemma C, Obstruction O (entry 48); six disjoint Bose translates (entry 49).
21. **NEW (round5_q6). Fejer route.** Lemma F: for X of size s, span <= S, Lam = lambda+1, N = S+Lam: s Lam + 2 sum_{l<=lambda}(Lam-l) r_X(l) >= s^2 Lam^2/N. Corollary F0: every binary source of span <= S has size <= K_F(S) := min_lambda [N/Lam + sqrt(v_1 N)], and K_F(S) >= sqrt(v_1 S). Theorem B: MS'(delta,S_0) => sum_e |S_e(d)| <= (1-delta/4) 3K_F(S) for S >= max{S_0, 10^4, delta^{-4}, 16384 delta^{-2}}. Proposition C: MS'(delta) => SD(eta) for eta < delta (SD(eta): sum_e |S_e(d)|^2 < 3(1-eta) v_1 S), and Corollary C1: SD(eta) => sum_e |S_e(d)| < (1-eta/2) 3K_F(S). So MS' is at least as strong as a proportional size deficit: MS' is not a reduction of (D-a). (Director checked Lemma F, F0, C1 by hand this step.)
22. **NEW (round5_q1).** Theorem B (single-window conversion, P-form cap K^flat at the same rank, no Pi recertification): WE(Lambda; alpha, E) at one window Lambda_c suffices. Window-energy identity W1 / Proposition E: WE splits into a size part plus a dispersion part, so for equidistributed classes WE is equivalent to the size bound itself. Lemma T: MS' trivial for lambda <= S/(600 delta(sqrt(2S)+1)). Lemma K0: binary source of span lambda has size <= 1 + 2 sqrt(lambda Q(lambda)). Proposition N: a failure of MS' (delta <= 1/6, S >= 146) forces every class to have size > S^{5/8}/16.
23. **NEW (round5_q2).** Inscribed-pair rule for binary sources (Lemma 2.3: psi proper iff for every p<y and inscribed t, not psi(p,p+t) = psi(y-t,y) = psi(p,y)); Corollary 2.4 (parallel-pair agreement; transport Z_j(l) ∩ (Z_j(l)-g) ⊆ Z_{jbar}(l+g); cross-lag consistency); Corollary 2.5 (corner agreement: p<q same piece at lag l, p<q' same piece at lag l', q+l = q'+l' => z_{d+l}(p) = z_{d+l'}(p)); Lemma 2.6 difference coverage of Sidon sets; Proposition 2.1/2.2 (content window and counterexample requirements). Correction of the director's round-5 heuristic: cross-lag coincidences are NOT rare (by their estimate a forced cell is shared by about 15 lag structures at lambda ≈ 7 sqrt S); the multi-lag single-class structure is the natural candidate source of a deficit (heuristic).
24. **NEW (round5_q3).** Same audit; size of a prefix-saturated class > about 0.42(1-3delta) sqrt(S) lambda^{1/4}; Q(m) >= sqrt(m)/2 + 1/4 for m >= 6 (Singer + Bertrand, cited).
25. **NEW (round5_q4).** Lemma K: binary source of span L has size <= sqrt(16 L Q(L)). Lemma G (gap coverage). Theorem N (necessary conditions for a refuting family). Proposition P: block-placed sources (incl. digit products M B + R, B Sidon, M > 2 rho) have joint prefix ratio <= theta + kappa ~ Q(rho)/sqrt(M) + O(g^{-1/2}) for every lambda: products cannot refute MS' at the top scale (proved replacement of the entry-53 lead). Difference colorings: ratio <= 1/3.
26. **NEW (round5_q5).** Theorem T: exact finite reformulation (T1)-(T4) of TSD for translate pairs (A, A+t), A Sidon without differences in [1,2t]. Proposition G1: explicit 6-point gadget (x<y in A, y1+y2 = x+y-t, z1+z2 = x+y+t, all four inside (x,y)) makes U = A ∪ (A+t) non-TSD-colorable, with a direct cell-by-cell proof valid in a general TSD form; this settles negatively the translate-pair satisfiability left open by Obstruction O whenever A contains G1. Lemma S (= gap coverage), Lemma W(a') (negative inner lag).

## Dead ends (each a REFUTED statement with its refuting file)
- U1 (entry 3), UW(1) (entry 4): d1 witnesses.
- round1_q2's original digit family proper (entry 10, round1_q2).
- UW(lambda) for every lambda (entry 20, round2_q1). U1-type energy for every C; union growth with positive liminf (entry 21, round2_q1).
- Union of same-corner pieces is Sidon (entry 16).
- (D-b)-type variants refuted by the lifted family (entry 32, round3_q3): fiber multiplicity >= m at request lags; class sizes >= c·span^alpha, alpha < 1/2.
- (D-c+) without near-extremality hypotheses (entry 35, round3_q2).
- MS (entry 41) and MS' (entry 52) are NOT refuted; they are retired as missing statements because round5_q6 Proposition C shows MS' implies the plain size deficit, which alone gives (D-a).

## Open gaps (set aside, not refuted)
- (D-b) at regime size (entry 38). Round5 (q1 Prop N, q2 Prop 2.2, q4 Theorem N, q6 4.3): any refutation of MS' or of a size deficit needs, at one shift, three binary sources each of size of order S^{3/4} (Fejer: >= about sqrt(v_1 S) ≈ sqrt(2) S^{3/4} for SD), far beyond any known construction (Sidon sets give sqrt S; lifted families span^{1/2-o(1)}). Problem SAT (round5_q4): do binary sources with saturated fibre prefix beyond lag sqrt(S) exist?
- Existence of binary sources of size >= S^{1/2+eps} (round5_q1 OQ3, round5_q6 O3): a negative answer with exponent < 3/4 makes the size deficit trivially true.
- AABA/ABAA forbiddenness (entry 28), (D-c) under (H1)-(H3) (entry 39), union growth under saturation (entry 7), TSD (entry 46), counting lemma G1(t) (round5_q5), the non-translate half of the TSD dichotomy, SC/SC' single-class prefix deficit, the extension question (round4_q1 Sec. 5).
- MS' (entry 52) and WE(Lambda_c) (round5_q1): open, retired as missing statements (they are at least as strong as the size deficit).

## The chain and the missing statement

No complete written proof or refutation of the [GOAL] claim is in hand.

**Chain.**
1. Entry 9 settles P1 (i)-(v) as posed. It remains to settle Part D at level (D-a).
2. Fix a proper ternary source (D, chi) and a shift d with S = span F_d(D) >= S_0. By entry 9 (iv) (heredity, round4_q6 Lemma B1) each class S_e(d) is a binary source of span <= S, and every fibre satisfies r_{S_e(d)}(l) <= v_l <= v_1 (round5_q2 Prop 2.1(a)).
3. Corollary F0 (round5_q6; new entry 55): every binary source of span <= S has size <= K_F(S) := min_{1<=lambda<=S} [N/Lam + sqrt(v_1 N)] (Lam = lambda+1, N = S+Lam), and K_F(S) >= sqrt(v_1 S). So 3K_F(S) is a sum of three separate, certified binary-source caps.
4. The missing statement FD(eta) below gives sum_e |S_e(d)| = |F_d(D)| <= 3(1-eta) sqrt(v_1 S) <= (1-eta)·3K_F(S).
5. That is the (D-a) inequality per shift, with delta = eta, the single named hypothesis S >= S_0, against the Fejer caps K_F. (Caveat for the consumer, not for the goal: the consumer's rank cap K may lie up to about 1% below K_F at the regime scale (round5_q6, heuristic numbers), so the saving against the consumer's own K is eta minus that gap.)
- MS' (entry 52) is retired: round5_q6 Proposition C proves MS'(delta) => SD(eta) (eta < delta), and SD(eta) => FD-type bounds by Cauchy-Schwarz, so MS' is at least as strong as FD and not a reduction of it.

**Missing statement FD(eta) (new OPEN ledger line, locator round6_plan).**
Let Q(m) (m >= 0) be the largest size of a Sidon set (all positive differences distinct; 3-term progressions excluded) inside m+1 consecutive integers, Q(m) = 0 for m < 0. FD asserts: there are explicit constants eta in (0,1) and S_0 >= 1 such that for every proper ternary source (D, chi) — a finite D ⊂ Z with a coloring chi of V(D) = {(v,u) : u < v; u, v in D} by P = {0,1,2} with no monochromatic directed L (x,y),(x+t,y),(x+t,y+t), t > 0, all three cells in V(D) — and every d >= 1 such that F_d(D) = {u : u, u+d in D} is nonempty and S := max F_d(D) - min F_d(D) >= S_0, one has

    |F_d(D)|  <=  3 (1 - eta) sqrt( v_1 S ),   where v_1 = Q(S-1) + Q(S-2).

(Equivalently sum_e |S_e(d)| <= 3(1-eta) sqrt(v_1 S), since the three classes S_e(d) partition F_d(D).)

**Why it should hold (director's sketch; candid).**
- Contrapositive. If |F_d(D)| >= 3(1-eta) sqrt(v_1 S), then T^2 <= 3 sum s_e^2 and Lemma F (windows Lam up to epsilon S) force each class X_e to have s_e >= (1-O(eta)) sqrt(v_1 S) (each s_e <= K_F), small window variance, and fibres r_{X_e}(l) >= (1-O(sqrt eta + epsilon)) v_l for most l <= epsilon S: each F_l(X_e) is two near-maximal Sidon sets at almost every lag up to a constant fraction of S.
- Then a pair p < y in X_e with y - p = L has about rho^2 L ≈ 2L/sqrt(S) inscribed pairs (p,p+t),(y-t,y) (rho = s/S ≈ sqrt(2) S^{-1/4}): typically many.
- Separation lemma (director; immediate from the inscribed-pair rule, round5_q2 Lemma 2.3): at each outer pair (p,y), all AGREEING inscribed pairs (psi(p,p+t) = psi(y-t,y)) carry the same colour, namely 1 - psi(p,y). Equivalently, with S_{t,t'} = {p : psi(p,p+t) = 0, psi(p,p+t') = 1} and E_{t,t'} = {y : psi(y-t,y) = 0, psi(y-t',y) = 1}, every p in S_{t,t'} and y in E_{t,t'} satisfy y <= p + max(t,t'), for every ordered lag pair t != t'.
- Under saturation the Golomb classes Z_0(t), Z_1(t) are near-maximal Sidon sets for every t <= epsilon S, so for random-like psi an outer pair would see both agreeing colours with probability 1 - O((3/4)^{rho^2 L}). The separation forces, for each lag pair, pattern-(0,1) ends to lie left of pattern-(0,1) starts (up to max(t,t')); points of X in the middle third are both starts and ends, and their start rows and end rows are tied together by the Sidon structure of every Z_j(t); a counting argument over lag pairs should show the patterns cannot be so separated for a positive proportion of lag pairs. That would be a single-class deficit SCF (|X| <= (1-eta) sqrt(v_1 S)), which implies FD at once.
- Fallback mechanism (three classes): the upper-row sets F_l(X_e), e in P, are pairwise disjoint, each avoids colour e at shift d+l, and the corners mixing classes (Lemma W(a)) couple their colourings; a joint separation lemma for the coupled structure (W, kappa) of entry 43.
- Risk: SCF improves the binary-source capacity itself and may hold only with tiny eta. A refutation of FD needs three binary sources of size about sqrt(2) S^{3/4} at one shift; no binary source larger than about sqrt(S) is known.

**Tried so far (on FD or its earlier, stronger wordings: joint per-lag bound entry 17, AD entry 29, MS entry 41, MS' entry 52).**
- round2_q4: mixed-quadruple pattern classification; Lemma F, AABA forcing; no bound.
- round3_q1: AABA/ABAA forbiddenness; forcing only.
- round3_q4: AD via corner exclusion with independence; prefix lemma, density obstruction; no correlation step.
- round2_q3, round1_q4: near-extremality hypotheses; energy route; conditional reductions only.
- round4_q1: chain audit, Bose six-translate obstruction (lag-by-lag additive information gives no delta).
- round4_q2: Lemma W / Corollary U; no single pattern forbidden; TSD reduction.
- round4_q3: chain audit, near-extremality transfer, lag-1 exclusions; row/column anti-correlation named.
- round4_q4 (partial): digit-product ceiling lead (now proved, round5_q4 Prop P).
- round4_q5: Fourier/uniformity: Lemma E, Lemma C, Obstruction O.
- round4_q6: Theorem A; window induction; shear to corners; decoupling remark.
- round5_q1, q2, q3 (closing task on MS'): chain audits (step-6 direction flaw fixed), single-window Theorem B, window-energy identity (MS'/WE equivalent to the size bound for equidistributed classes), Prop N / Prop 2.2 / P3 (counterexamples need classes >> sqrt S), inscribed-pair rule and corner agreement, cross-lag heuristic corrected; no proof.
- round5_q4 (refute MS'): Theorem N, Lemma K, Prop P (block/digit products cannot refute), difference colorings excluded; no counterexample; Problem SAT named.
- round5_q5 (single-lag core SL/TSD): SL => MS', Theorem T, gadget G1; counting lemma G1(t) open.
- round5_q6 (bare query): Fejer route (Lemma F, F0, Theorem B, Prop C): MS' implies the size deficit, so MS' is no reduction; recommended SD/FD as the target.

## Where the next round should concentrate (round 6, final)

**Progress test.** The last two rounds produced progress in the counted sense. Round 5 (round5_q6 Proposition C, Corollary C1, Lemma F / Corollary F0) proved universal results that replace the missing statement MS' by the strictly simpler FD (one inequality on |F_d(D)|: no prefixes, no lags, no slack term), with the chain re-derived above; round 4 gave Theorem A. The missing statement itself is not proved.
- Honest reading: FD is essentially the (D-a) clause in its cleanest form. Rounds 4-5 did not make Part D easier; they showed that every intermediate statement tried (MS, MS', WE) is at least as strong as FD.
- What differs from last round's sketch: last round located the deficit at a single lag (TSD gadgets); round5_q2 showed the multi-lag structure is dense, and the new sketch uses the outer-pair separation lemma across all lags of one class.

**Round 6 wave (final round; six queries).**
- q1 = q2 = q3: the closing task on FD (byte-identical), with P1 Part A, the Fejer material, the per-fibre cap, the inscribed-pair rule, Lemma W / Corollary U, Prop N and the sketch spliced in.
- q4: refute FD exactly as stated (wording new this round): an explicit family with |F_d(D)|/(3 sqrt(v_1 S)) -> 1; or, failing that, a proof that FD holds for a structural reason.
- q5: the hardest step of the sketch cut out: the single-class Fejer deficit SCF, with the separation lemma offered as a first move.
- q6: final-round allowance: an independent verification of the digit-family theorems of round2_q1 (Lemma A, Theorem B, Theorem D), the most intricate standing (D-b)-type result, so far resting on one written proof plus a script check for small k.
- If nothing settles FD, the final document presents the standing results above, P1 as the proved part of the goal, and FD as the clearly marked open statement.
