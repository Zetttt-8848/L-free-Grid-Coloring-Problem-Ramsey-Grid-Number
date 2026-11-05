# Research progress report

Prepared at the user's request after the0046 research batch. This report
supersedes the earlier request to withhold intermediate results. It does
not claim completion of the original research campaign.

## Completed objectives and approximate percentage

Of the four original major objectives, **one is complete and three remain
open**.

| Original objective | Status |
|---|---|
| A new reusable method demonstrated to improve the small-color bounds | Incomplete: several new mechanisms and intermediate theorems, but no successful global bound |
| Prove R3(L)<465 | Incomplete: working bound remains 21<=R3(L)<=465 |
| Prove R4(L)<100000, striving for <10000 | Incomplete: working upper bound remains21991300 |
| General C^{p(k)} bound with polynomial p | Complete as an attributed literature corollary, not an original theorem |

Counting these objectives equally gives **25% completion**. This is an
objective-count measure only. Research difficulty is uneven, and the
central breakthrough remains missing, so it is not a reliable estimate
of time remaining or proximity to a proof.

The latest batch completed **ten research/support notes**: seven
derivation or construction notes, two bounded computational summaries,
and one literature map. Intermediate notes are not additional completed
major objectives. CHECKPOINT_0046.md lists the exact inventory.

## How far the campaign is from completion

Neither small-color upper bound has improved. The remaining work requires
a new global mathematical argument, not merely finishing calculations or
writing up an existing proof.

A concrete sufficient remaining target is

    binom(|A|,2)<=21span(A)

for every properly two-colored strict source triangle in the stated
finite span range. Its complete conditional transfer would give

    R3(L)<=379, R4(L)<=99996.

Those numbers are conditional; the source inequality is unproved.
They show exactly what an adequate new source theorem would achieve.
The more ambitious R4(L)<10000 target needs further strength.

## Valuable theorems developed in the campaign

1. **Two-Golomb energy theorem.** If S is the disjoint union of two Golomb
   sets and n=|S|, then

       T(S)<=2binom(n,2), E(S)<=6n^2-5n.

   This improves the earlier class estimate and applies to every proper
   weak source and every actual weak difference fiber. It does not
   automatically apply to an arbitrary proper strict source.
   Full derivation: TWO_GOLOMB_MIXED_ENERGY_0040.md.

2. **Cube capacity and dimension boundary.** A Golomb subset of any
   injective positive Boolean four-cube has at most seven marks. Thus a
   proper weak source occupies at most14 of its16 vertices, and a proper
   strict source occupies at most30 of any five-cube's32 vertices.
   A symbolic proper strict four-cube construction exists. Consequently
   the largest full cube dimension in the separated family is exactly4.
   Full derivations: CUBE_PAIR_CAPACITY_0045.md and
   fibers/FOUR_CUBE_NONLINEAR_CONSTRUCTION_0045.md.

3. **Sharp three-cube mixed-corner theorem, new in0046.** Every proper
   two-color strict source containing an injective positive three-cube
   has at least nine mixed parallel-endpoint corners within that cube.
   A new symbolic coloring attains nine for separated weights. This is
   an exact structural cost of keeping such a cube properly colored.
   Full derivation: THREE_CUBE_MIXED_CORNER_MINIMUM_0046.md.

4. **Distinct-mark cost of a forcing biclique.** In a complete separated
   one-column forcing block with p inputs and q outputs, all pq third
   source marks are distinct. This converts one type of dense color
   interaction into an explicit source-size cost. New0046 companion
   lemmas also force either missing source marks or specified mixed
   corners when forcing configurations overlap. The still-missing step
   is a global bound on reuse across all such configurations.
   Full derivations: ANCHORED_REFLECTED_PRODUCT_FORCING_0045.md and
   fibers/COMPANION_FORCING_CUBE_SLOTS_0046.md.

Other bounded0046 results include T(S)<=2|B||C| when one Golomb diagonal
class has at most two marks, and the sharp endpoint deletion bound
e_0(A)<=|A|-2 for an all-forcing source with exactly one exceptional
anchor-color mark. These have narrower hypotheses.

The campaign also produced explicit counterexamples to tempting global
forcing-load and graph-degeneracy estimates. They are useful negative
results: they prevent false premises from entering the main argument.

These are new derivations within this project. A claim of priority over
the entire mathematical literature has not been established. None of
the intermediate theorems above currently proves a new unconditional
R3 or R4 upper bound.

## Completed general objective

GENERAL_BOUND.md derives

    R_k(L)<=ceil(exp(C(log(2k))^600))<=D^{k^600}

from Jaber-Liu-Lovett-Ostuni-Sawhney, arXiv2504.07006v1, Theorem1.1,
with absolute unspecified constants and the required positive-direction
and no-wraparound transfer. It satisfies the requested growth form but
provides no usable numerical R3 or R4 bound.
