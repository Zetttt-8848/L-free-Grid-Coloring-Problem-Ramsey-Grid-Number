# r3_verify: step-by-step check of the draft

Scope: every section of the draft between the markers was checked by hand. The earlier partial file contained only a plan; nothing in it was reused. Hand computations below are evidence for exactly what they check.

## Verdict on the four main statements

1. **"Part P1 (i)-(v) is proved completely": CORRECT.** Every step of Lemma 0, (i), (ii), (iii), (iv.0)-(iv.3) and the per-fibre cap follows as written. Only a wording imprecision in (v) (minor item m1).
2. **"Part D is NOT settled": CORRECT.** No proportional-loss inequality (D-a) is proved, and no regime-size counterexample (D-b) is given. The body says this consistently.
3. **"The listed partial results toward Part D are proved": CORRECT IN SUBSTANCE, with one overclaim in the Status section (S1 below) and a few overstated summary phrases (m4, m5).** Every theorem, lemma and proposition in Sections 2-4 checks out.
4. **"No bound on R_4 is claimed": CORRECT.** Section 5 is a conditional implication, its hypotheses (FD(η,S_0) with explicit S_0, certification c(S) ≤ K(S−j), recertified capacities) are named, and HEURISTIC and HYPOTHETICAL labels are used where needed.

**Fatal errors: none found. Serious: one (S1), a Status overclaim that does not affect any theorem.**

## Section 1 (Theorem 1), checked

- **Lemma 0.** (a) With x = u+d, y = u, t = h−d, the cells are (u+d,u), (u+h,u), (u+h,u+h−d). Correct. (b) The three cells need the pairs {u,u+d}, {u,u+h}, {u+h−d,u+h} in D, with the order conditions automatic. Correct. (c) x > y because (x,y) ∈ V(D), and the map is injective. Correct. Color rule: the vertical end is (w+d,w) with w = u+h−d. So (★) holds, and m_{e,h}(u) counts the L's with corner (u+h,u) and both arms of color e. Correct.
- **(i)** follows from (★) and the uniqueness in (c). The L's are described precisely: corner offset h, arms on offset d, arm length h−d. The inductive form is correct: the cells at offset h form the set F_h(D), they are colored independently, and R_e(h) depends only on offsets < h. The sentence "constrains |F_h| only from below" is informal (m9).
- **(ii)** Correct. u ∈ S_e(d) ⊆ D, and u+h = (u+h−d)+d ∈ D.
- **(iii)** Correct, and so is the sharp identity Σ k(u) = 2#{k=2} + #{k=1} = 2F − 2#{k=0} − #{k=1}. "At most two of three" is derived, not imported.
- **(iv.0)** L(a,d,d+b−a) has cells (a+d,a), (b+d,a), (b+d,b). Correct. The translate of an L of V(X) by d is again a directed L of V(D). Correct.
- **(iv.2)** I rechecked all four L's coordinate by coordinate.
  - L1 = L(u_1,h,h+r) has end cells of color f. Its corner is ψ(u_1, u_1+l+r), and u_1+r+l ∈ X because u_1+r ∈ F_l(X). So the corner is g.
  - L2 is the same with u_1+s.
  - L3: its vertical end (u_1+h+r+s, u_1+s) is exactly the corner of L2. So the corner of L3 is f.
  - L4 is then monochromatic.
  - The case r = s is included.
  - The equivalence of the "no u_1, r, s" form with the Sidon property: put u_1 = a, r = a'−a, s = b'−a. This is correct.
- **Per-fibre cap.** F_l(X) lies in [m, m+S−l]. The class that misses m lies in S−l consecutive integers, so it has at most Q(S−l−1) elements. This gives v_l. Correct.
- **(iv.3)** Correct.
- **Lemmas 1.1-1.3.** Both L's in 1.1 were rechecked. They are L(u,d,d') and L(u+h−d',d,d'), with vertical end (u+h,u+h−d) ∈ S_e(d). Correct. Lemma 1.2 is Lemma 0 for X, and Corollary 1.3 follows. Correct.

## Section 2, checked

