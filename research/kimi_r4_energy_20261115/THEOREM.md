# Four-color line energy and the closure of a uniform square-copy consumer

**No new Ramsey bound is established.** In particular, neither `R_3` nor `R_4`
changes. The pure second-order energy test has no contradiction, and the
preregistered uniform full-square embedding consumer has no viable asymptotic
margin after its boundary count is corrected.

## 1. Complete strict-triangle geometry

Use zero-based cells `(x,y)` and directed Ls
`L(x,y;d)={(x,y),(x+d,y),(x+d,y+d)}`. Let

```text
T_N={(x,y):0<=y<x<N},  M=C(N,2),  C=C(N,3),
S=N(N-1)(2N-1)/2.
```

Every L contained in `T_N` can be written uniquely as
`(u+d,u),(v+d,u),(v+d,v)` with `u<v`, `d>0`, and `v+d<N`. Hence there are `C`
such Ls.

Take the horizontal, vertical, and slope-one lines in `T_N`. Each direction has
one line of each length `1,...,N-1`, so

```text
sum_lambda |lambda|=3M,  sum_lambda |lambda|^2=S.
```

Every unordered pair on one of these lines has its unique directed-L completion
inside `T_N`. Conversely, every L in `T_N` has exactly one pair in each of the
three directions. The programs check this bijection literally at `N=2,3,4`.

For a `k`-coloring, let `n_(lambda,i)` be the color counts on a line and put

```text
D_k=sum_(lambda,i) (n_(lambda,i)-|lambda|/k)^2.
```

Let `P_k` count equal-color line pairs, `B_k` monochromatic Ls, and `R_k` Ls
using exactly three colors.

## 2. General line identity

**Proposition N1 (PROVED).** For every `k`-coloring of `T_N`, including improper
ones,

```text
P_k=C-R_k+2B_k,
D_k+2R_k-4B_k=2C-S/k+3M.                                      (1)
```

**Proof.** A monochromatic L contains three equal-color pairs, a two-color L
contains one, and a rainbow L contains none. This proves the first formula.
Expanding the squared line discrepancy gives

```text
P_k=D_k/2+S/(2k)-3M/2.
```

Substitution proves (1). QED.

For a proper coloring, `B_k=0`, so `P_k+R_k=C` and `D_k+2R_k=2C-S/k+3M`.
At `k=3`,

```text
2C-S/3+3M=N(N-1),
```

which is exactly manuscript Lemma `lem:variance`. Thus the generalization is a
technical extension of an existing identity, not a new numerical mechanism by
itself. All `4+64+4096=4164` four-color words on `T_2,T_3,T_4`, including
improper words, satisfy both formulas under two independently indexed
implementations.

## 3. Four-color balanced-line estimate

At `k=4`, the right side of the proper identity is

```text
H_N=2C-S/4+3M=N(N-1)(2N+23)/24.
```

For a line of length `l=4q+r`, `0<=r<4`, the sum of squared deviations is
minimized by color counts differing by at most one. Its minimum is

```text
delta_4(l)=r(4-r)/4 in {0,3/4,1,3/4}.
```

Consequently

```text
D_4>=E_N:=3*sum_(l=1)^(N-1) delta_4(l),
R_4(T_N)<=U_N:=(H_N-E_N)/2,
P_4>=C-U_N.                                                   (2)
```

This is PROVED for every proper four-coloring of `T_N`. Here `R_4(T_N)` is a
rainbow count, not the Ramsey number `R_4`; the notation is distinguished from
this point onward by using `calR_N` for the count.

The estimate cannot force impossibility. At `N=1`, all terms vanish; at `N=2`,
`H_N=E_N=9/4`. For `N>=3`, `delta_4(l)<=1` gives `E_N<=3(N-1)`, while

```text
H_N/(N-1)=N(2N+23)/24>=3.
```

Thus `U_N>=0` for every `N`. More precisely,

```text
C-U_N=N^3/8+O(N^2),  U_N=N^3/24+O(N^2),
(C-U_N)/C -> 3/4,    U_N/C -> 1/4.
```

The equal-pair lower bound therefore has leading coefficient `3/4`, below the
total-L coefficient. No negative rainbow ceiling or pure-energy Ramsey
contradiction exists. For example, `(U_3,U_4,U_5)=(1,4,10)` and
`(U_6,U_7,U_8)=(17,26,38)`. These are upper estimates on rainbow counts, not
lower bounds and not finite nonexistence claims.

**Route N disposition:** closed as a standalone second-order upper-bound
mechanism. No large energy scan or higher-order scan was run.

## 4. Full-square zero-rainbow witnesses

For a proper four-coloring `chi` of the complete `m by m` square, let `r_m(chi)`
count rainbow Ls in its strict lower triangle and let `rho_m=min_chi r_m(chi)`.

**Proposition F1 (COUNTEREXAMPLES to positive local minima).**

```text
rho_3=rho_4=rho_5=0.
```

**Proof.** The files `kernel_3.json`, `kernel_4.json`, and `kernel_5.json` are
complete proper four-colorings. Their strict lower triangles contain
respectively `1,4,10` Ls and no rainbow one. In fact, the project checker finds
zero rainbow Ls among all `5,14,30` Ls in these full squares. A nonnegative
minimum with a zero witness is exactly zero. QED.

The order-5 witness, with row `x` listing `y=0,...,4`, is

