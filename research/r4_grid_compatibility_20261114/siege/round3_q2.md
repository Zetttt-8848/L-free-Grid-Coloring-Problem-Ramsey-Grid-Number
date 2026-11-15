kind: attempt

Open question attempted (flagged OPEN by this run, ledger "(D-c): whether foreign requests force an explicit proportional imbalance lowering r_{S_e(d)}(l) below v_l"): Fix X = S_e(d), a lag l, h = d+l, the Golomb classes G' = G_{e'}, G'' = G_{e''} of F_l(X) (by the color of (u+h,u)), and the foreign-requested sets A = F_l(X) ∩ R_{e'}(h) ⊆ G'', B = F_l(X) ∩ R_{e''}(h) ⊆ G'. Settle the statement
  (D-c+) if |A| >= alpha |G''| then |G'| <= (1-beta)|G''| (or any explicit imbalance),
by EITHER (preferred, since the single-L analysis below shows no one-step obstruction) an explicit family of proper ternary sources, for every k >= 1, with |G'| = |G''| = k, A = G'' and B = G' (every fiber point foreign-requested, both classes equal), with a complete proof of properness covering every L; OR a proof of an explicit imbalance via chains of two or more L's.

## Facts you may use (proved earlier in this run; checked)
- Lemma 0. Every directed L inside V(D) is L(u,d,h) for exactly one triple of integers with 1 <= d < h. Its cells are the horizontal end (u+d,u), the corner (u+h,u) and the vertical end (u+h,u+h-d); its arm length is h-d. It lies in V(D) iff u, u+d, u+h-d, u+h all lie in D. Here d ranges over ALL of [1,h-1], including d > h/2 (then u+d > u+h-d). Equivalently: for p0 < p3 in D and an ORDERED pair (x,y) in D with x+y = p0+p3, p0 < x,y < p3, there is the L with cells (x,p0), (p3,p0), (p3,y); when x ≠ y both orders give distinct L's ("mirrored" L's). Every construction must handle both orders.
- (i) L(u,d,h) is monochromatic of color e iff u ∈ F_{h-d}(S_e(d)) ∩ S_e(h). Hence chi is proper iff S_e(h) ∩ R_e(h) = ∅ for all h >= 2 and all e. Equivalently: u ∈ F_{h-d}(S_e(d)) iff the L with corner (u+h,u) has BOTH arm cells of color e, so m_{e,h}(u) counts the L's with corner (u+h,u) whose two arms both have color e.
- (ii) R_e(h) ⊆ F_h(D). (iii) Every u ∈ F_h(D) lies in at most two of R_0(h), R_1(h), R_2(h), and u ∈ R_e(h) ∩ R_{e'}(h), e ≠ e', forces u ∈ S_{e''}(h). Sharp identity: sum_e |R_e(h)| = 2|F_h(D)| - 2#{u in no R_e(h)} - #{u in exactly one}.
- Row/column form of properness (immediate from Lemma 0): for u < v in D with h = v-u, write w_u(x) = chi(u+x,u) (row word of u) and c_v(x) = chi(v,v-x) (column word of v). Then chi is proper iff, for all such u,v and every d in (0,h) with u+d, v-d in D, NOT w_u(d) = c_v(d) = w_u(h). (Note w_u(h) = c_v(h) is the shared corner cell.)

## The single-class structure, quoted verbatim from an earlier answer in this run (checked)
--- begin quote ---
### (iv) Inside one class
Fix `X = S_e(d)`, `l >= 1`, `h = d+l`. Define `psi(a,b) = chi(b+d,a)` for `a<b` in `X`. These are the cells of the shifted source; they lie in `V(D)` because `a, b+d in D`.

**(iv.0) The shifted source avoids `e`.** For `a<b` in `X`, `L(a,d,d+(b-a))` has horizontal arm end `(a+d,a)` of color `e` (because `a in X`), vertical arm end `(b+d,b)` of color `e` (because `b in X`), and corner `(b+d,a)`. So `psi(a,b) ≠ e`. This is (i) applied to the `d`-term of `R_e(d+b-a)`. Hence `psi` takes values in `{e',e''}`.

**(iv.1) `F_l(X) ⊆ R_e(h)`.** `F_l(X) = F_{h-d}(S_e(d))` is the `d`-term of `R_e(h)`. ∎

**Color identification.** For `u in F_l(X)` we have `u, u+l in X`, so `chi(u+h,u) = psi(u,u+l)`, which lies in `{e',e''}`. Put `G_f = {u in F_l(X) : chi(u+h,u) = f}` for `f in {e',e''}`. These two sets partition `F_l(X)`, and `G_f = F_l(X) ∩ S_f(h)`.

**(iv.2) Golomb split, proved from scratch.** Each `G_f` is a Sidon set. More precisely, there are no `u_1` and `r, s > 0` with `u_1, u_1+s, u_1+r, u_1+r+s` all in `G_f`. The case `r = s` (a 3-term progression) is included. This is equivalent to all positive differences within `G_f` being distinct, including pairs that share an element, i.e. `a+b = a'+b'` only trivially.

*Proof.* Suppose such points exist. Let `g` be the other color of `{e',e''}` and put `u_2 = u_1+r`. All points `u_1+r+s+l`, `u_1+r+l`, `u_1+s+l`, `u_1+l` lie in `X`, since the four points lie in `F_l(X)`. Four L's:
- **L1** `= L(u_1, h, h+r)`: cells `(u_1+h,u_1)` [color f], corner `(u_1+h+r,u_1)`, `(u_1+h+r,u_1+r)` [color f, since `u_2 in G_f`]. So `chi(u_1+h+r,u_1) ≠ f`. This cell is `psi(u_1,u_1+l+r)`, so it is not `e` by (iv.0). Hence it is `g`.
- **L2** `= L(u_1+s, h, h+r)`: same argument with the pair `u_1+s, u_2+s in G_f`. So `chi(u_1+s+h+r, u_1+s) = g`.
- **L3** `= L(u_1, h+r, h+r+s)`: cells `(u_1+h+r,u_1)` [g by L1], corner `(u_1+h+r+s,u_1)`, `(u_1+h+r+s,u_1+s)` [g by L2]. So the corner is not `g`. It equals `psi(u_1,u_1+l+r+s)`, so it is not `e`. Hence it is `f`.
- **L4** `= L(u_1, h, h+r+s)`: cells `(u_1+h,u_1)` [f], corner `(u_1+h+r+s,u_1)` [f by L3], `(u_1+h+r+s,u_1+r+s)` [f, since `u_2+s in G_f`]. This L is monochromatic, a contradiction. ∎

The L's used are L1–L4, all of the form `L(·, h', h'')` with base offset `h' in {h, h+r}`, together with the source-avoidance L's of (iv.0).

