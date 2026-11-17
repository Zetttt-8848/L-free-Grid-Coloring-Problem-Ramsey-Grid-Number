# Contract: nonuniform scale dual for four-color square copies

Date: 2026-11-16. Author: Kimi.
Branch: `kimi/r4-hybrid-dual-20261116`.
Base branch: `kimi/r4-energy-20261115`.
Base commit: `e1a62f30ce74d03681c04b58d0486e551e775124`.

## No-new-bound presumption

This is a consumer audit, not a claimed Ramsey bound. Neither `R_3` nor `R_4`
changes unless a complete arbitrary-full-square argument is subsequently
closed. No binary-source capacity, rank-transfer, request, ternary-MS*, prefix,
or local-triangle search is part of this package.

## Candidate card

Limitation: Round 4 closed only uniform scale weights with a uniform incidence
cap. It did not determine whether nonuniform weights could increase the charged
copy mass enough to matter, even under the strongest possible local rainbow
bound.

Mechanism: Replace a scanned weight family by the complete finite cone of
nonnegative scale weights. Use linear-programming duality to certify an upper
bound on every such weighting, not merely on weights tested by a scan.

Statement: For the preregistered pairs `(N,m)=(30,6),(60,6),(120,6)`, determine
whether the exact weighted-copy program below has `C(m,3)*V(N,m) <= U_N`. This
is the strongest obstruction obtainable without knowing a positive local
rainbow minimum, because every order-`m` strict triangle has only `C(m,3)` Ls.

Cheapest test: Solve these three small finite programs. Floating-point LP is
permitted for discovery only. Every reported inequality must be certified by an
exact nonnegative primal or dual vector reconstructed and checked using integer
and rational arithmetic. A failed solver run is UNDECIDED, not a negative
result.

Consequence: If the certified inequality holds at a tested pair, no proper
order-`m` full-square kernel, even one whose every local L is rainbow, can give
a contradiction through this weighted uniform-incidence consumer at that `N`.
This is a finite consumer obstruction, not an asymptotic theorem. If the
opposite strict inequality is certified, it shows only that the best-case
consumer is not ruled out at that `N`; it does not prove a Ramsey bound and
does not by itself authorize a larger coloring enumeration.

## Object and coordinates

Use zero-based cells `(x,y)` and directed Ls
`(x,y),(x+d,y),(x+d,y+d)`, `d>0`. The host is the complete strict triangle
`T_N={(x,y):0<=y<x<N}`. A scale-`s` full `m`-square copy has cells
`(a+s*i,b+s*j)`, `0<=i,j<m`, and is valid exactly when `a-b+s>=1` and
`0<=a,b<=q`, where `q=N-1-(m-1)s>=0`.

For `s=1,...,floor((N-1)/(m-1))`, define

```text
q=N-1-(m-1)s,  t=min(s-1,q),
A_s=C(q+2,2)+t(q+1)-C(t+1,2),
c_j=C(m-j,2),  1<=j<=m-2,
C_m=C(m,3).
```

For a nonnegative scale vector `a`, define

```text
J(a)=sum_s A_s*a_s,
Lambda_h(a)=sum_(j|h,1<=j<=m-2) c_j*a_(h/j),
```

where only integer scales in the stated range occur and `1<=h<=N-2`. Round 4
proved `rho_m*J(a) <= sum_(rainbow host L) Lambda_h(a)`. If `Lambda_h(a)<=K`
for every `h`, then `rho_m*J(a)<=K*calR_N<=K*U_N`, where

```text
H_N=N(N-1)(2N+23)/24,
E_N=3*sum_(l=1)^(N-1) delta_4(l),
delta_4(l)=r(4-r)/4 for l=4q+r, 0<=r<4,
U_N=(H_N-E_N)/2.
```

Normalize `K=1` and define the finite fractional packing value

```text
V(N,m)=max {J(a):a_s>=0, Lambda_h(a)<=1 for every 1<=h<=N-2}.
```

Its dual is

```text
min {sum_h y_h:y_h>=0,
     sum_(j=1)^(m-2) c_j*y_(j*s)>=A_s for every scale s}.
```

Every exact feasible dual value is an upper bound on `V`; every exact feasible
primal value is a lower bound. Since `rho_m<=C_m`, the certified inequality
`C_m*V<=U_N` closes this consumer at `(N,m)` for every proper local kernel.

## Exact proposition and quantifiers

At each preregistered pair, quantify over every nonnegative scale vector, every
valid copy, every host step, and every proper four-coloring of every complete
order-`m` square used as a local kernel. The test does not assume that a kernel
with many rainbow Ls exists. It uses only the universal numerical ceiling
`rho_m<=C_m`.

## Information retained that the incumbent loses

The optimization retains each scale and each divisor coupling in `Lambda_h`.
The uniform argument replaces this vector by one scale-independent cap and one
aggregate copy count. The dual certificate controls all nonnegative scale
vectors simultaneously.

## Cheapest discriminating test and stop condition

Run only `(30,6),(60,6),(120,6)` in this round. Stop after these exact
certificates. If all three satisfy the nonpositive best-case margin, do not run
larger `N` or `m` automatically; the surviving task is an all-`N` dual
construction. If any has a positive best-case margin, record the exact gap and
stop; the missing input is an actual local rainbow lower bound, not another
weight scan. No timeout may be relabelled as impossibility.

## Consumer chain if successful

A positive actual local minimum would enter
`rho_m*J<=K*calR_N<=K*U_N`. The present experiment tests only whether the
strongest conceivable `rho_m=C_m` can ever make this chain nontrivial at the
three finite hosts. It supplies no positive `rho_m`, no all-`N` estimate, and no
full-square Ramsey contradiction.

## Nearest known obstruction

Round 4 found `rho_3=rho_4=rho_5=0`; those orders cannot be rescued by scale
weights. For every `m>=6`, uniform weights fail even at `rho_m=C_m`. Nonuniform
weights remain formally open, but a positive best-case LP margin would still be
only a numerical possibility, not evidence that a suitable proper kernel
exists. Position-dependent incidences and other host regions are outside this
contract.

## Status and evidence required

Store the discovery implementation, a separate standard-library exact checker,
raw floating-point solver diagnostics labelled as non-evidentiary, exact primal
and dual rational vectors, exact margins, commands, interpreter and SciPy
versions, and SHA-256 hashes. Test the checker on a deliberately infeasible
vector and on known small feasible vectors. All statuses attach only to the
three stated finite programs. Internal verification is not external peer review
or Lean formalization.
