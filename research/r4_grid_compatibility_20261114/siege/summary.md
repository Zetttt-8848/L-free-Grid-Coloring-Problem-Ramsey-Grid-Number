# Running summary after round 2 (written at the round-3 plan step)

## Goal (ledger entry 1, OPEN; unchanged)
P1 (i)-(v) exactly as posed, plus Part D settled at level (D-a) [an explicit-delta proportional-loss inequality with every hypothesis named] or (D-b) [an explicit, L-by-L checkable family of proper ternary sources showing that no request-based inequality of that kind can hold, with classes as large as the regime requires]. (D-c) is a separate OPEN line (entry 6) and not part of the goal. No complete proof of the goal exists, so the audit rule is not triggered. Ledger entries 18-29 were added at this step.

## Established

### P1 is proved (round1_q1, most complete; round1_q3 and round1_q4 agree; entry 9)
- Lemma 0. Every directed L inside V(D) is L(u,d,h) for exactly one triple with 1<=d<h: horizontal end (u+d,u), corner (u+h,u), vertical end (u+h,u+h-d), arm length h-d. It lies in V(D) iff u, u+d, u+h-d, u+h ∈ D. d ranges over all of [1,h-1], including d > h/2 (mirrored L's).
- (i) L(u,d,h) is monochromatic of color e iff u ∈ F_{h-d}(S_e(d)) ∩ S_e(h). So chi is proper iff S_e(h) ∩ R_e(h) = ∅ for all h, e. Uses all L's.
- (ii) R_e(h) ⊆ F_h(D). (iii) k(u) = #{e : u ∈ R_e(h)} <= 2; u ∈ R_e ∩ R_{e'} forces u ∈ S_{e''}(h); sharp identity sum_e |R_e(h)| = 2|F_h| - 2#{k=0} - #{k=1}.
- (iv) The shifted source of X = S_e(d) avoids e via L(a,d,d+(b-a)); F_l(X) ⊆ R_e(d+l); the classes G_f = F_l(X) ∩ S_f(h) are Sidon (3-APs included; round1_q1 proves it with four L's L1-L4); F_l(X) ∩ R_{e'} ⊆ G_{e''}; F_l(X) ∩ R_{e'} ∩ R_{e''} = ∅.
- (v) The chain uses only same-shift, same-class instances (binary-source property, Golomb split, partition of F_d(D)). New content: the union over d in R_e(h), (ii), (iii), and the cross-color parts of (iv).
- Useful reformulations (director, elementary):
  - u ∈ F_{h-d}(S_e(d)) iff the L with corner (u+h,u) has both arms of color e (round2_q1 (*)).
  - Row/column form: with w_u(x) = chi(u+x,u) and c_v(x) = chi(v,v-x), chi is proper iff for all u<v in D, h = v-u, and every d with u+d, v-d ∈ D, NOT w_u(d) = c_v(d) = w_u(h).
  - Agreement identity: with z_d(u) = chi(u+d,u), sum_e r_{S_e(d)}(l) is the lag-l agreement count of z_d on F_d(D), and sum_e N_e(h) = sum_{d<h} sum_e r_{S_e(d)}(h-d) = #{L's with corner offset h whose arms agree}.

### Single-shift structure (round1_q3, entry 12)
- D1: given the lower-shift classes, the shift-h L's are satisfiable iff R_0(h) ∩ R_1(h) ∩ R_2(h) = ∅.
- D2: single-shift counting only bounds |F_h(D)| from below. A proportional saving needs union growth |R_e(h)| > (2/3)|F_h| for all three e on an a-weighted share of h, or a multi-shift / joint-fiber argument.
- D3: per-class near-extremality refutations save only additively. The useful hypothesis is the averaged H_avg(eta), whose negation is the consumable saving.

### Energy facts
- Conditional reduction (round1_q4, entry 13): if sum_u m_{e,h}^2 <= C1 N_e + C2 N_e^2/|F_h| for all three e with C2 < 3/2, then min_e N_e(h) <= (2C1/(3-2C2))|F_h|.
- Forced energy (round2_q3 Lemma B, entry 25): in every proper source and every h, some color e has sum_u m_{e,h}(u)^2 >= (3/2) N_e(h)^2/|F_h(D)| (Cauchy-Schwarz plus min_e |R_e(h)| <= (2/3)|F_h|). So any energy bound with C2 < 3/2 must be color-asymmetric, or must track which color is minimal as h varies.
- round2_q3 also named H_avg(eta) and H_fib(eta) precisely (H_fib: sum_{l<=l_0} r_{S_e(d)}(l) >= (1-eta) sum_{l<=l_0} v_l(L-d)). It proved Lemma C (heavy start: for e-requests at d_1<...<d_m, the points u+(d_j-d_i) and u+l_i-(d_j-d_i) avoid S_e(d_i)), judged by itself a dead end (density 1/48 makes the exclusions automatic). Row, column and diagonal colorings are not proper at regime size (dead end as no-go models).

### Collision lemma (director, entry 15)
If u ∈ F_{h-d}(S_e(d)) ∩ F_{h-d'}(S_e(d')), d<d', then u+(d'-d) ∉ S_e(d) and u+(h-d') ∉ S_e(d) (L's L(u,d,d') and L(u+h-d',d,d')). Not yet turned into a bound.

### D-b: the digit families (round2_q1; entries 18-22; checked by the director)
- General digit family: copies c with shift h_c, role rho(c), atom set A_c (atoms smaller than h_c; implicit in round2_q1 and required), A_c^0 = A_c ∪ {0}. Atoms and shifts are distinct powers of B >= 9; T_c = tau_c B^M with tau a Sidon set; D = ∪_c T_c + (A_c^0 ∪ (h_c - A_c^0)).
- Coloring: corner C_c(a) = (T_c+h_c-a, T_c+a) gets rho(c); left (T_c+b,T_c+a) and up (T_c+h_c-a, T_c+h_c-b), a<b, get f_c(a,b) ≠ rho(c); mirror cells (T_c+h_c-x, T_c+y), x≠y, get rho(c)+1; cross corner (T_{c'}+h, T_c), T_c<T_{c'}, equal shifts, gets rho(c)+1; cross low cell (T_{c'},T_c) gets rho(c); everything else 0.
- Lemma A (coefficient lemma plus Sidon): the L's are exactly (S1), (S2) within copies (two per a<b, corner C_c(a)) and (X1), (X2) across equal-shift copies. Theorem B: proper for every rho, f. Lemma C: F_h(D) = {T_c : h_c = h}; the start T_c gets |A_c| requests of color rho(c)+1 from (S2) plus one request of color f_c(0,b) per atom b from (S1).
- Director's check (scratchpad scripts digit3.py, digit4.py; evidence only): 150 random instances (1-3 shifts, 2-6 copies, equal roles allowed) have no monochromatic L. A two-shift k=3 instance with one padding copy gives |F_h| = 4, N_e = (6,6,6), |R_e| = (1,1,1) at both shifts, as claimed. NOTE: my first test put atoms above the shift and produced monochromatic L's; that is outside the construction (E_c must lie in [0,h_c]).
- Consequences (PROVED):
  - UW(lambda) is false for every lambda (cyclic three-copy family: N_e = 2k, |F_h| = 3).
  - The U1-type energy bound is false for every C (padding s = k).
  - Union growth with positive liminf is false (padding s ~ sqrt k gives N_e/|F_h| ~ 2 sqrt k and |R_e|/|F_h| -> 0).
  - Theorem D: all three fail simultaneously on any finite set W of m shifts.
- Scope:
  - |D| = O(log span), classes of size r or O(1), fibers r_{S_e(d)}(l) <= 1, and the span is at least about 9^9.
  - Hence the families are NOT in the regime and NOT embeddable in a proper four-colored square (span exceeds 21,987,408).
  - Crucially, these families have min_e N_e(h)/(h|F_h(D)|) -> 0. So they leave alive the statement the consumer actually needs: min_e N_e(h) <= c h |F_h| with c below about 1/146. (Under H_fib, N_e(h) ≈ v h, and |F_h| <= 3K gives a contradiction exactly when c < v/(3K) ≈ 1/146.)
- Surviving variants (entry 23): polynomial class sizes; fibers >= 2 on many lags; interval averages at fixed window t; density of D; the "c h" form above. round2_q1 judged that digit designs cannot reach fibers >= 2 (heuristic only).
- Judgment: (D-b) "as posed" (classes as large as the regime requires) is NOT met. The families settle the sparse, arbitrary-source variants only.

### D-c (round1_q1, round2_q2; entries 6, 14, 24)
- Easy part: A = F_l(X) ∩ R_{e'}(h) ⊆ G_{e''} and B ⊆ G_{e'}; both are Sidon and disjoint. (C1)-(C3) are consistent with r_X(l) = 2Q (abstract model), so imbalance needs generating L's.
- Single-L coupling lemma (round2_q2, proved): the only L's containing a Golomb cell C_w = (w+h,w) and a witness cell (u+d',u) or (u+h,u+h-d') of a foreign-requested u are L(w,d',h) with w = u ∓ (h-d'), i.e. w's own request L. They never constrain membership in G'. Any imbalance must come from chains of >= 2 L's through free cells.
- round2_q2 conjectures (unproved) that a digit realization of balanced, fully foreign-requested classes exists at log scale.

### Joint fiber bound (round2_q4; entries 16, 17, 26, 27, 28)
- The two same-corner-color pieces G_e^f, G_{e'}^f need not have a Sidon union (entry 16; explicit witness D=[0,10) in the round-2 queries).
- Lemma F (proved): for p<q in pieces with the same corner color f, C(p,q) = (q+h,p) is the corner of L(p,h,h+q-p), whose ends are both f, so C(p,q) ≠ f. If p and q are in the same class e, C(p,q) is a shifted-source cell of S_e(d), so it is the third color.
- AABA (a, a+r, a+r+s in class e; a+s in e'): every corner-triangle cell is forced. C(a,a+r) = C(a,a+r+s) = C(a+r,a+r+s) = e', and C(a+s,a+r+s) = C(a,a+s) = e. No monochromatic L has been found yet; forbiddenness is OPEN (entry 28).
- Evidence: AABA and ABAA were never observed in random proper sources (n <= 16); ABBA, AAAB, ABBB, AABB and ABAB were observed.
- Consumer deduction (proved): sum the rank-neighbor inequality over the three classes S_e(d) with a common rank c < min s_e. This gives 2P(H_tot; w) + 12 sum_i (c-i) e_{i+1} <= 3L'c(c+1), where w_l = sum_e r_{S_e(d)}(l) and H_tot = sum_e (c s_e - c(c+1)/2). So a joint bound w_l <= (1-delta)3v_l lowers the joint cap of each main-color triple, hence U_d. delta' as a function of delta has not been computed.

### Agreement framing (director, round-3 plan; heuristic except the identities)
- Regime arithmetic:
  - D_c has density ≈ 1/4 (some diagonal color covers >= n/4 cells), and |F_h| ≈ n/16.
  - Lambda(h) := #{L's with corner offset h} ≈ h|F_h|/16 ≈ 8.6*10^4 h, while sum_e N_e(h) ≈ 3vh ≈ 2.8*10^4 h.
  - So the agreement rate is ≈ 1/3, the rate of a random coloring. "All binary caps nearly attained" means "the words z_d have random-like lag agreement", and a proportional agreement deficit is a proportional joint fiber deficit, consumable via the summed rank inequality.
- Heuristic for a deficit: for each pair u<v, the corner color w_u(h) is never an agreement color between w_u and c_v. Independent words would therefore agree at rate 2/9 only, and rate 1/3 needs positive row/column correlation. Sparse digit designs achieve agreement rate 1, so any valid deficit needs a density or near-cap hypothesis (entry 29).
- Bounding Lambda(h) through a ternary capacity of windows of length h does not help. In the regime D_c has density 1/4 in windows, which gives min_e N_e/(h|F_h|) ≈ 1/48 > 1/146. The missing factor is exactly the agreement deficit.

## Dead ends (and why)
- U1 and UW(1) (pre-registered witnesses; entries 3, 4). Now also UW(lambda), U1-type energy and union growth, for every constant, over arbitrary sources (entries 20, 21).
- Single-shift counting (D2).
- Sidon union of the same-f pieces (entry 16): the naive factor-2 joint saving is dead. Disjoint difference sets alone give no saving either.
- Imbalance from (C1)-(C3) alone (abstract model), and from any single L (entry 24).
- Lemma C exclusions by themselves (density makes them automatic).
- Row-, column- and diagonal-structured colorings as no-go models (not proper at size).
- Ternary-source capacity as a bound on Lambda(h): a factor 3 short.

## Open gaps between the state and the goal
1. (D-a) An explicit-delta proportional loss under named hypotheses: agreement deficit (entry 29), joint fiber bound (entry 17), union growth (entry 7), or a window-averaged color-asymmetric energy bound (entry 8). The consumer-side deduction is in place (entry 27); the missing piece is a structural inequality.
2. (D-b) A family meeting the surviving variants (entry 23): fibers >= 2, polynomial class sizes, interval averages, the "c h" form, density. Classes as large as the regime requires are likely out of reach of explicit construction: by the corners theorem dense sources have bounded span, and the binary caps K are not known to be nearly attained.
3. Mixed patterns AABA / ABAA (entry 28), as a step toward a joint fiber bound.
4. (D-c) An explicit balanced, fully foreign-requested realization, or a multi-L imbalance (entry 6).

## Where the next round should concentrate (round 3 wave: four attempt queries)
- q1: settle AABA and ABAA (forbidden, with an L-chain, or an explicit witness), and derive the pair bound if they are forbidden.
- q2: (D-c) an explicit digit realization of balanced, fully foreign-requested Golomb classes for every k, or a multi-L imbalance.
- q3: (D-b) extend the digit families to fibers of multiplicity >= m and larger classes with a large request ratio (variants (b), (a)), or prove an obstruction.
- q4: (D-a) the arm-agreement deficit (AD) under a named density/near-cap hypothesis, with the consumer link, or an explicit refutation.
- Escalation (state.md: ESC_ROUND=4) will likely require the next plan step to name a single missing statement. The strongest candidate is (AD) / the joint fiber bound.