- **Prop 2.1 and Prop 2.2.** The algebra is correct: 3N ≤ 2C_1F + 2C_2N. The sentence after Prop 2.2 does not follow from it (m2).
- **Digit family.**
  - The coefficient lemma is correct. Each point carries at most one shift power, with α ∈ {0,1}, and at most one atom power, with σ = ±1. So every coefficient below B^M is at most 4 in absolute value.
  - The table is well defined. A corner and a mirror both have a large column and a small row, but they differ in whether the atoms are equal. A cross corner never equals a cross low cell.
  - (H)-failure example. Here D = {−9900, 0, 100, 10000}, and (0,−9900), (10000,−9900), (10000,100) is an L with t = 10000. None of its cells is a left, up, corner or mirror cell. All three are "other" cells, colored 0. Confirmed.
  - **Lemma 2.3.** Rechecked case by case.
    - Sum 0 and sum 2 are correct: a sum of two elements of {0} ∪ {powers} determines its summands.
    - Sum 1: a_0 + a_2 = a_1 + a_3, and a_0 ≠ a_1, give (S1) and (S2). The identification M_c(b,a) = (T+h−b, T+a) is correct.
    - Cross copies: the atom of p_0 can only cancel against y, which forces y = x_0 unless a_0 = 0. The four points are then T_{c0}, T_{c0}+h, T_{c3}, T_{c3}+h, with equal shifts. The two orders are (X1) and (X2).
    - The list is complete.
  - **Theorem 2.4** is correct for all four types.
  - **Lemma 2.5** is correct. It needs h to be a shift value, which it is, so the coefficient of h is −1 when h_c > h. The L's with a ≠ 0 have span h_c − 2a, which gives coefficient −2 on a.
  - **Theorem 2.6** counts are correct.
    - The active copy of role e−1 has m_e = k' + k' = 2k'. The other copies have m_e = 0.
    - The energy ratio is 2k'(3+s)/(3+s+2k').
    - With s = ⌈sqrt k'⌉, all three ratios behave as claimed.
  - Hand count, evidence only. The two-shift instance with k' = 2, r = 1, s = 1 has 2·(3·6 + 2) = 40 points. Its L's number 3·2·6 = 36 of type (S1)/(S2) plus 2·2·C(4,2) = 24 of type (X1)/(X2), so 60 in all. Both numbers agree with the draft.
  - **Embedding.**
    - The span is at least B^M ≥ B^4 = 10^8. Correct.
    - For k = 2: 7 exponents give M ≥ 7. Correct.
    - For B = 9, with τ = {0,1,3}, M = 7 and shift 9^6, the span is 3·9^7 + 9^6 = 14,348,907 + 531,441 = 14,880,348. This matches the draft.
- **Lifted family.**
  - χ_B is proper: no arm of (S1) or (S2) is a corner cell.
  - Lemma 2.7 is correct. The 3-term relation forces one copy. Then either the atom forces b_0 = b_3, or the parity of α_0 + α_3 contradicts 2α_m.
  - The Erdős–Turán Sidon proof is correct. Reducing mod 2p gives q_a + q_b = q_c + q_d exactly. Then the sums and the products agree mod p, and p is odd.
  - Lemma 2.8: cases A (R1, R2) and B (I, II, III) are complete.
  - Theorem 2.9: all five rows were rechecked.
    - III: mono would need s = s' and t = s+1, but s = s' gives t = s+2.
    - R2: s = s' forces t = s+2.
    - R1: the arms are t+2 and the corner is in {t, t+1}.
  - Theorem 2.10 is correct.
    - F_H uses the uniqueness of the representation Lb+g.
    - The types with g_3 ≠ g_0 have span ≢ 0 mod L.
    - The type-II lifts give m = 2k[s_g = e−1].
    - The fibre cells are the diag lifts of left and up cells, colored 1 + s_g = e.
  - Corollary 2.11: 4k^2/(2k + 4k^2/3) = 6k/(3+2k) → 3, and |R_e|/|F| = 1/3. Correct.
  - Limitation. The (X2) base L has three cross cells, all colored 1, so it is monochromatic. Confirmed.

## Section 3, checked

