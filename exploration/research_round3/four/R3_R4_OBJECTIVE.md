# R3-R4 pinned objective and constraints

Base: `R3-CP0`.  Inherited without rederivation: the accepted theorem
`R_4(L)<=22006246`, FM1/FM2-4/FM3, its polynomial weight profile, and its
independent certificate check.

## OBJECTIVE

For fixed `t=36000` and integer weights

```text
w_i = i*(36001-i),  1<=i<=36000,
a_d = sum_{i=1}^{t-d} w_i*w_{i+d},
```

minimize the integer `n` among tested candidates for which

```text
M(n) = 2*sum_{d=1}^{t-1} (n-d-48*K_d(n))*a_d - 3*n*a_0 > 0.
```

Here `L_d=n-d-1`.  For each internal positive difference `h`, define

```text
Q(S) = min_c Cap(S,1,c),
V_{d,h} = 2*Q(L_d-h),
```

where `Cap` is the inherited exact first-forbidden-size consequence of
FM3.  The refined capacity `K_d(n)` is any exact bound obtained from the
profile neighbor inequality

```text
2*ProfileMin(c*(K+1)-c*(c+1)/2; V_{d,1},V_{d,2},...) 
    > L_d*c*(c+1).
```

Larger `M` is favorable.  The target is `M>0`.  The signed incumbent gap is
`22006246-n`, positive when the certified candidate improves the inherited
bound.

## CONSTRAINTS

The mathematical constraints are: integer `n>=t`; positive integer weights;
`1<=d<t`; `1<=h<=L_d`; integer neighbor parameter `1<=c<K+1`; nonnegative
autocorrelations (automatic here); `Q(S)` must be a proved Golomb-order cap
at span `S`; every profile multiplicity must be justified by FM1 at the
actual residual span `L_d-h`; and every final coefficient uses the exact
same `K_d` whose first-forbidden inequality is certified.  The four-color
implication is inherited FM2-4.

The initial numerical search box is `21950000<=n<=22006246`, with the
weight family and `t` fixed.  Any bounded scan establishes only the exact
scores it evaluates, not a global optimum over `n`, weights, windows, or
neighbor parameters.

## COEFFICIENT SOURCES

| Quantity | Source |
|---|---|
| `48` and `3*n*a_0` | Accepted Round-2 FM2-4 |
| `Cap`, first-forbidden inequality | Accepted Round-2 FM3 / Lemma 6.1 |
| `V_{d,h}=2Q(L_d-h)` | FM1 applied at the actual residual span; derivation to be supplied in this route |
| incumbent `22006246`, `t`, `w_i` | Accepted Round-2 exact certificate |
| span `L_d=n-d-1` | Accepted Round-2 index convention |

