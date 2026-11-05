# Constant-weight sources and the necessary energy scale

Root derivation, continuing R4-RESEARCH-0009. This is a construction
theorem and a lower constraint on a proposed energy inequality, not an
upper bound for a Ramsey number.

## 1. Construction and full corner argument

Fix integers k>=1 and r>=2k. Put w_i=5^i for 1<=i<=r, and write
W(X)=sum_(i in X) w_i. Let

    A_(r,k)={W(X): X subset [r], |X|=k}.

Equality of two differences of such sums forces equality of their
signed coordinate vectors. Indeed, subtraction gives sum c_i 5^i=0
with |c_i|<=2. If j is the largest nonzero coordinate, its absolute
contribution is at least 5^j, strictly greater than
2 sum_(i<j)5^i. This is impossible. The same argument makes W
injective, so m=|A_(r,k)|=binom(r,k).

Color a cell (W(Y),W(X)) with W(X)<W(Y) by

    chi(W(Y),W(X))=|X intersect Y| in {0,...,k-1}.       (1)

We prove that this is a proper k-coloring of the strict source
triangle. Fix a positive difference d. Every representation
W(Y)-W(X)=d has the same disjoint nonempty sets

    P=Y\X, N=X\Y, |P|=|N|=s>=1.

Consequently its representations have exactly the form

    X=N union U, Y=P union U,
    U subset [r]\(N union P), |U|=k-s.                 (2)

The endpoints of a corner on this difference fiber come from two
distinct sets U,V. Label them so that W(N union U)<W(N union V).
Their colors both equal k-s. The completion cell joins the lower
mark W(N union U) to the upper mark W(P union V). Its color is

    |(N union U) intersect (P union V)|=|U intersect V|.

Since U and V are distinct sets of the same size k-s, this is
strictly smaller than k-s. Thus every corner has two equal endpoint
colors and a strictly smaller completion color. If k-s=0 the fiber
has only one representation and gives no corner. These cases cover
every positive difference and prove properness.

The construction colors a source triangle, not a full integer square.
Its large coordinate weights do not supply a large-density example.

## 2. Exact additive energy

Let E(A) count ordered quadruples x+y=z+t of elements of A. In
the present construction the vector sum of two weight-k incidence
vectors has k-s coordinates equal to two and 2s coordinates equal
to one, for one integer s between zero and k.

The number of such sum vectors for a given s is

    binom(r,k-s) binom(r-k+s,2s).

To obtain an ordered pair of weight-k sets from one such vector,
choose which s of the 2s single coordinates belong to its first
set. There are binom(2s,s) choices. Coordinate dissociation implies
that distinct sum vectors yield distinct integer sums. Therefore

    E(A_(r,k)) = sum_(s=0)^k binom(r,k-s)
                    binom(r-k+s,2s) binom(2s,s)^2.    (3)

Counting ordered pairs rather than pairs of representations gives
the accompanying identity

    m^2 = sum_(s=0)^k binom(r,k-s)
                    binom(r-k+s,2s) binom(2s,s).      (4)

For fixed k, the s=k term in (3) has degree 2k in r; every other
term has degree k+s<2k. Its leading coefficient is
binom(2k,k)^2/(2k)!. Since m^2 has leading coefficient 1/(k!)^2,

    lim_(r->infinity) E(A_(r,k))/m^2 = binom(2k,k).    (5)

For any integer source, if M=binom(m,2) and T is its total number
of directed corners, counting zero and positive differences gives

    E=2m^2-m+4T.

Dividing by M and using (5) proves

    lim_(r->infinity) T(A_(r,k))/M(A_(r,k))
        = (binom(2k,k)-2)/2.                          (6)

Thus any uniform inequality T(A)<=kappa_k M(A) valid for every
properly k-colored source must have

    kappa_k >= (binom(2k,k)-2)/2.                     (7)

This is a necessary lower constraint. No matching upper inequality,
or even a finite universal kappa_k, has been established here.

## 3. The two-color calibration

For k=2 the fibers can be counted directly. There are binom(r,2)
exchange differences, each represented r-2 times, and
3 binom(r,4) singleton differences from pairs of disjoint sets.
Consequently

    T=binom(r,2) binom(r-2,2)=6 binom(r,4),
    M=binom(binom(r,2),2),
    T/M=2(r-3)/(r+1)=2-8/(r+1).                       (8)

The proof in fibers/WEIGHT_TWO_LAYER.md gives the equivalent
coloring with labels exchanged: intersecting pairs have color zero,
disjoint pairs color one, and every corner is (0,1,0).

For any kappa<2, choose r+1>8/(2-kappa). Formula (8) then gives
a properly two-colored source with T>kappa M. The unproved H(2)
in SOURCE_ENERGY_BOTTLENECK.md would therefore be asymptotically
sharp if true. H(5) remains sufficient for the conditional small-color
targets, and is not proved or refuted by this family.

## 4. Bounded discovery that is not used in the proof

constant_weight_probe.py and its adjacent JSON record a two-color
SAT witness at (r,k)=(6,3) and raw negative solver answers at
(7,3), (8,3), (8,4), and (9,4). These finite calls neither prove
a uniform obstruction nor turn the k-color construction into a
two-color construction. Equations (1)--(8) have the direct proofs
above and do not rely on these negative solver answers.
