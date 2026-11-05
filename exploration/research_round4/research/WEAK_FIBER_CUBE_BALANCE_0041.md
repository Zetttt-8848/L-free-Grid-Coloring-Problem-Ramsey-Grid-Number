# An exact cube balance across the weak fibers

Root derivation, continuation0041. The new two-Golomb energy theorem has
a simultaneous consequence for all fibers of a proper strict source.
This note derives that consequence, its exact nonnegative defect, and
its finite-interval localization. It is a universal profile condition,
not a proof of a constant source-energy bound or of S21.

Let A be a finite integer source with a proper two-color V(A). Put
m=|A|, M=binom(m,2), L=span(A),

    F_d=A intersect(A-d), r_d=|F_d|, d>0,
    T(A)=sum_d binom(r_d,2).

Every F_d has its actual proper translated weak triangle, whose two
diagonal classes are Golomb. The theorem in
TWO_GOLOMB_MIXED_ENERGY_0040.md therefore gives

    T(F_d)<=2 binom(r_d,2),
    E(F_d)<=6r_d^2-5r_d.                              (1)

## 1. Positive cubes, including coincident subset sums

For positive integers h_1,...,h_j define

    c_A(h_1,...,h_j)
      =|{x:x+sum_(i in I) h_i belongs to A
             for every I subset{1,...,j}}|.

The generators are ordered. They may be equal, and different subset
sums may coincide. Every listed vertex must be an actual integer mark;
there is no modular or negative-direction replacement in this definition.
Put K_j(A)=sum_(h_1,...,h_j>0)c_A(h_1,...,h_j). Then

    K_1(A)=M,
    K_2(A)=T(A),
    K_3(A)=sum_(d>0) T(F_d).                          (2)

For the second identity, at a fixed first generator d a positive second
generator chooses two distinct starts of F_d. For the third, fixing d
leaves exactly a positive two-generator cube in F_d. These are bijections,
so no generic-distinct-vertex assumption or division by permutations is
needed. Summing (1) proves

    K_3(A)<=2T(A).                                   (3)

## 2. The full signed cube identity

Let C_3(A) count x,h_1,h_2,h_3 in Z such that all eight subset-sum
vertices belong to A, now allowing zero and either sign for each h_i.
For a fixed set of j nonzero coordinates, changing each negative h_i
to its absolute value and shifting x by the sum of the negative h_i
is a bijection to a positive j-generator cube. Each nonzero coordinate
has two signs. Choosing the j coordinates therefore gives

    C_3(A)=m+6M+12T(A)+8K_3(A).                      (4)

The analogous two-coordinate count is the ordinary additive energy

    E(A)=m+4M+4T(A)=2m^2-m+4T(A).

Equations (3)-(4) give the complete signed-moment inequality

    C_3(A)<=m+6M+28T(A)
           =7E(A)-11m^2+5m.                         (5)

This is an identity/inequality for integer cubes, not an appeal to a
finite-field transfer or a Gowers theorem with unspecified constants.

## 3. The exact color-dependent defect

Use the actual diagonal partition F_d=B_d disjoint union C_d, with
b_d=|B_d|, c_d=|C_d|. For these two Golomb sets define the quantities
from the two-class energy decomposition:

    U_d=binom(b_d,2)+binom(c_d,2),
    rho_d=|Delta B_d intersect Delta C_d|,
    N_d=sum_h(beta_(d,h)+gamma_(d,h))(x_(d,h)+y_(d,h)),
    Q_d=sum_h x_(d,h)y_(d,h).

Here beta,gamma indicate within-class lengths h, while x,y count the
two orientations of mixed pairs at that length. The completed theorem
gives

    T(F_d)=2rho_d+N_d+Q_d,
    2rho_d<=U_d, N_d<=2b_dc_d, Q_d<=U_d.

Consequently the following three nonnegative resources give the exact
defect of (1):

    delta_d=(U_d-2rho_d)
              +(2b_dc_d-N_d)
              +(U_d-Q_d)
           =2binom(r_d,2)-T(F_d).                    (6)

The first term counts unequal within-class difference supports, the
second counts missing within-class support at mixed-pair lengths, and
the third is unused distinct-pair-sum capacity in the mixed opposite-
orientation collisions. Their nonnegativity uses the complete two-Golomb
argument, including the cases of repeated marks in pair sums.

Summing (6) over the actual fibers yields

    2T(A)-K_3(A)=sum_d delta_d.                       (7)

This retains the actual colors in the gap between the two moments.
It does not claim that different delta_d resources occupy disjoint
source cells or unused integer lengths. Such a further identification
would need proof.

## 4. Localizing by the total geometric span

For an integer window length t>=1, define

    K_j^(t)(A)
      =sum_(h_1,...,h_j>0)
          (t-h_1-...-h_j)_+ c_A(h_1,...,h_j).

The minimum and maximum vertices of a positive cube are x and
x+h_1+...+h_j. Exactly (t-h_1-...-h_j)_+ integer windows of t
consecutive positions contain them. Therefore

    K_j^(t)(A)=sum_(u in Z) K_j(A intersect[u,u+t-1]).

Each window restriction remains a proper strict source. Applying (3)
inside each window and summing gives

    K_3^(t)(A)<=2K_2^(t)(A).                          (8)

This weights a cube by its whole span, including all three generators.
Weighting each direction independently by an arbitrary function is not
asserted by (8).

## 5. A finite support moment inequality

For any S of size r and span at most ell, let p_s count ordered pairs
of S with sum s. Then sum_s p_s=r^2, at most 2ell+1 sums are available,
and Cauchy--Schwarz gives

    E(S)=sum_s p_s^2 >= r^4/(2ell+1).

Since span(F_d)<=L-d, summing this lower bound and (1) gives

    sum_(1<=d<=L) r_d^4/[2(L-d)+1]
        <=sum_d E(F_d)
        <=6sum_d r_d^2-5sum_d r_d
        =M+12T(A).                                  (9)

All terms and the decreasing available span are explicit. Empty fibers
contribute zero, and the single-position fiber uses denominator one.

Equations (7)-(9) are available finite-span inputs. They do not by
themselves control T/M: the previous constructions with all nonzero
overlaps Golomb already have K_3=0 and satisfy (3), while their normalized
energy can grow with span. In particular these formulas must not be
promoted to a uniform H10 theorem or a finite S21 bound without an
additional argument involving the actual shared colors or finite range.
No unconditional Ramsey number changes in this note.
