# Research checkpoint R4-RESEARCH-0036

Continuation of CHECKPOINT_0033.md. New work 0034-0036 includes a
proper-source energy theorem with a translation matching, an explicit
proper weak family refuting a mixed-difference loss budget, a finite
counterexample to a proposed weak-span inequality, and additional
shared-reflection constraints. The full goal remains active and
incomplete. The working bounds remain 21<=R3<=465 and R4<=21991300.
S21, D(7/5), the general H10 assertion, and the requested original
superior method are still open. The attributed general growth bound
is complete and unchanged.

The preceding continuation made progress by changing the mathematical
state through new complete class derivations and counterexamples.
No external blocker remains. Three concurrent file readers briefly
failed from a local memory error; their reported handles were polled
to terminal status. A subsequent single PowerShell reader with login
disabled succeeded. Prefer one lightweight shell process at a time
if the memory problem recurs; do not restart solver work because of a
file-reader failure. All research computations and agents listed here
are terminal, and no reset credit was used.

The user requests invention, full derivations, no separate audits or
repeated checking, and no results summary until the complete objective
is achieved. These instructions remain active.

## 1. Root: energy with a perfect translation matching

PAIRED_SOURCE_ENERGY_0036.md proves:

    If V(A) is properly two-colored and
    A=S disjoint union (S+d), d>0,
    then T(A)<=10M(A) and M(A)<=21 span(A).

Unlike the earlier no-carry product theorem, this permits arbitrary
collisions between numerical differences shifted by d and 2d.
The actual colors of the matched cells (x+d,x) partition S into two
Golomb sets B,C; S need only be a subset of F_d, not all of it.

For a Golomb B of size b with B intersect (B+d) empty, define
C_h(B)=sum_t r_B(t)r_B(t+h). The complete derivation gives

    E(B)=2b^2-b,
    C_d(B)<=b^2-b,
    C_(2d)(B)<=b^2+b-2,
    E(B union (B+d))
       =6E(B)+8C_d(B)+2C_(2d)(B)
       <=22b^2-12b-4.

For the last correlation bound, when h is represented, remove the
two terms t=0,-h and also the maximal signed difference from the
remaining overlap count; the singleton case is included explicitly.

The L4 energy triangle inequality combines the two actual Golomb
matching classes. Concavity of

    (22t^2-12t-4)^(1/4), t>=1,

follows from the exact second-derivative numerator

    -1936(t-3/11)^2-992.

When both classes are nonempty, with m=|A|, the resulting bound is

    E(A)<=22m^2-48m-64.

The one-class case is separately bounded, and in all cases
E(A)<=22m^2-21m, equivalent to T<=10M. The ordinary difference
Cauchy inequality then gives M<=21 span.

The matching hypothesis is exact: for a fixed d, the graph of source
marks joined at distance d is a union of paths, and it has a perfect
matching exactly when every component has even size. In particular
the theorem covers every source whose consecutive runs all have even
length. No such matching is known for a general source.

**Scope comparison retained in the note:** the source-size conclusion
on this class was already accessible from a simpler separate signed
Golomb count. With L=span(A)>=1, that count gives

    M(A)<=16L-13+3sqrt(8L-7)<18L.

Thus the new theorem's contribution is an energy estimate allowing
arbitrary shifted-difference collisions, not a stronger cardinality
estimate on already perfectly matched sources. It must not be sold as
an unconditional small-color improvement. Extending it to arbitrary
unmatched marks without an uncontrolled sum cost remains open.

## 2. Root: proper weak colorings with quadratic mixed-difference loss

WEAK_TWO_COPY_COLORINGS_0036.md takes a Golomb P={p_i} of size q and
Q>2 span(P), with a harmless translation making min P=0. On
S=P union (Q+P), assign arbitrary lower diagonal bits e_i and opposite
upper diagonal bits. Both diagonal color classes B,C have q marks.

For i<j the complete rule is

    z(p_j,p_i)=1-e_j,
    z(Q+p_j,Q+p_i)=e_j,
    z(Q+p_i,p_i)=e_i,
    z(Q+p_j,p_i)=1-e_i,
    z(Q+p_i,p_j)=e_i.

Diagonal-pair corners have opposite-colored completions whenever
their endpoint colors agree. Every strict corner is either the pair
of internal equal differences or a pair in F_Q=P; the displayed
rule makes a specified two cells in each such corner opposite.
This is a full direct proof of proper weak colorability, for arbitrary
choices of all q bits.

If p of the bits are one and Delta_mix is the set of distinct
positive absolute differences between B and C, the exact count is

    q^2-|Delta_mix|=q-1+p(q-p).

Balanced bits therefore give a quadratic loss. No linear bound on
this loss in |B|+|C| is valid even under actual proper weak coloring.
The construction has large separated span and does not refute a
finite-span cap or a tradeoff that retains unused lengths. This
closes the attempted direct payment in which nearly all mixed
absolute differences were to be distinct up to O(|B|+|C|) errors.

