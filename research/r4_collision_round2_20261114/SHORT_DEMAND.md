# Short-request demand and exact multiple-width certificates

Status: proved elementary inequalities, independently reviewed internally.
No new Ramsey bound. External Claude review is pending.

## Scope and definitions

Let A lie in p consecutive integer positions and admit a proper binary
coloring of V(A). At lag h, let C_h^0,C_h^1 be its two colored start classes,
r_h their total cardinality, and n=p-h. These starts lie in n positions.
Every pair u<v in one C_h^e produces one request to (v+h,u), with target
lag t=h+v-u and forced opposite color. This is the round-1 forcing lemma.
The number of colors is two at this level of the R4 recursion; no ternary
complementary-color assertion is being made.

For m>=1 and N>=0 write N=mq+a, 0<=a<m, and define

    bal(m,N) = m*q*(q-1)/2 + a*q.

This is the minimum of sum binom(b_i,2) over m nonnegative integer
occupancies with sum N: moving one unit from an occupancy at least two
larger than another strictly decreases that sum.

## Sliding-window lemma

For s>=1, use every window {x,...,x+s}, x=-s,...,n-1, after translating
the start interval to {0,...,n-1}. There are n+s potentially nonzero
windows per color. Each start occurs s+1 times. The total of the 2(n+s)
occupancies is (s+1)r_h. Therefore

    B_h(s) := bal(2(n+s),(s+1)r_h)
      <= sum_(same-color pairs u<v) (s+1-(v-u))_+.

Every pair at distance delta<=s appears in precisely s+1-delta windows.
In particular, the number P_h(s) of such pairs satisfies

    P_h(s) >= ceil(B_h(s)/s).

This statement holds even for arbitrary two-colored subsets of an interval;
properness is used only when interpreting the pairs as forced requests.

## Weighted dual without duplicate charges

Let w_t>=0 be finitely supported target-lag weights. For each h choose
finitely many lambda_(h,s)>=0 such that for every integer delta>=1,

    sum_(s>=delta) lambda_(h,s)*(s+1-delta) <= w_(h+delta).     (D)

Multiply the sliding-window inequality by lambda_(h,s), sum, and apply
(D) to each pair separately. This gives

    R_w(h) >= sum_s lambda_(h,s)*B_h(s),
    R_w    >= sum_h sum_s lambda_(h,s)*B_h(s).

A request has a unique originating lag h and same-color pair, so the
last sum has no additional multiplicity. Different widths may be added
only under (D), not by adding their separate demand estimates.

The one-width special case is

    R_w(h) >= B_h(s)*min_(1<=delta<=s) w_(h+delta)/(s+1-delta).

It may be combined by taking a maximum with
min_(1<=delta<=s) w_(h+delta)*ceil(B_h(s)/s).

## Finite exact certificate algorithm

Choose a finite list of widths. Linear optimization may propose nonnegative
coefficients, but only rational coefficients satisfying (D) are accepted.
For the existing window consumer, w_t is piecewise affine in integer t.
The left side of (D) is also piecewise affine, changing slope only at s+1.
It suffices to check endpoints and all these breakpoints, including the
translated coarse-window boundaries. Between consecutive checked integers,
the difference is affine and hence nonnegative if it is so at the endpoints.
Beyond the largest width the left side is zero.

The certificate generator records all coefficients as exact rationals.
An independent verifier additionally checks every integer delta in the
support; it does not trust the linear optimizer or the breakpoint reduction.
It also recomputes the occupancy lower bound by its defining formula.

## Remaining bridge and scale warning

This supplies demand, not control of collisions. A useful exclusion still
needs an upper bound on the same weighted requests, with matching weights,
span, and coloring assumptions. R_w^2<=U_w E_w from round 1 alone does not
provide a numerical gain.

For comparison, put M=binom(|A|,2), L=span(A)>0. The inherited exact identity

    R = (sum_h(r_h^2 + Delta_h^2 - 2r_h))/4

implies R>=M^2/(4L)-M/2. Even a hypothetical local bound m_t^e(u)<=C*sqrt(t)
would give only R<=C*sqrt(L)*M by counting at most M targets. Hence
M<=4C*L^(3/2)+2L and the same three-quarter-power cardinality exponent.
A square-root collision estimate alone does not automatically improve R4.

The multiwidth formulation is a new interface in this research package,
built from ordinary occupancy convexity and linear duality. No worldwide
novelty claim is made. The inherited request identity is already in the
manuscript's signed-completion theorem and is not claimed as new.
