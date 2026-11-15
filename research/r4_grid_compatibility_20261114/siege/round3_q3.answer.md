# round3_q3: lifting the digit family by a fine Sidon block (kills (b), and (a) for every exponent < 1/2)

Plan: lift the digit family to D = L*D_base + G, where G is a fine-scale Sidon set and the colors are twisted by g.
Each start u is replaced by |G| starts that share one request pattern. These starts form fibers of multiplicity about |G| at the request-producing lags.
Every L of the lifted set is listed (both middle orders), and properness is checked type by type.

## 1. Construction

**Base.** Take the digit family of section 0 of the quoted answer with these choices:
- copies c = 1..m', each with k atoms (|A_c| = k);
- pairwise DISTINCT shift values h_c (distinct powers of B, B = 100);
- distinct Sidon tau_c.

By Lemma A, the cross case forces h_{c0} = h_{c3}. So with distinct shifts the only L's of D_base are S1(a,b) and S2(a,b), for a < b in A_c^0, inside a single copy.

Binary base coloring: chi_B(b',b) = 0 if (b',b) is a corner cell C_c(a) = (T_c+h_c-a, T_c+a), and chi_B(b',b) = 1 for every other pair b < b' of D_base.
- No arm cell of S1 or S2 is a corner cell. A left cell has a small column offset. An up cell has a large row offset. A mirror (h-x, y) with x ≠ y would need x = y. Each of these is a coefficient mismatch.
- So every base L has corner 0 and arms 1. Hence chi_B is proper.

**Lemma 0' (D_base has no 3-AP).** If b0 + b3 = 2 b_m with b0 < b_m < b3 in D_base, we get a contradiction.
- Cross copies: the Sidon property gives {tau0, tau3} = {tau_m, tau_m}, so all three points lie in one copy.
- Same copy, atom a_m ≠ 0: its coefficient 2 sigma_m must come from b0 and b3. Both then carry a_m with the same sign, so alpha0 = alpha3 and b0 = b3.
- Same copy, a_m = 0 (so b_m is 0 or h_c): the atoms of b0 and b3 cancel. Either both atoms are 0, or they are equal with opposite signs. In both cases alpha0 + alpha3 = 1, which is odd, while it should equal 2 alpha_m.

All coefficients are at most 4 in absolute value, which is below B/2, so the coefficient lemma applies. ∎

**Fine block.**
- Let p be an odd prime and G0 = {2p i + (i^2 mod p) : 0 <= i < p}.
- G0 is Sidon (Erdős–Turán; proof below), and G0 ⊂ [0, 2p^2).
- Take G ⊆ G0 with |G| = 3r, and a labelling s : G -> P that takes each value exactly r times.
- Let L = 4p^2 + 1, which is > 2 max G.

*Sidon proof.* Write x = 2p i + q_i with q_i < p.
1. From x_a + x_b = x_c + x_d we get q_a + q_b ≡ q_c + q_d (mod 2p), and both sides are < 2p. So the q-sums are equal, and then i_a + i_b = i_c + i_d.
2. Mod p, the sum S and the sum of squares Q are therefore the same for both pairs. Since p is odd, the product (S^2 - Q)/2 is the same too.
3. So {i_a, i_b} and {i_c, i_d} are the root sets of the same quadratic over F_p. Their elements lie in [0,p), so they are equal. ∎

**Set.** D = {L b + g : b in D_base, g in G}. Write a point as (b,g). The order is lexicographic, because g < L.

**Coloring of a cell (q,p), q > p** (all colors mod 3).
- (diag) b_q > b_p and g_q = g_p = g: chi_B(b_q,b_p) + s_g.
- (off) b_q > b_p and g_q ≠ g_p: chi_B(b_q,b_p) + t(g_q,g_p). Here t = s+2 if s_{g_q} = s_{g_p} = s, and t = 0 otherwise.
- (same) b_q = b_p and g_q > g_p: ell(g_q,g_p) := t(g_q,g_p) + 2.

## 2. Lemma E (all L's of D)

Take p0 < x, y < p3 with x + y = p0 + p3, and write each point as (b,g).
- The relation reads L(b0+b3-bx-by) = gx+gy-g0-g3. The right side has absolute value < 2 max G < L, so both sides vanish.
- So the bases satisfy b0+b3 = bx+by, and the g's satisfy g0+g3 = gx+gy. Since G is Sidon, {gx,gy} = {g0,g3}.

**(A) Trivial base relation, {bx,by} = {b0,b3}.**
- If b0 = b3, then all four points share one base, so {x,y} = {p0,p3}, which is impossible. So b0 < b3.
- **R1:** bx = b0, by = b3. Then gx = g3 and gy = g0, and g3 > g0. The L is x = (b0,g3), y = (b3,g0).
- **R2:** bx = b3, by = b0. Then gx = g0 and gy = g3, and g3 > g0. The L is x = (b3,g0), y = (b0,g3).

**(B) Nontrivial base relation.** The order forces b0 <= bx, by <= b3.
- bx = b0 would force by = b3, which is trivial. So b0 < bx, by < b3.
- bx = by is excluded by Lemma 0'.
- So (b0, bx, by, b3) is a base L (S1 or S2, in its own order).
- **II:** gx = gy = g0 = g3.
- **III:** gx = g0, gy = g3, with g0 ≠ g3.
- **I:** gx = g3, gy = g0, with g0 ≠ g3.

There are no other L's. ∎

## 3. Theorem F (properness)

Let s = s_{g0}, s' = s_{g3} and t = t(g3,g0). Cells of each L are listed as (horizontal end, corner, vertical end).

| type | cells | colors | why not monochromatic |
|---|---|---|---|
| II | all diag, one g | chi_B + s_g on a base L | a shift of a proper coloring |
| I | all off, the same (g_q,g_p) = (g3,g0) | chi_B + t on a base L | a shift of a proper coloring |
| III | diag, off, diag; the base corner has chi_B = 0, the base arms 1 | 1+s, t, 1+s' | needs s = s' and t = s+1, but then t = s+2 |
| R2 | diag, off, diag, all on the pair (b3,b0); kappa = chi_B(b3,b0) | kappa+s, kappa+t, kappa+s' | needs s = s' = t, but t = s+2 |
| R1 | same, off, same | ell, kappa+t, ell | kappa+t ∈ {t, t+1} and ell = t+2, so the corner differs |

So chi is proper. ∎

## 4. Counts at the shifts H_c = L h_c (the set W, |W| = m')

**F_H(D).** A start u = (b,g) lies in F_H(D) iff u + H = (b + h_c, g) lies in D. This uses that the difference L h_c forces equal g. By Lemma C, F_H(D) = {(T_c, g) : g in G}, so |F_H| = 3r.

**L's of span H.** Types I, III, R1 and R2 have g3 ≠ g0, so their span ≡ g3 - g0 ≢ 0 (mod L). The span-H L's are therefore exactly the type-II lifts of S1(0,b) and S2(0,b), b in A_c. That gives 2k L's at each start (T_c, g).
- Corner color: s_g.
- Arm color: 1 + s_g.

**Consequences, for every e and every H in W.**
- m_{e,H}((T_c,g)) = 2k [s_g = e-1].
- N_e(H) = 2kr.
- min_e N_e/|F_H| = 2k/3.
- |R_e(H)| = r, and sum_e |R_e(H)| = |F_H| (≤ 2|F_H| by a wide margin).
- sum_u m_{e,H}(u)^2 = 4k^2 r.

**Fiber multiplicities.** Fix b in A_c and the class of color e at d = Lb.
- It contains every (T_c,g) with s_g = e-1, because the left cell is diag with color 1 + s_g.
- At lag l = L(h_c - b), every such start returns to the class.
- So r_{S_e(Lb)}(L(h_c-b)) >= r.
- Symmetrically, through the mirror arms, r_{S_e(L(h_c-b))}(Lb) >= r.

These are exactly the lags that produce the requests. The request-producing classes have size >= r.

**Size.**
- |D| = 3r * m'(2k+2).
- span(D) < L (span D_base + 1) <= (4p^2 + 1) * C(k,m'), where C(k,m') depends only on k and m' (C ≈ B^{M+1} * max tau).
- Take p → ∞ with k and m' fixed, and r = ⌊p/3⌋.
- Then the class sizes and fiber multiplicities are >= r >= span^{1/2 - o(1)}.
- The ratio 2k/3 is unbounded as k grows, with p chosen after k.

## 5. Status

**PROVED** (Lemma 0', Lemma E, Theorem F and the counts above). For every λ, every m', every α < 1/2 and every c > 0, there is a proper ternary source with all of the following on a set W of m' shifts:
- min_e N_e(H) >= λ |F_H(D)| for every e;
- sum_e |R_e(H)| = |F_H(D)|;
- U1-type energy ratio sum m^2 / (N + N^2/|F_H|) = 2k*3r / (3r + 2k), which is unbounded;
- the request-producing classes have size >= c span^α;
- their fibers at the request-producing lags have multiplicity >= c span^α.

Padding G-free copies is not needed for the UW and energy refutations. Hence:
- variant (b) (fiber multiplicity >= m, for any m, including m growing like span^{1/2-o(1)}) is KILLED;
- variant (a) is KILLED for every exponent α < 1/2;
- the "digit designs cannot reach r >= 2" heuristic of round 2 is refuted (fine-scale lifting does it).

**Not reached / OPEN.**
- (a) with α = 1/2 and a LARGE constant. The regime has |S| ≈ 98 sqrt(L) and fibers ≈ 2 sqrt(L). Here |S| <= |F_d(D)| = O(r), with r ≈ span^{1/2} / (const * sqrt(B^M tau)). So the class sizes reach only a tiny constant times sqrt(span), far below the regime and far below the binary cap K.
- (c) interval averaging with the weights a_h. At shifts h ∉ W the requests are few; this is not analysed.
- (d) density hypotheses on D: D here has density → 0.
- Embedding: not claimed. Any instance with ratio >= 240 has k >= 360, so span >= B^{M} with M > 360. That far exceeds 21,987,408 (the bound quoted from the brief). So these instances are not diagonal classes of a proper four-colored square.
- No statement about R_4 is made.

=== END OF ANSWER round3_q3 ===
