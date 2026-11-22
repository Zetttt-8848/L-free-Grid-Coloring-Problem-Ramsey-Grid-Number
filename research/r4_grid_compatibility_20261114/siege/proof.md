# Request geometry inside a three-colored diagonal class: what is proved, and what is open

## Answer in brief

- **Part P1 (i)-(v) holds exactly as posed, for every ternary source and every h ≥ 2.** The complete proof from the cell coordinates is Theorem 1 (Section 1).
- **Part D is not settled.** No proportional-loss inequality (D-a) with an explicit δ > 0 is proved for ternary sources of regime size. No regime-size counterexample (D-b) is given either. What is proved toward Part D:
  - (D-b) over arbitrary sources (Section 2). Explicit proper families, proved proper L by L, refute every request-counting inequality of the proposed kinds over arbitrary ternary sources.
  - (D-c) (Section 3). The forced sets are Golomb, but this costs nothing. An explicit proper family has full foreign-request coverage and balanced Golomb classes. Under near-extremality, an imbalance is the same thing as a fibre deficit.
  - An exact reduction (Section 4). Per shift and against the certified Fejér single-class caps, (D-a) is equivalent to the statement FD, up to O(S^{-3/8}).
  - A further sufficient reduction (Section 4.9). FD follows from NTSD, a statement about two disjoint near-maximal Sidon sets carrying a two-layer coloring. The implication is proved with explicit constants (Theorem R). NTSD itself is open. Its first-generation part is decided exactly (Theorem P, Section 4.10).
- **No bound on R_4 is claimed.** Section 5 gives only conditional implications.

The final sections "Status" and "Other routes" say exactly what is and is not proved.