**(iv.3)** Put `A = F_l(X) ∩ R_{e'}(h)`. For `u in A`:
- `u in R_{e'}(h)`, so `u ∉ S_{e'}(h)` by (i);
- `u in R_e(h)` by (iv.1), so `u ∉ S_e(h)`.

Hence `u in S_{e''}(h)`, that is, `u in G_{e''}`. Likewise `B = F_l(X) ∩ R_{e''}(h) ⊆ G_{e'}`. Finally, `A ∩ B ⊆ R_e ∩ R_{e'} ∩ R_{e''} = ∅` by (iii). ∎

--- end quote ---

## Earlier analysis of (D-c), quoted verbatim from an earlier answer in this run
**B1 (proved; immediate).** `A ⊆ G_{e''}` and `B ⊆ G_{e'}`, so `A` and `B` are Sidon sets. If `span` denotes the span of `F_l(X)`, then `|A|, |B| <= Q(span)`, and `|A| + |B| <= |F_l(X)|` because `A ∩ B = ∅`. This follows immediately from (iv.3) and (iv.2), since subsets of Sidon sets are Sidon. It gives nothing beyond the existing cap `r_X(l) = |G_{e'}| + |G_{e''}| <= 2Q`-type bounds.

**B2 (imbalance): not proved; OPEN.** I could not derive any statement of the form "if `|A| >= alpha·Q` then `r_X(l) <= (1-delta)v_l`".

