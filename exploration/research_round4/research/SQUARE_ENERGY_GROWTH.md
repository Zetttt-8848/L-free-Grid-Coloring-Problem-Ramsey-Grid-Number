# Square sources have unbounded corner-to-cell ratio

Root derivation following the bounded square-source task in
fibers/SQUARE_SOURCE_PROBE.md. This gives a self-contained lower
bound for total corners. It does not construct a proper coloring.
The growth of the additive energy of squares is a classical topic;
no priority claim is made for that growth statement.

Let A_m={1^2,...,m^2}, M_m=binom(m,2), and let T_m count all
directed corners in its strict source triangle, regardless of color.
For m>=60 put L=floor(m/12). We prove

    T_m >= (m^2/2048) log((L+1)/6),                    (1)
    T_m/M_m >= (1/1024) log((L+1)/6).                 (2)

In particular, T_m/M_m tends to infinity. The constants are chosen
to keep the proof elementary; no sharp asymptotic is asserted.

## 1. An injective family of corners

Choose integers p,q with

    3<=p<=L,  1<=q<p/2,  gcd(p,q)=1.

Put t=floor(m/(3p)), and choose integers x,y with

    t<=x<y<2t.

Define four positive root indices

    a=px-qy,    b=px+qy,
    c=py-qx,    d=py+qx.                              (3)

Positivity follows from p>2q: for example
a>pt-2qt>0, and c>pt-2qt>0. The largest index is d, because

    d-b=(p-q)(y-x)>0,
    d-c=2qx>0,
    c-a=(p+q)(y-x)>0.

Also d<2(p+q)t<3pt<=m. Thus all four squares belong to A_m.
Direct expansion yields

    b^2-a^2=4pqxy=d^2-c^2.                           (4)

Since a<c and b<d, the three cells

    (b^2,a^2), (d^2,a^2), (d^2,c^2)                  (5)

form a directed corner, of step c^2-a^2=d^2-b^2>0.
The possible equality b=c causes no problem: the three cells
in (5) are still distinct.

This construction is injective in (p,q,x,y). A corner (5)
determines its positive indices a,b,c,d. Equation (3) gives

    (b+a)/(d-c)=p/q.

The relatively prime positive numerator and denominator recover
p and q uniquely, and then

    x=(b+a)/(2p),    y=(b-a)/(2q)

recover x and y. Distinct choices therefore give distinct corners.

Let

    h(p)=#{q:1<=q<p/2, gcd(p,q)=1},
    h(1)=h(2)=0.

There are binom(t,2) choices of x<y in [t,2t). Since p<=m/12,

    t>=m/(3p)-1>=m/(4p),   t>=4,
    binom(t,2)>=t^2/4>=m^2/(64p^2).

Injectivity now gives

    T_m >= (m^2/64) sum_(p=1)^L h(p)/p^2.            (6)

## 2. Elementary supply of relatively prime parameters

For n>=1 let Q(n) count ordered pairs (u,v) in [n]^2 with
gcd(u,v)=1. Every other pair is divisible in both coordinates by
some integer j>=2. The union bound gives

    Q(n)>=n^2-sum_(j=2)^n floor(n/j)^2
         >=n^2[1-sum_(j=2)^infinity 1/j^2]
         >=n^2/4.                                   (7)

For the last estimate,

    sum_(j=2)^infinity 1/j^2
      <=1/4+integral_2^infinity x^(-2) dx=3/4.

Write phi(p)=#{1<=q<p:gcd(p,q)=1}. Classifying a relatively
prime pair by its maximum shows

    Q(n)=1+2 sum_(p=2)^n phi(p).

For p>=3, the involution q->p-q pairs the relatively prime
residues below and above p/2, without a fixed point. Hence
h(p)=phi(p)/2. Consequently, for n>=2,

    H(n):=sum_(p=1)^n h(p)=(Q(n)-3)/4.

When n>=5, (7) implies

    H(n)>=n^2/16-3/4>=n^2/32.                        (8)

Discrete summation by parts, with L>=5, gives

    sum_(p=1)^L h(p)/p^2
      =H(L)/L^2+sum_(n=1)^(L-1) H(n)
                              [1/n^2-1/(n+1)^2]
      >=(1/32) sum_(n=5)^(L-1) (2n+1)/(n+1)^2
      >=(1/32) sum_(j=6)^L 1/j
      >=(1/32) log((L+1)/6).                         (9)

The last line follows by comparing each 1/j with
integral_j^(j+1) dx/x. For L=5 the sum is empty and the logarithm
is zero, so the same statement applies at the boundary.

Combining (6) and (9) proves (1). Since M_m<=m^2/2, division
proves (2). The right-hand side of (2) tends to infinity.

## 3. Exact implication for the live hypothesis

If every V(A_m) has a proper two-coloring, this family refutes
every finite constant H(kappa) in SOURCE_ENERGY_BOTTLENECK.md.
Conversely, if any H(kappa) is true, some finite square source
must fail to admit a proper two-coloring.

Neither premise is settled. The bounded satisfiable instance at
m=200 proves neither the existence of a uniform coloring nor an
unbounded family of satisfiable instances. The five-mark pattern
in fibers/SQUARE_SOURCE_PROBE.md only rules out a coloring based
on the difference alone. The present proof counts corners without
reference to their colors and cannot supply the missing coloring.

The restricted H(5) needed only for source spans at most 91998 is
also not settled by (1). A possible counterexample at arbitrarily
large span would refute the global hypothesis without necessarily
refuting that finite-range route to the requested small-color bounds.
