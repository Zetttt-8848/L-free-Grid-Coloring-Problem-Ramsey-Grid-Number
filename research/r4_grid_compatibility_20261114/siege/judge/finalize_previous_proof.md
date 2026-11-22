# Request geometry inside a three-colored diagonal class: what is proved, and what is open

## Status (read this first)

- **Part P1 (i)-(v) is PROVED completely** from the cell coordinates (Theorem 1, Section 1).
- **Part D is NOT settled.** No explicit proportional-loss inequality (D-a) is proved for ternary sources at the regime size. No counterexample at regime size (D-b) is known either. What is proved is listed below. The single statement that remains open is named in Section 7 (statement FD, equivalently the per-shift (D-a) clause against the Fejér caps).
- **Proved toward Part D:**
  - (D-b) over arbitrary ternary sources (Section 2). Explicit proper families, checked L by L in the text, refute every request-counting inequality of the kinds proposed: the request ratio UW(λ) for every λ, U1-type energy bounds for every constant, and union growth. They do so simultaneously on any finite set of shifts. A lifted version has classes and fibres of size span^{1/2-o(1)}, but keeps only part of this. It still refutes UW(λ) for every λ. It refutes the U1-type energy bound only for constants C < 3, and union growth only for f with liminf f > 1/3 (Corollary 2.11). None of these sources can be a diagonal class of a properly four-colored square. Variants that survive: interval averaging with the weights a_h, classes of size near the regime constant times sqrt(span), and fibres near v_l.
  - (D-c) (Section 3). The forced sets are Golomb (Sidon), hence of size at most Q(span), but this costs nothing. An explicit proper family shows that full foreign-request coverage forces no Golomb imbalance. Under near-extremality, a Golomb imbalance is the same thing as a fibre deficit.
  - An exact reduction (Section 4). The per-shift (D-a) clause against certified single-class caps is equivalent, up to an explicit O(S^{-3/8}) term, to the single inequality FD. FD is implied by a single-binary-source deficit. Any violation of FD forces all three classes to be within 3η + O(S^{-3/8}) of the cap, with saturated fibres over all short lags. FD holds, with explicit η, in several structured sub-cases.
- **No new bound on R_4 is claimed.** Section 5 states only the conditional implication.

