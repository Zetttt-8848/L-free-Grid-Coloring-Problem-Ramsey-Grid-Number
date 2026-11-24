# A four-color upper bound of 21,948,402

Every four-coloring of this square contains the directed L. The [window method](FOUR_COLOR_WINDOW.md) controls twelve successive shifts through two short words. A somewhat longer interval admits a simpler proof with a larger total saving. The following computation needs only the 548 certified window capacities and a short integer recurrence on four color counts.

Use the same notation \(v,D,K\) for an isolated decrease in the capacity profile, and put \(d=D-s\) for \(1\le s\le20\). Assume the preceding capacity is constant for at least 20 offsets and the subsequent capacity for at least 12. At this lag the ordinary distinct-minima allowance above \(12K\) is \(\min(s,12)\). As in the preceding proof, its actual value is bounded by the number of matches between \(P_i\) and \(T_{20-s+i}\) for \(0\le i<s\), with at most three selected per original color in each row \(s\).

Fix the first word \(P\), and let \(h_j\) be the four color counts in its first \(j\) positions. Sum all selected matches over the 20 rows. A count by rows gives an upper bound \(\sum_{j=1}^{20}\sum_c\min(3,h_{j,c})\). A count by columns gives another upper bound \(\sum_{j=1}^{20}\max_c h_{j,c}\). Indeed column \(j-1\) of the second word can receive matches only from positions \(0,\ldots,j-1\) of the first word, and all counted arrivals there have one color. The sum of the two upper bounds bounds twice the score.

For an unordered four-count vector \(u\) let \(V(0)=0\) and
\[
 V(u)=\max_{i:u_i>0}V(\operatorname{sort}(u-e_i))
       +\max_i u_i+\sum_i\min(3,u_i).
\]
Deleting the last letter proves the recurrence by induction. Over all four-count vectors of total 20 it gives \(\max V=267\). Hence the integer score is at most 133. The ordinary total is \(1+\cdots+12+8\cdot12=174\), giving at least **41 missing matches** per block.

At side 21,948,402 there are 544 disjoint complete blocks. At the same outer window width 34,950, the baseline is \(-116,299,243,654,456,808,241,433,200\). Crediting each missing match at the smallest correlation in its block gives \(128,738,682,276,347,489,324,958,496\). The resulting positive margin is **12,439,438,621,890,681,083,525,296**.

Run **python verify_four_twenty.py**. Its first step verifies the preceding window certificate, including the 548 interval witnesses. An optional path to the authors' exact rational input tables enables the extended numerical verification described in the [previous proof](FOUR_COLOR_WINDOW.md).
