# A source-energy bound with controlled missing product marks

Root derivation, continuation 0028. This is a first extension of the
overlap-array argument to a genuinely incomplete product. Its row and
column density assumptions are explicit and are not known for a
general proper source.

## 1. Statement

Let B,C be finite integer sets with b=|B|>=28 and c=|C|>=28, and let
Q>2 span(B). Let

    A subset B+QC.

For z in C and x in B, define the actual neighborhoods

    N_z={x in B:x+Qz in A},
    P_x={z in C:x+Qz in A}.

Assume every column and every row has at most one eighth of its marks
missing:

    |N_z|>=7b/8 for every z in C,
    |P_x|>=7c/8 for every x in B.                    (1)

If V(A) has a proper two-coloring, then

    r_B(h)<=2,  r_C(delta)<=2 for all h,delta>0,       (2)
    T(A)<=5M(A),  M(A)<=11 span(A).                  (3)

The proof uses only cells present in A. It does not extend the coloring
to the missing source marks.

## 2. Three repeated factor differences would supply a forbidden array

Fix delta>0. If r_C(delta)>=3, choose three distinct starts
z_1,z_2,z_3 with z_i,z_i+delta in C. For each i put

    S_i=N_{z_i} intersect N_{z_i+delta}.

By (1), each S_i misses at most b/4 elements of B. Hence

    |S_1 intersect S_2 intersect S_3|>=b-3b/4=b/4>=7. (4)

Choose seven distinct x's in this common intersection. For each chosen
x and each i, both x+Qz_i and x+Q(z_i+delta) belong to A. Thus the
actual overlap F_{Q delta}=A intersect (A-Q delta) contains the complete
7 by 3 no-carry array

    {x+Qz_i:x chosen, 1<=i<=3}.                     (5)

Its inherited translated weak source triangle is properly two-colored.
Its two diagonal color classes are Golomb. A monochromatic rectangle
in (5) would put two different pairs of equal difference into one of
these Golomb classes. Such a rectangle cannot exist.

On the other hand, every two-color 7 by 3 array has a monochromatic
rectangle: choose a same-color pair in each of its seven rows; two
rows share one of the six pair-and-color labels. This contradiction
proves r_C(delta)<=2.

For h>0 with three distinct starts x_i,x_i+h in B, repeat the argument
using P_{x_i} intersect P_{x_i+h}. Each misses at most c/4 elements,
so their common intersection has at least seven elements. The actual
overlap F_h then contains a 3 by 7 array, giving the same contradiction.
This proves r_B(h)<=2 and completes (2). Coincidences between the six
named column or row indices only reduce the missing-set union and do
not affect the seven by three product of distinct starts.

## 3. Energy transfer without filling the coloring

Put n=bc and m=|A|. The neighborhood bound gives m>=7n/8. Because the
coordinate differences are unique,

    E(B+QC)=E(B)E(C).

From (2) and the difference-cap calculation,

    E(B)<=3b^2-2b,   E(C)<=3c^2-2c.

Every ordered energy quadruple of A is also an ordered energy quadruple
of the ambient product, irrespective of whether that product can be
properly colored. Thus energy monotonicity alone gives

    E(A)<=E(B+QC)<=9n^2.                             (6)

The function 12s^2-11s is increasing for s>=1. Since n>=28^2 and
m>=7n/8,

    12m^2-11m-9n^2
      >=12(7n/8)^2-11(7n/8)-9n^2
      =n(3n-154)/16>0.                              (7)

Equations (6)-(7) yield E(A)<=12m^2-11m. Using
E(A)=2m^2-m+4T(A) proves T(A)<=5 binom(m,2). Finally the usual
positive-difference Cauchy step gives M(A)<=11 span(A).

## 4. Scope of the extension

Unlike the full-product theorem, this argument allows missing marks.
The row and column bounds guarantee that three candidate factor
translations still have seven common supported positions. The
forbidden array therefore lies inside an actual overlap, and the
ambient product is used only for its numerical energy upper bound.
There is no assumed coloring of the filled product.

This covers products with up to one eighth of the entries missing in
each row and column, provided both factors have at least 28 marks.
It does not show that every proper source has such a dense product
description. Sparse or highly irregular supports can fail (1), and no
uncontrolled completion or block decomposition is justified. The
general S21 and D(7/5) statements and the small-color objectives remain
open.