Labels: **PROVED** means proved in full in this document. **CITED** marks a classical fact quoted by name. **HEURISTIC** marks an estimate that nothing depends on. Small members of every construction in Section 2 and Section 3 were also checked exhaustively by computer against every L; those checks are evidence only, and every claim below is proved by hand in the text. The members checked were:
- a two-shift instance of Theorem 2.6 (k' = 2, r = 1, s = 1; 40 points, 60 L's): proper, with |F_h| = 4, N_e = 4, |R_e| = 1 and Σ m^2 = 16 at both shifts, as predicted;
- the three-copy family of Theorem 2.4 with k = 2, 3, 4 and random admissible f_c: proper;
- the (H)-failure example of Section 2.2: monochromatic, as stated;
- the lifted family of Section 2.3 with (p, r, k, m') = (5,1,1,2), (5,1,2,2), (7,2,1,2): proper, with the counts of Theorem 2.10;
- the family of Theorem 3.2 with k = 1, 2, 3: proper, with X = F_d(D), |F_l(X)| = 2k, A = G_2 and B = G_1;
- the m = 23 datum and the Bose translates of Section 6, and the numerical values in Sections 4-5.

The family of Theorem 3.2 (k = 1, 2, 3: 32, 144 and 336 L's) and the numerics of Sections 4-5 were rechecked independently at the last revision.

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

**Inductive form (PROVED, immediate).** Every L has its corner on a strictly larger diagonal offset than its arms. So χ is proper iff, for every h and every u ∈ F_h(D), the corner color χ(u+h,u) avoids every color e with u ∈ R_e(h). Here R_e(h) depends only on the colors at offsets < h. In particular, given the colors at offsets < h, the cells at offset h can be colored so that every L with corner offset h is non-monochromatic iff R_0(h) ∩ R_1(h) ∩ R_2(h) = ∅. Single-shift counting therefore constrains |F_h(D)| only from below: a large union of requests must fit inside F_h(D).

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
- The binary-source property of each S_e(d). This is (iv.0), i.e. (i) restricted to the L's L(a, d, h') whose two arms lie on the same offset d and in the same class.
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

So any energy bound with C_2 < 3/2 must be color-asymmetric.

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

These instances are not diagonal classes of a four-colored square: a ratio of 240 needs k ≥ 360, so span ≥ B^M with M > 360.

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

So if r_X(l) ≥ (1−ε) v_l, the imbalance is at most Q(S−l) − Q(S−l−1) + ε v_l. Conversely, a forced imbalance lowers r_X(l) below v_l by the same amount.

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
- (c) Each Golomb class is ≤ Q(S−1) ≤ Q(S−2) + 1, and r(l) ≥ (1−β)(Q(S−1) + Q(S−2)). ∎

Combined with Proposition 4.6(b), taking θ = 3η + 2ξ and λ ≈ εS: an FD-violator at level η has, in each of its three classes and at all but a weighted fraction O((η + ε + S^{−3/8})/β) of the lags l ≤ εS, fibres that are unions of two Sidon sets each of size ≥ Q(S−2) − βv_1. (HEURISTIC reading at the regime, with S = 2.2·10^7 and v_1 = 9.4·10^3, using the numerical value K_F/c − 1 ≈ 0.0021 in place of ξ: for η = 0.01, each class must be within about 3.4% of c, i.e. θ ≈ 0.034, and at λ = 0.02 S the bound (a) gives D̄(λ) ≤ about 0.089, i.e. a weighted mean fibre deficit below about 9% over the lags l ≤ 0.02 S. With the proved ξ(S) ≈ 0.0068 instead, the numbers are θ ≈ 0.044 and D̄ ≤ about 0.107.)

**Proposition 4.8 (FD in structured sub-cases). PROVED.**
- (a) **Translation-invariant colorings**, χ(v,u) = φ(v−u). Then F_d(D) = S_{φ(d)}(d) is a single class, so |F_d(D)| ≤ K_F ≤ (1+ξ)c. FD holds with η = (2 − ξ(S_0))/3, for example η = 0.6 for S_0 = 2700.
- (b) **Shifts with a small class.** If some class at shift d has size ≤ (1−θ')c, then |F_d(D)| ≤ (3 − θ' + 2ξ)c, i.e. the shift satisfies FD with η = (θ' − 2ξ)/3. (Contrapositive of 4.6(b).)
- (c) **Difference-colored classes.** Suppose the shifted source of X = S_e(d) is difference-colored: ψ(a,b) = f(b−a). Then each F_l(X) is a single Golomb class, so r_X(l) ≤ Q(S−l) ≤ Q(S−1). The argument of Corollary 4.3 and Lemma 4.4, with v_1 replaced by Q(S−1), gives |X| ≤ (1 + 5S^{−3/8}) sqrt(Q(S−1) S). Since Q(S−1)/v_1 ≤ Q(S−1)/(2Q(S−1) − 1) by (Q-step), this is (1/sqrt 2 + o(1)) c(S). If all three classes at d are difference-colored, FD holds at d with η = 1 − 1/sqrt 2 − o(1) ≈ 0.29.

*Proof of the constant in (c).* sqrt(Q(S−1)S) ≥ sqrt(sqrt((S−1)/8)·S) ≥ S^{3/4}/2 for S ≥ 34. Rerunning Lemma 4.4 gives (S^{3/8}+1)/sqrt(Q(S−1)S) ≤ 4S^{−3/8}, plus S^{−3/8}. ∎

*Remark (PROVED).* For a difference-colored binary source X, properness is equivalent to f(x) = f(y) ≠ f(x+y) for every realized pair (x,y), i.e. every (x,y) with some u such that u, u+x, u+y, u+x+y ∈ X. The case x = y is included. *Proof.* The realized pair (x,y) gives the L L(u, x, x+y), with arm lags x, x and corner lag x+y; the symmetric pair gives arm lags y, y. With two colors, f(x) ≠ f(x+y) and f(y) ≠ f(x+y) force f(x) = f(y). Conversely, every L has this form. ∎ Consequently such an X contains no Hilbert cube u + {0,d_1} + {0,d_2} + {0,d_3}. The pairs (d_1,d_2), (d_1,d_3), (d_2,d_3) and (d_1+d_2, d_3) are all realized at u, which gives f(d_1+d_2) ≠ f(d_1) = f(d_3) = f(d_1+d_2).

---

## 5. Consequence for R_4 (implication only; no bound is claimed)

Suppose FD(η, S_0) holds with explicit η and an explicit S_0 (how small S_0 must be is stated below). Apply it to each D_c (c a main-diagonal color) at every shift d ≤ t−1 = 34,999. Then

  X_d = Σ_c |F_d(D_c)| ≤ 12(1−η) c(n−1−d) + 4S_0,

using that c is nondecreasing. Here:
- D_c, with χ restricted to V(D_c), is a proper ternary source after relabelling the three colors other than c, and span F_d(D_c) ≤ n−1−d.
- The term 4S_0 covers the colors c for which span F_d(D_c) < S_0. Such a set has at most S_0 elements.
- At the regime, 12 c(n−1−d) ≈ 5.45·10^6 (HEURISTIC inputs as in Section 4). So 4S_0 ≤ (η/2)·12c(n−1−d) as soon as S_0 ≤ 6·10^5·η. Then X_d ≤ 12(1−η/2) c(n−1−d). So FD is useful to the consumer only with S_0 well below the spans, not merely below about 2·10^7. This gives the problem's hypothetical saving X_d ≤ (1−δ)U_d only after one more step: certify c(S) ≤ K(S−j) for the consumer's rank caps K at the spans used, with Q replaced by a certified upper bound (replacing Q by an upper bound only enlarges the right side of FD).

The problem's numbers suggest c ≈ 4.55·10^5 against K ≈ 4.58·10^5, a margin of about 0.7%. This is HEURISTIC and must be certified. The margin shrinks to about 0.1% if v_1 is computed from the classical bound Q(m) ≤ sqrt(m) + m^{1/4} + 1 (v_1 ≈ 9,517, c ≈ 4.574·10^5). The loss of staggering (12 distinct minima) is additive and of relative size about 10^{−6}.

With that, δ ≥ η/2 (δ ≥ η − O(S_0/c) in general), and the sensitivity statement of the problem applies: a factor of about 1 − 3.9δ (HYPOTHETICAL).

**Remark (HEURISTIC; a single-class question, outside Part D).** The same numbers place the Fejér cap itself below the consumer's cap: K_F ≈ 4.557·10^5 (computed from v_1 = 9.4·10^3, S = 2.2·10^7) against K ≈ 4.58·10^5, about 0.5% lower. Corollary 4.3 is a valid single-class cap for every class, with Q replaced by any certified upper bound. If, after both caps are recomputed with the same certified Q-bound at the consumer's spans, K_F(S−j) < K(S−j) still holds, then replacing K by min(K, K_F^♯) in U_d is a proportional saving obtained without any cross-class information. This is not established here, and the sign is fragile. Computer evaluation at S = 2.1987·10^7 (HEURISTIC inputs):
- with v_1 = 9,350, 9,400 or 9,450 (the rounding range of "9.4·10^3"), K_F/4.58·10^5 − 1 is about −0.8%, −0.5% and −0.3%;
- with the classical upper bound Q(m) ≤ sqrt(m) + m^{1/4} + 1 (CITED, Erdős–Turán/Lindström type), v_1 ≈ 9,517 and K_F is about 0.1% above 4.58·10^5. K_F^♯ is still 0.03% above it.

So the comparison is decided by which certified Q-bound the consumer's v_l uses, and by the unrounded K. It concerns the binary-source capacity, not the request geometry of Part D.

Nothing in this document proves FD. So nothing here improves R_4.

---

## 6. Other routes (recorded so they are not repeated)

- **Joint fibre and prefix deficits.** The statements MS (a joint prefix deficit of Σ_e r_{S_e(d)}(l) against 3v_l for all λ) and MS' (the same with an additive slack S/100 and S ≥ S_0) were the missing statements of earlier rounds. They are neither proved nor refuted. They were retired, because MS' implies the size deficit Σ_e s_e^2 < 3(1−η) v_1 S, hence FD. The proof is Lemma 4.2 summed over windows. So MS' is no reduction of the goal. A rank-based conversion "prefix deficit δ ⇒ cap loss about δ/2" against the consumer's rank caps was also proved; it is superseded here by the cleaner Fejér route.
- **Lag-by-lag information cannot give a deficit.**
  - For every prime power q ≥ 7 there are six pairwise disjoint Sidon sets of size q in [0, q^2 − 2]. *Proof:* a Bose set A ⊂ Z/(q^2−1) (CITED) has q elements, is Sidon mod q^2−1, and its nonzero differences are exactly the residues not divisible by q+1. So the translates A + j(q+1), 0 ≤ j < q−1, are pairwise disjoint, each is Sidon mod q^2−1, and read as subsets of [0, q^2−2] each is Sidon in Z. (Checked by computer for q = 7.) So "six disjoint Sidon pieces per lag" gives no joint deficit.
  - In the coupled one-lag structure, no single mixed additive-quadruple pattern is forbidden. A single quadruple's constraints are unsatisfiable only when all four points have the same (class, color) type.
  - The single-lag statement TSD (two disjoint Sidon sets A, B whose union carries a proper 2-coloring of its strict source, constant on A-pairs and on B-pairs with different constants, lose a fixed proportion of Q(m) + Q(m−1)) fails at m = 23: A = {0,1,4,13,15,21}, B = {2,5,7,16,22,23} reach 12 = Q(23) + Q(22). (Finite facts, computer-checked, evidence for exactly this instance: A and B are disjoint Sidon sets; there is no 7-element Sidon set in [0,23], so Q(23) = Q(22) = 6; V(A ∪ B) contains 76 L's, and a backtracking search finds a proper 2-coloring with A-pairs 0 and B-pairs 1.) So TSD can hold only asymptotically.
- **Lag-pair counting is balanced (HEURISTIC dead end).** At saturation, parallelogram counts, Sidon agreement bounds, transport and separation (Corollary 1.3) are all met in proportion by random-like colorings. A ±1 sum over all L's reduces to bookkeeping. Energy and Gowers-type counts are consistent at saturation. A proof must be global across lags.
- **Constructions toward a counterexample that fail.**
  - Block-placed and digit-product sources (M·B + R with B Sidon) have joint prefix ratio at most about Q(ρ)/sqrt(M). Base-M products need full-grid 2-colorings and do not raise the exponent above 1/2.
  - Doubling reduces the converse of Proposition 4.6(a) to the square problem.
  - Difference colorings lose a factor 1/sqrt 2 (Proposition 4.8(c)).
  - Row, column and diagonal colorings fail on long progressions.
  - No binary source of size span^{1/2+ε} is known; Sidon sets give about sqrt(span).
- **Necessary size of a counterexample.** Any violation of MS' (and hence any route through it) needs classes of size > S^{5/8}/16. Any violation of FD needs three classes of size about sqrt 2·S^{3/4} (Proposition 4.6).
- **Density.** Modulo the corners theorem (CITED from memory, non-explicit), for fixed ρ > 0 no proper ternary source has D of density ≥ ρ on an interval of length ≥ S(ρ). This is non-explicit and gives no δ.
- **Band lemma (PROVED, no quantitative use found).** At one shift, β(y,a) := χ(a+d, y) for y, a ∈ F_d(D) with a+d > y is a proper 3-coloring of the sparse grid {(a,y) : a > y−d}, whose diagonal classes are the S_e(d). It contains (iv.0) and the cross-class coupling.

---

## 7. What remains open (the gap)

**The open core of Part D is the statement FD(η, S_0)** of Section 4:

> There are explicit η ∈ (0,1) and S_0 such that for every proper ternary source (D,χ) and every d with S = span F_d(D) ≥ S_0,
> |F_d(D)| ≤ 3(1−η) sqrt(v_1 S), with v_1 = Q(S−1) + Q(S−2).

By Theorem 4.5 this is, up to O(S^{−3/8}), the same as the (D-a) clause per shift against the Fejér caps. By Proposition 4.6 it follows from the single-binary-source deficit SCD.

SCD is a statement about binary sources alone: are binary sources of span S bounded by (1−η) sqrt(v_1 S), or even by o(S^{3/4}) or S^{1/2+o(1)}? A negative answer to the existence of binary sources of size S^{1/2+ε} would settle FD with η → 1. SCD improves the binary-source capacity itself, which lies outside this attempt's lane.

What is not done:
- **(D-a): not proved,** in any of the forms requested, per shift or a_h-averaged, with any explicit δ > 0.
- **(D-b) at regime size: not done.** The constructions of Section 2 refute every request-based inequality over arbitrary sources. The lifted family, with classes of size span^{1/2−o(1)}, refutes UW(λ) for every λ, but energy bounds only for C < 3 and union growth only beyond 1/3. In all of them the classes are far below the regime (about 98 sqrt(span)) and below the binary cap. None is a diagonal class of a four-colored square. A refutation of FD would need three disjoint binary sources of size (1−o(1)) sqrt 2·S^{3/4} at one shift. No binary source beyond about sqrt(span) is known.
- **Interval averaging** with the weights a_h is not refuted by any construction here; the counterexample shift sets W are sparse.
- **(D-c) under near-extremality** is equivalent to a fibre deficit (Proposition 3.3), hence again to the open core.
- The consumer comparison c(S) ≤ K(S) at S ≈ 2.2·10^7 needs a numerical certification (Section 5).
- Whether the Fejér cap K_F alone undercuts the consumer's rank cap K, once both use the same certified Q-bound, is unchecked here (Section 5, remark). It is a single-class question.
- Any proof of FD must come with an explicit S_0 well below the spans (S_0 ≤ 6·10^5·η suffices at the regime), because the shifts where F_d(D_c) has span below S_0 enter the consumer as an additive term 4S_0 (Section 5).
- The lifted family of Section 2.3 has no padding. A lifted family that refutes energy bounds with C ≥ 3, or union growth with f ≤ 1/3, at classes of size span^{1/2−o(1)}, is not known (Corollary 2.11).
