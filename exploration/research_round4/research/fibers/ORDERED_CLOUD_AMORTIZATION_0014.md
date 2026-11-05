# Ordered cloud cuts and a retained routing moment

This note isolates one consequence of ordered completion-cloud separation
that is not visible in the scalar overlap bound.  It is an auxiliary lemma
for a possible amortized attack on S11.  It does not prove S11.

## 1. Setup

Translate the source so that

```text
A subset {0,...,L}.
```

For `d>0`, write

```text
F_d={x:x,x+d in A},
z_d(x) in {+1,-1}
```

for the actual color of the cell `(x+d,x)`.  Fix two different offsets

```text
0<d<e,        h=e-d.
```

The starts of the corners whose two offset-`d` cells have separation `h`
are

```text
G_{d,e}={x:x,x+h in F_d}.
```

For `x in G_{d,e}`, put

```text
L_x=(x+d,x),       Q_x=(x+e,x),       R_x=(x+e,x+h).
```

These are a corner of step `h`.  In particular `x in F_e`.  The equal
pair of this corner is a diagonal pair `{L_x,R_x}`, a column pair
`{L_x,Q_x}`, or a row pair `{Q_x,R_x}`.

## 2. One-cut routing lemma

**Lemma.**  Fix a sign `s` and let

```text
B_s={x in G_{d,e}:z_e(x)=s}.
```

Partition `B_s` into the following three sets:

```text
J_s={x:z_d(x)=z_d(x+h)=-s},
C_s={x:z_d(x)=s,  z_d(x+h)=-s},
R_s={x:z_d(x)=-s, z_d(x+h)=s}.
```

Then

```text
|J_s|<=1,                                                   (1)
x<y for every x in C_s and y in R_s.                       (2)
```

Here `J_s` consists of the corners whose equal pair is diagonal,
`C_s` of those whose equal pair is in column `x`, and `R_s` of those
whose equal pair is in row `x+e`.  Thus, after deleting at most one
diagonal exception, the column-routed starts form a prefix and the
row-routed starts form a suffix.  The cut is taken in the actual integer
order, so it retains the positions inside the interval `[0,L-e]`.

**Proof.**  Properness excludes
`z_d(x)=z_d(x+h)=z_e(x)=s`; the three displayed cases therefore exhaust
`B_s`.  Suppose `x<y` were two members of `J_s`.  The offset-`d` cells
with starts `x` and `y+h` both have sign `-s`, so they force their
completion `(y+e,x)` to sign `s`.  But the offset-`e` cells with starts
`x<y` both have sign `s`, and they force the same completion `(y+e,x)`
to sign `-s`.  This contradiction proves (1).  It is also the usual
one-difference instance of the signed-fiber Golomb property.

For (2), suppose instead that `y<x` for some `x in C_s` and
`y in R_s`.  The two offset-`d` cells with starts `y` and `x+h` are

```text
(y+d,y),       (x+e,x+h),
```

and both have sign `-s`.  Their completion is `(x+e,y)`, so properness
forces that cell to sign `s`.  On the other hand, the two offset-`e`
cells with starts `y<x` are

```text
(y+e,y),       (x+e,x),
```

and both have sign `s`.  Their completion is the same cell `(x+e,y)`,
which is therefore forced to sign `-s`, a contradiction.  Hence every
member of `C_s` precedes every member of `R_s`, proving (2).  This is the
ordered completion-cloud separation written directly in row/column
routing coordinates.

The direction of the cut does not depend on `s`: column routes always
come first and row routes always come last.  This is the useful coupling
between the actual color classes on offsets `d` and `e`.

## 3. Exact weighted cut certificate

Let `B_s\J_s={b_1<...<b_m}`.  Give the possible column and row equal
pairs at start `b_i` arbitrary nonnegative weights `a_i` and `b_i'`,
respectively.  The lemma gives an integer `k`, `0<=k<=m`, for which the
weight of the actual row/column equal pairs is exactly

```text
sum_{i<=k} a_i + sum_{i>k} b_i'.                           (3)
```

Consequently it is at least the explicit one-dimensional cut value

```text
Cut(B_s\J_s;a,b')
  = min_{0<=k<=m}
      (sum_{i<=k} a_i + sum_{i>k} b_i').                  (4)
```

The location of the possible diagonal exception need not be known in
advance.  If `g_j` is the nonnegative weight assigned to the diagonal
equal pair at a possible exception `j in B_s`, define `g_bot=0` and
`B_s\{bot}=B_s`.  The total equal-pair weight contributed by the corners
in `B_s` is at least

```text
min_{j in B_s union {bot}}
  [ g_j + Cut(B_s\{j};a,b') ].                            (5)
```

This is a concrete cut-packing certificate.  Unlike a separate minimum
for each row graph and column graph, it forces all corners in the block
`(d,e,s)` to use one common cut.  Weights in (4)--(5) may depend on the
actual coordinate `b_i`, on the available row `b_i+e`, and on the
available column `b_i`; no replacement of the source by a cardinality
profile is required.

