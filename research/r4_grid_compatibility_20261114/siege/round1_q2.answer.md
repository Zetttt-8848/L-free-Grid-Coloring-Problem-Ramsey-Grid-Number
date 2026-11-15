# round1_q2: the request ratio of a ternary source is unbounded (route (A), proved)

## Summary
PROVED: for every k >= 2 there is an explicit proper ternary source (D_k, chi_k) and a shift h with |F_h(D_k)| = 3 and N_e(h) >= k-1 for all three e. So UW(lambda) fails for every lambda. Variants give energy and union-growth counterexamples. The family is sparse, and it works at only one shift h per source. "Positive proportion of h" and "dense D" are left OPEN. It cannot sit inside a four-colored square once its span is at least R_4.

## 0. Fact 1 (parametrisation; proof)
A directed L in V(D) has the form (v,w),(v+t,w),(v+t,w+t). Write w=u, v=u+d, h=d+t. The cells are left (u+d,u), corner (u+h,u), up (u+h,u+h-d), with arm length t=h-d, and 1<=d<h. All three cells lie in V(D) iff u, u+d, u+h-d, u+h are in D. (The strictness conditions u<u+d, u<u+h, u+h-d<u+h hold automatically.) The L is monochromatic in e iff u in S_e(d), u+(h-d) in S_e(d) (since chi(u+h,u+h-d) = chi((u+h-d)+d, u+h-d)), and u in S_e(h). This is exactly u in F_{h-d}(S_e(d)) ∩ S_e(h).
Hence chi is proper iff S_e(h) ∩ R_e(h) = ∅ for all e and h.
If u were in all three R_e(h), the corner color chi(u+h,u) = e would put u in S_e(h) ∩ R_e(h). So for proper chi, u lies in at most two R_e(h), and sum_e |R_e(h)| <= 2|F_h(D)|. Also R_e(h) ⊆ F_h(D), because u, u+h are in D.
In D-terms: an L is a 4-tuple p0<p1<=p2<p3 in D with p0+p3 = p1+p2, where u=p0, d=p1-p0, h=p3-p0.

## 1. Construction
Fix k >= 2 and base B = 100. Define the following.
- Atoms a_{j,i} = B^{jk+i} for j in {0,1,2} and i = 1..k. Set A_j = {a_{j,1},...,a_{j,k}} and A_j^0 = A_j ∪ {0}.
- h = B^{3k+1}.
- T_j = t_j B^{3k+3}, with (t_0,t_1,t_2) = (0,1,3). This is a Sidon triple.
- E_j = A_j^0 ∪ (h - A_j^0), and D = ∪_j (T_j + E_j).

Coloring chi on V(D):
- corner cells C_j(a) = (T_j+h-a, T_j+a), for a in A_j^0, get color j;
- for a<b in A_j^0, the left cell (T_j+b, T_j+a) and the up cell (T_j+h-a, T_j+h-b) both get color f_j(a,b) in P\{j}, chosen freely (fixed below);
- every other cell of V(D) gets color 0.
These cell types are pairwise distinct: they are small-small, large-large and small-large inside one copy, and the cross-copy cells are separate again.

## 2. Lemma (all L's of V(D)). Proof
Each element of D is T_j + αh + σ·(atom or 0), with α in {0,1} and σ in {+1,-1}.
p0+p3-p1-p2 = 0 is then an integer combination of distinct powers of B with coefficients of absolute value at most 6 < B/2. Hence every coefficient vanishes. (Look at the lowest nonzero coefficient c_m: the sum is ≡ c_m B^m, which is ≢ 0 mod B^{m+1}.) The cases are as follows.

(T-part) t_{j0}+t_{j3} = t_{j1}+t_{j2}. Since {0,1,3} is Sidon, {j0,j3} = {j1,j2} as multisets. Copies are ordered by T, and consecutive copies are separated by more than the copy diameter (B^{3k+3} > 2h). So either all four points lie in one copy, or j0<j3, p1 lies in copy j0 and p2 lies in copy j3 (p1<=p2).

(Same copy j, offsets x_i in E_j.) Call x "small" if x is in A_j^0 and "large" if x is in h-A_j^0. Every small offset is less than every large one.
- All four small: atom vectors give multiset {x0,x3} = {x1,x2}, which contradicts x0<x1<=x2<x3.
- All four large: the same argument applied to h-x.
- Otherwise the h-coefficients force x0 small, x3 large, and exactly one of x1,x2 large; so x1 is small and x2 large. Write x2 = h-q2 and x3 = h-q3. The atoms give {x0,q2} = {x1,q3}, and x0 ≠ x1, so q3 = x0 and q2 = x1.
- So the L's in a copy are exactly: for a<b in A_j^0, left (T_j+b,T_j+a), corner C_j(a), up (T_j+h-a,T_j+h-b).

