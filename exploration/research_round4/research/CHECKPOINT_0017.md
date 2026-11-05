# Research checkpoint R4-RESEARCH-0017

This checkpoint preserves the new routes from rounds 0016--0017 and the
launch of source-compatible work for 0018. The campaign is incomplete.

## Mandate and communication

The controlling objective remains the file in attachment
1b639c86-e74d-43dc-b451-d0fd3ce53dfc, read again in this continuation.
The user subsequently requested continued in-depth research and no results
output until all objectives are achieved. Intermediate mathematics is being
saved locally. No results summary should be presented as completion.
The active substantive goal was recreated after get_goal returned null.

Continue invention and full derivations. Do not conduct independent
verification, proof audits, repeated checking, or review of completed notes.
The general literature growth bound is already complete and attributed.
Do not replay its transfer or the completed eight-mark proof from 0015.

Working bounds remain 21<=R3<=465 and R4<=21991300. S11 and H5 remain open.
The newly explored routes have not changed those bounds.

## 1. Retained dyadic and reflected-corner results

fibers/DYADIC_CHARGING_0016.md derives an injective fixed-(d,h) endpoint
route for bichromatic diagonal pairs, using the supported reflected corner.
For H<=h<2H, it gives T_H<=2g_H M and

    X_H^2/(4M)-X_H/2 <= 2g_H S_<H,
    g_H=floor((1+sqrt(8H-7))/2).

The factor counts physical centers; it is not a pointwise completion cap.
The properly colored dilated five-mark interval has T_H=3M/5, so an
uncorrected M/2 bound for each dyadic band is false.
The signed-fiber-only six-edge path bound is weaker than the inherited
weak-triangle AP5 exclusion: actual F_d runs have at most three edges.

fibers/REFLECTION_CLOSURE_0016.md derives the exact h-run discrepancy
between monochromatic pairs on offsets d and d+h, bounded by one endpoint
term per run, and a weighted path inequality. Summing in d does not
automatically telescope: the positive term needs four source marks, while
the translated reflected term needs six. The note retains this support
mismatch explicitly.

## 2. The standalone Cartesian route is now closed

A proposed shortcut was C(c): a proper two-color Cartesian product B x C
has U(B,C)=sum_h r_B(h)r_C(h)<=c|B||C|. Both c=2 and c=3/2 were considered.

**Every universal constant version is false.** The complete new direct
construction is fibers/BINARY_STRIP_CONSTRUCTION_0017.md:

    C_m={2^j-1:0<=j<m},
    color(x,2^j-1)=floor(x/2^j) mod 2,  x in Z.

For j<k the column gap 2^k-2^j is an odd multiple of 2^j, so the first two
cells of the original positive corner have different colors. Hence the
whole infinite strip is proper. For B={0,...,N-1}, with N beyond the column
span,

    U=binom(m,2)N-[(m-3)2^m+m+3],
    U/(Nm) -> (m-1)/2.

Replicating the column set in blocks separated by more than the row span
preserves the ratio. When m divides N, N/m copies give |C'|=|B|=N.
Thus even equal coordinate cardinalities do not rescue a constant bound.
This does not refute S11: the interval row source itself cannot carry the
required proper strict-source coloring. A future cut argument must retain
both child triangles and their shared colors with the cross rectangle.

fibers/CARTESIAN_CUT_LEMMA_0016.md and
fibers/CARTESIAN_THREE_HALVES_0017.md contain useful exact routing identities
but their proposed uniform payment inequalities are refuted by the strip.
Their collision forest sends excess routes to genuine monochromatic
diagonal pairs, while the unbounded congestion is identified in
fibers/PERIODIC_CARTESIAN_DERIVATION_0017.md. In the strip all bichromatic
routes go upward and

    load(y,c_j)=#{i<j:bit_i(y)=bit_j(y)}.

The mean is j/2. Both the monochromatic-pair count and repeated routed load
grow quadratically in the column count per row; unused-cell credit does not.

The Cartesian reflection-switch theorem itself remains valid:
fibers/CARTESIAN_REFLECTION_0016.md forces the inverse corner NAE when
b-h,b,b+h are rows and c,c+h,c+2h are columns. Its count consequence is

    inverse monochromatic corners
      <= U-sum_h p_B(h)p_C(h).

The source note includes counterexamples to deleting either extension.

## 3. Exact cut bookkeeping and additive limitations

CARTESIAN_SOURCE_TRANSFER_0016.md records the exact decomposition for B<C:

    q(h)=#{(u,v) in B x C:v-u=h},
    sum_h q(h)^2=bc+2U,
    V=sum_h (r_B(h)+r_C(h))q(h),
    T(B union C)-T(B)-T(C)=2U+V.

