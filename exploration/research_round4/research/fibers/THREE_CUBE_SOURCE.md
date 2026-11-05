# Three-dimensional Boolean source cube

Base: `R4-RESEARCH-0007`.

## PROPERTY (formal)

Let `w_1=a`, `w_2=b`, `w_3=c` be positive integers satisfying the
two-dissociation condition

```text
k_1 a+k_2 b+k_3 c=0,  k_i in {-2,-1,0,1,2}
    implies k_1=k_2=k_3=0.                                 (D)
```

A convenient sufficient separated-step hypothesis is

```text
b>2a,   c>2(a+b).                                          (S)
```

Indeed, under (S) a nonzero `k_3` cannot be cancelled by the two lower
terms, and after `k_3=0` a nonzero `k_2` cannot be cancelled by the first.
The example `(a,b,c)=(1,4,16)` satisfies (S).

For `x=(x_1,x_2,x_3)` in `{0,1}^3`, put

```text
V(x)=a x_1+b x_2+c x_3,
A={V(x):x in {0,1}^3}={0,a,b,a+b,c,a+c,b+c,a+b+c}.
```

Condition (D) makes `V` injective.  Thus every source mark has a unique bit
vector.  The strict completion triangle is

```text
T(A)={(V(y),V(x)):V(x)<V(y)}.
```

The question is whether the additive relations forced by the Boolean cube
make every two-coloring of `T(A)` contain a monochromatic corner.

## CHANNEL USED

A tiny Boolean search was used only to discover an affine rule.  The result
below is proved symbolically for the whole parameter range (D); the search
result is not a proof premise.  No higher-dimensional search or construction
was pursued.

## WITNESS + CERTIFICATE

For bit vectors `x,y` with `V(x)<V(y)`, color the cell `(V(y),V(x))` by

```text
chi(y,x)=x_1 xor x_3 xor y_1 xor y_2.                       (C)
```

Formula (C) is a full symbolic specification of all 28 strict cells.

### Theorem (**PROVED**)

Under (D), the coloring (C) has no monochromatic corner in `T(A)`.

### Proof

Take any corner in `T(A)`.  There are four source marks

```text
V(x), V(x'), V(y), V(y')
```

such that

```text
V(x')-V(x)=V(y')-V(y)=t>0,   V(x)<V(y).                    (1)
```

The three corner cells, in order, are

```text
(V(y),V(x)), (V(y'),V(x)), (V(y'),V(x')).                  (2)
```

Put `delta=x'-x` coordinatewise.  Equality (1) says

```text
sum_i ((x'_i-x_i)-(y'_i-y_i)) w_i=0.
```

Every coefficient lies in `{-2,-1,0,1,2}`, so (D) gives

```text
x'-x=y'-y=delta.                                           (3)
```

For each coordinate let

```text
s_i=1 if delta_i is nonzero, and s_i=0 otherwise.
```

Since the endpoints are Boolean, (3) implies, in arithmetic modulo two,

```text
x'_i=x_i xor s_i,   y'_i=y_i xor s_i.                      (4)
```

Let the colors of the three cells in (2) be `C_0,C_1,C_2`.  Applying (C)
and cancelling repeated bits gives

```text
C_0 xor C_1 = s_1 xor s_2,
C_1 xor C_2 = s_1 xor s_3.                                (5)
```

If the corner were monochromatic, both expressions in (5) would vanish.
Hence

```text
s_1=s_2=s_3.                                               (6)
```

The vector `s` cannot be `(0,0,0)`, because then `delta=0` and (1) would
give `t=0`.  It also cannot be `(1,1,1)`.  If `delta_i=1`, Booleanity
forces `x_i=y_i=0`; if `delta_i=-1`, it forces `x_i=y_i=1`.  Thus when
all three coordinates of `delta` are nonzero, `x=y`, contradicting the
strict inequality `V(x)<V(y)` in (1).

Both possibilities allowed by (6) are impossible.  Therefore at least one
of the two adjacent color changes in (5) is nonzero, and the corner is not
monochromatic.  Since the corner in (1) was arbitrary, (C) is corner-free.

## COMPLETE CASE COVERAGE

The proof accounts for every possible equality of source differences:

- Condition (D) eliminates all carry cases and forces the same signed
  coordinate difference `delta` on the two translated pairs.
- Each coordinate of `delta` is `-1`, `0`, or `1`.  Its support vector `s`
  is nonzero because the corner step is positive.
- A corner needs two distinct starts `x` and `y`; therefore the support of
  `delta` cannot contain all three coordinates.
- Equations (5) separate every nonzero proper support of `delta`.  No
  assumption on the signs of its nonzero coordinates remains.

The argument is therefore a pencil-and-paper verification of the complete
symbolic coloring, rather than an enumeration of the concrete cube.

## CONSEQUENCE AND EXACT SCOPE

The generic separated three-dimensional Boolean cube does **not** force a
monochromatic corner in its strict completion triangle.  Its unavoidable
additive parallelograms are compatible with the explicit two-coloring (C).
Equivalently, coloring the eight source-diagonal cells with a third color
gives a corner-free coloring of the completion-closed weak triangle on `A`.

This conclusion holds under the exact two-dissociation hypothesis (D), and
hence under the simple sufficient inequalities (S).  It makes no assertion
for weaker separation where two source differences may agree through a
nonzero carry.  It also gives no coloring of a full square, no Ramsey bound,
and no higher-dimensional product construction.

## VERIFICATION METHOD

The symbolic check is (3)--(6): equality of numerical differences becomes
coordinatewise equality by (D), and monochromaticity would force the change
support to be either empty or all three coordinates.  The corner conditions
exclude both.  No solver output, finite count, or external result is used as
evidence.

## BEST-KNOWN GAP TABLE

No extremal optimization parameter is defined in this bounded question.

| Side | Result | Scope | Evidence |
|---|---|---|---|
| Construction | Proper two-coloring (C) of `T(A)` | Every positive `(a,b,c)` satisfying (D), including every triple satisfying (S) | Symbolic proof above |
| Exclusion | False in this scope | The cube relations alone do not force a monochromatic corner | Construction (C) |

## VERDICT

**PROVED CONSTRUCTION:** the strict triangle on the separated Boolean
three-cube is two-colorable by (C).  The proposed exclusion route therefore
fails at dimension three under the stated source condition.
