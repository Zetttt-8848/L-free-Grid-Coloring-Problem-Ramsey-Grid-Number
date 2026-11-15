# Running summary after round 1 (written at the round-2 plan step)

## Goal (ledger entry 1, OPEN; unchanged)
P1 (i)-(v) exactly as posed, plus Part D settled at level (D-a) [an explicit-delta proportional-loss inequality with every hypothesis named] or (D-b) [an explicit, L-by-L checkable family of proper ternary sources showing that no request-based inequality of that kind can hold]. (D-c), the forced-color alternative, is a separate OPEN line (entry 6) and not part of the goal.

## Established

### P1 is proved (round1_q1, most complete; round1_q3 and round1_q4 agree independently)
- Lemma 0. Every directed L inside V(D) is L(u,d,h) for exactly one triple with 1<=d<h. Its cells are the horizontal end (u+d,u), the corner (u+h,u) and the vertical end (u+h,u+h-d), with arm length h-d. It lies in V(D) iff u, u+d, u+h-d, u+h are all in D. NOTE: d ranges over all of [1,h-1], including d > h/2, where u+d > u+h-d. Coincident middle points (d = h-d) are harmless.
- (i) L(u,d,h) is monochromatic of color e iff u ∈ F_{h-d}(S_e(d)) ∩ S_e(h). Hence chi is proper iff S_e(h) ∩ R_e(h) = ∅ for all h and e. This uses all L's.
- (ii) R_e(h) ⊆ F_h(D).
- (iii) k(u) := #{e : u ∈ R_e(h)} <= 2, and u ∈ R_e ∩ R_{e'} forces u ∈ S_{e''}(h). The posed inequality holds, and so does the sharp identity sum_e |R_e(h)| = 2|F_h(D)| - 2#{k=0} - #{k=1}.
- (iv) The shifted source of X = S_e(d) avoids e, via L(a,d,d+(b-a)), and F_l(X) ⊆ R_e(d+l). The classes G_f = F_l(X) ∩ S_f(h), f ≠ e, are Sidon (3-APs included); round1_q1 proves this from scratch with four L's (L1-L4). F_l(X) ∩ R_{e'}(h) ⊆ G_{e''}, and F_l(X) ∩ R_{e'} ∩ R_{e''} = ∅.
- (v) The chain uses only the same-shift, same-class instances: the binary-source property, the Golomb split, and the partition of F_d(D). New content: the union over d in R_e(h); (ii); (iii) and the cross-color statements of (iv).
- Ledger entry 9 records this as PROVED. P1 is part of the goal, so it will need the verify audit together with whatever settles Part D.

### Single-shift structure (round1_q3, proved)
- D1. Fix the classes at shifts < h. A partition of F_h(D) satisfies all L's with corner at shift h iff each u avoids every color e with u ∈ R_e(h). This is possible iff R_0 ∩ R_1 ∩ R_2 = ∅.
- D2. Single-shift counting therefore bounds |F_h(D)| only from below: |F_h| >= (1/2) sum_e |R_e|. The per-class bound |S_e(h)| <= |F_h| - |R_e(h)|, summed over e, is vacuous. A proportional saving can come only from forcing a nonempty triple intersection, i.e. union growth |R_e(h)| > (2/3)|F_h| for all three e, on a positive a-weighted share of shifts h.
- D3 (logic). Refuting a per-class near-extremality hypothesis saves only additively at one shift, which is negligible. The useful hypothesis is the averaged one, H_avg(eta): sum_d a_d X_d >= (1-eta) sum_d a_d U_d. Its negation is exactly the consumable proportional saving (about a factor 1-3.9 eta; hypothetical).

### Conditional energy reduction (round1_q4, proved)
If sum_u m_{e,h}(u)^2 <= C1 N_e(h) + C2 N_e(h)^2/|F_h| holds for all three e, with C2 < 3/2, then min_e N_e(h) <= (2C1/(3-2C2)) |F_h| (Cauchy-Schwarz plus double cover). round1_q4 also gives a window-averaged variant, but only as a sketch (an unverified convexity step).

### D-c, easy part (round1_q1, proved)
- A = F_l(X) ∩ R_{e'}(h) ⊆ G_{e''} and B ⊆ G_{e'}. Both are Sidon, and A ∩ B = ∅.
- The constraints (C1) containment, (C2) disjointness and (C3) Sidon are jointly consistent with r_X(l) = 2Q and A = G'', B = G' (an abstract model). So imbalance cannot follow from (i)-(iv) as stated; it would need the generating L's (C4)-(C6) listed in round1_q1.
- No explicit ternary source realizing the model exists yet.
- Consumer quantity: an imbalance r_X(l) <= (1-delta) v_l would lower v_l, hence K through the rank inequality, hence U_d.

### Plan-step facts (director, round2_plan; each checked)
- Collision lemma (ledger entry 15). Suppose u ∈ F_{h-d}(S_e(d)) ∩ F_{h-d'}(S_e(d')) with d < d'. Then u+(d'-d) ∉ S_e(d) and u+(h-d') ∉ S_e(d).
  Proof: L(u,d,d') has horizontal end (u+d,u) of color e, corner (u+d',u) of color e, and vertical end (u+d', u+d'-d). So the vertical end is not e, i.e. u+d'-d ∉ S_e(d). Likewise L(u+h-d',d,d') has corner (u+h,u+h-d') of color e and vertical end (u+h,u+h-d) of color e, so its horizontal end (u+h-d'+d, u+h-d') is not e.
  So a collision at u forces the inner symmetric points u+delta and u+l-delta (l = h-d, delta = d'-d) out of S_e(d), while u and u+l are in it. Checked on 562 collisions in random proper sources: 0 violations. It is not yet turned into any bound.
- Mixed Golomb pieces (ledger entry 16). Fix (d,l) and a corner color f. The f-colored starts G_e^f = F_l(S_e(d)) ∩ S_f(h), for the two classes e ≠ f, are each Sidon, but their UNION need not be Sidon. Explicit witness: D = [0,10), with rows u = 0..8 listing chi(v,u) for v = u+1..9:
  0: 200221121 / 1: 22210010 / 2: 1021102 / 3: 101202 / 4: 10101 / 5: 2020 / 6: 210 / 7: 02 / 8: 2
  It is proper (all L's checked). With d = 1, l = 1, f = 0, the starts 0, 2, 3, 5 have classes 2, 1, 1, 2 and 0+5 = 2+3.
- Pattern data (evidence only). In random proper sources on [0,n), n <= 16, the additive quadruples a, a+r, a+s, a+r+s (r <= s) inside G_e^f ∪ G_{e'}^f had class patterns (A = class of a) ABBA 22, AAAB 18, ABBB 13, AABB 4, ABAB 1. No AABA or ABAA appeared; AAAA and BBBB are impossible.

### Correction to round1_q2 (ledger entries 10, 11)
- round1_q2 claimed an explicit proper digit family with |F_h| = 3 and min_e N_e(h) >= k-1. Its L-lemma assumes p0 < p1 <= p2 < p3, i.e. d <= h/2, so it MISSES the mirrored L's with d > h/2. As written, the family is NOT proper. Exhaustive check: 6 monochromatic L's at k=2, 9 at k=3, 13 at k=4.
  - Within copy j, the missed L's are left (T_j+h-b, T_j+a), corner C_j(a), up (T_j+h-a, T_j+b), for a < b. Both arm cells are default 0, so for j = 0 the L is monochromatic.
  - Across copies j < j', the missed L is left (T_j', T_j), corner (T_j'+h, T_j), up (T_j'+h, T_j+h). All three cells are default 0.
- Repair (director; exhaustive L check for k = 2..6 with the balanced and the cyclic choice gives 0 monochromatic L's):
  - color the mirror cells M_j(x,y) = (T_j+h-x, T_j+y), x ≠ y in A_j^0, with j+1 mod 3;
  - color the cross corners (T_j'+h, T_j) with 1.
  Then |F_h| = 3 and N_e(h) >= k for every e. The cyclic choice f_j ≡ j+1 puts all of color e's requests on one start, with multiplicity 2k.
  So the conclusions "UW(lambda) false for every lambda" and "U1-type energy bounds false for every C, over arbitrary ternary sources" very probably stand. They need a written proof of the corrected L-lemma, including the mirrored cases; this is asked in round2_q1. Until then they are OPEN (entry 11).
- Scope (unchanged): the family is sparse, has |F_h| = 3, and works at a single h. It says nothing about the regime (classes near cap, |F_h| comparable to span). By the corners theorem, ternary sources of positive density cannot have unbounded span, so a (D-b) family must sit at the sparse scale of the binary caps (|S_e(d)| ~ span^{3/4} heuristically).

### Global identities (director, elementary)
- sum_h N_e(h) = sum_d C(|S_e(d)|,2).
- sum_e r_{S_e(d)}(l) is the lag-l autocorrelation (agreement count) of the 3-colored word z_d(u) = chi(u+d,u) on F_d(D). Its six Golomb pieces G_e^f (e ≠ f) all lie disjointly in F_{d+l}(D).
- Summing the rank-neighbor inequality over the three classes S_e(d), with a JOINT multiplicity cap w_l >= sum_e r_{S_e(d)}(l), bounds sum_e |S_e(d)| directly. So any joint fiber bound sum_e r_{S_e(d)}(l) <= (1-delta) * 3 v_l is consumable: it lowers K jointly, hence U_d.

## Dead ends (and why)
- U1 and UW(1) are refuted by the pre-registered witnesses (entries 3, 4). Pointwise energy or ratio bounds for arbitrary sources fail (and fail for every constant, given the repaired family of entry 11).
- Single-shift counting (D2) is vacuous; only multi-shift union growth or joint-fiber arguments can save.
- "The union of the two same-corner-color Golomb pieces is Sidon" is false (entry 16), so the naive factor-2 joint fiber saving is dead.
- Imbalance from (C1)-(C3) alone is impossible (abstract model, round1_q1).

## Open gaps between the state and the goal
1. (D-b) A family where the ratio is large for many h (a positive proportion of a growing window) with |F_h| -> infinity, ideally with classes or fibers as large as additive structure allows. It must come with a complete written proof of properness that covers ALL L's, including d > h/2. Entry 5 for the general UW question; entry 11 for the repaired single-shift family.
2. (D-a) Anti-collision or union growth under H_avg(eta) or another named hypothesis, giving |R_e(h)| > (2/3)|F_h| for all e on a positive a-weighted share of h (entry 7). Alternatively, a window-averaged energy bound with C2 < 3/2 (entry 8). The collision lemma (entry 15) is the only L-constraint on collisions identified so far.
3. (D-c) Imbalance from the generating L's (C4)-(C6), or an explicit proper source realizing balanced, fully foreign-requested Golomb classes (entry 6).
4. (Fresh) A joint fiber bound sum_e r_{S_e(d)}(l) <= (1-delta) 3 v_l, or a joint constraint between the six Golomb pieces (mixed additive patterns), fed into the summed rank inequality (new entry 17).

## Where the next round should concentrate
Explore, with four genuinely different attempts:
- (q1, D-b) Write the corrected proof of the repaired digit family. Then build a multi-shift, growing-|F_h| version with ratio -> infinity for all e on many h. Say what it kills.
- (q2, D-c) Realize the abstract balanced model by an explicit proper source, or prove imbalance from (C4)-(C6).
- (q3, D-a) Anti-collision or energy under a named averaged hypothesis, building on the collision lemma. Or prove a no-go: an explicit model of complete collision consistent with every L.
- (q4, fresh lens) A joint fiber bound for the six Golomb pieces via mixed-pattern L's and the summed rank inequality.

Every claimed construction must cover all L's, including the mirrored ones with d > h/2, which round1_q2 missed.
