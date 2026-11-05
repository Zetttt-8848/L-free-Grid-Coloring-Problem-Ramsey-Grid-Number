# Simultaneous three-color fiber derivations

Base: `R4-RESEARCH-0001`.

This note records auxiliary consequences of the two-color structure of the
strict completion triangle.  Every displayed claim labeled **PROVED** is a
direct consequence of corner-freeness and the definitions.  No improved
Ramsey bound is claimed.

## Setup

Let `A` be a monochromatic set on the diagonal of offset `sigma` in a
corner-free three-color grid.  Its strict completion triangle is

```text
T(A) = {(v+sigma,u) : u,v in A and u<v}.
```

The source color is absent from `T(A)`, so label the two possible colors on
`T(A)` by `+` and `-`.  For `d>0`, put

```text
F_d = A intersect (A-d),
F_d^eps = {u in F_d : (u+d+sigma,u) has color eps},  eps in {+,-}.
```

Thus `F_d=F_d^+ disjoint-union F_d^-`.  The inherited forcing lemma says
that both signed fibers are Golomb sets.

For `u<v` in `F_d^eps`, define

```text
Phi_d(u,v) = (v+d+sigma,u),
Q_d^eps = {Phi_d(u,v) : u<v in F_d^eps}.
```

The three cells

```text
(u+d+sigma,u), (v+d+sigma,u), (v+d+sigma,v)
```

form a corner of step `v-u`.  Its first and third cells have color `eps`.
The middle cell lies in `T(A)`, so it has color `-eps`.  Consequently

```text
u in F_{d+v-u}^{-eps}.                                      (1)
```

This is the pointwise fiber-propagation rule.

## 1. Opposite-cloud separation

### Lemma (**PROVED**)

For every positive `d,e`,

```text
Q_d^+ intersect Q_e^- = empty,
Q_d^- intersect Q_e^+ = empty.                              (2)
```

For the more informative ordered form, fix `0<d<e`, set
`Delta=e-d`, and define

```text
C = F_d^+ intersect F_e^-,
D = F_e^- intersect (F_d^+ - Delta)
  = {q in F_e^- : q+Delta in F_d^+}.
```

Then

```text
sum_{q in D} |{u in C : u<q}| = 0.                         (3)
```

Hence, when `C,D` are nonempty,

```text
max D <= min C.                                             (4)
```

In particular,

```text
|F_d^+ intersect F_e^-|
  + |F_e^- intersect (F_d^+ - Delta)| <= |F_e^-|+1.        (5)
```

The color-reversed inequality also holds:

```text
|F_d^- intersect F_e^+|
  + |F_e^+ intersect (F_d^- - Delta)| <= |F_e^+|+1.        (6)
```

Equivalently, extending indicators by zero outside their domains, (5) is
the two-shift correlation inequality

```text
sum_u 1_{F_e^-}(u)
      (1_{F_d^+}(u)+1_{F_d^+}(u+Delta)) <= |F_e^-|+1.      (7)
```

### Proof

Equation (1) gives color `-` to every point of `Q_d^+` and color `+` to
every point of `Q_e^-`, proving (2).

For the ordered statement, write a point of `Q_d^+` as
`Phi_d(u,v)` and a point of `Q_e^-` as `Phi_e(p,q)`.  Equality of their
columns and rows is equivalent to

```text
u=p,  v+d=q+e,
```

or `u=p` and `v=q+Delta`.  Both source pairs are valid exactly when
`u in C`, `q in D`, and `u<q`.  The map from `(u,q)` to the common point
`(q+e+sigma,u)` is injective.  Thus the left side of (3) is exactly
`|Q_d^+ intersect Q_e^-|`, which is zero by (2).

Equation (4) restates the absence of a pair `u in C`, `q in D` with
`u<q`.  Both `C` and `D` are subsets of `F_e^-`.  Moreover
`|C intersect D|<=1`: two points `x<y` in the intersection would give
the forbidden ordered pair `u=x`, `q=y`.  Therefore

```text
|C|+|D| = |C union D|+|C intersect D| <= |F_e^-|+1,
```

which proves (5).  Interchanging the signs proves (6).

### Why this is stronger than separate Golomb caps

The Golomb property constrains repeated differences inside one signed
fiber.  Equations (3)--(7) instead compare an unshifted overlap of two
oppositely colored fibers with a shifted overlap of the same two fibers,
and force the two overlap sets to occur in a fixed order.  This information
is lost when each `F_d` is replaced only by the scalar bound
`|F_d|<=2q(n-d)`.

The `+1` in (5) cannot be removed under the stated hypotheses.  Use the
following explicit completion-closed corner-free region:

```text
A={1,4,8,14,18,21},
```

give the six source-diagonal cells a third color, and color the strict
triangle `T(A)` by putting sign `-` only at `(21,1)` and `(18,4)`, with
sign `+` at its other thirteen cells.  The complete positive-difference
list of `A` has repeated fibers

```text
d=3,4,7,10,13,17, each of size 2,
```

