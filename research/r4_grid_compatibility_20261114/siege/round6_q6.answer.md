# round6_q6 answer: independent verification of the general digit family

Scope: I checked the spliced proof line by line, using only the definitions in it and in problem.md. I could not run the k = 2..6 computer check because no code execution was available, so no part of this verdict rests on it. I did not read round2_q1.md. The "repaired family" is therefore checked as it is described in the spliced text: three copies, tau = (0,1,3), one common h, |A_j| = k, rho(j) = j, in-copy colours from the table, cross corner 1, cross low cell 0.

## 0. Verdict (summary)

(a) **Properness.** The family is proper for every rho and every f, but only after one hypothesis is added that the Data list leaves out:

  **(H) every atom of copy c is < h_c.**

The text uses (H) when it writes "E_c ⊂ [0,h_c]", which it states as a consequence when it is really a hypothesis. Without (H) the table is ill-posed and the construction fails; an explicit monochromatic L is given in Section 1.3. With (H) added, Lemma A (the complete list of L's) and Theorem B are correct. That includes the mirrored L's with d > h/2, the L's with x = y, and the cross-copy L's.

There is one more caveat. The padded family of 2.1 with "any rho" is proper only under the general table (cross corner rho(c0)+1). Under the repaired cross colours (corner 1, low cell 0), padding copies of role 1 create monochromatic L's (Section 3.2).

(b) **Theorems B and D hold as stated**, with (H) imposed on the atoms of every copy. The following side claims are wrong or unproved, and none of them affects the main theorems:
- the "≥ 2k/(1+1.5/√(2k))-ish" aside in Theorem D is false;
- the claim that "B = 9 still does not embed by span" is false;
- the bound "h ≥ B^{3·2+1}" is off by one, and harmlessly so;
- the wording "no member of these families" must be restricted to the families that are actually used;
- the claim that "generic d is realized O(1) times" is asserted without proof. A sketch confirming it is given in Section 3.4.

## 1. Definitions

### 1.1 Base, exponents and the coefficient lemma

The coefficient lemma and its proof are correct. The proof only needs 0 < |c_m| < B, which is weaker than the stated |c_m| < B/2. For four points p0+p3-p1-p2, each point contributes at most ±1 to the coefficient of any given power B^m with m < M. The reason is that a point contributes alpha·h_c and sigma·a, and these two powers have distinct exponents. So |c_m| ≤ 4.

This uses the stated condition that atom exponents are pairwise distinct and distinct from all shift exponents. Shift values may coincide, and then the coefficients of the coinciding shift add, which is still ≤ 4 in absolute value.

The B^M coefficient is tau_{c0}+tau_{c3}-tau_{c1}-tau_{c2}. The Sidon property is used in the B_2 sense: all sums tau+tau' with tau ≤ tau' are distinct, repeated summands included. Under that reading it gives the multiset identity {c0,c3} = {c1,c2}. The set tau = (0,1,3) qualifies, since its pair sums 0,1,2,3,4,6 are all distinct.

Copy separation: all exponents are < M, so max h ≤ B^{M-1}. Since T_{c'} - T_c is a nonzero multiple of B^M, it is ≥ 100·max h > 2·max h. Given (H), the copies occupy the disjoint intervals [T_c, T_c+h_c], in the order of T.

### 1.2 Unique representation, and small below large (needs (H))

Assume (H). Two atoms a, a' of copy c are distinct powers of B below h_c, so a, a' ≤ h_c/B and a + a' < h_c. Hence

  small := {0} ∪ A_c  <  large := {h_c - a : a ∈ A_c^0},

elementwise, and the 2|A_c^0| elements alpha·h_c + sigma·a are pairwise distinct. So the representation is unique and E_c ⊂ [0,h_c].

The cell types are pairwise distinct, so the colouring is well defined. A cell is written by its (column offset, row offset), both in E_c, inside one copy:
- corner (h-a, a): large column, small row, and the column index equals the row index (x = y);
- mirror (h-x, y), x ≠ y: large column, small row, and x ≠ y;
- left (b, a), a < b: small column, small row;
- up (h-a, h-b): large column, large row.

All of these lie in V(D), because large > small; for left cells b > a, and for up cells h-a > h-b. Cross cells have row and column in different copies, so they cannot coincide with in-copy cells.

A cross corner (T_{c'}+h, T_c) never equals a cross low cell (T_{c''}, T_c). Equality would force T_{c''} - T_{c'} = h, which is impossible: T differences are multiples of B^M, and 0 < h < B^M. The pair (c, c') is recovered from the cell, so every listed cell receives exactly one colour, and every remaining cell of V(D) gets 0.

### 1.3 Gap: without (H) the construction fails (explicit L)

Take one copy, T = 0, h = B = 100, A = {B^2 = 10^4}, M = 3 (any rho, any f). Then E = {0, 10^4, 100, 100-10^4 = -9900}, so D = {-9900, 0, 100, 10000} and E ⊄ [0,h].

Consider the L with p0 = -9900, x = 0, y = 100, p3 = 10000. It satisfies x + y = 100 = p0 + p3, and the cells are (0,-9900), (10000,-9900), (10000,100).

Under the table:
- the corner cells C(a') = (h-a', a') are (100,0) and (-9900,10^4); the second is not even a cell of V(D);
- the only left cell is (10^4, 0);
- the only up cell is (100, -9900);
- the mirror cells (100,10^4) and (-9900,0) are not in V(D).

So all three cells of this L are "other" and coloured 0. **It is a monochromatic L.** (Shift by +9900 if nonnegative D is wanted.) The repair is to add (H) to the Data. In Theorem D this means that every copy at shift h_i uses atoms below h_i; putting all atom exponents below all shift exponents is the simplest way. With (H), everything below goes through.

## 2. Lemma A and Theorem B, inference by inference (assuming (H))

### 2.1 L parametrisation

The pair language used is exact. An L (X,Y),(X+t,Y),(X+t,Y+t) in V(D) corresponds to p0 = Y, x = X, p3 = X+t and y = Y+t. The conditions are p0 < x, p0 < y < p3, x < p3 and x + y = p0 + p3. The ordered pair (x,y) runs over both orders, so d = x - p0 > h/2 is included. The case **x = y** (d = h/2) is also allowed, and the written proof does not mention it. I checked it separately:
- Sidon step: unaffected.
- Same copy, all alpha = 0: the vector equation becomes e_{a0} + e_{a3} = 2e_{a_y}. This forces a0 = a3 or an impossible identity, so there is no L.
- Same copy, mixed alpha: one middle point is small and the other large, so x = y cannot occur.
- Cross copies: y and z lie in different copies, so x = y cannot occur.

So no L is missing on this account.

### 2.2 Sidon step

If c0 = c3, then c1 = c2 = c0. If c0 ≠ c3, then {c1,c2} = {c0,c3}, and p0 < p3 gives T_{c0} < T_{c3}. No other configuration is possible. Correct.

### 2.3 Same copy

The h_c-coefficient only receives contributions from the four points of this copy, so alpha0 + alpha3 = alpha_y + alpha_z. Its value is 0, 1 or 2, giving three cases.

- **Sum 0.** The sum of two members of {0} ∪ basis determines the multiset of the two summands: 0 gives {0,0}, e_i gives {e_i,0}, 2e_i gives {e_i,e_i}, and e_i+e_j gives {e_i,e_j}. So {y,z} = {x0,x3}, which contradicts strict betweenness. The written subcases a0 = 0 and a0 ≠ 0 are instances of this. Correct.
- **Sum 2.** The reflection x -> h - x reduces it to sum 0. Correct.
- **Sum 1.** By 1.2, x0 is small and x3 large; call y the small middle point and z the large one. The atom identity is e_{a0} + e_{a2} = e_{a1} + e_{a3}, so the multiset {a0,a2} equals {a1,a3}. Since a1 > a0, we get a0 = a3 =: a and a1 = a2 =: b > a. Conversely, every a < b in A^0 gives an L. Strict betweenness holds because a < b < h-b < h-a, and this ordering follows from small < large.
- **The two orders.** Order (x,y) = (b, h-b) gives S1: left (b,a), corner (h-a,a), up (h-a,h-b). Order (h-b, b) gives S2: M(b,a) = (h-b,a), corner, and M(a,b) = (h-a,b). The span is h - 2a. Correct.

### 2.4 Cross copies

Atoms of c0 appear only in p0 and y, so sigma0·e_{a0} = sigma_y·e_{a_y}. This gives a0 = a_y, and the signs agree when a0 ≠ 0.

- **a0 ≠ 0.** Then alpha0 = alpha_y, so y = p0, which is impossible.
- **a0 = 0.** Then x0, y ∈ {0, h_{c0}} with x0 < y, so x0 = 0 and y = h_{c0}.
- **a3 ≠ 0.** The same argument gives z = x3 directly, i.e. z = p3, which is already impossible. The written route via the shift coefficient is also valid: with x0 = 0, y = h_{c0} it gives alpha0 - alpha_y = -1, plus 0 from c3, which is ≠ 0.
- So z = 0 and x3 = h_{c3}. If h_{c0} ≠ h_{c3}, the h_{c0}-coefficient is -1, a contradiction. Hence the two shifts are equal, call the value h.
- **The L's.** The points are T_{c0}, T_{c0}+h, T_{c3}, T_{c3}+h. The two orders give X1 (arms C_{c0}(0), C_{c3}(0)) and X2 (arms (T_{c3},T_{c0}) and (T_{c3}+h, T_{c0}+h)). The second arm of X2 is an "other" cell, coloured 0, and this is irrelevant.

**Lemma A is complete. CONFIRMED (under (H)).**

### 2.5 Theorem B, for every rho and every f

- **S1:** the corner is rho(c) and the left cell is f_c(a,b) ≠ rho(c).
- **S2:** the corner is rho(c) and M(b,a) is rho(c)+1.
- **X1:** the corner is a cross corner (h_{c0} = h_{c3} was proved, so the rule applies), coloured rho(c0)+1. The horizontal end C_{c0}(0) is coloured rho(c0).
- **X2:** the corner is rho(c0)+1 and the low cell is rho(c0).

In each case the horizontal end differs from the corner, whatever rho and f are. **CONFIRMED.**

**Repaired special case** (three copies, rho(j) = j, cross corner 1, low cell 0):
- X1 is monochromatic only if j = j' = 1, which is impossible since j ≠ j'.
- X2 has corner 1 and low cell 0.

**CONFIRMED.**

## 3. Section 2 counts, Theorem D and the embedding remark

### 3.1 Identity (*) and Lemma C

**(*):** u ∈ F_{h-d}(S_e(d)) holds iff the four points u, u+d, u+h-d, u+h lie in D, chi(u+d,u) = e and chi(u+h,u+h-d) = e. Given the corner (u+h,u), the L is determined by d. Correct.

**Lemma C:**
- Cross-copy differences are ≥ B^M - max h > h.
- Same copy with h_c = h: E_c ⊂ [0,h] forces x = 0, and both 0 and h lie in E_c.
- h_c < h: impossible.
- h_c > h: in the equation (alpha1-alpha2)h_c + sigma1·a1 - sigma2·a2 - h = 0, the power h is neither h_c nor an atom, so its coefficient is -1. That is a contradiction.

**CONFIRMED.**

**Span-h L's:**
- Type S with a ≠ 0: h_c - h - 2a = 0 has a coefficient of -2 on a, which is impossible.
- Type S with a = 0: then h_c = h.
- Type X: the span exceeds B^M - max h > h.

So the L's with corner (T_c+h, T_c) are exactly S1 and S2 with a = 0, one pair for each b ∈ A_c. This gives m_{e,h}(T_c) = #{b : f_c(0,b) = e} + |A_c|·[e = rho(c)+1], and m_{rho(c)} = 0. **CONFIRMED.**

### 3.2 Section 2.1

**Cyclic:** m_{j+1}(T_j) = 2k, N_e = 2k, |R_e| = 1, sum m^2 = 4k^2. Correct.

**Balanced:** m_{j+1}(T_j) = k + ⌈k/2⌉ and m_{j+2}(T_j) = ⌊k/2⌋. So N_e = k + ⌈k/2⌉ + ⌊k/2⌋ = 2k, |R_e| = 2 for k ≥ 2, and sum m^2 = (k+⌈k/2⌉)^2 + ⌊k/2⌋^2. Correct.

UW(lambda) fails once 2k/3 > lambda. Correct.

**Padded:** |F_h| = 3+s, N_e = 2k, sum m^2 = 4k^2. The ratio is 4k^2 / (2k + 4k^2/(3+s)) = 2k(3+s)/(3+s+2k). Correct.
- s = k gives (2k/3)(k+3)/(k+1) ≥ 2k/3. Correct.
- s = ⌊√k⌋ gives N_e/|F_h| = 2k/(3+s) → ∞ and |R_e|/|F_h| = 1/(3+s) → 0. This kills union growth with liminf f > 0. Correct.

**Caveat (proved, explicit).** "Any rho" for the padding is valid only under the general table of Section 0. If the repaired cross colours (corner 1, low cell 0) are kept and a padding copy p has rho(p) = 1, take T_1 < T_p. Then X1 has corner (T_p+h, T_1) coloured 1, arm C_1(0) coloured 1 and arm C_p(0) coloured 1: **monochromatic**. The same happens for two padding copies of role 1. As a Section 0 instance (cross corner rho(c0)+1), the padded family is proper.

### 3.3 Theorem D

The construction is a Section 0 instance; (H) must hold for each copy, which is achievable. All taus are distinct members of one finite Sidon set, for example powers of 2.

For h = h_i ∈ W:
- By Lemma C, |F_h| = 3r + rs = r(3+s) ≥ k.
- N_e(h) = r·2k', coming from the r active copies of role e-1; padding copies and copies at other shifts contribute nothing.
- |R_e(h)| = r and sum m^2 = 4k'^2·r.
- min_e N_e/|F_h| = 2k'/(3+s) ~ 2√k'. Correct.
- With s = 0: ratio 4k/3 ≥ k and |F_h| = 3k. Correct.
- With s = ⌈√k'⌉: the energy ratio is 2k'(3+s)/(3+s+2k'), which is ~ 3+s → ∞, and sum|R_e| / sum|F_h| = 1/(3+s) → 0. Correct.

The quantities are identical for every h ∈ W, so every nonnegative weighting over W gives the same conclusions. **Theorem D CONFIRMED (under (H)).**

**Error in an aside.** The phrase "this is >= 2k/(1 + 1.5/√(2k))-ish" is false. The true value is 4k/(3+⌈√(2k)⌉) ~ 2√2·√k, not ~2k. The text then switches to s = 0 for the exact claim, so the theorem is unaffected.

**Caveat (correct as stated).** W is sparse, and interval averages with weights a_h are not refuted.

### 3.4 Section 3 parameters

- S_e(h_i) = {T_c : h_c = h_i, rho(c) = e}, because the corner C_c(0) has colour rho(c). Correct.
- r_{S}(l) ≤ 1 for these classes, because positive differences of a Sidon set are distinct. Correct.

**"Generic d is realized O(1) times"** is stated without proof. Here is a sketch, which is not a full proof. Take d ∉ {shift values}.

For d > B^M/2: d determines tau' - tau, hence the pair of copies (c, c'), hence the offset difference. The coefficient lemma then fixes the atoms and signs, leaving only the alpha ambiguity when an atom is 0 and the shifts are equal. That gives ≤ 4 representations.

For d < max h: the representation is within a single copy, because the atoms identify the copy. Some atom is involved, since d is not a shift power. The two-term multiset analysis gives ≤ 2 representations, coming from the pairs (b,a)/(h-a,h-b), (h-b,a)/(h-a,b), and (a,0)/(h,h-a).

So |F_d(D)| ≤ 4 off W is plausible. It is not part of the claimed theorems.

### 3.5 Section 4 (embedding)

Within the stated family (B = 100) the remark is correct. Under (H), the repaired family with k ≥ 1 and every Theorem D member have large spans:
- span ≥ (tau_max - tau_min)·B^M ≥ B^M, with M ≥ 1 + (number of distinct exponents used);
- for the repaired family with k = 2 that is M ≥ 7, so the span is ≥ 10^14.

This exceeds the largest side that a proper four-coloured square can have under the brief's excluded n = 21,987,409. The bound is cited from the brief, and properness is inherited by sub-squares. So these members are not diagonal classes. **CONFIRMED.**

The following must be corrected:
- **Off by one.** "h ≥ B^{3·2+1}" should read h ≥ B^{3k} = B^6. Atoms can use exponent 0. The conclusion is unaffected, because the span bound comes from B^M.
- **"No member of these families" is too broad.** The general family has trivial members, for example one copy with A = ∅ and h = 1, so D = {0,1}, which embed. The claim must be restricted to the repaired family and the Theorem D families.
- **The B = 9 aside is false.** With B = 9, k = 2, atom exponents 0..5, h = 9^6, M = 7 and tau = (0,1,3), the span is 3·9^7 + 9^6 = 14,348,907 + 531,441 = 14,880,348. That is **less than** 21,987,408, so span alone does not exclude it. The quoted "3·9^9" corresponds to M = 9, which is not minimal. Whether that 18-point set can occur as a diagonal class is not settled here. (B = 9 does satisfy the needs of the coefficient lemma; in fact B ≥ 5 suffices, given |c| ≤ 4 < B.)

## 4. Final verdict

- **(a)** Proper exactly as stated: **no, but the gap is repairable.** Add hypothesis (H). Without it, Section 1.3 gives an explicit monochromatic L: D = {-9900, 0, 100, 10000}, cells (0,-9900), (10000,-9900), (10000,100), all coloured 0. With (H), proper for every rho and every f. The L-list of Lemma A is complete, including the mirrored L's (d > h/2), the case d = h/2, and the cross-copy L's. For the padded family, "any rho" must use the general table.
- **(b)** Theorems B and D hold as stated under (H). Lemma C, the counts N_e, |R_e| and sum m^2, and the refutations of UW(lambda), of the U1 energy bound and of union growth (pointwise and W-averaged) are all confirmed. Weaken or correct:
  - the 2k/(1+…) aside;
  - the B = 9 embedding aside, which is false;
  - h ≥ B^7, which should be h ≥ B^6;
  - "no member", which must be restricted to the families used;
  - the generic-d O(1) claim, which is only sketched.
- **Not checked:** the k = 2..6 computer check (no code execution), and the original text of round2_q1 for the repaired family.

=== END OF ANSWER round6_q6 ===
