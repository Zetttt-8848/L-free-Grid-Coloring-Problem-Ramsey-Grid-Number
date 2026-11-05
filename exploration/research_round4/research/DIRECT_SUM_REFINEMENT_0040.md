# Refined bound for complete direct sums

Root derivation, continuation 0040. The improved two-Golomb energy
estimate gives T<=7M and M<=15L for every properly colored complete
two-factor no-carry source. This improves the earlier H8 and factor17
on that class. The general source and Ramsey objectives remain open.

Let B,C be finite integer sets, with b=|B|>=2 and c=|C|>=2, Q>2span(B),
and

    A=B+QC, n=bc, M=binom(n,2), L=span(A).

Assume V(A) is properly two-colored. The complete derivations in
PROPER_DIRECT_SUM_ENERGY_0028.md supply the following inputs:

1. E(A)=E(B)E(C), by exact coordinate-difference separation.
2. Both factors admit two-Golomb partitions, inherited from actual
   coordinate overlap fibers.
3. If one factor has at least seven marks, every positive difference
   multiplicity of the other is at most two; if it has at least five,
   those multiplicities are at most four. These are the inherited
   complete-rectangle restrictions on the overlap partitions.
4. Every r-mark integer set has T<=binom(r,3) and
   E<=e_r=r(2r^2+1)/3.

We retain all full-product hypotheses of those inputs. The new theorem
TWO_GOLOMB_MIXED_ENERGY_0040.md improves input 2 quantitatively to

    E(B)<=6b^2-5b, E(C)<=6c^2-5c.                   (1)

We will prove E(A)<=16n^2-15n, which is equivalent to T(A)<=7M.
The arguments are symmetric in the factors; label the smaller size b.

## 1. A small-factor consequence of properness

An r-mark set attains T=binom(r,3) only if it is an arithmetic
progression. To derive this, reuse the injection from corners to
increasing index triples in the preceding direct-sum note. Equality
means every index triple is in its image. Write the set as
a_1<...<a_r and put h=a_2-a_1. The triples (1,2,k), k>=3, then force
a_k-h to belong to the set; a_2-h=a_1 already does. Therefore every
mark except a_1 has its predecessor at distance h. Repeated subtraction
must terminate at the only mark without a required predecessor, a_1.
All marks lie in its h-chain and no intermediate point can be missing.
This is exactly an arithmetic progression.

Each factor's strict triangle inherits properness from a layer of A.
A six-mark arithmetic progression is not properly two-colorable, by
the completed six-mark source exclusion in COMPLETION_CUT_BUDGET.md.
Consequently a six-mark factor cannot attain T=binom(6,3)=20, and the
integer count gives

    T<=19, E<=2*6^2-6+4*19=142.                     (2)

This is a deliberately sufficient small-factor bound; no claim of an
optimal six-mark energy is made.

## 2. Both factor sizes at most six

For 2<=r<=5, e_r/r^2=(2r+1/r)/3<=17/5. If b,c<=5, then

    E(A)/n^2<=(17/5)^2=289/25<49/4
                  <=16-15/n,

where n>=4. This proves the desired energy inequality in that case.

If c=6 and b<=5, (2) gives

    E(A)/n^2<=(17/5)(71/18)=1207/90<14.

Here n>=12, so 14<16-15/n. Finally, if b=c=6, the direct estimate is

    E(A)<=142^2=20164<=20196=16*36^2-15*36.          (3)

Thus all small-factor cases are covered without assuming that a raw
finite computation determines their optimum.

## 3. At least one factor has at least seven marks

Suppose c>=7. The inherited multiplicity cap for B gives

    E(B)<=3b^2-2b.                                  (4)

If b>=7 as well, E(A)<=9n^2<16n^2-15n because n>=49.

If b=2, its exact energy is six. Equation (1) yields

    E(A)<=6(6c^2-5c)=9n^2-15n<=16n^2-15n.          (5)

If b is three or four, combining (4) with (1) gives

    E(A)<=(18-12/b)n^2-(15b-10)n
         <=15n^2-35n<16n^2-15n.                    (6)

If b is five or six, the inherited cap r_C(d)<=4 gives
E(C)<=5c^2-4c. Thus

    E(A)<=(15-10/b)n^2-(12b-8)n
         <=(40/3)n^2-52n<16n^2-15n.                (7)

These alternatives exhaust the remaining factor sizes.

## 4. The class conclusion

The energy identity now gives

    4T(A)<=16n^2-15n-(2n^2-n)=14n(n-1),
    T(A)<=7M(A).

Positive-difference Cauchy then gives

    M(A)^2<=L[M(A)+2T(A)]<=15LM(A),
    M(A)<=15span(A).

All estimates concern a complete direct sum with the stated difference
separation. They neither fill holes of a partial product nor prove a
decomposition theorem for arbitrary proper sources. For progression
factors the new PROGRESSION_PRODUCT_REFINEMENT_0040.md is stronger,
with T<=7M/2 and M<=8L. Both are class improvements; the unconditional
R3 and R4 bounds have not changed.
