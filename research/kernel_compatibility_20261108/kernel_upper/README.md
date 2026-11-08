# A polynomial-weight certificate for the new joint packing count

The decisive input in this package is the parallel geometry route's count
of **disjoint** Golomb completion classes. Combining it with the existing
joint convolution argument proves `R3<=464`. Merely changing the weights
with the old separate capacities does not give this result: the same
polynomial weight has a negative old-capacity gap.

This directory supplies a short closed-form certificate and an independent
integer implementation. The geometric mechanism and its further use are
developed in the parallel geometry package. The initial Fourier scout is
retained as exploration, not as part of the proof.

## Why disjoint rulers save capacity

Assume an L-free three-color square of side n. At positive difference d,
let `p=n-d`, and define six sets indexed by distinct colors c,b:

`B_(c,b)={u: chi(u,u)=chi(u+d,u+d)=c, chi(u+d,u)=b}`.

The diagonal completion excludes b=c. Each set is Golomb: it is a diagonal
color class in the two-colored weak source inherited from the original
color-c diagonal class. Explicitly, a repeated difference in B would force
three strict weak-source cells to the remaining color, creating an L.
The six sets are pairwise disjoint, since u determines both c and b.
Their total size is the same-color diagonal difference count R_d.

Use the previously authenticated external span lower bounds
`G(24)>=425` and `G(25)>=480`. When `p<=480`, no B has25 marks. If B has24
marks its least element is at most `p-426`, since its span is at least425.
The minima of distinct B are distinct. At most
`min(6,max(0,p-425))` of the six sets can therefore have24 marks. It follows
that

`R_d <= U(p):=min(p,138+min(6,max(0,p-425)))`.

This is a joint resource count: a short prefix has only p-425 positions
available for the minima of the large classes. Separate use of six Golomb
cardinality bounds loses this competition. At p=426,...,430 the new
capacities are139,...,143, while the separate bound is144.

More generally, if q pairwise disjoint integer Golomb sets lie in p
positions, `p<=G(m+1)`, and `G(m)>=g`, then their union has at most
`q(m-1)+min(q,max(0,p-g))` points. This elementary packing statement applies
to any number of disjoint rulers. The reduction from the square to exactly
six Golomb classes is specific to three square colors; no four-color
Ramsey bound is asserted.

## Joint convolution bridge

Let f_c be the three diagonal indicators, extended by zero, and let w be
a nonnegative weight sequence supported on at most n consecutive positions.
Thus only d<n contributes. Put `a_d=sum_i w_i*w_(i+d)`.
Because `sum_c f_c` is the complete n-position indicator, pointwise Cauchy
gives `3 sum_c (f_c*w)^2 >= (1_[n]*w)^2`. Expanding and summing yields

`n*a0 >= sum_(d>=1) (n-d-3*R_d)*a_d`.

As every a_d is nonnegative, the necessary condition

`sum_(d>=1) (n-d-3*U(n-d))*a_d <= n*a0`                         (1)

follows. No class balance, G9, S21 or rainbow assumption is used.

## Closed-form contradiction at464

Take `N=86` and `w_i=i*(N-i)` for `1<=i<=N-1`, zero elsewhere. For
`0<=d<=84`, put m=N-d. Its autocorrelation has the closed form

`a_d = m*(m^2-1)*(m^2+1+5*d*N)/30`.                            (2)

To derive it, set `t_i=i*(m-i)`. The summand `w_i*w_(i+d)` is
`t_i^2+d*N*t_i`, while
`sum_i t_i=(m^3-m)/6` and `sum_i t_i^2=(m^5-m)/30`.
Thus (2) is a direct power-sum calculation, with no numerical eigenvector
in the certificate.

At n=464 all used p are between380 and463, so only the two cited Golomb
inputs are needed. The coefficient `n-d-3U(n-d)` in (1) equals

| Difference d | Coefficient |
|---|---:|
| 1 through33 | 32-d |
| 34 through38 | 2d-67 |
| 39 through84 | 50-d |

Substitution of (2) gives the following exact integers:

| Quantity | Value |
|---|---:|
| a0 | 156809003 |
| First weighted sum, d=1,...,33 | 70470797408 |
| Middle weighted sum, d=34,...,38 | 1810500079 |
| Last weighted sum, d=39,...,84 | 956045048 |
| Total left side of (1) | 73237342535 |
| Right side464*a0 | 72759377392 |
| Left minus right | **477965143** |

This contradicts (1), proving `R3<=464` using the stated external inputs.
For comparison, the same weights with separate capacities give
`-2799639872`. The distinct-minima count contributes exactly3277605015,
which changes the sign. This isolates the contribution of the new count.

At n=463 the same kernel gives `-3527580772`, and does not exclude that
side. That failure is not an optimality theorem for kernels or packing.

## Actual computation and evidence limits

Run `python research/kernel_compatibility_20261108/kernel_upper/certificate.py`
from the repository root. It uses Python integers and the polynomial
formula, checks the formula against literal products for520 parameter
pairs, and writes [certificate.json](certificate.json). Floating discovery
code is neither imported nor trusted by the checker.

Before the distinct-minimum inequality was available, an inline Fourier
LP probe used4097 equally spaced frequencies, the published full capacity
table, and sides464,463,462,460. All four returned numerically feasible.
This did not establish an actual diagonal or a rigorous feasible point
for the continuum relaxation. The saved `fourier_scout.py` repeats those
specified probes and adds the new capacity at464 and463; results are
explicitly `UNDECIDED_FLOATING_SCOUT`. They are not proof dependencies.

A positive-kernel eigenvector scout over lengths50 through120 showed the
new scalar capacity could cross464; a subsequent exact search among
parabolic weights produced the readable N=86 certificate above. Both
agents independently found this same simple weight. The floating search
does not prove optimality, and neither the weight search nor the old
convolution bridge is claimed as the new counting idea.

The external inputs were checked in the preceding package against the
primary [OGR24](https://blogs.distributed.net/2004/11/) and
[OGR25](https://blogs.distributed.net/2008/10/) completion announcements.
This work does not re-run the distributed exhaustive calculations. The
2025 comparison source is [Mammel--Smith--Yerger, Theorem6 and Algorithm3](https://arxiv.org/html/2502.05162v1).
No global literature-priority claim or Lean verification is made.

CLAIM: polynomial464 contradiction gap | MY VALUE: 477965143 | THEIR VALUE: 477965143 | VERDICT: PASS | METHOD: closed polynomial correlations independently matched with literal products

CLAIM: same kernel with old separate capacities | MY VALUE: -2799639872 | THEIR VALUE: -2799639872 | VERDICT: PASS | METHOD: exact coefficient substitution, isolating the new joint counting gain

CLAIM: numerical Fourier feasibility establishes a coloring | MY VALUE: not established | THEIR VALUE: not claimed | VERDICT: UNDECIDED | METHOD: floating relaxation has no exact coloring or continuum feasibility certificate
