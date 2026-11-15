# Running summary after round 3 (written at the round-4 plan step)

## Goal (ledger entry 1, OPEN; unchanged)
P1 (i)-(v) exactly as posed, plus Part D settled at level (D-a) or (D-b).
- (D-a): an explicit-delta proportional-loss inequality sum_e |S_e(h)| <= (1-delta)(sum of separate binary caps), per h or a_h-averaged, with every hypothesis named.
- (D-b): an explicit, L-by-L checkable family of proper ternary sources showing that no request-based inequality of that kind can hold, with classes as large as the regime requires.
- (D-c) is a separate line (entries 6, 35, 39), not part of the goal.
- No complete written proof of the goal is in hand, so the audit rule is not triggered. The escalation rule applies from this round on.

## Standing results (never dropped)
1. **P1 (i)-(v), complete (entry 9; round1_q1 Part A is the cleanest chain; round1_q3 and round1_q4 agree).**
   - Lemma 0: every L in V(D) is L(u,d,h), 1<=d<h, with cells (u+d,u), corner (u+h,u), (u+h,u+h-d), arm length h-d; it lies in V(D) iff u, u+d, u+h-d, u+h ∈ D.
   - (i) L(u,d,h) is monochromatic of color e iff u ∈ F_{h-d}(S_e(d)) ∩ S_e(h).
   - (ii) R_e(h) ⊆ F_h(D).
   - (iii) Double cover, with the sharp identity sum_e |R_e| = 2|F_h| - 2#{k=0} - #{k=1}.
   - (iv) The shifted source avoids e; F_l(X) ⊆ R_e(h); the Golomb split by four L's; F_l(X) ∩ R_{e'} ⊆ G_{e''}; F_l(X) ∩ R_{e'} ∩ R_{e''} = ∅.
   - (v) Accounting.
2. Single-shift satisfiability: the shift-h L's are satisfiable iff R_0 ∩ R_1 ∩ R_2 = ∅. Single-shift counting bounds |F_h| only from below (entry 12, round1_q3).
3. Conditional energy reduction: if the energy bound holds with C2 < 3/2 for all e, then min_e N_e <= (2C1/(3-2C2))|F_h| (entry 13, round1_q4).
4. Forced energy: some color e has sum m^2 >= (3/2)N_e^2/|F_h| (entry 25, round2_q3).
5. Collision lemma (entry 15, round2_plan).
6. Single-L coupling lemma (entry 24, round2_q2).
7. Lemma F, and the forcing of five triangle cells for AABA (entry 26, round2_q4) and for ABAA (round3_q1, entry 30); r = s is impossible for both (round3_q1).
8. Summed rank-neighbor inequality 2P(H_tot;w) + 12 sum_i (c-i)e_{i+1} <= 3L'c(c+1), with joint multiplicity w_l = sum_e r_{S_e(d)}(l) (entry 27, round2_q4).
9. Prefix formula and prefix-dominated sufficiency (entry 33, round3_q4).
   - P(H;w) = sum_{lambda>=0} max(0, H - C_w(lambda)), where C_w(lambda) = sum_{l<=lambda} w_l.
   - Hence C_w(lambda) <= C_{w'}(lambda) for all lambda implies P(H;w) >= P(H;w').
   - So a prefix-averaged joint deficit sum_{l<=lambda} sum_e r_{S_e(d)}(l) <= (1-delta) sum_{l<=lambda} 3v_l suffices for the summed rank inequality with w' = (1-delta)3v.
   - Director's addition (elementary, from the prefix formula with real multiplicities): P(H; alpha w) = alpha P(H/alpha; w). The integer rounding of alpha w_l is not yet handled. The conversion delta -> delta' has NOT been computed.
10. Digit families (entries 18-22, round2_q1). The general family is proper for every choice of roles and arm colors. Over arbitrary sources it refutes:
    - UW(lambda) for every lambda;
    - the U1-type energy bound for every C;
    - union growth with positive liminf;
    and it does so simultaneously on any finite set of shifts. It is not embeddable (span > 21,987,408).
11. Lifted digit family (round3_q3; entries 31, 32). D = L·D_base + G with G a fine Sidon block of size 3r, colors twisted by the labels s_g. It is proper (Lemma 0', Lemma E, Theorem F). On every shift H of a set W of m' shifts:
    - min_e N_e(H) >= lambda|F_H|;
    - sum_e |R_e(H)| = |F_H|;
    - the energy ratio is unbounded;
    - the request-producing classes and their fibers at the request lags have size >= c·span^alpha, for every alpha < 1/2.
    - Director's check (scratchpad r3q3.py; evidence only): 9 instances with p in {5,7}, 1-2 copies, k = 2-3; 0 monochromatic L among up to 2772 L's; N_e = 2kr exactly as claimed.
    - Not embeddable (k >= 360 is needed for ratio 240).
12. (D-c+) is refuted for arbitrary sources (round3_q2; entries 34, 35). An explicit family, proper L by L, has a fiber F_l(S_0(d)) of 2k points:
    - the two Golomb classes are balanced (k each);
    - every point is foreign-requested (A = G'', B = G').
    - Director's check (scratchpad r3q2.py; evidence only): k = 1, 2, 3 give 0 monochromatic L's; the Golomb colors and request colors are as claimed.
13. Density obstruction, MODULO the corners theorem cited from memory (entry 36, round3_q4). For fixed rho > 0, no proper ternary source has D of density >= rho on an interval of length >= S(rho). S(rho) is non-explicit, so the statement is useless at the scale 2.2*10^7.
14. Director's lemma, color Cauchy-Schwarz (entry 37, round4_plan; proved below; numerically sanity-checked on random sets). Let Y = F_d(D), let w >= 0 be supported on [1,t], and put a_k = sum_i w_i w_{i+|k|} >= 0. Then
    - sum_{k∈Z} a_k r_Y(k) <= 3 sum_e sum_{k∈Z} a_k r_{S_e(d)}(k), with r_X(0) = |X| and r_X(-k) = r_X(k);
    - with the per-class caps r_{S_e(d)}(l) <= v_l this gives sum_{l>=1} a_l r_{F_d(D)}(l) <= a_0 |F_d(D)| + 9 sum_{l>=1} a_l v_l.
    - Proof: sum_k a_k r_X(k) = sum_x (1_X ⋆ w)(x)^2, and pointwise (sum_e y_e)^2 <= 3 sum_e y_e^2.
    - Meaning: r_{F_d(D)}(l) = #{u : u, u+d, u+l, u+l+d ∈ D} is the "rectangle count" of D. In the regime both sides are about 8.5*10^4 (the regime sits at equality of the color Cauchy-Schwarz). This is a second-order analogue of the outer inequality. Equality forces the three classes to be locally equidistributed at window scale t. By itself it gives no saving.

## Dead ends (each a REFUTED statement with its refuting file)
- U1 (entry 3, d1 witness). UW(1) (entry 4, d1 witness).
- round1_q2's original digit family being proper (entry 10, round1_q2: its mirrored L's are monochromatic).
- UW(lambda) for every lambda (entry 20, round2_q1).
- U1-type energy for every C, and union growth with positive liminf, over arbitrary sources, also on finite shift sets (entry 21, round2_q1).
- The union of the same-corner-color pieces G_e^f ∪ G_{e'}^f is Sidon (entry 16, explicit witness on D = [0,10)).
- (D-b)-type variants refuted by the lifted family (entry 32, round3_q3):
  - every inequality hypothesizing fiber multiplicity >= m at the request lags (variant b);
  - every inequality hypothesizing class sizes >= c·span^alpha with alpha < 1/2 (variant a below 1/2).
- (D-c+) without near-extremality hypotheses (entry 35, round3_q2): "|A| >= alpha|G''| implies |G'| <= (1-beta)|G''|" fails for all alpha <= 1 and beta > 0.
- Fixed-density counter-families at unbounded span (entry 36, round3_q4, modulo the corners theorem).

## Open gaps (set aside, not refuted)
- **(D-b) at regime size.** This means class sizes about 98 sqrt(span), fibers near 2 sqrt(span), the a_h-weighted interval average, and density 1/4 at span about 2.2*10^7 (entry 38).
  - Product/digit designs reach only a tiny constant times sqrt(span).
  - Explicit constructions at regime size look out of reach.
- **AABA / ABAA forbiddenness (entry 28).** round3_q1 shows that even forbidding both gives no proportional saving by counting alone. This is deprioritized.
- **(D-c) under the near-extremality hypotheses (H1)-(H3) of round3_q2 (entry 39)**, and multi-L imbalance chains.
- **Union growth and anti-collision under saturation (entry 7).** The sparse refutations do not touch the saturated regime.
- **Arm-agreement deficit (AD), entry 29.** It is subsumed by the missing statement below: its prefix form is the joint deficit.
- **The conversion delta -> delta'.** This is elementary but not done.

## The chain and the missing statement

**Chain.**
1. Entry 9 settles P1 (i)-(v) as posed. It remains to settle Part D at (D-a).
2. Fix a shift d and the three classes S_e(d), each a binary source of span <= S := max F_d(D) - min F_d(D).
   - Entry 27 gives the summed rank-neighbor inequality with joint multiplicity w_l = sum_e r_{S_e(d)}(l).
   - Entry 33 gives the prefix form: if C_w(lambda) <= C_{w'}(lambda) for every lambda, then the summed inequality holds with w replaced by w'.
3. The missing statement MS (below) gives exactly that domination with w' = (1-delta)·3v.
4. Hence 2P(H_tot; (1-delta)3v) + 12 sum_i (c-i)e_{i+1} <= 3S c(c+1) for every admissible c. By the scaling identity P(H; alpha w) = alpha P(H/alpha; w) (real multiplicities; rounding to be handled), this is the single-class rank inequality at total size sum_e s_e with the multiplicities scaled by (1-delta).
5. Optimizing c as in the certification of K gives sum_e |S_e(d)| <= (1-delta')·3K(S) with explicit delta' > 0 (heuristically delta' ≈ 1 - sqrt(1-delta) ≈ delta/2, from P ~ H^2/(2w)).
   - This is the (D-a) inequality per shift d, for every proper ternary source, with no hypothesis.
   - Applied to each main color c in the square, it lowers U_d by the factor (1-delta').
6. What remains after MS: the explicit computation of delta' in step 5. It is an elementary finite optimization, not a structural question.

**Missing statement (MS; ledger entry 41, OPEN, locator round4_plan).**
Let Q(m), for m >= 0, be the largest size of a Sidon set (no a+b = c+d except trivially, 3-term progressions included) contained in m+1 consecutive integers, and put Q(m) = 0 for m < 0. MS asserts: there is an explicit absolute constant delta > 0 such that the following holds for every proper ternary source (D, chi), i.e. every finite set D ⊂ Z with a coloring chi of V(D) = {(v,u) : u < v, u,v ∈ D} by P = {0,1,2} having no monochromatic directed L (x,y),(x+t,y),(x+t,y+t), t > 0. For every d >= 1 with F_d(D) ≠ ∅, write:
- S = max F_d(D) - min F_d(D);
- v_l = Q(S-l) + Q(S-l-1), the per-class fiber cap of the consumer;
- S_e(d) = {u ∈ F_d(D) : chi(u+d,u) = e};
- r_X(l) = #{u ∈ X : u+l ∈ X}.

Then for every integer lambda with 1 <= lambda <= S,

    sum_{l=1}^{lambda} sum_{e∈P} r_{S_e(d)}(l)  <=  (1-delta) · sum_{l=1}^{lambda} 3 v_l.

Equivalently, the lag-l agreement counts of the word z_d(u) = chi(u+d,u) on F_d(D), summed over l <= lambda, fall a fixed proportion short of three times the summed single-class caps.
- For small S the statement holds trivially, since r_{F_d(D)}(l) <= S-l+1 is far below 3v_l. Its content lies at large S.
- It is a universal statement and carries no hypothesis.

**Why it should hold (director's sketch; heuristic).**
- Equality in MS needs all six Golomb pieces G_e^f(l) = F_l(S_e(d)) ∩ S_f(d+l), e ≠ f, to be near-maximal Sidon sets for most l <= lambda.
- Near-maximal Sidon sets are Fourier-uniform and equidistributed (Erdős–Turán, Lindström type).
- By entry 37, in the regime the color Cauchy-Schwarz is near equality, so the three classes are locally equidistributed in F_d(D).
- Candidate mechanism (corner exclusion with uniformity): every start u ∈ G_e^f(l) has corner (u+h,u) of color f, while its two arms both have color e.
  - Uniformity of the pieces makes the row word w_u and the column word c_v asymptotically independent on the non-corner colors. This should push the agreement rate toward 2/9 rather than 1/3.
  - Equivalently, in the request picture, saturation makes the request sets R_e(h) of all three colors exceed (2/3)|F_h|, which contradicts the double cover (iii).
- Concretely: show that saturation of the six pieces at lags l <= lambda forces some two pieces with equal corner color f to share additive quadruples at a positive rate. Lemma F plus the forced AABA/ABAA triangles would then give monochromatic L's at a positive rate.
- A proof would plausibly be a counting (Cauchy-Schwarz / Fourier) argument with explicit, possibly tiny, delta.
- Risk: MS may be false if near-cap ternary sources exist with a perfectly 1/3 random-like agreement. No such source is known, and none is excluded.

**Tried so far (on MS or earlier wordings: entry 17 joint per-lag bound, entry 29 AD).**
- round2_q4: pattern classification of mixed additive quadruples. It gave Lemma F, the AABA forcing, and the refutation of the Sidon union (entry 16); no bound.
- round3_q1: AABA/ABAA forbiddenness. Only forcing was found (r = s degenerate; ABAA triangle forced). It showed that forbidding both patterns gives no saving by counting.
- round3_q4: AD via corner exclusion with independence. It gave the prefix sufficiency lemma and the density obstruction; the correlation step was not achieved.
- round2_q3: near-extremality hypotheses H_avg, H_fib and the Lemma C exclusions; no deficit.
- round1_q4: energy route; conditional reduction only.

## Where the next round should concentrate

**Progress test.** Rounds 2-3 produced no proof of the missing statement and no proof of the goal.
- They did produce new PROVED universal results that shorten the chain on the consumer side:
  - the summed rank inequality (entry 27, round 2);
  - the prefix sufficiency lemma (entry 33, round 3), which weakened the needed per-lag joint bound to a prefix-averaged one.
- This counts as progress, but only on the consumption side. The structural core (any joint deficit at all) had no progress in rounds 2-3.
- The sparse/product refutations narrow the D-b side only.
- What differs this round: the missing statement is posed for the first time, in its weakest consumable (prefix) form. The sketch now names a uniformity / Cauchy-Schwarz mechanism, anchored by the new equality-case observation (entry 37), instead of local pattern-forbidding.

**Round 4 wave (escalation; six attempt queries, all on MS).**
- q1-q3: identical closing task on MS. It carries P1's key lemmas, the Golomb split with proof, Lemma F, the AABA/ABAA forcing, the prefix lemma with proof, the summed rank inequality, entry 37, and the chain.
- q4: refute MS exactly as stated (an explicit family with prefix joint ratio -> 1), or derive something false from it.
- q5: the hardest step of the sketch: saturation of the six pieces implies a positive rate of monochromatic L's (the uniformity / corner-exclusion counting step), posed as a self-contained claim through the Fourier / Cauchy-Schwarz approach.
- q6: bare query (MS plus the cited statements only). It must derive the chain itself, then attack MS by a first move none of the listed attempts used, or report the derivation flawed.
- Next round: if any of q1-q3 or q5 proves MS, the [GOAL] goes PROVED with the conversion delta -> delta' still needed. Check whether the closing answer supplies it. If it does not, the delta' computation becomes the next missing statement (the chain then needs it).
