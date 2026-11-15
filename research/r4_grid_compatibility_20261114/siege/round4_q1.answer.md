# round4_q1 answer: the prefix-averaged joint fiber deficit (MS)

## Plan / statement attempted
- Goal: prove MS with an explicit delta, or refute it with an explicit source checkable L by L.
- Steps: (1) audit the chain MS => (D-a) and make steps 2-5 exact (I re-checked the earlier worker's Section 1 and reproduce it with my own proofs); (2) find out how much of MS the chain actually needs (new: additive error and truncation in lambda are free); (3) show which ranges of lambda are automatic; (4) find the obstruction to a proof of MS in the remaining range.
- Outcome (summary; details below): MS is **neither proved nor refuted**. Proved: the chain audit; a strictly weaker sufficient statement MS*(E, Lambda); automatic validity of MS at large lambda; a proof that the additive constraints alone (six pairwise disjoint Sidon pieces per lag) cannot give any delta.

## 1. Audit of the chain MS => (D-a) (PROVED)

Notation. For a weight u = (u_l)_{l>=1} with u_l >= 0, put C_u(lambda) = sum_{1<=l<=lambda} u_l (so C_u(0) = 0), and for real x >= 0
   P_u(x) = sum_{lambda>=0} max(0, x - C_u(lambda)).
**Prefix lemma (quoted; I re-checked the proof).** If H is an integer with H <= sum_l u_l and u is integer valued, then P_u(H) is the sum of the H smallest elements of the multiset with u_l copies of l. Proof: if t_1 <= ... <= t_H are those elements, sum_k t_k = sum_{lambda>=0} #{k : t_k > lambda}, and #{k : t_k <= lambda} = min(H, C_u(lambda)). ∎

**Lemma 1.1.** (a) P_{(1-delta)u}(x) = (1-delta) P_u(x/(1-delta)) for 0 <= delta < 1. (b) P_{3u}(3x) = 3P_u(x). (c) P_u is nondecreasing in x, and P_u(x) >= P_{u'}(x) whenever C_u <= C_{u'} pointwise.
*Proof.* Termwise: max(0, x-(1-delta)C) = (1-delta)max(0, x/(1-delta) - C); max(0,3x-3C) = 3max(0,x-C); max(0, x - C) is nondecreasing in x and nonincreasing in C. ∎

**Proposition 1.2.** Fix a proper ternary source, a shift d, the classes X_e = S_e(d) with sizes s_e, all of span <= S. Let e_j be the span lower bounds used by the single-class certificate (valid for the hereditary family of binary sources: a subset of a binary source is a binary source, since the restriction of a proper colouring is proper). Let 1 <= c < min_e s_e, s̄ = (s_0+s_1+s_2)/3, H̄ = c s̄ - c(c+1)/2. Put w_l = sum_e r_{X_e}(l). If C_w(lambda) <= (1-delta) C_{3v}(lambda) for all lambda >= 0, then
   2 P_{(1-delta)v}(H̄) + 4 sum_{i=0}^{c-1} (c-i) e_{i+1} <= S c(c+1).    (1.2)
*Proof.* For each e the rank-neighbour inequality gives 2 Sigma_e + 4 sum_i (c-i)e_{i+1} <= S c(c+1), where Sigma_e is the sum of the H_e = c s_e - c(c+1)/2 selected differences (rank <= c) of X_e. The selected differences of X_e at value l are distinct pairs of X_e at distance l, so at most r_{X_e}(l) of them. Hence the union over e of the selected multisets is a sub-multiset of the multiset with w_l copies of l, of cardinality H_tot = sum_e H_e = 3H̄ (an integer) <= sum_e C(s_e,2) = sum_l w_l (because c < s_e gives H_e <= C(s_e,2)). So sum_e Sigma_e >= P_w(3H̄) by the prefix lemma. Summing the three inequalities: 2P_w(3H̄) + 12 sum_i (c-i)e_{i+1} <= 3Sc(c+1). By Lemma 1.1(c), (b): P_w(3H̄) >= P_{(1-delta)3v}(3H̄) = 3P_{(1-delta)v}(H̄). Divide by 3. (For lambda > S, r_{X_e}(lambda) = 0, so domination for lambda <= S, which is MS, gives it for all lambda.) ∎

**Consequences and precisions (checked).**
- (1.2) is the single-class certificate for the *mean* class size, with caps v_l replaced by (1-delta)v_l. Let K^{(delta)}(S) be the capacity it certifies. Under MS: sum_e |S_e(d)| <= 3K^{(delta)}(S), provided the chosen c is < min_e s_e. If some s_e <= c, then sum_e s_e <= 2K(S) + c, which is harmless when c << K(S). This case split must be stated; it is not a flaw.
- In the square, the triple at main colour c gets the cap 3K^{(delta)}(n-d-1) in place of the staggered sum_{j} K(n-d-j-1); the staggering can be re-inserted only with an explicit additive correction, which must be computed. Not a flaw.
- delta' := 1 - K^{(delta)}/K is not a universal function of delta; it comes from rerunning the certificate. Heuristic (not proved): if v_l is roughly constant over the lags used, P_v(x) ≈ x^2/(2v̄), the e-term is lower order, and s̄ scales like sqrt(1-delta), so delta' ≈ delta/2 (and somewhat less with the e-term). I cannot run the recertification here; **delta' is not computed**.

**Audit verdict.** The chain MS => (D-a) is correct (with the two stated precisions). It is, however, wasteful: it asks much more than it uses. Section 2 makes this exact.

## 2. What the chain really needs: MS*(E, Lambda) (PROVED reduction)

**Lemma 2.1 (additive error and truncation are free).** Let w, w' >= 0 be lag weights, H >= E >= 0 reals, and Lambda := min{lambda >= 0 : C_{w'}(lambda) >= H - E} (assume it exists). If
   C_w(lambda) <= C_{w'}(lambda) + E   for every 0 <= lambda < Lambda,
then P_w(H) >= P_{w'}(H - E).
*Proof.* Since C_{w'} is nondecreasing, max(0, H-E-C_{w'}(lambda)) = 0 for lambda >= Lambda, so P_{w'}(H-E) = sum_{lambda<Lambda} max(0, H-E-C_{w'}(lambda)). For lambda < Lambda, H - C_w(lambda) >= H - E - C_{w'}(lambda), hence max(0, H - C_w(lambda)) >= max(0, H-E-C_{w'}(lambda)). Sum over lambda < Lambda and drop the (nonnegative) terms lambda >= Lambda of P_w(H). ∎

