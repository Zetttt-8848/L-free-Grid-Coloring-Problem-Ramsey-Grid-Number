# Retaining dilation bounds for larger local triangles

Checkpoint-0013 update: F13 is false. The complete construction in
THIRTEEN_TRIANGLE_FOURTEEN_RAINBOW.md has fourteen rainbow corners and
no monochromatic corner. The exact multiplicity theorem below remains
valid, but the uniform whole-corner T_13 scalar amplification is now
excluded at host side 464. Its historical conditional calculation is
retained to identify the failed premise precisely.

Root derivation continuing R4-RESEARCH-0010. This refines a conditional
rainbow-counting criterion. No local rainbow lower bound, and no
improved Ramsey number, is proved here.

Use the notation and simplex embeddings of TRIANGLE_RAINBOW_ENERGY.md.
For a host triangle T_N and local triangle T_m put

    D=floor((N-2)/(m-2)),
    C(N,m)=sum_(d=1)^D binom(N-d(m-2),2),
    M_N=binom(N,2).

There are binom(m-j,2) local corners of step j. A fixed host corner
of step h can receive such a corner only at dilation d=h/j, which
must be an integer at most D. Thus its multiplicity is at most

    b_trunc(N,m)=max_(1<=h<=N-2)
           sum_(1<=j<=m-2, j divides h, h/j<=D) binom(m-j,2). (1)

This still disregards the host corner's boundary position. If every
proper three-coloring of T_m has at least rho rainbows, the incidence
count and the host budget R<=M_N give

    rho C(N,m)<=b_trunc(N,m) M_N.                    (2)

A strict reverse inequality is therefore a sufficient contradiction.
This proof retains the allowed dilation; replacing b_trunc by
binom(m,3) is only a coarser version of the same criterion.

For orientation, exact finite arithmetic at N=464 gives

| m | D | C(464,m) | b_trunc | rho sufficient in (2) |
|---:|---:|---:|---:|---:|
| 11 | 51 | 1790610 | 143 | 9 |
| 12 | 46 | 1606251 | 185 | 13 |
| 13 | 42 | 1455419 | 233 | 18 |

The maximum in (1) is a finite explicit expression. These evaluations
illustrate (2), but no numerical Ramsey improvement relies on them.
The unconditional multiplicity lower bound below, in contrast, has
a direct geometric proof and will control the exact-boundary version.

## A single host corner that enforces a multiplicity cost

In T_464 choose the host corner of step 12 with common gap base
(150,150,150). Its three gap vectors sum to 462, as required.
For each local step j dividing 12 and each local corner with common
base b=(b_1,b_2,b_3), its only possible dilation is d=12/j.

For m in {11,12,13}, every such corner embeds at this host corner.
Indeed, b_i<=m-2-j, so

    d b_i <=(12/j)(m-2-j)<=12(m-3)<=120<150.

The last comparison is valid throughout these three local sizes.
Thus (150-d b_1,150-d b_2,150-d b_3) is a nonnegative translation.
Its coordinate sum is precisely 462-d(m-2), because
sum b_i=m-2-j and dj=12. Hence it is one of the permitted embeddings.
Different local corners give different embeddings by their dilation
and translation.

All these incidences occur at one actual host corner. Consequently
the exact maximum host multiplicity b_exact satisfies

    b_exact >= b_12(m)
      :=sum_(j in {1,2,3,4,6}) binom(m-j,2),         (3)

namely

    b_12(11)=45+36+28+21+10=140,
    b_12(12)=55+45+36+28+15=179,
    b_12(13)=66+55+45+36+21=223.                    (4)

These are lower bounds, not claimed exact maxima.

## How a literal coloring rules out the uniform density route

Suppose a displayed proper local coloring has r_m rainbow corners.
Every valid universal lower bound rho must satisfy rho<=r_m.
If

    r_m C(464,m)<=b_12(m) M_464,                    (5)

then even the exact-boundary scalar criterion
rho C>b_exact M_464 is impossible: its left side cannot exceed
r_m C, and its right side is at least b_12 M_464.

At the three local sizes, witnesses with respectively at most
8,11,16 rainbows suffice to establish (5). In particular,

    8*1790610=14324880 <140*107416=15038240,
    11*1606251=17668761<179*107416=19227464,
    16*1455419=23286704<223*107416=23953768.          (6)

This is stronger than merely comparing with binom(m,3). The
construction note fibers/LARGER_TRIANGLE_RAINBOW_PROBE.md records
the literal local colorings and their direct proofs. Its final
counts determine which instances of (5) have actually been met.

