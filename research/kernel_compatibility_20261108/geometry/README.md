# Six disjoint completion classes: a joint bound that reaches464

This work proves the shared-position bound

`R_d <= sum_(j=0)^5 g(n-d-j)`

for the total number R_d of same-color main-diagonal pairs at difference d
in any proper three-color square. Here g(p) is maximum Golomb cardinality
in p consecutive positions. The six classes are defined from **actual**
diagonal/completion color pairs and are disjoint, so their minima cannot
reuse positions. This improves on summing six independent capacities.

Using only G(24)>=425 and G(25)>=480, this joint count with the explicit
weights `w_i=i*(86-i)`, i=1,...,85, proves **R3<=464**. The exact positive
contradiction margin is477965143. The same weights with independent
capacities give -2799639872; the new compatibility count is essential to
this certificate.

[SIX_CLASS_LEMMA.md](SIX_CLASS_LEMMA.md) gives the full geometric reduction,
arbitrary-q packing lemma, threshold conventions, weighted inequality and
source boundaries. It also derives a stronger color-incidence inequality
for adjacent differences; its further numerical consequence is not claimed
in this directory. Disjoint Golomb rulers and endpoint packing are existing
subjects, so no global priority claim for those ideas is made.

## Exact checks

From the repository root:

```sh
python research/kernel_compatibility_20261108/geometry/audit_464.py
python research/kernel_compatibility_20261108/geometry/verify_geometry.py
```

Both use Python's standard library only. The first reconstructs85 integer
weights, all autocorrelations, the joint-capacity margin and a second
literal-convolution Cauchy margin955930286. It imports no numerical or
discovery implementation. [audit_464.json](audit_464.json) records every
integer and binds the input proof and checker hashes.

The second independently checks:

- all2470 Ls of the published20-square and its actual six classes;
- all59049 three-color assignments of the complete10-cell weak triangle
  of side4, including all17316 proper assignments, with no symmetry quotient;
- all4096 subsets of12 positions, giving463 Golomb subsets, and exact
  two-class disjoint packing optimum9. Separate capacity would be10;
  the new joint bound is9 and an explicit disjoint pair attains it.

The latter checks audit the formula and illustrate a strict shared-position
gain; the universal statements are established by the written proof.
No larger square existence or nonexistence is inferred from small checks.
Results and hashes are in [geometry_verification.json](geometry_verification.json).

Discovery used a floating eigenvalue scout to choose a smooth weight shape,
then replaced it with a simple polynomial formula. Only the exact integer
certificate is used. Parent and numerical routes independently derived
the geometry and coefficient expansion. The external distributed Golomb
optimality computations were authenticated by source, not rerun locally.
No Lean formalization or global literature novelty audit is claimed.
