# Dyadic endpoint charging and its exact crowding gap

Let `A subset [0,L]` be a finite integer source whose strict completion
triangle is properly two-colored.  For `d>0`, write

```text
F_d={x:x,x+d in A},       r_d=|F_d|,
```

and let `F_d^+`, `F_d^-` be the two actual color classes of the cells
`(x+d,x)`.  Put

```text
M=binom(|A|,2)=sum_d r_d.
```

Fix an integer `H>=1` and the dyadic start-gap band

```text
I_H={h in Z:H<=h<2H}.
```

The number of corners in this band is

```text
T_H=sum_d sum_{h in I_H} |F_d intersect (F_d-h)|.          (1)
```

This note gives an ordered charging rule, a scale-descent inequality, and
a direct counterexample to a raw `T_H<=M/2` target.  It does not prove an
`O(M log L)` bound.

## 1. Fixed-gap chains

Fix `d,h>0`.  Join `x` to `x+h` when both belong to `F_d`.  The resulting
graph is a disjoint union of paths along residue classes modulo `h`.
For one component write its starts as

```text
x,x+h,...,x+ell h.
```

### Lemma 1: a component has at most six edges

The two color classes among the `ell+1` offset-`d` cells are Golomb after
division of their start differences by `h`.  A color class of size `k`
therefore has `binom(k,2)` distinct positive integer differences in
`{1,...,ell}`, so

```text
binom(k,2)<=ell.                                           (2)
```

For `ell=2m>=8`, one class has at least `m+1` elements, and
`binom(m+1,2)>2m`; for `ell=2m+1>=9`, one class has at least `m+1`
elements, and `binom(m+1,2)>2m+1`.  Thus (2) excludes every
`ell>=8`.  It remains to exclude `ell=7`.  In that case both classes must
have four elements.  A four-mark Golomb subset of `{0,...,7}` has span at
least six.
The endpoints `0,7` cannot have the same color, because the other class
would then lie in an interval of span five.

Suppose `0` has sign `+` and `7` sign `-`.  The plus class must end at `6`
and have span six.  If its consecutive gaps are `a,b,c`, its six positive
differences are distinct and lie in `{1,...,6}`.  Hence
`{a,b,c}={1,2,3}`, and avoiding an adjacent sum `1+2=3` forces

```text
(a,b,c)=(1,3,2) or (2,3,1).
```

Thus the plus class is `{0,1,4,6}` or `{0,2,5,6}`.  Their complements are
`{2,3,5,7}` and `{1,3,4,7}`, respectively; the first has span five and the
second repeats difference three.  Neither is Golomb.  This excludes
`ell=7` and proves

```text
ell<=6.                                                    (3)
```

The constant six is attainable at the level of signed fibers: the word
`0011010` on starts `0,...,6` partitions them into the Golomb sets
`{0,1,4,6}` and `{2,3,5}`.

## 2. The supported reflected corner gives an injective route charge

For an edge `x -> x+h` of a fixed-gap chain, put

```text
L_x=(x+d,x),
Q_x=(x+d+h,x),
R_x=(x+d+h,x+h).
```

If `L_x,R_x` have different colors, properness makes `Q_x` agree with
exactly one of them.  Charge the corner to `L_x` when `Q_x=L_x` in color
(a column route), and to `R_x` when `Q_x=R_x` (a row route).

This charge is injective on all bichromatic edges of the fixed `(d,h)`
chain graph.  The only possible collision would occur at the common cell
`R_x=L_{x+h}` of two consecutive edges: the first edge would have to use
a row route and the second a column route.  Then

```text
Q_x, R_x=L_{x+h}, Q_{x+h}
```

would all have the color of the common cell.  These three cells are the
supported reflected corner.  Its six supporting source marks are present
because `x,x+h,x+2h` all lie in `F_d`.  The reflected-corner constraint
therefore forbids the collision.

Consequently, if `X_{d,h}` is the number of bichromatic endpoint pairs at
this `(d,h)`, the actual route charge gives

```text
X_{d,h}<=r_d.                                              (4)
```

Also, the signed-Golomb property allows at most one monochromatic pair of
each sign at the fixed difference `h`.  Thus there are at most two
uncharged diagonal exceptions.  Lemma 1 says more geometrically that every
fixed-gap component contains at most six corners.

The point of (4) is the charge itself, rather than its scalar right side:
it sends each bichromatic corner to the endpoint cell whose color it
shares with the completion, and supported reflection proves that this
choice does not collide at a shared chain vertex.

## 3. An elementary dyadic capacity

Define

```text
g_H=max{k>=0:binom(k,2)<=H-1}
   =floor((1+sqrt(8H-7))/2).                              (5)
```

Any Golomb set contained in an integer interval of `H` positions has at
most `g_H` elements, because all its positive pair differences belong to
`{1,...,H-1}`.

