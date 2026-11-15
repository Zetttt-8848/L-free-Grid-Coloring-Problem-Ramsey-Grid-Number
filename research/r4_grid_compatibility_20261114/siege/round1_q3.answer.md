# round1_q3 answer: request geometry in a ternary source

Status summary: P1 (i)-(v) PROVED below. Part D: no proportional-loss inequality is proved. Proved instead: (a) an exact local characterization showing that request counting can only act through triple coverage; (b) the observation that double cover gives a LOWER bound on |F_h(D)|, never an upper one; (c) a logical point: refuting the per-class hypothesis H(eta) as worded in the query gives no usable saving, and the hypothesis that has to be refuted is the a-weighted one, H_avg(eta). The anti-collision / union-growth lemma is still OPEN.

Throughout, (D, chi) is a ternary source, P = {0,1,2}, and {e,e',e''} = P.

## P1

**Lemma 0 (L's in V(D)).** An L (x,y),(x+t,y),(x+t,y+t) with t>0 lies in V(D) iff y, x, x+t, y+t are in D and y<x. (The membership conditions are y<x for the first cell, y<x+t for the second, and y+t<x+t for the third; the last two follow from y<x and t>0.) Write u=y, d=x-y >= 1, h=x+t-y, so h-d=t >= 1 and d<h. The cells are then: horizontal end (u+d,u), corner (u+h,u), vertical end (u+h,u+h-d). The corner is the cell (x+t,y). Both arms have length t=h-d. The four points involved are u, u+d, u+h-d, u+h, all in D.

**(i) Reformulation.** Claim: such an L is monochromatic of color e iff u ∈ S_e(h) ∩ F_{h-d}(S_e(d)).

Proof. Here u ∈ S_e(d) means u, u+d ∈ D and chi(u+d,u)=e. Next, u+h-d ∈ S_e(d) means u+h-d, u+h ∈ D and chi(u+h,u+h-d)=e. Finally, u ∈ S_e(h) means u, u+h ∈ D and chi(u+h,u)=e. Together these say exactly that the three cells of the L lie in V(D) and all have color e. Conversely, every L in V(D) has this form by Lemma 0.

So chi is proper iff S_e(h) ∩ R_e(h) = ∅ for all h >= 2 and all e. The L's used are the ones with corner (u+h,u), horizontal arm to (u+d,u), vertical arm to (u+h,u+h-d), and arm length h-d, for every 1 <= d < h. The S_e(h) partition F_h(D) because chi takes exactly one value on (u+h,u). ∎

**(ii)** If u ∈ F_{h-d}(S_e(d)), then u ∈ S_e(d) ⊆ D, and u+h-d ∈ S_e(d) gives u+h ∈ D. So u ∈ F_h(D). ∎

**(iii) Double cover.** Suppose u ∈ F_h(D). Then u lies in exactly one S_f(h), and by (i) u ∉ R_f(h). So u lies in at most two of the R's. If u ∈ R_e ∩ R_{e'}, then u is in neither S_e(h) nor S_{e'}(h), so u ∈ S_{e''}(h).

For the count, sum_e |R_e(h)| = sum_{u∈F_h(D)} #{e : u ∈ R_e(h)}. Here we use (ii) to restrict to F_h(D). Each term is at most 2, and it is at most 1 = 2-1 on the starts lying in at most one R. This gives the stated inequality. ∎

**(iv) Inside one class.** Let X=S_e(d), l>=1 and h=d+l. By definition F_l(X) = F_{h-d}(S_e(d)) ⊆ R_e(h).

First, the cells of the binary source avoid e. For u<v in X, the L (u+d,u),(v+d,u),(v+d,v) has t=v-u, and its two end cells have color e. So chi(v+d,u) ≠ e.

For u ∈ F_l(X), take v=u+l. The Golomb class of u is labelled by chi(u+h,u), and this color lies in P∖{e}. If also u ∈ R_{e'}(h), then (i) gives chi(u+h,u) ≠ e'. Hence chi(u+h,u) = e'', and u lies in the e''-Golomb class. If u were in both R_{e'}(h) and R_{e''}(h), its color would avoid e, e' and e'', which is impossible. So F_l(X) ∩ R_{e'}(h) ∩ R_{e''}(h) = ∅. ∎

**(v) Accounting.**
- The chain uses (i) only for the L's lying inside the strict source of a single class X=S_e(d): the L's with corner (v+d,u), u<v in X, arm length v-u, where both arm ends have the class's own color e. This is what gives the binary-source property, the Golomb split, and K. It also uses the partition of F_d(D) by e, through X_d.
- New content: (i) for the cross-shift L's in full, (ii), and (iii), in particular how different colors interact. Also new is the forced-membership part of (iv): foreign requests fix the Golomb class.

## Part D

**Proposition D1 (exact local criterion; proved).** Fix h. Suppose the classes S_f(d) for d<h are given, so the sets R_e(h) are determined. A partition of F_h(D) into S_0(h), S_1(h), S_2(h) satisfies every L whose corner is at shift h iff each u is placed in a color e with u ∉ R_e(h). Such a partition exists iff R_0(h) ∩ R_1(h) ∩ R_2(h) = ∅. If it exists, the forced starts are exactly those lying in two R's.

Proof. This is immediate from (i): the L's with corner (u+h,u) constrain only the choice of the color of (u+h,u), and they rule out exactly the colors e with u ∈ R_e(h). ∎

Consequence: at a single shift, the request structure obstructs only through a triple intersection. The inequality sum_e|R_e(h)| <= 2|F_h(D)| is necessary for the empty triple intersection but not sufficient.

**Proposition D2 (direction of the counting; proved).** Double cover gives |F_h(D)| >= (1/2) sum_e |R_e(h)|. This is a lower bound on |F_h(D)| = sum_e |S_e(h)|. The quantity the consumer needs to cap is exactly this one, since X_h is the sum over c of |F_h(D_c)|.

The per-class consequence of (i) is |S_e(h)| <= |F_h(D)| - |R_e(h)|. It improves on the cap K only if |R_e(h)| > |F_h(D)| - K, which is about 2K in the regime. Summed over e it gives sum_e |S_e(h)| <= 3|F_h(D)| - sum_e|R_e(h)|, and by double cover the right side is at least |F_h(D)|, so it is vacuous.

Hence a proportional saving cannot come from counting at one shift. It can only come as a contradiction: a union-growth lemma forcing |R_e(h)| > (2/3)|F_h(D)| for all three e at once contradicts (iii). The same holds by D1 for any lemma forcing a nonempty triple intersection. ∎

**Remark D3 (the hypothesis must be averaged; proved, logic only).** The negation of the per-class hypothesis H(eta) in the query only says that some single class at some single shift d, or some single lag l, misses its cap by a factor eta. That lowers one U_d by about eta*K/12. This is an additive saving at one shift, which the sensitivity analysis shows is negligible. A usable target must therefore be the averaged hypothesis

H_avg(eta): sum_{d=1}^{t-1} a_d X_d >= (1-eta) sum_{d=1}^{t-1} a_d U_d,

whose negation is exactly the weighted proportional saving the outer inequality can consume. By the stated sensitivity this would move the excluded side by a factor of about 1-3.9 eta. That figure is hypothetical; it is not a bound. Refuting H_avg needs union growth on a positive a-weighted share of the shifts h, not at one shift.

**Heuristic (not proved).** In the regime, the sets F_{h-d}(S_e(d)) have density about 1/146 in F_h(D), and there are h-1 of them for each e. If they behaved independently, each R_e(h) would cover almost all of F_h(D) once h >> 146. That would force triple coverage, contradicting D1. So in the regime the request sets must collide massively. Neither the collision nor its absence is proved here.

**Part D-c (partial).** By (iv), F_l(X) ∩ R_{e'}(h) lies in the e''-Golomb class of F_l(X), which is a Sidon set of span at most L-l. So |F_l(X) ∩ R_{e'}(h)| <= Q(L-l) holds, but trivially. An imbalance between the two Golomb classes would lower v_l, which feeds into P(H;v) and hence into K. No forced imbalance is proved.

## Open
1. An anti-collision bound on |F_{h-d}(S_e(d)) ∩ F_{h-d'}(S_e(d'))| for d ≠ d', under H_avg or under a named near-maximal Sidon rigidity hypothesis, strong enough to give |R_e(h)| > (2/3)|F_h(D)| for all e on a positive a-weighted share of h.
2. Alternatively, a construction (D-b) of ternary sources in the regime with empty triple intersections at every h.

## Exact statements proved
- P1 (i)-(iv) for every ternary source and every h >= 2, and the accounting (v).
- D1: at each shift, consistency holds iff the triple intersection of the R_e(h) is empty.
- D2: single-shift request counting bounds |F_h(D)| only from below; the per-class bound is vacuous after summing.
- D3: refuting per-class H(eta) gives only a negligible saving; H_avg(eta) is the hypothesis whose refutation gives the weighted proportional saving the consumer can use.

=== END OF ANSWER round1_q3 ===
