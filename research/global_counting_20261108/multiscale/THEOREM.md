# Counting the span paid by incompatible extremal shapes

Status: **PROVED using the cited OGR-24 uniqueness theorem and OGR-25 span
bound**. No exhaustive optimal-ruler computation is repeated here.

## A general span-cost inequality

Let `B_1,...,B_t` be disjoint m-mark Golomb sets in p consecutive integer
positions. Suppose every m-mark Golomb set has span at least g, and at most
`a` sets of span exactly g can occur disjointly in this interval. Then

`t*g + max(0,t-a) <= t*(p-t)`.                         (1)

For the lower bound, all but at most a classes have integer span at least
g+1. For the upper bound, let l_i and r_i be the distinct minima and distinct
maxima. Independently sorting these two sets of endpoints gives

`sum_i (r_i-l_i) <= [(p-t)+...+(p-1)]-[0+...+(t-1)]`

`                    = t*(p-t)`.

No correspondence between the sorted minima and sorted maxima is assumed.
Empty classes are excluded from this statement because t counts only the
m-mark classes. The inequality concerns the total span, not a disjointness
assumption about the difference sets.

More generally, assume every class has span at least g_0. If successive
span levels `g_0<g_1<...<g_s` are integers and at most a_j of the t classes
can have span strictly below g_j, then

`sum_i span(B_i) >= t*g_0 + sum_(j=1)^s (g_j-g_(j-1))*max(0,t-a_j)`.

This follows by writing a span as its successive level increments. It is
valid only when every a_j is independently proved. The present application
uses only `g_0=425,g_1=426,a_1=2`; it does not assume information about
longer 24-mark rulers.

## At most two optimal 24-mark shapes

