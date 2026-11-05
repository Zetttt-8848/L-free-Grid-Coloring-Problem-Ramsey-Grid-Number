# Exact line-factor inequalities for the pair-potential candidate

Multiply all fifth-denominator coefficients in
`PAIR_POTENTIAL_CANDIDATE_0014.json` by `5`.  For a line factor with
ordered signs `x_0,...,x_{n-1}`, let

```text
P(x)=sum_{i<j} c_ij x_i x_j,       x_i in {+1,-1}.
```

This note proves the four scaled local bounds

```text
R:8   P>=-14,
C:0   P>=-15,
C:1   P>= -7,
C:2   P>= -6.                                      (1)
```

These are precisely five times the listed normalization targets.  The
proofs below use only algebra on signs.

For a set `S` of `k` sign variables, abbreviate the complete-clique sum by

```text
K(S)=sum_{i<j, i,j in S} x_i x_j.
```

Since

```text
K(S)=((sum_{i in S}x_i)^2-k)/2,
```

one always has

```text
K(S)>=-floor(k/2).                                  (2)
```

## 1. The row `R:8`

Use the vertex order

```text
0=(8,0), 1=(8,1), 2=(8,2), 3=(8,3),
4=(8,4), 5=(8,6), 6=(8,7).
```

The scaled polynomial has nonzero coefficients

```text
c01=2  c02=5  c04=3  c05=4  c06=4
c12=3  c13=2  c15=3  c16=4
c23=2  c24=3  c25=3  c26=4
c34=2  c36=2  c45=2  c56=2.
```

It has the exact positive clique decomposition

```text
P_R8 = 2 K(0,1,2,5,6)
       +K(1,2,5)
       +2K(0,4,5)
       +K(0,2,4)
       +2K(2,3,4)
       +2K(1,3,6)
       +2K(0,2,6).                                  (3)
```

Indeed, the `K_5` supplies coefficient `2` on its ten pairs.  The six
triangle types then add respectively

```text
125:1, 045:2, 024:1, 234:2, 136:2, 026:2,
```

which gives exactly the displayed coefficient list.  By (2), the first
term in (3) is at least `-4`; the triangle weights total
`1+2+1+2+2+2=10` and contribute at least `-10`.  Therefore

```text
P_R8>=-4-10=-14.                                    (4)
```

## 2. The column `C:1`

Use the vertex order

```text
0=(2,1), 1=(3,1), 2=(4,1),
3=(6,1), 4=(7,1), 5=(8,1).
```

Here

```text
c01=1  c02=2  c04=4  c05=3
c13=2  c15=3  c24=2  c35=2  c45=2.
```

The polynomial decomposes as

```text
P_C1 = K(0,1,5)
       +2K(0,2,4)
       +2K(1,3,5)
       +2K(0,4,5).                                  (5)
```

All four summands are triangle sums.  Their total weight is `7`, so (2)
gives

```text
P_C1>=-7.                                            (6)
```

## 3. The column `C:2`

Use the vertex order

```text
0=(3,2), 1=(4,2), 2=(6,2), 3=(7,2), 4=(8,2).
```

The coefficients are

```text
c01=1  c03=3  c04=4  c12=2
c14=3  c24=2  c34=3.
```

They have the exact decomposition

```text
P_C2 = K(0,1,4)+3K(0,3,4)+2K(1,2,4).                (7)
```

The triangle weights total `6`; hence

```text
P_C2>=-6.                                            (8)
```

## 4. The column `C:0`

Use the vertex order

```text
0=(1,0), 1=(2,0), 2=(3,0), 3=(4,0),
4=(6,0), 5=(7,0), 6=(8,0).
```

The nonzero coefficients are

```text
c01=1  c02=2  c03=3  c05=2  c06=4
c12=2  c13=2  c14=3  c16=4
c23=2  c25=2
c34=2  c35=2  c36=3
c45=4  c46=5  c56=2.                                (9)
```

Because `P_C0` contains only pair products, global sign reversal permits
the normalization `x_3=1`.  First minimize algebraically over `x_2` and
`x_4`.  Their complete contributions are

```text
x_2 [2+2x_0+2x_1+2x_5],
x_4 [2+3x_1+4x_5+5x_6],
```

so their minima are the negatives of the corresponding absolute values.
Put

```text
a=x_1,       b=x_5,       c=x_6.
```

The remaining minimum over `x=x_0` is

```text
B(a,b,c)+min_{x=+/-1}
  { x L(a,b,c)-2|1+x+a+b| },                         (10)
```

where

```text
B=2a+2b+3c+4ac+2bc-|2+3a+4b+5c|,
L=3+a+2b+4c.                                         (11)
```

There are only eight triples `(a,b,c)`.  Substitution in the integer
expression (10) gives

```text
 a   b   c       minimum in (10)
----------------------------------
 +   +   +              -15
 +   +   -              -15
 +   -   +               -7
 +   -   -              -15
 -   +   +              -15
 -   +   -               -7
 -   -   +              -15
 -   -   -              -15.                         (12)
```

For completeness, the two values minimized in each row require no hidden
casework.  If `a=b=+1`, they are `L-8` and `-L-4`; if `a` and `b` differ,
they are `L-4` and `-L`; and if `a=b=-1`, they are `L` and `-L-4`.
Together with (11), these formulas give every entry of (12) directly.
Thus the minimum of `P_C0` is at least `-15`.

Combining (4), (6), (8), and (12) proves all four local line-factor
inequalities in (1).  These are local algebraic bounds only; their use in
the cancelling global pair-potential certificate is separate.
