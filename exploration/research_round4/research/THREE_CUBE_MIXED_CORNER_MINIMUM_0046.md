# Exactly nine mixed parallel-endpoint corners in a separated three-cube

For a proper two-color strict source, call a corner mixed when its two
equal-offset parallel endpoint cells have different colors. Write B for
their number and H for the remaining forcing corners, so T=B+H. This
note derives an exact local minimum for an injective three-cube and gives
a weight-independent construction attaining it in the dissociated case.
It is a local input, not a global source-energy bound.

## 1. A lower bound for every injective positive three-cube

Let Q be the eight distinct subset sums of three positive generators
w_1,w_2,w_3, and let V(Q) be properly two-colored. Fix a generator w_i.
Its actual difference fiber contains the four subset sums of the other
two generators. Those four starts form a nondegenerate parallelogram

    {0,w_j,w_k,w_j+w_k},

whose two positive w_j differences repeat. It is therefore not a Golomb
set. Each same-color part of an actual difference fiber is Golomb, so
these four parallel cells cannot all have one color.

If k of the four cells have one color, their six corner pairs contain
k(4-k) mixed pairs. For k=1,2,3 this is at least3. The three generators
are distinct by subset-sum injectivity, and therefore their three sets of
corner pairs have different parallel offsets. Adding gives

    B(V(Q))>=9.                                     (1)

Additional numerical difference coincidences can create more corners but
cannot remove these nine required mixed corners. No dissociation beyond
the stated injectivity is needed for (1).

## 2. A symbolic coloring attaining the lower bound

Assume now that the weights are2-dissociated: no nonzero relation with
coefficients in{-2,-1,0,1,2} holds. Label every mark by its subset of
{1,2,3}. A strict cell is specified by its unordered endpoint labels,
with its physical orientation determined by their numerical values.
Give it color1 exactly in the following three cases:

* one label is empty and the other has size1 or2;
* one label is a singleton and the other is the full three-element set;
* the two labels are a singleton and its complementary doubleton.

Give every other strict cell color0. These rules are independent of the
relative sizes of the positive weights.

To prove properness, classify positive differences by their signed
coordinate support. A support of size t has 2^(3-t) representations,
indexed by the common bits outside its support. Equality of numerical
differences is equality of signed supports by2-dissociation.

For a primitive difference w_i, the four parallel cells have common-bit
sets empty,{j},{k},{j,k}. Their colors are respectively1,0,0,0.
The pair between the empty common-bit set and a singleton common-bit
set completes at an empty/doubleton cell of color1. The pair between
the empty and doubleton common-bit sets completes at the empty/full
cell of color0. Both types have mixed parallel colors and are proper.
The three pairs between the common-bit sets {j},{k},{j,k} all complete
at color1: either a singleton/complementary-doubleton cell or a
singleton/full cell. Their parallel colors are0,0, so these corners
are proper as well. This covers all six corners at each primitive offset.

A two-coordinate signed support has two representations. If its two
signs agree, the positive difference is w_i+w_j. Its endpoint cells
are empty/doubleton and singleton/full, both color1. Their outer
completion is empty/full, color0. If its signs disagree, the two cells
join distinct singletons and distinct doubletons, respectively; both
have color0. Their outer completion is a complementary singleton/
doubleton cell, color1. These exhaust the six positive signed supports
of size2. A support of size3 has one representation and creates no corner.

Thus every actual corner is nonmonochromatic.

## 3. Exact mixed and forcing counts

There are three primitive offsets with four parallel cells each, six
two-coordinate positive offsets with two cells each, and four
three-coordinate offsets with one cell each. Consequently

    M=3*4+6*2+4=28,
    T=3*binom(4,2)+6*binom(2,2)=24.

Each primitive fiber has a1+3 color split and contributes exactly3
mixed corners. Every two-cell fiber is monochromatic under the rule,
so it contributes none. Therefore

    B=9, H=15.                                      (2)

Together with (1), this proves that9 is the exact minimum number of
mixed parallel-endpoint corners on a separated three-cube. It also
shows directly that an all-forcing proper source cannot contain an
injective positive three-cube.

The new rule differs from the earlier symmetric0044 strict three-cube
rule in the three empty/doubleton cells. Its use here is the new exact
mixed-corner minimum; no earlier properness proof is being rechecked.

## 4. Scope of a global application

Applying (1) to many cubes requires an exact multiplicity bound for how
often one mixed source corner appears in their three primitive fibers.
Such a global constant has not been established. Sources with Golomb
overlaps may have no nontrivial three-cubes while their uncolored energy
is large; their full properness is a separate question. Thus neither
(1) nor (2) alone proves H10, S21, or a new Ramsey bound.
