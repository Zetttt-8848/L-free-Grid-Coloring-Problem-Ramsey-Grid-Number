# Reflected triples and competing completion colors

Root derivation, continuing checkpoint 0030 and the new auxiliary path in
`fibers/CUBE_FREE_SOURCE_FORCING_0032.md`. This note derives a shared-color
constraint and an exact separation of its internally supported and open
parts. It does not prove S21, a constant energy bound, or a new Ramsey bound.

Let A be a finite integer source with a proper two-coloring
z:V(A)->{+1,-1}. Write

    F_d={x:x,x+d in A},  F_d^s={x in F_d:z(x+d,x)=s},
    M=binom(|A|,2),     T=sum_d binom(|F_d|,2).

Every F_d^s is Golomb, an inherited consequence of the actual proper
source coloring. Put

    H=sum_(d,s) binom(|F_d^s|,2),
    B=sum_d |F_d^+||F_d^-|=T-H.                         (1)

Here H counts corners with equally colored parallel endpoint cells.
The elementary balancing identity gives T<=2H+M/2. Controlling H still
requires a uniform argument.

## 1. A three-corner color transport

Fix d>0, s in {+1,-1}, and a<b<c in F_d^s. Set

    X_t=(t+d,t) for t=a,b,c,
    P=(b+d,a), Q=(c+d,a), R=(c+d,b),
    w=a+c-b.                                          (2)

All three X cells have color s. Their pairwise source completions P,Q,R
therefore have color -s.

If w belongs to A, the three cells

    P=(b+d,a), Q=(c+d,a), Z=(c+d,w)                    (3)

form a positive corner of step c-b. Thus z(Z)=s. This conclusion uses
only the two completion corners on the pairs {X_a,X_b}, {X_a,X_c},
followed by (3); the completion on {X_b,X_c} is not needed for this
orientation.

If w+d belongs to A, then

    W=(w+d,a), Q=(c+d,a), R=(c+d,b)                    (4)

form a positive corner of step b-a, giving z(W)=s. Here the two seed
completion corners use {X_a,X_c} and {X_b,X_c}.

The target offsets in (3) and (4) are, respectively,

    offset(Z)=d+b-a>d,
    offset(W)=d+c-b>d.                                 (5)

Consequently an equally colored triple on one offset can force its own
color at a larger offset. This supplements the original rule that an
equally colored pair forces the opposite color at its larger-offset
completion. The intermediate cells in (3)-(4) are actual source cells;
no filled triangle or unsupported reflected mark is used.

## 2. An injective charge for reflections whose two marks exist

Call the seed triple internally supported when w lies in F_d, so both
orientations (3)-(4) exist. Since F_d^s is Golomb, w cannot also belong
to F_d^s. Indeed,

    w-a=c-b>0,

would repeat a positive difference in that signed fiber. If w=b, the
two distinct pairs {a,b} and {b,c} already repeat their gap; this case
is excluded by the same Golomb property. Hence

    z(w+d,w)=-s.                                      (6)

The column orientation of an internally supported seed triple maps to
the ordered bichromatic pair of starts

    (w,c) in F_d,                                     (7)

whose upper start has sign s. This map is injective, including the
parameters d and s in its domain. To recover a seed from (7), its gap
is h=c-w=b-a, its sign s is the known sign at c, and the pair {a,b}
is the unique pair of positive difference h in the Golomb set F_d^s.
The start c is already given. Therefore no second seed has this image.

The row orientation similarly maps injectively to

    (a,w) in F_d,                                     (8)

whose lower start has sign s: the unique pair {b,c} in F_d^s of
difference w-a recovers the seed.

Let K be the total number of internally supported seed triples over
all d and s. Equations (7) and (1) give

    K<=B.                                             (9)

The two orientations are not asserted disjoint after charging to
unordered bichromatic pairs. Their safe combined bound is

    number of internally supported oriented transports =2K<=2B.
                                                        (10)

This charge has multiplicity one in each fixed orientation. It differs
from the older fan-pair closure charge, where the unused reflected
source pair leaves a multiplicity 2r_A(h). It does not remove the open
part considered next.