## 4. The signed rank and coordinate moments

Write

```text
c=|C_s|,       r=|R_s|,       m=c+r,
rho_i=+1 on C_s and rho_i=-1 on R_s
```

after the possible exception has been removed.  Since the route vector
is `c` plus signs followed by `r` minus signs, direct integer summation
gives the exact signed rank moment

```text
sum_{i=1}^m (2i-m-1) rho_i = -2cr.                        (6)
```

There is also a coordinate form which retains gaps in `A`.  Let

```text
Gamma_{d,e,s}=sum_{x in C_s, y in R_s}(y-x).
```

Then

```text
m( sum_{x in C_s}x - sum_{y in R_s}y )
 -(c-r)( sum_{x in C_s}x + sum_{y in R_s}y )
   = -2 Gamma_{d,e,s}.                                    (7)
```

Equivalently, if `bar{x}` is the mean of the `m` routed starts,

```text
sum_{x in C_s}(x-bar{x})
 -sum_{y in R_s}(y-bar{x})
   = -(2/m) Gamma_{d,e,s}.                                (8)
```

When `c,r>0`, all column starts precede all row starts.  Distinct integer
positions therefore give

```text
Gamma_{d,e,s} >= cr(c+r)/2,                               (9)
```

with equality when the routed starts are consecutive integers.  Also
all starts lie in `[0,L-e]`, so

```text
Gamma_{d,e,s} <= cr(L-e).                                 (10)
```

Formula (6) is the rank-only residue of (7); formula (7) keeps the actual
separation and hence the span.  Both vanish if one route type is absent,
which correctly records the high-load examples in which all completions
choose the same direction.

To check (6), the coefficient sum is zero and the first `c` coefficients
sum to `c(c-m)=-cr`; changing the sign on the remaining coefficients
doubles this value.  For (7), expanding its left side gives

```text
2r sum_{x in C_s}x - 2c sum_{y in R_s}y
 = -2 sum_{x in C_s,y in R_s}(y-x).
```

For (9), replace the ordered starts by their ranks `1,...,m`; closing any
integer gap can only decrease every cross-cut distance.  The resulting
sum is

```text
sum_{i=1}^c sum_{j=c+1}^{c+r}(j-i)=cr(c+r)/2.
```

## 5. Exact remaining amortization gap

Every corner belongs to exactly one block `(d,e,s)`.  If `T` is the
number of corners and `H_D` is the number whose equal pair lies in a
difference fiber, then the preceding partition gives the exact identities

```text
T   = sum_{d<e,s} (|J_s|+|C_s|+|R_s|),
H_D = sum_{d<e,s} |J_s|,
T-H_D = sum_{d<e,s} (|C_s|+|R_s|).                        (11)
```

Thus the cut lemma refines the row/column part of the exact equal-pair
budget by locating its routes; it does not create an additional count of
equal pairs.

The moment inequalities can be summed without loss.  For arbitrary
nonnegative multipliers `lambda_{d,e,s}`, with zero contribution when
`c+r=0`, (8)--(9) give

```text
sum_{d<e,s} lambda_{d,e,s}
  [ sum_{x in C_s}(x-bar{x})-sum_{y in R_s}(y-bar{x}) ]
 = -sum_{d<e,s} lambda_{d,e,s} 2 Gamma_{d,e,s}/(c+r)
 <=-sum_{d<e,s} lambda_{d,e,s} |C_s||R_s|.                (12)
```

The exact remaining inequality is a global lower bound for the left side
of (12), or equivalently a global upper bound for its gap-energy middle
term, obtained from the shared cell signs and the finite interval
`[0,L]`.  A useful bound must control the repeated appearances of the
same endpoint **cell and color variable** across different blocks;
applying (10) separately gives only

```text
sum lambda 2 Gamma/(c+r)
 <= sum lambda 2|C_s||R_s|(L-e)/(c+r),                    (13)
```

which keeps the span but loses the shared colors.  Similarly, (9) alone
only lower-bounds a sum which may reuse the same endpoint cell in many
blocks.

There is no pair-edge overlap between different blocks: each physical
pair edge belongs to at most one corner.  This fact also identifies a
necessary caution in using (4)--(5).  Arbitrary direction-dependent
weights give a valid lower bound for a weighted equal-edge total, but
that total has no automatic upper bound by `T`.  If all three pair types
of a corner are instead given the same corner weight, the usual weighted
upper budget is available, but the cut minimum merely returns that one
weight per corner and yields no gain.

Thus the exact cut-language gap is to couple direction-dependent row and
column weights to a legitimate global upper bound or dual potential built
from the shared line-color variables.  Such a potential would have to
dominate the weighted equal-edge total for every coloring while leaving
the sum of the one-cut minima (5) quantitatively large.  No such dual
potential is proved here.  The new retained datum for that task is that
each block has one common cut and the exact negative moment (6)--(8);
allowing an independent route for every corner discards precisely this
datum.
