# A position-weighted proof that the three-color grid number is at most 144

Every three-coloring of the 144 by 144 square contains a monochromatic directed L. Combined with the published 20 by 20 construction, this gives $21\le R_3\le 144$. The proof uses finite triangle coloring counts and integer arithmetic. Its local catalogs cover $T_{11}$ through 6 rainbows (59,401 orbits), $T_{12}$ through 9 rainbows (16,060 orbits), $T_{13}$ through 12 rainbows (488 orbits), $T_{14}$ through 13 rainbows (0 orbits), $T_{15}$ through 14 rainbows (0 orbits), $T_{16}$ through 15 rainbows (0 orbits), up to simultaneous renaming of colors and permutations of the three geometric coordinates.

## Local scores

Give each cell of $T_m$ its nonnegative coordinates $(x-y-1,y,m-x-1)$, of sum $m-2$. An L of leg $j$ has vertices obtained by adding $j$ in each of the three coordinate directions to a fixed vector $(a,b,c)$ of sum $m-j-2$. Its symmetry class is $(j,\mathrm{sort}(a,b,c))$.

For each source order $m$ and dilation $d$, the certificate assigns a nonnegative integer weight to each such class. Let $b_m$ be the archived rainbow cutoff for that order. A coloring with more than $b_m$ rainbows has weight at least $(b_m+1)\min w$. For every coloring at or below the cutoff, sum the weights of its actual rainbow Ls. The minimum of those finite scores and the preceding lower bound is a valid lower bound $s_{m,d}$ for every proper coloring. The exhaustive [boundary-deletion recurrence](LOCAL_RAINBOW_MINIMA.md) supplies the deeper catalogs through order 14 and the earlier order-15 obstruction. The [order-15 and order-16 interior refutations](LOCAL_RAINBOW_MINIMA.md#fourteen-through-eighteen-rainbows-at-orders-14-through-18) supply the remaining empty catalogs used at side 144.

## Using the surrounding square

Assume that the whole $N$ by $N$ square is properly colored. The triangle supplies the upper bound on rainbows. Its surrounding square supplies additional lower bounds. A source triangle of order $m$ with translation $(a,b,c)$ and dilation $d$ has an axis-aligned bounding square of side $m-1$ in its own lattice. Its lower-left lattice point in host coordinates is $(1+a+b,b)$.

The [square extension checks](SQUARE_PATCHES.md) increase the guaranteed count on specific placements. Test every certified offset and its antidiagonal reflection. If an enclosing square of side $s$ and step $d$ fits inside the host and forces at least $r$ rainbows, omit catalog profiles containing fewer than $r$ rainbows. The new floor is the minimum over the remaining profiles and the unseen-coloring floor $\max(b_m+1,r)\min w$. The certificate uses the enclosing-square checks specified by its patch level, including the order-13 dilation and placement rules. For each rule the checker counts every eligible translation once, including when several enclosing squares fit. Placements outside the certified positions use the original floor. Summing these contributions gives $J$.

## Copies and the boundary of the host

The host is $T_N$ with $N=144$. At a dilation $d$ the translation triple $(\alpha,\beta,\gamma)$ has sum $Q=N-2-d(m-2)$. A rule may select only copies with $\ell\le\min(\alpha,\beta,\gamma)<u$. The number of such copies is $H_Q(\ell)-H_Q(u)$, where $H_Q(t)=\binom{Q-3t+2}{2}$ for $Q\ge3t$ and zero otherwise. Subtract $t$ from all three coordinates to obtain this formula. These counts give the base contribution to $J$ before the placement-specific increases.

Other rules select $\ell\le\max(\alpha,\beta,\gamma)<u$. For any threshold $t$, the indicator that all three coordinates are less than $t$ equals the product of the three factors $1-\mathbf 1_{\alpha_i\ge t}$. Expanding it gives eight signed restrictions on coordinatewise lower bounds. Subtract the expansion for $t=\ell$ from that for $t=u$. A term with lower bounds $(r,s,t)$ contributes $\binom{Q-r-s-t+2}{2}$ translations when $r+s+t\le Q$ and zero otherwise. Each selected copy contributes one regardless of its translation region. Summing over overlapping rules is legitimate because each rule contributes its own specified weights.

## Joint restrictions on the translation

Some rules use a half-open interval for both the smallest and the largest translation coordinate. Write their endpoints as $(l_1,u_1)$ and $(l_2,u_2)$. Membership is the product of the two earlier band indicators. In a signed term with lower threshold $l$ on every coordinate and lower threshold $r$ on some selected coordinates, impose $\max(l,r)$ on the selected coordinates and $l$ on all the others. Expanding the product gives an integer sum of translated regions. The verifier also enumerates the translations and compares their literal count with that expansion. After locating a host corner, its three gaps must satisfy both bands.

Fix a host L of step $h$ and base coordinates $(A,B,C)$, with $A+B+C=N-h-2$. A source L at $(a,b,c)$ of step $j$ maps to it exactly when $h=dj$ and
\[
 \ell\le\min(A-da,B-db,C-dc)<u.
\]
For a maximum-coordinate rule, require all three gaps nonnegative and apply the same band to their maximum. The translation is then unique. Add the applicable weights to get the incidence $I(e)$ of each host corner $e$. For an independent integer count, the code handles the lower threshold $t=\ell$ by adding its weight and handles $t=u$ by subtracting it. At fixed $h,A$ the admissible $B$ for threshold $t$ form the interval $[db+t,N-h-2-A-dc-t]$ when $A\ge da+t$. For a general signed term with shifts $(r,s,t)$, use the interval $[db+s,N-h-2-A-dc-t]$ when $A\ge da+r$. Integer interval additions followed by a scan cover every host position.

The manuscript's line identity bounds the host's total number of rainbows by $U_N=\binom N2-(N-1)+\lfloor(N-1)/3\rfloor$. The same bound applies separately inside every translated copy of $T_m$ in the host. The certificate assigns a nonnegative integer coefficient $c_H$ to selected such copies $H$. A sorted translation $(i,j,k)$ stands for each distinct permutation of those coordinates, with $m=N-i-j-k$. Its total contribution to the ceiling is $c_H U_m$ per copy. A host corner of step $h$ and base $(A,B,C)$ belongs to that copy exactly when $A\ge i$, $B\ge j$, and $C\ge k$ for the chosen ordering. These inequalities already imply $h\le m-2$.

Subtract the weights of all covering copies from each host incidence to form $I'(e)=I(e)-\sum_{H\ni e}c_H$. The maximum possible rainbow score is bounded by
\[
 V=\sum_H c_H U_{|H|} + \text{sum of the } U_N \text{ largest values of } \max(0,I'(e)),
\]
where $|H|$ denotes the triangle's order. Indeed the original score is the sum of the residuals on the rainbow set plus $\sum_H c_H r(H)$, where $r(H)$ counts the rainbows in $H$. Each local count satisfies its own line bound, and the whole set has at most $U_N$ elements. For side 144 the translated copies contribute 397,458,186,959,858 and the ranked residual contributes 10,115,750,201,381,457. Together they give $V=10,513,208,388,341,315$. The lower score is $J=10,531,184,078,145,519$, hence **$J-V=17,975,689,804,204>0$**. A proper square of side $N$ would force its triangular subregion to satisfy both counts. Their strict inequality proves the bound. [Three-color line identity and embedding argument](../../manuscript/main.tex)

## Reproduction

Run the first command to check the exact integer contradiction against the archived catalogs. To reconstruct all the inputs, run the remaining commands in the same directory. The finite refutations use python-sat and drat-trim. The triangle enumeration uses C99 and the Python standard library.

~~~sh
python verify_triangle_grid.py
python verify_square_patches.py /path/to/drat-trim --cache /path/to/proofs
python verify_minimizer_extensions.py --through-12
python verify_order16_interior.py /path/to/drat-trim --improved
cc -O3 -std=c99 verify_rainbow_neighborhood.c -o rain_search
cc -O3 -std=c99 verify_triangle_stream.c -o triangle_stream
cc -O3 -std=c99 verify_triangle_extensions.c -o triangle_extend
python verify_triangle_grid.py --rebuild ./rain_search ./triangle_extend --jobs 4 --stream-extend ./triangle_stream --rup-checker /path/to/drat-trim
~~~

To reproduce the order-13 catalog and order-14 obstruction separately, run **python verify_triangle_stream.py ./rain_search ./triangle_stream --jobs 4 --order-13-through-12**. The [boundary-deletion recurrence](LOCAL_RAINBOW_MINIMA.md) describes why the enumeration covers every proper coloring within its rainbow budget.
