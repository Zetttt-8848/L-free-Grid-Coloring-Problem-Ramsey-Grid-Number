# round1_q4 answer

Status summary: P1 (i)-(v) PROVED below. Part D: only a CONDITIONAL reduction is proved (Lemma D1: any energy bound with C_2 < 3/2 forces min_e N_e(h)/|F_h(D)| <= 2C_1/(3-2C_2)). The requested window-averaged energy bound (a), the union bound (b), and a counter-family (c) all remain OPEN. No statement about R_4 is made.

## P1

**Lemma 1 (parametrisation of L's in V(D)).** Every directed L inside V(D) is exactly one triple (u,d,h) with 1 <= d < h. Its cells are: left end (u+d,u), corner (u+h,u), upper end (u+h,u+h-d). Its arm length is h-d. It lies in V(D) iff u, u+d, u+h-d, u+h are all in D.

*Proof.* Take an L (x,y),(x+t,y),(x+t,y+t) with t>0. All three cells must lie in V(D), so their columns exceed their rows. Set u=y, d=x-y >= 1, h=d+t > d. Then the cells are (u+d,u), (u+h,u), (u+h,u+t) with u+t = u+h-d. Membership in V(D) holds iff the following pairs are in D: {u, u+d}, {u, u+h}, {u+h-d, u+h}. The order conditions u<u+d, u<u+h and u+h-d<u+h are automatic. Conversely every such (u,d,h) gives an L. The map is a bijection. QED

**(i)** The L (u,d,h) is monochromatic of color e iff three things hold: chi(u+d,u)=e (u in S_e(d)), chi(u+h,u+h-d)=e (u+h-d in S_e(d)), and chi(u+h,u)=e (u in S_e(h)). Membership in S_e(.) already contains the D-conditions. The first two conditions together say u in F_{h-d}(S_e(d)). So a monochromatic L of color e with parameters (d,h) exists iff S_e(h) ∩ F_{h-d}(S_e(d)) ≠ ∅. Taking the union over d < h: chi is proper iff S_e(h) ∩ R_e(h) = ∅ for all h >= 2 and all e. The L's used are all L's in V(D): the corner is (u+h,u) (the cell whose class S_·(h) is tested), the arms end at (u+d,u) and (u+h,u+h-d), and the arm length is h-d. QED

**(ii)** Let u in F_{h-d}(S_e(d)). Then u in D, and u+h-d in S_e(d) ⊆ F_d(D), so u+h in D. Hence u in F_h(D). QED

**(iii)** Let u in F_h(D). Then u lies in exactly one class S_f(h), with f = chi(u+h,u). By (i), u ∉ R_f(h). So u lies in at most the two sets R_e(h) with e ≠ f. If u in R_e ∩ R_{e'} with e ≠ e', then f is neither e nor e', so f = e''. Summing over u in F_h(D), using (ii): sum_e |R_e(h)| = sum_u #{e : u in R_e(h)} <= 2|F_h(D)| - #{u : count <= 1}. QED

**(iv)** Let X = S_e(d) and h = d+l. If u in F_l(X), then u, u+l in S_e(d), so u in F_{h-d}(S_e(d)) ⊆ R_e(h). The binary source of X consists of the cells (v+d,u) with u<v in X. For v = u+l this is the cell (u+h,u). Since u in R_e(h), (i) gives chi(u+h,u) ≠ e. So the fiber F_l(X) splits into the two Golomb classes G_f = F_l(X) ∩ S_f(h), for f ≠ e.

Now let u in F_l(X) ∩ R_{e'}(h), with e' ≠ e. Then u in R_e ∩ R_{e'}, so by (iii) u in S_{e''}(h) = Golomb class G_{e''}. If u were also in R_{e''}(h), then u would lie in all three R's, contradicting (iii). Hence F_l(X) ∩ R_{e'}(h) ∩ R_{e''}(h) = ∅. QED

**(v) Accounting.** What the chain uses:
- The binary-source property of each X = S_e(d). This is the instance of (i) for a single (d, e): S_e(h) ∩ F_{h-d}(S_e(d)) = ∅, i.e. corner colors on F_l(X) avoid e.
- The Golomb split of F_l(X).

What is new:
- The union over d in R_e(h), with (ii).
- The cross-color statements: (iii), and the forced class membership and disjointness in (iv).

## Part D

**Lemma D1 (conditional reduction; PROVED).** Fix h and write F = |F_h(D)|. Suppose that for all three e,

sum_u m_{e,h}(u)^2 <= C_1 N_e(h) + C_2 N_e(h)^2 / F, with C_2 < 3/2.

Then min_e N_e(h) <= (2C_1/(3-2C_2)) F.

*Proof.* By Cauchy-Schwarz, |R_e(h)| >= N_e^2 / sum m^2 >= F N_e / (C_1 F + C_2 N_e). By (iii), sum_e |R_e| <= 2F, so some e has |R_e| <= 2F/3. For that e, N_e (3 - 2C_2) <= 2 C_1 F. QED

The same argument works for weighted averages over a window h in W, provided the hypothesis holds in the averaged form with F replaced by the weighted fiber mass. This also needs a convexity step that is not verified here, so this variant is only a SKETCH.

Consequence (implication only): in the heuristic regime, N_e(h)/F ≈ h/146 is far above 2C_1/(3-2C_2) for h ≫ 1. So such a bound would contradict near-extremality. To get an explicit delta one would need the bound to hold with the actual class sizes and to track how N_e scales with sum_d |S_e(d)|^2 (fact 2: sum_h N_e(h) = sum_d C(|S_e(d)|,2)). That gives delta of order 1 - sqrt(2C_1(...)/...); I did not carry this out.

**Open:**
- (a) The window-averaged energy bound with explicit C_1 and C_2 < 3/2. The corner-linking L's of the brief (arm length d'-d) forbid color e on cells at diagonal offsets d and h-d'... I did not turn this into a bound.
- (b) A union lower bound.
- (c) A counter-family.
- D-c (whether the forced sets are Golomb).

## Exact statements proved
- Lemma 1.
- P1 (i)-(iv) as stated, and the accounting in (v).
- Lemma D1, conditional on its stated hypothesis.

=== END OF ANSWER round1_q4 ===
