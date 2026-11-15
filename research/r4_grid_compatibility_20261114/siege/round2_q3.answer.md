# round2_q3 answer: averaged hypothesis, forced-energy lemma, status of (D-a)

Outcome: PARTIAL. I name an averaged hypothesis precisely and prove one necessary-collision lemma (Lemma B) plus a consequence of item 6 (Lemma C). I did NOT prove (a), the impossibility of the hypothesis with an explicit eta, and I did NOT prove (b), a no-go model. Both remain OPEN.

## 1. Named hypothesis

Let (D, chi) be a ternary source with D ⊆ [0,L), let a_h >= 0 be window weights, and let K be the certified capacity function. Throughout, r_D(h) = |F_h(D)| = sum_e |S_e(h)|, since the S_e(h) partition F_h(D).

**H_avg(eta).** sum_h a_h r_D(h) >= (1-eta) sum_h a_h 3K(L-h).

**H_fib(eta).** For every d in the window and every e:
sum_{l=1}^{l_0} r_{S_e(d)}(l) >= (1-eta) sum_{l=1}^{l_0} v_l(L-d),
where v_l(S) = Q(S-l) + Q(S-l-1).

Under H_fib, N_e(h) = sum_{d<h} r_{S_e(d)}(h-d) is (on average over h) at least about (1-eta) h v. That is the "large-ratio" input.

## 2. Proved statements

**Lemma A (double cover forces a small request set).** For every h there is a color e with |R_e(h)| <= (2/3) r_D(h).
*Proof.* By fact 2(iii), sum_e |R_e(h)| <= 2 r_D(h). Take the minimum over the three colors. ∎

**Lemma B (forced energy).** For every ternary source and every h >= 2 there is a color e with
E_e(h) := sum_u m_{e,h}(u)^2 >= (3/2) N_e(h)^2 / r_D(h).
*Proof.* m_{e,h} is supported on R_e(h). By Cauchy-Schwarz, N_e(h)^2 <= |R_e(h)| E_e(h). Apply Lemma A to that color. ∎

Contrapositive, which is the form a (D-a) proof must use: if one proves E_e(h) <= C1 N_e + C2 N_e^2/r_D(h) for all three e with C2 < 3/2, then fact 4 gives min_e N_e(h) <= (2C1/(3-2C2)) r_D(h). Under H_fib this means r_D(h) >~ (3-2C2) h v / (2 C1), which is incompatible with r_D(h) <= 3K once h is large. So the entire gap is a window-averaged energy bound with C2 < 3/2. Lemma B shows that in any proper source at least one color has normalized energy E r_D / N^2 >= 3/2. Any valid energy bound must therefore allow C2 >= 3/2 for that color. A successful lemma has to be color-asymmetric, or it has to show that the color achieving the bound changes with h in a way that the a-average sees.

**Lemma C (structure of a heavy start; from item 6).** Let u have e-requests at shifts d_1 < ... < d_m < h, with m = m_{e,h}(u). Then for every pair i < j, with l_i = h - d_i and delta = d_j - d_i:
- u, u+l_i ∈ S_e(d_i);
- u+delta ∉ S_e(d_i) and u+l_i-delta ∉ S_e(d_i).

So for a fixed i, the set {u + (d_j - d_i) : j > i} ∪ {u + l_i - (d_j - d_i) : j > i} is disjoint from S_e(d_i). These are 2(m-i) points, distinct up to the symmetric coincidence delta = l_i - delta, in the interval (u, u+l_i).
*Proof.* This is item 6 applied to each pair (d_i, d_j). ∎

Consequence (proved, weak): the smallest shift d_1 has a gap structure of at least m-1 symmetric excluded pairs inside an S_e(d_1)-pair of lag l_1. Under the heuristic density p ≈ 1/48 of S_e(d_1), this exclusion is automatically satisfied by most points. So Lemma C by itself does not contradict heavy collision: about m <= l_1 points are excluded from a set of density 1/48. **Dead end as a standalone argument.** It would only bite in combination with a lower bound on how many distinct (u, d_1) pairs are forced, and I have not proved one.

## 3. Attempted no-go models (dead ends, not counterexamples)

I looked for structured proper ternary sources with complete collision:
- chi(v,u) = f(u) (row coloring);
- chi(v,u) = g(v) (column coloring);
- chi(v,u) = phi(v-u) (diagonal coloring).

Each is proper only if a 3-coloring of a long interval has no monochromatic pair at a prescribed set of differences. This fails once D contains long progressions. So none of these models reaches the regime's sizes. No explicit no-go model is claimed.

## 4. Summary of exact status

Proved (for every ternary source and every h >= 2):
- Lemma A;
- Lemma B;
- Lemma C;
- the reduction: an energy bound with C2 < 3/2 for all three colors, combined with H_fib, contradicts r_D(h) <= 3K for large h.

Heuristic only:
- that H_fib forces N_e(h) ≈ h v;
- the density-based dismissal of Lemma C.

OPEN:
- (D-a) an explicit eta for which H_avg(eta) together with H_fib(eta) is impossible;
- a window-averaged energy bound with C2 < 3/2 that is consistent with Lemma B (it must be color-asymmetric);
- (D-b) an explicit proper family with near-extremal classes and complete request collision.

No statement about R_4 is made.

=== END OF ANSWER round2_q3 ===
