# round2_q4: joint fiber bound for the three completion classes at one shift

Status summary: PARTIAL. Proved: the exact consumer deduction (Task 4, conditional on a joint
bound), and forced corner colours for the mixed patterns AAAB, AABB, AABA. NOT proved: no mixed
pattern is shown forbidden. No joint bound w_l <= (1-delta)3v_l is established, and none is
refuted. The main question stays OPEN.

Notation: d, l, h = d+l are fixed. A point u in piece G_e^f satisfies u, u+l in S_e(d) and chi(u+h,u)=f.
L(u,x,y) has horizontal end (u+x,u), corner (u+y,u) and vertical end (u+y,u+y-x) (Lemma 0).

## Basic forcing lemma (proved)
**Lemma F.** Let p < q be points in pieces with the same corner colour f, with p in class e and q in class e_q.
Then the cell C(p,q) = (q+h, p) is the corner of L(p,h,h+q-p). Its two ends are (p+h,p) and (q+h,q), and both
have colour f. So chi(C(p,q)) != f. If moreover e_q = e, then p and q+l are both in S_e(d). So
C(p,q) = (q+l+d, p) is a cell of the d-shifted source of S_e(d), and by (iv.0) it is != e.
Hence C(p,q) is the third colour. ∎

## Task 1: mixed quadruples a, a+r, a+s, a+r+s (0<r<=s), all with corner colour f
- **AAAA** is forbidden (single-class proof, quoted).
- **AAAB** (the first three points in class e, the last in class e'): Lemma F gives C(a,a+r) = C(a,a+s) = C(a+r,a+s) = e'
  (the third pair needs r<s). The single-class closing step needs C(a+s,a+r+s), which is
  unavailable. In the evidence this pattern occurred 18 times, so it is presumably allowed. No witness is extracted here.
- **AABB**: C(a,a+r) = e' and C(a+s,a+r+s) = e. These differ, so L3 does not close. The evidence
  lists 4 occurrences.
- **AABA** (the points a, a+r, a+r+s in class e and a+s in class e'): Lemma F gives C(a,a+r) = C(a,a+r+s) = C(a+r,a+r+s) = e'
  (the last uses r<s or r=s). Then:
  - L(a,h+r,h+r+s) has ends C(a,a+r)=e' and vertical end (a+h+r+s, a+s). Its corner is C(a,a+r+s)=e'.
    So (a+h+r+s,a+s) != e'.
  - That cell is C(a+s,a+r+s), and by the first half of Lemma F it is != f. Hence it is e.
  - L(a,h+s,h+r+s) has ends (a+h+s,a) and (a+h+r+s,a+r)=C(a+r,a+r+s)=e', and its corner is e'. So C(a,a+s) != e'.
    By Lemma F, C(a,a+s) is also != f. Hence C(a,a+s) = e.

  So every cell of the quadruple's corner triangle has a forced colour. I did not find a monochromatic L
  among these cells and the d-cells. Whether AABA is forbidden (it was not observed, which is suggestive) is **OPEN**.
- ABAA, ABBA, ABAB, ABBB: not analysed beyond Lemma F. ABBA, ABAB and ABBB were observed, so they are presumably allowed. ABAA was not observed; it is OPEN.

## Task 2/3
No forbidden mixed pattern is proved, so no joint additive-energy argument is available.
As the task's caution notes, the disjointness of difference sets alone gives no saving. **OPEN.**

The hypothesis that would rescue the bound is the following. If AABA and ABAA (and their analogues) were forbidden,
then within G_e^f ∪ G_{e'}^f every additive quadruple would have at most one point from one class
in a constrained position. Turning that into a quantitative saving would still need an Erdos-Turan-type
interval count. I have no explicit delta for it.

## Task 4: the consumer deduction (proved, conditional)
Let the three classes X_e = S_e(d) have sizes s_e and spans <= L'. Use a common rank c < min s_e.
The rank-neighbour inequality for each class gives
2 Σ_sel(X_e) + 4Σ_i(c-i)e_{i+1} <= L'c(c+1), where Σ_sel(X_e) is the sum of the selected differences.
The selected differences of X_e at lag l are pairs in X_e at distance l, at most r_{X_e}(l) of them.
So the union multiset (over e) of selected differences has multiplicity at lag l at most
w_l := Σ_e r_{X_e}(l). Its cardinality is H_tot = Σ_e (c s_e - c(c+1)/2). Hence
Σ_e Σ_sel(X_e) >= P(H_tot; w). Summing over e gives
**2P(H_tot; w) + 12Σ_i(c-i)e_{i+1} <= 3L'c(c+1)**, which is valid for unequal sizes.
If a joint bound w_l <= (1-delta)3v_l holds on all lags used, then P(H_tot; w) >= P(H_tot; (1-delta)·3v).
Since P is evaluated on a thinner multiset, it grows. This caps Σ_e s_e, and so it lowers the per-main-colour
triple inside U_d = Σ_{12 classes} K. Here U_d must be replaced by Σ_c(joint cap of the triple at main colour c).
In the sensitivity model this is exactly the X_d <= (1-delta')U_d input. The size of delta' as a function of delta was not computed.

## Open
1. Is AABA (or ABAA) forbidden?
2. Is there any joint bound Σ_e r_{S_e(d)}(l) <= (1-delta)3v_l?
3. Can explicit witnesses be given for AAAB, AABB, ABBA, ABAB and ABBB? (They are only observed in random search, which is evidence only.)

=== END OF ANSWER round2_q4 ===
