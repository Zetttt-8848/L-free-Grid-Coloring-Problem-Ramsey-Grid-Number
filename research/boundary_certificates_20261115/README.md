# Finite certificates for directed L-grid Ramsey numbers

The [three-color proof at side 461](THREE_COLOR_461.md) gives **$21\le R_3\le461$**. It combines a [forced-color exclusion](NO_OPTIMAL_461.md) with a complete count of 35-letter diagonal words. The side-462 proof below uses fewer external Golomb inputs.

The [four-color proof at side 21,948,404](FOUR_COLOR_WINDOW.md) combines a decreasing distance capacity with a bound shared across twelve consecutive shifts. The [earlier 21,953,510 proof](FOUR_COLOR_SIDON.md) uses the finite Sidon cardinality theorem. The accompanying [recursive span proof](FOUR_COLOR.md) gives a self-contained four-color upper bound of **21,987,409**. The fixed-word certificate below tests the next three-color obstruction. The [global occurrence certificate](RULER_OCCURRENCES.md) also restricts the entire 461 diagonal to at most two optimal completion classes.

15 November 2026. **PROVED with external inputs** G(24) >= 425 and G(25) >= 480. For the directed shape
$$
 (x,y),\quad (x+d,y),\quad (x+d,y+d), \qquad d>0 ,
