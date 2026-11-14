# Four colors at side 21,953,510

Every four-coloring of the square of side **21,953,510** contains a monochromatic directed equal-leg L. This certificate uses one external finite Sidon-set theorem. The [earlier elementary proof](FOUR_COLOR.md) gives **21,987,409** without that input.

## The input and its scope

Carter, O'Bryant and Tao prove that a set of $k\ge483$ integers in $N$ consecutive positions with all positive differences distinct satisfies

$$
k\le \sqrt{N}+0.94304\,N^{1/4}+0.44466.
$$

The definition of Sidon set in the preprint is equivalent to unique positive differences. Translation preserves the property. We use the finite cardinality bound in Section 1.1, with the constants as printed in version 1. [Carter, O'Bryant and Tao, *On the diameter and distribution of Sidon sets*, October 2026](https://arxiv.org/html/2610.36207v1#S1.SS1)

Let $Q(p)$ be an upper bound for the size of a Golomb set in $p$ consecutive positions. The checker tabulates the first possible length under the displayed inequality for each size from 4,700 to 4,800. Every query lies inside this table. If size $k$ is excluded, a larger set would contain an excluded $k$-element subset. For exact threshold calculation, set $S=100000$, $B=94304$ and $Y=Sk-44466$. Size $k$ is excluded at length $p$ precisely when both

$$
Y^2>S^2p,
\qquad
(Y^2+S^2p)^2>p(2YS+B^2)^2
$$

hold. The first comparison preserves the sign in squaring. These strict comparisons implement the stated external estimate with integer arithmetic.

## Propagation to the square

Take a set with a proper binary strict source in $p$ consecutive positions. At internal distance $h$, the two disjoint Golomb classes of starts are supported on $p-h$ consecutive positions. Their two distinct minima give the joint bound $Q(p-h)+Q(p-h-1)$. For a candidate $k$-mark binary source and a rank $r$, let $H=rk-r(r+1)/2$. The least possible sum of its rank-neighbor differences is bounded below by the cost of the cheapest $H$ positive differences in this profile. The upper bound on the sum uses the minimum spans of both endpoint blocks at every rank, from the elementary recursion in [the preceding proof](FOUR_COLOR.md). The first failing size excludes every larger size by restriction.

The file **four_sidon_runs.json** records an offset, a capacity and a witnessing rank in each row. The indexing origin is 21,975,000. A row of offset $u$ bounds every binary-source set in at most $21{,}975{,}000-u$ consecutive positions. The next row begins when a tighter capacity is available. The verifier checks each strict rank inequality at the first offset in its run and explicitly checks coverage of the offsets used by the square.

For the square, each main-diagonal shift $d$ has twelve disjoint classes of starts. Each class has a proper binary strict source. Ordering their minima gives $U_d=\sum_{j=0}^{11}K(21{,}953{,}510-d-j)$ as a bound on all equal-color pairs at shift $d$, where $K(p)$ is the certified capacity in $p$ positions. The geometry and the convolution inequality are proved in [the preceding proof](FOUR_COLOR.md).

With $t=34{,}700$ and $w_i=i(t+1-i)$, the necessary nonpositive doubled margin is **3,322,828,120,073,118,722,559,272**. The positive sign rules out a proper square. The checker uses 543 interval witnesses and all 34,699 positive kernel lags. This is an application of the cited result to the directed-L reduction.

## Reproduction

Run **python verify_four_sidon.py** in this directory. The verifier computes interval capacities in blocks between exact Sidon thresholds and computes correlations from power sums. The discovery calculation instead used cumulative sums over individual differences, bounded radicals and a closed product for the correlations. Both give the same integer margin.