**Proposition 2.2 (weakened sufficient statement).** In the setting of Proposition 1.2, suppose that for some delta in [0,1), E >= 0,
   (MS*)  C_w(lambda) <= (1-delta) C_{3v}(lambda) + E   for all lambda < Lambda,  where Lambda = min{lambda : (1-delta)C_{3v}(lambda) >= 3H̄ - E}.
Then
   2 P_{(1-delta)v}(H̄ - E/3) + 4 sum_{i=0}^{c-1}(c-i)e_{i+1} <= S c(c+1).    (2.2)
*Proof.* As in 1.2, 2P_w(3H̄) + 12 sum(c-i)e_{i+1} <= 3Sc(c+1). Lemma 2.1 with w' = (1-delta)3v, H = 3H̄ gives P_w(3H̄) >= P_{(1-delta)3v}(3H̄ - E) = 3P_{(1-delta)v}(H̄ - E/3) (Lemma 1.1(b)). Divide by 3. ∎

**Reading of (2.2).** Since H̄ - E/3 = c(s̄ - E/(3c)) - c(c+1)/2, (2.2) is the certificate (1.2) for the shifted mean s̄ - E/(3c). Hence, under MS*, sum_e |S_e(d)| <= 3K^{(delta)}(S) + E/c (same small-class proviso). So:
1. **Only lambda < Lambda matters.** Lambda is fixed by the rank c of the certificate; heuristically Lambda ≈ 3H̄/(3v̄) ≈ c s̄/v̄. (In the problem's heuristic regime this is the "saturated up to l ≈ 3.5*10^5" range, i.e. c of order 7*10^3; this numerical identification is heuristic.) Lags beyond Lambda are irrelevant.
2. **Small lambda is irrelevant.** Any deficit failure confined to lags with 3C_v(lambda) <= E costs only E/c in the final cap. With c ~ 7*10^3 and a target loss delta'·3K ~ 0.005·1.4*10^6, E may be ~ 5*10^7, i.e. MS may fail completely on all lags l up to a few thousand (3C_v(lambda) ≈ 2.8*10^4·lambda) without hurting (heuristic arithmetic, regime numbers).
3. **Consequence for refutations.** A counterexample to MS at lambda = 1 (or any bounded lambda) would refute MS as stated but **not** the statement the consumer needs. The right target is MS* with E = eta·H_tot for a small explicit eta, on lambda in [lambda_E, Lambda). I recommend replacing MS by:

**MS\* (recommended target).** There are explicit delta > eta >= 0 (with delta/2 - eta > 0 bounded away from 0) such that for every proper ternary source and every d, with (c, s̄, H̄) the rank and mean used by the certificate at span S,
   C_w(lambda) <= (1-delta) C_{3v}(lambda) + 3 eta H̄   for every lambda < Lambda.
By (2.2) with E = 3 eta H̄, the mean satisfies the certificate with H̄ replaced by (1-eta)H̄ and v by (1-delta)v. Heuristic first-order reading (P ≈ x^2/(2v̄), e-term neglected): s̄ scales by sqrt(1-delta)/(1-eta), so delta' ≈ delta/2 - eta. MS is the special case eta = 0, Lambda = S+1 of MS*, and is strictly stronger.

## 3. MS is automatic at large lambda (PROVED, conditional only on the definition of K)

**Lemma 3.1.** Let K(L) be the maximum size of a binary source of span <= L (any certified upper bound may be used). For every proper ternary source and every d, C_w(lambda) <= sum_e C(s_e, 2) <= 3 C(K(S), 2). Hence MS holds, for the given delta, at every lambda with (1-delta)C_{3v}(lambda) >= 3C(K(S),2).
*Proof.* C_w(lambda) counts pairs inside the classes at distance <= lambda, so it is at most the total number of pairs, sum_e C(s_e,2). Each X_e = S_e(d) is a binary source (iv.0) of span <= S, so s_e <= K(S). ∎
At S ≈ 2.2*10^7 with K ≈ 4.58*10^5 and 3v_l ≈ 2.8*10^4 this covers only lambda >~ 1.1*10^7 (regime numbers), far above Lambda. So Lemma 3.1 does not touch the needed range; it only shows that MS's content lies at lambda <~ S/2, and by Section 2 the consumer's content lies in [lambda_E, Lambda).

## 4. The six pieces per lag, and why additive information alone gives no delta (PROVED)

Fix d, l >= 1, h = d+l. For e != f put G_e^f = F_l(S_e(d)) ∩ S_f(h). By (iv), F_l(S_e(d)) = G_e^{f} ⊔ G_e^{f'} ({f,f'} = P \ {e}), each piece is Sidon, so w_l = sum of the six piece sizes.