$$
every three-coloring of $\{0,\ldots,461\}^2$ contains a monochromatic copy. Thus $R_3\le462$. The previously checked $20\times20$ construction gives $21\le R_3\le462$. [Lower-bound construction](https://arxiv.org/html/2312.01159v1)

## Numerical certificate

A proper square would require the expression in the last column to be nonpositive. The three-color capacities in the table use only the certified span lower bounds for 24- and 25-mark Golomb rulers. The proof checkers run locally. The external exhaustive Golomb searches are cited inputs.

| Side | Overlap layers $k$ | Baseline $G_0$ | Certified lower bound on loss $D$ | $G_0+3D$ |
|---:|---:|---:|---:|---:|
| 463 | 1–10 | −3,527,580,772 | 1,322,324,010 (attained) | +439,391,258 |
| 462 | **1–36** | **−7,476,723,318** | **2,500,000,000** | **+23,276,682** |
| 462 | 1–23 | −7,476,723,318 | 2,492,241,107 | +3 |

For 462, 2,500,000,000 is a universal lower bound on the weighted loss. Its exact minimum is open here. An explicit tested word has loss 3,325,904,997. The proof uses the lower bound alone.

## From the square to a single word

In a hypothetical proper $n\times n$ square let $z_i$ be the color of diagonal cell $(i,i)$. At each $d>0$ let $R_d$ count the starts $u$ with $z_u=z_{u+d}$. For each such $u$, let $c=z_u$ and let $e$ be the color of $(u+d,u)$. Since $e\ne c$, these starts fall into six mutually disjoint classes $B_{c,e}$, all in $[0,n-d-1]$.

**Each class is a Golomb ruler.** Fix $c$ and let $F=\{u:z_u=z_{u+d}=c\}$. The weak triangle indexed by $v,u\in F,\ v\ge u$ has cell color $\chi(v+d,u)$. Every cell avoids $c$, since $(u,u)$ and $(v+d,v+d)$ have color $c$. The coordinate translation preserves the directed triples. The $e$-colored diagonal points of this binary triangle are exactly $B_{c,e}$. For $s<t$ among those points the strict cell $(t,s)$ in the translated coordinates must have the other color. Suppose $a,a+h$ and $a+t,a+t+h$ were two pairs among the points with the same positive difference, $t>0$. Then the three strict cells
$$
 (a+h,a),\quad (a+t+h,a),\quad (a+t+h,a+t)
$$
all have that other color and form a directed L of step $t$. This contradiction also covers $h=t$. [Repository six-class proof](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/blob/6630b5e27a07a35ac5a06af325551265a692daf6/research/kernel_compatibility_20261108/geometry/SIX_CLASS_LEMMA.md)

A 25-mark ruler has span at least 480 and a 24-mark ruler has span at least 425. On the two sides considered, every class therefore has at most 24 marks. Write $b=n-425$. The minimum of a 24-mark class must lie among the first $k=b-d$ starts if $k>0$. When $k\le0$, there are no such classes. There are at most $\min(k,6)$ large classes when $k>0$, because their minima are distinct. This gives $U_d=138+\min(6,\max(0,b-d))$ as the baseline bound on $R_d$. [OGR-24 exhaustive result](https://blogs.distributed.net/2004/11/) · [OGR-25 exhaustive result](https://blogs.distributed.net/2008/10/)

Keep the actual prefix word $z_0,\ldots,z_{b-1}$. For $1\le k<b$ put $d=b-k$ and
$$
 m_c(k)=\#\{0\le i<k:z_i=z_{i+d}=c\},\qquad
 T_k=\sum_{c=0}^2\min(2,m_c(k)).
$$
Each color has just two possible completion colors. Each 24-mark class needs a distinct matching start of its color. The number of such classes is therefore at most $T_k$, so $R_{b-k}\le138+T_k$. Every $\delta_k=\min(k,6)-T_k$ is nonnegative.

Take $w_i=i(86-i)$ for $1\le i\le85$, zero elsewhere, and $a_d=\sum_i w_iw_{i+d}$. If $f_c$ is the indicator of diagonal color $c$ on the full diagonal, then $\sum_c f_c=1_{[0,n-1]}$. At every position apply $(p+q+r)^2\le3(p^2+q^2+r^2)$ to the three convolutions $f_c*w$. Summing over positions and expanding gives
$$
 n a_0+2\sum_{d>0}(n-d)a_d
 \ \le\ 3n a_0+6\sum_{d>0}R_d a_d .
$$
Since $a_d\ge0$ and $a_d=0$ for $d>84$, define
$$
 G_0=-n a_0+\sum_{d=1}^{84}(n-d-3U_d)a_d,\qquad
 D_K(z)=\sum_{k=1}^K a_{b-k}\delta_k .
$$
The preceding inequalities give **$G_0+3D_K(z)\le0$** for the actual prefix of every proper square and every $K\le b-1$. Thus a certified lower bound on $D_K$ large enough to reverse the sign rules out the square. At $n=462$, $b=37$ and $G_0=-7{,}476{,}723{,}318$. The integer cutoff for a contradiction is $2{,}492{,}241{,}107$.

## How the finite proof covers every word

The search assigns the physical positions $0,b-1,1,b-2,\ldots$, with the middle position assigned once. It tests all 36 shifts on this same word when $n=462$. It uses only a simultaneous permutation of color names. The first position can be fixed to color 0 with multiplicity 3. The second can be 0 with multiplicity 1 or 1 with multiplicity 2. At every later position all three choices occur.

For a partial word, define $P_c(d)$ as the starts $i<b-d$ for which neither endpoint $i,i+d$ has been assigned a color different from $c$. In every completion, the true color-$c$ matching starts form a subset of $P_c(d)$. The completed matching starts for the three colors are disjoint. Consequently
$$
 \widehat T_k=\min\left\{k,6,\ \sum_c\min(2,|P_c(d)|),\
                         \left|\bigcup_c P_c(d)\right|\right\}
$$
is an upper bound on the eventual $T_k$. Replacing $T_k$ by $\widehat T_k$ in $D_K$ gives a lower bound for **every** word extending the partial assignment. The checker prunes a branch only when that lower bound reaches the certificate cutoff. All summands are nonnegative, so an early exit during the sum is valid.

A pruned branch after $h$ positions accounts for its color multiplicity times $3^{b-h}$ labeled words. The leaves of the proof are disjoint. The checker sums these counts and also requires zero surviving words. At 462 its full-shift run covers exactly **450,283,905,890,997,363** words, visits **364,264,507** nodes, and prunes **242,843,004** branches. All counters fit in an unsigned 64-bit integer. The finite proof at 463 covers $3^{38}$ words. Only its first and last ten letters enter the score, so the remaining letters receive their full multiplicity. The witness **00111111110000000000000000000000000011** attains the reported ten-layer loss.

I checked the computation twice. The discovery enumeration used masks of assigned colors, one optimistic bound per color, first-use palette normalization, and the closed form for $a_d$. The supplied checker uses masks of forbidden colors, the union bound above, only the two initial color normalizations, and literal autocorrelation sums. On a seven-letter instance it first compares against literal enumeration of all 2,187 words, with 417 words on the feasible side of its test cutoff. At 463 the original Python minimizer also returns the same exact optimum.

## Which shifts make the difference

Among initial blocks of overlap layers $1,\ldots,K$, **23 is the first sufficient length at 462 for these weights and caps**. The first 23 cover shifts $d=36,35,\ldots,14$. They already give a positive certified margin. The complete 37-letter word

**0002222111220111101020020020020121121**

has $D_{22}=2{,}488{,}214{,}141$ and margin **−12,080,895**. It gives the same loss when the optional ruler-shape cap of PR 7 is included. Shorter initial blocks have loss at most $D_{22}$. This proves the threshold for initial blocks; a different subset of shifts could have a smaller cardinality. At 23 overlaps the two 23-letter ends share nine letters, so consistency through the middle is automatically enforced by the search.

## An explicit obstruction at 461

At 461 there are 36 letters and 35 nonzero shifts. Even after imposing the extra ruler-shape cap at layers 3–6, the word

**122120100110100020212021121202210012**

has full loss **3,501,823,174** and margin **−863,712,470**. The loss needed is **3,789,727,331**. This gives a counterexample to the universal loss inequality for this side, kernel, and prefix model. It is a test word for the diagonal.

I also checked whether that word triggers the local three-color requests of PR 7. In the triangular grid of its 36 positions, prescribe the diagonal and every cell whose two diagonal endpoints have equal colors. This gives 234 prescribed cells. The supplied witness colors them and chooses a color for each remaining mixed cell. All **370** triples with three prescribed cells and all **1,887** triples with exactly two prescribed cells are proper. Thus even the enlarged family containing every request from two prescribed cells is consistent on this word. Triples with two or three mixed cells remain available to a stronger argument.

## Two mixed cells change the fixed-word result

For the 36-letter word **122120100110100020212021121202210012**, the included source assignment and mixed-cell colors satisfy every directed triple with at least two prescribed cells. Here a prescribed cell has equal diagonal endpoint colors. Now include all directed triples with **at least one** prescribed cell and allow all the source and mixed colors to be chosen afresh. This finite instance is **UNSAT with a checked RUP refutation**. The word is excluded as the prefix of a proper square. Other 36-letter words remain possible under this test.

The triangle has 666 positions, with exactly one of three colors at each. The diagonal is fixed to the displayed word. Each strict cell with equal endpoint colors must avoid that common color. For each directed triple having at least one prescribed position include one three-negative-literal clause per color. This gives 1,998 variables and 19,587 clauses. For each triple the left endpoint in the lower triangle and its positive step determine its other two positions. There is no imposed geometric symmetry. A proper full square extending the word restricts to a satisfying triangle assignment.

To reproduce, run **python verify_mixed.py /path/to/drat-trim**. The checker regenerates the CNF from the word, verifies its SHA-256 and the decompressed proof digest, and requires the external checker to accept in RUP-only mode. The original discovery used CaDiCaL 1.9.5 via PySAT. The proof was reduced and verified again with drat-trim at commit **2e3b2dc0ecf938addbd779d42877b6ed69d9a985**. On Windows the same C source was compiled with **-Dgetc_unlocked=getc**. Compressed proof SHA-256 is **b584e45fe8280944391f80f2384deadcb4674008f02d63a0fa37e3d46540b623**. [Proof-checker source](https://github.com/marijnheule/drat-trim/tree/2e3b2dc0ecf938addbd779d42877b6ed69d9a985)

## Two follow-up checks from the plan

**Shared completion cells.** In PR 7's order-10 example the mixed cell $(8,3)$ receives color-0 inputs from $(9,3),(9,4)$, color-1 inputs from $(7,2),(8,2)$, and color-2 inputs from $(6,1),(8,1)$. I verified all three requests and all 19 already-prescribed triples. The supplied alternative source coloring of the *same* diagonal word admits a local choice at every mixed cell. A 37-letter sample of loss 3,325,904,997 also admits such choices, as does the 461 word above. This identifies an explicit obstacle to deriving three-color conflicts solely from diagonal matches and single mixed cells. [PR 7 request theorem](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/blob/6630b5e27a07a35ac5a06af325551265a692daf6/research/global_counting_20261108/completion/COUNTING.md)

**Four colors.** The earlier twelve-distinct-minima certificate gives $R_4\le21{,}991{,}247$. I tested retaining both endpoint ranks at $n=21{,}991{,}246$. At all 35,999 active distances, the 23 consecutive interval capacities needed for endpoint rank sums $j+q$, $0\le j,q\le11$, are constant or have one downward unit step. For a unit step after $h$ entries put $s=\min(12,h)$. Pair the first $s$ starting ranks in reverse order with the first $s$ ending ranks. Each pair has sum $s-1<h$; pair the remaining ranks identically. This realizes exactly the first-end-only capacity sum. If the window is constant every matching gives the same sum. The abstract worst-case matching therefore gives **zero strict savings at every distance**. The existing margin stays negative at this side. Further four-color progress along this route needs actual restrictions on which classes can pair their endpoints, or a finer capacity estimate. [Four-color archive](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/blob/6630b5e27a07a35ac5a06af325551265a692daf6/exploration/research_round3/four/R3_R4_REPORT.md)

## Four-color upper bound of 21,991,247


Fix a lag $d>0$ and put $p=n-d$. Every start $u$ with equal original diagonal endpoint colors $c$ belongs to one of twelve classes indexed by $(c,e)$, where $e\ne c$ is the actual completion color. These classes are disjoint in the same $p$ positions. Each class $B$ admits a properly two-colored strict source. For $u<v$ in $B$, the cell $(v+d,u)$ avoids $c$ because the diagonal endpoints $u,v+d$ both have color $c$. It avoids $e$ because $(u+d,u),(v+d,u),(v+d,v)$ would form a monochromatic L. The coordinate shift preserves all directed Ls. [Four-color source reduction](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/blob/6630b5e27a07a35ac5a06af325551265a692daf6/research/four_color_sensitivity_20261113/README.md)

Let $C(p)$ be any nondecreasing certified upper bound on the size of such a set in $p$ consecutive positions. Sorting the nonempty classes by minimum, the class of zero-based rank $j$ starts at position at least $j$. It therefore fits in $p-j$ positions. Empty classes can be padded with nonnegative upper bounds. Consequently the total number of equal-color pairs at lag $d$ satisfies
$$
 R_d\le\sum_{j=0}^{11} C(n-d-j).
$$
This is the joint count used below. The earlier certificate used $12C(n-d)$. The local calculation uses the archive's already certified capacities, with the shorter available span attached to each class. [Archived capacity proof](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/blob/6630b5e27a07a35ac5a06af325551265a692daf6/exploration/research_round3/four/R3_R4_REPORT.md)

Precisely, let $N=21{,}991{,}300$ and let $K_s$ be the archived bound for span at most $N-s-1$, $1\le s\le35999$. For a class in $n-d-j$ positions, use $s=\min(35999,N-n+d+j)$, since its span is at most $n-d-j-1$. The last table entry remains valid on every shorter span. Let $U_d$ be the sum of those twelve entries. With $w_i=i(36001-i)$, $1\le i\le36000$, and its correlations $a_d$, Cauchy on four colors gives the necessary inequality
$$
 2\sum_{d=1}^{35999}(n-d-4U_d)a_d-3na_0\le0 .
$$
The author reran the upstream checker for all 561 capacity runs and 35,999 positive distances, then evaluated the new sum both directly and by sliding sums. At $n=21{,}991{,}247$ the left side is **+19,425,438,581,938,424,787,936**. Keeping the twelve intervals at equal length gives **−249,084,824,594,960,116,300,176,576** at the same side. At $21{,}991{,}246$ the distinct-minima calculation gives **−15,150,556,292,665,326,284,166,784**. The sign change identifies where a stronger joint count first becomes useful for this certificate. [Upstream verifier](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/blob/6630b5e27a07a35ac5a06af325551265a692daf6/exploration/research_round3/four/verify_r4_profile_certificate.py)


## Reproduce

The primary proof requires a C99 compiler and the standard library. From this directory on Linux or macOS run

~~~sh
cc -std=c99 -O3 verify_462.c -o verify_462
./verify_462
~~~

On Windows with the locally installed Zig Python package run

~~~powershell
py -3.11 -m ziglang cc -std=c99 -O3 verify_462.c -o verify_462.exe
.\verify_462.exe
~~~

For independent inspection of the explicit completion witnesses and the four-color matching calculation, run **verify_followups.py** using Python 3.10 or later in the same directory. It reads **completion_witnesses.json** and the existing **r4_profile_endpoint_21991300.json**. No solver is needed to verify these witnesses. **verify_bounds.py** reproduces the preceding 463 and four-color computations. The side-462 proof uses the span bounds alone. The side-461 proof also uses uniqueness of the optimal ruler and the separate forced-color verifier.