Fix one start `x in F_d`.  Its right neighbors `y` with
`y-x in I_H` lie in an interval of `H` positions.  Splitting them by their
two actual colors and applying (5) to each signed fiber gives at most
`2g_H` neighbors.  Counting every band edge from its left endpoint yields
the valid scale bound

```text
T_H<=2g_H sum_d r_d=2g_H M.                               (6)
```

This is `O(M sqrt(H))`, rather than `O(M)`.  It records the best immediate
cell capacity supplied by signed-Golomb alone.

## 4. Crowded route charges descend to smaller gaps

The ordered route charge gives a more structured refinement for the
bichromatic part.  For a cell `p=(x+d,x)`, let

```text
lambda_right(p)=number of column-route charges to p
                with h in I_H,
lambda_left(p) =number of row-route charges to p
                with h in I_H.
```

The neighboring offset-`d` cells in either bucket all have color opposite
to `p`.  Two neighbors in the same bucket have start difference strictly
less than `H`; hence they form a same-color pair in a smaller gap.  Put

```text
W_H=sum_p [binom(lambda_right(p),2)
           +binom(lambda_left(p),2)],                     (7)
```

and let

```text
S_<H=sum_d sum_{eps in {+,-}}
       |{{y,z} subset F_d^eps:0<z-y<H}|.                  (8)
```

There is an exact double count of `W_H` by a smaller-gap leaf pair and a
center which receives both associated route charges.  A fixed leaf pair
`y<z` of sign `eps` can have at most `g_H` centers to its left: all such
centers have sign `-eps` and lie in the interval

```text
z-2H < x <= y-H,
```

which has at most `H` integer positions.  The same argument gives at most
`g_H` centers to its right.  Therefore every leaf pair in (8) has total
multiplicity at most `2g_H`, and

```text
W_H<=2g_H S_<H.                                           (9)
```

Let `X_H` be the total number of bichromatic corners in (1).  There are
two directional buckets for each of the `M` cells and the route charge
counts every bichromatic corner once, so

```text
sum_p(lambda_right(p)+lambda_left(p))=X_H.
```

Cauchy--Schwarz applied to the `2M` bucket sizes gives

```text
W_H >= X_H^2/(4M)-X_H/2.                                 (10)
```

Combining (9)--(10) produces the dyadic descent inequality

```text
X_H^2/(4M)-X_H/2 <= 2g_H S_<H.                           (11)
```

Every term in (11) comes from actual shared cell colors.  In particular,
the multiplicity `2g_H` counts centers in the two physical directions;
it is not a per-completion load assumption.

## 5. A coefficient-one-half per-scale bound is false

Take the dilated five-mark interval

```text
A_H={0,H,2H,3H,4H}.
```

It has a proper two-coloring obtained by assigning, in increasing row and
then increasing column order,

```text
(H,0)                         0
(2H,0),(2H,H)                 1 0
(3H,0),(3H,H),(3H,2H)         0 0 1
(4H,0),(4H,H),(4H,2H),(4H,3H) 1 1 0 0.                  (12)
```

The ten corner color triples, grouped by difference-fiber offsets
`H,2H,3H`, are

```text
offset H:  010, 001, 010, 001, 010, 100,
offset 2H: 100, 110, 010,
offset 3H: 011.
```

All are nonmonochromatic.  Thus (12) is a legitimate properly colored
source, not merely a signed-fiber profile.

The band `I_H` contains the start gap `h=H`.  Its corner count is

```text
T_H=(4-1)+(3-1)+(2-1)=6,
M=binom(5,2)=10.                                          (13)
```

Hence

```text
T_H=(3/5)M>M/2.                                           (14)
```

So a universal raw estimate `T_H<=M/2` cannot hold at any binary scale.
A coefficient-one-half statement would need an additive correction, a
different allocation of rectangles between scales, or cancellation with
a neighboring-scale quantity.

## 6. Exact remaining inequality

Inequality (11) is the concrete gain from crowded ordered charges, but it
does not control isolated charges: its lower bound is nonpositive when
`X_H<=2M`.  It therefore cannot by itself reach even the necessary
coefficient `3/5` indicated by (14).  Moreover, the present multiplicity
bound in (9) is `2g_H`, of order `sqrt(H)`.

The remaining dyadic task is now precise.  One needs a cross-gap
properness inequality which does at least one of the following:

```text
(a) charges singly occupied route buckets as well as the wedges in (7),
or
(b) replaces the pointwise 2g_H multiplicity in (9) by an amortized
    constant through the shared completion colors at different h.
```

The supported reflected-corner rule supplies exactly the same-`h`
injectivity in Section 2.  It does not by itself compare two distinct
gaps `h_1,h_2 in I_H` charged to the same cell; that is the missing
inequality.  Any successful `O(M log L)` argument along this route must
add that cross-gap coupling and must accommodate the explicit `3M/5`
single-scale example above.