Why the constraints listed in (i)–(iv) cannot give this by themselves: here is an abstract model that satisfies every constraint (ii)–(iv) places on one fiber. Take
- any partition `F_l(X) = G' ⊔ G''` into two Sidon sets, each of maximum size `Q`;
- any `A ⊆ G''` and `B ⊆ G'`, for example `A = G''` and `B = G'`, so that a full proportion of the fiber is foreign-requested.

The constraints (ii)–(iv) on this fiber are exactly:
- (C1) `A ⊆ G''` and `B ⊆ G'`;
- (C2) `A ∩ B = ∅`;
- (C3) `G'` and `G''` are Sidon.

All three hold, and `r_X(l)` attains `2Q`. So imbalance cannot follow from (i)–(iv) as stated. As the task note says, containing a large prescribed Sidon subset does not shrink a Sidon set.

The model ignores the genuine L-constraints that **generate** `A`. Each `u in A` has a witness `d' < h` with `u, u+h-d' in S_{e'}(d')`. So, beyond (C1)–(C3), the following hold for each such `u`:
- (C4) `chi(u+d',u) = chi(u+h,u+h-d') = e'` and `chi(u+h,u) = e''`;
- (C5) the binary-source/Golomb structure of the foreign class `S_{e'}(d')` at lag `h-d'`, which contains `u` in its own Golomb class of color `e''` (by (iv.3) applied to `S_{e'}(d')`);
- (C6) the L's `L(u, h, h+s)` mixing the fiber `G''` with cells of the foreign source.