**Lemma 4.1.** The six pieces are pairwise disjoint subsets of [m, M-l], where m = min F_d(D), M = max F_d(D).
*Proof.* (e,f) != (e2,f2): if e != e2 the pieces lie in the disjoint sets S_e(d), S_{e2}(d); if e = e2 then f != f2 and they lie in the disjoint sets S_f(h), S_{f2}(h). A start u of F_l(S_e(d)) has u >= m and u+l <= M. ∎

**Proposition 4.2 (the additive model saturates).** For every prime power q >= 7 there are six pairwise disjoint Sidon sets B_0,...,B_5 ⊆ [0, q^2-2], each of size q. Since Q(m) <= m^{1/2} + O(m^{1/4}) (Erdős–Turán / Lindström upper bound, cited from memory), q/Q(q^2-2) -> 1. Hence, at a single lag, the constraints "six pairwise disjoint Sidon pieces in an interval of length S-l" are compatible with sum of piece sizes = (1-o(1))·3v_l; **no proof of MS can use only Lemma 4.1 and the Sidon property of the pieces** (lag by lag).
*Proof.* Let theta generate F_{q^2}^*, N = q^2-1, and B = {a in Z/N : theta^a - theta in F_q} (Bose). |B| = q, since theta + x != 0 for x in F_q (theta ∉ F_q). *Sidon mod N:* if a-b ≡ a'-b' with a != b, write theta^a = theta+x etc.; then (theta+x)(theta+y') = (theta+x')(theta+y). As 1, theta are F_q-independent and theta^2 cancels, x+y' = x'+y and xy' = x'y. Put m = x'-x = y'-y; then x(y+m) = (x+m)y gives m(x-y) = 0, and x != y, so m = 0, (a,b) = (a',b'). *Missing differences:* F_q^* = {theta^k : (q+1) | k}; for a != b in B, theta^{a-b} = (theta+x)/(theta+y) ∈ F_q^* would force x = y; so (q+1) ∤ (a-b) (well defined since (q+1) | N). Put B_j = B + j(q+1) mod N, j = 0..5 (distinct mod N since 6 < q-1). If B_j ∩ B_k != ∅ (j<k) then a - b ≡ (k-j)(q+1) with a,b in B, and a != b since 0 < (k-j)(q+1) < N; contradiction. Translates of a Sidon set mod N are Sidon mod N, and integer representatives in [0,N-1] of a Sidon set mod N form an integer Sidon set (an integer relation a+b = c+d reduces mod N). ∎

