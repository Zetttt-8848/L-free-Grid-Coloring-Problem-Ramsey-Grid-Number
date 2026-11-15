kind: attempt

Open question attempted (flagged by this run as OPEN): Part D (D-a) under an explicitly named near-extremality hypothesis — prove that the three completion classes at one shift cannot all be near their binary-source caps, with an explicit proportional loss delta > 0, by a union-growth / anti-collision argument for the request sets.

Background you need (the capacity K is derived as follows; this is quoted from the project record that certifies it).

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
(In the quote, "a member with j marks must have span at least e_j" are the recursively computed span lower bounds; Q(S) is the largest size of a Golomb (Sidon) set of span at most S, about sqrt(S). The Golomb split is the fact, stated in the problem, that each fiber of a binary source splits into two Sidon sets by the color of the completion cell.)

Heuristic consequences (NOT theorems; use them only to guide; derive anything you rely on):
- With v_l about 2 sqrt(L) for all small l, the cheapest H differences cost about H^2/(4 sqrt L), and H is about cs, so the inequality gives s <~ sqrt(2) L^{3/4}; at L = 2.2*10^7 this is about 4.6*10^5 = K. Equality-type behaviour needs EVERY lag l up to about l_0 ~ 3.5*10^5 to have fiber multiplicity close to v_l, i.e. each class behaves like a set of density p = sqrt(2) L^{-1/4} (about 1/48) whose fibers r(l) are all about p^2 L, and each of its two Golomb classes at lag l is a NEAR-MAXIMAL Sidon set in an interval of length L - l.
- In that regime D = D_c has density about 1/4, |F_h(D)| ~ 1.37*10^6, and each request set F_{h-d}(S_e(d)) has size ~9.4*10^3, i.e. relative density about 1/146 inside F_h(D). There are h-1 such sets for each color. If they were roughly independent, R_e(h) would cover all of F_h(D) once h >> 146 for every e, which is impossible since by properness each start lies in at most two R_e(h) (so sum_e |R_e(h)| <= 2|F_h(D)|). So in the regime the request sets must collide massively: a typical requested start u in R_e(h) has multiplicity m_{e,h}(u) >= about h/97.
- In corner/arm language, m_{e,h}(u) = #{d < h : chi(u+d,u) = e = chi(u+h, u+h-d)} counts e-agreements between the row word of u and the reflected column word of u+h. Massive collision means: for many pairs (u, u+h), row u and column u+h agree in color e on a fixed positive fraction (about 1/97 or more) of the arms d < h, for two of the three colors, while never agreeing in the corner color.

Task. Name a precise near-extremality hypothesis H(eta), e.g.

  H(eta): for each e in P and each shift d in a window [1, T], |S_e(d)| >= (1-eta) K(L_d), and r_{S_e(d)}(l) >= (1-eta) v_l for all 1 <= l <= l_0, where L_d is the span available to S_e(d);

(you may choose a different, weaker, or averaged hypothesis, e.g. only on a_h-weighted averages; say exactly what it is), and then do one of:
(1) Prove that H(eta) is impossible for some explicit eta > 0 (that is the proportional loss: then sum_e |S_e(h)| <= (1-delta) * sum of caps follows with delta tied to eta — make this deduction explicit and say which consumer quantity, v_l, K or U_d, it lowers); the natural route is an ANTI-COLLISION lemma bounding the overlaps |F_{h-d}(S_e(d)) ∩ F_{h-d'}(S_e(d'))| for d != d' (six points u, u+d, u+d', u+h-d, u+h-d', u+h of D are involved; find the L's among the cells they span that constrain the overlap), or a bound on the request energy E_e(h) = sum_u m_{e,h}(u)^2 = sum_{d,d'} |F_{h-d}(S_e(d)) ∩ F_{h-d'}(S_e(d'))|, so that by Cauchy-Schwarz |R_e(h)| >= N_e(h)^2 / E_e(h) > (2/3)|F_h(D)| for every e, contradicting double cover. Note that the trivial overlap bound (each overlap at most min of the two fiber sizes, ~2Q) gives only |R_e(h)| >~ 2Q, useless; and the pointwise energy bound U1 (sum m^2 <= (3/2)(N + N^2/|F_h|)) is FALSE in general (a source on D = [0,14) has one start carrying all four requests at h = 5), so the lemma must use the near-extremal structure or be averaged over h. A promising handle: near-maximal Sidon sets are rigid (their difference sets have density close to 1/2 in [1, span]; they are equidistributed in intervals and residue classes at suitable scales — state and prove whatever version you use, or cite a precise classical theorem with its exact statement), and the request set F_{h-d}(S_e(d)) is a union of two such near-maximal Sidon classes; show two such unions for different d cannot coincide on more than a small fraction without creating a monochromatic L.
(2) Or show that H(eta) is consistent with all constraints you can identify (give an explicit abstract model satisfying every L-constraint among the cells involved, or a proof that no request-type argument can exclude it), and identify exactly which additional property would be needed.

Every constant must be explicit. Separate proved statements from heuristics, and end with a list of the exact statements proved (with all hypotheses).
