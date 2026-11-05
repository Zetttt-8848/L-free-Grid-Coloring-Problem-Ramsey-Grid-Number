# Golomb sumset completion-triangle construction

Base: `R4-RESEARCH-0001`.

## PROPERTY (formal)

Let `B,G` be finite nonempty subsets of the integers.  A set is **Golomb**
when every positive difference between two of its elements has a unique
ordered representation.  Put

```text
S = span(B) = max(B)-min(B),
A = B+H G = {b+Hg : b in B, g in G},
```

where `H` is an integer satisfying `H>2S`.  The strict completion triangle is

```text
T(A) = {(y,x) : x,y in A and x<y}.
```

Every `a in A` has a unique representation `a=Hg+b`.  For `x=Hg+b` and
`y=Hg'+b'` with `x<y`, define

```text
c(y,x)=1  iff  g'>g and b'>b,
c(y,x)=0  otherwise.                                      (C)
```

The claim is that if both `B` and `G` are Golomb, then (C) is a total
two-coloring of `T(A)` with no monochromatic corner.

The only equivalence used is literal equality of integer sets and cells;
translations of all marks preserve the construction and corner property.

## CHANNEL USED

**C2, explicit product construction.**  The supplied rule is handled
symbolically.  Solver search and probabilistic arguments are inapplicable to
the universal claim and were not used.

## WITNESS + CERTIFICATE

The witness is the full symbolic family (C), and this document is its proof
certificate.  No isolated finite instance is asserted as a substitute for
the family theorem.

### Preliminary no-carry facts

If

```text
Hg+b = Hh+c,
```

then `H(g-h)=c-b`.  The right side has absolute value at most `S<H`, so
`g=h` and `b=c`.  Thus every element of `A` has a unique pair of digits.
It follows at once that

```text
|A|=|B||G|.                                                 (1)
```

The order is lexicographic in the `G` digit: if `g<h`, then

```text
Hh+c-(Hg+b) >= H-S > 0.
```

Consequently `Hg+b<Hh+c` implies either `g<h`, or `g=h` and `b<c`.
In particular, the rule (C) assigns exactly one color to every strict cell.

The stronger threshold `H>2S` is used when two differences are equal.  If

```text
H(g_1-g_0)+(b_1-b_0)
  = H(g_3-g_2)+(b_3-b_2),                                  (2)
```

then

```text
H((g_1-g_0)-(g_3-g_2))
  = (b_3-b_2)-(b_1-b_0).
```

The right side has absolute value at most `2S<H`.  Since its left side is
an integer multiple of `H`, both sides vanish.  Therefore

```text
g_1-g_0=g_3-g_2,    b_1-b_0=b_3-b_2.                       (3)
```

This excludes every nonzero carry between the two digits.

### Theorem (**PROVED**)

The coloring (C) is corner-free.  In fact every corner in `T(A)` has its
three colors, in corner order, equal to `(0,1,0)`.

#### Proof

Take an arbitrary corner in `T(A)`.  Its four source marks can be written

```text
a_0,  a_1=a_0+t,  a_2,  a_3=a_2+t,
```

where `t>0` and `a_0<a_2`.  The three cells of the corner are

```text
(a_2,a_0), (a_3,a_0), (a_3,a_1).                           (4)
```

Write `a_i=Hg_i+b_i` using the unique digits above.  The equality
`a_1-a_0=a_3-a_2` and (3) give

```text
p := g_1-g_0 = g_3-g_2 >= 0,
b_1-b_0=b_3-b_2.                                           (5)
```

The inequality `p>=0` follows from `a_0<a_1` and the lexicographic order.
There are exactly two cases.

**Case 1: `p>0`.**  The two ordered pairs `(g_0,g_1)` and `(g_2,g_3)`
give the same positive difference in the Golomb set `G`.  Hence

```text
g_0=g_2,    g_1=g_3.                                       (6)
```

Since `a_0<a_2` and their `G` digits agree, `b_0<b_2`.  Rearranging the
second equality in (5) gives

```text
b_2-b_0=b_3-b_1>0.
```

Golomb uniqueness in `B` now gives

```text
b_0=b_1,    b_2=b_3.                                       (7)
```

For the first cell in (4), the two `G` digits are equal by (6), so its
color is `0`.  For the middle cell, `g_3=g_1>g_0` and
`b_3=b_2>b_0`, so its color is `1`.  For the last cell the two `G`
digits are equal by (6), so its color is `0`.

**Case 2: `p=0`.**  Now `g_0=g_1` and `g_2=g_3`.  Since `t>0`, (5)
gives the same positive difference

```text
b_1-b_0=b_3-b_2>0
```

twice in the Golomb set `B`.  Thus

```text
b_0=b_2,    b_1=b_3.                                       (8)
```