Labels: **PROVED** means proved in full in this document. **CITED** marks a classical fact quoted by name. **HEURISTIC** marks an estimate that nothing depends on. Small members of every construction in Section 2 and Section 3 were also checked exhaustively by computer against every L; those checks are evidence only, and every claim below is proved by hand in the text. The members checked were:
- a two-shift instance of Theorem 2.6 (k' = 2, r = 1, s = 1; 40 points, 60 L's): proper, with |F_h| = 4, N_e = 4, |R_e| = 1 and Σ m^2 = 16 at both shifts, as predicted;
- the three-copy family of Theorem 2.4 with k = 2, 3, 4 and random admissible f_c: proper;
- the (H)-failure example of Section 2.2: monochromatic, as stated;
- the lifted family of Section 2.3 with (p, r, k, m') = (5,1,1,2), (5,1,2,2), (7,2,1,2): proper, with the counts of Theorem 2.10;
- the family of Theorem 3.2 with k = 1, 2, 3: proper, with X = F_d(D), |F_l(X)| = 2k, A = G_2 and B = G_1;
- the m = 23 datum of Section 4.10, the Bose translates of "Other routes", and the numerical values in Sections 4-5;
- Theorem P of Section 4.10, on 2,990 random small instances.

The family of Theorem 3.2 (k = 1, 2, 3: 32, 144 and 336 L's) and the numerics of Sections 4-5 were rechecked independently at the last revision.

---

---

## 0. Conventions

- A cell is (x,y): column x, row y. A directed L is (x,y),(x+t,y),(x+t,y+t) with t > 0. Its **corner** is (x+t,y). Its **horizontal arm end** is (x,y) and its **vertical arm end** is (x+t,y+t). The arm length is t.
- A ternary source (D,χ): D ⊂ Z finite, V(D) = {(v,u) : u < v; u,v ∈ D}, χ : V(D) → P = {0,1,2}. Proper means no monochromatic directed L with all three cells in V(D).
- Notation as in the problem: F_t(X), r_X(t), S_e(d), R_e(h), m_{e,h}, N_e(h). Throughout, {e,e',e''} = P are three distinct colors. Colors are taken mod 3 where a formula adds them.
- A **binary source** is a finite set X ⊂ Z with a proper coloring of V(X) by two colors.
- **Sidon set.** A Sidon set is a set with no solution of a+b = a'+b' other than the trivial ones, repeated summands included. So 3-term progressions are excluded. Q(m), for m ≥ 0, is the largest size of a Sidon set inside m+1 consecutive integers. Q(m) = 0 for m < 0, and Q is nondecreasing.
- **Span.** span X = max X − min X. For a fixed shift d of a source we write S = span F_d(D), v_l = Q(S−l) + Q(S−l−1), and c(S) = sqrt(v_1 S).

---

## 1. Theorem 1 (Part P1, complete). PROVED

### Lemma 0 (parametrisation of all L's in V(D))

For integers u and 1 ≤ d < h, let L(u,d,h) be the triple

- horizontal arm end (u+d, u),
- corner (u+h, u),
- vertical arm end (u+h, u+h−d),

with arm length h−d.

(a) L(u,d,h) is a directed L: take x = u+d, y = u, t = h−d > 0.

(b) L(u,d,h) ⊆ V(D) iff u, u+d, u+h−d, u+h all lie in D. The three cells lie in V(D) iff the pairs {u, u+d}, {u, u+h}, {u+h−d, u+h} lie in D, because the order conditions u < u+d, u < u+h, u+h−d < u+h hold automatically.

(c) Every directed L inside V(D) equals L(u,d,h) for exactly one triple. Given (x,y),(x+t,y),(x+t,y+t) in V(D), we have x > y. Put u = y, d = x−y ≥ 1, h = d+t > d. Conversely, L(u,d,h) determines y = u, x = u+d, t = h−d.

Coincidences such as d = h−d are harmless: condition (b) is a membership condition on the set {u, u+d, u+h−d, u+h}. The three cells are always distinct.

**Colors of the three cells.** χ(u+d,u) = e iff u ∈ S_e(d). The vertical arm end is (w+d, w) with w = u+h−d, so χ(u+h,u+h−d) = e iff u+h−d ∈ S_e(d). χ(u+h,u) = e iff u ∈ S_e(h). Hence:

> **(★)** L(u,d,h) lies in V(D) and is monochromatic of color e iff u ∈ F_{h−d}(S_e(d)) ∩ S_e(h).

Membership in S_e(·) already contains the D-membership conditions of (b). Also, m_{e,h}(u) is the number of L's with corner (u+h,u) whose two arm cells both have color e.

### (i) Exact reformulation

**Claim.** χ is proper iff S_e(h) ∩ R_e(h) = ∅ for every h ≥ 2 and every e ∈ P.

*Proof.* By (★), a monochromatic e-colored L with corner (u+h,u) exists iff u ∈ S_e(h) ∩ ⋃_{d<h} F_{h−d}(S_e(d)) = S_e(h) ∩ R_e(h). By Lemma 0(c), every L in V(D) has this form for exactly one (u,d,h). Both directions follow. ∎

**L's used.** All L's of V(D), each as L(u,d,h). The corner is (u+h,u), on diagonal offset h. The two arms end at (u+d,u) and (u+h,u+h−d), both on diagonal offset d < h. The arm length is h−d. The d-term F_{h−d}(S_e(d)) of R_e(h) is exactly the set of corner rows of the L's with corner offset h and arm length h−d whose two arms have color e.

**Inductive form (PROVED, immediate).** Every L has its corner on a strictly larger diagonal offset than its arms. So χ is proper iff, for every h and every u ∈ F_h(D), the corner color χ(u+h,u) avoids every color e with u ∈ R_e(h). Here R_e(h) depends only on the colors at offsets < h. In particular, given the colors at offsets < h, the cells at offset h can be colored so that every L with corner offset h is non-monochromatic iff R_0(h) ∩ R_1(h) ∩ R_2(h) = ∅. (Informal reading, not a theorem: single-shift counting constrains |F_h(D)| only from below, because a large union of requests must fit inside F_h(D).)

### (ii) Containment R_e(h) ⊆ F_h(D)

If u ∈ F_{h−d}(S_e(d)), then u ∈ S_e(d) ⊆ F_d(D) ⊆ D. Also u+h−d ∈ S_e(d) ⊆ F_d(D), so u+h = (u+h−d)+d ∈ D. Hence u ∈ F_h(D). ∎

### (iii) Double cover

For u ∈ F_h(D), let k(u) = #{e : u ∈ R_e(h)}. The classes S_0(h), S_1(h), S_2(h) partition F_h(D), so u ∈ S_f(h) for exactly one f, namely f = χ(u+h,u). By (i), u ∉ R_f(h). Hence k(u) ≤ 2. If u ∈ R_e(h) ∩ R_{e'}(h) with e ≠ e', then f ∉ {e,e'}, so f = e''.

By (ii), Σ_e |R_e(h)| = Σ_{u∈F_h(D)} k(u). Pointwise k(u) ≤ 2 − [k(u) ≤ 1]. Summing gives the inequality as posed:

  Σ_e |R_e(h)| ≤ 2|F_h(D)| − #{u ∈ F_h(D) : k(u) ≤ 1}.

The sharp form is the identity Σ_e |R_e(h)| = 2|F_h(D)| − 2#{k=0} − #{k=1}. ∎

No three-color fact was imported: "at most two of three" was derived from the partition of F_h(D) and from (i).

### (iv) Inside one class

Fix X = S_e(d), a lag l ≥ 1, and h = d+l. For a < b in X put ψ(a,b) = χ(b+d, a). This cell lies in V(D), because a, b+d ∈ D and b+d > a.

**(iv.0) The shifted source is a binary source avoiding e. PROVED.**
- For a < b in X, the L L(a, d, d+(b−a)) has horizontal arm end (a+d,a), of color e because a ∈ X. Its vertical arm end is (b+d,b), of color e because b ∈ X. Its corner is (b+d,a). So ψ(a,b) ≠ e, and ψ takes values in {e', e''}.
- ψ is proper on V(X) under the identification (b,a) ↦ (b+d,a). An L (x,y),(x+t,y),(x+t,y+t) in V(X) maps to (x+d,y),(x+t+d,y),(x+t+d,y+t). That is a directed L of V(D): it is the horizontal translate by d, and x+d > y, x+t+d > y+t.
- So X is a binary source. The same holds for every subset of X (heredity), and span X ≤ span F_d(D).

**(iv.1) F_l(X) ⊆ R_e(h).** F_l(X) = F_{h−d}(S_e(d)) is the d-term of R_e(h). ∎

**Color identification.** For u ∈ F_l(X) we have u, u+l ∈ X, so χ(u+h, u) = ψ(u, u+l) ∈ {e', e''}. For f ∈ {e',e''} put G_f = {u ∈ F_l(X) : χ(u+h,u) = f} = F_l(X) ∩ S_f(h). The two Golomb classes G_{e'} and G_{e''} partition F_l(X).

**(iv.2) Golomb split. PROVED.** Each G_f is a Sidon set. Equivalently, there are no u_1 and r, s > 0 with u_1, u_1+s, u_1+r, u_1+r+s ∈ G_f; the case r = s, a 3-term progression, is included.

*Proof.* Suppose such points exist. Let g be the color of {e',e''} other than f. The points u_1+l, u_1+s+l, u_1+r+l, u_1+r+s+l lie in X, because the four points lie in F_l(X). Consider four L's.
- **L1 = L(u_1, h, h+r).** Its cells are (u_1+h, u_1), of color f; the corner (u_1+h+r, u_1); and (u_1+h+r, u_1+r), of color f because u_1+r ∈ G_f. So the corner is not f. The corner is ψ(u_1, u_1+l+r), so it is not e by (iv.0). Hence it is g.
- **L2 = L(u_1+s, h, h+r).** The same argument with u_1+s, u_1+s+r ∈ G_f gives χ(u_1+s+h+r, u_1+s) = g.
- **L3 = L(u_1, h+r, h+r+s).** Its cells are (u_1+h+r, u_1), of color g by L1; the corner (u_1+h+r+s, u_1); and (u_1+h+r+s, u_1+s), of color g by L2. So the corner is not g. It is ψ(u_1, u_1+l+r+s), so it is not e. Hence it is f.
- **L4 = L(u_1, h, h+r+s).** Its cells are (u_1+h, u_1), of color f; the corner (u_1+h+r+s, u_1), of color f by L3; and (u_1+h+r+s, u_1+r+s), of color f because u_1+r+s ∈ G_f. This L is monochromatic, a contradiction.

All four L's lie in V(D) by Lemma 0(b), since all the required points lie in D. ∎

**Per-fibre cap (PROVED).** Let X ⊆ F_d(D) be any class and S = span F_d(D). Then F_l(X) lies in an interval of S−l+1 integers and is the union of two disjoint Sidon sets. They cannot both contain the left endpoint, so one of them lies in S−l consecutive integers. Hence r_X(l) ≤ Q(S−l) + Q(S−l−1) = v_l ≤ v_1.

**(iv.3) Foreign requests.** Put A = F_l(X) ∩ R_{e'}(h). For u ∈ A:
- u ∈ R_{e'}(h), so u ∉ S_{e'}(h) by (i);
- u ∈ R_e(h) by (iv.1), so u ∉ S_e(h).

Hence u ∈ S_{e''}(h), that is, u ∈ G_{e''}. Likewise F_l(X) ∩ R_{e''}(h) ⊆ G_{e'}. Finally F_l(X) ∩ R_{e'}(h) ∩ R_{e''}(h) ⊆ R_e ∩ R_{e'} ∩ R_{e''} = ∅ by (iii). ∎

### (v) Accounting

**What the R4 chain already uses.**
- The binary-source property of each S_e(d). This is (iv.0). It uses two families of L's: the L's L(a, d, h') whose two arms lie on offset d inside the class (they give ψ ≠ e), and the horizontal translates by d of the L's of V(X), whose two arms lie on a common offset x−y+d > d (they give properness of ψ).
- The Golomb split (iv.2). It uses the L's L(·, h, ·) and L(·, h+r, ·) whose arms lie in the shifted source of a single class, together with (iv.0).
- The consequence χ(u+h,u) ≠ e on F_l(S_e(d)). This is (iv.1) read for a single d.
- Capacity K, staggering and the outer inequality are combinatorics on top of these facts.

**New content.**
- The full request sets R_e(h): the union over all d < h, and the interaction between different d of the same color.
- The containment (ii).
- The at-most-two-of-three cover (iii), with its sharp identity.
- The cross-color facts (iv.3): foreign requests fix Golomb-class membership, and the two foreign request sets are disjoint.
- The inductive form of (i).

### Two further elementary lemmas (PROVED)

**Lemma 1.1 (collision lemma).** If u ∈ F_{h−d}(S_e(d)) ∩ F_{h−d'}(S_e(d')) with d < d' < h, then u+(d'−d) ∉ S_e(d) and u+(h−d') ∉ S_e(d).

*Proof.* L(u, d, d') has arms (u+d, u) of color e and (u+d', u+d'−d), and its corner (u+d', u) has color e because u ∈ S_e(d'). So u+d'−d ∈ S_e(d) would make it monochromatic. The L L(u+h−d', d, d') has horizontal arm (u+h−d'+d, u+h−d'). Its corner (u+h, u+h−d') has color e because u+h−d' ∈ S_e(d'). Its vertical arm (u+h, u+h−d) has color e because u+h−d ∈ S_e(d). So u+h−d' ∈ S_e(d) would make it monochromatic. In both cases the four points lie in D whenever the excluded membership holds. ∎

**Lemma 1.2 (inscribed-pair rule for binary sources).** Let X be finite and let ψ color the pairs p < q of X with two colors. Then ψ is proper iff there are no p < y in X and t with 1 ≤ t < y−p, p+t ∈ X, y−t ∈ X and ψ(p,p+t) = ψ(y−t,y) = ψ(p,y).

*Proof.* This is Lemma 0 for X, with u = p, h = y−p and d = t. ∎

**Corollary 1.3 (separation lemma).** In a binary source with colors {0,1}, no outer pair p < y has inscribed lags t, t' with ψ(p,p+t) = ψ(y−t,y) = 0 and ψ(p,p+t') = ψ(y−t',y) = 1.

*Proof.* The first pair forces ψ(p,y) = 1, and the second forces ψ(p,y) = 0, by Lemma 1.2. ∎

---

## 2. Request-counting inequalities: what holds and what fails

### 2.1 Two conditional statements (PROVED)

**Proposition 2.1 (energy reduction).** Fix h, write F = |F_h(D)|, and suppose that for all three e

  Σ_u m_{e,h}(u)^2 ≤ C_1 N_e(h) + C_2 N_e(h)^2/F, with C_2 < 3/2.

Then min_e N_e(h) ≤ (2C_1/(3−2C_2)) F.

*Proof.* m_{e,h} is supported on R_e(h), so Cauchy-Schwarz gives |R_e| ≥ N_e^2/Σ m^2 ≥ F N_e/(C_1 F + C_2 N_e) when N_e > 0. By (iii), Σ_e |R_e| ≤ 2F, so some e has |R_e| ≤ 2F/3. For that e, 3N_e ≤ 2C_1 F + 2C_2 N_e. ∎

**Proposition 2.2 (forced energy).** In every proper ternary source and every h ≥ 2, some color e has Σ_u m_{e,h}(u)^2 ≥ (3/2) N_e(h)^2/|F_h(D)|.

*Proof.* Take e with |R_e(h)| ≤ (2/3)|F_h(D)|, which exists by (iii). Then N_e^2 ≤ |R_e| Σ m^2 by Cauchy-Schwarz. ∎

(Here F_h(D) ≠ ∅ is assumed.) Proposition 2.1 shows that an energy bound with C_2 < 3/2 holding for all three colors bounds min_e N_e by a constant times F. Theorem 2.6 below refutes such color-symmetric bounds for every constant.

### 2.2 The general digit family (PROVED)

**Data.**
- Fix the base B = 100. Any B ≥ 5 would do; see the coefficient lemma.
- A finite set of **copies** c. Each copy has a shift h_c, a power of B, and a role ρ(c) ∈ P.
- Each copy has a set A_c of **atoms**, powers of B, possibly empty. Put A_c^0 = A_c ∪ {0}.
- All atom exponents are pairwise distinct and distinct from all shift exponents. Two copies may share a shift value.
- **(H) Every atom of copy c is smaller than h_c.** The simplest way to arrange this is to put all atom exponents below all shift exponents.
- All exponents are < M. Put T_c = τ_c B^M, where the τ_c are distinct members of a Sidon set of nonnegative integers.
- Left/up colors: any f_c(a,b) ∈ P∖{ρ(c)} for a < b in A_c^0.

**Set.** E_c = A_c^0 ∪ (h_c − A_c^0) and D = ⋃_c (T_c + E_c).

*Consequences of (H).*
- Two elements a, a' of A_c^0 are distinct powers of B below h_c, or 0. So a + a' ≤ 2h_c/B < h_c.
- Hence the "small" elements {a} are all below the "large" elements {h_c − a}, so E_c ⊂ [0, h_c].
- Every element of E_c is written uniquely as α h_c + σ a with a ∈ A_c^0, α ∈ {0,1}, and σ = +1 if α = 0, σ = −1 if α = 1.
- For T_c < T_{c'} we have T_{c'} − T_c ≥ B^M ≥ B·max h > 2 max h. So the copies occupy disjoint intervals [T_c, T_c+h_c], in the order of T.

**Hypothesis (H) is necessary (explicit failure).** Take one copy, T = 0, h = B = 100, A = {B^2}. Then D = {−9900, 0, 100, 10000}. Under the table below, the L with cells (0,−9900), (10000,−9900), (10000,100) consists of three "other" cells, all colored 0. It is monochromatic. Everything below assumes (H).

**Coefficient lemma.** Suppose Σ_{m≤M} c_m B^m = 0 with |c_m| ≤ 4 for m < M and c_M an arbitrary integer. Then every c_m = 0.

*Proof.* Let m < M be least with c_m ≠ 0. Every other term is a multiple of B^{m+1}, so the sum is ≡ c_m B^m ≢ 0 mod B^{m+1}, since 0 < |c_m| < B. Hence c_m = 0 for all m < M, and then c_M = 0. ∎

For four points of D, expand p_0 + p_3 − p_1 − p_2. Each point is τ B^M + α h + σ a and carries at most one atom. So every atom power and every shift power below B^M gets a coefficient of absolute value at most 4. The B^M-coefficient is τ_{c0} + τ_{c3} − τ_{c1} − τ_{c2}. Consequences:
- by the Sidon property, {c0,c3} = {c1,c2} as multisets;
- for each atom, the signed contributions cancel;
- for each shift value, the h-coefficients cancel.

**Coloring.** Cells are written in absolute coordinates.

| cell | color |
|---|---|
| corner C_c(a) = (T_c+h_c−a, T_c+a), a ∈ A_c^0 | ρ(c) |
| left (T_c+b, T_c+a) and up (T_c+h_c−a, T_c+h_c−b), a < b in A_c^0 | f_c(a,b) |
| mirror M_c(x,y) = (T_c+h_c−x, T_c+y), x ≠ y in A_c^0 | ρ(c)+1 |
| cross corner (T_{c'}+h, T_c), T_c < T_{c'}, h_c = h_{c'} = h | ρ(c)+1 |
| cross low cell (T_{c'}, T_c), T_c < T_{c'} | ρ(c) |
| every other cell of V(D) | 0 |

**The coloring is well defined.**
- A left cell has small column and small row.
- An up cell has large column and large row.
- Corner and mirror cells have large column and small row, with equal atoms for a corner and different atoms for a mirror.
- Cross cells have row and column in different copies.
- A cross corner never equals a cross low cell: that would need T_{c''} − T_{c'} = h, but T-differences are nonzero multiples of B^M > h.

**Lemma 2.3 (complete list of L's).** Every L of V(D) has four points p_0 < p_3 and an ordered middle pair (x,y), all in D, with x + y = p_0 + p_3 and p_0 < x, y < p_3. Its cells are (x, p_0), the corner (p_3, p_0) and (p_3, y). Both orders of the middle pair are included, so d = x − p_0 > h/2 and x = y are covered. The L's are exactly the following.
- **(S1)** For each copy c and a < b in A_c^0: (T_c+b, T_c+a) [left], corner C_c(a), (T_c+h_c−a, T_c+h_c−b) [up].
- **(S2)** For each copy c and a < b in A_c^0: M_c(b,a), corner C_c(a), M_c(a,b).
- **(X1)** For copies T_{c0} < T_{c3} with equal shift h: C_{c0}(0) = (T_{c0}+h, T_{c0}), corner (T_{c3}+h, T_{c0}), C_{c3}(0).
- **(X2)** For the same pairs: (T_{c3}, T_{c0}) [cross low cell], corner (T_{c3}+h, T_{c0}), (T_{c3}+h, T_{c0}+h).

*Proof.*
- **Sidon step.** Either all four points lie in one copy, or p_0 lies in c0 and p_3 in c3 with T_{c0} < T_{c3}, and the middle points are one in each of these copies.
- **Same copy c.** Write x_0 < x_3 for the offsets of p_0, p_3, and y, z for the middle offsets, with y + z = x_0 + x_3 and both strictly between. The h_c-coefficient gives α_0 + α_3 = α_y + α_z.
  - **Sum 0.** A sum of two members of {0} ∪ {atoms} determines the multiset of summands. So {y, z} = {x_0, x_3}, which contradicts strict betweenness. This includes y = z.
  - **Sum 2.** The reflection x ↦ h_c − x reduces this to sum 0.
  - **Sum 1.** x_0 = a_0 is small and x_3 = h_c − a_3 is large. One middle point is small, y = a_1, and the other large, z = h_c − a_2; in particular y ≠ z. The atom identity is e_{a_0} + e_{a_2} = e_{a_1} + e_{a_3} (with e_0 = 0), and a_1 > a_0. So a_0 = a_3 =: a and a_1 = a_2 =: b > a.
    - The order "small middle point first" gives (S1).
    - The other order gives (S2).
    - Conversely, each a < b gives these L's, since a < b < h_c − b < h_c − a.
- **Cross copies.** Write the middle points as y ∈ E_{c0} and z ∈ E_{c3} (offsets). The atom sets of the two copies are disjoint, so a_0 = a_y and a_3 = a_z.
  - If a_0 ≠ 0, the signs agree, so α_0 = α_y and y = x_0, which is impossible. Hence a_0 = a_y = 0.
  - Symmetrically a_3 = a_z = 0.
  - Then x_0 < y in {0, h_{c0}} gives x_0 = 0, y = h_{c0}, and z < x_3 in {0, h_{c3}} gives z = 0, x_3 = h_{c3}.
  - If h_{c0} ≠ h_{c3}, the h_{c0}-coefficient is −1, a contradiction. So the shifts are equal, and the two orders give (X1) and (X2). ∎

**Theorem 2.4 (properness). PROVED.** χ is proper for every choice of ρ and of the f_c.
- (S1): the corner has color ρ(c), the left cell f_c(a,b) ≠ ρ(c).
- (S2): the corner has color ρ(c), the horizontal end ρ(c)+1.
- (X1): the corner is a cross corner, of color ρ(c0)+1; the horizontal end C_{c0}(0) has color ρ(c0).
- (X2): the corner has color ρ(c0)+1; the horizontal end, a cross low cell, has color ρ(c0). ∎

**Lemma 2.5 (fibres and requests at a shift value h).** F_h(D) = {T_c : h_c = h}. The L's with corner (T_c + h, T_c) are exactly (S1) and (S2) with a = 0, one of each per b ∈ A_c. Hence

  m_{e,h}(T_c) = #{b ∈ A_c : f_c(0,b) = e} + |A_c|·[e = ρ(c)+1], and m_{ρ(c),h}(T_c) = 0.

*Proof.*
- Cross-copy differences exceed max h, so both points of a pair at distance h lie in one copy c.
  - If h_c < h, this is impossible, since E_c ⊂ [0, h_c].
  - If h_c = h, then E_c ⊂ [0,h] forces the pair (0, h).
  - If h_c > h, the difference (α−α')h_c + σa − σ'a' = h has coefficient −1 on the power h, which is a contradiction.
- (S)-type L's have span h_c − 2a. If a ≠ 0, the identity h_c − 2a = h puts coefficient −2 on a, which is impossible. So a = 0 and h_c = h.
- (X)-type L's have span greater than B^M − max h > h.
- By (★) and the table: (S1)(0,b) has both arms of color f_c(0,b), and (S2)(0,b) has both arms of color ρ(c)+1. ∎

**Theorem 2.6 (refutation of request-counting inequalities over arbitrary sources). PROVED.**

For all λ > 0, C > 0, ε > 0 and m ≥ 1 there is a proper ternary source (D,χ) and a set W of m shifts such that, for every h ∈ W and every e ∈ P:
- (a) N_e(h) ≥ λ |F_h(D)|;
- (b) Σ_u m_{e,h}(u)^2 > C (N_e(h) + N_e(h)^2/|F_h(D)|);
- (c) |R_e(h)| ≤ ε |F_h(D)|.

Consequently, every weighted average over W of UW(λ), of the U1-type energy bound with any constant C, or of a union-growth bound |R_e| ≥ f(N_e/|F_h|)|F_h| with liminf f > 0, fails.

*Construction.* Fix k' ≥ 1, r ≥ 1 and s ≥ 0. Choose distinct shift powers h_1, …, h_m, with all atom exponents below all shift exponents, so that (H) holds. For each i take:
- 3r active copies with shift h_i, |A_c| = k', roles 0, 1, 2 each used r times, and f_c ≡ ρ(c)+1;
- r·s padding copies with shift h_i, A_c = ∅ and arbitrary roles. The general table (cross corner ρ(c)+1) is used.

All copies use distinct τ from one Sidon set.

*Proof.* The source is proper by Theorem 2.4. By Lemma 2.5, at h = h_i:
- |F_h| = r(3+s);
- each active copy of role e−1 has m_{e,h}(T_c) = 2k', and every other start has m_{e,h} = 0;
- so N_e(h) = 2k'r, |R_e(h)| = r and Σ m^2 = 4k'^2 r.

Then:
- N_e/|F_h| = 2k'/(3+s);
- the energy ratio Σ m^2/(N + N^2/|F_h|) = 2k'(3+s)/(3+s+2k');
- |R_e|/|F_h| = 1/(3+s).

Take s = ⌈sqrt(k')⌉ and k' large. All three ratios then go the required way: the first two are of order sqrt(k') and the third tends to 0. ∎

*Special cases.*
- Three copies, one common shift, r = 1, s = 0 ("cyclic repaired family"): |F_h| = 3, N_e(h) = 2k for every e, |R_e(h)| = 1.
- s = 0: min_e N_e ≥ (2k'/3)|F_h| on every h ∈ W.

**Embedding (PROVED, conditional only on the bound stated in the problem).** The problem states that the outer inequality excludes n = 21,987,409. Properness is inherited by sub-squares, so a properly four-colored square has side at most 21,987,408, and every diagonal class has span at most 21,987,407.
- Every member of the families of Theorem 2.6 (k' ≥ 1) has at least three copies and at least four exponents in use (three atoms and one shift), so M ≥ 4 and its span is at least (τ_max − τ_min) B^M ≥ B^4 = 10^8 > 21,987,407. None of them is a diagonal class.
- For the cyclic repaired family with k = 2, M ≥ 7 and the span is at least 10^14.
- This applies to the families used. Trivial members of the general family, such as D = {0,1}, do embed.
- With B = 9 instead of 100, span alone does not exclude the smallest member (for k = 2 its span is 14,880,348), and its embeddability is not settled.

### 2.3 The lifted digit family: fibres and classes of size span^{1/2−o(1)} (PROVED)

**Base.** Take the digit family with m' copies, each with k atoms, pairwise distinct shift values h_c, and (H). By Lemma 2.3, with distinct shifts the only L's of D_base are (S1) and (S2). Base binary coloring: χ_B(q,p) = 0 if (q,p) is a corner cell C_c(a), and χ_B(q,p) = 1 for every other pair p < q of D_base.

No arm cell of (S1) or (S2) is a corner cell:
- a left cell has small column;
- an up cell has large row;
- a mirror cell has different atoms.

So every base L has corner 0 and arms 1, and χ_B is proper.

**Lemma 2.7 (D_base has no 3-term progression).** Suppose b_0 + b_3 = 2b_m with b_0 < b_m < b_3 in D_base.
- The B^M-coefficient gives τ_0 + τ_3 = 2τ_m, so all three points lie in one copy, by the Sidon property with repeated summands.
- If the atom a_m of b_m is nonzero, its coefficient 2σ_m must come from b_0 and b_3. Both then carry a_m with sign σ_m, so α_0 = α_3 and b_0 = b_3, a contradiction.
- If a_m = 0, then b_m ∈ {0, h_c}. The atoms of b_0 and b_3 cancel, so either both atoms are 0 or they are equal with opposite signs. In both cases α_0 + α_3 = 1, but the h_c-coefficient requires α_0 + α_3 = 2α_m. Contradiction. ∎

**Fine block.**
- Let p be an odd prime and G_0 = {2pi + (i^2 mod p) : 0 ≤ i < p} ⊂ [0, 2p^2).
- **G_0 is Sidon (Erdős–Turán; proof).** Write x = 2pi + q_i with 0 ≤ q_i < p. Suppose x_a + x_b = x_c + x_d. Reducing mod 2p gives q_a + q_b = q_c + q_d, since both sides are < 2p; then i_a + i_b = i_c + i_d. Mod p the sums and the sums of squares agree, so, p being odd, the products agree too. Then {i_a, i_b} and {i_c, i_d} are the root multisets of one quadratic over F_p, with elements in [0,p), so they are equal.
- Take G ⊆ G_0 with |G| = 3r and a labelling s : G → P taking each value exactly r times. Put L = 4p^2 + 1 > 2 max G.

**Set.** D = {L b + g : b ∈ D_base, g ∈ G}. Write a point as (b,g); the order is lexicographic, since g < L.

**Coloring of a cell (q,p) with q > p.** Write q = (b_q, g_q), p = (b_p, g_p). Put t(g,g') = s_g + 2 if s_g = s_{g'}, and t(g,g') = 0 otherwise.
- (diag) b_q > b_p and g_q = g_p = g: χ_B(b_q, b_p) + s_g.
- (off) b_q > b_p and g_q ≠ g_p: χ_B(b_q, b_p) + t(g_q, g_p).
- (same) b_q = b_p and g_q > g_p: ℓ(g_q, g_p) := t(g_q, g_p) + 2.

**Lemma 2.8 (all L's).** Take p_0 < x, y < p_3 with x + y = p_0 + p_3.
- The relation reads L(b_0 + b_3 − b_x − b_y) = g_x + g_y − g_0 − g_3. The right side has absolute value < L, so both sides vanish.
- Since G is Sidon, {g_x, g_y} = {g_0, g_3}.

The cases are as follows.
- **(A) Trivial base relation, {b_x, b_y} = {b_0, b_3}.** Here b_0 < b_3, since otherwise {x,y} = {p_0,p_3}.
  - **R1:** x = (b_0, g_3), y = (b_3, g_0), with g_3 > g_0.
  - **R2:** x = (b_3, g_0), y = (b_0, g_3), with g_3 > g_0.
- **(B) Nontrivial base relation.** The order gives b_0 ≤ b_x, b_y ≤ b_3. Equality b_x = b_0 would force b_y = b_3, which is the trivial relation. b_x = b_y is excluded by Lemma 2.7. So (b_0, b_x, b_y, b_3) is a base L, (S1) or (S2). Then:
  - **II:** g_x = g_y = g_0 = g_3;
  - **III:** g_x = g_0, g_y = g_3 ≠ g_0;
  - **I:** g_x = g_3, g_y = g_0 ≠ g_3.

There are no other L's. ∎

**Theorem 2.9 (properness). PROVED.** Let s = s_{g_0}, s' = s_{g_3} and t = t(g_3, g_0). For each type the cells are listed as (horizontal end, corner, vertical end).

| type | colors | not monochromatic because |
|---|---|---|
| II | χ_B + s_g on a base L | it is a shift of the proper χ_B |
| I | χ_B + t on a base L (all three cells off with the same pair (g_3,g_0)) | it is a shift of the proper χ_B |
| III | 1+s, t, 1+s' (base corner 0, base arms 1) | monochromatic would need s = s' and t = s+1, but then t = s+2 |
| R2 | κ+s, κ+t, κ+s', with κ = χ_B(b_3,b_0) | monochromatic would need s = s' = t, but then t = s+2 |
| R1 | ℓ, κ+t, ℓ | κ+t ∈ {t, t+1} and ℓ = t+2 |

∎

**Theorem 2.10 (counts). PROVED.** Put H_c = L h_c and W = {H_c}, so |W| = m'. Then for every e and every H ∈ W:
- |F_H(D)| = 3r and min_e N_e(H)/|F_H| = 2k/3;
- N_e(H) = 2kr, |R_e(H)| = r and Σ_e |R_e(H)| = |F_H|;
- Σ_u m_{e,H}(u)^2 = 4k^2 r.

Moreover, every request-producing class S_e(Lb), b ∈ A_c, contains the r starts (T_c, g) with s_g = e−1, and r_{S_e(Lb)}(L(h_c − b)) ≥ r.

*Proof.*
- **The fibre.** (b,g) + H ∈ D forces g unchanged and b + h_c ∈ D_base. By Lemma 2.5, F_H(D) = {(T_c, g) : g ∈ G}.
- **L's of span H.** Types I, III, R1 and R2 have g_3 ≠ g_0, so their span is ≡ g_3 − g_0 ≢ 0 mod L. Type-II lifts of base L's of span h_c are, by Lemma 2.5 and the distinct shifts, the lifts of (S1)(0,b) and (S2)(0,b).
- **Requests.** Each such L has corner color 0 + s_g and both arms of color 1 + s_g. So m_{e,H}((T_c,g)) = 2k·[s_g = e−1].
- **Fibre multiplicity.** The cell ((T_c+b, g), (T_c, g)) is a diag lift of a left cell, so its color is 1 + s_g = e. Hence (T_c, g) ∈ S_e(Lb). The cell ((T_c+h_c, g), (T_c+h_c−b, g)) is a diag lift of an up cell, also of color e, so (T_c + h_c − b, g) ∈ S_e(Lb). ∎

**Scale.**
- span D < L·(span D_base + 1) ≤ (4p^2+1)·C(k,m'), with C depending only on k and m'.
- Take r = ⌊p/3⌋ and p → ∞ with k and m' fixed.

So the request-producing classes, and their fibres at the request-producing lags, have size ≥ r ≥ span^{1/2−o(1)}. The ratio 2k/3 is unbounded, with p chosen after k.

**Corollary 2.11. PROVED.** Suppose one adds either of the following hypotheses at the request-producing classes:
- fibre multiplicities ≥ m, for any m (even growing like span^{1/2−o(1)});
- class sizes ≥ c·span^α, for any c > 0 and α < 1/2.

Then the following inequalities are still false:
- UW(λ), min_e N_e(H) ≤ λ|F_H|, for every λ;
- the U1-type energy bound Σ_u m_{e,H}(u)^2 ≤ C(N_e + N_e^2/|F_H|), for every C < 3;
- union growth |R_e(H)| ≥ f(N_e/|F_H|)|F_H|, for every f with liminf_{x→∞} f(x) > 1/3.

*Proof.* By Theorem 2.10, N_e/|F_H| = 2k/3. The energy ratio is 4k^2 r/(2kr + 4k^2 r/3) = 6k/(3+2k), which tends to 3 from below. Also |R_e(H)|/|F_H| = 1/3. Take k large, then p large. ∎

**Limitation (stated so it is not overread).** The lifted family does not refute an energy bound with C ≥ 3, nor a union-growth bound with f ≤ 1/3. The reason is that it has no padding: every start of F_H requests exactly one color. Padding copies of the kind used in Theorem 2.6 cannot be added directly. Two base copies with equal shifts create an (X2)-type base L. Its three cells (T_{c3}, T_{c0}), (T_{c3}+h, T_{c0}) and (T_{c3}+h, T_{c0}+h) are all cross cells, none of them a corner cell, so all three have color 1 under χ_B: the L is monochromatic. Whether a lifted family with padding exists is not settled here. Only Theorem 2.6, whose classes are far below sqrt(span), refutes these two bounds for every constant.

Instances with ratio ≥ 240 are not diagonal classes of a four-colored square: the ratio 2k/3 ≥ 240 needs k ≥ 360, each shift then exceeds 360 distinct atom powers of B, so the span is at least B^{360}. Smaller lifted members are not excluded by span, and their embeddability is not settled.

**What survives Sections 2.2-2.3 (OPEN).**
- Class sizes c·sqrt(span) with c near the regime value. The regime has |S| ≈ 98 sqrt(span); here the classes are a tiny constant times sqrt(span), far below the binary cap.
- Fibres near v_l on many lags.
- Interval averaging over consecutive shifts h = 1, …, t−1 with the weights a_h. W is sparse here.
- Positive density of D.

---

## 3. Part (D-c): the forced-color alternative

**Proposition 3.1 (forced sets are Golomb; PROVED).** Let X = S_e(d), h = d+l and S = span F_d(D). Put A = F_l(X) ∩ R_{e'}(h) and B = F_l(X) ∩ R_{e''}(h).
- A ⊆ G_{e''} and B ⊆ G_{e'}, so A and B are Sidon sets.
- |A|, |B| ≤ Q(S−l), and A ∩ B = ∅.

*Proof.* This is (iv.2) together with (iv.3). Subsets of Sidon sets are Sidon, and F_l(X) lies in S−l+1 consecutive integers. ∎

This bound is never stronger than the per-fibre cap r_X(l) ≤ v_l.

**Abstract obstruction (PROVED).** The constraints that (ii)-(iv) place on one fibre are:
- A ⊆ G_{e''} and B ⊆ G_{e'};
- A ∩ B = ∅;
- G_{e'} and G_{e''} are Sidon.

They are all satisfied by A = G_{e''} and B = G_{e'}, with both Golomb classes of maximum size. So (i)-(iv) alone cannot force an imbalance. Any imbalance must come from the L's that generate A and B.

**Theorem 3.2 (full foreign coverage with balanced Golomb classes). PROVED.** For every k ≥ 1 there is a proper ternary source, with colors e = 0, e' = 1, e'' = 2, a class X = S_0(d) and a lag l with the following properties:
- |F_l(X)| = 2k;
- |G_2| = |G_1| = k;
- A = F_l(X) ∩ R_1(h) = G_2 and B = F_l(X) ∩ R_2(h) = G_1.

Hence the statement "(D-c+): |A| ≥ α|G_{e''}| forces |G_{e'}| ≤ (1−β)|G_{e''}|" fails for every α ≤ 1 and β > 0 without near-extremality hypotheses.

*Construction.* Fix k and B = 100. For i = 1..2k put d'_i = B^i, d = B^{2k+1}, l = B^{2k+2}, h = d+l and u_i = B^{2k+2+i}. Let w_i = h − d'_i and Δ_i = {0, d'_i, d, l, w_i, h}, so 0 < d'_i < d < l < w_i < h. Put D = ⋃_i (u_i + Δ_i). The blocks are disjoint and ordered by i. Let c_i = 2 for i ≤ k and c_i = 1 for i > k, and c̄_i = 3 − c_i.

*Same-block cells.* Write [a,b]_i for the cell (u_i+a, u_i+b).

| cell | color |
|---|---|
| [d,0], [h,l] | 0 |
| [h,0] | c_i |
| [d'_i,0], [h,w_i] | c̄_i |
| [l,0], [w_i,0], [w_i,d'_i] | 0 |
| [d,d'_i], [l,d'_i] | 1 |
| every other same-block cell | 0 |

*Cross cells* (u_j+α, u_i+β) with i < j. Put Δ^0 = {0, d, l, h}. If α ∉ Δ^0 or β ∉ Δ^0, the color is 0. Otherwise the color is κ_{ij}(α,β):
- κ(0,·) = 0, κ(d,·) = 1, κ(l,·) = 2;
- κ(h,d) = 1, κ(h,l) = 2, κ(h,h) = 0;
- κ(h,0) = s_{ij}, where s_{ij} = c̄ if c_i = c_j = c, and s_{ij} = 1 if c_i ≠ c_j.

*All L's.* Each point is a single u-digit plus an offset whose digits have coefficients in {−1,0,1}. So in p_0 + p_3 − x − y every power of B has a coefficient of absolute value ≤ 4, and by the coefficient lemma every coefficient vanishes.
- **Same block i.** In the basis (d, l, d'_i) the offsets are 0 = (0,0,0), d'_i = (0,0,1), d = (1,0,0), l = (0,1,0), w_i = (1,1,−1), h = (1,1,0). Among all 21 pair sums, doubles included, the only coincidence is 0+h = d+l = d'_i+w_i. Using the order of the offsets, the same-block L's are exactly six:
  - [d,0], [h,0], [h,l]: colors 0, c_i, 0;
  - [l,0], [h,0], [h,d]: colors 0, c_i, 0;
  - [d'_i,0], [h,0], [h,w_i]: colors c̄_i, c_i, c̄_i;
  - [w_i,0], [h,0], [h,d'_i]: colors 0, c_i, 0;
  - [d,d'_i], [w_i,d'_i], [w_i,l]: colors 1, 0, 0;
  - [l,d'_i], [w_i,d'_i], [w_i,d]: colors 1, 0, 0.

  None is monochromatic, since c_i ≠ 0 and c̄_i ≠ c_i.
- **Cross blocks.** Let p_0 = u_i+δ_0 and p_3 = u_j+δ_3 with i < j. One middle point is u_i+δ_y with δ_y > δ_0, the other u_j+δ_z with δ_z < δ_3. The digit d'_i cancels on its own, so δ_0 and δ_y have the same d'_i-coefficient. Being distinct, both lie in Δ^0; likewise δ_z, δ_3 ∈ Δ^0. Also δ_y − δ_0 = δ_3 − δ_z =: g > 0.
  - **Order 1** (the horizontal middle point lies in block i). The cells are (u_i+δ_y, u_i+δ_0), the corner (u_j+δ_3, u_i+δ_0), and (u_j+δ_3, u_j+δ_z). On Δ^0 the only nonzero same-block cell is [h,0].
    - If g ≠ h, both arms are 0. The corner has δ_3 ∈ {d,l,h} and δ_0 ∈ {0,d,l}, and every such κ value is nonzero.
    - If g = h, the arms are c_i and c_j and the corner is s_{ij}. If c_i = c_j = c, then s_{ij} = c̄ ≠ c; otherwise the arms differ.
  - **Order 2** (the horizontal middle point lies in block j). All three cells are cross cells: (u_j+δ_z, u_i+δ_0), the corner (u_j+δ_3, u_i+δ_0), and (u_j+δ_3, u_i+δ_y).
    - If δ_z = 0, the horizontal end is 0 and the corner is nonzero, since δ_3 > 0 and δ_0 ≠ h.
    - (δ_z, δ_3) = (d,l), so (δ_0, δ_y) = (d,l): the horizontal end is 1 and the corner 2.
    - (d,h) with (δ_0, δ_y) = (0,l): the cells are 1, s, 2.
    - (d,h) with (d,h): the cells are 1, 1, 0.
    - (l,h) with (0,d): the cells are 2, s, 1.
    - (l,h) with (l,h): the cells are 2, 2, 0.

    None is monochromatic.

So χ is proper.

*The fibre.*
- The points x with x+d ∈ D are the block offsets 0 and l, and both completion cells [d,0], [h,l] are 0. So X = S_0(d) = F_d(D) = {u_i, u_i+l} and F_l(X) = {u_i}.
- The Golomb cell of u_i is [h,0] = c_i, so G_2 = {u_1..u_k} and G_1 = {u_{k+1}..u_{2k}}.
- The cells [d'_i,0] and [h,w_i] both have color c̄_i, so u_i ∈ F_{h−d'_i}(S_{c̄_i}(d'_i)) ⊆ R_{c̄_i}(h). This gives A = G_2 and B = G_1. ∎

**Proposition 3.3 (under near-extremality, imbalance is a fibre deficit; PROVED).** For every class X ⊆ F_d(D) and every l, both Golomb classes of F_l(X) have size ≥ r_X(l) − Q(S−l) ≥ Q(S−l−1) − (v_l − r_X(l)).

So if r_X(l) ≥ (1−ε) v_l, the imbalance is at most Q(S−l) − Q(S−l−1) + ε v_l. Conversely, a forced imbalance lowers r_X(l) below v_l by the same amount, up to the additive term Q(S−l) − Q(S−l−1) ≤ 1.

*Proof.* Each Golomb class is ≤ Q(S−l), and the two add up to r_X(l). ∎

**Consumer quantity.** A proportional imbalance on a positive share of lags would lower the per-fibre caps v_l. Through the rank inequality this lowers the single-class capacity K, and hence U_d. Section 4 shows that, at the level of sizes, this is equivalent to the open statement FD.

---

## 4. Exact reduction of the per-shift (D-a) clause (PROVED)

Fix a proper ternary source, a shift d, Y = F_d(D), S = span Y, X_e = S_e(d) and s_e = |X_e|, so Σ_e s_e = |Y|. By (iv.0) each X_e is a binary source of span ≤ S, and by the per-fibre cap r_{X_e}(l) ≤ v_l ≤ v_1.

**Lemma 4.1 (bounds on Q).**
- (Q-up) Q(m) ≤ sqrt(2m) + 1. A Sidon set of size q in m+1 consecutive integers has q(q−1)/2 distinct positive differences, all ≤ m.
- (Q-low) Q(m) > sqrt(m/8) for m ≥ 32. Put x = sqrt(m/8) ≥ 2 and n = ⌊x⌋ ≥ 2. By Bertrand's postulate (CITED: for every integer n ≥ 2 there is a prime p with n < p < 2n) there is a prime p with x < n+1 ≤ p < 2n ≤ 2x; p ≥ 3 is odd. The Erdős–Turán set G_0 of Section 2.3 is Sidon, has p elements, and its largest element is at most 2p(p−1) + (p−1) = 2p^2 − p − 1 < 2p^2 ≤ 8x^2 = m. So G_0 ⊂ [0, m] and Q(m) ≥ p > x.
- (Q-step) Q(m−1) ≥ Q(m) − 1: delete the largest element.
- Consequently, for S ≥ 34, v_1 ≥ 2Q(S−2) > sqrt((S−2)/2) ≥ sqrt(S)/2, and c(S) = sqrt(v_1 S) ≥ S^{3/4}/sqrt 2.

**Lemma 4.2 (sliding-window second moment).** Let X ⊂ Z, |X| = s, span X ≤ S, λ ≥ 0, Λ = λ+1 and N = S+Λ. Then

  sΛ + 2 Σ_{l=1}^{λ} (Λ−l) r_X(l) ≥ s^2 Λ^2 / N.

*Proof.* Let f(x) = |X ∩ [x, x+λ]|. Then Σ_x f(x) = sΛ, and f vanishes outside a set of at most span X + Λ ≤ N integers. Also Σ_x f(x)^2 = Σ_{a,b∈X} (Λ − |a−b|)_+ = sΛ + 2 Σ_{l=1}^{λ} (Λ−l) r_X(l). Cauchy-Schwarz over the support finishes the proof. ∎

**Corollary 4.3 (Fejér single-class cap).** Every binary source of span ≤ S whose fibres satisfy r(l) ≤ v_1 has size at most

  K_F(S) := min_{1≤λ≤S} [ N/Λ + sqrt(v_1 N) ],

and K_F(S) ≥ c(S). In particular every class satisfies s_e ≤ K_F(S).

*Proof.* 2Σ(Λ−l) r(l) ≤ v_1 λΛ ≤ v_1 Λ^2. So Lemma 4.2 gives s^2 ≤ (N/Λ)s + v_1 N, and s^2 − bs − c ≤ 0 implies s ≤ b + sqrt(c). The lower bound holds because N > S. ∎

*Sharper form (PROVED, same proof).* Keeping the factor λ/Λ gives s^2 ≤ b s + c' with b = N/Λ and c' = v_1 λN/Λ. So s ≤ K_F^♯(S) := min_λ (b + sqrt(b^2 + 4c'))/2 ≤ K_F(S). Nothing below needs this form. It matters only for the numerics of Section 5.

The per-fibre cap applies to every binary source X of span ≤ S, with the Golomb split of its own fibres. In this document it is proved for the classes S_e(d); for an abstract binary source the Golomb split follows from Lemma 1.2 by the argument of (iv.2) with d = 0.

**Lemma 4.4 (K_F is asymptotically c).** For S ≥ 34, K_F(S) ≤ (1 + ξ(S)) c(S) with ξ(S) = 3.83 S^{−3/8}.

*Proof.*
- Take Λ = ⌈S^{5/8}⌉, so 2 ≤ Λ ≤ 2S^{5/8} ≤ S.
- N/Λ ≤ S^{3/8} + 1.
- sqrt(v_1 N) = c·sqrt(1+Λ/S) ≤ c(1 + Λ/(2S)) ≤ c(1 + S^{−3/8}).
- (S^{3/8}+1)/c ≤ sqrt 2 (S^{3/8}+1) S^{−3/4} ≤ 2 sqrt 2 S^{−3/8}, and 1 + 2 sqrt 2 < 3.83. ∎

(Numerical evaluation, HEURISTIC inputs S = 2.2·10^7 and v_1 = 9.4·10^3, minimum taken over integer λ by computer: c ≈ 4.548·10^5. K_F ≈ 4.557·10^5, i.e. 0.21% above c, at λ ≈ 46,000. K_F^♯ ≈ 4.554·10^5, i.e. 0.15% above c.)

**Definition (FD(η, S_0)).** For every proper ternary source and every d with S = span F_d(D) ≥ S_0,

  |F_d(D)| ≤ 3(1−η) c(S).

**Theorem 4.5 (equivalence of FD with the per-shift (D-a) clause against the Fejér caps). PROVED.**
- (a) FD(η, S_0) implies Σ_e |S_e(d)| ≤ (1−η)·3K_F(S) for all S ≥ S_0. That is the (D-a) inequality per shift, with δ = η, against the sum of the three separate certified single-class caps K_F(S).
- (b) Conversely, if Σ_e |S_e(d)| ≤ (1−δ)·3K_F(S) for all S ≥ S_0 ≥ 34, then FD(η, S_0) holds with η = δ − (1−δ)ξ(S_0).

*Proof.* (a) holds by Corollary 4.3, since c ≤ K_F. (b) holds by Lemma 4.4, since (1−δ)(1+ξ) = 1 − (δ − (1−δ)ξ), and ξ is decreasing in S. ∎

So, against certified single-class caps of Fejér type, Part D (D-a) per shift is exactly FD, up to O(S^{−3/8}).

**Proposition 4.6 (single-class deficit implies FD; structure of any violator). PROVED.**
- (a) Suppose every binary source of span S' ≥ S_1 has size ≤ (1−η') c(S') (statement **SCD(η', S_1)**). Then FD(η, S_0) holds for every η < η', with S_0 = max(34, (sqrt 2·S_1/(η'−η))^{4/3}).
- (b) If |F_d(D)| ≥ 3(1−η) c(S) with S ≥ 34, then every class satisfies s_e ≥ (1 − 3η − 2ξ(S)) c(S).
- (c) Hence a family refuting FD for every η > 0 contains, at one shift and inside one interval of S+1 integers, three pairwise disjoint binary sources of size (1−o(1)) c(S). Here c(S) ≥ S^{3/4}/sqrt 2 by Lemma 4.1, and c(S) = (1+o(1)) sqrt 2·S^{3/4} if Q(m) = (1+o(1)) sqrt m (CITED: Erdős–Turán upper bound and Singer sets). In particular such a family refutes SCD(η') for every η' > 0.

*Proof.*
- (a) A class of span S_e ≥ S_1 has size ≤ (1−η') c(S_e) ≤ (1−η') c(S), since c is nondecreasing, Q being nondecreasing. A class of span < S_1 has size ≤ S_1. So |F_d(D)| ≤ 3(1−η') c(S) + 3S_1, and 3S_1 ≤ 3(η'−η) c(S) once S^{3/4}/sqrt 2 ≥ S_1/(η'−η).
- (b) s_e ≥ |F_d(D)| − 2K_F(S) ≥ (3(1−η) − 2(1+ξ)) c.
- (c) follows from (b). ∎

The converse of (a), whether FD implies SCD, is OPEN. It would need three interleaved near-cap binary sources to be realised as the classes of one shift. Doubling, D = Y ∪ (Y+d) with d > 2 span Y, gives F_d(D) = Y, but it turns the task into a proper 3-coloring of the full grid Y × Y with prescribed diagonal, which is the original square problem on Y.

**Proposition 4.7 (saturation of a near-cap class; explicit). PROVED.** Let X be a binary source of span ≤ S (S ≥ 34) with fibres r(l) ≤ v_1 and s = |X| ≥ (1−θ) c(S), 0 ≤ θ < 1. Let 1 ≤ λ, Λ = λ+1 ≤ S, and

  D̄(λ) := 2 Σ_{l=1}^{λ} (Λ−l)(v_1 − r(l)) / (v_1 λΛ) ∈ [0,1].

Then:
- (a) D̄(λ) ≤ 2θ + Λ/S + s/(v_1 λ), and s/v_1 ≤ (1+ξ(S)) sqrt 2·S^{1/4};
- (b) for β > 0, the (Λ−l)-weighted fraction of lags l ≤ λ with r(l) < (1−β) v_1 is at most D̄(λ)/β;
- (c) at every lag with r(l) ≥ (1−β) v_1, both Golomb classes have size ≥ Q(S−2) − β v_1, so both are near-maximal Sidon sets.

*Proof.*
- (a) If θ ≥ 1/2 the bound is trivial, since D̄ ≤ 1 ≤ 2θ. Let θ < 1/2. Since 2Σ_{l≤λ}(Λ−l) = λΛ, we have 2Σ(Λ−l)(v_1 − r) = v_1λΛ − 2Σ(Λ−l)r, and Lemma 4.2 gives 2Σ(Λ−l)(v_1 − r) ≤ v_1 λΛ + sΛ − s^2Λ^2/N. Divide by v_1 λΛ. Use Λ ≥ λ, s^2 ≥ (1−θ)^2 v_1 S ≥ (1−2θ) v_1 S > 0 and S/N ≥ 1 − Λ/S, so that s^2Λ/(v_1 λN) ≥ (1−2θ)(1−Λ/S) ≥ 1 − 2θ − Λ/S. The bound on s/v_1 follows from s ≤ K_F ≤ (1+ξ)c and c/v_1 = sqrt(S/v_1) ≤ sqrt 2·S^{1/4}.
- (b) is Markov's inequality for the weights (Λ−l), whose total is λΛ/2.
- (c) Each Golomb class is ≤ Q(S−l) ≤ Q(S−1), so the other one is ≥ r(l) − Q(S−1) ≥ (1−β)(Q(S−1) + Q(S−2)) − Q(S−1) ≥ Q(S−2) − βv_1. ∎

Combined with Proposition 4.6(b), taking θ = 3η + 2ξ and λ ≈ εS: an FD-violator at level η has, in each of its three classes and at all but a weighted fraction O((η + ε + S^{−3/8})/β) of the lags l ≤ εS, fibres that are unions of two Sidon sets each of size ≥ Q(S−2) − βv_1. (HEURISTIC reading at the regime, with S = 2.2·10^7 and v_1 = 9.4·10^3, using the numerical value K_F/c − 1 ≈ 0.0021 in place of ξ: for η = 0.01, each class must be within about 3.4% of c, i.e. θ ≈ 0.034, and at λ = 0.02 S the bound (a) gives D̄(λ) ≤ about 0.089, i.e. a weighted mean fibre deficit below about 9% over the lags l ≤ 0.02 S. With the proved ξ(S) ≈ 0.0068 instead, the numbers are θ ≈ 0.044 and D̄ ≤ about 0.107.)

**Proposition 4.8 (FD in structured sub-cases). PROVED.**
- (a) **Translation-invariant colorings**, χ(v,u) = φ(v−u). Then F_d(D) = S_{φ(d)}(d) is a single class, so |F_d(D)| ≤ K_F ≤ (1+ξ)c. FD holds with η = (2 − ξ(S_0))/3, for example η = 0.6 for S_0 = 2700.
- (b) **Shifts with a small class.** If some class at shift d has size ≤ (1−θ')c, then |F_d(D)| ≤ (3 − θ' + 2ξ)c, i.e. the shift satisfies FD with η = (θ' − 2ξ)/3. (Contrapositive of 4.6(b).)
- (c) **Difference-colored classes.** Suppose the shifted source of X = S_e(d) is difference-colored: ψ(a,b) = f(b−a). Then each F_l(X) is a single Golomb class, so r_X(l) ≤ Q(S−l) ≤ Q(S−1). The argument of Corollary 4.3 and Lemma 4.4, with v_1 replaced by Q(S−1), gives |X| ≤ (1 + 5S^{−3/8}) sqrt(Q(S−1) S). Since Q(S−1)/v_1 ≤ Q(S−1)/(2Q(S−1) − 1) by (Q-step), this is (1/sqrt 2 + o(1)) c(S). If all three classes at d are difference-colored, FD holds at d with η = 1 − 1/sqrt 2 − o(1) ≈ 0.29.

*Proof of the constant in (c).* sqrt(Q(S−1)S) ≥ sqrt(sqrt((S−1)/8)·S) ≥ S^{3/4}/2 for S ≥ 34. Rerunning Lemma 4.4 gives (S^{3/8}+1)/sqrt(Q(S−1)S) ≤ 4S^{−3/8}, plus S^{−3/8}. ∎

*Remark (PROVED).* For a difference-colored binary source X, properness is equivalent to f(x) = f(y) ≠ f(x+y) for every realized pair (x,y), i.e. every (x,y) with some u such that u, u+x, u+y, u+x+y ∈ X. The case x = y is included. *Proof.* The realized pair (x,y) gives the L L(u, x, x+y), with arm lags x, x and corner lag x+y; the symmetric pair gives arm lags y, y. With two colors, f(x) ≠ f(x+y) and f(y) ≠ f(x+y) force f(x) = f(y). Conversely, every L has this form. ∎ Consequently such an X contains no Hilbert cube u + {0,d_1} + {0,d_2} + {0,d_3}. The pairs (d_1,d_2), (d_1,d_3), (d_2,d_3) and (d_1+d_2, d_3) are all realized at u, which gives f(d_1+d_2) ≠ f(d_1) = f(d_3) = f(d_1+d_2).

### 4.9 Reduction of FD to two near-maximal Sidon sets (NTSD ⇒ FD). PROVED

Throughout this subsection, fix a proper ternary source (D, χ), a shift d ≥ 1 and a lag l ≥ 1, and put h = d+l. Write Y = F_d(D), S = span Y, X_e = S_e(d) and s_e = |X_e|.

**The lag-l start set.**
- Put A^e = F_l(X_e). The sets A^0, A^1, A^2 are pairwise disjoint, because the X_e are.
- Put W = A^0 ∪ A^1 ∪ A^2.
- For p ≤ q in W put κ(p,q) := χ(q+h, p).

This is a cell of V(D). We have p ∈ D. Also q+l ∈ X_e ⊆ F_d(D), so q+h = (q+l)+d ∈ D. Finally q+h > p.

**Lemma W.**
- (a) *Properness.* Let p ∈ W and 0 ≤ x < y with p+x, p+y−x, p+y ∈ W. Then κ(p,p+x), κ(p,p+y) and κ(p+y−x,p+y) are not all equal.
- (b) *In-class constraint.* If p ≤ q both lie in A^e, then κ(p,q) ≠ e. In particular κ(p,p) = χ(p+h,p) differs from the class color e of p.

*Proof.*
- (a) Take L(p, h+x, h+y) of Lemma 0; here 1 ≤ h+x < h+y.
  - Its horizontal arm end is (p+h+x, p), with color κ(p,p+x).
  - Its corner is (p+h+y, p), with color κ(p,p+y).
  - Its vertical arm end is (p+h+y, p+y−x), with color κ(p+y−x, p+y).

  By Lemma 0(b) it lies in V(D) iff p, p+h+x, p+y−x and p+h+y all lie in D. This holds: p and p+y−x lie in W ⊆ D, and p+x, p+y ∈ W give p+x+h, p+y+h ∈ D by the remark above. Properness of χ gives the claim.
- (b) We have p, q+l ∈ X_e and p < q+l. By (iv.0), ψ(p, q+l) = χ(q+l+d, p) = κ(p,q) ≠ e. ∎

**The three layers.** For f ∈ P put U_f = {p ∈ W : κ(p,p) = f}. By Lemma W(b), U_f contains no point of A^f. Let {e,e'} = P∖{f}. Then U_f is the disjoint union of
- A_f := A^e ∩ U_f, the f-colored Golomb class F_l(X_e) ∩ S_f(h) of F_l(X_e), and
- B_f := A^{e'} ∩ U_f, the f-colored Golomb class of F_l(X_{e'}).

**Corollary U.** Write c(p,q) = κ(p,q) for p < q in U_f.
1. c takes values in {e, e'}.
2. The coloring (q,p) ↦ c(p,q) of V(U_f) is proper.
3. c ≡ e' on pairs inside A_f, and c ≡ e on pairs inside B_f.

*Proof.*
- **Item 1.** Lemma W(a) with x = 0 and y = q−p shows that κ(p,p), κ(p,q) and κ(q,q) are not all equal. The first and the last equal f, so c(p,q) ≠ f.
- **Item 2.** Let u < v in U_f and g > 0 with u+g, v+g ∈ U_f. Apply Lemma W(a) with p = u, x = g and y = v+g−u, so 0 ≤ x < y. The points p+x = u+g, p+y−x = v and p+y = v+g lie in U_f. So c(u,u+g), c(u,v+g) and c(v,v+g) are not all equal. By Lemma 0 applied to the set U_f, these triples are exactly the L's of V(U_f), and the case v = u+g is included.
- **Item 3.** For p < q in A_f we have c(p,q) ≠ f by item 1 and c(p,q) ≠ e by Lemma W(b). So c(p,q) = e'. The argument for B_f is the same. ∎

**Definition (TSD instance).** A TSD instance of span m is a triple (A, B, c) with the following properties.
- A and B are disjoint Sidon sets, both contained in one interval of m+1 consecutive integers. Put U = A ∪ B.
- c colors the pairs x < y of U with {0,1}.
- c(x,y) = 0 whenever x, y ∈ A ("A-pairs"), and c(x,y) = 1 whenever x, y ∈ B ("B-pairs").
- c is proper: for all u < v in U and g > 0 with u+g, v+g ∈ U, the values c(u,u+g), c(v,v+g) and c(u,v+g) are not all equal. The case v = u+g is included.

By Lemma 0, the last condition says exactly that the coloring of V(U) given by c is proper. Pairs with one end in A and the other in B are called *mixed*; their colors are not prescribed.

**Definition (NTSD(β, m_0)).** For every m ≥ m_0 there is no TSD instance of span m with |A| ≥ (1−β)Q(m) and |B| ≥ (1−β)Q(m).

NTSD is a statement about two disjoint Sidon sets and a 2-coloring of their mixed pairs. In the ternary source, it concerns the interaction of two different completion classes at one shift, not the capacity of one binary source.

**Lemma D (each layer is a TSD instance).** Let f ∈ P and {e,e'} = P∖{f}. Color the pairs p < q of U_f by c'(p,q) = 0 if κ(p,q) = e', and c'(p,q) = 1 if κ(p,q) = e. Then (A_f, B_f, c') is a TSD instance of span m = S − l.

*Proof.*
- c' is well defined, by Corollary U item 1.
- A_f and B_f are disjoint, since A^e ∩ A^{e'} = ∅. Both are Sidon by (iv.2), being Golomb classes.
- U_f ⊆ F_l(X_e) ∪ F_l(X_{e'}) ⊆ [min Y, max Y − l], an interval of S−l+1 integers.
- c' ≡ 0 on A_f-pairs and c' ≡ 1 on B_f-pairs, by Corollary U item 3.
- c' is proper by Corollary U item 2, since it is a bijective renaming of c. ∎

**Three elementary facts** are used below.
- *Q is nondecreasing.* An interval of m+1 consecutive integers lies inside one of m+2. Hence v_1(S) and c(S) are nondecreasing in S.
- *Write ξ*(S) := K_F(S)/c(S) − 1.* By Corollary 4.3 and Lemma 4.4, 0 ≤ ξ*(S) ≤ ξ(S) = 3.83 S^{−3/8} for S ≥ 34.
- By Lemma 4.1, v_1 ≥ sqrt(S)/2 for S ≥ 34, so c(S)/v_1 = sqrt(S/v_1) ≤ sqrt 2·S^{1/4}.

**Lemma A (an FD-violator has three near-cap classes).** Let S ≥ 34 and η ≥ 0, and suppose |Y| ≥ 3(1−η)c(S). Then every class satisfies s_e ≥ (1−θ)c(S), with θ := 3η + 2ξ*(S).

*Proof.* Each class is a binary source of span ≤ S with fibres ≤ v_1, by (iv.0) and the per-fibre cap. By Corollary 4.3 each class has size ≤ K_F(S) = (1+ξ*)c. So s_e = |Y| − Σ_{e'≠e} s_{e'} ≥ 3(1−η)c − 2(1+ξ*)c. ∎

**Lemma B (one lag saturated for two classes).** Let S ≥ 34 and θ = 3η + 2ξ*(S). Let λ be an integer with 1 ≤ λ ≤ S−1, put Λ = λ+1, and let β' ∈ (0,1). Put

  B(S, λ, η) := 2θ + Λ/S + K_F(S)/(v_1 λ).

Assume |Y| ≥ 3(1−η)c(S) and **(H1)** 2B(S,λ,η) < β'. Then for any two classes X_e, X_{e'} there is a lag l ∈ [1, λ] with r_{X_e}(l) ≥ (1−β')v_1 and r_{X_{e'}}(l) ≥ (1−β')v_1.

*Proof.*
- (H1) gives 2θ < β'/2 < 1, so θ < 1.
- By Lemma A, X_e and X_{e'} satisfy the hypotheses of Proposition 4.7 with this θ, and Λ ≤ S.
- Proposition 4.7(a), with s_e ≤ K_F(S), gives D̄_e(λ) ≤ B. Likewise D̄_{e'}(λ) ≤ B.
- Let Bad_x = {l ≤ λ : r_{X_x}(l) < (1−β')v_1}. By Proposition 4.7(b), the (Λ−l)-weight of Bad_x is at most (B/β')·λΛ/2.
- So the weight of Bad_e ∪ Bad_{e'} is at most (2B/β')·λΛ/2. By (H1) this is less than λΛ/2, the total weight.
- Every lag l ≤ λ has weight Λ−l ≥ 1. So some lag lies outside both bad sets. ∎

**Lemma C' (saturated fibres have two near-maximal Golomb classes).** Let X be a class, 1 ≤ l ≤ S−1 and 0 < β' < β/2. Suppose r_X(l) ≥ (1−β')v_1 and **(H3)** Q(S−l) ≥ (1−β')/(β−2β'). Then both Golomb classes of F_l(X) have size ≥ (1−β)Q(S−l).

*Proof.*
- Each Golomb class is a Sidon set in an interval of S−l+1 integers, so it has size ≤ Q(S−l).
- So the smaller class has size g ≥ r_X(l) − Q(S−l).
- We have v_1 ≥ 2Q(S−l) − 1. For l ≥ 2 this holds because Q(S−1), Q(S−2) ≥ Q(S−l). For l = 1 it holds because Q(S−2) ≥ Q(S−1) − 1, by (Q-step).
- Hence g ≥ (1−β')(2Q(S−l) − 1) − Q(S−l) = (1−2β')Q(S−l) − (1−β').
- This is ≥ (1−β)Q(S−l) iff (β−2β')Q(S−l) ≥ 1−β', which is (H3). ∎

**Theorem R' (parametrised reduction).** Assume NTSD(β, m_0) with β ∈ (0, 1/2] and m_0 ≥ 1. Let S ≥ 34, η ≥ 0, β' ∈ (0, β/2) and an integer λ ∈ [1, S−1] satisfy
- (H1) 2[6η + 4ξ*(S) + (λ+1)/S + K_F(S)/(v_1(S)λ)] < β';
- (H2) S − λ ≥ m_0;
- (H3) Q(S−λ) ≥ (1−β')/(β−2β').

Then every proper ternary source and every shift d with span F_d(D) = S satisfy |F_d(D)| < 3(1−η)c(S).

*Proof.* Suppose instead that |Y| ≥ 3(1−η)c(S). The bracket in (H1) is B(S,λ,η), since 2θ = 6η + 4ξ*.
1. Fix f = 0 and {e,e'} = {1,2}. Lemma B gives a lag l ∈ [1,λ] at which X_e and X_{e'} both have r ≥ (1−β')v_1.
2. Q(S−l) ≥ Q(S−λ), so (H3) holds with S−l in place of S−λ. By Lemma C', the f-colored Golomb classes A_f of F_l(X_e) and B_f of F_l(X_{e'}) both have size ≥ (1−β)Q(m), where m = S−l.
3. By Lemma D, (A_f, B_f, c') is a TSD instance of span m. Also m ≥ S−λ ≥ m_0 by (H2).
4. This contradicts NTSD(β, m_0). ∎

Only one instance is used: one lag and one pair of classes. The third class enters only through Lemma A.

**Theorem R (explicit constants).** For β ∈ (0, 1/2] and m_0 ≥ 1 put

  η(β) = β/48,  S_0(β, m_0) = max( (1471/β)^{8/3}, (96/95)m_0 ).

Then NTSD(β, m_0) implies FD(η(β), S_0(β, m_0)). In fact |F_d(D)| < 3(1−β/48)c(S) whenever S = span F_d(D) ≥ S_0.

*Proof.* Let S ≥ S_0, and take β' = β/3, η = β/48 and λ = ⌊βS/48⌋. We check the hypotheses of Theorem R'.

*Preliminaries.*
- S ≥ (1471/β)^{8/3} ≥ 2942^{8/3} > 1.7·10^9. So S ≥ 34 and βS ≥ 96.
- Hence λ ≥ βS/48 − 1 ≥ βS/96 ≥ 1, and λ ≤ βS/48 ≤ S/96 ≤ S−1.
- 4ξ(S) = 15.32 S^{−3/8}, and 15.32 S^{−3/8} ≤ β/96 iff S ≥ (1470.72/β)^{8/3}. So 4ξ*(S) ≤ 4ξ(S) ≤ β/96, and in particular ξ(S) ≤ 1/768.
- 1/S ≤ β/384.

*(H1).*
- K_F/(v_1λ) = (1+ξ*)c/(v_1λ) ≤ (1 + 1/768)·sqrt 2·S^{1/4}·96/(βS) ≤ 135.95 S^{−3/4}/β.
- This is ≤ β/192 as soon as S^{3/4} ≥ 26,103/β², i.e. S ≥ (26,103/β²)^{4/3}. That is implied by S ≥ (1471/β)^{8/3} = (1471²/β²)^{4/3}.
- (λ+1)/S ≤ β/48 + β/384.
- Summing: 6η + 4ξ* + (λ+1)/S + K_F/(v_1λ) ≤ β/8 + β/96 + β/48 + β/384 + β/192 = 63β/384 < β/6.
- So the doubled bracket is < β/3 = β'.

*(H2).* S − λ ≥ (1 − β/48)S ≥ (95/96)S ≥ m_0.

*(H3).* Here (1−β')/(β−2β') = 3/β − 1. Put m' = S−λ ≥ (95/96)S. Then m' ≥ 72/β² ≥ 288 ≥ 32, since (1471/β)^{8/3} ≥ 1471^{8/3} β^{−2}. By (Q-low), Q(m') > sqrt(m'/8) ≥ 3/β. ∎

The numerical inequalities used here were rechecked by computer: 15.32·96 = 1470.72, (1 + 1/768)·sqrt 2·96 < 135.95, 135.95·192 < 26,103 < 1471², and 2942^{8/3} > 1.7·10^9.

**Remark (other constants).** The same proof gives, for every fixed η < β/24, an explicit S_0 such that NTSD(β, m_0) implies FD(η, S_0).
- Choose β' with 12η < β' < β/2, and λ = ⌊εS⌋ with ε small.
- Then ξ(S) → 0, Λ/S → ε, and K_F/(v_1λ) = O(S^{−3/4}/ε) → 0. (H3) holds for large S by (Q-low).
- The limit β/24 is forced by the method, since 12η ≤ 4θ must be < β' < β/2.

**Corollary R.** Assume NTSD(β, m_0). For every proper ternary source and every d with span F_d(D) = S ≥ S_0(β, m_0):

  Σ_e |S_e(d)| = |F_d(D)| < 3(1−β/48)c(S) ≤ (1−β/48)·3K_F(S).

This is the per-shift (D-a) inequality with δ = β/48, against the sum of the three separate Fejér caps.

*Proof.* Theorem R, then c ≤ K_F (Corollary 4.3). ∎

**Scale caveat.** S_0 > 1.7·10^9 for every admissible β. That is far above the spans ≈ 2.2·10^7 of the R4 consumer, so Corollary R with these constants is vacuous at the current scale. Only Theorem R' could matter there, applied with numerically certified values of ξ*(S) and K_F(S)/v_1(S) at the actual spans.

HEURISTIC estimate. Take S = 2.2·10^7, v_1 = 9.4·10^3, ξ* ≈ 0.0021 and K_F/v_1 ≈ 48.5. The best λ is about 3.3·10^4. Then (H1) reads roughly η < (β/4 − 0.0114)/6. This is positive only for β > 0.046; for example, β = 0.1 gives η ≈ 0.0023.

### 4.10 What is known about NTSD

Let (A, B, c) be a TSD instance and U = A ∪ B. For a Sidon set A and g > 0, let α_A(g) be the start of the unique A-pair of difference g, if it exists.

**Lemma C1 (first-generation forcing). PROVED.**
- (AB cell) Let a ∈ A and a+g ∈ B. If α_A(g) > a, then c(a,a+g) = 1. If α_B(g) < a, then c(a,a+g) = 0.
- (BA cell) Let b ∈ B and b+g ∈ A. If α_B(g) > b, then c(b,b+g) = 0. If α_A(g) < b, then c(b,b+g) = 1.

*Proof.* Write α = α_A(g) and β_0 = α_B(g).
- AB, first claim. The L with u = a < v = α has cells c(a,a+g), c(α,α+g) = 0 and c(a,α+g) = 0; the last is an A-pair.
- AB, second claim. The L with u = β_0 < v = a has cells c(β_0,β_0+g) = 1, c(a,a+g) and c(β_0,a+g) = 1; the last is a B-pair.
- BA, first claim. The L with u = b < v = β_0 has cells c(b,b+g), c(β_0,β_0+g) = 1 and c(b,β_0+g) = 1, a B-pair.
- BA, second claim. The L with u = α < v = b has cells c(α,α+g) = 0, c(b,b+g) and c(α,b+g) = 0, an A-pair. ∎

**Lemma C (no collision). PROVED.** Let g > 0, with α_A(g) and α_B(g) both defined.
- If α_B(g) < α_A(g), no a ∈ A with a+g ∈ B satisfies α_B(g) < a < α_A(g).
- If α_A(g) < α_B(g), no b ∈ B with b+g ∈ A satisfies α_A(g) < b < α_B(g).

*Proof.* Otherwise Lemma C1 forces both colors on one cell. ∎

A configuration that violates Lemma C is a **C-collision**. Each C-collision certifies that the pair (A, B) carries no TSD coloring.

**Proposition O (translates have no collision). PROVED.** Let t ≥ 1, let A be a Sidon set with no positive difference in [1, 2t], and put B = A + t. Then A ∩ B = ∅, B is Sidon, and (A, B) has no C-collision.

*Proof.*
- A ∩ B = ∅ because t is not a difference of A.
- For a difference g of A, α_B(g) = α_A(g) + t > α_A(g), so only the BA case can occur.
- A BA cell (b, b+g) with b = a'+t, a' ∈ A, and α_A(g) < b < α_A(g)+t, would give 0 < |a' − α_A(g)| < t. That is a difference of A in [1, 2t]. ∎

Deleting all differences in [1, 2t] costs a Sidon set at most 2t points, since each difference occurs at most once. So Proposition O applies to near-maximal Sidon sets.

**Theorem P (collisions decide the first-generation subsystem exactly). PROVED.** Let Σ_1 be the set of L's of V(U) whose spanning cell (u, v+g) is an A-pair or a B-pair. Some coloring of the mixed pairs satisfies every L of Σ_1 iff (A, B) has no C-collision.

*Proof.*
- **Decoupling.** In an L of Σ_1 the mixed cells can only be the short cells (u,u+g) and (v,v+g), and both have lag g. A mixed pair (x,y) is a short cell only at the lag y−x. So Σ_1 splits into independent systems Σ_1(g), one for each lag g.
  - The variables of Σ_1(g) are γ(p) := c(p,p+g) for the mixed starts p, i.e. p and p+g in U, one in A and one in B.
  - The values γ(α_A(g)) = 0 and γ(α_B(g)) = 1 are fixed.
- **The constraints of Σ_1(g).** Take starts p < q at lag g.
  - If p ∈ A and q+g ∈ A, the constraint is "not γ(p) = γ(q) = 0".
  - If p ∈ B and q+g ∈ B, it is "not γ(p) = γ(q) = 1".

  A start is of type AA, AB, BA or BB according to the memberships of p and p+g. The AA-start and the BB-start, if they exist, are unique. Going through the types of p and q, the constraints are:
  1. an AB-start p < α_A gets γ(p) = 1, and an AB-start p > α_B gets γ(p) = 0;
  2. a BA-start q > α_A gets γ(q) = 1, and a BA-start q < α_B gets γ(q) = 0;
  3. for an AB-start p and a BA-start q: if p < q, not both 0; if q < p, not both 1;
  4. two AB-starts, or two BA-starts, give no constraint, because the spanning cell is mixed. The pair α_A, α_B gives none either.

  Items 1 and 2 are Lemma C1.
- **Only if.** A C-collision forces one variable to both values.
- **If.** Pick a real τ that is not a start. Set γ(p) = 1 for AB-starts p < τ and γ(p) = 0 for AB-starts p > τ. Set γ(q) = 0 for BA-starts q < τ and γ(q) = 1 for BA-starts q > τ.
  - Item 3 holds for every τ. AB p < BA q both 0 would mean p > τ > q. BA q < AB p both 1 would mean q > τ > p.
  - Items 1 and 2 need four implications: AB p < α_A ⇒ p < τ; AB p > α_B ⇒ p > τ; BA q > α_A ⇒ q > τ; BA q < α_B ⇒ q < τ.
  - Suppose both α's exist and α_B < α_A. There is no AB-start in (α_B, α_A), since there is no collision. Take τ ∈ (α_B, α_A). An AB-start p < α_A then has p < α_B < τ. An AB-start p > α_B has p > α_A > τ. The BA conditions are immediate.
  - If α_A < α_B, there is no BA-start in (α_A, α_B). Take τ ∈ (α_A, α_B); the checks are symmetric.
  - If only one α exists, take τ equal to it. If neither exists, any τ works.
- Since the Σ_1(g) are independent, Σ_1 is satisfiable. ∎

(Computer check, evidence only. On 2,990 random pairs of disjoint Sidon sets in intervals of length 10-30, satisfiability of Σ_1 was decided by exhaustive search. It agreed with the absence of C-collisions in every case.)

**Corollary P1. PROVED.** Every contradiction in the TSD system of a collision-free pair involves an L whose spanning cell is mixed. With Proposition O, this means no argument confined to the first-generation L's can prove NTSD.

**Proposition 2G (second-generation conflicts). PROVED.** For a start p at lag g, let φ_g(p) ∈ {0, 1, ∗} be its forced value:
- φ_g(α_A) = 0 and φ_g(α_B) = 1;
- for mixed starts, φ_g(p) is the value given by Lemma C1;
- φ_g(p) = ∗ otherwise.

Every TSD coloring has c(p,p+g) = φ_g(p) whenever φ_g(p) ≠ ∗. If p < q are starts at lag g with φ_g(p) = φ_g(q) = f, then the L (p,p+g), (q,q+g), (p,q+g) forces c(p, q+g) = 1−f. When (p, q+g) is mixed, call this a forcing of that mixed cell from lag g. Each of the following excludes every TSD coloring:
- **Type I.** A mixed cell (x,y) is forced to 1−f from some lag g, and φ_{y−x}(x) = f.
- **Type II.** A mixed cell (x,y) is forced to 0 from one lag and to 1 from another.

*Proof.* In type I the forcing gives c(x,y) = 1−f, while c(x,y) = φ_{y−x}(x) = f. In type II the two forcings conflict. ∎

**NTSD fails at small spans (finite fact, checked by computer).**
- A = {0,1,4,13,15,21} and B = {2,5,7,16,22,23} are disjoint Sidon sets in [0,23].
- There is no 7-element Sidon set in [0,23], so Q(22) = Q(23) = 6 and |A| = |B| = Q(23).
- V(A ∪ B) contains 76 L's. An exhaustive backtracking search finds a proper coloring with A-pairs 0 and B-pairs 1.

So this is a TSD instance of span 23 with both sets of maximum size, and NTSD(β, m_0) can hold only with m_0 > 23. These facts were rechecked at the final revision.

**What is open.** NTSD(β, m_0) itself is open for every β > 0. By Theorem P, a proof must refute every collision-free near-maximal pair through an L with a mixed spanning cell, for example by a type I or type II conflict. What is missing is control of the relative order of α_A(g), α_B(g) and the mixed starts across lags. Pair counts, energy and Fourier-magnitude bounds do not see this order.

---

---

## 5. Consequence for R_4 (implication only; no bound is claimed)

Suppose FD(η, S_0) holds with explicit η and an explicit S_0 (how small S_0 must be is stated below). Apply it to each D_c (c a main-diagonal color) at every shift d ≤ t−1 = 34,999. Then

  X_d = Σ_c |F_d(D_c)| ≤ 12(1−η) c(n−1−d) + 4S_0,

using that c is nondecreasing. Here:
- D_c, with χ restricted to V(D_c), is a proper ternary source after relabelling the three colors other than c, and span F_d(D_c) ≤ n−1−d.
- The term 4S_0 covers the colors c for which span F_d(D_c) < S_0. Such a set has at most S_0 elements.
- At the regime, 12 c(n−1−d) ≈ 5.45·10^6 (HEURISTIC inputs as in Section 4). So 4S_0 ≤ (η/2)·12c(n−1−d) as soon as S_0 ≤ 6·10^5·η. Then X_d ≤ 12(1−η/2) c(n−1−d). So FD is useful to the consumer only with S_0 well below the spans, not merely below about 2·10^7. Section 4.9 gives such an FD from NTSD, but with S_0 > 1.7·10^9, so that route is vacuous at this scale unless Theorem R' is applied with certified numerics at the actual spans. This gives the problem's hypothetical saving X_d ≤ (1−δ)U_d only after one more step: certify c(S) ≤ K(S−j) for the consumer's rank caps K at the spans used, with Q replaced by a certified upper bound (replacing Q by an upper bound only enlarges the right side of FD).

The problem's numbers suggest c ≈ 4.55·10^5 against K ≈ 4.58·10^5, a margin of about 0.7%. This is HEURISTIC and must be certified. The margin shrinks to about 0.1% if v_1 is computed from the classical bound Q(m) ≤ sqrt(m) + m^{1/4} + 1 (v_1 ≈ 9,517, c ≈ 4.574·10^5). (Lindström's bound, as recalled, reads F(N) < N^{1/2} + N^{1/4} + 1 for subsets of {1,…,N}; since Q(m) = F(m+1), the exact form is Q(m) < sqrt(m+1) + (m+1)^{1/4} + 1. The difference is numerically negligible here.) The loss of staggering (12 distinct minima) is additive and of relative size about 10^{−6}.

With that, δ ≥ η/2 (δ ≥ η − O(S_0/c) in general), and the sensitivity statement of the problem applies: a factor of about 1 − 3.9δ (HYPOTHETICAL).

**Remark (HEURISTIC; a single-class question, outside Part D).** The same numbers place the Fejér cap itself below the consumer's cap: K_F ≈ 4.557·10^5 (computed from v_1 = 9.4·10^3, S = 2.2·10^7) against K ≈ 4.58·10^5, about 0.5% lower. Corollary 4.3 is a valid single-class cap for every class, with Q replaced by any certified upper bound. If, after both caps are recomputed with the same certified Q-bound at the consumer's spans, K_F(S−j) < K(S−j) still holds, then replacing K by min(K, K_F^♯) in U_d is a proportional saving obtained without any cross-class information. This is not established here, and the sign is fragile. Computer evaluation at S = 2.1987·10^7 (HEURISTIC inputs):
- with v_1 = 9,350, 9,400 or 9,450 (the rounding range of "9.4·10^3"), K_F/4.58·10^5 − 1 is about −0.8%, −0.5% and −0.3%;
- with the classical upper bound Q(m) ≤ sqrt(m) + m^{1/4} + 1 (CITED, Erdős–Turán/Lindström type), v_1 ≈ 9,517 and K_F is about 0.1% above 4.58·10^5. K_F^♯ is still 0.03% above it.

So the comparison is decided by which certified Q-bound the consumer's v_l uses, and by the unrounded K. It concerns the binary-source capacity, not the request geometry of Part D.

Nothing in this document proves FD or NTSD. So nothing here improves R_4.

---

## Status

**Main claim: NOT fully proved.** The task asks for P1 (i)-(v) complete, and for Part D settled at level (D-a) or (D-b). P1 is fully proved. Part D is not settled.

**Fully proved in this document.**
- Part P1 (i)-(v), exactly as posed (Theorem 1). This includes the L parametrisation (corner (u+h,u), arms (u+d,u) and (u+h,u+h−d), arm length h−d), the sharp double-cover identity, and the four-L Golomb split.
- Section 2: request-counting inequalities over arbitrary sources.
  - The digit families refute UW(λ) for every λ, U1-type energy bounds for every C, and union growth with liminf f > 0, simultaneously on any finite set of shifts (Theorem 2.6).
  - The lifted family has request-producing classes and fibres of size span^{1/2−o(1)}. It refutes UW(λ) for every λ, energy bounds only for C < 3, and union growth only for liminf f > 1/3 (Corollary 2.11).
- Section 3: (D-c). The forced sets are Sidon (Proposition 3.1). Full foreign coverage with balanced Golomb classes occurs (Theorem 3.2), so (D-c+) fails without near-extremality. Under near-extremality, an imbalance is a fibre deficit up to an additive 1 (Proposition 3.3).
- Section 4: per shift and against the Fejér caps K_F, (D-a) is equivalent to FD up to O(S^{−3/8}) (Theorem 4.5). SCD implies FD (Proposition 4.6). An FD-violator has three near-cap classes whose fibres are saturated on all lags l ≤ λ except a (Λ−l)-weighted fraction O((η + λ/S + S^{−3/8})/β) (Proposition 4.7). FD holds in structured sub-cases (Proposition 4.8).
- Section 4.9: NTSD(β, m_0) implies FD(β/48, S_0) with S_0 = max((1471/β)^{8/3}, (96/95)m_0) (Theorem R), together with the parametrised form (Theorem R').
- Section 4.10: Theorem P (collisions decide the first-generation subsystem exactly) and Propositions O and 2G.

**Gaps (open).**
- **(D-a) is not proved** in any requested form, per shift or a_h-averaged, with any explicit δ > 0. Its per-shift core is FD(η, S_0). FD is implied by SCD (a single-binary-source deficit) and by NTSD. Neither SCD nor NTSD is proved, and NTSD fails at span 23.
- **(D-b) at regime size is not done.** Every construction here has classes far below the regime (about 98·sqrt(span)) and below the binary cap. No construction refutes interval averaging with the weights a_h; the shift sets used are sparse.
- **Embedding.** The Theorem 2.6 families (B = 100) have span ≥ 10^8, and lifted instances with N_e/|F_H| ≥ 240 need k ≥ 360 atoms below the shift, so span ≥ B^{360}. By the R4 bound stated in the problem, none of these is a diagonal class of a properly four-colored square. For smaller lifted members (for example m' = 1, k = 1, small p) the span does not exclude them, and their embeddability is **not settled**. The B = 9 variant of the cyclic family (span 14,880,348) is also not settled.
- Even a proof of NTSD would not give an R_4 improvement with the constants of Theorem R, since S_0 > 1.7·10^9. Theorem R' needs certified values of ξ* and K_F/v_1 at spans ≈ 2.2·10^7, and NTSD with β > 0.046 there.
- The consumer comparison 12c(n−1−d) ≤ (1−δ')U_d (Fejér scale against rank caps with staggering) is not certified (Section 5).
- **No bound on R_4 is claimed.**

---

## Other routes

These are recorded so that they are not repeated. Items marked "earlier work" were obtained in earlier rounds of this attempt. They are **not proved in this document** and nothing above uses them.

- **Joint fibre and prefix deficits (earlier work).** The statements MS and MS' were the missing statements of earlier rounds. MS is a joint prefix deficit of Σ_e r_{S_e(d)}(l) against 3v_l for all λ. MS' is the same with an additive slack S/100 and S ≥ S_0. They are neither proved nor refuted. They were retired because MS' implies the size deficit Σ_e s_e^2 < 3(1−η)v_1 S, hence FD, by Lemma 4.2 summed over windows. So MS' is no reduction of the goal. Earlier work also gave a rank-based conversion "prefix deficit δ ⇒ cap loss about δ/2" against the consumer's rank caps. The Fejér route of Section 4 replaces it here.
- **Lag-by-lag information cannot give a deficit.**
  - For every prime power q ≥ 7 there are six pairwise disjoint Sidon sets of size q in [0, q^2−2]. *Proof:* a Bose set A ⊂ Z/(q^2−1) (CITED) has q elements, is Sidon mod q^2−1, and its nonzero differences are exactly the residues not divisible by q+1. So the translates A + j(q+1), 0 ≤ j < q−1, are pairwise disjoint and each is Sidon mod q^2−1; read as subsets of [0, q^2−2], each is Sidon in Z. (Checked by computer for q = 7.) So "six disjoint Sidon pieces per lag" gives no joint deficit.
  - Earlier work: in the coupled one-lag structure, no single mixed additive-quadruple pattern is forbidden. A single quadruple's constraints are unsatisfiable only when all four points have the same (class, color) type.
  - The TSD instance at span 23 of Section 4.10 shows that the per-lag statement "two disjoint Sidon pieces carrying a TSD coloring lose a fixed proportion of Q(m) + Q(m−1)" can hold only asymptotically.
- **Lag-pair counting is balanced (HEURISTIC dead end).** At saturation, parallelogram counts, Sidon agreement bounds, transport and the separation lemma (Corollary 1.3) are all met in proportion by random-like colorings. A ±1 sum over all L's reduces to bookkeeping. Energy and Gowers-type counts are consistent at saturation. A proof must be global across lags.
- **Toward NTSD (leads, not proved).**
  - *Translate model.* For B = A + t, one can show that the TSD system reduces to a finite system in which one family of constraints says that a graph on A defined by forced labels must be a split graph. An induced 2K_2, C_4 or C_5 among forced labels would then give a contradiction. This uses the Földes-Hammer characterization (CITED from memory) and was not completed.
  - *Computer evidence, evidence only.* In samples of near-maximal Bose-type pairs (q = 7 to 23, spans up to about 500), no TSD coloring was found. Trimmed small translates (the Proposition O regime) were mostly not colorable for q ≥ 13. Below near-maximality, colorings are common: greedy colorable pairs reach about 0.77-0.87 of Q(m)+Q(m−1) at m ≤ 160. So β cannot be large; roughly β < 0.2 at these sizes.
- **Constructions toward a counterexample that fail (earlier work).**
  - Block-placed and digit-product sources (M·B + R with B Sidon) have joint prefix ratio at most about Q(ρ)/sqrt(M). Base-M products need full-grid 2-colorings and do not raise the exponent above 1/2.
  - Doubling, D = Y ∪ (Y+d) with d > 2 span Y, gives F_d(D) = Y. But it turns the converse of Proposition 4.6(a) into a proper 3-coloring of the full grid Y × Y with prescribed diagonal, which is the original square problem on Y (HEURISTIC remark).
  - Difference colorings lose a factor 1/sqrt 2 (Proposition 4.8(c), proved above).
  - Row, column and diagonal colorings fail on long progressions.
  - No binary source of size span^{1/2+ε} is known; Sidon sets give about sqrt(span).
- **Necessary size of a counterexample.** Any violation of FD needs three classes of size about sqrt 2·S^{3/4} at one shift (Proposition 4.6, proved above). Earlier work: any violation of MS' needs classes of size > S^{5/8}/16.
- **Density (CITED, non-explicit).** Modulo the corners theorem (cited from memory), for fixed ρ > 0 no proper ternary source has D of density ≥ ρ on an interval of length ≥ S(ρ). This is non-explicit and gives no δ.
- **Band lemma (earlier work, no quantitative use found).** At one shift, β(y,a) := χ(a+d, y) for y, a ∈ F_d(D) with a+d > y is a proper 3-coloring of the sparse grid {(a,y) : a > y−d}, whose diagonal classes are the S_e(d). It contains (iv.0) and the cross-class coupling. Section 4.9's (W, κ) is the one-lag version of this structure.
- **Single-class Fejér cap versus the rank cap (HEURISTIC, single-class question).** See the remark in Section 5. Whether min(K, K_F^♯) gives a proportional saving with no cross-class information depends on the certified Q-bound, and the sign is fragile.