So a proof of MS (or MS*) must use **L-constraints coupling different pieces**, i.e. corner cells (q+h, p) with p, q in different pieces (Lemma F and its AABA/ABAA consequences), or constraints across different lags l of the same word z_d, or cells outside the shifted source of F_d(D). I checked that Lemma F forbids, among additive quadruples u_1 + v_2 = v_1 + u_2 inside G_e^f ∪ G_{e'}^f ({e,e',f} = P), only the all-one-piece patterns (already excluded by Sidon): an L (v_1+h,u_1),(v_2+h,u_1),(v_2+h,u_2) has a forced colour on a cell only when the two indices of that cell lie in the same piece (A-A gives e', B-B gives e), and all three cells forced to the same colour needs u_1,v_1,u_2,v_2 in one piece. All mixed patterns only propagate colours (as in AABA/ABAA). This is the obstruction I met: the known forcing never closes into a contradiction, so it yields no counting loss.

## 5. MS depends only on the shifted triangle of F_d(D) (PROVED) and an open extension question

Let Y = F_d(D) and T_d(Y) = {(v+d, u) : u <= v, u, v in Y} (diagonal u = v included; these cells lie in V(D) since u < v+d and u, v+d in D). The quantities in MS (S, the classes S_e(d) = colour classes of the diagonal cells (u+d,u), and their fibers) are functions of chi restricted to the diagonal of T_d(Y). The facts used so far (iv.0, Golomb split, Lemma F) use only L's whose three cells lie in T_d(Y) — check: the L's of (iv.0), (iv.2) and Lemma F have all cells of the form (b+d, a) with a <= b in Y.
**Restriction lemma.** If (D,chi) is a proper ternary source, chi restricted to T_d(Y) is a proper colouring of T_d(Y) (an L in T_d(Y) is an L in V(D)). ∎
**Open (extension).** Is every proper 3-colouring of T_d(Y) (for every finite Y) the restriction of a proper ternary source? If yes, MS is equivalent to a statement about properly 3-coloured non-strict shifted triangles, and a counterexample could be sought in that smaller setting; if no, a proof of MS must use L's with cells outside T_d(Y) (e.g. via the cross-shift requests R_f(h) of (i)-(iii)). I did not settle this.

## 6. Status

**Proved (complete proofs above):**
- Sec. 1: the chain MS => per-shift (D-a) is correct, with the small-class case split and the staggering correction stated; MS gives sum_e |S_e(d)| <= 3K^{(delta)}(S).
- Sec. 2: Lemma 2.1 / Prop. 2.2: the chain needs only MS*(E, Lambda): domination with an additive error E (costing E/c in the cap) and only for lambda < Lambda, Lambda determined by the certificate's rank c. A failure of MS at bounded lambda (e.g. lambda = 1) does not refute what the consumer needs.
- Sec. 3: MS holds automatically for lambda with (1-delta)C_{3v}(lambda) >= 3C(K(S),2).
- Sec. 4: the six pieces per lag are pairwise disjoint; six disjoint near-maximal Sidon sets exist (Bose translates), so lag-by-lag additive information cannot give any delta; Lemma F forbids no mixed additive pattern.
- Sec. 5: MS is a statement about the restriction of chi to the shifted triangle T_d(F_d(D)).

**Not obtained:** a proof of MS or MS* with explicit delta; an explicit counterexample to MS (I found no construction whose properness I could verify by hand: any violation needs, at some lag, six pieces of total size close to 3v_l ≈ 6 S^{1/2}, hence S >~ 50 already at lambda = 1, too large for a hand-checked L-by-L witness without an algebraic structure, and I found no such structure). delta' as a function of delta is not computed (heuristic delta' ≈ delta/2, or delta/2 - eta under MS*).

**Open questions (explicit):**
1. MS, and the weaker MS* of Sec. 2 (the consumer's real need), for explicit delta (> 2 eta).
2. Whether AABA/ABAA configurations (Sec. 4 context) are forbidden; even if they are, a counting argument converting this into a proportional loss is missing.
3. The extension question of Sec. 5.
4. Whether a single binary source can have all fibers r_X(l) close to v_l for l <= Lambda (if not, the single-class cap K is itself improvable, independently of MS).
No statement about R_4 is made beyond the implication: MS (or MS* with delta' > 0 after recertification) would lower U_d by the factor (1-delta') and, via the sensitivity model, lower the excluded side; neither hypothesis is established.

=== END OF ANSWER round4_q1 ===
