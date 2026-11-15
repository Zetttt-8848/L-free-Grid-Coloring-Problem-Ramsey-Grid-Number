kind: attempt

Open question attempted (flagged OPEN by this run, ledger "whether AABA or ABAA mixed quadruples are forbidden", part of the joint-fiber-bound question): Fix d, a lag l, h = d+l and a corner color f. For the two classes e, e' ≠ f, the Golomb pieces G_e^f = {u : u, u+l ∈ S_e(d), chi(u+h,u) = f} and G_{e'}^f are each Sidon, but their union need not be. Consider additive quadruples a, a+r, a+s, a+r+s (0 < r <= s; r = s allowed where it makes sense) inside G_e^f ∪ G_{e'}^f, labelled by class, A = class of a. Settle, for each of the patterns AABA (a, a+r, a+r+s in class e; a+s in class e') and ABAA (a, a+s, a+r+s in class e; a+r in class e'): is it FORBIDDEN in every proper ternary source (give the complete chain of L's), or is it ALLOWED (give an explicit proper ternary source, checkable L by L, that contains it)? Then say what follows for the pair G_e^f, G_{e'}^f.

## Facts you may use (proved earlier in this run; checked)
- Lemma 0. Every directed L inside V(D) is L(u,d,h) for exactly one triple of integers with 1 <= d < h. Its cells are the horizontal end (u+d,u), the corner (u+h,u) and the vertical end (u+h,u+h-d); its arm length is h-d. It lies in V(D) iff u, u+d, u+h-d, u+h all lie in D. Here d ranges over ALL of [1,h-1], including d > h/2 (then u+d > u+h-d). Equivalently: for p0 < p3 in D and an ORDERED pair (x,y) in D with x+y = p0+p3, p0 < x,y < p3, there is the L with cells (x,p0), (p3,p0), (p3,y); when x ≠ y both orders give distinct L's ("mirrored" L's). Every construction must handle both orders.
- (i) L(u,d,h) is monochromatic of color e iff u ∈ F_{h-d}(S_e(d)) ∩ S_e(h). Hence chi is proper iff S_e(h) ∩ R_e(h) = ∅ for all h >= 2 and all e. Equivalently: u ∈ F_{h-d}(S_e(d)) iff the L with corner (u+h,u) has BOTH arm cells of color e, so m_{e,h}(u) counts the L's with corner (u+h,u) whose two arms both have color e.
- (ii) R_e(h) ⊆ F_h(D). (iii) Every u ∈ F_h(D) lies in at most two of R_0(h), R_1(h), R_2(h), and u ∈ R_e(h) ∩ R_{e'}(h), e ≠ e', forces u ∈ S_{e''}(h). Sharp identity: sum_e |R_e(h)| = 2|F_h(D)| - 2#{u in no R_e(h)} - #{u in exactly one}.
- Row/column form of properness (immediate from Lemma 0): for u < v in D with h = v-u, write w_u(x) = chi(u+x,u) (row word of u) and c_v(x) = chi(v,v-x) (column word of v). Then chi is proper iff, for all such u,v and every d in (0,h) with u+d, v-d in D, NOT w_u(d) = c_v(d) = w_u(h). (Note w_u(h) = c_v(h) is the shared corner cell.)

## The single-class Golomb split, quoted verbatim from an earlier answer in this run (checked)
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

## What is known about the six pieces (quoted from the previous query of this run)
Fix d, l, h = d+l. For e ≠ f put G_e^f = F_l(S_e(d)) ∩ S_f(h) = {u : u, u+l ∈ S_e(d), chi(u+h,u) = f}.
- The six pieces are pairwise disjoint subsets of F_h(D). Their total is sum_e r_{S_e(d)}(l), which is the lag-l agreement count of the 3-colored word z_d(u) = chi(u+d,u) on F_d(D).
- Each piece is Sidon (quote above).
- The two pieces with the same corner color f, coming from the two classes e ≠ f, both lie in S_f(h). Their UNION need NOT be Sidon. Explicit proper witness: D = [0,10), where row u lists chi(v,u) for v = u+1,...,9:
  u=0: 2 0 0 2 2 1 1 2 1; u=1: 2 2 2 1 0 0 1 0; u=2: 1 0 2 1 1 0 2; u=3: 1 0 1 2 0 2; u=4: 1 0 1 0 1; u=5: 2 0 2 0; u=6: 2 1 0; u=7: 0 2; u=8: 2.
  With d = 1, l = 1, f = 0, the starts 0, 2, 3, 5 lie in classes 2, 1, 1, 2 and satisfy 0+5 = 2+3.
- Evidence only (random proper sources on [0,n), n <= 16). Consider additive quadruples a, a+r, a+s, a+r+s (0 < r <= s) inside G_e^f ∪ G_{e'}^f, labelled by class, with A = the class of a. The observed patterns were ABBA 22, AAAB 18, ABBB 13, AABB 4, ABAB 1. No AABA or ABAA occurred; AAAA is impossible.
  Partial forcing seen at the planning step, for the pattern AABB (a, a+r in class e; a+s, a+r+s in class e'; corner color f):
  - L(a,h,h+r) gives chi(a+h+r,a) ≠ f, and since a, a+r+l ∈ S_e(d) it is ≠ e. So it equals e'.
  - Likewise chi(a+s+h+r, a+s) = e.
  - These differ, so the single-class closing step (L3 in the quote) does not apply.

## Partial forcing proved in the previous round (quoted verbatim from its answer; checked by hand at the planning step)
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

## Task
1. AABA. All cells of the corner triangle of the quadruple are forced above. Push the forcing further: use L's whose cells are corner cells C(p,q) = (q+h,p) for p,q in the quadruple, cells (p+h,p), the shifted-source cells (q+l+d,p) with p,q+l ∈ S_e(d) (which avoid e by (iv.0)), the cells (p+d,p) and (p+h,p+l) (color = class of p), and L's with arm lengths l, d, r, s, s-r, r+s, h+r, h+s. Either derive a monochromatic L (pattern forbidden), or give an explicit proper ternary source containing the pattern. An explicit witness may be small (e.g. D an interval [0,n) with n <= 20, chi given as rows u: chi(u+1,u), ..., chi(n-1,u)), but then you must yourself verify properness L by L and say how; preferably give a structured witness whose properness you prove.
2. ABAA (r < s, and if relevant r = s): the same, starting from Lemma F (pairs (a,a+s), (a,a+r+s), (a+s,a+r+s) are same-class pairs, so their corner cells are e').
3. Also settle AAAB only if it falls out of the same analysis (it is believed allowed; a witness would be welcome).
4. Consequence. If AABA and ABAA are both forbidden, the additive quadruples of G_e^f ∪ G_{e'}^f are only of the shapes ABBA, AABB, ABAB, ABBB, AAAB (up to relabelling). Prove the strongest bound you can on |G_e^f| + |G_{e'}^f| within a span S, with explicit constants, and state whether it beats 2Q(S) (Q = Sidon cap ≈ sqrt(S)) by a proportional factor. Caution: two Sidon sets whose positive-difference sets are disjoint can still have total size about 2 sqrt(S) by plain counting (C(a,2)+C(b,2) <= S), so a saving needs a finer argument; if you invoke an Erdos-Turan-type interval count, prove it in full.

Rules: every proof complete and from the cell coordinates; every counterexample explicit and checkable L by L (both orders of every middle pair); finite computations are evidence only for exactly what they check. Do not import three-color facts. End with the exact statements proved, refuted, and still open.