The inequality `a_0<a_2`, together with `b_0=b_2`, forces `g_0<g_2`.
For the first cell in (4), its `B` digits are equal, so its color is `0`.
For the middle cell, `g_3=g_2>g_0` and `b_3=b_1>b_0`, so its color is
`1`.  For the last cell, its `B` digits are equal, so its color is `0`.

Both cases give `(0,1,0)`.  A negative value of `p` is impossible by
the order fact, and a nonzero carry is impossible by `H>2S`; hence the two
cases exhaust all corners.  This proves the theorem.

### Exact corner count (**PROVED**)

Fix `g<g'` in `G` and `b<b'` in `B`.  The four marks

```text
Hg+b,  Hg+b',  Hg'+b,  Hg'+b'
```

supply exactly two corners.  The `p>0` corner uses the two equal differences
`H(g'-g)`:

```text
(Hg+b, Hg'+b),  (Hg+b', Hg'+b').
```

The `p=0` corner uses the two equal differences `b'-b`:

```text
(Hg+b, Hg+b'),  (Hg'+b, Hg'+b').
```

Written as triangle cells, both corners have the same color-`1` completion

```text
(Hg'+b', Hg+b).
```

Conversely, Case 1 of the proof uniquely recovers `g<g'` and `b<b'`
from a `p>0` corner, and Case 2 uniquely recovers them from a `p=0`
corner.  Thus this list neither omits nor repeats a corner, and

```text
#corners in T(A) = 2 binom(|G|,2) binom(|B|,2).             (9)
```

The exact count is compatible with corner-freeness because each listed
corner has colors `(0,1,0)`.

### Boundary cases and exact scope

- Singleton `B` or singleton `G` is allowed.  The proof then shows that
  the incompatible case simply contains no corner; the coloring remains
  valid.
- Empty sets are excluded only because `span(B)` was defined using a
  maximum and minimum.  If either input is empty, `T(A)` is empty and the
  conclusion is vacuous.
- Elements of `B` and `G` may be negative.  Translating `A` into positive
  grid coordinates does not change any corner or color comparison.
- The proof uses the strict hypothesis `H>2 span(B)`.  It makes no claim at
  `H<=2 span(B)`, where a nonzero carry in (2) is no longer excluded.
- Coloring the source diagonal on `A` with a third color extends (C) to a
  corner-free coloring of the completion-closed weak triangle on `A`:
  every corner meeting the source diagonal has two source-colored diagonal
  endpoints and a differently colored strict completion.
- This is a coloring of the completion triangle, not an extension to a
  complete square and not a lower bound for the full grid Ramsey number.

### Arbitrarily many translates

For every `m>=1`, the set

```text
G_m={1,2,4,...,2^{m-1}}
```

is Golomb.  Indeed, in an equality
`2^j-2^i=2^l-2^k` with `i<j` and `k<l`, the two-adic valuation first
gives `i=k`, and cancellation then gives `j=l`.  Therefore, for any fixed
nonempty Golomb set `B` and fixed integer `H>2 span(B)`, the sets

```text
A_m=B+H G_m
```

have `|A_m|=m|B|` and their strict completion triangles all admit the
coloring (C).  The `m` blocks `B+Hg`, `g in G_m`, are pairwise disjoint by
the unique-representation argument.  In particular, fixing any three-mark
Golomb set `B` produces arbitrarily many disjoint translates of that same
three-mark pattern inside sets whose strict completion triangles remain
properly two-colored.

Thus the number of sufficiently separated translates of one fixed Golomb
set cannot, by itself, force a non-two-colorable completion triangle.  A
blanket exclusion of the fixed three-mark pattern together with any constant
number of its translates therefore cannot be inferred from this source
condition.  A source-size argument along that line needs additional input,
such as a non-Golomb relation among the block indices, a density/span
constraint, or compatibility with cells outside the weak triangle.

## VERIFICATION METHOD

The verification is symbolic and consists of the exhaustive dichotomy
`p=0` or `p>0` after the no-carry identity (3).  Each branch invokes Golomb
uniqueness once in each digit in the order shown and evaluates all three
cells directly from (C).  There is no omitted sign, carry, or within-block
case.  No solver, finite enumeration, or external theorem is used.

## BEST-KNOWN GAP TABLE

This task does not define an extremal optimum, so an upper/lower numerical
gap is not applicable.  The project-local status on 2026-09-12 is:

| Side | Result | Scope | Evidence |
|---|---|---|---|
| Construction | `|A|=|B||G|`, with a two-colored `T(A)` | All finite nonempty integer Golomb `B,G` and integer `H>2 span(B)` | Symbolic proof above |
| Impossibility | None requested or proved | `H<=2 span(B)` and full-square extension remain open here | Not applicable |

## VERDICT

**PROVED:** under the exact hypotheses above, the proposed coloring of
`T(B+HG)` is corner-free, and every corner has color pattern `(0,1,0)`.
No upper bound, optimality statement, or full-grid coloring is claimed.
