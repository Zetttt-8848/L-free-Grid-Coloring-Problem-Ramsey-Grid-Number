# A point-deletion bound for two-distance sources

Root derivation, continuation 0038. This closes the coefficient-ten gap
left by the auxiliary endpoint estimate using a rigidity argument for its
remaining orthogonal component. It is a theorem for the two-distance
representation class, not a representation theorem for general proper
sources. The earlier global H7 estimate on this class remains stronger
than the H10 conclusion obtainable by summing the new deletion bound.
The new content is the pointwise deletion estimate.

## 1. Statement and existing geometric input

Suppose a finite integer source A admits an injective Freiman-2
homomorphism into a Euclidean set X whose distinct squared distances
are tau and 2tau, with tau>0. Then, for every a in A,

    T(A)-T(A\{a}) <=10(|A|-1).                       (1)

In particular the open EP10 assertion holds throughout this class at
both endpoints, and indeed at every mark. No source-size range is needed.

We use the completed geometric facts in
TWO_DISTANCE_SOURCE_ENERGY_0025.md. Every nontrivial additive
parallelogram in X is a square: its sides have squared length tau,
its diagonals 2tau, and adjacent side vectors are orthogonal. There
are no nontrivial three-term progressions. At the midpoint of k long
pairs, the antipodal axes are mutually orthogonal, with squared norm
tau/2. If k>=9, those 2k points separate from all other additive
squares: a square meeting them belongs to this same midpoint fiber.
The full proof of that separation is already in the cited local note.

Scale to tau=1 and translate the chosen image point to p=0. Every
other point of X is near (squared norm 1) or far (squared norm 2).
Let their counts be n_1,n_2, and put n=n_1+n_2=|A|-1.

For each far point w let q_w be the number of unordered pairs of near
points {u,v} with u+v=w, and let D_w contain their 2q_w endpoints.
The pairs in D_w are disjoint, since w and one endpoint determine the
other. Each is a square through 0, with w as the opposite vertex.

Every source parallelogram containing a maps injectively to one of
these squares. A four-distinct-mark integer parallelogram contributes
two source corners, both of which disappear on removing any one of
its marks. There are no source three-term progressions, by injectivity
and the two-distance fact above. Extra geometric relations need not
come from A, so the direction needed here is the inequality

    T(A)-T(A\{a}) <=2 sum_(w far) q_w.               (2)

## 2. Reduction to midpoint fibers of size at most eight

If 0 belongs to a midpoint fiber of k>=9 long pairs, the existing
separation theorem puts every square through 0 in that fiber. There
are k-1 alternatives to its own long pair. Thus

    2 sum_w q_w=2(k-1)<=|A|-2<=10(|A|-1),            (3)

and (1) follows.

Otherwise every midpoint fiber containing 0 has k<=8. In particular

    q_w<=7 for every far w.                          (4)

Define the high-output set

    H={w far:q_w>=6}.                                (5)

We will control how often the sets D_w for w in H can share a near
point. The geometry of six or seven decompositions makes the number
of far near-neighbors of w bounded independently of the ambient dimension.

## 3. Rigidity at an output with six or seven decompositions

Fix w in H. Put c=w/2 and p_0=c. Write its near pairs as

    c+p_i, c-p_i, 1<=i<=q_w.

Together with the pair 0,w, these are the k=q_w+1 midpoint pairs.
The k vectors p_0,...,p_(k-1) are orthogonal and have squared norm 1/2.

Take a different far point v with squared distance ||v-w||^2=1, and
put eta_v=v-c. Since ||v||^2=||w||^2=2,

    <v,w>=3/2, ||eta_v||^2=1,
    <eta_v,p_0>=1/4.                                (6)

For every i, the two squared distances from v to c+p_i,c-p_i belong
to {1,2} and average ||eta_v||^2+||p_i||^2=3/2. Hence one is 1 and
the other 2, giving

    <eta_v,p_i> in {1/4,-1/4}.                       (7)

The sign for i=0 is fixed positive. The projection of eta_v onto the
k axes has coefficients +/-1/2 and squared norm k/8.

If q_w=7, then k=8, so this projection exhausts ||eta_v||^2=1.
Each v is consequently specified by seven variable signs. If two
such sign words differ in r positions, their squared distance is r/2.
Since distinct points of X are at squared distance 1 or 2, their
binary words have Hamming distance 2 or 4.

