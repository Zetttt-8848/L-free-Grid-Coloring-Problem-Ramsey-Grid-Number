# A proper three-cube with no shared signed-fiber differences

Root construction, continuation0044. A bounded auxiliary discovery on
the weights 1,4,16 suggested a symmetric rule. The rule below is derived
for arbitrary two-dissociated positive weights; the SAT status is not a
premise. It shows why the interlaced shared-pair mechanism must have a
separate branch for sources without its shared-difference resources.

Let w_1,w_2,w_3 be positive integers such that

    sum_i k_i w_i=0, k_i in {-2,-1,0,1,2}
       implies k_1=k_2=k_3=0.                       (1)

For X subset {1,2,3}, put a_X=sum_(i in X)w_i and
A={a_X:X subset {1,2,3}}. The eight marks are distinct. Identify each
strict cell with its unordered pair of distinct endpoint subsets; its
actual row is always the larger integer endpoint.

## 1. The coloring

Give a cell color 1 exactly when its endpoint pair is one of

    {empty,{i}},
    {{i},{1,2,3}},
    {{i},{1,2,3}\{i}},           i=1,2,3.           (2)

Give every other strict cell color 0. This is a full coloring of all
28 cells, symmetric in the three coordinate names. Its definition is
independent of which endpoint subset represents the larger integer.

The bounded numerical discovery had color 0 on one of the three
complementary singleton/doubleton cells. The new symmetric rule gives
all three of those cells color 1. The proof below treats the resulting
rule directly, rather than replaying the numerical assignment.

## 2. Classification of every positive corner

Any positive corner has four source marks

    x, x+d, x+h, x+d+h,           d,h>0,             (3)

and its cells are

    (x+d,x), (x+d+h,x), (x+d+h,x+h).

The equality between the two translated differences in (3), together
with (1), is coordinatewise equality between their Boolean difference
vectors. Each coordinate is therefore either constant or changes
along exactly one of the two generators d,h. It cannot change along
both: the single-generator vertices and the double-generator vertex
would then require three Boolean values in that coordinate. Both
generator supports are nonempty and disjoint.

Thus their combined support has size two or three. We list the two
positive corners of each rectangle. Interchanging the two positive
generators interchanges those two corners, so the middle numerical
order requires no extra case.

If the total support has size two, each generator changes one
coordinate. Positivity of the weights makes both changes 0 to 1.
The third coordinate is fixed.

* If it is fixed at 0, the rectangle's endpoint subsets are empty,
  two singletons, and their doubleton. In each corner the first cell
  has color 1, the completion cell has color 0, and the last cell
  is a contained singleton/doubleton pair of color 0. Both corner
  patterns are (1,0,0).
* If it is fixed at 1, the rectangle's subsets are one singleton,
  two doubletons containing it, and the full set. Both corners have
  pattern (0,1,0).

If the total support has size three, call the one-coordinate
generator i and the other two coordinates j,k. The i change is again
0 to 1. There are two possibilities for the positive two-coordinate
generator.

* For two positive coordinate changes, the rectangle consists of
  empty, {i}, {j,k}, and the full set. The i-generator corner has
  pattern (1,0,0); the other corner has pattern (0,0,1).
* For one positive and one negative change, rename j,k so the
  change is {j} to {k}, with w_k>w_j. The rectangle is
  {j}, {i,j}, {k}, {i,k}. Its completion cell joins the complementary
  singleton {j} to doubleton {i,k}, so has color 1. The other cells
  are contained singleton/doubleton pairs, two singletons, or two
  doubletons, all of color 0. Both patterns are (0,1,0).

Two negative coordinate changes cannot have positive total weight.
The cases exhaust (3), and every listed corner uses both colors.
Therefore (2) is a proper two-coloring of V(A) under (1).

## 3. Every actual signed-fiber overlap is unshared

For a positive difference d, its unique Boolean difference vector has
some support size j in {1,2,3}. Its nonzero coordinates fix the lower
endpoint bits, while the other coordinates are free. Hence

    |F_d|=2^(3-j).                                   (4)

Distinct signed difference vectors cannot have the same numerical
value by (1). Up to negation, their numbers at support size j are

    binom(3,j) 2^(j-1).                              (5)

If j>=2, the fiber has at most two starts. Its two actual diagonal
color classes therefore cannot both contain a pair, and their
positive difference sets have empty intersection.

If j=1, positivity gives d=w_i. The four parallel edge cells have
color 1 only at the edge from empty to {i}; the other three colors
are 0 by (2). One diagonal fiber class is a singleton. Again the
two signed classes have no shared positive difference.

Thus, for the actual coloring (2),

    rho_d=|Delta F_d^0 intersect Delta F_d^1|=0
       for every d>0.                               (6)

In particular every interlaced-pair and reflected-middle seed count
from INTERLACED_SHARED_PAIR_COMPLETION_0044.md vanishes.

This does NOT say F_d itself is Golomb. Each primitive-direction
fiber is a four-point rectangle and has two repeated differences.
The absence in (6) concerns differences shared between its two
actual diagonal color classes.

## 4. Nonzero cube count and the scope of the example

Equations (4)-(5) give the complete size profile:

    three fibers of size 4,
    six fibers of size 2,
    four fibers of size 1.

Consequently

    M=3*4+6*2+4*1=28,
    T(A)=3*binom(4,2)+6*binom(2,2)=24.               (7)

Each size-four fiber is a two-generator rectangle; it has exactly
two positive ordered two-generator cubes. All other fibers have
size at most two and have none. Therefore

    K_3(A)=sum_d T(F_d)=3*2=6.                      (8)

So rho_d=0 for every d does not imply positive three-cube avoidance,
even for an actually proper strict source. This strengthens the
distinction between missing shared-color resources and missing
uncolored cube configurations.

The example has T/M=6/7. It is not a counterexample to H10, S21,
or any requested small-color bound. Nor is it a full-grid coloring.
Its contribution is the explicit parameterized construction and
the exact limitation (6)-(8): a complete argument based on activated
shared differences must also control proper sources for which
those resources all vanish.