It also derives a generic conditional induction from C(c), with

    E_+(A)<=kappa(c) M(A),
    kappa(c)=3+8c+sqrt(8+48c+64c^2).

That conditional argument is not a new bound: its universal Cartesian
premise is now false, and even c=2 would only give 19+6sqrt(10)>11.

The independent additive transfer candidate

    T(A)<=(1+2Lambda(A))M(A)

is still open. Lambda is the maximum U(B,C)/(bc) over splits of every
contiguous source-index interval. A bounded 100-source diagnosis found no
counterexample, which is not a proof.

fibers/ORDERED_ENERGY_TRANSFER_0016.md derives exact binary interval-tree
bookkeeping. Let E_tree count four-distinct-mark additive quadruples whose
least containing node splits them 1+3 or 3+1, and put

    S_tree=sum_nodes [Lambda |B||C|-U(B,C)].

Then

    T=2Lambda M+2(E_tree-S_tree)+P3.

The exact remaining target is E_tree<=S_tree+(M-P3)/2. The stronger version
that discards S_tree is false for uncolored integer intervals: every tree
captures at most n^3/18 quadruples, and the explicit n=32 calculation
already violates the slack-free bound. This does not close the actual
Lambda transfer or a proper-source-specific tree estimate.

BALANCED_MIXED_CUT_LIMITS_0017.md closes two other shortcuts:

* V<=bc fails on the balanced split of the inherited proper ten-mark source
  {0,1,3,4,6,7,8,10,11,13}: V=28, bc=25.
* V<=bc+U fails without properness even at equal sizes. For
  B={-2i:0<=i<96}, C={3j:1<=j<=96}, V-U-bc=304.

The second example is uncolored and contains long progressions. It leaves
a color-dependent replacement open.

## 4. Discovery provenance and source inputs

All discovery outputs below are terminal. They are construction or conjecture
inputs, not certificates of universal claims, and received no separate
checking pass.

* CARTESIAN_CUT_DISCOVERY_0016.py/json: 30 retained Cartesian candidates,
  at most 100 cells, one SAT call each. The agent disclosed an initial
  over-cap candidate, excluded from retained data.
* ORDERED_ENERGY_TRANSFER_DISCOVERY_0016.py/json: 100 source-only examples,
  exact ratios over contiguous subinterval cuts; no counterexample found.
* CARTESIAN_DENSE_DISCOVERY_0017.py/json: 1000 new candidates above ratio
  3/2, 978 raw UNSAT and 22 raw SAT. One seed has B=0,...,11,
  C={0,2,3,5,7,9}, U/(bc)=59/36. The stronger binary-strip construction,
  rather than a separate array-checking pass, settles the failed constant.
* PERIODIC_CARTESIAN_DISCOVERY_0017.py/json: 79 new finite periodic models,
  producing the binary-bit pattern subsequently derived symbolically.

Wolfram was used for one context query and two new symbolic calculations:
the conditional cut recurrence and the mixed-cut counterfamily's finite
sums. The written derivations contain the algebra; no auditing workflow
was invoked. Mathbox and Deep Research skills were used; the Research
Toolbox router was read, but no irrelevant figure/DSPy runtime was needed.

literature/EDGE_COLORED_SOURCE_INPUTS_0016.md records three primary-source
near-matches: locally additive ordered edge colorings, grid-Ramsey edge
rectangles, and vertex Sidon--Ramsey numbers. None supplies the required
source-span theorem. Do not import their mismatched hypotheses.

## 5. Active work launched for 0018

Root now retains one coloring on all of V(B union C), including V(B), V(C),
the Cartesian cross region, and the corners connecting these pieces.
The standalone rectangle is not an adequate relaxation.

The new source-compatible cut quantities are U and 2U+V above. Bounded
assignments have been activated (inspect live state before waiting):

* cut_fiber_derivation: SOURCE_COMPATIBLE_CLOUD_0018.md, a repeated-support
  cloud inequality that keeps the child-edge colors paying its load.
* product_core_geometry: SOURCE_SEPARATOR_SWITCH_0018.md, a two-quadruple
  switch retaining both child and cross-cell colors.
* source_constraint_map: SOURCE_CUT_PROFILE_DISCOVERY_0018.py/json, new cut
  quantities on at most 100 stored proper-source candidates, with no new
  colorability solve or rechecking of their original colorings.

The root-owned question remains a complete source-size estimate sufficient
for the small-color transfers, not another standalone local obstruction.