## 3. A finite weak-span candidate is false, with a direct construction

The new candidate L>=(b-1)(c-1) for a proper weak source with diagonal
classes of sizes b,c was investigated because a suitable version near
b=c=23 would help the inherited R3 cap route. It is false as stated.

fibers/WEAK_PRODUCT_SPAN_DISCOVERY_0035.py/json made new joint-source
calls for balanced r=4,5,6 at L=(r-1)^2-1, each with a three-second
cap. The first two returned raw UNSAT; the third returned raw SAT in
about 1.54 seconds. The r=7 call was not made after this discovery.
The JSON stores all 78 weak-cell colors, without an independent
checking pass. The negative small cases are not paper claims.

fibers/WEAK_SOURCE_PRODUCT_SPAN_0035.md converts the positive lead into
an explicit mathematical construction:

    P={0,4,7,12,21,23},
    S=P union (P+1), B=P, C=P+1.

It gives six internal-block colors and four Boolean rules for all
two-by-two blocks, followed by a complete classification of equal-
colored endpoint groups and their opposite completions. Thus W(S)
is properly colored with b=c=6 and span 24<25. The raw SAT verdict is
not a premise of that proof.

The same note records the exact identity, with
R=|Delta B intersect Delta C| and U=L-|Delta B union Delta C|,

    L-(b-1)(c-1)
      =U+[(b-c)^2+b+c-2]/2-R.

For the explicit source R=15,U=9 and the allowance is 5, so the
proposed payment fails by one. The weaker expression bc-b-c happens
to equal its span; no corrected universal inequality is asserted.
The product-span conclusion remains valid for shallow hull overlap
omega<=[(b-c)^2+b+c-2]/2, or sufficiently unbalanced class sizes
(b>=2c-2 or the symmetric case), by the complete elementary arguments
in the note. These special cases do not cover the finite-cap target.

## 4. Additional shared-reflection constraints

fibers/OPEN_REFLECTION_COLLISIONS_0034.md fixes q=(v,u), s=z(q).
At a lower offset d, at most one column-open seed and at most one
row-open seed can target q, by signed Golombness. Such an open
transport excludes an ordinary completion pair at the same offset.
Two column-open transports and one monochromatic ordinary fan pair
inject, for fixed q, into a row-v triple of colors s,s,-s. The row-
open analogue injects into a column-u triple. Consequently

    binom(|C_q|,2) H_q<=binom(N_v^s,2) N_v^(-s),
    binom(|R_q|,2) H_q<=binom(N_u^s,2) N_u^(-s).

The same physical line triple can be reused at different targets,
and mixed orientations lie on different lines. No global injection
or linear source budget follows from these targetwise statements.

fibers/REFLECTION_SEED_COUPLING_0034.md derives further exact relations
in the earlier 26-mark cube-free lead. Four seed triples with offsets
29,59,67,76 share intermediates P=(91,0),Q=(96,0) and target Z=(96,5).
Any two of those seed triples that are monochromatic must have the
same color. Another reflected triple at offset 27 crosses the offset-
27 and offset-64 fan blocks at Z. When combined with a monochromatic
offset-76 seed, it forces the two offset-64 endpoints to be opposite.
This shortest composition satisfies the fan instead of producing
the proposed contradiction. It does not force any seed monochromatic.
The full 26-mark source still has no paper noncolorability proof.

## 5. Exact finite R3 cap input preserved

fibers/R3_FINITE_CAP_INPUTS_0034.md now distinguishes the strict
two-color V(A) obtained from a monochromatic grid diagonal from the
translated weak W(F_d) supplied by one fiber. Its finite open profile
for |A|=155 in positions 0,...,463 is

    r_A(d)<=46 for 1<=d<=27,
    r_A(d)<=45 for d=1,2,3.

Root located its complete existing conditional transfer in
research_round3/round3_report.tex beginning at line 403. The recorded
lower and upper sums are 25110 and 25091, respectively, implying
R3<=464 conditional on the new cap profile and inherited spacing.
These figures were reused without recomputation. The different
conditional_descent.json profile uses 45 throughout d<=27 and is not
the citation for this mixed profile. The inherited H_j position minima
and window-13 spacing remain inputs, not new results.

## 6. Next central work

The paired-source theorem allows overlapping difference ranges but
does not remove the perfect-matching restriction; its cardinality
corollary alone does not advance the general S21 target. The explicit
weak-span and mixed-difference counterexamples show why the obvious
short cardinality payments fail. Do not assume bc-b-c is universally
valid merely because one example attains it.

The root still owns the main finite-span inequality and the R4
breakthrough. The shared completion profile, reflected transport,
and open fan identities remain exact inputs with their stated global
reuse gaps. A finite R3 cap route can run alongside the root effort,
but the new twelve-mark counterexample must be retained before
proposing another joint-ruler span formula. All child agents and
bounded computations are terminal and available for fresh, bounded
subtasks. Preserve the full objective and continue without a results
summary or a completion claim.
