# A positional budget for supported internal reflections

Root derivation, continuation 0040. This sums a new fixed-output
multiplicity bound across both diagonal color classes, retaining their
order. It bounds internally reflected triples, not every additive
parallelogram, and it does not give a weak-source span bound by itself.

Let B,C be disjoint finite Golomb sets, of sizes b,c. For r not in B put

    mu_B(r)=#{a<t<q in B:r=a+q-t}.

The auxiliary derivation fibers/GOLOMB_REFLECTION_MULTIPLICITY_0040.md
proves the positional bound

    mu_B(r)<=min(|B intersect (-infinity,r)|,
                  |B intersect (r,infinity)|).        (1)

Indeed every reflected triple has a<r<q. A fixed lower extreme a fixes
the positive difference q-t=r-a, hence the whole triple by Golombness.
A fixed upper extreme q similarly fixes t-a=q-r. Thus both extremal
maps are injective. The uniform coefficient 1/2 at a fixed r is sharp;
the auxiliary note gives finite and infinite constructions, so it
cannot be replaced by a smaller constant without another hypothesis.

Define the two-color internal reflection count

    K=sum_(r in C) mu_B(r)+sum_(r in B) mu_C(r).      (2)

We prove

    K<=floor(bc/2).                                 (3)

## 1. Symmetric rank pairs count the available capacity

Order B as b_1<...<b_b and pair its outer ranks into open intervals

    I_i=(b_i,b_(b+1-i)), 1<=i<=floor(b/2).

For any r outside B, exactly
min(|B<r|,|B>r|) of these intervals contain r. Consequently the first
sum in (2) is at most sum_i |C intersect I_i|. Define likewise

    J_j=(c_j,c_(c+1-j)), 1<=j<=floor(c/2),

from the ordered C marks. The second sum in (2) is at most
sum_j |B intersect J_j|. Thus

    K<=sum_i |C intersect I_i|+sum_j |B intersect J_j|. (4)

## 2. Each pair of rank intervals has capacity two

Fix I_i and J_j. Their four endpoints are distinct because B,C are
disjoint. Count the endpoints of J_j lying in I_i, together with the
endpoints of I_i lying in J_j. The count is zero for disjoint intervals,
two for nested intervals, and two for crossing intervals. In particular
it is at most two in every case.

Let u=floor(b/2), v=floor(c/2), epsilon=b-2u, eta=c-2v, so epsilon
and eta are each zero or one. The paired endpoints in (4) therefore
contribute at most 2uv. If C has an unpaired median, its contribution
to the B intervals is at most u; if B has an unpaired median, its
contribution to the C intervals is at most v. Hence

    K<=2uv+eta u+epsilon v
      =floor(bc/2),                                 (5)

which proves (3), including empty or singleton parts.

## 3. Actual weak colors and the missing part of the count

When B,C are the diagonal classes of one proper weak source W(S), an
internal B triple a<t<q reflected to r in C forces the two actual
mixed cells

    z(r,a)=z(q,r)=the B diagonal color.

These are the two reflected-triple orientations. The bound (3) therefore
limits the total number of such supported forcing events across both
colors, and improves the coarser unweighted bc count for this particular
internal-triple inventory.

The unsupported inventory is exactly

    binom(b,3)+binom(c,3)-K,

since the internal reflection of a same-class triple cannot return to
that Golomb class. These missing reflected marks can still recur across
many triples. Bound (1) limits recurrence at a fixed mark, but summing
its two color capacities over all missing positions does not currently
give the required source-size estimate. Also, reflections placing the
new mark outside the triple's hull are not included in K. They must
not be inserted into (3) without a different derivation.

Thus (3) is a complete new positional budget and an actual-color input
for the weak-source route; it is not a proof of C46/45(463), S21, or a
new small-color Ramsey number.

## 4. A Golomb set admits every one-point weak extension

There is a direct construction showing that mere weak-source properness
cannot improve the fixed-output coefficient 1/2. Let B be any Golomb
set and r any integer outside it. On W(B union {r}), assign:

* diagonal B cells color +, and (r,r) color -;
* every strict cell with both coordinates in B color -;
* every strict cell incident with r color +.

We prove properness by the two parallel endpoint cells of a corner.
At offset zero, two + endpoints are distinct B diagonal cells and
their completion is a - strict B-cell; there is only one - diagonal
cell. At a positive offset, there cannot be two - endpoints, because
they would be two different B-pairs with the same positive difference.
Two + endpoints must both be incident with r. At one fixed positive
offset d, the only two possibilities are (r,r-d) and (r+d,r); if both
exist, their completion (r+d,r-d) is a - strict B-cell. Thus every
equal-color endpoint pair has an opposite-color completion.

This works for every position of r, with no new support premise. Apply
it to the equality families in GOLOMB_REFLECTION_MULTIPLICITY_0040.md:
the other diagonal class is the singleton {r}, and mu_B(r) still
attains floor(|B|/2). Therefore a uniform smaller coefficient at a
single opposite-color output is false even under actual proper weak
coloring. A stronger estimate would have to use several output marks
simultaneously, a span restriction, or another additional hypothesis.
