# Rainbow counts forced by an enclosing square

A free proper order-13 triangle can contain just eleven rainbow directed Ls. An order-12 triangle can contain six. Requiring the coloring to extend to a particular square raises each lower bound.

| Triangle | Enclosing square | Offset of the triangle | Colorings excluded up to palette permutation | Forced rainbows |
|---|---|---|---:|---:|
| Order 13 | 17 by 17 | (5, 0) | 126 | 12 |
| Order 13 | 18 by 18 | (0, 0) | 126 | 12 |
| Order 12 | 18 by 18 | (3, 3) | 1,578 | 8 |
| Order 12 | 18 by 18 | (0, 0) | 1,578 | 8 |
| Order 12 | 18 by 18 | (7, 0) | 1,578 | 8 |
| Order 12 | 18 by 18 | (3, 3) | 11,028 | 9 |

At offset $(i,j)$ the triangle cell $(x,y)$, with $0\le y<x<m$, occupies square cell $(i+x-1,j+y)$. Reflecting the square by $(x,y)\mapsto(s-1-y,s-1-x)$ preserves directed Ls and the triangular shape. Thus every row in the table also holds at offset $(s-m+1-j,s-m+1-i)$. Relabeling colors and taking positive integer dilations preserve each conclusion.

## Finite proof

The complete [triangle catalogs](LOCAL_RAINBOW_MINIMA.md) contain every proper coloring through the cutoffs. Expand each geometric orbit through its six coordinate permutations, normalizing colors by first appearance. At order 13 this gives all 126 words with eleven rainbows. At order 12 there are 204 with six rainbows and 1,374 with seven.

For each square and offset impose exactly one of three colors on each cell. For every directed equal-leg L forbid its three monochromatic assignments. Require the triangular cells to match one of the listed words. The formula for each group of words is unsatisfiable. The checker rebuilds its clauses from the literal square coordinates and verifies a reverse unit propagation refutation. It partitions the two order-13 rows into 1 and 6 groups and the three 1,578-word checks into 53 groups each. The stronger interior check uses 184 groups and checks every oriented word.

The canonical source catalogs and the formulas are fixed. Running **python verify_square_patches.py /path/to/drat-trim --cache /path/to/proofs** reconstructs and checks the proof traces. The first run uses python-sat with Glucose 4 and [drat-trim](https://github.com/marijnheule/drat-trim). Cached compressed traces can subsequently be checked without a SAT solver.

## Where order 13 gains a rainbow

Write $(a,b,c)$ for the three nonnegative translation coordinates in the host triangle and let $d$ be the dilation. They obey $a+b+c=N-2-11d$. The order-13 bounding square occupies columns and rows starting at $(1+a+b,b)$ and spanning $11d$ in each direction. The 17-square fits at the first offset exactly when $1+a+b\ge5d$ and $1+a+c\ge5d$. The 18-square fits at one of its two reflected offsets when $b\ge6d$ or $c\ge6d$.

In particular **every order-13 copy of dilation $d$ in the standard host triangle has at least twelve rainbows if $N\ge22d$** and the host square is proper. If none of the offsets fits then $a+\min(b,c)\le5d-2$ and $\max(b,c)\le6d-1$. Adding gives $N-2-11d\le11d-3$, contradicting $N\ge22d$. The weighted verifier tests the actual bounding squares individually, which also covers some larger dilations.

## Where order 12 gains two rainbows

**If $N\ge24d$, every order-12 triangle of dilation $d$ in the standard $T_N$ of a proper $N$ by $N$ square contains at least eight rainbows.** Write $a+b+c=N-2-10d$. The offsets $(0,0)$ and $(7,7)$ fit if $c\ge7d$ or $b\ge7d$, respectively. The offset $(7,0)$ fits if both $1+a+b$ and $1+a+c$ are at least $7d$. If all three fail, then $a+\min(b,c)\le7d-2$ and $\max(b,c)\le7d-1$. This gives $N-2-10d\le14d-3$, contrary to $N\ge24d$. The offset $(3,3)$ supplies additional placements near the cutoff.

## Even dilations of the order-13 triangle

Every order-13 triangle of **even dilation** in a proper square contains at least **twelve** rainbows. Write its dilation as $2e$. Its bounding square contains a 23 by 23 lattice at spacing $e$, and the triangular cells occupy positions $(2(x-1),2y)$ in that lattice. This entire enclosing lattice lies inside the bounding square of the original triangle, including when the triangle touches the edge of the host.

A copy with eleven rainbows would realize one of the 126 oriented minimum words. Divide them into six groups of 21 and impose each group at the displayed stride-two positions. The six refutations rule out every group. Run **python verify_square_patches.py /path/to/drat-trim --stride 2 --cache /path/to/proofs** to reconstruct and check these formulas. This adds a forcing condition at every even dilation, including those outside the range $N\ge22d$.

## Thirteen rainbows in an order-13 triangle

All 2,928 oriented words with at most twelve rainbows fail at each of the offsets $(3,3)$, $(6,0)$ and $(0,0)$ in a proper 18 by 18 square. Each check partitions the complete [488-class catalog](triangle_13_through_12.txt.xz) into 61 groups of 48 words and verifies every refutation. Run **python verify_square_patches.py /path/to/drat-trim --cutoff 12 --cache /path/to/proofs**.

In particular, every order-13 triangle of dilation $d$ in the standard triangle of a proper square has at least thirteen rainbows whenever $N\ge23d$. In translation coordinates $a+b+c=N-2-11d$, the offset $(6,0)$ fits whenever $1+a+\min(b,c)\ge6d$. The offset $(0,0)$ or its reflection fits whenever $\max(b,c)\ge6d$. If all fail, addition gives $N-2-11d\le12d-3$. This contradicts the assumed side length. The interior offset also covers positions outside this uniform guarantee.
