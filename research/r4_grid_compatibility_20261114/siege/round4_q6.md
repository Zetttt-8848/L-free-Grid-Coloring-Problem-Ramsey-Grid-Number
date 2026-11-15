kind: attempt

Open question attempted (flagged OPEN by this run, ledger entry 41): the missing statement MS below. You get only the statement and the statements of the results it is meant to combine with - no proofs, no suggested mechanism - on purpose.

Task, in order:
(A) Derive for yourself whether MS, together with the facts listed below, would settle Part D of the problem at level (D-a) - i.e. give sum_e |S_e(d)| <= (1-delta')(sum of the three separate binary-source caps) with an explicit delta' > 0 for every proper ternary source. Write the derivation out. If it does not go through, or MS looks implausible (false, or vacuous, or not what the consumer needs), say exactly why; that is a result.
(B) Then attack MS - prove it with an explicit delta, or refute it by an explicit, L-by-L checkable counterexample family - by a FIRST MOVE none of the following earlier attempts used: classifying mixed additive quadruples (AABA, ABAA, ...) in the union of Golomb pieces and forbidding patterns by explicit L's; request-energy (sum of squared request multiplicities) bounds; union growth of the request sets R_e(h) under near-extremality hypotheses; a corner-exclusion "independent row and column words agree at rate 2/9" heuristic; density/corners-theorem arguments; sparse digit or product (fine Sidon lifting) constructions. Name your first move at the start. Examples of moves not yet used (you need not pick one of these): an entropy or flag-algebra-type inequality on the colored triangle over F_d(D); a rank or linear-algebra argument on the three class indicator vectors; an induction on S using the hereditary structure of binary sources; an extremal-structure (stability) theorem for near-maximal Sidon sets applied to the six pieces; a search-guided explicit construction at small S with a ratio near 1, generalized and proved.
A proof for only part of the cases MS covers does not answer the question, though it should be reported if it is all you found.

**Missing statement (MS).** Let Q(m), for m >= 0, be the largest size of a Sidon set (no a+b = c+d except trivially, 3-term progressions included) contained in m+1 consecutive integers, and put Q(m) = 0 for m < 0. Then there is an explicit absolute constant delta > 0 such that the following holds for every proper ternary source (D, chi), i.e. every finite set D of integers with a coloring chi of V(D) = {(v,u) : u < v, u,v in D} by P = {0,1,2} having no monochromatic directed L (x,y),(x+t,y),(x+t,y+t), t > 0. For every d >= 1 with F_d(D) nonempty, write
- S = max F_d(D) - min F_d(D);
- v_l = Q(S-l) + Q(S-l-1), the per-class fiber cap of the consumer;
- S_e(d) = {u in F_d(D) : chi(u+d,u) = e};
- r_X(l) = #{u in X : u+l in X}.

Then for every integer lambda with 1 <= lambda <= S,

    sum_{l=1}^{lambda} sum_{e in P} r_{S_e(d)}(l)  <=  (1-delta) * sum_{l=1}^{lambda} 3 v_l.

Equivalently: the lag-l agreement counts of the 3-colored word z_d(u) = chi(u+d,u) on F_d(D), summed over l <= lambda, fall a fixed proportion short of three times the summed single-class caps. (Each single class satisfies r_{S_e(d)}(l) <= v_l, by the Golomb split below, so the statement asks that the three classes cannot be jointly saturated, in the prefix-averaged sense, for any lambda.) For small S it holds trivially (r_{F_d(D)}(l) <= S-l+1 is far below 3v_l); its content is at large S, in particular at the scale S ~ 2.2*10^7 of the problem.

## Statements you may use (all proved earlier in this run; statements only)
- Lemma 0. Every directed L inside V(D) is L(u,d,h) for exactly one triple with 1 <= d < h: horizontal end (u+d,u), corner (u+h,u), vertical end (u+h,u+h-d), arm length h-d; it lies in V(D) iff u, u+d, u+h-d, u+h are in D (d ranges over all of [1,h-1]).
- P1 (i): L(u,d,h) is monochromatic of color e iff u ∈ F_{h-d}(S_e(d)) ∩ S_e(h); chi is proper iff S_e(h) ∩ R_e(h) = ∅ for all h, e. (ii) R_e(h) ⊆ F_h(D). (iii) Every u ∈ F_h(D) lies in at most two of R_0(h), R_1(h), R_2(h), and u ∈ R_e ∩ R_{e'} (e != e') forces u ∈ S_{e''}(h).
- P1 (iv), binary source and Golomb split: for X = S_e(d) and a < b in X, chi(b+d,a) != e (so X has a properly two-colored strict source shifted by d); for l >= 1 and h = d+l, F_l(X) ⊆ R_e(h), and F_l(X) splits by the color f = chi(u+h,u) in P\{e} into two Sidon sets (3-term progressions excluded) G_e^f(l) = F_l(X) ∩ S_f(h). Hence r_X(l) <= v_l.
- Lemma F: for p < q in pieces at the same (d,l) with the same corner color f, chi(q+h,p) != f; if p, q are in the same class e it is the third color.
- The union G_e^f ∪ G_{e'}^f of the two same-corner-color pieces need not be Sidon (explicit witness).
- Rank-neighbor inequality (the consumer's tool): for a member b_1 < ... < b_s of span L of a hereditary family in which a member with j marks has span >= e_j, any 1 <= c < s, H = cs - c(c+1)/2, and multiplicity caps v_h on positive differences, with P(H;v) = sum of the H cheapest terms of the multiset with v_h copies of h: 2P(H;v) + 4 sum_{i=0}^{c-1} (c-i) e_{i+1} <= L c(c+1). The binary-source cap K(L) is certified from this.
- Summed over the three classes S_e(d) (sizes s_e, spans <= S, common rank c < min s_e): 2P(H_tot; w) + 12 sum_i (c-i) e_{i+1} <= 3 S c(c+1), with H_tot = sum_e (c s_e - c(c+1)/2) and w_l = sum_e r_{S_e(d)}(l).
- Prefix formula: P(H;w) = sum_{lambda>=0} max(0, H - C_w(lambda)), C_w(lambda) = sum_{l<=lambda} w_l; hence C_w <= C_{w'} pointwise implies P(H;w) >= P(H;w').
- Color Cauchy-Schwarz: for Y = F_d(D), w >= 0 on [1,t], a_k = sum_i w_i w_{i+|k|}: sum_k a_k r_Y(k) <= 3 sum_e sum_k a_k r_{S_e(d)}(k) (r_X(0) = |X|, r_X(-k) = r_X(k)).
- Explicit sparse proper families show that per-shift request inequalities (min_e N_e(h) <= lambda|F_h(D)|, request-energy bounds, union growth) fail over arbitrary sources; their fibers are far below v_l, so they do not touch MS.

## Rules
Every proof complete; every counterexample explicit and checkable L by L; finite computations are evidence only; do not import three-color facts; no claim about R_4 except as an implication from stated hypotheses. End with the exact statements proved and what stays open.