(Cross copies j0<j3.) Here x1-x0 = x3-x2 > 0. The atom part of the left side is in copy j0's atoms and that of the right side is in copy j3's atoms, so both vanish. Elements of E_j with equal atom part and different value are only 0 and h. So x0 = x2 = 0 and x1 = x3 = h. The L is left (T_{j0}+h,T_{j0}) = C_{j0}(0), color j0, and up (T_{j3}+h,T_{j3}) = C_{j3}(0), color j3 ≠ j0. It is not monochromatic.

**Properness.** A same-copy L has corner color j and left color f_j ≠ j. A cross-copy L has two different colors. So chi is proper for every choice of the f_j. ∎

## 3. Counts at shift h
F_h(D) = {T_0,T_1,T_2}.
- Within a copy, x and x+h both in E_j forces x = 0, by comparing h-coefficients and atoms.
- Between copies, the gap exceeds h.

The L's with span h are the same-copy L's with a = 0 (span h-2a). So m_{e,h}(T_j) = #{b in A_j : f_j(0,b) = e} for e ≠ j, and m_{j,h}(T_j) = 0.

- (Balanced choice) Alternate f_j(0,·) between the two colors ≠ j. Then N_e(h) >= 2⌊k/2⌋ >= k-1 for every e, while |F_h| = 3. The ratio is at least (k-1)/3 → ∞. **UW(lambda) is false for every lambda.** The excess is not small-count: N_e/|F_h| itself is unbounded.
- (Cyclic choice) Use f_0(0,·) ≡ 1, f_1(0,·) ≡ 2, f_2(0,·) ≡ 0. Then for each e, N_e(h) = k, carried by one start, so |R_e(h)| = 1 = |F_h|/3, and sum_u m² = k².
- (Padding) Add q-3 further copies T_j + {0,h}. For these, A_j = ∅; take t_j from a Sidon set of size q and B large enough that the coefficient bound stays below B/2. The same proof applies. These copies add q-3 starts with no requests. With the cyclic choice: |F_h| = q, N_e = k, sum m² = k². Taking q = k, the bound C(N + N²/|F_h|) = 2Ck is less than k² once k > 2C. **Every energy bound of the U1 form, for every C, is false.**
- **Union growth.** |R_e(h)| >= f(N_e/|F_h|)·|F_h| fails for any f with lim f > 1/q. With padding this rules out any positive limit.

## 4. Square embedding and survivors
- **Embedding.** The span of D_k is about 3·100^{3k+3}. A diagonal class of a proper four-colored [0,n)^2 has span < n < R_4 (which is finite, about 2.2·10^7 by the outer inequality). So D_k cannot be a diagonal class once its span is at least R_4. In fact no family whose span tends to infinity can be one. The counterexamples therefore refute only the "every ternary source" versions.
- **What survives.**
  - Inequalities that use density or near-extremal size hypotheses. Examples: |S_e(d)| close to K(span), or r_{S_e(d)}(l) close to v_l for many l, together with |F_h(D)| comparable to the span.
  - Window-averaged statements over h. Here, for h' ≠ h, every span-h' corner belongs to at most one a, and each such corner has a single corner color.
  - Bounds using the near-extremality hypothesis "N_e(h)/|F_h| ≈ h/146 for a positive proportion of h".
  
  D_k has density → 0, |F_h| = 3, and ratio about k = O(log span). It is nowhere near the regime.

## 5. Status
PROVED:
- Fact 1 (exact reformulation, containment, at most two of three, sum_e |R_e| <= 2|F_h|).
- Lemma 2 (all L's of D_k) and properness of chi_k.
- The counts of §3.
- The negation of UW(lambda) for every lambda, of U1-type energy bounds for every C, and of union growth with any positive limit, all over arbitrary ternary sources.

OPEN:
- (O1) A family with min_e N_e(h)/|F_h| → ∞ for a positive proportion of h in a growing window, or with D of positive density.
- (O2) UW or energy bounds under density or near-cap hypotheses (the regime of the problem). The present construction says nothing about them.
- (O3) The forced-color alternative (D-c) was not addressed here.

No statement about R_4 is made.

=== END OF ANSWER round1_q2 ===