The unresolved question is whether (C4)–(C6), applied simultaneously for all `d'`, constrain `|G'|`. I found no joint configuration of L's that bounds `|G'| + |G''|` in terms of `|A|`. The four-L argument of (iv.2) only uses same-color cells. Foreign requests contribute cells of color `e'` at positions `(u+d',u)`, which lie on rows `u` but off the offsets `h + r` that the Golomb L's use. So I see no direct interaction.

I did not construct an explicit ternary source realizing the model. That would need many classes and a full properness check, which I could not do reliably by hand. The existence of a genuine counterexample is therefore also OPEN.

## Single-L coupling lemma, quoted verbatim from the previous round's answer (proved)
## 1. Single-L coupling lemma (PROVED)

Fix u ∈ A with witness d' < h, d' ≠ d is not needed: u, u+h-d' ∈ S_{e'}(d'). The
witness cells are W1 = (u+d',u) and W2 = (u+h,u+h-d'), both of color e'; the
own cells of u are (u+d,u), (u+h,u+l) (color e) and (u+h,u) (color e'').
Let w ∈ F_l(X), w ≠ u, with Golomb cell C_w = (w+h,w).

**Lemma 1.** An L containing C_w and a witness cell W1 or W2 of u exists only in
the following two shapes, both of which are L(w, d', h):
- w = u-(h-d'): the L has ends (w+d',w), (w+h,w+h-d') = W1 and corner C_w;
- w = u+(h-d'): the L has ends (w+d',w) = W2, (w+h,w+h-d') and corner C_w.

In each case the L is the d'-term request L of w itself, i.e. it constrains C_w only
when w ∈ F_{h-d'}(S_{e'}(d')), and then forces w ∉ S_{e'}(h), i.e. (since w ∈ R_e(h))
w ∈ G''. It never constrains membership in G'.

*Proof.* An L has two cells in its bottom row p0 (corner, horizontal end) and one
cell in row p2 > p0 in the corner's column. We check all role pairs.

(a) W1 = (u+d',u) and C_w = (w+h,w), rows u ≠ w.
- C_w corner, W1 horizontal end: same row needed, u = w; excluded.
- C_w corner, W1 vertical end: column u+d' = w+h, and arm equality: horizontal end
  (p1,w) with p1 = w+h-(u-w)... precisely p3-p1 = u-w, so p1 = w+h-(u-w) = w+d'
  using u = w+h-d'. This is the first listed shape.
- C_w horizontal end, W1 corner: same row, excluded. W1 vertical end: corner
  (u+d',w) with u+d' > w+h, arms u+d'-w-h and u-w; equal iff d' = h; excluded.
- C_w vertical end: corner (w+h,p0), p0 < w. W1 corner: u+d' = w+h and u < w give
  d' > h; excluded. W1 horizontal end: p0 = u, arms (w+h)-(u+d') and w-u, equal iff
  d' = h; excluded.

(b) W2 = (u+h,u+h-d') and C_w, columns u+h ≠ w+h.
- C_w corner: W2 vertical end needs column w+h, excluded; W2 horizontal end needs
  row w = u+h-d', horizontal arm (w+h)-(u+h) = w-u = h-d', so the vertical end is
  (w+h, w+h-d') and the horizontal end (u+h,w) = (w+d',w) = W2. Second shape.
- C_w horizontal end (row w, corner column p3 > w+h): W2 corner needs row w,
  i.e. u+h-d' = w, column u+h = w+d' < w+h; excluded. W2 vertical end: p3 = u+h,
  arms u-w and u+h-d'-w, equal iff d' = h; excluded.
- C_w vertical end (corner (w+h,p0), p0<w): W2 corner needs column w+h; excluded.
  W2 horizontal end: p0 = u+h-d', arms (w+h)-(u+h) = w-u and w-(u+h-d'), equal iff
  d' = h; excluded. ∎

Also (proved in the quoted (iv.2) argument, restated): the L's containing the
own cell (u+h,u) of u ∈ A and C_w are L(min, h, h+|w-u|); when both lie in G''
they force the corner to be e' (via (iv.0)); when w ∈ G' they force nothing. So
no single L joins "u is foreign-requested" with "w ∈ G'".

**Consequence.** Any implication "|A| large ⇒ |G'| small" must pass through
chains of at least two L's sharing a cell that is not one of the listed
determined cells (free cells, each a priori with two admissible colors). The
one-step argument (C4)–(C6) of the earlier answer therefore cannot give D-c+;
this is now a proof, not an impression, for single L's.

## A construction technique that is PROVED in this run: the general digit family, quoted verbatim from the previous round's answer
(Implicit in it and required: every atom of copy c is smaller than its shift h_c, so that E_c ⊂ [0,h_c]. With that proviso the director checked properness by enumerating all L's on 150 random instances, including equal roles and several shifts: no monochromatic L. The proof below is the authority.)
--- begin quote ---
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
--- end quote ---
Further facts about this family (same answer): at a shift h in {h_c}, F_h(D) = {T_c : h_c = h}; the start T_c receives, for each atom b, the (S1) request of color f_c(0,b) and the (S2) request of color rho(c)+1, so m_{rho(c),h}(T_c) = 0. Its classes S_e(d) are tiny and its fibers have multiplicity <= 1, so it does NOT by itself realize a fiber F_l(X) with large Golomb classes; you must design one.

## Task
1. Design. Build, for every k, a proper ternary source containing a class X = S_e(d) and a lag l such that F_l(X) has k points in each Golomb class G', G'', and every point of G'' is in R_{e'}(h) and every point of G' is in R_{e''}(h) (h = d+l). A natural route: let X contain pairs u, u+l for u in a Sidon set U = U' ⊔ U'' of size 2k (digits or a Sidon set of a different scale), give (u+h,u) color e'' on U'' and e' on U', and supply for each u ∈ U'' a witness shift d'_u with u, u+h-d'_u ∈ S_{e'}(d'_u) (and symmetrically for U'), all with fresh digit coordinates so that the only additive relations among points of D are the designed ones. Then list ALL L's (both middle orders; same-copy and cross-copy cases; L's of the binary structure of X itself, i.e. (iv.0) and (iv.2)) and prove each non-monochromatic. Explicitly check that the Golomb split does not forbid your fiber: G', G'' must be Sidon.
2. If a design fails, identify the forced monochromatic L chain and turn it into an imbalance statement with explicit constants.
3. State exactly what the result kills or establishes for (D-c): an explicit family refutes D-c+ for arbitrary ternary sources (at the sparse scale of the construction); say which near-extremality hypothesis (class sizes, fiber sizes relative to Q(span)) would still be needed for a positive (D-c) statement, and which consumer quantity (v_l, K via the rank-neighbor inequality, U_d) it would lower.

Rules: every proof complete and from the cell coordinates; every counterexample explicit and checkable L by L (both orders of every middle pair); finite computations are evidence only. Do not import three-color facts. End with the exact statements proved, refuted, and still open.
