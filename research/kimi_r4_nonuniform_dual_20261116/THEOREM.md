# Exact nonuniform scale optima and the remaining six-square barrier

**No new Ramsey bound.** This package proves three finite linear-programming
values and their implications for a consumer. It does not determine the actual
minimum rainbow count `rho_6`, and it does not exclude any arbitrary coloring
of a full square.

## 1. Finite weighted-copy program

Use the coordinates and definitions in `CONTRACT.md`. Fix `N` and `m`, put
`S=floor((N-1)/(m-1))`, and for `1<=s<=S` define

```text
q=N-1-(m-1)s,  t=min(s-1,q),
A_s=C(q+2,2)+t(q+1)-C(t+1,2).
```

For `1<=j<=m-2`, put `c_j=C(m-j,2)`. The primal program is

```text
V(N,m)=max sum_(s=1)^S A_s*a_s
subject to a_s>=0,
           sum_(j|h,1<=j<=m-2,h/j<=S) c_j*a_(h/j)<=1
           for every 1<=h<=N-2.
```

Its dual has one nonnegative variable `y_h` for every host step and requires

```text
sum_(j=1)^(m-2, j*s<=N-2) c_j*y_(j*s)>=A_s
for every 1<=s<=S.
```

**Weak duality.** For feasible `a` and `y`,

```text
sum_s A_s*a_s
<= sum_(s,j) a_s*c_j*y_(j*s)
=  sum_h y_h*Lambda_h(a)
<= sum_h y_h.
```

Thus equal feasible primal and dual values prove the exact optimum. The stored
vectors in `dual_results.json` are exact rational numbers. The independent
standard-library checker reconstructs every coefficient and verifies every
inequality; no floating-point solver output is used in this proof.

## 2. Exact values at the preregistered hosts

At `m=6`, `C_6=20` and `(c_1,c_2,c_3,c_4)=(10,6,3,1)`. Equal feasible primal
and dual values give

| `N` | `S` | Exact `V(N,6)` | `U_N` | Exact `20*V-U_N` |
|---:|---:|---:|---:|---:|
| 30 | 5 | `7458/125` | 1477 | `-7093/25` |
| 60 | 11 | `671151/1250` | 10490 | `31052/125` |
| 120 | 23 | `2810248/625` | 78130 | `1474742/125` |

All three primal vectors satisfy every one of the `N-2` incidence constraints,
and all three dual vectors satisfy every one of the `S` scale-covering
constraints. Their objective values agree exactly, so these are optima rather
than lower-bound scans or approximate upper estimates.

For comparison, the uniform normalized weights `a_s=1/20` have best-case
margins `-672`, `-3105`, and `-15060`, respectively. Nonuniform weights improve
the two larger finite programs from negative to positive best-case margins.

## 3. Consumer consequence

Let `rho_m` be the minimum number of rainbow Ls in the strict lower triangle of
a proper four-colored complete `m`-square. Round 4 proved that, whenever
`Lambda_h(a)<=1` for every host step,

```text
rho_m*J(a)<=calR_N<=U_N.
```

Since a local strict triangle has only `C_m` Ls, `rho_m<=C_m`. Therefore:

- At `(N,m)=(30,6)`, `20*V<U_30`. No local proper six-square kernel and no
  nonnegative scale weighting can produce a positive margin through this
  uniform-incidence consumer at `N=30`.
- At `(60,6)` and `(120,6)`, the best-case numerical ceiling does not obstruct
  the consumer. This is not an existence theorem for a useful kernel.

Using the exact optimal copy mass, a contradiction at the tested host would
require the actual local minimum to satisfy respectively

| `N` | Necessary strict requirement |
|---:|---|
| 30 | `rho_6>184625/7458`, approximately `24.7553`, impossible because `rho_6<=20` |
| 60 | `rho_6>13112500/671151`, approximately `19.5373` |
| 120 | `rho_6>24415625/1405124`, approximately `17.3761` |

These thresholds apply to the optimal weighted consumer at the stated finite
host. They do not assert anything about other `N`, position-dependent
incidences, other host regions, or non-rainbow statistics.

## 4. Status and non-claims

| Statement | Status |
|---|---|
| Three finite LP values | PROVED by exact feasible primal-dual certificates |
| Six-square uniform-incidence consumer at `N=30` | Closed even under `rho_6=20` |
| Best-case numerical possibility at `N=60,120` | PROVED as a finite optimization statement |
| Actual `rho_6` | UNDECIDED in this package; not searched |
| Actual consumer at `N=60,120` | UNDECIDED; a positive best-case margin is insufficient |
| All-`N` or asymptotic nonuniform consumer | UNDECIDED; no extrapolation from three hosts |
| New bound on `R_3` or `R_4` | None |

The evidence is internal to this repository. It is not external peer review or
Lean formalization.
