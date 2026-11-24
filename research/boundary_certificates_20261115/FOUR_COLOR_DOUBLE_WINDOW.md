# A four-color upper bound of 21,948,350

Every four-coloring of the square of side **21,948,350** contains a monochromatic directed equal-leg L. The same discrete window improves two different counts. First it limits the number of marks in an ordinary Golomb ruler. The resulting integer thresholds then limit the size of a set with a properly two-colored strict triangle. The external data are the authors' six exact rational windows and their coverage tables. [Window construction and discrete lifting](FOUR_COLOR_WINDOW.md) · [Authors' exact rational data](https://github.com/dcartermath/sidon-error/tree/ff5b032fc3745140549777a96a9ec3ba7f8dd954/asymptotic)

Suppose a Golomb set has \(k\) marks in \(p\) consecutive positions. At every positive shift its difference multiplicity is at most one. For the nonnegative windows dilated by \(B\) let \(a_h\) be the averaged correlation. Mass one gives \(2\sum_{h>0}a_h=1-a_0\), and \(a_0=r_0/B\) in the normalized coarse units of the earlier proof. The coverage and Cauchy inequalities give
\[
 k^2\le(p+B\alpha)\bigl(1+(k-1)r_0/B\bigr).
\]
Consequently, for \(c=(k-1)r_0\), any admissible integer \(B\) gives the lower bound
\[
 L(k,B)=\left\lceil\frac{k^2B}{B+c}-B\alpha\right\rceil
\]
on the number of positions. Formally, to rule out all shorter rulers it suffices to embed each in \(L(k,B)-1\) positions. The checker verifies \(L(k,B)-2\ge 400B\) at that length. It chooses five integer candidates near the continuous maximum \(B=k\sqrt{c/\alpha}-c\) and checks each using rational arithmetic.

For \(4600\le k\le4800\), the 201 verified thresholds replace the rounded cardinality estimate in the [binary source argument](FOUR_COLOR_WINDOW.md). The 548 resulting interval certificates appear in **four_double_window_runs.json**. With outer width 34,950 and side 21,948,350, their weighted baseline is \(-118,121,816,949,773,746,256,344,944\). The [twenty-shift recurrence](FOUR_COLOR_TWENTY.md) gives 41 missing matches in each of 544 disjoint blocks. Their minimum weighted contribution is \(128,790,196,918,860,365,939,231,648\). The positive margin is **10,668,379,969,086,619,682,886,704**.

Run **python verify_four_double.py**. Passing the path to the authors' **asymptotic** directory also regenerates the window correlations and checks all 401 coverage alignments from their exact input tables.
