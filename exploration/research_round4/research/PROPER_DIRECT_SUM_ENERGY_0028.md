# Energy of complete direct sums with a proper source coloring

Continuation 0040: DIRECT_SUM_REFINEMENT_0040.md reuses the exact
factorization and complete-overlap restrictions below with the stronger
two-Golomb input from TWO_GOLOMB_MIXED_ENERGY_0040.md. It proves
T(A)<=7M(A) and M(A)<=15span(A) on the same complete class. The
historical H8/factor17 proof remains valid but is superseded there.

Root derivation, continuation 0028. This extends the proper-product
argument from progression factors to arbitrary complete factors. The
uniform source theorem remains open; the theorem here has an explicit
direct-sum hypothesis.

## 1. Statement and inherited overlap condition

Let B,C be finite integer sets with b=|B|>=2 and c=|C|>=2. Let
Q>2 span(B), and put

    A=B+QC,    m=bc,    M=binom(m,2).

The no-carry hypothesis gives unique representations, unique coordinate
differences, and the exact ordered-energy factorization

    E(A)=E(B)E(C).                                  (1)

Suppose V(A) is properly two-colored. The theorem to be proved is

    T(A)<=8M,    M<=17 span(A).                     (2)

For every positive difference d of A, the translated weak triangle on
F_d=A intersect (A-d) is properly two-colored by the source coloring.
Its two diagonal color classes are Golomb. Thus every F_d is a union
of two Golomb sets. This is the established weak-source diagonal lemma.

For h>0 and delta>0, coordinate uniqueness gives the specific fibers

    F_h=(B intersect (B-h))+QC             (h in Diff^+(B)),
    F_{Q delta}=B+Q(C intersect (C-delta)) (delta in Diff^+(C)).  (3)

In particular, by taking one nonempty coordinate fiber in each line
of (3), both B and C themselves admit two-Golomb partitions. The
partitions need not be the same for different chosen fibers; only
their existence is used in the following energy bounds.

PROPER_PROGRESSION_PRODUCT_ENERGY_0027.md, section 1, gives

    E(S)<=8|S|(|S|-1)                               (4)

for any union S of two Golomb sets of size at least two. Its full
derivation is not repeated here.

## 2. Rectangles inside a two-Golomb partition

Suppose a no-carry product U+QV is a union of two Golomb sets. Color
the corresponding |U| by |V| array by that partition. A monochromatic
axis-parallel rectangle is impossible: its four marks include two
distinct pairs with the same nonzero difference. They would lie in
one Golomb part.

Two elementary finite array facts will be used.

**Fact A.** Every two-color 7 by 3 array has a monochromatic rectangle.
Each of the seven rows contains a same-color pair among its three
positions. Choose one such pair. There are only six labels consisting
of a position pair and its color. Two rows receive the same label,
giving the required rectangle. The transposed assertion also holds.

**Fact B.** Every two-color 5 by 5 array has a monochromatic rectangle.
If no such rectangle exists, a pair of rows can share a given color
in at most one column. The total number of columnwise same-color row
pairs is consequently at most 2 binom(5,2)=20. A column with r red
entries contributes

    binom(r,2)+binom(5-r,2)>=4,

with equality only for r=2 or 3. All five columns must attain equality,
and each of the two colors must use all ten available row pairs.
If k columns have three red entries, the red-pair total is 5+2k.
It cannot equal ten for integral k, a contradiction.

Apply these facts to the products in (3). They give

    b>=7 => r_C(delta)<=2 for every delta>0,
    b>=3 => r_C(delta)<=6 for every delta>0,
    b>=5 => r_C(delta)<=4 for every delta>0,           (5)

and the corresponding statements with B and C exchanged. The first
line uses a 7 by 3 subarray; the second uses a 3 by 7 subarray; the
third uses a 5 by 5 subarray. These are constraints on actual overlaps,
not assumptions that an arbitrary two-color array is a source coloring.

For any finite set S of n marks with r_S(d)<=k at all positive d,

    E(S)=n^2+2 sum_{d>0} r_S(d)^2
         <=n^2+2k binom(n,2)
         =(k+1)n^2-kn.                              (6)

