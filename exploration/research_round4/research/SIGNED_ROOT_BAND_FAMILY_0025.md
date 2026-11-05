# Signed two-atom sources: band concentration and a coloring obstruction

Root construction analysis, checkpoint 0025. This family is a substantive
stress input for the single-band target. The band counts below are
uncolored quantities. A direct two-color obstruction is proved for at
least seven atoms; the smaller raw negative cases remain separate.

## 1. Integer encoding

Fix r>=3. Put v_i=9^i for 1<=i<=r and S=sum_i v_i. Choose a power of two
H>8S and put D=3H/4, an integer. Define w_i=D+v_i and

    A_r={epsilon w_i+eta w_j:i<j, epsilon,eta in {-1,1}}.

There are m=4 binom(r,2)=2r(r-1) distinct source marks. No relation
sum_i c_i w_i=0 with integers |c_i|<=4 is nontrivial: the small summand
sum c_i v_i has magnitude at most 4S<D, so the coefficient of D must
vanish; then the largest power of nine dominates four times the sum of
all smaller powers. This also ensures that comparing source differences
introduces no unintended equality. All difference counts can therefore
be obtained from signed coordinate vectors.

## 2. Complete nonzero difference types

The following table gives the coefficient type, the number of positive
integer difference values of that type, and the representation count R.
Signs in a type are independent, and all displayed indices are distinct.

| Type | Number of positive values | R |
|---|---:|---:|
| +/-2e_i +/-2e_j | 2 binom(r,2) | 1 |
| +/-2e_i +/-e_j +/-e_k | 4r binom(r-1,2) | 2 |
| +/-e_i +/-e_j +/-e_k +/-e_l | 8 binom(r,4) | 6 |
| +/-2e_i | r | 2(r-1) |
| +/-e_i +/-e_j | r(r-1) | 4(r-2) |

Here a coefficient vector denotes the corresponding combination of
the w_i. To derive the list, compare the two signed two-atom source
vectors. If their supports are disjoint, the four unit coefficients
remain. Choosing which two coordinates belong to the target gives six
representations. If the supports meet at one coordinate, opposite signs
there give the doubled coordinate and the other two unit coordinates;
the latter can be assigned to target and source in two ways. Equal signs
at the common coordinate cancel, leaving two unit coordinates. There
are two ways to assign those coordinates to target versus source, and
2(r-2) choices of the cancelled signed atom for each assignment. Finally,
equal supports give either two doubled coordinates, uniquely represented,
or one doubled coordinate, with 2(r-1) choices of the cancelled signed
atom. Equal source vectors give zero and are omitted. These cases exhaust
all support intersections. Each nonzero coefficient vector has a distinct
negative partner, so taking one positive value halves the sign counts.

Consequently the total corner count is

    T(A_r)=4r binom(r-1,2)+120 binom(r,4)
           +r binom(2r-2,2)
           +r(r-1) binom(4r-8,2).                  (1)

## 3. The concentrated band

Every source difference has total coordinate coefficient in
{-4,-2,0,2,4}. Its small part has magnitude at most 2S<H/4. Hence a
positive difference belongs to [H,2H) exactly when its total coefficient
is two: it then lies in 2D+[-2S,2S], strictly inside the band. Total
coefficient zero stays below H, and total coefficient four lies above 2H.

In the second row of the table, coefficient sum two means the doubled
coordinate is positive and the other two signs are opposite, giving
2r binom(r-1,2) values. In the four-unit row, three signs are positive,
giving 4 binom(r,4) values. The last two rows contribute respectively r
and binom(r,2) values. The first row contributes none with coefficient
sum two. Thus

    T_H=2r binom(r-1,2)+60 binom(r,4)
         +r binom(2r-2,2)
         +binom(r,2) binom(4r-8,2).                 (2)

The leading terms of (1), (2), and M=binom(2r(r-1),2) give

    T/M -> 13/2,       T_H/M -> 13/4.               (3)

For r=5, (2) gives T_H=1160 and M=780, hence T_H/M=58/39>7/5.
This is an uncolored source above the proposed band budget, not a
counterexample to D(7/5). A proper two-coloring would be required.

## 4. A direct obstruction from exchange fibers

Suppose V(A_r) had a proper two-coloring. Fix i<j and consider the
positive exchange d=w_j-w_i. Its start fiber is

    F_d=(w_i+C) union (-w_j+C),
    C={+w_k,-w_k:k distinct from i,j}.

Translation by w_j turns this into

    F=C union (E+C),   E=w_i+w_j.                    (4)

The inherited weak-triangle reduction says that a properly two-colored
strict source gives a properly two-colored translated weak triangle on
F_d. Its two diagonal color classes are Golomb sets. Thus the set F in
(4) would admit a partition into two Golomb classes.

Write k=r-2 for the number of remaining signed axes. For each remaining
atom x=w_l, the four points

    -x, x, E-x, E+x

are distinct. Color the six pairs joining these four points by whether
their two endpoints have the same class color. Every two-coloring of
four points has at least two such monochromatic pairs: the minimum of
binom(a,2)+binom(4-a,2), 0<=a<=4, is two.

Across all k axes, the 6k pairs fall into four families:

* the 2k vertical pairs (-x,E-x) and (x,E+x), all of difference E;
* the 2k cross-antipodal pairs (-x,E+x) and (x,E-x), all of sum E;
* the k bottom antipodal pairs (-x,x), all of sum zero;
* the k top antipodal pairs (E-x,E+x), all of sum 2E.

Each family contains at most one monochromatic pair of each color.
For the first this is positive-difference uniqueness in a Golomb class.
For each other family it is uniqueness of an unordered distinct-pair
sum, equivalent to Golomb difference uniqueness. The pairs in each
family are distinct, as follows from the dissociated coordinates.
Therefore there are at most eight monochromatic pairs in total.
The four-point lower bounds give at least 2k, so

    2k<=8,    hence r<=6.                            (5)

This contradiction proves that V(A_r) has no proper two-coloring for
every r>=7. It uses the actual source-to-weak-fiber reduction and a short
integer counting argument, without a solver premise.

## 5. Bounded discovery scope and open smaller cases

fibers/SIGNED_ROOT_SOURCE_DISCOVERY_0024.py/json records new full-source
colorability calls for r=3,4,5,6. The saved outputs are raw SAT for r=3
and raw UNSAT for r=4,5,6. A preliminary generation pass incorrectly used
only band corners; the agent disclosed that error and replaced the saved
run with the full directed-corner system. No separate coloring check was
run. The raw negative cases are not paper obstruction proofs.

Equation (5) proves only r>=7. A direct argument for r=4 or r=5 remains
a bounded auxiliary question; it is not assumed in a Ramsey theorem.
This family shows why the single-band count cannot be bounded without a
properness or representation hypothesis. It has not refuted D(7/5), and
no working Ramsey upper bound changes.
