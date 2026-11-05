# A structured finite candidate against H(2)

Root bounded discriminator, continuing R4-RESEARCH-0010. No coloring
or obstruction theorem is established at the high-energy rank.

Let r>=3, w_i=5^i for 0<=i<r, and

    A_r={w_i-w_j:0<=i,j<r, i!=j},  m=r(r-1).

Equality of two differences of elements of A_r gives a linear
combination of the w_i with coefficients between -4 and 4. Its
largest nonzero term would dominate all smaller terms, since
4 sum_(i<j)5^i=5^j-1. Thus equality forces equality of all
coordinate coefficients, and m has the displayed value.

Every nonzero difference of two roots e_i-e_j has one of the
following four forms. Negation pairs signed differences with
exactly one positive integer difference. The table counts only
that positive member.

| Coordinate type | Number of positive fibers | Multiplicity |
|---|---:|---:|
| 2e_i-2e_j | binom(r,2) | 1 |
| plus or minus (2e_i-e_j-e_k), distinct indices | r binom(r-1,2) | 2 |
| e_i+e_j-e_k-e_l, four distinct indices | 3 binom(r,4) | 4 |
| e_i-e_j | binom(r,2) | 2(r-2) |

For the first type only the pair of opposite roots represents it.
For the second, assigning j or k to the negative coordinate of the
first root gives its two representations. For the four-index type,
choose one of the two positive and one of the two negative indices
for the first root; the other root is then forced, giving four.
For e_i-e_j, every third index t gives the two representations

    (e_i-e_t)-(e_j-e_t),
    (e_t-e_j)-(e_t-e_i).

No other cancellation type is possible: subtracting two roots starts
with two positive and two negative unit coordinates. Cancelling or
coalescing them yields exactly the listed types (or zero).

The exact corner count is consequently

    T_r = binom(r,2) binom(2r-4,2)
           +r binom(r-1,2)+18 binom(r,4),             (1)
    M_r = binom(r(r-1),2).                           (2)

In particular, T_r/M_r tends to 7/2, and at r=8,

    m=56, M=1540, T=3276>2M=3080.                   (3)

A proper two-coloring at rank eight would therefore refute H(2).
This is a conditional discriminator, not a construction claim.

signed_root_source_probe.py returned SAT at ranks three through
seven and an interrupted, undecided answer at rank eight. Its
rank-seven ratio is 1680/861<2. The separate signed_root_order_probe
tested six scalar orderings at rank eight using stored random
integer weights. All six had the counts in (3) and all ended
undecided within their fixed time bounds. These terminal calls prove
no rank-eight impossibility and provide no high-energy proper witness.

The arbitrary-sign cube counterexample in PROPERNESS_ESSENTIAL.md
is a different result: its signs are explicitly not proper. Neither
that example nor the present undecided probes refutes H(5), and no
small-color Ramsey bound follows here. The direct finite-span size
target remains the more immediate sufficient route to those bounds.
