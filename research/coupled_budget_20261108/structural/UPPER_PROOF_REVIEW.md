# Independent upper-bound review

Reviewer route: `/root/structural`, independent of the numerical discoverer.
Base: `df6e35cfff68580dc78aa91bc35d4c6399a6464a`.

## Verdict and dependencies

**PASS for the mathematical implications and exact arithmetic.** The joint
rank-pair argument excludes side 466 using the stated published Golomb table.
The inherited convolution argument already excludes side 465 using only
`G(24)>=425` and `G(25)>=480`. The latter is stronger and is historical work,
not a new discovery in this round. Neither implication uses the refuted
rainbow lemma, `G(9)`, or the failed `S21` proposal.

This review independently derives the implications and recalculates their
integer certificates. It does not independently replay the external Golomb
exhaustions. Acceptance of cited mathematical results and a requirement for
local exhaustive replay are distinct evidence standards.

## Geometry and Golomb bridge

Let `A` be one color class on the main diagonal of an L-free three-color
`n`-square, indexed by integers 1 through n. A cell `(v,u)` with `u<v` in A
cannot have A's color: together with `(u,u)` and `(v,v)` it would be a
forbidden directed L. Thus the complete strict source on A is two-colored.

Fix `d>0`, and put `F_d={u:u,u+d in A}`. The induced weak source on `F_d`
has color `w(v,u)=color(v+d,u)`, for `u<=v`. A directed L in this weak source
would translate to an L in the original square. Each color class on the
weak-source diagonal is Golomb. To check the last assertion, repeated
differences `b-a=e-c=t>0`, with `a<c`, give diagonal pairs `(a,b)` and
`(c,e)`: the completion cells `(b,a)` and `(e,c)` have the opposite color.
These two cells are separated by the same positive step `c-a=e-b`.
Their completion `(e,a)` must then have the original color; but its diagonal
endpoints `(a,a)` and `(e,e)` also have that color, a contradiction. This
includes the overlapping case `b=c`.

The marks in `F_d` occupy at most `n-d` integer positions (span at most
`n-d-1`). Consequently

`r_d(A) <= C_d := min(n-d, 2*g(n-d))`,

where `g(L)` bounds the number of Golomb marks in L occupied positions.
The occupied-position table is printed in Algorithm 3 of
[Mammel--Smith--Yerger, arXiv:2502.05162v1](https://arxiv.org/html/2502.05162v1).
This explains the off-by-one convention in the code: order 24 needs at
least 426 positions, and order 25 at least 481 positions.

## Joint rank-pair argument at side 466

The independent script `audit_joint_bound.py` uses the published thresholds,
not the numerical discoverer's implementation. At `n=466`, it obtains
`sum_d C_d=15624`. Since `binom(178,2)=15753`, each diagonal color class has
at most 177 marks. Since there are three classes partitioning 466 positions,
each has at least 112 marks.

In each class `a_1<...<a_m`, select all pairs `(a_i,a_(i+j))` with
`1<=j<=k=22`. There are `km-k(k+1)/2` such pairs. Their total count across
the three classes is therefore `K=9493`. At distance d at most `3*C_d`
pairs can be selected. Filling these capacities in increasing d minimizes
the sum of distances: moving any unit from a larger occupied distance to a
smaller unsaturated one decreases that sum. The exact lower bound is 319760.

The coefficient of `a_r` in a class's selected distance sum is
`min(k,r-1)-min(k,m-r)`. As `m>=112>=2k`, its coefficient multiset is
`-k,...,-1`, `m-2k` zeros, and `1,...,k`. Across all three classes there
are exactly three copies of each nonzero coefficient. Each position
1 through n occurs once. The rearrangement inequality therefore gives

`sum(selected distances) <= 3*k*(k+1)*(n-2*k-1)/2 = 319539`.

One can obtain the formula directly by pairing each positive coefficient
with its negative coefficient and placing the largest positive weights at
the largest positions. The independent script also explicitly constructs
and sorts all coefficients for all 2211 feasible ordered class-size
triples. The contradiction margin is `319760-319539=221`.

At side 465 this same `k=22` certificate has margin -339 and does not
prove exclusion. This failure does not invalidate the stronger historical
convolution proof below.

## Historical convolution argument at side 465

Let `f_c` be the indicator of diagonal color class c, extended by zero
outside `[1,n]`. For finitely supported nonnegative weights `w_i`, set
`X_c(t)=sum_i w_i*f_c(t+i)`, `W(t)=sum_c X_c(t)`, and
`a_d=sum_i w_i*w_(i+d)`. Cauchy--Schwarz gives
`sum_c X_c(t)^2 >= W(t)^2/3` for every integer t.

Write `S_d=sum_c r_d(A_c)`. Summing over t and expanding both squares gives

`n*a_0 + 2*sum_(d>0) a_d*S_d >= (n*a_0 + 2*sum_(d>0) (n-d)*a_d)/3`,

where `(n-d)` is replaced by zero for d>=n. All used d below are less than
n. If every class satisfies `r_d<=2*b(n-d)`, then `S_d<=6*b(n-d)`.
Since every `a_d>=0`, substitution and rearrangement give the necessary
inequality

`sum_(d>0) (n-d-18*b(n-d))*a_d <= n*a_0`.

Take `n=465` and `w_i=min(i,94-i)` for `i=1,...,93`. The only nonzero
positive correlations have `1<=d<=92`. The two external inputs give
`b(n-d)<=24` for `1<=d<=39` and `b(n-d)<=23` for `40<=d<=92`.
In the first interval the largest possible span is 463, below 480;
in the second it is 424, below 425. These are upper bounds on Golomb
cardinality, not assertions that all such cardinalities are attainable.

The independent direct products in `audit_convolution.py` give

| Quantity | Exact value |
|---|---:|
| `a_0` | 69231 |
| `P=sum_(d=1)^39 a_d` | 2038439 |
| `Q=sum_(d=40)^92 a_d` | 366786 |
| `D=sum_(d=1)^92 d*a_d` | 53496528 |
| `465*(P+Q)-D-18*(24*P+23*Q)-465*a_0` | **285630** |

The positive final line contradicts the necessary inequality. The old
proof is already recorded in
`exploration/research_round4/checks/build_verification_report.py`, under
"Direct conditional proof of the inherited three-color bound". Its earlier
pending status concerned the external-input verification standard. It is
incorrect to reject this implication merely because a different historical
rainbow route was refuted.

## Reproduction and scope

Run `python audit_joint_bound.py` and `python audit_convolution.py` from
this directory. Their JSON records contain exact values and code hashes.
This is a written mathematical review with independently recomputed finite
sums, not a Lean formalization or a new proof of Golomb ruler optimality.
