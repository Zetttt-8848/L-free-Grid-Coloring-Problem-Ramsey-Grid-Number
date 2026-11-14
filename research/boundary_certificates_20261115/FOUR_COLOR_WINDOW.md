# A four-color upper bound of 21,948,404

Every four-coloring of the square of side **21,948,404** contains a monochromatic directed equal-leg L. The proof uses finite Sidon estimates and the published nonnegative window and table of Carter, O'Bryant and Tao. Two additional counts drive the improvement. Inside a binary source the allowed difference multiplicity decreases with the distance. On the outer diagonal, twelve successive capacity changes share the same two short color words. The latter observation saves at least 30 matches per complete block. [Carter, O'Bryant and Tao, Sections 2.2 and A.3](https://arxiv.org/html/2610.36207v1) · [Authors' exact rational witness](https://github.com/dcartermath/sidon-error/tree/ff5b032fc3745140549777a96a9ec3ba7f8dd954/asymptotic)

## Discrete convolution with decreasing multiplicities

Let \(A\) be a set of \(k\) integers in an interval of \(p\) consecutive positions with a properly binary-colored strict source. The [two-class reduction](FOUR_COLOR.md) partitions its starts at shift \(h>0\) into two disjoint Golomb sets. Write \(Q(t)\) for the [certified Sidon cardinality cap](FOUR_COLOR_SIDON.md) in \(t\) consecutive positions. Sorting the two minima gives
\[
 r_A(h)\le v_h=Q(p-h)+Q(p-h-1).
\]
Only positive shifts in the support of the window enter the argument.

For an integer block width \(B\), replicate each column of each of the authors' six window rows \(G_j\) exactly \(B\) times. Divide by \(BM\), where all rows have the same sum \(M\). The resulting discrete window \(w_j\) has mass one and \(mB\) cells, where \(m=200\). Use their published probabilities to average over \(j\). The table consists of the first \(m\) columns of their row \(H_j\) repeated \(B\) times, a constant middle of length \(p-mB\), and the last \(m\) columns repeated \(B\) times. Its total length is \(p+mB\). We use \(p-1\ge2mB\). With \(\alpha=\mathbf E\sum_i H_{j,i}^2-2m\), the expected squared table norm is \(p+B\alpha\).

At any of the original \(2m+1\) integer alignments, the expected dot product of \(G_j/M\) and the corresponding \(m\) consecutive columns of \(H_j\) is at least one. These are checked directly from the published rational matrices. At an intermediate integer shift after replication the dot product is the linear interpolation of the adjacent coarse values. Stretching the constant middle retains both endpoint checks and gives coverage one in the interior. Consequently every \(x\in[0,p-1]\) has expected coverage at least one. In the indexing used here, the window for a mark \(x\) covers the positions \(x,\ldots,x+mB-1\) of the table.

Write \(a_h=\mathbf E\sum_i w_{j,i}w_{j,i+h}\). Summing coverage over the marks and applying Cauchy's inequality first over table positions and then over \(j\) gives
\[
 k^2\le (p+B\alpha)\left(k a_0+2\sum_{h=1}^{mB-1}v_h a_h\right).
\]
The nonnegative entries justify using the separate upper capacity at each shift. This is the point at which the full correlation profile of the published window enters.

The verifier stores \(r_j=\mathbf E\sum_i G_{s,i}G_{s,i+j}/M^2\) for \(0\le j<m\), and takes \(r_m=0\). At \(h=jB+t\), \(0\le t<B\), its exact discrete correlation is \(((B-t)r_j+t r_{j+1})/B^2\). All changes of \(v_h\) follow from the integer Sidon thresholds. At a threshold of \(Q\), the correction to the constant multiplicity budget is one entire tail sum of \(2a_h\). The checker verifies 548 intervals from **four_window_runs.json**. A row \((v,K,B)\) excludes \(K+1\) at \(p=21,975,000-v\). Subsets and subintervals give the same upper bound for every smaller \(p\) until a stronger row takes over.

## Thirty compulsory losses in twelve consecutive shifts

At an outer shift \(d\), the twelve completion classes have a properly binary-colored strict source. Let \(C(p)\) be the preceding nondecreasing capacity. The ordinary bound on their total is \(\sum_{j=0}^{11}C(n-d-j)\) by their distinct minima. [Outer class partition](FOUR_COLOR.md)

Consider a decrease from \(K+1\) to \(K\) at offset \(v\), with at least twelve positions to each neighboring decrease. Set \(D=v-(21,975,000-n)\). For \(d=D-s\) and \(1\le s\le12\), the ordinary bound is \(12K+s\). Every class with \(K+1\) starts must have its minimum in positions \(0,\ldots,s-1\). For such a minimum \(i\), the main diagonal colors at \(i\) and \(i+d\) agree. For each original color there are at most three completion colors, so at most three such minima count. Thus its true capacity is at most \(12K+M_s\), where for the two length-12 words \(P_i=z_i\) and \(T_j=z_{D-12+j}\),
\[
 M_s=\sum_{c=0}^3
     \min\left(3,\#\{0\le i<s:P_i=T_{12-s+i}=c\}\right).
\]
Each deficit \(s-M_s\) is nonnegative. Over all twelve shifts the same two words apply.

For any such \(P,T\), \(\sum_s M_s\le48\); the sharp example is \(P=000111111111\), \(T=000000000111\). To verify the upper bound, fix \(P\). Choose any collection of pairs \((s,c)\) and charge three units to each. Remove its votes from the matching cells. In each column \(j\) the second word has one color, hence its uncharged contribution is at most the largest remaining vote count of any one color in that column. The sum of these column maxima and the charges is an upper bound for every \(T\). The accompanying C checker finds a charge collection of value at most 48 for each of the 700,075 first words up to palette permutation. It also verifies the equality example. The total deficit in each block is at least \(\sum_{s=1}^{12}s-48=30\).

## Final integer sum

Take the outer window \(w_i=i(34951-i)\) for \(1\le i\le34950\), with correlations \(b_d\). The [four-color convolution](FOUR_COLOR.md) requires
\[
 -3nb_0+2\sum_{d=1}^{34949}(n-d-4U_d)b_d\le0
\]
for any upper bounds \(U_d\) on equal-colored starts. More generally the same inequality holds after substituting any certified upper bound on the *weighted sum* of those starts. At \(n=21,948,404\), the distinct-minima baseline has margin \(-90,422,183,662,414,011,960,985,072\). There are 544 disjoint complete blocks. For each block add \(8\cdot30\min_{1\le s\le12}b_{D-s}\) to the margin. Their total correction is \(94,186,029,099,831,697,780,548,480\). The resulting **positive margin is 3,763,845,437,417,685,819,563,408**.

To reproduce, compile and run **verify_quota12.c** with any C99 compiler. Run **python verify_four_window.py** in this directory. To check the correlation array, table excess and coverage inequalities against the authors' coefficients as well, pass the path to their **asymptotic** directory as its sole argument. Both Python modes use the standard library. The [preceding 21,953,510 proof](FOUR_COLOR_SIDON.md) uses only the published Sidon size inequality and has a separate checker.