- **Prop 3.1** and the abstract obstruction are correct.
- **Theorem 3.2.** Fully rechecked.
  - Same block. In the basis (d,l,d'_i), all 21 pair sums, doubles included, were listed by hand. The only coincidence is (1,1,0) = 0+h = d+l = d'_i+w_i. This gives exactly six L's, including the two with outer pair (d'_i, w_i). All six colorings are as stated, using [h,d] = [h,d'_i] = [w_i,l] = 0.
  - Cross blocks. The d'_i-digit argument forces Δ^0. In order 1 the only nonzero same-block cell on Δ^0 is [h,0]. All order-2 subcases were rechecked, including (d,l) with (d,l): its colors are 1, 2, κ(l,l) = 2, so it is not monochromatic.
  - Hand count, evidence only. Each pair of blocks has 10 quadruples with equal gap g ∈ {d, l, h, l−d}, and each quadruple gives two orders. So the total is 12k + 20·C(2k,2), which is 32, 144 and 336 for k = 1, 2, 3. This matches the draft's computer counts.
  - The fibre: F_d(D) = {u_i, u_i+l}, and F_l(X) = {u_i}. The request is u_i ∈ F_{w_i}(S_{c̄_i}(d'_i)), via [d'_i,0] and [h,w_i]. Then A = G_2 and B = G_1 by (iv.3). Correct.
- **Prop 3.3** is correct up to an additive 1 (m3).

## Section 4, checked

- **Lemma 4.1.**
  - (Q-up) holds: (1 + sqrt(1+8m))/2 ≤ 1 + sqrt(2m).
  - (Q-low) holds. Bertrand's postulate (for n ≥ 2 there is a prime with n < p < 2n) is stated correctly. Then p > x and p < 2x, so 2p^2 < 8x^2 = m, and G_0 ⊂ [0,m].
  - The consequence v_1 ≥ sqrt(S)/2 holds for S ≥ 34. The last step needs only S ≥ 4.
- **Lemma 4.2 and Corollary 4.3.** Correct. The support has at most span X + Λ points, and 2Σ_{l≤λ}(Λ−l) = λΛ. K_F^♯ is also correct.
- **Lemma 4.4.**
  - Λ = ⌈S^{5/8}⌉ satisfies 2 ≤ Λ ≤ 2S^{5/8} ≤ S for S ≥ 34.
  - The excess is (1 + 2 sqrt 2) S^{−3/8} = 3.828… S^{−3/8} < 3.83 S^{−3/8}. Correct.
  - Numerics, recomputed approximately. The value c = 4.548·10^5 is right. The optimal Λ ≈ S sqrt(2/c) ≈ 46,100 gives an excess of about 955, i.e. 0.21%. For K_F^♯ the optimal Λ ≈ S/sqrt c gives an excess of about sqrt c ≈ 674, i.e. 0.15%.
  - The proved ξ(2.2·10^7) is 0.0068.
- **Theorem 4.5.** Correct as stated, against K_F.
- **Prop 4.6.** (a) The S_0 formula is correct. (b) Correct. (c) Correct; Q(m) ~ sqrt m is a classical fact, correctly flagged as CITED/conditional.
- **Prop 4.7.**
  - (a) Correct: S/N ≥ 1 − Λ/S, and (1−θ)^2 ≥ 1 − 2θ.
  - (b) Correct: Markov with total weight λΛ/2.
  - (c) Correct; the "+1" is superfluous (m8).
  - The heuristic numbers 0.034/0.089 and 0.044/0.107 are reproduced.
- **Prop 4.8.**
  - (a) Correct: ξ(2700) ≈ 0.198, so η ≈ 0.6007.
  - (b) Correct.
  - (c) Correct. Here sqrt(Q(S−1)S) ≥ S^{3/4}/2, and the ratio Q/v_1 ≤ Q/(2Q−1).
- **Remark on difference-colored sources** and the Hilbert-cube consequence. Correct.

## Section 5, checked

- X_d ≤ 12(1−η)c(n−1−d) + 4S_0 is correct.
- The threshold S_0 ≤ 6·10^5 η is sufficient; the exact value is about 6.8·10^5 η.
- The extra certification step c(S) ≤ K(S−j) is named.
- Numerics recomputed:
  - margin about 0.7%;
  - v_1 ≈ 9,517 gives c ≈ 4.574·10^5, a margin of about 0.13%;
  - K_F against 4.58·10^5 at v_1 = 9,350 / 9,400 / 9,450 / 9,517 gives about −0.8% / −0.5% / −0.26% / +0.09%;
  - K_F^♯ at v_1 = 9,517 gives about +0.03%.
- No overclaim: "Nothing in this document proves FD" is accurate.

## Errors and gaps, by severity

**Fatal.** None.

**Serious.**
- **S1 (Status, second bullet: "None of these sources can be a diagonal class of a properly four-colored square").** The body proves this only for two sets of sources:
  - the Theorem 2.6 families with B = 100 (span ≥ 10^8);
  - lifted instances with ratio ≥ 240 (Section 2.3).

  It is false as a proved statement for the lifted family in general. With m' = 1, k = 1, B = 100 we get D_base = {0,1,99,100}, of span 100. For p = 199, L = 158,405 and the span of D is below 101·L ≈ 1.6·10^7 < 21,987,407. For p = 3 the span is only about 3,700. The span argument excludes none of these, and their embeddability is not settled.

  Fix: restrict the sentence to "the Theorem 2.6 families (B = 100) and the lifted instances with N_e/|F_H| ≥ 240". The main claim is not affected, because no theorem uses this sentence.

**Minor.**
- m1 ((v) Accounting). "(iv.0), i.e. (i) restricted to the L's L(a,d,h') whose two arms lie on offset d" describes only the avoidance part of (iv.0). The properness of ψ uses the translated L's, whose two arms lie on a common offset x−y+d > d. Fix: name both families.
- m2 (after Prop 2.2). "So any energy bound with C_2 < 3/2 must be color-asymmetric" does not follow from Prop 2.2 alone. It follows from Prop 2.1 together with Theorem 2.6. In fact Theorem 2.6 already refutes symmetric bounds for every constant. Also, Prop 2.2 is undefined when F_h(D) = ∅.
- m3 (Prop 3.3, "lowers r_X(l) below v_l by the same amount"). It does so only up to the additive term Q(S−l) − Q(S−l−1) ≤ 1.
- m4 (Status, third bullet, "saturated fibres over all short lags"). Prop 4.7 gives saturation only on all but a weighted fraction O((η+ε+S^{−3/8})/β) of the lags l ≤ εS.
- m5 (Status, "against certified single-class caps"). Theorem 4.5 is proved only against the Fejér caps K_F, not against arbitrary certified caps such as the consumer's rank caps K.
- m6 (Section 6). Several items carry PROVED language but are not proved in the document, contrary to the stated label convention:
  - the rank-based conversion ("was also proved");
  - "Any violation of MS' needs classes of size > S^{5/8}/16";
  - the doubling remark "it turns the task into a proper 3-coloring of the full grid Y × Y".

  Fix: label them "recorded from earlier rounds, not proved here" or HEURISTIC.
- m7 (Section 5, citation). Lindström's bound, as I recall it, is F(N) < N^{1/2} + N^{1/4} + 1 for subsets of {1,…,N}. Since Q(m) = F(m+1), the correct form is Q(m) < sqrt(m+1) + (m+1)^{1/4} + 1. The difference is numerically negligible.
- m8 (Prop 4.7(c)). The inequality Q(S−1) ≤ Q(S−2) + 1 is not needed.
- m9 ((i), inductive form). "Single-shift counting therefore constrains |F_h(D)| only from below" is an informal reading, not a theorem.

**Presentational.**
- In Lemma 2.3, "y" names both the vertical middle point and the small middle offset.
- In Prop 3.1, "never stronger than the per-fibre cap" compares bounds on different quantities.
- The Status list of computer checks is evidence only, as the draft says. My hand counts confirm the L counts 60, 32, 144 and 336, and the B = 9 span 14,880,348.

## Is the main claim proved?

Yes, with the corrections above. The overclaim S1 and the summary phrases m4 and m5 are in the Status section, not in any theorem.
- Part P1 (i)-(v) is proved.
- Part D is correctly reported as unsettled.
- All theorems and propositions in Sections 2-4 are proved as stated in the body.
- No R_4 bound is claimed.

The open core is still FD(η,S_0), or SCD for binary sources. No construction refutes interval averaging with the weights a_h or the regime-size statements.

=== END OF ANSWER r3_verify ===
