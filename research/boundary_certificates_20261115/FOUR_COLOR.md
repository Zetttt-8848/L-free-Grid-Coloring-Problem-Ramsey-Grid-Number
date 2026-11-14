# Recursive span bounds in the four-color count

**Result.** Every four-coloring of a square of side **21,987,409** contains a monochromatic triple $(x,y),(x+d,y),(x+d,y+d)$ with $d>0$. The verifier uses integer arithmetic and 608 short witnesses. The proof below derives its span bounds from scratch. In particular it has no external optimal-ruler table or archived capacity lemma as a numerical premise.

## Rank-neighbor inequality

Consider a hereditary family of finite sets of integers. Let $b_1<\dots<b_s$ be a member of span $L$. Suppose a member with $j$ marks must have span at least $e_j$, for the smaller ranks used below. Choose $1\le c<s$ and take all differences of rank at most $c$, numbering $H=cs-c(c+1)/2$ of them. If the multiplicity of positive difference $h$ is bounded by $v_h$, let $P(H;v)$ be the sum of the cheapest $H$ terms in the multiset containing $v_h$ copies of $h$. Then
$$
 2P(H;v)+4\sum_{i=0}^{c-1}(c-i)e_{i+1}\ \le\ Lc(c+1).
$$
Indeed the sum of the selected differences telescopes to $\sum_{i=0}^{c-1}(c-i)(b_{s-i}-b_{i+1})$. The first and last $i+1$ marks each have span at least $e_{i+1}$, so their endpoint difference in this expression is at most $L-2e_{i+1}$. This remains true when the blocks overlap. The sum is at least $P$ by construction. The archive used $e_{i+1}=i$. Here the endpoint blocks belong to the same family as the original set, allowing an induction on cardinality. [Earlier rank-neighbor inequality](../../exploration/research_round3/four/R3_R4_REPORT.md)

## Two span recursions

First take the family of Golomb sets, whose positive differences have multiplicity at most one. Compute a lower span $g_s$ for $2\le s\le4900$ starting with $g_1=0$. For each $1\le c\le\min(130,s-1)$, insert $2P=H(H+1)$ and $e_j=g_j$ in the rank inequality. Round the resulting lower bound on $L$ upwards. Take the largest bound among these and $g_{s-1}+1$. The latter follows by deleting the largest mark. All right-hand values were computed at smaller sizes. Define $Q(S)=\max\{s:g_s\le S\}$ on the spans used. The verifier establishes $g_{4900}>21{,}991{,}300$, so the finite table covers the full range.

Next take sets admitting a proper two-coloring of their strict source $V(A)=\{(v,u):u<v,\ u,v\in A\}$. This family is also hereditary. At shift $h>0$ partition the starts $u,u+h\in A$ by the color of $(u+h,u)$. These two sets of starts are Golomb. To see this, on the starts form the weak triangle with entries $z(v+h,u)$ for $v\ge u$, where $z$ is the binary strict-source coloring. Its entries stay in $V(A)$. A repeated difference in one diagonal color forces a monochromatic L in the other color as in the six-class argument in README.md. Both sets have span at most $L-h$. In particular $v_h\le2Q(L-1)$ for every $h$.

Compute lower spans $e_s$ for this family, starting with $e_1=0$ and trying $L=e_{s-1}+1$. For each rank $c\le\min(80,s-1)$ apply the displayed inequality with the uniform cap $M=2Q(L-1)$ and already computed $e_j$. If $H=Mt+r$ with $0\le r<M$, then $2P=Mt(t+1)+2r(t+1)$. Advance $L$ through every value excluded by this test. An earlier rejection of a smaller $L$ remains valid when another rank is tested. The final $L$ is a certified lower bound on the span of every $s$-mark member.

## Large binary sources and the four-color square

For a binary-source set of span at most $L$, the two Golomb start classes at internal distance $h$ occupy the same interval of span $L-h$. Their minima are distinct when both are nonempty. Ordering them gives the stronger multiplicity profile
$$
 v_h\le Q(L-h)+Q(L-h-1).
$$
An empty second class costs zero. Only positive spans enter the active profiles. The rank inequality now uses the small binary-source spans $e_j$ and this decreasing profile. For each row of **four_capacity_runs.json**, let $v,K,c$ be its three integers and $N=21{,}991{,}300$. At $L=N-v-1$, the checker proves that size $s=K+1$ violates the inequality at rank $c$. Every larger set would contain a subset of this excluded size. Each row therefore bounds every span at most $L$ and gives the claimed cap up to the next row. $N$ is an indexing origin. Its status as a prior bound plays no role.

Fix $n=21{,}987{,}409$. At each main-diagonal shift $d>0$, partition equal-colored pairs by the original color and the actual completion color. The twelve classes share the $n-d$ possible starting positions. Each class has a proper binary strict source. Indeed its cells $(v+d,u)$ avoid the original diagonal color and the common completion color. The first exclusion follows from the two main-diagonal endpoints and the second from $(u+d,u),(v+d,u),(v+d,v)$. Translation preserves directed Ls. Sort the nonempty classes by their distinct minima. Class of rank $j$, starting at rank zero, fits in $n-d-j$ consecutive positions. Hence their total is bounded by $U_d=\sum_{j=0}^{11}K_{N-n+d+j}$.

Use $t=35{,}000$, $w_i=i(t+1-i)$ for $1\le i\le t$, and $a_d=\sum_i w_iw_{i+d}$. Pointwise Cauchy on the four diagonal color indicators gives the necessary inequality
$$
 2\sum_{d=1}^{t-1}(n-d-4U_d)a_d-3na_0\le0.
$$
The check reconstructs all 34,999 positive lag weights and verifies the left side is **2,727,455,661,705,377,936,113,840**, which is strictly positive. This excludes the square.

## Reproduce

Run **python verify_four_rank.py** in this directory. Each row of the adjacent JSON file is checked by proving its strict first-forbidden-size inequality. Finding the best possible rank or smallest possible side is unnecessary. The proof introduces recursive span costs at both levels and staggers the two inner and twelve outer intervals. An exploratory alternative using the repository's order-13 window classification was not needed for this certificate.
