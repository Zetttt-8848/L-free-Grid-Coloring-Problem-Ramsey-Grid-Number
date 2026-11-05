# Corner-sum coordinates and a periodic obstruction to restricted-step forcing

Root derivation, R4-RESEARCH-0005. These are auxiliary algebraic results and an explicit uniform construction. They do not improve R3 or R4. The construction shows why unit-step identities and their powers of three cannot, by themselves, settle the local rainbow-forcing problem.

## 1. Zero-sum corners over F3

Identify the three color labels with the field F3. Three labels have sum zero exactly when they are all equal or all distinct. Indeed, an all-equal triple sums to three times its label, and the three distinct labels sum to 0+1+2. A triple with repeated label a and different label b sums to 2a+b=b-a, which is nonzero.

Consequently, in a coloring with no monochromatic corners, zero-sum corners are precisely rainbow corners. Requiring every corner to use exactly two colors is equivalent to requiring every corner sum to lie in {1,-1}. This latter requirement is stronger than ordinary corner-freeness.

Use the triangular coordinates

    S_m={(x,y): x,y>=0, x+y<=m},
    F(x,y)=c(x+y+1,y).

This identifies S_m with T_(m+2). A directed L becomes the unordered triple

    (x,y), (x+d,y), (x,y+d).

Write X and Y for the commuting forward shifts in x and y, and

    D_d=I+X^d+Y^d,       g_d=D_d F.

Thus g_d is defined on S_(m-d). Operator identities below are asserted only at bases where every indicated shifted cell lies in S_m.

## 2. Compatibility between step sizes

Over F3, commuting operators satisfy

    D_(3d)=D_d^3,
    D_e g_d=D_d g_e.                                  (1)

For the first identity, expand (I+X^d+Y^d)^3. Every mixed multinomial coefficient is divisible by three; the surviving terms are I, X^(3d), and Y^(3d). The second identity follows by interchanging the commuting polynomials D_d and D_e.

In particular,

    g_(3d)=D_d^2 g_d.                                 (2)

The second iterate has the explicit form

    D_d^2=I+X^(2d)+Y^(2d)-X^d-Y^d-X^d Y^d.           (3)

If g_d and g_e take only the values 1 and -1, a sum of three entries of either function is zero exactly when those three signs agree. Equation (1) therefore says that the step-e sign corner in g_d is monochromatic exactly when the corresponding step-d sign corner in g_e is monochromatic. These are equalities of actual fields derived from one F; independent sign fields need not satisfy them.

## 3. An exact reconstruction formula

Assume m>=2 and let M=|S_m|=binom(m+2,2). The following data determine F uniquely, and every assignment of these data in F3 occurs:

* F(0,0) and F(1,0);
* all values g_1(x,y) on S_(m-1);
* the values h(x)=g_2(x,0), for 0<=x<=m-2.

There are M-2 displayed corner-sum coordinates. In particular, they are linearly independent.

Proof. The polynomial identity

    (X-I)^2=(Y-X-I)D_1-D_2                            (4)

holds over F3: the right side expands to X^2+X+I, which also equals the left side. Put a_x=F(x,0). Its consequence on the bottom row is

    a_(x+2)+a_(x+1)+a_x
      =g_1(x,1)-g_1(x+1,0)-g_1(x,0)-h(x).            (5)

Given a_0 and a_1, equation (5) successively determines a_2,...,a_m. All terms on its right side are among the prescribed data. Now construct the subsequent rows by

    F(x,y+1)=g_1(x,y)-F(x,y)-F(x+1,y).                (6)

For each successive y, the entire row on the right has already been constructed. This defines every cell of S_m and enforces D_1 F=g_1. Identity (4), together with (5), then enforces D_2 F(x,0)=h(x). Thus the prescribed data are attained. Both recurrences determine their next value uniquely, proving uniqueness. Finally,

    |S_(m-1)|+(m-1)=binom(m+1,2)+m-1=M-2,

as asserted.

Two immediate consequences distinguish what this parametrization does and does not establish.

First, the common kernel of D_1 and D_2 on the full triangle is exactly

    F(x,y)=alpha+beta(x-y),       alpha,beta in F3.    (7)

To prove this, zero corner-sum data in (5) make a_x=a_0+x(a_1-a_0); substituting into (6) gives (7). Conversely, substitution into any D_d gives zero. The reconstruction result also shows that having zero g_1 and just the selected bottom-row g_2 values already implies (7).

Second, the number of functions for which all M-2 selected corner sums are nonzero is exactly

    9*2^(M-2).                                       (8)

The two initial values have nine choices, and each of the independent sums has two choices. More generally, the number having exactly r zero coordinates in this specified basis is exactly

    9*binom(M-2,r)*2^(M-2-r).                         (9)

A zero-sum-free coloring on the entire triangle must belong to the family counted in (8), but other corner sums can still vanish. An ordinary corner-free coloring can have zero coordinates: they are its rainbow corners in the selected basis. Formula (8) must not be advertised as a count of all ordinary corner-free colorings, nor does it show that the remaining constraints are inconsistent.

## 4. The affine freedom changes monochromatic corners into rainbow corners

For beta in F3 put F_beta(x,y)=F(x,y)+beta(x-y). Every corner sum is unchanged by (7). This does not mean that corner-freeness is preserved.