## 3. The exact open part and a scope limit

A column transport is open when w is in A but w+d is absent. A row
transport is open when w+d is in A but w is absent. These are exactly
the remaining supported transports: when both marks are absent there
is no target from this seed. Let O_col and O_row count them, with seed
and orientation multiplicities retained, and put O=O_col+O_row.
The total number J of oriented transports is exactly

    J=2K+O<=2B+O.                                     (11)

In particular, if every entire F_d is Golomb, then K=0: the four starts
a,b,c,w cannot all lie in F_d. In that case every supported reflected
transport is open. This is why internally supported charges alone
cannot settle the cube-free source lead.

The following color-free estimate records the loss if the open part is
counted using only separate signed Golomb fibers. For a column-open
transport fix d,w with w in A and w+d absent. For each choice of c in
F_d above w, its sign s is fixed and the gap h=c-w specifies at most
one pair {a,b} in F_d^s. There are at most r_d choices of c, where
r_d=|F_d|, and |A|-r_d choices of w. Thus

    O_col<=sum_d r_d(|A|-r_d).

For the row orientation fix the mark w+d in A lacking its backward
d-translate, and choose a in F_d below w. The gap w-a and the sign at
a specify at most one pair {b,c} in that signed fiber. Therefore

    O<=2sum_d r_d(|A|-r_d)
      =2[(|A|-1)M-2T].                                (12)

The equality uses sum r_d=M and sum r_d^2=M+2T. This bound usually has
order |A|M and is not the missing linear source budget. Equation (12)
is stated to expose that loss, not as a closure of (11).

## 4. Pair and triple rules compete at the same physical cell

For a cell q, let H_q^s count all equally colored parallel endpoint
pairs of sign s whose unique completion is q. Let J_q^s count all
supported oriented reflected seed triples of sign s whose target is
q, with the multiplicities in Sections 1-3. Properness gives

    H_q^s>0 implies z(q)=-s,
    J_q^s>0 implies z(q)= s.                           (13)

In particular the following products all vanish:

    H_q^+ H_q^-=0,
    J_q^+ J_q^-=0,
    H_q^s J_q^s=0 for s=+1,-1.                        (14)

The last two types couple distinct completion blocks. They are lost
when fibers or reflected targets receive separate color assignments.

Write

    H_q=H_q^++H_q^-,  h_q=H_q^+-H_q^-,
    J_q=J_q^++J_q^-,  j_q=J_q^+-J_q^-.

Equations (13) imply the exact identities

    h_q=-z(q)H_q,  j_q=z(q)J_q,
    h_q j_q=-H_q J_q,
    |j_q-h_q|=J_q+H_q.                                (15)

Also sum_q H_q=H and sum_q J_q=J. Thus (11), (14), and (15) retain both
the multiplicities and the common color of every target. An estimate
that maximizes the signs for H and J independently would discard the
key condition in (14).

One concrete forbidden pattern follows directly: the three seed cells
of a supported reflected transport and the two endpoints of any other
completion at its target cannot all have the same color. If the five
roles occupy distinct cells, this is a five-cell monochromatic-pattern
exclusion derived from four ordinary corners (three for transport and
one at the common target). If roles coincide, the same implication is
understood on the actual set of cells; no distinctness is presumed.

## 5. Quantitative gap

The new rule supplies an exact charge for internal returns and exact
sign incompatibility between open transports and ordinary completions.
To prove a useful general source estimate one still needs either:

* a lower bound on supported transports together with a uniform bound
  on their compatible occupancy of targets in (14); or
* an amortization of the open part O using the actual colors at its
  shared targets, stronger than (12).

No such uniform estimate is established here. In particular (11) is
an upper bound on a transport count, not a lower bound on T, and cannot
be inverted to claim H10 or S21. The abstract counterexample in
`fibers/ORDERED_GROUP_HYPERGRAPH_0031.md` shows that injective output
groups do not automatically resolve color consistency. The actual
integer geometry and conditions (14) remain part of the open argument.
