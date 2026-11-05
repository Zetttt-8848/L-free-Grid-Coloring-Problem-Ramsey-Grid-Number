# A properly colored source with unbounded load at one completion

Root derivation, R4-RESEARCH-0009. This construction distinguishes a global
source-energy bound from a bound on each individual forced cell.

Let C be a finite Golomb set of nonnegative integers containing 0, with
q=|C| and L=max C. Choose an integer s>4L, and put

    A=C union (s-C).

The two parts are disjoint, so |A|=2q. A Golomb set has distinct unordered
sums as well: if x+y=x'+y' with x<=y, x'<=y' and the unordered pairs
are different, then x<x' after swapping pairs. The equality gives the
same positive difference x'-x=y-y', so Golomb uniqueness forces
x=y' and x'=y, contrary to the two orderings and x<x'. This argument
also covers repeated summands.

Every positive difference of A belongs to exactly one of the following
types.

* A positive difference within C occurs once there and once in s-C,
  giving multiplicity two. All such differences are at most L.
* A cross difference is s-(x+y), with x,y in C. It exceeds 2L and
  cannot coincide with a difference of the first type. Unordered-sum
  uniqueness shows that its multiplicity is two if x<y and one if x=y.

Thus every positive difference fiber has at most two cells. There are
2*binom(q,2) fibers of size two and q fibers of size one.

Let Q=(s,0). For each d in A other than 0,s, the two cells

    (d,0),       (s,s-d)

form the entire difference-d fiber, because A is symmetric under x to
s-x and the fiber has multiplicity at most two. Give both cells color 0.
Give Q color 1. The difference of Q is s and has multiplicity one, so
this assignment conflicts with none of the preceding fibers.

On each remaining size-two fiber, give the two cells different colors.
Give color 0 to every remaining singleton. This specifies a total
two-coloring of the strict triangle. A corner can be monochromatic only
if its two diagonal endpoint cells have the same color. The only such
pairs are exactly the selected pairs above, each of color 0, and their
unique completion is Q of color 1. Hence this coloring is proper.

In the notation of SIGNED_COMPLETION.md, the load at Q is exactly

    H_Q=|A|-2=2q-2.                                    (1)

There are no other d in its defining set: its intermediate source marks
are precisely A without its endpoints. All these contributions have
equal-colored endpoints by construction.

Arbitrarily large choices of q are explicit. For example,

    C={2^i-1:0<=i<q}

is Golomb: in equality of positive differences of powers of two, their
two-adic valuations identify the smaller exponent, after which the
larger exponent is also determined. Translation by -1 preserves the
differences. Taking s=4L+1 satisfies the required separation.

The exact total number of corners and cells is

    T(A)=2*binom(q,2)=q(q-1),
    M(A)=binom(2q,2)=q(2q-1).

Therefore T(A)/M(A)=(q-1)/(2q-1)<1/2 for q>=1, while H_Q is
unbounded. In particular, this family is not a counterexample to H(2)
or H(5) in SOURCE_ENERGY_BOTTLENECK.md. It shows why neither conjecture
can be established by bounding the forcing load of every cell by a
fixed constant. Any successful charge argument needs a global estimate.