Now let q_w=6, so k=7. Write the orthogonal remainder as r_v. It has

    ||r_v||^2=1/8.                                  (8)

There are six variable axis signs. For v!=v', let d be their Hamming
distance on these six signs. Orthogonality gives

    ||v-v'||^2=d/2+||r_v-r_v'||^2,
    0<=||r_v-r_v'||^2<=1/2.                         (9)

The allowed squared distances 1,2 force the following exhaustive
alternatives:

    d=1 or 3: ||r_v-r_v'||^2=1/2, so r_v=-r_v';
    d=2 or 4: ||r_v-r_v'||^2=0,   so r_v=r_v'.       (10)

The case d=0 cannot give distinct points, since their distance would
be at most 1/2. Cases d>=5 have distance greater than 2. The equality
case of the triangle inequality in the first line of (10), together
with (8), gives the asserted antipodality.

Fixing one v therefore places all residuals in a single antipodal
pair. An additional binary sign records which member occurs. By
(10), that sign changes exactly when the six-coordinate Hamming
distance is odd. The resulting seven-bit code again has pairwise
Hamming distances 2 or 4.

Thus the residual component in the k=7 case is not arbitrary: the
two-distance condition itself confines it to one line and supplies
the missing seventh bit.

## 4. A small code bound with an elementary proof

Any binary length-seven code with all pairwise distances in {2,4}
has at most 29 words. Replace its bits by signs s in {-1,1}^7.
Distinct codewords have inner products 3 or -1. For each codeword s
consider the function on the full sign cube

    F_s(t)=(<s,t>-3)(<s,t>+1).                       (11)

On the selected codewords this function is zero except at s, where
it is (7-3)(7+1)=32. The functions F_s are consequently linearly
independent after restriction to the code.

On the sign cube, t_i^2=1, so all functions (11) lie in the span of

    1; the seven functions t_i; the 21 functions t_i t_j, i<j.

That space has dimension at most 1+7+21=29. Linear independence of
their restrictions proves the bound. No optimal code size is needed.

By Section 3, every w in H has at most 29 far points v with
||v-w||^2=1.                                            (12)

## 5. Shared decomposition endpoints and the global excess

If v,w are distinct far points and D_v intersects D_w, then

    ||v-w||^2=1.                                    (13)

To see this, suppose instead ||v-w||^2=2. At c=w/2 write eta=v-c.
Then ||eta||^2=3/2. For each antipodal near pair c+/-p_i in D_w,
the two distances to v are in {1,2} and have average
||eta||^2+||p_i||^2=2. Both must be 2. Thus v is at squared distance
2 from every u in D_w. But u in D_v would require v-u to be a near
point, giving ||v-u||^2=1, a contradiction. This proves (13).

Fix a near point u. The outputs w in H for which u belongs to D_w
are pairwise near by (13). After choosing one of them, (12) allows
at most 29 others. Hence u belongs to at most 30 of the sets D_w.
Double counting gives

    I:=sum_(w in H) 2q_w <=30n_1.                   (14)

For q in {6,7}, one has q-5<=2q/7. Therefore the total excess over
five decompositions obeys

    E:=sum_(w in H)(q_w-5) <=I/7<=30n_1/7.          (15)

Every other far output has q_w<=5. Combining (2), (4), and (15),

    T(A)-T(A\{a})
       <=2 sum_w q_w
       <=10n_2+2E
       <=10n_2+(60/7)n_1
       <=10(n_1+n_2)=10(|A|-1).                    (16)

Together with the large-midpoint alternative (3) and the immediate
zero- or one-point cases, this completes the proof of (1).

## 6. Scope for the main research objective

The argument establishes EP10 on the entire two-distance representation
class, strengthening the auxiliary endpoint constant 14 to 10 without
classifying all two-distance sets. It also explains precisely how the
formerly residual norm tau/8 becomes a single binary coordinate.

This is not a theorem for every proper source. Such sources may have
three-term progressions and cannot all have this literal representation.
The previously established H7 and M<=15 span bounds on this class are
retained; summing the new point-deletion bound would give the weaker H10.
The main research opportunity is to find a counterpart of the bounded
shared-output multiplicity in the general actual-color addition graph,
or a different argument for EP10/S21 that needs no geometric embedding.
No unconditional Ramsey bound changes here.