At a zero-sum corner write its ordered labels as (a,a+t,a-t). Under F_beta the parameter t becomes t+beta*d. If 3 does not divide d, exactly one of the three choices of beta makes the corner monochromatic; the other two make it rainbow. If 3 divides d, all three types are unchanged.

For example, if F has no monochromatic corners, let R_non3 be its number of rainbow corners whose steps are not divisible by three. Then

    B(F_1)+B(F_2)=R_non3,                             (10)

where B counts monochromatic corners. Each such rainbow contributes once to the left, whereas a rainbow of step divisible by three contributes nothing. Thus treating all three affine transforms as proper colorings would be an invalid step.

There is also an exact criterion for which lifts of a corner-sum signature are proper. Prescribe the M-2 coordinates from section 3 and reconstruct their canonical lift F_0 by setting F_0(0,0)=F_0(1,0)=0. All nine lifts are

    F_0(x,y)+alpha+beta(x-y).

Consider every zero-sum corner of F_0, including steps outside the selected basis. If one of step divisible by three is monochromatic, none of the nine lifts is proper. Otherwise form the subset H of F3 consisting of

    -[F_0(x+d,y)-F_0(x,y)]/d                         (11)

over all its zero-sum corners with 3 not dividing d. Here d is inverted in F3. The exact number of proper lifts is

    3*(3-|H|).                                       (12)

Indeed, a corner with nonzero sum can never become monochromatic under these lifts. A zero-sum corner of step divisible by three has unchanged type. For every other zero-sum corner, the preceding calculation excludes exactly the beta in (11). A single common beta must avoid their union H; alpha has three unrestricted choices. This proves the formula, including the case H=F3, when no proper lift exists.

This converts the remaining issue into a global exclusion condition on the slopes of zero-sum corners of one reconstructed array. It is not valid to choose a different beta for each corner.

## 5. A uniform quadratic coloring for four step residues

There is a three-coloring of the entire integer plane with neither monochromatic nor rainbow directed Ls at any positive step

    d congruent to 1, 2, 3, or 4 modulo 6.            (13)

In particular, such a coloring exists on arbitrarily large triangles when only steps 1,2,3,4 are imposed. It also avoids zero-sum corners simultaneously at every step 1,3,9,27,... . This is an explicit limitation of restricted-step forcing, not a corner-free coloring for all steps.

Define p to be v modulo 2, q to be u modulo 2, and r to be v+u modulo 3. Regard p and q as the field elements 0 or 1. Set

    c(v,u)=(1+pq)r^2+(q-p)r-p-q-pq    in F3.         (14)

Equivalently, c(v,u)=Q_(p,q)(r), where

| (p,q) | Q_(p,q)(r) |
|---|---|
| (0,0) | r^2 |
| (0,1) | r^2+r-1 |
| (1,0) | r^2-r-1 |
| (1,1) | -r^2 |

The formula has period six in each coordinate. For a directed L based at (v,u), the three arguments r are r,r+d,r+2d.

If d is 2 or 4 modulo 6, the parities do not change and these arguments run through all three field elements. For a quadratic A*r^2+B*r+C their sum is -A: the sums of the constant and linear terms vanish, and 0^2+1^2+(-1)^2=-1 in F3. Each quadratic in the table has A equal to 1 or -1, so this sum is nonzero.

If d is odd, the parity pairs of the three cells are

    (p,q), (1-p,q), (1-p,1-q).

Substituting the four displayed quadratics and adding gives the following corner sums. This table is obtained by polynomial addition in F3; it lists entire polynomials, not a sample of their values.

| base (p,q) | d=1 modulo 6 | d=3 modulo 6 |
|---|---|---|
| (0,0) | r^2+1 | r^2-r-1 |
| (0,1) | r^2-r-1 | r^2+1 |
| (1,0) | -1 | 1 |
| (1,1) | r^2+r-1 | r^2+r-1 |

Each entry is nonzero for every r in F3. For r^2+1, the possibilities are 1 and -1. For r^2-r-1, evaluating at 0,1,-1 gives -1,-1,1; for r^2+r-1 the values are -1,1,-1. The constant entries are also nonzero. This proves (13) by the zero-sum characterization in section 1.

The limits are concrete. At every step divisible by six the three cells have identical residues in (14), hence are monochromatic. Step five can fail too: the cells (6,3),(11,3),(11,8) all have color 2. Thus the construction does not satisfy the full proper-coloring hypothesis in TRIANGLE_RAINBOW_ENERGY.md and does not refute that note's conditional criterion.

## Research consequence

Equations (1)-(6) give an exact way to work with coupled corner sums instead of independent local choices. Formula (12) expresses ordinary corner-freeness as an exact global condition on all the zero-sum corners of a canonical lift. The new construction proves that an argument using only the nonvanishing of D_1,...,D_4, or only the tower D_(3^j), cannot force a contradiction on arbitrarily large triangles. A successful algebraic argument must use additional steps or additional information from the global absence of monochromatic corners.

Unlike the interval-Golomb route, this formulation keeps the actual ternary labels and the compatibility of all corner sums, rather than only bounds on repeated distances. That is a difference in formulation, not evidence of superior bounds or a claim of historical priority. The shift and reconstruction calculations use elementary finite-field algebra. No numerical Ramsey improvement or universal originality claim follows from these auxiliary results.
