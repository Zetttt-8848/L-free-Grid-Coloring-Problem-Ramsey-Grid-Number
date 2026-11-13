# Counting colored recurrence across every cardinality threshold

Status: the inequalities below are **PROVED** by the displayed arguments.
The final word-independent optimization is **UNDECIDED**. No numerical
improvement over `R3 <= 464` is asserted by this package.

## 1. The object that scalar capacities discard

Let `g(p)` be the maximum size of an integer Golomb set in `p` consecutive
positions, and put `g(p)=0` for `p<=0`. Write `G(m)` for the minimum span
of an m-mark Golomb ruler, with `G(1)=0`. Thus

`g(p) = sum_(m>=1) 1[p >= G(m)+1]`.

This section states an exact identity with the actual extremal function.
Certified lower bounds on `G(m)` give upper bounds on its right side and
can be used instead, provided every cardinality allowed in the ambient
interval has a justified threshold. Omitting a level is not permitted.

For a hypothetical L-free three-color square, let `A_c` be the positions
of diagonal color c. At lag d put `p=n-d` and

`F_c(d) = {u in [0,p): u,u+d in A_c}`, `r_c(d)=|F_c(d)|`.

The actual completion colors split F_c(d) into at most two disjoint
Golomb classes. This geometric reduction is proved in the preceding
checkpoint's `geometry/SIX_CLASS_LEMMA.md`. It uses the specified directed
equal-leg L and is not being assumed for arbitrary three-color graphs.

For a fixed c,d, let `s_c,1 < s_c,2` be the first two members of F_c(d),
using an absent contribution of zero if fewer than two exist. Define

`P_c(d) = g(p-s_c,1) + g(p-s_c,2)`.

**First-return theorem.** `r_c(d) <= P_c(d)`.

Proof. Order the minima of the nonempty completion classes. Their first
minimum is at least s_c,1, and their second, if present, is at least s_c,2,
because they are distinct members of F_c(d). A class whose minimum is u
fits inside p-u positions, so has size at most g(p-u). Monotonicity of g
gives the assertion. If only one class is nonempty the unused summand is
nonnegative; empty cases are immediate.

This differs from replacing all six minima by 0,...,5: it retains the
actual color and the actual lag of each first return.

## 2. An all-level capped-autocorrelation identity

Put `b_m=n-G(m)` and let `A_c^(m)=A_c intersect [0,b_m)`, with an empty
set when `b_m<=0`. Then exactly

`P_c(d) = sum_(m>=1) min(2, r_d(A_c^(m)))`,                 (1)

where `r_d(S)=#{u:u,u+d in S}`.

Indeed `p-s_c,i >= G(m)+1` is equivalent to
`s_c,i < n-G(m)-d = b_m-d`. The number of the first two return positions
satisfying this inequality is the smaller of two and the number of all
such returns. These are exactly the pairs counted by r_d(A_c^(m)). Sum
the indicator identity over m. All sums are finite.

Formula (1) is a simultaneous count over **every cardinality level**.
The level-24 term used previously is only one summand. The prefixes are
nested and come from one actual diagonal word; they cannot be optimized
independently. Reversing the word yields an analogous suffix functional
Q_c(d), and `r_c(d) <= min(P_c(d),Q_c(d))`.

The pointwise estimate can also retain the elementary bound r_c(d)<=p,
or any separately proved bound. No strict-source count has been substituted
for a full-square coloring.

## 3. A two-end transport improvement

First and last returns are not independent resources. For a nonempty
finite set `F={f_1<...<f_r}` that is the union of at most two disjoint
Golomb sets, define E(F)=1 if r=1, and for r>=2 define

```
E(F) = max(
    g(f_r-f_1+1) + g(f_(r-1)-f_2+1),
    g(f_(r-1)-f_1+1) + g(f_r-f_2+1)
).
```

For F empty set E(F)=0. Then

