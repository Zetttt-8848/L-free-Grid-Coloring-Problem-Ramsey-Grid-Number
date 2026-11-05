# An energy theorem for two-distance source representations

Root derivation, checkpoint 0025. This gives a complete constant-energy
theorem for a larger Euclidean representation class. The representation
is a real hypothesis; it is not known for a general properly two-colored
source. No unconditional Ramsey bound is changed by this note.

## 1. Squares in a two-distance set

Let X be a finite subset of a real Euclidean space such that every
squared distance between two distinct points is either tau or 2tau,
where tau>0. A common sphere is not needed for the argument below.

There is no three-term progression of distinct points in X: its outer
squared distance would be four times its side squared distance, larger
than 2tau. Every nontrivial equality x_1+x_4=x_2+x_3 consequently has
four distinct points. Write its parallelogram sides as u,v. The sum of
the two diagonal squared lengths is

    ||u+v||^2+||u-v||^2=2(||u||^2+||v||^2).

Both sides have squared length at least tau, and both diagonals have
squared length at most 2tau. Hence equality is forced throughout:

    ||u||^2=||v||^2=tau,
    ||u+v||^2=||u-v||^2=2tau,
    <u,v>=0.                                        (1)

Thus every such parallelogram is a square, with its two long pairs
sharing a midpoint. Conversely two distinct long pairs with the same
midpoint form one of these squares.

For a midpoint c of long pairs, write k_c for the number of unordered
pairs {x,y} in X with x+y=2c and ||x-y||^2=2tau. These pairs are disjoint
in their endpoints. Define

    T_geom(X)=2 sum_c binom(k_c,2)
             =sum_c k_c(k_c-1).                     (2)

This is twice the number of nontrivial unordered equal-sum pair
collisions. For an integer source faithfully represented by X it is
the original source-corner count; a one-way relation-preserving map
still makes it an upper bound for that count.

## 2. A large midpoint fiber separates from all other squares

Fix a midpoint c with k=k_c>=9, and let Y consist of the endpoints of
all its long pairs. Write

    Y={c+p_i,c-p_i:1<=i<=k},
    ||p_i||^2=tau/2.

For i!=j, the squared distances ||p_i-p_j||^2 and ||p_i+p_j||^2
both belong to {tau,2tau} and sum to 2tau. They must both be tau.
Thus the p_i are pairwise orthogonal.

Take any z=c+q in X\Y. Put t=||q||^2+tau/2. For each i, its two
squared distances to c+/-p_i are

    t-2<q,p_i>,  t+2<q,p_i>,

and each is tau or 2tau. Their common average t is therefore tau,
3tau/2, or 2tau. If t=3tau/2, then ||q||^2=tau and every
|<q,p_i>|=tau/4. Orthogonality gives

    ||q||^2 >= sum_i <q,p_i>^2/||p_i||^2
              =k tau/8 >tau,

a contradiction. In either remaining case both distances in the pair
are equal, so <q,p_i>=0 for every i. Consequently every point outside
Y projects to zero on P=span{p_i} after translation by c.

We now show that no square mixes Y with X\Y. A long pair inside Y is
antipodal and has midpoint c. A long pair with exactly one endpoint in
Y has endpoint-sum projection +/-p_i on P. A second long pair with the
same sum would also have exactly one endpoint in Y and the same signed
p_i. That fixes this endpoint; equality of sums then fixes the other,
so the pair would be identical. Pairs with both endpoints inside Y,
or both outside it, have sum projection zero and cannot be alternatives
to such a cross pair.

Finally, an outside long pair of midpoint c is impossible because Y
was defined using all long pairs at c. Thus a repeated long-pair midpoint
fiber either is the fiber defining Y, or uses points entirely outside Y.
By (1)-(2),

    T_geom(X)=T_geom(Y)+T_geom(X\Y),
    T_geom(Y)=k(k-1).                                (3)

This is an exact separation of additive squares, not merely an estimate
on the number of outside neighbors. It avoids a pointwise bound on k.

## 3. The uniform energy bound

Repeatedly remove the sets Y from section 2 while a midpoint fiber has
at least nine pairs. The process terminates because a removal deletes
at least eighteen points. Let X_0 be the remainder and Y_1,...,Y_s the
removed, pairwise disjoint sets, with |Y_i|=2k_i. Exact separation gives

    T_geom(X)=T_geom(X_0)+sum_i k_i(k_i-1).           (4)

Every midpoint fiber in X_0 has k_c<=8, so

    T_geom(X_0)=sum_c k_c(k_c-1)
               <=7 sum_c k_c
               <=7 binom(|X_0|,2).                 (5)

The last inequality counts long pairs, each of which has one midpoint.
Also k_i(k_i-1)<=7 binom(2k_i,2). Since the point sets in the partition
are disjoint,

    binom(|X_0|,2)+sum_i binom(|Y_i|,2)
       <=binom(|X|,2).

Combining with (4)-(5) proves the theorem

    T_geom(X)<=7 binom(|X|,2).                       (6)

No graph classification theorem or spectral hypothesis is used. The
constant eight in the local alternative comes directly from the
orthogonal projection calculation in section 2.

## 4. Integer source consequence and its scope

Suppose a finite integer set A has an injective map phi:A->X as above
that preserves all equalities a+b=c+d occurring in A. Such a map is an
injective Freiman-2 homomorphism; reflection of additional equalities
is not required for the following upper bound. Three-term progressions
in A are impossible by injectivity and the first paragraph of section 1.
Every four-distinct-mark additive equality of A maps to a square of X.
Since phi is injective, different unordered pair collisions remain
different. The source identity T(A)=2D(A)+P3(A), with P3(A)=0, and (6)
give

    T(A)<=7 M(A).                                   (7)

The original directed source triangle then has an explicit proper
two-coloring: color (b,a) by whether ||phi(b)-phi(a)||^2 is tau or 2tau.
Every source corner maps to a square as in (1); its two parallel endpoint
cells have squared distance tau and its outer completion has squared
distance 2tau. This preserves the original positive equal-step corner,
with no reverse inference from a source triangle to a full grid.

The standard positive-difference Cauchy deduction now yields the actual
source-size estimate for this representation class

    M(A)<=15 span(A).                               (8)

Indeed sum_h r_A(h)=M and sum_h r_A(h)^2=M+2T<=15M,
so M^2<=span(A)*15M, including the zero-size cases separately.

Equation (8) is stronger than S21 on this class. The missing implication
for the research objective is a theorem covering every properly
two-colored strict source, or another argument controlling those sources
without such a representation. Proper sources may contain three-term
and four-term progressions, so this literal two-distance representation
cannot be universal. No general-source embedding is asserted, and the
working Ramsey bounds remain unchanged.
