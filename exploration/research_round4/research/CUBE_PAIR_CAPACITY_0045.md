# Difference and pair-sum capacities in an injective Boolean cube

This note derives an elementary obstruction for actual weak fibers and
combines it with the separated four-cube construction. It does not give a
source-size inequality or change a Ramsey bound.

## 1. The two pair inventories

Let positive real weights w_1,...,w_d have distinct subset sums. Write

    s(epsilon)=sum_i epsilon_i w_i,   epsilon in {0,1}^d,
    Q={s(epsilon):epsilon in {0,1}^d}.

Only injectivity of s is assumed; no dissociation of differences or sums
is needed. Let B be a Golomb subset of Q: distinct unordered pairs of B
have distinct positive differences. For a nonempty coordinate subset J,
let e_J(B) count unordered pairs of B whose two binary labels differ
exactly in J. Put j=|J|.

**Pair-capacity lemma.**

    e_J(B) <= min(2^(j-1), 2^(d-j)).                 (1)

For the first bound, order the endpoints of a pair temporarily and record
their signed coordinate difference on J. There are 2^j sign vectors,
paired under overall negation. Thus there are 2^(j-1) unoriented signed
types. Every pair of one type has the same absolute numerical difference,
independently of its common bits outside J. Golombness permits at most
one pair of each type. The difference is nonzero by injectivity of s.
If distinct signed types have the same numerical difference, the number
of admissible pairs decreases; this does not weaken the bound.

For the second bound, record the common endpoint bits outside J. There
are 2^(d-j) such records. At every active coordinate the two bits sum to
one; at each inactive coordinate their sum is twice the recorded bit.
Consequently all pairs with one record have the same numerical pair sum.
A Golomb set has at most one unordered distinct-endpoint pair at any
given sum. Indeed, two different pairs at one sum cannot share an
endpoint. If a<b and c<e are two disjoint pairs with a+b=c+e, relabel so
a<c. Then e<b and c-a=b-e>0, a repeated positive difference between
different endpoint pairs. This contradicts Golombness. Again, numerical
coincidences between distinct records can only strengthen the bound.
This proves (1).

Partitioning all pairs of B by J gives

    binom(|B|,2) <= W_d,
    W_d=sum_(j=1)^d binom(d,j) min(2^(j-1),2^(d-j)). (2)

The first inventory is strongest for small active support and the second
for large active support. Keeping their minimum separately for every J
is the substance of (2); replacing either inventory by its total loses
the four-dimensional obstruction below.

## 2. Four-dimensional consequence

For d=4, the contributions of supports of sizes 1,2,3,4 in (2) are

    4*1=4,  6*2=12,  4*2=8,  1*1=1.

Thus W_4=25. Since binom(8,2)=28>25, every Golomb subset of an
injectively represented Boolean four-cube has at most seven marks.
It follows that the union of two Golomb sets occupies at most fourteen
of the sixteen cube marks. This is an upper bound; sharp attainment of
fourteen is not asserted.

Suppose W(S)={(v,u):u,v in S,u<=v} has a proper two-coloring with respect
to the positive equal-step corner {(x,y),(x+h,y),(x+h,y+h)}, h>0.
Its diagonal color classes are Golomb, by the established weak-source
completion lemma. Restriction to any subset preserves properness and
the diagonal classes. Therefore

**Weak-cube obstruction.** A properly two-colored weak source occupies
at most fourteen marks of every injective positive Boolean four-cube.
In particular it cannot contain all sixteen marks.

For comparison, (2) at d=3 gives W_3=3+6+1=10 and only the one-class
bound |B|<=5. The complete proper weak three-cube construction in
fibers/PROPER_WEAK_RESOURCE_CYCLE_CONSTRUCTION_0044.md is consistent
with this inventory. No three-cube exclusion is claimed.

## 3. Transfer through an actual strict-source fiber

Let A be a finite set of real marks whose strict source
V(A)={(v,u):u,v in A,u<v} has a proper two-coloring z. For d>0 put
F_d=A intersect (A-d). Every pair u<=v in F_d gives an actual strict
source cell (d+v,u), since u,v,d+u,d+v belong to A and d+v>u.
The assignment

    w_d(v,u)=z(d+v,u)                              (3)

is a proper weak coloring of W(F_d): translation of the first coordinate
by d preserves each positive equal-step corner and all its cells remain
in V(A). Thus the preceding weak-cube obstruction applies to F_d.

If A contained all thirty-two marks of an injective positive Boolean
five-cube with generators w_1,...,w_5, its fiber F_(w_5) would contain
all sixteen subset sums of the first four generators (with the same
translation as the five-cube). These remain distinct. Formula (3)
would give a proper weak coloring of that four-cube, a contradiction.

**Strict-cube obstruction.** A proper two-colored strict source contains
no injective positive Boolean five-cube.

There is also a useful occupancy version. If Q_4 is a translated
injective four-cube and d>0, then for every proper strict A,

    |Q_4 intersect A intersect (A-d)| <= 14.        (4)

For a five-cube viewed as paired lower and upper four-faces at distance
d, at most fourteen of its sixteen paired starts can have both endpoints
in A. Hence A occupies at most thirty of its thirty-two vertices:
if k pairs are complete, the occupancy is at most 2k+(16-k)=16+k<=30.
This assertion does not require that the two faces be separated in order.

## 4. Scope relative to the new construction

fibers/FOUR_CUBE_NONLINEAR_CONSTRUCTION_0045.md gives fixed lower,
upper, and cross-copy color tables and a complete signed-support proof
of properness for every four-cube satisfying

    w_(i+1)>2 sum_(j<=i) w_j.

Together with Section 3, the largest full cube dimension that admits a
proper strict coloring in this separated family is exactly four.
The old typed four-factor numerical negative used identifications among
distinct cells and is superseded for unrestricted four-cube existence.
Neither that old numerical status nor the new discovery status is a
premise of either paper derivation used here.

The capacity argument is a structural restriction on actual fibers.
Generic cube avoidance alone does not imply S21, H10, or either requested
small-color bound. A further span-sensitive use of (4) would be required.