The limitation concerns uniform counting of all local rainbow
corners and scalar amplification through R<=M_464. It does not
exclude selected or signed local weights, a joint use of line
variance and properness, or another embedding family. In particular,
a witness which only defeats the coarse binom(m,3) criterion must
not be said to defeat exact-boundary counting without (5).

## The exact multiplicity at local size thirteen

For m=13, the exact maximum multiplicity is

    b_exact(464,13)=223.                             (7)

The lower bound was proved in (3)--(4). Here is a direct upper
bound, retaining the actual allowed dilations and boundary.
There are D=42 possible dilations. For host step h>42, a local
step-one corner cannot embed. Consequently its multiplicity is
at most binom(13,3)-binom(12,2)=286-66=220<223.

For h<=42, ignore the boundary temporarily. Every local step
which can contribute belongs to {1,...,11} and divides h.
The possible divisor sets are contained in those of the following
nine representative values. The middle column lists the entire
relevant divisor set, and the last is its corner weight.

| representative h | divisors between 1 and 11 | sum binom(13-j,2) |
|---:|:---|---:|
| 22 | 1,2,11 | 122 |
| 33 | 1,3,11 | 112 |
| 28 | 1,2,4,7 | 172 |
| 35 | 1,5,7 | 109 |
| 42 | 1,2,3,6,7 | 202 |
| 30 | 1,2,3,5,6,10 | 218 |
| 40 | 1,2,4,5,8,10 | 198 |
| 24 | 1,2,3,4,6,8 | 233 |
| 36 | 1,2,3,4,6,9 | 229 |

To see that the list covers all h<=42, first consider a multiple
of 11: it is 11,22,33 and is covered by the first two rows.
A multiple of 7 is 7,14,21,28,35,42 and is covered by the next
three. A remaining multiple of 5 is 5,10,15,20,25,30,40 and
is covered by 30 or 40. If h has a prime factor at least 13,
the other factor is at most three, so its relevant divisors are
contained in {1,2} or {1,3}. Otherwise h has only prime factors
2 and 3. The possibilities 2^a 3^b<=42 have relevant divisors
contained in those of 24 or 36: for b=0 only 1,2,4,8 can
occur; for b=1 the largest allowed 2-power is 8; for b=2 it
is 4; and b=3 gives only 1,3,9. Larger b is impossible.

Only the divisor weights for h=24 and h=36 exceed 223.
Moreover no other h<=42 has those full divisor sets: their
least common multiples are 24 and 36. If a proper subset of
the h=24 set occurs outside those already bounded rows, losing
any non-unit divisor of weight at least 10 reduces its weight
to at most 223. For h=36, losing any divisor other than 9
loses at least 21, whereas losing 9 leaves precisely the
weight-223 set {1,2,3,4,6}. Thus all remaining cases are at
most 223 even before accounting for the boundary.

For h=24 let g be the common host gap base. It satisfies
sum g_i=462-24=438, so at least one coordinate g_i<=146.
A local step-one corner has a base b with sum b_i=10 and
must be dilated by 24. If that coordinate b_i>=7, then
24 b_i>=168>g_i and the embedding fails. There are
binom(10-7+2,2)=10 such local bases. At least ten of the
233 possible incidences are absent, leaving at most 223.

For h=36, one host base coordinate is at most 142. The
step-one dilation is 36, so every local base with b_i>=4
fails there. There are binom(10-4+2,2)=28 such bases.
Thus the multiplicity is at most 229-28=201<223.
This proves the upper bound and hence (7).

Consequently the following finite statement would prove R3<=464:

    Every proper three-coloring of T_13 has at least
    seventeen rainbow corners.                     (F13)

Indeed, under (F13), incidence counting would give

    17*1455419=24742123
       <=223*107416=23953768,

whose left side exceeds its right side by 788355. This
contradiction is a complete deduction from (F13).

The premise (F13) is false, by the fourteen-rainbow proper coloring in
THIRTEEN_TRIANGLE_FOURTEEN_RAINBOW.md. A valid uniform lower count is
therefore at most fourteen, and

    14*1455419=20375866<23953768=223*107416.

Thus the exact-multiplicity uniform scalar scheme is excluded at side
464. The earlier 21-rainbow coloring and undecided searches had not
settled it; the new literal construction does. Nonuniform local or
embedding weights, or a stronger host-coloring inequality, are outside
this particular limitation.
