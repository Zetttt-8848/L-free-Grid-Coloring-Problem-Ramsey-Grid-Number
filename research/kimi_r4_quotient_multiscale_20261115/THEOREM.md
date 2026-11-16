# Quotient-color statements and contiguous-block averaging

## 1. Definitions

Let a proper four-coloring of `[n]^2` avoid every monochromatic forward L
`L(x,y;d)={(x,y),(x+d,y),(x+d,y+d)}` with integer `d>0`. There are seven
nontrivial bipartitions `P` of the four-color palette, up to interchanging the
two sides. For each `P`, identify colors within each side and call the resulting
binary coloring the quotient coloring.

A geometric L is **pair-tight for P** if all three original colors lie in one
side of P. This is equivalent to that L being monochromatic in the quotient.
Its signature `S(L)` is the set of all seven bipartitions for which it is
pair-tight.

## 2. Three-L cover lower bound

**Proposition Q1 (PROVED with external input R_2=5).** Every proper
four-coloring of a full contiguous 5 by 5 square contains a collection of
pair-tight Ls whose signatures cover all seven bipartitions. At least three
distinct Ls are necessary for such a cover.

**Proof.** Apply `R_2=5` to each of the seven quotient colorings. It supplies a
pair-tight L for every bipartition, so some collection covers all signatures.
Since the original coloring is proper, no L uses exactly one original color.
If an L uses exactly two original colors `{a,b}`, it is pair-tight precisely
when `a` and `b` lie on the same side. Fixing `{a,b}` as one side, the other two
colors give exactly three nontrivial complementary choices: `{c}`, `{d}`, or
`{c,d}`. Thus its signature has size three. If the L uses exactly three colors,
only the bipartition with those three colors against the fourth is pair-tight,
so the signature has size one. If it uses four colors, its signature is empty.
Hence every L covers at most three of seven required signatures, and fewer than
three Ls cannot suffice. QED.

This is a covering lower bound, not a claim that exactly three Ls always cover.

## 3. Counterexample to universal three-L sufficiency

**Statement Q2 (REFUTED).** It is not true that every proper four-coloring of a
5 by 5 square has three Ls whose signatures cover all seven bipartitions.

The zero-based row matrix of the checked witness is

```text
1 3 1 2 3
1 3 2 3 0
3 3 0 1 2
3 2 3 3 1
0 3 3 2 2
```

`verify_results.py` independently enumerates all 30 geometric Ls, checks that
none is monochromatic, and enumerates every subset of size 0, 1, 2, and 3. No
such subset covers all seven signatures. Thus this is a COUNTEREXAMPLE to Q2,
not merely an unsuccessful random search.

## 4. Invalid combinatorial-subselection mechanism

The initially considered application of `R_2=5` to every selection of five
arbitrary rows and five arbitrary columns is invalid. Rank-space equality of
row and column steps does not imply equality of their original integer
distances. Such a selection does not in general preserve the directed equal-leg
L family. No averaging bound over arbitrary combinatorial subsquares is claimed.
This is a failure of that mechanism, not a counterexample to R_2=5.

## 5. Contiguous-block weighted count

Let `P_d` be the number of pair-tight Ls of step `d` in a proper four-coloring
of `[n]^2`, `n>=5`, and consider only contiguous 5 by 5 blocks.

**Proposition Q3a (PROVED with external input R_2=5).**

```text
sum_(d=1)^4 P_d/(5-d)^2 >= 3(n-4)^2.
```

In particular, the unweighted number `P=sum_d P_d` satisfies
`P>=3(n-4)^2`.

**Proof.** By Q1, every contiguous 5-block contains at least three distinct
pair-tight Ls. There are `(n-4)^2` such blocks. A fixed L of step `d<=4` lies in
exactly `(5-d)^2` contiguous 5-blocks: independently choose the block's row and
column origins among `5-d` possibilities. Divide by these exact multiplicities
and sum. The unweighted consequence follows from `1/(5-d)^2<=1`. QED.

The total number of geometric Ls in the full square is

```text
N_n=sum_(d=1)^(n-1)(n-d)^2=n(n-1)(2n-1)/6.
```

Consequently `P/N_n>=18(n-4)^2/(n(n-1)(2n-1))`, whose asymptotic is `9/n`.
This is only a lower bound on pair-tight incidence. No matching upper bound or
contradiction with the incumbent capacity certificate has been established.

## 6. Status and scope

- Q1: PROVED with external input `R_2=5`; author proof and independent finite
  implementation checks.
- Q2: REFUTED by the explicit complete witness above; independently checked.
- Arbitrary combinatorial-subselection averaging: REFUTED as a mechanism by the
  geometric argument in Section 4.
- Q3a: PROVED with the same external input; incidence arithmetic independently
  checked for the stored side list, with direct small-side enumeration.
- A new numerical bound on R_4: not established.
- The exact maximum or universal minimum quotient-cover size beyond the Q1
  lower bound: UNDECIDED.
