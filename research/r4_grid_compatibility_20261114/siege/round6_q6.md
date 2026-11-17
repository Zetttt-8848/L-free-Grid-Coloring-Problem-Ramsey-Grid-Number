kind: verify

# Task: independent step-by-step verification of the digit-family theorems (a standing result)

This is a verification task for a result the final write-up of this run will present: the "general digit family" of proper ternary sources and its consequences (Lemma A, Theorem B, Theorem D, the embedding remark). It is a (D-b)-type standing result about the problem below: over ARBITRARY proper ternary sources, request-based inequalities of the UW / U1-energy / union-growth kind fail. It rests on one written proof (spliced below verbatim) plus a computer check of all L's for one sub-family at k = 2..6. An earlier, different digit family was found NOT proper because its L-list omitted the mirrored L's with d > h/2 (within one copy and across copies), so the completeness of the L-list is the critical point.

What to do:
1. Check the definitions for consistency: the base B = 100 and the exponent conditions, the coefficient lemma, the colouring table (is every cell of V(D) assigned exactly one colour? are the listed cell types really pairwise distinct?).
2. Check Lemma A (the complete list of L's) inference by inference: every L of V(D) — with the parametrisation recalled below, cells (u+d,u), corner (u+h,u), (u+h,u+h-d), 1 <= d < h, all of u, u+d, u+h-d, u+h in D — must fall into one of the listed cases, including L's whose four points lie in two or more copies, L's with d > h/2 (the mirrored ones), and L's whose arms are corner, mirror, cross or "other" cells. Then check that no listed case is monochromatic under the table, for EVERY admissible choice of roles rho and arm colours f.
3. Check the fibre/request counts of Section 2 (|F_h| and N_e(h) in the repaired family; Theorem D's simultaneous many-shift claims) and the embedding remark of Section 4.
4. End with an explicit verdict: (a) the family is proper exactly as stated (for all parameter choices), or with a precise list of the gaps / counterexample L's found; (b) Theorems B and D hold exactly as stated, or how they must be weakened.
Report every gap precisely (which case, which cells, which colours). Do not rewrite the construction unless you find a gap; if you find one, say whether it is repairable and how.

Reference (Lemma 0 of an earlier proved answer, P1): every L of V(D) is L(u,d,h) with 1 <= d < h: horizontal arm end (u+d,u), corner (u+h,u), vertical arm end (u+h,u+h-d), arm length h-d; it lies in V(D) iff u, u+d, u+h-d, u+h are in D. In the pair language used below: an L consists of p0 < p3 in D and x, y in D with x + y = p0 + p3, p0 < x, y < p3; its cells are (x,p0), (p3,p0), (p3,y).

## The written proof under review (verbatim)

# round2_q1 answer: repaired digit family, and a many-shift version

All numbering follows round2_q1.md. One fact is used throughout, and it follows directly from the definitions. A start u lies in F_{h-d}(S_e(d)) iff chi(u+d,u) = e and chi(u+h,u+h-d) = e. That is, the L with corner (u+h,u), horizontal end (u+d,u) and vertical end (u+h,u+h-d) has **both arms of color e**. Hence

    m_{e,h}(u) = #{L with corner (u+h,u) whose two arm cells both have color e}.   (*)

## 0. A general digit family (it contains the repaired family as a special case)

**Data.**
- A finite index set of "copies" c. Each copy has a shift h_c and a role rho(c) in P.
- Distinct "atoms": each atom belongs to exactly one copy. A_c is the atom set of copy c (possibly empty), and A_c^0 = A_c ∪ {0}.
- Base B = 100. Every atom and every shift value is a power of B. All these exponents are pairwise distinct (shift values may repeat between copies; two copies either have equal h or different powers). All exponents are < M.
- T_c = tau_c B^M, where (tau_c) are distinct members of a Sidon set of nonnegative integers. Their size is unrestricted.

**Set.** E_c = A_c^0 ∪ (h_c - A_c^0) ⊂ [0,h_c], and D = ∪_c (T_c + E_c). Every element of E_c is written uniquely as alpha h_c + sigma a, with a in A_c^0, alpha in {0,1}, and sigma = +1 if alpha = 0, sigma = -1 if alpha = 1. Two copies with T_c < T_{c'} satisfy T_{c'} - T_c >= B^M > 2 max h, so the copies occupy disjoint intervals in the order of T.

**Coefficient lemma.** Suppose sum_m c_m B^m = 0, with |c_m| < B/2 for all m < M and c_M an arbitrary integer. Then every c_m = 0.
Proof. Let m < M be the least index with c_m ≠ 0. The sum is ≡ c_m B^m ≢ 0 (mod B^{m+1}), since 0 < |c_m| < B. Hence all c_m with m < M vanish, and then c_M B^M = 0. ∎

Expand p0 + p3 - p1 - p2 for four points of D. Each atom or shift power comes with coefficient ±1 from each point, so its total coefficient has |.| <= 4 < 50. The coefficient of B^M is tau_{c0} + tau_{c3} - tau_{c1} - tau_{c2}. Consequences:
- The Sidon property gives {c0,c3} = {c1,c2} as multisets.
- For each copy, the signed atom vectors cancel.
- For each shift value, the h-coefficients cancel.

**Coloring.** The left/up colors are given by any f_c(a,b) in P \ {rho(c)}, for a < b in A_c^0.

| cell | color |
|---|---|
| corner C_c(a) = (T_c+h_c-a, T_c+a), a in A_c^0 | rho(c) |
| left (T_c+b, T_c+a) and up (T_c+h_c-a, T_c+h_c-b), a<b in A_c^0 | f_c(a,b) |
| mirror M_c(x,y) = (T_c+h_c-x, T_c+y), x ≠ y in A_c^0 | rho(c)+1 (mod 3) |
| cross corner (T_{c'}+h, T_c), T_c<T_{c'}, h_c=h_{c'}=h | rho(c)+1 |
| cross low cell (T_{c'}, T_c) | rho(c) |
| every other cell of V(D) | 0 |

The listed cell types are pairwise distinct, so the coloring is well defined:
- left cells have a small column offset;
- up cells have both offsets large;
- mirror and corner cells have a large column and a small row;
- the cross cells lie in different copies.

**The repaired family of round2_q1 is a special case.** It has three copies with tau = (0,1,3), a common shift h, |A_j| = k, and rho(j) = j. Its cross corner gets 1 instead of rho(j)+1, and its cross low cell gets 0. This is equally fine for j < j' in {0,1,2}: the corner is 1, the low cell is 0, and the type-1 cross arms are j ≠ j'. So the same proof covers it. The rule in the table is needed only when copies with equal roles coexist.

## 1. Lemma A (complete list of L's). Proof

An L in V(D) consists of p0 < p3 in D and an ordered pair (x,y) in D with x + y = p0 + p3 and p0 < x, y < p3. Its cells are:
- horizontal end (x, p0);
- corner (p3, p0);
- vertical end (p3, y).

Take d = x - p0. Then y = p0 + h - d, and the ordered pair runs over both orders of the middle pair, which covers d > h/2 as well.

By the Sidon property, either all four points lie in one copy, or p0 lies in copy c0, p3 lies in copy c3 with T_{c0} < T_{c3}, and the middle points are one in each of these copies.

**Same copy c, offsets x0 < x3, middle offsets {y,z} with y+z = x0+x3, both strictly between.** The h_c-coefficients give alpha0 + alpha3 = alpha_y + alpha_z.
- **All alpha = 0.** The atom vectors give a0 + a3 = a_y + a_z, where each term is one basis vector or 0, and a3 ≠ 0.
  - If a0 = 0, then {a3} is the nonzero part of {a_y, a_z}. So one of y, z equals 0 = x0, which is impossible.
  - If a0 ≠ 0, then {y,z} = {x0,x3}, which is also impossible.
- **All alpha = 1.** This is the symmetric case, applied to h_c - x.
- **Mixed.** Then x0 = a0 is small, x3 = h_c - a3 is large, y = a1 is small and z = h_c - a2 is large. The atoms give a0 + a2 = a1 + a3, and a1 > a0 because y > x0.
  - If a0 = 0, then a1 ≠ 0 forces a2 = a1 and a3 = 0.
  - If a0 ≠ 0, then a0 = a3 and a1 = a2.
  - Either way, a := a0 = a3 and b := a1 = a2 > a.

So the L's of copy c are exactly two for each a < b in A_c^0, and both have corner C_c(a), span h_c - 2a:
- **(S1)** horizontal end left (T_c+b, T_c+a), vertical end up (T_c+h_c-a, T_c+h_c-b);
- **(S2)** horizontal end (T_c+h_c-b, T_c+a) = M_c(b,a), vertical end (T_c+h_c-a, T_c+b) = M_c(a,b).

**Cross copies c0, c3.** Write the middle points as y in E_{c0} and z in E_{c3} (offsets). The atom sets of the two copies are disjoint, so a0 = a_y and a3 = a_z as vectors.
- If a0 ≠ 0, then the signs agree, so alpha0 = alpha_y and y = x0, which is impossible. So a0 = a_y = 0.
- If a3 ≠ 0, then x3 = z. The shift coefficients then force alpha0 = alpha_y, so x0 = y, which is impossible. So a3 = a_z = 0.

Hence x0, y, x3, z all lie in {0, h_c}. The order conditions give x0 = 0, y = h_{c0}, z = 0 and x3 = h_{c3}. The shift equation then gives h_{c0} = h_{c3} =: h. Points: T_{c0}, T_{c0}+h, T_{c3}, T_{c3}+h. There are two L's, both with corner (T_{c3}+h, T_{c0}):
- **(X1)** arms C_{c0}(0) and C_{c3}(0);
- **(X2)** arms (T_{c3}, T_{c0}) and (T_{c3}+h, T_{c0}+h).

There are no other L's. ∎

**Theorem B (properness).** chi is proper for every choice of the f_c and of rho.
- (S1): the corner has color rho(c), the left cell has color f ≠ rho(c).
- (S2): the corner has color rho(c), the horizontal end has color rho(c)+1.
- (X1) and (X2): the corner has color rho(c0)+1, and the horizontal end has color rho(c0) (for X1 this is C_{c0}(0); for X2 it is the low cell).

This also re-proves the repaired family. The finite checks for k = 2..6 agree with this but are no longer needed. ∎

## 2. Fibers and requests at a shift h in {h_c}

**Lemma C.** F_h(D) = {T_c : h_c = h}.
- **Same copy.** If x and x+h both lie in E_c ⊂ [0,h_c], then:
  - when h_c = h, x = 0;
  - when h_c < h, this is impossible;
  - when h_c > h, the difference h would be a power of B that is absent from the expansion of a difference of two elements of E_c (coefficients <= 2). This is impossible by the coefficient lemma.
- **Cross copies.** Differences between copies exceed max h. ∎

**Span-h L's.**
- S-type L's have span h_c - 2a. This equals h only if h_c = h and a = 0: otherwise h_c - h = 2a, which is a coefficient mismatch.
- X-type L's have span > h.

By (*), the start T_c (with h_c = h) has, for each b in A_c:
- the (S1) request of color f_c(0,b);
- the (S2) request of color rho(c)+1.

So **m_{e,h}(T_c) = #{b : f_c(0,b) = e} + |A_c|·[e = rho(c)+1]**, and m_{rho(c),h}(T_c) = 0.

### 2.1 Repaired family (three copies, rho(j) = j, |A_j| = k, |F_h| = 3)
- **Cyclic** (f_j ≡ j+1). m_{j+1}(T_j) = 2k and all other m vanish. N_e(h) = 2k, |R_e(h)| = 1, sum m^2 = 4k^2 for every e.
- **Balanced** (f_j(0,·) alternates between j+1 and j+2, starting with j+1). m_{j+1}(T_j) = k + ⌈k/2⌉ and m_{j+2}(T_j) = ⌊k/2⌋. N_e(h) = 2k, |R_e(h)| = 2 for k >= 2, and sum m^2 = (k+⌈k/2⌉)^2 + ⌊k/2⌋^2.
- In both cases min_e N_e/|F_h| = 2k/3 → ∞. **UW(lambda) fails for every lambda: PROVED.** (The quoted text said N_e >= k-1 or N_e = k; the correct value is 2k, because the mirrored L's add k requests.)
- **Padded** (add s further copies with A = ∅, shift h, Sidon tau, any rho). |F_h| = 3 + s, N_e = 2k, |R_e| = 1 (cyclic) and sum m^2 = 4k^2. The ratio is

      sum m^2 / (N + N^2/|F_h|) = 2k(3+s) / (3 + s + 2k).

  - Taking s = k gives a value of at least about (2/3)k, which is unbounded. **The U1-form energy bound fails for every C: PROVED.** (The quoted 2Ck < k^2 arithmetic is corrected to this.)
  - Taking s = ⌊√k⌋ gives N_e/|F_h| ~ 2√k → ∞ and |R_e|/|F_h| = 1/(3+s) → 0. **No union-growth bound |R_e| >= f(N_e/|F_h|)|F_h| with liminf_{λ→∞} f(λ) > 0 holds: PROVED.**
  - The quoted phrase "lim f > 1/q" is not a statement about a fixed f. The correct statement is the one just given.

### 2.2 Main task (D-b, many shifts) — Theorem D

Fix k. Let k' = 2k, r = k, s = ⌈√k'⌉ and m >= 1. Choose distinct shift powers h_1, ..., h_m.

For each shift index i, take:
- 3r "active" copies with h_c = h_i, |A_c| = k', and roles rho = 0,1,2 used r times each, with f_c ≡ rho(c)+1;
- r·s padding copies with h_c = h_i and A_c = ∅.

All copies use distinct tau from one Sidon set. This is an instance of section 0, so it is proper by Theorem B.

By Lemma C and the count above, for every h in W = {h_1, ..., h_m}:
- |F_h| = r(3+s) >= k;
- N_e(h) = 2k'r for every e;
- min_e N_e / |F_h| = 2k'/(3+s) ≈ 2√k' → ∞. Since k' = 2k, this is >= 2k/(1 + 1.5/√(2k))-ish. To get min_e N_e >= k|F_h| exactly, take s = 0 instead: then the ratio is 2k'/3 = 4k/3 >= k and |F_h| = 3k >= k.
- |R_e(h)| = r;
- sum_u m_{e,h}(u)^2 = 4k'^2 r.

**This holds for ALL h in W, and |W| = m is arbitrary.** Summing over W:
- sum_W min_e N_e >= k sum_W |F_h| (with s = 0);
- with s = ⌈√k'⌉, sum_W sum m^2 / sum_W (N + N^2/|F_h|) = 2k'(3+s)/(3+s+2k') → ∞, and sum_W |R_e| / sum_W |F_h| → 0.

So the W-averaged UW, energy and union-growth versions are refuted: PROVED.

**Caveat.** W is a sparse set of powers of B, not an interval. An interval average with weights a_h (h = 1..t-1) is NOT refuted. At other shifts h, F_h(D) is nonempty and carries few or no requests.

## 3. Which (D-a) variants survive

**Parameters of the family.**
- |D| = O(m r k' + m r s) and span ~ B^M · max tau. Here M > (number of atoms and shifts) = Θ(m r k'), so |D| = O(log span).
- Every class satisfies |S_e(d)| <= |F_d(D)| <= max(r(3+s), O(1)). For d = h_i the classes are the role groups, of size r (padding copies, of roles chosen freely, add up to rs).
- Fiber multiplicities: r_{S_e(d)}(l) <= 1 for d in W, because the starts T_c have pairwise distinct differences, which is the Sidon property. Generic d is realized O(1) times.
- The regime asks for classes ~ span^{1/2} and fibers ~ 10^4. The family is polylogarithmic in span with fibers <= 1, so it is very far from the regime.

**Killed (PROVED):**
- pointwise UW(lambda) for every lambda;
- the U1-type energy bound for every C;
- union growth with a positive limit;
- the same three statements averaged over any finite set of shifts.

**Survive (OPEN):** inequalities with any of the following hypotheses:
- (a) |S_e(d)| >= c·span^alpha, alpha > 0, or even |S_e(d)| >= (log span)^{1+eps};
- (b) r_{S_e(d)}(l) >= 2 for many l;
- (c) averaging over intervals of consecutive shifts with the weights a_h;
- (d) density hypotheses on D.

**Digit designs.** I did not prove that digit-type designs cannot reach (b). The reason they fail here is that r >= 2 needs undesigned additive quadruples u, u+l, u+d, u+d+l, which the Sidon and coefficient structure forbids. This is a heuristic only.

## 4. Embedding

Every member has span >= h >= B^{3·2+1} = 10^{14} with B = 100. Any B > 8 is enough for the coefficient lemma (bound 4 < B/2 requires B >= 9). Even with B = 9 and the smallest case k = 2, the 3-copy family has max T = 3·9^{9} ≈ 1.2·10^9.

This exceeds 21,987,408. That number is the largest side that can still be properly four-colored, given the proved bound R_4 <= 21,987,409 stated in the brief (cited from the brief, not re-derived). So **no member of these families is a diagonal class of a proper four-coloring of any square: PROVED** (from the span alone).

Whether a compressed, non-digit version embeds is OPEN. The construction is a counterexample to the ternary-source statements only.

## Summary

**PROVED:**
- Lemma A (all L's of the general digit family, mirrored and cross ones included);
- Theorem B (properness for every f and rho, including the repaired family for all k >= 2);
- Lemma C;
- exact N_e, |R_e| and sum m^2 for the cyclic, balanced and padded choices;
- refutation of UW(lambda), of U1-type energy bounds for every C, and of union growth with a positive limit;
- Theorem D (all three refutations simultaneously on m arbitrary shifts, with |F_h| >= k and min_e N_e >= k|F_h| on every h in W);
- non-embeddability of these families by span.

**OPEN:**
- the (D-a) variants (a)–(d) listed in section 3, in particular interval-averaged versions and versions with fiber multiplicity >= 2 or polynomial class sizes;
- whether digit designs can reach r >= 2 fibers;
- embeddable counterexamples.

