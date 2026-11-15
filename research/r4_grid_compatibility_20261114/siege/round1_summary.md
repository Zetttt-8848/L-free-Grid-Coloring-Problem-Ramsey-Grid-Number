# Round 1 summary (written at the round-1 plan step; no worker results yet)

## Goal (ledger entry 1, OPEN)
P1 (i)-(v) exactly as posed, plus Part D settled at level (D-a) [explicit-delta proportional-loss inequality, hypotheses named] or (D-b) [explicit checkable family of proper ternary sources showing no request-based inequality of that kind can hold]. (D-c), the forced-color alternative, is tracked as a separate OPEN line (entry 6), not part of the goal.

## Established so far
- Nothing from worker files yet (round 1).
- Independently re-checked at the plan step (Python, every L of V(D)): the two pre-registered witnesses in d1/d1_search_seed20261114.json are proper and have the stated counts. U1 witness D=[0,14), h=5: per color (N, sum m^2, |support|) = (4,4,4), (4,16,1), (6,10,4), |F_5|=9. UW(1) witness D=[0,18), h=15: (5,13,2) for each color, |F_15|=3. The search (8,425 proper colorings, 600 s) had max U1 ratio 2.77 and max min_e N_e/|F_h| ratio 5/3. Ledger entries 3, 4 (REFUTED).

## Plan-step observations (mine; elementary, to be confirmed by round1_q1's written proofs)
- Parametrisation of every L in V(D): (u,d,h), 1<=d<h, cells (u+d,u) left, (u+h,u) corner, (u+h,u+h-d) up, arm length h-d; inside V(D) iff u, u+d, u+h-d, u+h in D; monochromatic e iff u in S_e(d) ∩ (S_e(d) - (h-d)) ∩ S_e(h). This gives P1(i) both directions, (ii), and (iii) (a start in all three R_e has no admissible corner color). For a PROPER source sum_e |R_e(h)| <= 2|F_h(D)| is automatic, so (D-b) only needs properness plus a large ratio N_e(h)/|F_h(D)| for all three e.
- (iv) containment of foreign-requested starts in one Golomb class is immediate; hence F_l(X) ∩ R_{e'}(h) is Sidon trivially (subset of a Sidon set). The substantive D-c question is imbalance, which pure containment cannot give.
- Corner/arm language: m_{e,h}(u) = #{d<h : chi(u+d,u) = e = chi(u+h,u+h-d)}, the e-agreements between row word of u and reflected column word of u+h. Properness: agreement colors at each corner avoid the corner color.
- Global identity: sum_{h} N_e(h) = sum_d C(|S_e(d)|,2); total request mass is forced by the fiber sizes of D (convexity over e).
- Heuristic regime analysis (NOT theorems): K ~ sqrt(2) L^{3/4} from the rank-neighbor inequality with v_l ~ 2 sqrt(L); near-cap classes behave like density ~1/48 sets with uniform fibers and near-maximal Sidon Golomb classes; each request set has relative density ~1/146 in F_h(D); random-like behaviour would cover F_h(D) for every color once h >> 146, impossible; so the regime forces typical multiplicity m >= ~h/97 on requested starts. A loss must come from proving such concentration impossible (anti-collision), or one must show it is possible (D-b).
- Trivial energy bounds give only |R_e(h)| >~ 2Q; U1-type pointwise energy bounds are false; any valid lemma must use near-extremal structure or average over h and tolerate small/boundary effects.
- Context: the only known lower bound is R_4 >= 21, so regime-scale explicit constructions are not to be expected; a (D-b) answer must be a scaling family.

## Dead ends
- U1 (pointwise energy with constant 3/2) and UW(1): refuted by explicit witnesses (entries 3, 4).

## Open gaps between the current state and the goal
1. Written, checkable proofs of P1 (entry 2).
2. Is min_e N_e(h)/|F_h(D)| bounded by an absolute constant (UW(lambda))? A family with ratio -> infinity would be (D-b)-type evidence and kill UW for all lambda; a bound would be a strong (D-a) (entry 5).
3. Anti-collision under a named near-extremality hypothesis (entry 7).
4. Window-averaged energy/union-growth inequality (entry 8).
5. D-c imbalance (entry 6).

## Round 1 wave (composed at this step; all four are attempt queries)
- round1_q1: complete proofs of P1 (i)-(v) (including checking whether the (iii) correction term is right) plus D-c (imbalance).
- round1_q2: UW(lambda) dichotomy: explicit family with ratio -> infinity (digit/lexicographic constructions suggested) or a proof of boundedness; square-embedding check and list of killed/surviving variants.
- round1_q3: D-a under named near-extremality H(eta): anti-collision via rigidity of near-maximal Sidon sets; quoted rank-neighbor inequality inline.
- round1_q4: D-a window-averaged: request budget/energy over h windows, using the forced global mass identity and the L's linking two agreements at one corner.

## Where the next round should concentrate
Read the four answers. If q1 gives complete P1 proofs, record PROVED and keep for proof assembly (it is part of the goal, so it needs the audit too once a Part D settlement exists). Then exploit whichever Part D route made real progress: a family from q2 (then verify properness and check what it kills), or a concrete anti-collision/energy lemma from q3/q4 (then push it to explicit delta and verify). If all Part D routes stall, try a fresh lens (e.g. structure of the row/column agreement matrix as a 2-dimensional object, or reducing to a statement about binary sources alone).
