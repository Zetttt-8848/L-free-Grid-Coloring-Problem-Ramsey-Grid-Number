# A four-color upper bound of 21,947,877

Every four-coloring of the square of side **21,947,877** contains a monochromatic directed equal-leg L. At the edge of a finite interval, a Golomb set can supply only a bounded number of marks to a window. For seven entries of the published tables, this count forces the convolution strictly below the value required for equality in Cauchy's inequality. Keeping the squared discrepancy sharpens both applications of the [two-level window proof](FOUR_COLOR_DOUBLE_WINDOW.md). [Original rational window data](https://github.com/dcartermath/sidon-error/tree/ff5b032fc3745140549777a96a9ec3ba7f8dd954/asymptotic)

## An explicit lower bound on the squared discrepancy

Use the discrete windows \(w_i\), expanded tables \(T_i\), probabilities \(\pi_i\), and table excess \(\alpha\) of the [window construction](FOUR_COLOR_WINDOW.md). Let \(A\) have \(k\) marks in \(p\) positions and put \(S_i=1_A*w_i\). Coverage gives \(\mathbf E\langle S_i,T_i\rangle\ge k\). Write \(E\) for the upper bound on \(\mathbf E\|S_i\|_2^2\) obtained from the allowed difference multiplicities, and \(P=p+B\alpha\). For every \(\lambda>0\),
\[
 \mathbf E\|S_i-\lambda T_i\|_2^2\le E-2\lambda k+\lambda^2P.
\]
If the left side is at least \(\lambda^2D\) for \(\lambda=k/(P-D)\), substitution gives \(k^2\le(P-D)E\).

Let \(Q(u)\) cap the number of marks in any interval of \(u\) positions in the relevant hereditary family. In one sample, look at output positions \(jB+t\) measured from the chosen end, \(0\le t<B\). Let \(g\) be the normalized coefficient of the \(j\)-th coarse window bin, \(g_-\) the sum of earlier normalized coefficients from this end, and \(H\) the table entry at that bin. Each earlier bin sees at most \(Q(B)\) marks. The new bin sees at most \(Q(t+1)\). Consequently
\[
 S_i(jB+t)\le \frac{g_-Q(B)+gQ(t+1)}{B}.
\]
Reversing the kernel and table gives the same upper bound at the other end. With the stated table indexing, its last output cell is empty and the preceding reversed convolution has one fewer position available in the new bin. The displayed bound covers both conventions.

For certified ranges \(B_0\le B\le B_1,\ p\le p_1,\ k\ge k_0\) put \(\lambda_0=k_0/(p_1+B_1\alpha)\). The required \(\lambda\) is at least \(\lambda_0\). Group \(t=0,\ldots,B_0-1\) into blocks \(\ell\le t<u\). For that sample the normalized squared discrepancy has the lower bound
\[
 \pi_i\sum_{[\ell,u)} (u-\ell)
 \left[H-\frac{g_-Q(B_1)+gQ(u)}{B_0\lambda_0}\right]_+^2 .
\]
Here \([v]_+=\max(0,v)\). The seven samples specify a table row, side, and bin. Within a table row their output positions are disjoint. The condition \(p-1\ge400B\) separates the left and right edge bands. Summing the seven bounds is therefore valid. Each coefficient in **four_window_edges.json** can be regenerated from the original rational matrices.

## Elementary small-interval capacities

For an ordinary Golomb set in \(u\) positions, \(\binom{k}{2}\le u-1\). A rectangular window of arbitrary positive integer width \(w\) also gives
\[
 wk^2\le (u+w-1)\bigl(k+\gamma(w-1)\bigr)
\]
when every positive difference has multiplicity at most \(\gamma\). This follows by squaring and summing the window counts and applying Cauchy's inequality on their support. For Golomb sets take \(\gamma=1\). For a set with a properly two-colored strict source take twice the resulting Golomb cap in \(u\) positions, by the two-class partition. The verifier takes the minimum over 17 explicit integer widths and the trivial family caps. These local calculations use only elementary counting.

| Family | Range of \(B\) | \(p_1\) | \(k_0\) | Group width | Certified \(D\) |
|---|---:|---:|---:|---:|---:|
| Ordinary Golomb | 15,000–16,600 | 22,500,000 | 4,600 | 8 | 52 |
| Proper binary strict source | 1,720–1,820 | 21,975,000 | 455,000 | 4 | 213 |

The first correction adds 52 positions to the 201 ordinary Golomb thresholds evaluated at the chosen dilations. Each exclusion embeds the prospective set in the tested interval of length one less than its threshold. The second correction applies to 565 binary-source interval witnesses. All parameter ranges are checked for each invocation.

## The outer four-color contradiction

Take \(T=35,990\), \(u_i=i(T+1-i)\), and \(w_i=u_i(5(T+1)^2+6u_i)\) for \(1\le i\le T\). Its integer correlations are \(b_d=\sum_i w_iw_{i+d}\). As a function of \(T-d\) this sum is a polynomial of degree at most nine, by summing a polynomial of total degree at most eight in \(i\) and \(T-d\). The checker reconstructs the polynomial by finite differences and checks five correlations by direct summation.

At side 21,947,877, the distinct-minima baseline in the [four-color convolution inequality](FOUR_COLOR_WINDOW.md) is \(-8,994,733,962,487,986,521,984,660,222,886,550,382,497,049,520\). The [twenty-shift recurrence](FOUR_COLOR_TWENTY.md) forces 41 missing matches in each of 561 disjoint blocks. Their total weighted correction is \(9,898,715,879,654,775,090,490,051,377,873,405,177,480,967,584\). The positive margin is **903,981,917,166,788,568,505,391,154,986,854,794,983,918,064**.

Run **python verify_four_edges.py**. For full regeneration of the input coefficients and all 401 coarse coverage inequalities, pass the path to the authors' **asymptotic** directory. The calculation uses the Python standard library.