The primary [OGR-24 completion announcement](https://blogs.distributed.net/2004/11/)
(2004-11-01, nugget entry) explicitly reports uniqueness up to reflection
as well as optimal span 425. In ascending marks the unique normalized ruler is

`Q=(0,9,33,37,38,97,122,129,140,142,152,191,205,208,252,278,`
`   286,326,332,353,368,384,403,425)`.

The adjacent gregh explanation reports that its first missing positive
difference is128; the exact checker independently verifies that every
integer1 through127 occurs once in Q. The primary uniqueness statement is
stronger input than the optimum-span statement used by the preceding464
certificate, and is recorded separately here.

If two translates of Q lie in p positions with `p<=553`, their starting
positions differ by at most127. A positive difference in that range belongs
to `Q-Q`, so the translates intersect. Identical starting positions also
intersect. The same argument applies to the reflected shape `425-Q`.
Consequently any disjoint family of span425 rulers in such an interval has
at most two members, one from each orientation.

The number two is attainable in427 positions: `Q+1` and `425-Q` are
disjoint. The checker records both explicit sets and verifies all differences.
This witness is a packing of rulers, not a proper weak-source or square
coloring, and makes no lower-bound claim.

## Four stronger subdiagonal capacities

For `p<=480`, the [OGR-25 completion announcement](https://blogs.distributed.net/2008/10/)
gives `G(25)>=480`, so a Golomb set in p positions has at most24 marks.
Let t be the number of 24-mark sets among six disjoint Golomb classes.
Then their total cardinality is at most `138+t`, and (1) gives

`425*t+max(0,t-2) <= t*(p-t)`.                         (2)

For p=428,429,430,431 the old distinct-minima count allowed respectively
t=3,4,5,6. Each of these choices makes the right side `425*t`, strictly
smaller than the left side. Thus the valid combined capacity is

| p | Previous joint capacity | With extremal-shape cost |
|---|---:|---:|
|428|141|140|
|429|142|141|
|430|143|142|
|431|144|143|

In the range1 through480 no other improvement follows from (2) alone.
Use `min(p,138+t_max(p))`, where t_max is the largest integer0<=t<=6
satisfying (2). These are bounds, not assertions of attainability.

For the original square, the six classes are

`B_(c,b)(d)={u: chi(u,u)=chi(u+d,u+d)=c, chi(u+d,u)=b}`, `b!=c`.

Their pairwise disjointness and Golomb property are proved in
[`../../kernel_compatibility_20261108/geometry/SIX_CLASS_LEMMA.md`](../../kernel_compatibility_20261108/geometry/SIX_CLASS_LEMMA.md).
Apply the present inequality with p=n-d. It is important that the six
classes coexist on one physical set of starts: this proof cannot be obtained
by adding six independent span bounds.

The shape-cost and colored-boundary-word bounds constrain the same t. Their
numerical savings must not simply be added. If `k=p-425` lies in3 through6,
the boundary-word value is capped further at k-1; use the minimum of the
two capacities before optimizing across d.

## The same extremal shapes across all offsets

The coordinator proposed the following global extension. Let the whole
main diagonal have length n<=553. For Q or its reflection P, let T_P be
the starts s for which P+s is monochromatic. Two distinct starts have
distance at most n-426<=127. Since this distance occurs exactly once in
`P-P`, their copies intersect in exactly one mark. Therefore all
monochromatic copies of one orientation have the **same original color**.
The two orientations can have equal or different original colors; neither
case is excluded in the argument.

Put t=|T_P|, and let r(x) count the copies containing x. Then exactly

`sum_x r(x)=24*t`,

`sum_x binom(r(x),2)=binom(t,2)`,

`sum_x r(x)^2=t*(t+23)`.                              (3)

The second equality counts each unordered pair of copies at its unique
intersection. If their common original color class has cardinality m,
Cauchy applied on their union and ordinary two-term inclusion-exclusion give

`m >= ceil(576*t/(t+23))`,

`m >= 24*t-binom(t,2)`.                               (4)

The first bound is interpreted as zero at t=0. It avoids the decreasing
tail of the second bound for large t. These inequalities count actual
overlaps, retaining a constraint across offsets that a separate span
capacity discards.

For every extremal completion class of orientation P at offset d, its
start s has both s and s+d in T_P, and its original diagonal color is the
common color of those occurrences. The class injects into the occurrence
pair `{s,s+d}`. Accordingly, for arbitrary nonnegative weights v_d,

`sum_d v_d*e_P(d) <= sum_(s<t in T_P) v_(t-s)`,         (5)

where e_P(d) counts extremal completion classes of orientation P at d.
Moreover e_P(d)<=1 by the single-offset packing argument. Equality in (5)
is not asserted: a pair of monochromatic occurrences need not make its
completion cells monochromatic.

### Quantification at n=463 and464

The following standard one-class convolution estimate was supplied by the
coordinator to quantify (4). For the indicator f of one original diagonal
color class, put `w_i=i*(86-i)`, 1<=i<=85, and use the correlations a_d
defined in the preceding package. The convolution support has n+84
positions and its sum is `m*W`, where W=105995 and a_0=156809003. Hence

`m^2*W^2 <= (n+84)*(m*a_0+S_n)`,

`S_n=2*sum_(d=1)^84 C(n-d)*a_d`,

where C(p)=48 for p>=426 and C(p)=46 for p<=425 in the range used here.
This follows by Cauchy and the two-Golomb bound on one color's pair counts.
Only the cited G24/G25 inputs are needed, because n-d>=379. Exact integer
substitution shows m<=164 at both n=463 and464. The small-rank counts are
not premises of this estimate.

There are at most n-425 possible starts of P. Evaluating both inequalities
(4) for these integer t shows `|T_P|<=8` at both candidate sides. Therefore
each orientation supplies at most28 extremal completion classes in total
across all d, and both orientations together at most56. This global count
is stronger than allowing two independent extremal classes at every one
of the37 or38 available positive offsets. It concerns **span425 classes**,
not every24-mark class; larger-span classes must retain their extra cost.

Equations (1), (3), and (5) can be used together: a class avoiding the
global extremal-occurrence budget must pay span at least426. A complete
optimization retaining this global tradeoff and producing a smaller R3
has not been carried out here. Neither the count56 nor the four corrected
scalar capacities alone proves a new Ramsey bound.

## Scope and provenance

The general endpoint inequality is elementary. The new use in this project
is to charge incompatible extremal shapes against the common sum of spans.
No historical priority claim is made. The primary reports were read on
2026-11-08; the OGR-24 source specifically states uniqueness, while the
near-optimal table at <https://www.feiri.de/ogr/nearopt.html> leaves longer
order24 entries blank. Blank entries are not zeros and provide no additional
exclusion here.

The source-type exploration also rediscovered AP5 uniqueness. A repository
search found it already proved in `exploration/research_round3/cap/ap5_uniqueness.md`
and independently reviewed under `audits/setup_sol/`. It is not counted as
a new result of this package. The adjacent-translate near-sum obstruction
and signed support correlation also already exist in research_round4.

For k>3 square colors, deleting one diagonal color does not leave a binary
weak source; the six-Golomb-class reduction does not apply. The abstract
span-cost theorem remains valid for any number of disjoint Golomb sets.
