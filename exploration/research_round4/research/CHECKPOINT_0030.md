# Research checkpoint R4-RESEARCH-0030

Continuation of CHECKPOINT_0028.md. The previous turn made substantive
progress through new complete product-class theorems. This continuation
adds a sharp limitation of the unlabeled-overlap relaxation, an explicit
proper source requiring nonconstant colors within distance fibers, and
partial-support identities. The working bounds remain 21<=R3<=465 and
R4<=21991300. S21, D(7/5), and the requested original superior method
remain unproved. The general literature growth bound remains complete.

The goal is active. The user asks for invention, no separate audits or
verification, and no results summary until all objectives are achieved.
All auxiliary tasks and bounded executions named below are terminal.
No reset credit was authorized or used.

## 1. New root limitation: even Golomb overlaps permit unbounded energy

GOLOMB_OVERLAPS_DO_NOT_BOUND_ENERGY_0029.md proves that the property

    G: every nonzero F_d=A intersect (A-d) is itself Golomb

does not imply any absolute total-energy or source-size constant.
This is stronger than separate two-Golomb partitions. A random deletion
construction uses N=q^9, p=q^(-4), q>=5. Positive three-generator cubes
with repeated generators allowed have at most the following parameter
counts: N^4 for eight distinct marks, 6N^3 for six/seven, and 4N^2 for
four/five. The degenerate cases are classified explicitly, not omitted.

The expected size minus cube count is at least

    q^5-q^4-6q^3-4q^2 >= q^5/2.

Deleting one mark per surviving cube gives a set A of that size in
[1,q^9]. If F_d were not Golomb, its repeated positive difference would
create exactly such a cube in A. Thus G holds, while

    M/span >=q/8-1/(4q^4),
    T/M >=q/16-1/(8q^4)-1/2.

In particular M>21 span and T>10M for q>=169, in an asymptotic range
far beyond the finite S21 range. No proper source coloring is claimed.
The completed band-to-size implication also prevents G alone from
implying D(7/5) on every scale.

## 2. Stronger root limitation: concentrate the obstruction in one band

COHERENT_COLORS_ARE_NEEDED_0030.md takes an even-size instance S of the
preceding construction and chooses a balanced partition S=B disjoint
union C, with |B|=|C|=r. A four-distinct equal-difference pair crosses
the partition as two monochromatic edges with probability

    r(r-1)/[2(2r-1)(2r-3)]>=1/8.

The shared-endpoint pairs are the three-term progressions, at most M(S).
Therefore some balanced partition has

    U(B,C)>=[T(S)-M(S)]/8.

Every same-side overlap and every signed cross overlap B intersect
(C-delta) is Golomb; the delta=0 cross overlap is empty. Nevertheless
U/(|B||C|) is unbounded.

Choose a power of two H>2 span(S), set Q=3H/2, and form
A=B union (Q+C). Internal differences are below H and all cross
differences are in [H,2H), so T_H(A)=U(B,C). The projection A->S is
injective and preserves every difference equality because Q>2 span(S).
A cube in A would project to one in S with nonzero signed generators;
reversing the negative generators makes a forbidden positive cube.
Thus the new separated A still satisfies G, and

    T_H(A)/M(A)>=[T(S)/M(S)-1]/8 -> infinity.

This rules out every absolute single-band coefficient under separate
Golomb overlap conditions, even with balanced clusters and all overlaps
on both sides retained. It does not supply compatible source colors,
and it does not refute a properly colored or finite-span target.

The central consequence is sharp in scope: better separate energy
bounds for F_d cannot close a general source theorem on their own.
The actual colors at shared completion cells, or another stronger
finite-span condition, must enter. The full/dense product results of
0028 remain valid through their structural hypotheses.

## 3. A proper cube-free source whose colors cannot depend only on distance

fibers/NONCONSTANT_CUBE_FREE_SOURCE_0030.md gives a complete symbolic
proper coloring of all 28 cells for

    B={0,1,3,4}, C={0,1,4,5}, A=B union (Q+C), Q>20.

All twenty source corners are classified by their same-side and signed
cross fibers. Every F_d is Golomb. The five fibers larger than two are

    F_1={0,3,Q,Q+4}, F_3={0,1,Q+1}, F_4={0,Q,Q+1},
    F_Q={0,1,4}, F_{Q+1}={0,3,4}.

