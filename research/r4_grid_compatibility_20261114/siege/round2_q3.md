kind: attempt

Open questions attempted (flagged OPEN by this run): Part (D-a).
- Is there an anti-collision / union-growth lemma, under a NAMED averaged near-extremality hypothesis, that forces |R_e(h)| > (2/3)|F_h(D)| for all three e on a positive a-weighted share of shifts h? That contradicts double cover and so yields a proportional loss with explicit delta.
- Or is there a window-averaged request-energy bound with constant C2 < 3/2?
If neither can hold, prove a NO-GO instead: give an explicit model (a proper ternary source, or a family of them, checkable L by L) in which the hypotheses hold in the relevant scaled form while the requests collide completely. Then name exactly what extra property a successful lemma would need.

## Facts you may use (proved earlier in this run)
1. Lemma 0. Every directed L in V(D) is L(u,d,h) for exactly one triple with 1 <= d < h. Its horizontal end is (u+d,u), its corner (u+h,u), its vertical end (u+h,u+h-d), and its arm length h-d. It lies in V(D) iff u, u+d, u+h-d, u+h are in D. Here d ranges over all of [1,h-1], including d > h/2.
2. (i) L(u,d,h) is monochromatic of color e iff u ∈ F_{h-d}(S_e(d)) ∩ S_e(h). So chi is proper iff S_e(h) ∩ R_e(h) = ∅ for all h,e. (ii) R_e(h) ⊆ F_h(D). (iii) k(u) = #{e: u ∈ R_e(h)} <= 2, and sum_e |R_e(h)| = 2|F_h(D)| - 2#{k=0} - #{k=1}. (iv) For X = S_e(d) and h = d+l: F_l(X) ⊆ R_e(h). F_l(X) splits into the two Sidon sets G_f = F_l(X) ∩ S_f(h), f ≠ e. F_l(X) ∩ R_{e'}(h) ⊆ G_{e''}.
3. Single-shift futility. Fix the classes at shifts < h. The L's with corner at shift h are satisfiable iff R_0(h) ∩ R_1(h) ∩ R_2(h) = ∅. Counting at one shift only gives |F_h(D)| >= (1/2) sum_e |R_e(h)|. A saving therefore needs union growth on many shifts at once.
4. Energy reduction. Suppose sum_u m_{e,h}(u)^2 <= C1 N_e(h) + C2 N_e(h)^2/|F_h(D)| for all three e, with C2 < 3/2. Then min_e N_e(h) <= (2C1/(3-2C2))|F_h(D)|. The proof is Cauchy-Schwarz, |R_e| >= N_e^2 / sum m^2, plus double cover.
5. Pointwise bounds are false for arbitrary sources. An explicit proper source on D = [0,14), h = 5, has one start carrying all 4 requests of a color, with |F_5| = 9. A sparse digit family has |F_h| = 3 and N_e(h) >= k for every e and every k. In the cyclic version all requests of a color sit on one start. So any valid lemma must use a size / near-extremality hypothesis, or average over h, or both.
6. Collision lemma (two L's linking two agreements at one corner). Suppose u ∈ F_{h-d}(S_e(d)) ∩ F_{h-d'}(S_e(d')) with d < d'. Then u+(d'-d) ∉ S_e(d) and u+(h-d') ∉ S_e(d).
   Proof: L(u,d,d') has horizontal end (u+d,u) and corner (u+d',u), both of color e. So its vertical end (u+d', u+d'-d) is not e. L(u+h-d',d,d') has corner (u+h,u+h-d') and vertical end (u+h,u+h-d), both of color e. So its horizontal end (u+h-d'+d, u+h-d') is not e.
   Thus, writing l = h-d and delta = d'-d, a collision forces u, u+l ∈ S_e(d) and u+delta, u+l-delta ∉ S_e(d). The energy is E_e(h) = sum_u m_{e,h}(u)^2 = N_e(h) + 2 sum_{d<d'} |F_{h-d}(S_e(d)) ∩ F_{h-d'}(S_e(d'))|.
7. Global identity: sum_h N_e(h) = sum_d C(|S_e(d)|, 2).

## How the capacities K arise (quoted from the certifying project record)
--- quoted: the rank-neighbor inequality ---
Consider a hereditary family of finite sets of integers. Let $b_1<\dots<b_s$ be a member of span $L$. Suppose a member with $j$ marks must have span at least $e_j$, for the smaller ranks used below. Choose $1\le c<s$ and take all differences of rank at most $c$, numbering $H=cs-c(c+1)/2$ of them. If the multiplicity of positive difference $h$ is bounded by $v_h$, let $P(H;v)$ be the sum of the cheapest $H$ terms in the multiset containing $v_h$ copies of $h$. Then
$$
 2P(H;v)+4\sum_{i=0}^{c-1}(c-i)e_{i+1}\ \le\ Lc(c+1).
$$
Indeed the sum of the selected differences telescopes to $\sum_{i=0}^{c-1}(c-i)(b_{s-i}-b_{i+1})$. The first and last $i+1$ marks each have span at least $e_{i+1}$, so their endpoint difference in this expression is at most $L-2e_{i+1}$. This remains true when the blocks overlap. The sum is at least $P$ by construction. The archive used $e_{i+1}=i$. Here the endpoint blocks belong to the same family as the original set, allowing an induction on cardinality. [Earlier rank-neighbor inequality](../../exploration/research_round3/four/R3_R4_REPORT.md)
--- quoted: how it is applied to binary sources ---
Next take sets admitting a proper two-coloring of their strict source $V(A)=\{(v,u):u<v,\ u,v\in A\}$. This family is also hereditary. At shift $h>0$ partition the starts $u,u+h\in A$ by the color of $(u+h,u)$. These two sets of starts are Golomb. To see this, on the starts form the weak triangle with entries $z(v+h,u)$ for $v\ge u$, where $z$ is the binary strict-source coloring. Its entries stay in $V(A)$. A repeated difference in one diagonal color forces a monochromatic L in the other color as in the six-class argument in README.md. Both sets have span at most $L-h$. In particular $v_h\le2Q(L-1)$ for every $h$.

For a binary-source set of span at most $L$, the two Golomb start classes at internal distance $h$ occupy the same interval of span $L-h$. Their minima are distinct when both are nonempty. Ordering them gives the stronger multiplicity profile
$$
 v_h\le Q(L-h)+Q(L-h-1).
--- end of quotes ---
(Q(S) is the largest size of a Sidon set of span at most S, about sqrt(S). The e_j are recursively computed span lower bounds.)

## Heuristic regime (NOT theorems)
- With v_l about 2 sqrt(L) for all small l, the cheapest H differences cost about H^2/(4 sqrt L), and H is about cs, so the inequality gives s <~ sqrt(2) L^{3/4}; at L = 2.2*10^7 this is about 4.6*10^5 = K. Equality-type behaviour needs EVERY lag l up to about l_0 ~ 3.5*10^5 to have fiber multiplicity close to v_l, i.e. each class behaves like a set of density p = sqrt(2) L^{-1/4} (about 1/48) whose fibers r(l) are all about p^2 L, and each of its two Golomb classes at lag l is a NEAR-MAXIMAL Sidon set in an interval of length L - l.
- In that regime D = D_c has density about 1/4, |F_h(D)| ~ 1.37*10^6, and each request set F_{h-d}(S_e(d)) has size ~9.4*10^3, i.e. relative density about 1/146 inside F_h(D). There are h-1 such sets for each color. If they were roughly independent, R_e(h) would cover all of F_h(D) once h >> 146 for every e, which is impossible since by properness each start lies in at most two R_e(h) (so sum_e |R_e(h)| <= 2|F_h(D)|). So in the regime the request sets must collide massively: a typical requested start u in R_e(h) has multiplicity m_{e,h}(u) >= about h/97.
- In corner/arm language, m_{e,h}(u) = #{d < h : chi(u+d,u) = e = chi(u+h, u+h-d)} counts e-agreements between the row word of u and the reflected column word of u+h. Massive collision means: for many pairs (u, u+h), row u and column u+h agree in color e on a fixed positive fraction (about 1/97 or more) of the arms d < h, for two of the three colors, while never agreeing in the corner color.

## Task
1. Name a precise hypothesis. It must be stated as inequalities on class sizes and/or fiber multiplicities, and it must be AVERAGED: a hypothesis on a single class at a single shift gives only a negligible additive saving. A natural candidate, for one ternary source (D, chi) with D ⊆ [0,L) and window weights a_h:

   H_avg(eta): sum_h a_h sum_e |S_e(h)| >= (1-eta) sum_h a_h * 3K(L-h),

   possibly together with fiber hypotheses of the form sum_l r_{S_e(d)}(l) * (weights) >= (1-eta)(...). You may use any variant; state it exactly.
2. Then either:
   (a) prove that the hypothesis is impossible for an explicit eta > 0, with every constant explicit, by an anti-collision, union-growth or window-averaged energy argument. Then deduce explicitly the resulting proportional loss sum_e |S_e(h)| <= (1-delta)(sum of caps) on a-average, and say which consumer quantity it lowers. Exploit the collision lemma, item 6, and any further L's you find among the six points u, u+d, u+d', u+h-d, u+h-d', u+h and their neighbours. One possible handle: in a near-extremal class, the "inner symmetric pair" u+delta, u+l-delta must avoid S_e(d) for every colliding delta, while near-extremal fibers say that S_e(d) has the right number of pairs at every lag. Find whether this is incompatible with heavy collision.
   (b) or prove a no-go: an explicit model (proper ternary sources, a complete properness proof covering every L including d > h/2) in which the request sets collide completely, e.g. R_e(h) small while N_e(h)/|F_h(D)| is large on many h, AND the class sizes and fiber multiplicities are as large as possible for the model's scale. Then state precisely which variants of (D-a) survive.
3. Separate proved statements from heuristics, and end with a list of the exact statements proved, with all hypotheses.

Rules: every proof complete; every counterexample explicit and checkable L by L; finite computations are evidence only. Do not import three-color facts (in three colors a start is requested by at most one color; here it is "at most two of three", item 2(iii)).