and singleton fibers `d=6,14,20`.  Hence the only corners wholly inside
the strict triangle are the six coming from those repeated differences.
The `d=3,7,13,17` corners all have completion `(21,1)`, while the `d=4,10`
corners have completion `(18,4)`.  In every case both same-diagonal
endpoint cells have sign `+` and the completion has sign `-`.  A corner
using a source-diagonal cell uses two such cells and one strict completion,
so it is also nonmonochromatic.  This proves corner-freeness directly;
completion closure is immediate for the weak triangle on `A`.

For `d=3`, `e=20`, `Delta=17`, this coloring gives

```text
F_3^+={1,18},  F_20^-={1},  C=D={1}.
```

Thus the left side of (5) is `2=|F_20^-|+1`.

## 2. Support transfer retained from the propagation rule

### Corollary (**PROVED**)

Let `Diff^+(S)={v-u:u<v in S}` and
`Supp^eps={h>0:F_h^eps is nonempty}`.  Then

```text
d + Diff^+(F_d^eps) is a subset of Supp^{-eps}.             (8)
```

Because `F_d^eps` is Golomb, all its pair differences are distinct, so

```text
binom(|F_d^+|,2) <= sum_{h>d} 1_{F_h^- nonempty},
binom(|F_d^-|,2) <= sum_{h>d} 1_{F_h^+ nonempty}.            (9)
```

Writing `r_d=|F_d|` and using the minimum of
`binom(b,2)+binom(r_d-b,2)` over integral `b` gives the color-free profile
constraint

```text
floor((r_d-1)^2/4)
  <= sum_{h>d} (1_{F_h^+ nonempty}+1_{F_h^- nonempty})
  <= sum_{h>d} min(2,r_h).                                  (10)
```

More generally, for arbitrary nonnegative weights `lambda_d`, if
`Lambda_h=sum_{d<h}lambda_d`, then

```text
sum_d lambda_d floor((r_d-1)^2/4)
  <= sum_h Lambda_h min(2,r_h).                             (11)
```

### Proof

In (1), every pair `u<v` in `F_d^eps` supplies a point in the signed
fiber `F_{d+v-u}^{-eps}`, proving (8).  Golomb distinctness makes the
`binom(|F_d^eps|,2)` resulting offsets distinct, proving (9).  Add the
two inequalities and minimize their left side over the two-color split to
obtain (10).  Multiplying (10) by `lambda_d`, summing, and reversing the
order of summation proves (11).

For a concrete scale indication, at `n=464`, if some `r_d=48`, then (10)
requires at least `552` later signed-fiber support slots.  Since there are
only `463-d` later offsets, at least

```text
552-(463-d)=89+d
```

of those offsets must contain both signs.  This is a structural consequence,
not a proof that `r_d<=47`.

## 3. Relation to the quadratic outer-cell operator

For an outer cell `q=(v+sigma,u)` with `u<v` in `A`, let

```text
D_q={d:0<d<v-u, u+d in A, v-d in A}.
```

Let `P_q` count those `d` for which both length-`d` end-cap cells have
sign `+`, and let `M_q` count those for which both have sign `-`.  If
`z(x,y)` denotes the sign of the triangle cell `(x+sigma,y)` and

```text
H_q=P_q+M_q,
S_q=(1/2) sum_{d in D_q}
    (z(u+d,u)+z(v,v-d)),
```

then `S_q=P_q-M_q`.  Corner-freeness says every `++` decomposition forces
`q` to sign `-`, while every `--` decomposition forces it to sign `+`.
Therefore

```text
P_q M_q=0,
H_q=|S_q|,
H_q^2-S_q^2=4P_qM_q=0.                                    (12)
```

Each same-sign pair in a signed fiber supplies exactly one outer cell and
one end-cap decomposition, so

```text
sum_q H_q
  = sum_d (binom(|F_d^+|,2)+binom(|F_d^-|,2)).              (13)
```

Also, `P_qM_q` counts ordered choices of a `+` cloud and a `-` cloud
which both contain `q`.  Consequently

```text
sum_q P_qM_q = sum_{d,e}|Q_d^+ intersect Q_e^-| = 0.        (14)
```

The order-separation lemma is the fixed-`d,e` coordinate form of the
nonnegative cross term `P_qM_q=0`.  Summing (12) gives the proposed exact
quadratic identity `||H||_2^2=||S||_2^2`; no cancellation is involved.

### Precise obstruction to a pointwise deficit (**PROVED by the existing witness**)

The same explicit six-mark coloring shows that (12) cannot be strengthened to a
universal pointwise inequality `H_q<=|D_q|-1` when `D_q` is nonempty.
For `q=(21,1)`,

```text
D_q={3,7,13,17}.
```

For every one of these four decompositions, both end-cap cells have
triangle color 1.  Hence

```text
P_q=4,  M_q=0,  H_q=|S_q|=|D_q|=4.
```

Thus even four different source fibers may align and force the same outer
cell with no local loss.  Any quantitative gain from the quadratic operator
must use the sharing of endpoint-color variables between different outer
cells, or a global restriction on the signed support profile.  A per-cell
multiplicity deficit is false.

## Conjectural next use

The natural analytic input is to sum (5)--(7) over `d<e` with nonnegative
weights and retain the order cut `max D<=min C`, rather than relaxing each
intersection to its cardinality.  It is presently **CONJECTURAL** that this
ordered family yields a strict improvement in the `n=464` three-color
profile optimization.  No such improvement has been proved here.
