# Why universal linear energy estimates do not suffice

Root derivation continuing R4-RESEARCH-0010, using the explicit family
in fibers/ROW_COLUMN_SIGN_PROBE.md. The results here exclude specified
proof strategies. They do not refute the energy hypothesis for proper
colorings and do not improve a Ramsey bound.

## 1. The exact relation and the tempting sufficient inequality

Let V(A) be a strict source triangle with M cells and T corners. Give
its cells arbitrary signs z in {-1,+1}. For a corner with two
same-offset endpoints P,R and completion C, define

    D(z)=sum_corners z_P z_R,
    Q(z)=sum_corners z_C(z_P+z_R),
    B(z)=number of monochromatic corners.

The sum of the three pair products is 3 on a monochromatic corner
and -1 on a nonmonochromatic two-color corner. Thus

    D(z)+Q(z)=4B(z)-T.                                (1)

If s_d is the sum of the signs in the difference fiber of size r_d,
then each unordered endpoint pair occurs once, giving

    D(z)=1/2 sum_d (s_d^2-r_d)>=-M/2.                 (2)

In a proper coloring B=0. Therefore a universal bound

    Q(z)>=-(9/2)M                                    (3)

would imply T=-D-Q<=5M, exactly H(5).

But (3), even when restricted to actual sign vectors, is false.
The auxiliary note supplies a direct formula on the dissociated
binary cube A_r={sum_(i in X)5^i:X subset [r]}:

    z(Y,X)=+1 if |X intersect Y|<=floor(r/4),
           -1 otherwise.

It proves

    M_r=(4^r-2^r)/2,
    Q(z)=-(1/2+o(1))6^r,
    Q(z)/M_r=-(1+o(1))(3/2)^r.                       (4)

An elementary finite bound already violates (3) for all r>=256.
The note also displays a monochromatic corner, so these signs
are not examples contradicting H(5).

This closes the arbitrary-sign row/column inequality, beyond the
earlier failure of a constant least-eigenvalue bound. It does not
close a lower bound for Q which uses properness essentially.

## 2. Vanishing monochromatic fraction on sources of growing energy

The same family gives a stronger limitation. Its exact corner count is

    T_r=(6^r-2*4^r+2^r)/4.                           (5)

Indeed, for difference support size s there are
binom(r,s) 2^(s-1) positive differences, each with 2^(r-s)
representations. Summing binom(2^(r-s),2) times that multiplicity
over s=1,...,r gives (5).

We prove B(z)/T_r tends to zero. In the six-state product count
from the auxiliary note, the two endpoint common sets are U,V.
Let

    J=|U intersect V|, U_0=|U|, V_0=|V|,
    q=floor(r/4).

Under the uniform product measure on the six choices per coordinate,

    J~Bin(r,1/6),  U_0~Bin(r,1/3),  V_0~Bin(r,1/3).

They need not be independent. When J<=q, U_0>q and V_0>q, the
three corner signs are (-1,+1,-1) and hence not monochromatic.
For r>=24 the elementary estimates proved in the auxiliary note are

    Pr(J>q)<=80/r,
    Pr(U_0<=q)<=32/r,  Pr(V_0<=q)<=32/r.

Thus the exceptional proportion is at most 144/r.

The six-state count includes zero difference support and U=V; these
do not give corners. Every actual corner appears four times among
the remaining states: twice from exchanging U,V and twice from
negating the signed difference. The sign pattern is unchanged by
those exchanges because it depends only on intersections. Removing
noncorners therefore gives the valid upper bound

    B(z) <= (1/4)6^r*(144/r) = 36*6^r/r.             (6)

Dividing (6) by (5) proves

    B(z)/T_r <= (144/r)/[1-2(2/3)^r+(1/3)^r]
                 ->0.                              (7)

At the same time, (2) of the auxiliary note and (5) give

    T_r/M_r ~ (1/2)(3/2)^r ->infinity.               (8)

## 3. No universal linear supersaturation from total source energy

There are no absolute constants a>0 and finite b such that

    B(z)>=a T(A)-b M(A)                              (9)

holds for every source A and every two-coloring of V(A).

For if (9) held, divide it by T_r and apply the family above.
Equation (7) makes the left side tend to zero, whereas (8) makes
the right side tend to a>0, a contradiction. This also covers
negative b; no assumption b>=0 is needed.

Consequently, H(5) cannot be obtained by first proving a universal
linear lower bound of the form (9) and then setting B=0. A proof
restricted to proper colorings, a nonlinear statement, or a direct
bound involving source span remains possible. No claim about those
alternatives follows from this counterexample.
