# Rainbow Ls on the outer sides at orders 14 through 18

Let $14\le n\le18$ and let $r$ count the rainbow Ls in a proper
three-coloring of $T_n$. The [baseline result](../boundary_certificates_20261115/LOCAL_RAINBOW_MINIMA.md#fourteen-through-eighteen-rainbows-at-orders-14-through-18)
gives $r\ge n$. If $r=n$, **exactly two or three rainbow Ls meet
the boundary. Each meets a single outer side, and these sides are
different.** The inner $T_{n-3}$ then contains $n-2$ or $n-3$ rainbows.
The assertion is conditional on the rainbow count. It also gives
unconditional inequalities for weighted searches.

## The order-14 calculation

With fourteen rainbows, each outer side can contain at most one because
deleting it leaves at least thirteen. The [multi-side refutations](ORDER14_BOUNDARY.md)
show that a boundary rainbow can touch only one side. To exclude a
single boundary rainbow, choose its side by geometric symmetry. The
formula specifies one such rainbow, permits thirteen more in the interior,
and forbids all remaining boundary rainbows. Its RUP refutation applies
to all three choices of side.

For the case of zero boundary rainbows, the three extreme cells form
a bichromatic L. A geometric symmetry and a palette permutation put
their colors in the order 0, 0, 1. Inside $T_{14}$, take $T_4$ at
scale six using $(x,y)\mapsto(1+6(x-1),6y)$. All four Ls of this
six-cell triangle meet multiple sides of $T_{14}$ and must be bichromatic.
Of the $3^6$ possible words, eight satisfy the fixed outer colors and
these four conditions. The verifier enumerates them and takes the least
representatives under geometric and palette symmetries. The six resulting
words are `001021`, `002021`, `010001`, `010011`, `020001`,
and `022021`. All six formulas have RUP refutations.

For a translated order-12, order-11, or order-10 triangle, an outside
rainbow budget follows from its [local minimum](ORDER14_EXTENSIONS.md).
If the entire marked side is outside, its one rainbow has already
consumed one unit of that budget. The formula subtracts that unit
and counts the remaining exterior marks.

## Higher orders

At orders 15 and 16 the extra refutations exclude every coloring with
at most $n$ rainbows all lying in the interior. Their exterior budgets
use the unconditional floors at orders 14 and 15 and the improved
small-subtriangle floors under total budget at most sixteen. Any embedded
$T_{11}$, $T_{12}$, or $T_{13}$ extends inside the host to a unit-step
$T_{14}$ by decreasing its nonnegative boundary margins until they sum
to $n-14$. The enclosed $T_{14}$ then contains at most sixteen rainbows.
At orders 17 and 18 the [baseline boundary certificates](../boundary_certificates_20261115/verify_rainbow_boundary_layers.py)
already force a boundary rainbow in every proper coloring.

Proceed by induction on $n$. At $r=n$, deleting any one outer side
removes at most one rainbow since the child has order $n-1$. If
there were only one boundary rainbow, deleting a side that it touches
would leave a child with exactly $n-1$ rainbows. Two outer sides of
the child are portions of the original outer sides. Neither contains
a remaining rainbow. This contradicts the induction hypothesis that
the child has rainbows on at least two different sides.

There are therefore at least two boundary rainbows, with disjoint sets
of touched sides. If one touched two sides, another would have to touch
the third. Deleting that third side would leave the first rainbow on at
least two sides of a child having exactly $n-1$ rainbows, again a
contradiction. A rainbow touching all three sides already rules out a
second one. This proves the asserted structure through order 18.

In particular, if the order-14 lower bound increases from 14 to 15,
the lower bounds on orders 15 through 18 increase to **16, 17, 18, 19**.
A putative coloring at the old bound has a boundary rainbow. Deleting
its side would violate the improved lower bound at the preceding order.
The [complete two- and three-side coarse refutations](ORDER14_MIN15.md)
subsequently establish $r_{14} \ge 15$ unconditionally, activating these
upgraded minima.

## Unconditional weighted inequalities

Let $s_1,d_2,d_3$ be the numbers of rainbow Ls meeting exactly one, two,
or three outer sides. At every order $14\le n\le18$,

$$
2r+s_1\ge 2n+2,\qquad 3r-d_2-2d_3\ge 3n.
$$

The first follows from $s_1\ge2$ at $r=n$. At $r\ge n+1$ it follows
from $s_1\ge0$. The second was proved [at order 14](ORDER14_BOUNDARY.md).
For $n\ge15$ and $r=n$, both discounts vanish. At $r=n+k$ with $k\ge1$,
each side contains at most $k+1$ rainbows by deletion. Thus
$2d_2+3d_3\le3(k+1)$. Since $d_3\le1$, this gives
$d_2+2d_3\le\lfloor(3k+4)/2\rfloor\le3k$.
At orders 17 and 18 one more inequality is
$r+s_1+d_2+d_3\ge n+2$, since every proper coloring has a boundary rainbow.

## Reproduction

The nine new traces are in `orders-14-to-18-boundary-layers.zip` with
SHA-256 `183048d5a82b57de50744e2b2aee25d604dfe9e6c9586f814a16514273a8f702`.
The [manifest](data/tight_shells.json) records the individual formula and
proof hashes. With python-sat installed, run the following command from
this directory after extracting the archive.

```sh
python3 verify_tight_shells.py --proof-dir /path/to/extracted-proofs \
    --drat-trim /path/to/drat-trim --rup-check /path/to/rup_check --jobs 2
```
