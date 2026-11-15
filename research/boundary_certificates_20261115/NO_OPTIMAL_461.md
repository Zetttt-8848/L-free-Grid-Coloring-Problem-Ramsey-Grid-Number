# An optimal 24-mark completion class excludes too many diagonal positions

In a proper three-color square of side 461 **no completion class can have 24 marks and span 425**. The proof compares two counts of the original color on the same diagonal. Every color occupies at least 135 positions. A span-425 completion class forces its original color into at most 95 positions. The finite check uses only binary forced-color deductions. Its geometric premises are the six-class lemma and the externally certified optimal spans for 24 and 25 marks, including uniqueness up to reflection for order 24. [Six-class argument](README.md) · [OGR-24 announcement](https://blogs.distributed.net/2004/11/) · [OGR-25 announcement](https://blogs.distributed.net/2008/10/)

## Diagonal color frequencies

Let $A$ be any one diagonal color class and put $m=|A|$. On the positive lags $1\le d\le84$, at most two Golomb classes contribute starts to $r_A(d)=|A\cap(A-d)|$. Each fits in $461-d$ consecutive positions. The available span is at most $460-d$. Thus $r_A(d)\le48$ for $d\le35$ and $r_A(d)\le46$ for $d\ge36$. Write these caps as $v_d$. They use the elementary order-24 and order-25 span thresholds.

Set $w_i=i(86-i)$ for $1\le i\le85$, and let $a_d$ be its autocorrelation. The sum of $1_A*w$ is $m\sum w_i$, and its support fits in $461+84$ positions. Cauchy's inequality gives

$$
m^2\left(\sum_i w_i\right)^2
\le 545\left(m a_0+2\sum_{d=1}^{84} v_da_d\right).
$$

Here $\sum w_i=105995$, $a_0=156809003$ and $2\sum v_da_d=527135185836$. The largest integer satisfying this inequality in $[0,461]$ is 163. Since the three frequencies sum to 461, every one is at least $461-2\cdot163=135$.

## Forced cells after adding one candidate mark

Let $P=Q$, the optimal 24-mark ruler listed in [the occurrence theorem](RULER_OCCURRENCES.md). Suppose a class at shift $d$ is $s+Q$, with original diagonal color $c$ and completion color $e\ne c$. In coordinates relative to $s$, the compulsory diagonal positions of color $c$ are $B=Q\cup(d+Q)$. Every cell in the strict source on $B$ avoids $c$. It therefore has two available colors, and every cell $(v+d,v)$ with $v\in Q$ has the particular color $e$.

For each candidate diagonal position $u$, suppose it too has color $c$. The same constraints now hold on the strict source of $B\cup\{u\}$. Start with the prescribed completion cells. Whenever two cells of a directed L already have the same binary color, force its third cell to the other binary color. A demand for both colors on one cell excludes $u$. Positions for which this procedure stops without contradiction remain eligible.

For a fixed lag $d$, admissible starts are $s=0,\ldots,35-d$. At such a start the full relative diagonal interval is $[-s,460-s]$. The verifier computes every individual exclusion once per lag and counts eligible positions in every one of these intervals. The largest count is **95**, attained by this test at $d=2$. It is an upper bound on $|A_c|$ for any hypothetical completion class of this shape. This contradicts the lower bound 135. The reflected orientation is covered by $(x,y)\mapsto(460-y,460-x)$, which takes each directed L to another of the same positive step. The reflection preserves the unique completion cell and exchanges the other two vertices.

Run **python verify_no_optimal.py**. The checker constructs the forced cells directly from their integer coordinates using the three possible roles in a directed L. A separate Boolean implication implementation obtained the same largest counts for all 35 lags. The [earlier two-class certificate](RULER_OCCURRENCES.md) uses a different obstruction and is retained for comparison.