`|F| <= E(F)`.                                            (2)

Proof. When two classes are nonempty, order their minima and maxima
separately. The ordered minima are coordinatewise at least f_1,f_2;
the ordered maxima are coordinatewise at most f_(r-1),f_r. Their actual
class incidences form one of the two matchings between these ordered
pairs. Replacing minima downwards and maxima upwards cannot decrease
either permitted size. The class-size sum is bounded by the matching's
sum of g-values, hence by their maximum. With only one class, its bound
g(f_r-f_1+1) is contained in the first displayed sum. The convention
g(nonpositive)=0 handles r=2 and crossed endpoint positions.

For F within [0,p), E(F) is at most both the first-return bound
`g(p-f_1)+g(p-f_2)` and its reverse
`g(f_r+1)+g(f_(r-1)+1)`: each matching is bounded by either sum separately.
Thus (2) can strengthen even the minimum of the separate prefix and
suffix bounds. It retains which two ends can belong to the same class.

For a concrete strict separation, consider
`F={0,2,3,4,5,6,7,8,11,12}` inside fourteen positions. The first-return
bound, last-return bound, and twice the Golomb capacity of its occupied
span are all 10. In contrast, each endpoint matching has capacity 9:
`g(13)+g(10)=5+4` and `g(12)+g(11)=5+4`. Thus this ten-mark set cannot be
partitioned into two Golomb sets. This follows from the displayed count;
the checker additionally examines all 1024 partitions. It is an example
of a restriction lost by both separate endpoint budgets, not a square
coloring counterexample or a new Ramsey bound.

The identical proof works for q classes: for each possible number t<=q
of nonempty classes, match the t smallest available marks to the t largest
available marks, sum the corresponding g(interval-length) values, and
take the maximum over matchings and t. This is a general disjoint-ruler
transport inequality. The reduction to q=2 per diagonal color is the
three-square-color part of the argument.

## 4. Exact bridge to the square upper bound

Let `w>=0` be supported on at most n consecutive positions and
`a_d=sum_i w_i*w_(i+d)`. For a diagonal word z define

`C_d(z)=sum_c min(P_c(d),Q_c(d),E(F_c(d)))`.

Since E already implies the two one-ended bounds, one may simply use
`C_d=sum_c E(F_c(d))`. We display all three to show the provenance of
the constraints. The actual `R_d=sum_c r_c(d)` satisfies `R_d<=C_d(z)`.
The same three-color convolution Cauchy inequality as the previous
checkpoint gives the necessary condition

`sum_(d=1)^(n-1) (n-d-3*C_d(z))*a_d <= n*a_0`.            (3)

Alternatively, using the first-return count alone, a sufficient condition
for exclusion of side n is the **universal** inequality

```
max over all three-color words z of length n:
    sum_m sum_c sum_(d>0) a_d * min(2,r_d(A_c^(m)))
  < (sum_(d>0)(n-d)*a_d - n*a_0)/3.
```

This is a concrete new counting target with all multiplicities retained:
each term is a level, a diagonal color, and a lag of the same word.
It is not a statement that the maximum has been evaluated. Replacing the
maximum by random words, short-word experiments, or separately chosen
level maximizers would not prove (3) impossible.

## 5. Scope and the remaining obstruction

The resource identity improves the *information retained*, not yet the
published numerical bound. A root-level scout found that merely summing
scalar disjoint-minimum bounds at all available thresholds did not exclude
a side below 464. That experiment is separate from the proof here.

The next useful step is a universal weighted count for nested capped
autocorrelations or for the two-end matching functional. It must exploit
that the colors at all levels and lags come from the same word. Merely
lengthening the earlier K=9 finite boundary enumeration does not establish
that general estimate. General originality priority has not been audited;
the disjoint-ruler setting and classical convolution ideas predate this
checkpoint. The claimed contribution here is this explicit colored,
all-level, two-end resource formulation and its proved square bridge.
