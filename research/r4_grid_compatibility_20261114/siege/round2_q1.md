kind: attempt

Open question attempted (flagged OPEN by this run): Part (D-b), and the question whether min_e N_e(h)/|F_h(D)| is bounded by an absolute constant (UW(lambda)). Specifically: (1) give a complete, corrected proof that a repaired digit family is proper and has min_e N_e(h)/|F_h(D)| -> infinity; (2) then construct an explicit family in which the ratio is large for all three colors simultaneously on MANY shifts h (a positive proportion of a growing window of shifts), with |F_h(D)| -> infinity, again with a complete properness proof covering every L.

## Facts you may use (proved earlier in this run)
- Every directed L in V(D) is L(u,d,h) for exactly one triple of integers with 1 <= d < h. Its cells are the horizontal end (u+d,u), the corner (u+h,u) and the vertical end (u+h,u+h-d), with arm length h-d. It lies in V(D) iff u, u+d, u+h-d, u+h are all in D. IMPORTANT: d ranges over ALL of [1,h-1]. So for four points p0 < p3 of D and a middle pair {p1,p2} of D with p0+p3 = p1+p2 and p1 ≠ p2, there are TWO L's: one with horizontal end (p1,p0) and vertical end (p3,p2), and one with horizontal end (p2,p0) and vertical end (p3,p1). Both have corner (p3,p0). When p1 = p2 there is one L.
- chi is proper iff S_e(h) ∩ R_e(h) = ∅ for all h, e. R_e(h) ⊆ F_h(D). Each start lies in at most two R_e(h), so for proper chi, sum_e |R_e(h)| <= 2|F_h(D)| holds automatically.

## A previous attempt, quoted verbatim (it contains an ERROR, explained after the quote)
--- begin quote ---
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

--- end quote ---

## The error, and a repair that has passed a finite check (not yet proved)
The quoted lemma treats an L as a 4-tuple p0 < p1 <= p2 < p3. It therefore misses every L with d > h/2, i.e. the L whose horizontal end is (p2,p0) and whose vertical end is (p3,p1). As written, the coloring is NOT proper. An exhaustive check over all 4-point additive relations in D finds 6 monochromatic L's at k=2, 9 at k=3 and 13 at k=4. They are of two kinds.
- Same copy j, for a < b in A_j^0: horizontal end (T_j+h-b, T_j+a), corner C_j(a) of color j, vertical end (T_j+h-a, T_j+b). Both arm cells are "other cells" of color 0, so for j = 0 this L is monochromatic.
- Across copies j < j': horizontal end (T_j', T_j), corner (T_j'+h, T_j), vertical end (T_j'+h, T_j+h). All three cells have color 0.

Proposed repair:
- color every mirror cell M_j(x,y) = (T_j+h-x, T_j+y), with x ≠ y in A_j^0, by j+1 mod 3 (the corner cells C_j(a) = M_j(a,a) keep color j);
- color every cross corner (T_j'+h, T_j), j < j', by 1;
- leave everything else as in the quote.

An exhaustive computer check of all L's for k = 2,...,6, with both the balanced and the cyclic choice of f_j, found NO monochromatic L. It found |F_h| = 3 and N_e(h) >= k for every e. This is evidence only. Note that the repair changes the counts: the mirrored L's with a = 0 add k requests of color j+1 at the start T_j.

## Task
1. Write a complete proof, from the definitions, that the repaired family is proper for every k >= 2. List ALL L's of V(D), including the mirrored ones and all cross-copy ones, and justify the base-B coefficient argument (check that the coefficient bound really is < B/2 for every relation used). Compute N_e(h), |R_e(h)| and sum_u m_{e,h}(u)^2 exactly, for the balanced choice, the cyclic choice and the padded variant. Conclude, or correct, the statements:
   - "UW(lambda) fails for every lambda";
   - "for every C, the energy bound sum_u m^2 <= C(N + N^2/|F_h|) fails";
   - "no union-growth bound |R_e(h)| >= f(N_e/|F_h|)|F_h| with lim f > 0 holds".
   If you find the repair itself wrong, give a different explicit proper family with the same features and a full proof.
2. Main task (D-b, many shifts). Construct, for every k, an explicit proper ternary source and a window W of shifts with |W| -> infinity, in which for at least half of the h in W (or for all of them):
   - min_e N_e(h) >= k |F_h(D)|;
   - |F_h(D)| >= k.
   Sum over h in W too, so that the window-averaged versions of UW and of the energy bound are also refuted. Suggested route: superpose many copies of a single-shift gadget, with shifts h_1, ..., h_m drawn from a Sidon-type set of large powers of B. Alternatively, nest the atoms so that one copy serves many shifts. Control every additive relation p0+p3 = p1+p2 in D, and prove properness for every L, mirrored ones included.
3. Say precisely which variants of Part (D-a) survive your family, and which are killed. Examples: inequalities with a density hypothesis; with class sizes |S_e(d)| >= c * span^alpha for some alpha; with fiber multiplicities r_{S_e(d)}(l) >= rho for many l; window-averaged ones. Give, for your family, the class sizes |S_e(d)|, the largest fiber multiplicities r_{S_e(d)}(l), and the span, so that the distance to the regime is explicit. If you can, push one structural parameter towards the regime: for instance fibers r_{S_e(d)}(l) >= 2 for many l, or class sizes polynomial in log(span). Or prove that digit-type designs, where the only additive relations are designed ones, cannot do this.
4. Embedding: can a member of your family be a diagonal class D_c of a proper four-coloring of some square? Note that this needs the span to be below R_4 (finite, at most about 2.2*10^7), and that the full square's other cells must be colorable. Answer as far as you can prove.

Rules: every claimed counterexample must be an explicit object, with a proof that covers every L of V(D). Finite computations count only as evidence. End with a list of the exact statements you proved, and of what stays open.