## 3. An elementary energy bound for a small factor

For completeness, every ordered n-mark integer set S satisfies

    T(S)<=binom(n,3),
    E(S)<=e_n:=n(2n^2+1)/3.                         (7)

Here is a direct injection proving the first inequality. Write the
marks as a_1<...<a_n. A collision of positive difference d has two
starts a_i<a_j and endpoint a_k=a_j+d. Associate to it the index
triple (i,j,k), with i<j<k. The triple determines d=a_k-a_j and then
the other endpoint a_i+d, so it determines the original collision.
The associated triple is therefore injective into the binom(n,3)
increasing triples. Equation (1) of the preceding energy note gives
the second bound in (7).

For integers 2<=n<=6, e_n/n^2=(2n+1/n)/3 is increasing in n, and

    e_n/n^2<=73/18,
    (73/18)^2=5329/324<17.                           (8)

## 4. The energy estimate for all factor sizes

We prove the equivalent form of the first claim in (2),

    E(A)<=18m^2-17m.                                (9)

The estimates in (1), (3)-(6) are symmetric in the two factors, even
though the original integer notation writes only one as the scaled
factor. We may consequently label the smaller size b, so b<=c.

### Both factors have size at most six

By (1), (7), and (8), E(A)<17m^2. If m>=17, this is at most the
right side of (9). If m<=16, the following three possibilities exhaust
b<=c<=6: b=2; b=3 with c<=5; or b=c=4. In these cases (7) gives
respectively

    E(A)/m^2 <= (3/2)(73/18)=73/12<8,
    E(A)/m^2 <= (19/9)(17/5)=323/45<8,
    E(A)/m^2 <= (11/4)^2=121/16<8.

Thus E(A)<8m^2 in the small-m case. Since m>=4,
18m^2-17m-8m^2=m(10m-17)>0, proving (9) in all these cases.

### At least one factor has size at least seven

Now c>=7. The exchanged first line of (5) gives r_B(h)<=2, hence

    E(B)<=3b^2-2b.                                 (10)

If b>=7, the same bound holds for C. Therefore E(A)<=9m^2, which
is below (9) because m>=49.

If b=2, its exact energy is six. Bound (4) for C gives

    E(A)<=6(8c^2-8c)=12m^2-24m,

again below (9).

If b is three or four, the second line of (5) and (6) give
E(C)<=7c^2-6c. Together with (10), this yields

    E(A)<=(21-14/b)m^2-(18b-12)m
         <=(35/2)m^2-42m
         <=18m^2-17m.                               (11)

Finally, if b is five or six, the third line of (5) gives
E(C)<=5c^2-4c. Hence

    E(A)<=(15-10/b)m^2-(12b-8)m
         <=(40/3)m^2-52m
         <=18m^2-17m.                               (12)

These alternatives exhaust all factor sizes and prove (9). Since
E(A)=2m^2-m+4T(A), inequality (9) is exactly T(A)<=8M. Finally
sum_d r_A(d)^2=M+2T<=17M and positive-difference Cauchy give
M<=17 span(A), as claimed in (2).

## 5. What is new in this implication and what remains open

The additive energy factorization by itself allows the two factors to
amplify each other. Actual properness prevents unrestricted amplification:
every coordinate overlap must be partitionable into two Golomb sets.
The small monochromatic-rectangle arguments turn that shared-color
condition into explicit difference-multiplicity caps on the factors.
Both caps and the two-Golomb energy estimate are then used in the same
calculation.

This proves a source-size estimate stronger than S21 for every complete
two-factor no-carry direct sum. The separate progression-product theorem
has the better constant 11 when one full factor is an arithmetic
progression. Neither theorem covers arbitrary subsets of a product:
the arrays in section 2 must be present in full, and filling holes can
make an originally proper source uncolorable.

The remaining central implication is a decomposition or quantitative
argument that controls general properly colored sources, including
incomplete Cartesian supports, without losing the constant budget.
No unconditional R3 or R4 improvement, universal product representation,
or superiority claim completing the research objective follows here.
