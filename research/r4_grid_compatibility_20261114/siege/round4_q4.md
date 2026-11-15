kind: attempt

Open question attempted (flagged OPEN by this run, ledger entry 41): the missing statement MS below. YOUR TASK IS TO TRY TO REFUTE MS EXACTLY AS STATED: for every delta > 0 (or for every delta in a range that defeats every explicit choice), exhibit an explicit proper ternary source (D, chi), a shift d and a lag bound lambda that violate the inequality, with a complete L-by-L proof of properness; or derive from MS something known to be false. If after a serious attempt you believe MS true, say why (the obstruction your constructions hit), and prove whatever rigorous partial statement you reached - e.g. an explicit upper bound on how close to 1 the ratio sum_{l<=lambda} sum_e r_{S_e(d)}(l) / sum_{l<=lambda} 3v_l can get for some natural class of constructions, or an explicit family achieving a ratio bounded below by a positive constant (that is not a refutation, but it is useful).

**Missing statement (MS).** Let Q(m), for m >= 0, be the largest size of a Sidon set (no a+b = c+d except trivially, 3-term progressions included) contained in m+1 consecutive integers, and put Q(m) = 0 for m < 0. Then there is an explicit absolute constant delta > 0 such that the following holds for every proper ternary source (D, chi), i.e. every finite set D of integers with a coloring chi of V(D) = {(v,u) : u < v, u,v in D} by P = {0,1,2} having no monochromatic directed L (x,y),(x+t,y),(x+t,y+t), t > 0. For every d >= 1 with F_d(D) nonempty, write
- S = max F_d(D) - min F_d(D);
- v_l = Q(S-l) + Q(S-l-1), the per-class fiber cap of the consumer;
- S_e(d) = {u in F_d(D) : chi(u+d,u) = e};
- r_X(l) = #{u in X : u+l in X}.

Then for every integer lambda with 1 <= lambda <= S,

    sum_{l=1}^{lambda} sum_{e in P} r_{S_e(d)}(l)  <=  (1-delta) * sum_{l=1}^{lambda} 3 v_l.

Equivalently: the lag-l agreement counts of the 3-colored word z_d(u) = chi(u+d,u) on F_d(D), summed over l <= lambda, fall a fixed proportion short of three times the summed single-class caps. (Each single class satisfies r_{S_e(d)}(l) <= v_l, by the Golomb split below, so the statement asks that the three classes cannot be jointly saturated, in the prefix-averaged sense, for any lambda.) For small S it holds trivially (r_{F_d(D)}(l) <= S-l+1 is far below 3v_l); its content is at large S, in particular at the scale S ~ 2.2*10^7 of the problem.