Their distinct internal differences and the full coloring are explicit
in the note; no solver status is a proof premise.

A difference-constant two-color rule is impossible. The B rectangle
forces gamma_1=gamma_3!=gamma_4; the C rectangle forces
gamma_1=gamma_4!=gamma_5. Root integrated this direct contradiction
into the note. Hence a canonicalization of every proper source to
colors depending only on numerical difference is invalid, even in the
cube-free setting. The actual variable colors within fibers matter.

fibers/CUBE_FREE_FORCING_MOTIFS_0030.md separately treats
{0,a,2a,4a,5a}. It is cube-free and has a three-link odd conditional
forcing motif, yet an explicit proper coloring. An odd conditional
cycle alone is not an obstruction. Outputs from different start-pair
gaps in one Golomb fiber have distinct offset diagonals; making two
such outputs parallel would recreate a deleted additive cube.

## 4. Partial supports and two-layer identities

fibers/PARTIAL_THREE_COLUMN_OVERLAPS_0029.md proves the sharp abstract
bound for a partially occupied two-color b-by-three array without a
monochromatic rectangle:

    full rows f<=6, occupied entries<=2b+f<=2b+6.

The six nonconstant binary rows and repeated two-entry bichromatic rows
give sharp constructions. They are abstract arrays, not full-source
colorings. For actual column overlaps S_j=N_{c_j} intersect N_{c_j+delta},
the note retains |intersection of three S_j|<=6 and the exact missing
sets. For q=r_C(delta)>=3, summing all triples gives

    |F_{Q delta}|<=q(2|B|+6)/3,
    total missing overlap incidences>=q(|B|-6)/3.

Missing incidences may be reused across differences; no constant global
budget follows. The root examples in sections 1-2 show that a general
extension using only unlabeled overlap restrictions cannot succeed.

fibers/TWO_LAYER_OVERLAP_ENERGY_0029.md uses script E for T, not for
ordered additive energy. In unambiguous T notation, with
D_delta=B intersect (C-delta), B_h=B intersect (B-h), it proves

    sum_delta binom(|D_delta|,2)=U(B,C),
    sum_delta T(D_delta)=sum_{h>0}U(B_h,C_h),

and

    sum_delta T(D_delta)
      <=sqrt[(T(B)+2sum_h T(B_h))(T(C)+2sum_h T(C_h))].

The last bound is exact when B=C. An upper cap on T(D_delta) transfers
to an upper cap proportional to U, but these identities do not bound
U itself. The new balanced construction has all D_delta Golomb and
unbounded U, closing any inference based solely on these local caps.
Its actual source-color compatibility is still not supplied.

## 5. Bounded discovery and source inputs

fibers/CUBE_FREE_CATALOG_DISCOVERY_0029.py/json reads the 109 stored
minimal-bad window-13 supports once and computes only the new G property.
None satisfies G. This did not run SAT, inspect old colorings, or check
the old catalog labels. The data do not decide general cube-free source
colorability. No solver remains live.

literature/SIDON_OVERLAP_FAMILY_INPUTS_0029.md records a bounded primary
search for a translate-family theorem. One-Sidon-set and global higher-
energy premises do not control independently varying overlap partitions.
literature/GOLOMB_FIBER_CUBE_INPUTS_0030.md distinguishes the present
repeated-generator Hilbert cubes from conventions requiring eight distinct
marks. The examined host-set/cube results and Sidon baseline do not give
the required finite-range theorem. No novelty claim follows from absence
in these focused searches.

## 6. Next central work

Keep the complete and dense-partial product theorems as positive inputs,
but do not spend another turn extending them from separate overlap caps
alone. That universal relaxation is now refuted even for one band.
The required general argument must retain how different fibers force
the same completion color. The exact signed-completion and cloud/Hall
identities remain available, with their previously recorded fan-in gaps.
Constant-per-distance colorings cannot be assumed after the explicit
proper example in section 3.

Cube-free source colorability itself is not settled by the new examples:
the asymptotic construction has no coloring, while the small family is
proper. A bounded new exploration of the nonlocal compatibility may be
useful, but neither observation is a universal theorem. Root retains the
central method and small-color derivations. All three agents are terminal
and may be reactivated for concrete auxiliary tasks. Preserve the full
goal and continue substantive research without a results summary.