```text
0 0 0 0 0
0 1 0 1 0
0 1 2 0 0
0 1 2 3 0
0 1 3 2 2
```

The other two complete matrices are stored in the named JSON files. The
witnesses use at most four colors and do not imply a new lower bound: the
existing proper 20-square is already much stronger. No claim is made about
`rho_m` for `m>=6`.

The zero-witness search used first-appearance color renaming in row-major cell
order. This symmetry is safe because every coloring has exactly one
representative obtained by assigning names `0,1,...` at the first occurrence of
each new color. Since zero witnesses were found, no completeness assertion
about an exhaustive positive-minimum catalog is needed or made. The separate
known-answer checks reproduce a proper two-color 4-square and exhaustive
two-color nonexistence at side 5.

## 5. Corrected full-square embedding count

The contracted expression `(N-s(m-1))^2` counts all square origins, but some
copies have their local strict lower triangle outside the host `T_N`. That
expression must not be charged to the host rainbow count. See
`CONSUMER_ERRATUM.md`.

A scale-`s` square copy has cells `(a+s*i,b+s*j)`, `0<=i,j<m`. Its complete
local strict lower triangle lies in host `T_N` exactly when

```text
a-b+s>=1.                                                     (3)
```

Indeed the smallest difference `x-y` among local strict-triangle cells occurs at
`i=j+1`. Put

```text
q=N-1-(m-1)s,  t=min(s-1,q).
```

For `q>=0`, the exact number of valid origins is

```text
A(N,m,s)=C(q+2,2)+t(q+1)-C(t+1,2),                            (4)
```

and zero for `q<0`. This follows by counting origin differences `a-b`, and is
also checked by literal enumeration of every origin and every local triangle
cell in five small host scenarios.

With nonnegative finitely supported weights `a_s`, define the corrected copy
weight `J=sum_s a_s A(N,m,s)`. For a host L of step `h`, an upper incidence
bound is

```text
Lambda_h=sum_(j|h,1<=j<=m-2) a_(h/j)*C(m-j,2).                 (5)
```

There are `C(m-j,2)` local Ls of step `j`; after the host L and scale are fixed,
each local position determines at most one valid origin. Boundary conditions can
only remove incidences. Therefore, if every valid full `m`-square copy has at
least `rho_m` rainbow Ls, then

```text
rho_m*J <= sum_(host rainbow L) Lambda_h <= K*calR_N,
```

whenever `Lambda_h<=K` for every `h`. This is a proved conditional embedding
statement; it does not supply a positive `rho_m`.

## 6. Uniform-scale consumer threshold

Take `a_s=1` on all scales with `q>=0`. By (5),

```text
K<=sum_(j=1)^(m-2) C(m-j,2)=C(m,3)=C_m.
```

For the region `q>=s-1`, formula (4) is
`(q^2+2sq-s^2+q+3s)/2`; for `q<=s-1`, it is `(q+1)^2`. The two ranges meet at
`s=N/m` up to lower-order boundary terms. Exact finite summation gives

```text
J/N^3 -> (m+1)/(6m(m-1)).
```

The independent verifier reconstructs this coefficient by exact finite sums and
third finite differences on the divisibility subsequence `m(m-1)|N`, for each
`m=3,...,8`; ordinary floor effects affect only lower-order terms. Meanwhile
`U_N/N^3 -> 1/24`.

A uniform-`K` contradiction `rho_m J>C_m U_N` therefore requires the asymptotic
local fraction

```text
rho_m/C_m > m(m-1)/(4(m+1)).
```

The first thresholds are

| m | `C_m` | limit `J/N^3` | strict required `rho_m` | actual finite evidence |
|---:|---:|---:|---:|---|
| 3 | 1 | 1/9 | `rho_3>3/8` | `rho_3=0` |
| 4 | 4 | 5/72 | `rho_4>12/5` | `rho_4=0` |
| 5 | 10 | 1/20 | `rho_5>25/3` | `rho_5=0` |
| 6 | 20 | 7/180 | `rho_6>150/7>C_6` | no search needed |

For every `m>=6`, `m(m-1)/(4(m+1))>1`, so even the impossible extreme
`rho_m=C_m` could not produce a positive leading margin. For `m=3,4,5`, the
stored witnesses make the lower score zero. Thus the uniform-weight,
uniform-incidence asymptotic consumer is closed for every `m`.

This closure does **not** refute nonuniform weights, position-dependent
incidence estimates, other host regions, or every isolated finite `N`. It does
show that merely enumerating larger `m` cannot improve the large-`N` uniform
consumer. No such larger enumeration was run.

## 7. Status and non-claims

| Statement | Status |
|---|---|
| General identity (1) | PROVED; 4,164 finite words independently checked |
| Four-color estimate (2) | PROVED; no Ramsey contradiction |
| `rho_3=rho_4=rho_5=0` | PROVED by complete literal witnesses |
| Corrected valid-origin formula (4) | PROVED; direct geometry checks passed |
| Uniform-scale threshold | PROVED asymptotic consumer audit |
| Nonuniform or position-dependent consumers | UNDECIDED, not tested |
| New numerical bound on `R_3` | None |
| New numerical bound on `R_4` | None |

All verification is internal to this package. It is not external peer review or
Lean formalization, and no collaborator's numerical bound is adopted as an
input.