## Why this matters
MS is the one missing statement of a chain that would turn the per-class binary-source caps of the R4 consumer into a proportional joint saving: by a summed rank-neighbor inequality, a prefix-dominated joint deficit with constant delta lowers the joint cap sum_e |S_e(d)| <= (1-delta')3K(S). A refutation shows the three completion classes at one shift can be jointly saturated in the prefix sense, so no saving of this form exists; that is a result the run must know.

## What a violation needs
A ratio near 1 at some (d, lambda) means: for most lags l <= lambda, all six Golomb pieces G_e^f(l) = {u : u, u+l in S_e(d), chi(u+d+l,u) = f}, e != f, are Sidon sets of size close to Q(S-l) (each class's fiber F_l(S_e(d)) splits into the two Sidon pieces by the Golomb split below, which is why r_{S_e(d)}(l) <= v_l). Already lambda = 1 would do: six disjoint near-maximal Sidon sets in the span, each consisting of starts u with u, u+1 in the same class S_e(d), with prescribed corner colors. Two disjoint Sidon sets can each be near-maximal (a Singer perfect difference set and a translate of it minus one point), so the obstruction, if any, is in the L's, not in additive combinatorics of disjoint Sidon sets alone. Explicit near-maximal Sidon sets (Singer, Bose-Chowla, Erdos-Turan {2p*i + (i^2 mod p)}) and product/lifting constructions are natural tools.

## Proved facts you may use (spliced verbatim from earlier answers in this run; all checked)

### P1: the parametrization of L's, the exact reformulation, the double cover, and the Golomb split
### Lemma 0 (parametrization of the L's in V(D))
For integers `u`, `1 <= d < h`, let `L(u,d,h)` be the triple
`(u+d,u)` (horizontal arm end), `(u+h,u)` (corner), `(u+h,u+h-d)` (vertical arm end), arm length `t = h-d`.

(a) `L(u,d,h)` is a directed L: take `x=u+d, y=u, t=h-d>0`. Then `(x+t,y) = (u+h,u)` and `(x+t,y+t) = (u+h,u+h-d)`.

(b) `L(u,d,h) ⊆ V(D)` iff `u, u+d, u+h-d, u+h` all lie in `D`. Proof: `(u+d,u) in V(D)` iff `u,u+d in D` (because `u+d>u`). `(u+h,u) in V(D)` iff `u,u+h in D` (because `h>0`). `(u+h,u+h-d) in V(D)` iff `u+h-d, u+h in D` (because `u+h > u+h-d`, since `d>0`). The point `u+h-d > u` because `h>d`. Collecting these gives the claim.

(c) Every directed L inside `V(D)` equals `L(u,d,h)` for exactly one triple. Proof: let `(x,y),(x+t,y),(x+t,y+t)` lie in `V(D)`. Since `(x,y) in V(D)` we have `x>y`. Put `d = x-y >= 1`, `u = y`, `h = d+t > d`. Then the triple is `L(u,d,h)`. Conversely, `L(u,d,h)` determines `y=u`, `x=u+d`, `t=h-d`. So the map `(u,d,h) -> L(u,d,h)` is a bijection from `{1<=d<h}` with condition (b) onto the L's in `V(D)`.

**Edge cases.** If `d = h-d` or `u+d = u+h-d`, the four points in (b) are not distinct. Condition (b) is still a membership condition on the set `{u,u+d,u+h-d,u+h}`, so nothing changes. The three cells of the L are always distinct, since their x-coordinates are `u+d < u+h` and the last two differ in y (`h-d > 0`). Also `d = t` is allowed: nothing in the argument requires `d ≠ h-d`.

### (i) Exact reformulation
**Claim.** `chi` is proper iff `S_e(h) ∩ R_e(h) = ∅` for all `h >= 2` and all `e in P`.

**Colors of the three cells of `L(u,d,h)`.**
- `chi(u+d,u) = e` iff `u in S_e(d)`.
- Write `w = u+(h-d)`. The vertical arm end is `(u+h,u+h-d) = (w+d,w)`, so `chi(w+d,w) = e` iff `u+(h-d) in S_e(d)`.
- `chi(u+h,u) = e` iff `u in S_e(h)`.

So `L(u,d,h)` lies in `V(D)` and is monochromatic of color `e` iff
`u in S_e(d)`, `u+(h-d) in S_e(d)` and `u in S_e(h)`,
that is, iff `u in F_{h-d}(S_e(d)) ∩ S_e(h)`. These memberships imply condition (b): `S_e(d) ⊆ F_d(D)` gives `u, u+d, u+h-d, u+h in D`.

Taking the union over `1 <= d < h` shows that there is a monochromatic e-colored L with corner row `u` and corner column `u+h` iff `u in S_e(h) ∩ R_e(h)`. By Lemma 0(c), every L in `V(D)` has this form for exactly one `(u,d,h)`. Hence chi has a monochromatic L iff some `S_e(h) ∩ R_e(h)` is nonempty. Both directions follow.

**L's used.** All L's in `V(D)`, in the form `L(u,d,h)`. The corner is `(u+h,u)`, the arms end at `(u+d,u)` and `(u+h,u+h-d)`, and the arm length is `h-d`. The term `d` of `R_e(h)` is exactly the set of L's with corner on diagonal offset `h` and arm length `h-d`.

### (ii) Containment `R_e(h) ⊆ F_h(D)`
Let `u in F_{h-d}(S_e(d))`.
- Then `u in S_e(d) ⊆ F_d(D)`, so `u in D`.
- Also `u+h-d in S_e(d) ⊆ F_d(D)`, so `u+h = (u+h-d)+d in D`.

Hence `u in F_h(D)`. ∎

### (iii) Double cover
Let `k(u) = #{e : u in R_e(h)}` for `u in F_h(D)`. Since `S_0(h), S_1(h), S_2(h)` partition `F_h(D)`, `u` lies in `S_f(h)` for exactly one `f`. By (i), `u ∉ R_f(h)`, so `k(u) <= 2`. If `u in R_e(h) ∩ R_{e'}(h)` with `e ≠ e'`, then `f ∉ {e,e'}`, so `f = e''`.

By (ii), every request lies in `F_h(D)`, so `sum_e |R_e(h)| = sum_{u in F_h(D)} k(u)`. Pointwise, `k(u) <= 2 - [k(u) <= 1]`: if `k(u) = 2` both sides equal 2, and if `k(u) <= 1` the right side is 1. Summing gives the inequality **as posed, which is correct**:
`sum_e |R_e(h)| <= 2|F_h(D)| - #{u in F_h(D) : k(u) <= 1}`.

The sharp form is the identity
`sum_e |R_e(h)| = 2|F_h(D)| - 2·#{k=0} - #{k=1}`.

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


### A general digit family that is proper (from an earlier answer; checked by computer on random instances)
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


### Lifting by a fine Sidon block (from a later answer; checked by computer on small instances). Here "the digit family of section 0 of the quoted answer" is the family just quoted.
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

Note: these families are proper but far from saturation: their fibers are at most |G| ~ sqrt(span)/(huge constant), far below v_l, so they do not refute MS. They show how proper sources with controllable completion classes can be built; whether such methods can saturate the caps is the question.

## Rules
Every counterexample explicit and checkable L by L, with both middle orders of each L handled (every L is L(u,d,h) with 1 <= d < h, including d > h/2). Finite computations are evidence only for exactly what they check. Do not import three-color facts. End with the exact statements proved and what stays open.
