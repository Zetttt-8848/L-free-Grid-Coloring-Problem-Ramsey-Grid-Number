kind: attempt

Open question attempted (flagged OPEN by this run: the (D-a) goal itself, and the ledger lines "a joint fiber bound sum_e r_{S_e(d)}(l) <= (1-delta) 3 v_l" and "a window-averaged inequality valid for all proper ternary sources that forces a proportional loss"): prove an ARM-AGREEMENT DEFICIT, i.e. an explicit delta > 0 and a named hypothesis H (density of D and/or near-cap fibers, stated as inequalities) such that, for every proper ternary source satisfying H,

  sum_{h in W} a_h sum_e N_e(h) <= (1-delta) * (1/3) * sum_{h in W} a_h Lambda(h) + (explicit error),   (AD)

where Lambda(h) = #{(u,d) : 1 <= d < h, u, u+d, u+h-d, u+h all in D} (the number of L's of V(D) with corner offset h), W is a window of shifts and a_h >= 0 are weights; OR refute every such statement by an explicit family (checkable L by L) satisfying H with agreement rate >= 1/3 on the window; OR reduce (AD) to a strictly easier, precisely stated lemma.

## Facts you may use (proved earlier in this run; checked)
- Lemma 0. Every directed L inside V(D) is L(u,d,h) for exactly one triple of integers with 1 <= d < h. Its cells are the horizontal end (u+d,u), the corner (u+h,u) and the vertical end (u+h,u+h-d); its arm length is h-d. It lies in V(D) iff u, u+d, u+h-d, u+h all lie in D. Here d ranges over ALL of [1,h-1], including d > h/2 (then u+d > u+h-d). Equivalently: for p0 < p3 in D and an ORDERED pair (x,y) in D with x+y = p0+p3, p0 < x,y < p3, there is the L with cells (x,p0), (p3,p0), (p3,y); when x ≠ y both orders give distinct L's ("mirrored" L's). Every construction must handle both orders.
- (i) L(u,d,h) is monochromatic of color e iff u ∈ F_{h-d}(S_e(d)) ∩ S_e(h). Hence chi is proper iff S_e(h) ∩ R_e(h) = ∅ for all h >= 2 and all e. Equivalently: u ∈ F_{h-d}(S_e(d)) iff the L with corner (u+h,u) has BOTH arm cells of color e, so m_{e,h}(u) counts the L's with corner (u+h,u) whose two arms both have color e.
- (ii) R_e(h) ⊆ F_h(D). (iii) Every u ∈ F_h(D) lies in at most two of R_0(h), R_1(h), R_2(h), and u ∈ R_e(h) ∩ R_{e'}(h), e ≠ e', forces u ∈ S_{e''}(h). Sharp identity: sum_e |R_e(h)| = 2|F_h(D)| - 2#{u in no R_e(h)} - #{u in exactly one}.
- Row/column form of properness (immediate from Lemma 0): for u < v in D with h = v-u, write w_u(x) = chi(u+x,u) (row word of u) and c_v(x) = chi(v,v-x) (column word of v). Then chi is proper iff, for all such u,v and every d in (0,h) with u+d, v-d in D, NOT w_u(d) = c_v(d) = w_u(h). (Note w_u(h) = c_v(h) is the shared corner cell.)

## Why (AD) is the right target (director's derivation; every identity below is elementary — re-verify it)
1. sum_e N_e(h) = #{(u,d) : the L(u,d,h) exists and its two arms have the same color} (by (i)). So sum_e N_e(h) <= Lambda(h), and sum_e N_e(h)/Lambda(h) is the arm-agreement rate at offset h.
2. Write z_d(u) = chi(u+d,u) = w_u(d) on F_d(D). The vertical end of L(u,d,h) is (u+h, u+l) with l = h-d, i.e. z_d(u+l). Hence the request of L(u,d,h) is exactly an agreement z_d(u) = z_d(u+l), and
   sum_e r_{S_e(d)}(l) = #{u : u, u+l in F_d(D), z_d(u) = z_d(u+l)}  (lag-l agreement count of the word z_d),
   sum_e N_e(h) = sum_{d<h} sum_e r_{S_e(d)}(h-d).
3. Heuristic regime (from the problem statement): D = D_c has density about 1/4 at span about 2.2*10^7 (some diagonal color occupies >= n/4 diagonal cells), |F_h(D)| ≈ 1.37*10^6 ≈ n/16, r_{S_e(d)}(l) ≈ v ≈ 9.4*10^3. Then Lambda(h) ≈ (1/16) h |F_h(D)| ≈ 8.6*10^4 h and sum_e N_e(h) ≈ 3 v h ≈ 2.8*10^4 h, i.e. agreement rate ≈ 1/3, exactly the rate of an unconstrained random coloring. Thus "all binary caps nearly attained" means "the words z_d have random-like (1/3) lag agreement". A proportional agreement deficit is therefore exactly a proportional deficit in the joint fiber multiplicities w_l = sum_e r_{S_e(d)}(l), which the consumer can use (see 5).
4. Heuristic for a deficit (NOT a proof). By (i) and Lemma 0, for every pair u < v in D, h = v-u, the colors of agreement {w_u(d) : d in (0,h), u+d, v-d in D, w_u(d) = c_v(d)} never contain the corner color w_u(h). If the row word w_u and the column word c_v were independent and uniform, agreements would occur only in the two non-corner colors, at rate 2/9 < 1/3. So agreement rate 1/3 requires POSITIVE correlation between row words and column words in the non-corner colors. Note the strong coupling: the corner colors w_u(h), h varying, form the row word of u itself. Sparse designs CAN have agreement rate 1: in the proved digit families of this run (quoted below), every L of the active copies has agreeing arms. So any valid (AD) needs a density-type or near-cap hypothesis; name it.
5. Consumption (proved in this run). The rank-neighbor inequality, quoted verbatim from the certifying project record:
Consider a hereditary family of finite sets of integers. Let $b_1<\dots<b_s$ be a member of span $L$. Suppose a member with $j$ marks must have span at least $e_j$, for the smaller ranks used below. Choose $1\le c<s$ and take all differences of rank at most $c$, numbering $H=cs-c(c+1)/2$ of them. If the multiplicity of positive difference $h$ is bounded by $v_h$, let $P(H;v)$ be the sum of the cheapest $H$ terms in the multiset containing $v_h$ copies of $h$. Then
$$
 2P(H;v)+4\sum_{i=0}^{c-1}(c-i)e_{i+1}\ \le\ Lc(c+1).
$$
Indeed the sum of the selected differences telescopes to $\sum_{i=0}^{c-1}(c-i)(b_{s-i}-b_{i+1})$. The first and last $i+1$ marks each have span at least $e_{i+1}$, so their endpoint difference in this expression is at most $L-2e_{i+1}$. This remains true when the blocks overlap. The sum is at least $P$ by construction. The archive used $e_{i+1}=i$. Here the endpoint blocks belong to the same family as the original set, allowing an induction on cardinality. [Earlier rank-neighbor inequality](../../exploration/research_round3/four/R3_R4_REPORT.md)
   and its summed form over the three classes, quoted verbatim from the previous round's answer:
## Task 4: the consumer deduction (proved, conditional)
Let the three classes X_e = S_e(d) have sizes s_e and spans <= L'. Use a common rank c < min s_e.
The rank-neighbour inequality for each class gives
2 Σ_sel(X_e) + 4Σ_i(c-i)e_{i+1} <= L'c(c+1), where Σ_sel(X_e) is the sum of the selected differences.
The selected differences of X_e at lag l are pairs in X_e at distance l, at most r_{X_e}(l) of them.
So the union multiset (over e) of selected differences has multiplicity at lag l at most
w_l := Σ_e r_{X_e}(l). Its cardinality is H_tot = Σ_e (c s_e - c(c+1)/2). Hence
Σ_e Σ_sel(X_e) >= P(H_tot; w). Summing over e gives
**2P(H_tot; w) + 12Σ_i(c-i)e_{i+1} <= 3L'c(c+1)**, which is valid for unequal sizes.
If a joint bound w_l <= (1-delta)3v_l holds on all lags used, then P(H_tot; w) >= P(H_tot; (1-delta)·3v).
Since P is evaluated on a thinner multiset, it grows. This caps Σ_e s_e, and so it lowers the per-main-colour
triple inside U_d = Σ_{12 classes} K. Here U_d must be replaced by Σ_c(joint cap of the triple at main colour c).
In the sensitivity model this is exactly the X_d <= (1-delta')U_d input. The size of delta' as a function of delta was not computed.

## The sparse counter-family (proved in this run; summary)
Copies T_c + (A_c^0 ∪ (h_c - A_c^0)), atoms and shifts distinct powers of B >= 9 (atoms below their copy's shift), T_c = tau_c B^M with tau Sidon. All L's: within a copy, for a < b in A_c^0, (S1) arms (T_c+b,T_c+a), (T_c+h_c-a,T_c+h_c-b) and (S2) arms (T_c+h_c-b,T_c+a), (T_c+h_c-a,T_c+b), both with corner (T_c+h_c-a, T_c+a); across copies with equal shift, two L's with corner (T_{c3}+h, T_{c0}). The coloring gives each (S1) L both arms f_c(a,b), each (S2) L both arms rho(c)+1, corners rho(c). So agreement rate 1 on these L's, and min_e N_e(h)/|F_h(D)| is unbounded, but |D| = O(log span): density -> 0, and min_e N_e(h)/(h |F_h(D)|) -> 0.

## Task
1. Verify the identities 1-2 and the consumer link 5 (how a deficit (AD) on a window, or a per-lag deficit w_l <= (1-delta) 3 v_l, feeds the summed rank-neighbor inequality; state precisely what averaged-over-l deficit suffices).
2. Attempt (AD). Suggested lines: (a) per pair (u,v) the corner color is excluded from agreements; sum over the triangle of pairs and use that row u's corner colors are its own word, to show the row/column correlation needed for rate 1/3 is incompatible with properness on a positive share of pairs; (b) a second-moment or Cauchy-Schwarz argument on the words z_d across consecutive d (z_d(u) and z_{d+1}(u) are adjacent cells of row u); (c) combine with double cover (iii) and the forced-energy fact: in every proper source and every h some color e has sum_u m_{e,h}(u)^2 >= (3/2) N_e(h)^2/|F_h(D)| (proved in this run, by Cauchy-Schwarz with |R_e(h)| <= (2/3)|F_h(D)| for the minimizing color).
3. If (AD) fails, give an explicit family satisfying a density hypothesis (|D ∩ I| >= rho |I| on the relevant intervals, any explicit rho > 0 and as large spans as you can) with agreement rate >= 1/3, with complete properness proof; or state precisely the strongest hypothesis under which you can prove (AD), with explicit delta.
4. Whatever you prove, state which consumer quantity it lowers (v_l, K, U_d) and the explicit delta, and make no claim about R_4 except as an implication from stated hypotheses.

Rules: every proof complete and from the cell coordinates; every counterexample explicit and checkable L by L (both orders of every middle pair); finite computations are evidence only. Do not import three-color facts. End with the exact statements proved, refuted, and still open.
