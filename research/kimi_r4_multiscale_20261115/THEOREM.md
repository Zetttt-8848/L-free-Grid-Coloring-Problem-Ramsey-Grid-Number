# Erratum and triviality theorem for multiscale quotient counts

**No new Ramsey bound is established.** The old Q3a inequality is false. Its
proposed multiscale extensions based on pair-tight counts or seven-quotient
incidence have no Ramsey consumer. The round-1 Q1 cover bound and Q2
counterexample are separate statements and are not refuted here.

## 1. Definitions

Use zero-based cells `(x,y)` in `[n]^2` and the L
`L(x,y;d)={(x,y),(x+d,y),(x+d,y+d)}`, `d>0`. The seven palette quotients are
the nontrivial bipartitions of four colors, up to interchanging the sides. The
signature `S(L)` is the set of quotients for which all colors used by the three
vertices lie in one side. An L is pair-tight when its signature is nonempty.

Let `P_d` count pair-tight Ls of step `d` in the whole square. For a positive
integer scale `s`, a copy is a Cartesian arithmetic-progression grid
`{(a+s*i,b+s*j):0<=i,j<5}` contained in the host. It has `C_s=(n-4s)^2` copies.
Each copy has 30 geometric Ls. Define `m_s(L)` as the number of scale-`s` copies
containing `L`.

## 2. Signature trichotomy and the collapse of `P_d`

**Proposition M1 (PROVED).** If a three-cell word in four colors uses `r`
distinct colors, then its signature has size `2^(4-r)-1`. Thus the sizes for
`r=1,2,3` are respectively `7,3,1`. In particular, every geometric L in every
four-coloring, proper or improper, is pair-tight for some quotient, and

```text
P_d=(n-d)^2  for every 1<=d<n.
```

**Proof.** Choose the side containing the nonempty set of `r` used colors. Each
of the other `4-r` colors can independently be assigned to that side or its
complement. The unique assignment putting every color on that side leaves the
other side empty and is invalid. Every other assignment gives one unordered
nontrivial bipartition, and the side containing the used colors is unique, so
there is no double count. The count is `2^(4-r)-1`. Since `r<=3` for three
cells, this number is always positive. For fixed `d`, there are `(n-d)^2`
geometric Ls. QED.

The two independent programs exhaust all 64 color words and obtain the word
counts 4, 36, and 24 for signatures of sizes 7, 3, and 1, respectively.

## 3. Complete counterexample to old Q3a

**Old Q3a (REFUTED).** The published assertion was

```text
sum_(d=1)^4 P_d/(5-d)^2 >= 3(n-4)^2
for every proper four-coloring of [n]^2.
```

The following matrix is a proper four-coloring of the 6 by 6 square. As in the
source file, row `x` lists `y=0,...,5`.

```text
2 1 1 0 1 0
1 1 0 1 0 2
1 0 0 1 0 1
0 0 2 0 0 2
1 2 2 0 2 2
2 0 1 2 2 1
```

It is the unmodified crop of the stored proper 20 by 20 three-coloring. Both the
new independent verifier and the project's standard coloring checker enumerate
all 55 geometric Ls and find no monochromatic one. No external theorem is needed
for this finite object.

By M1, `(P_1,P_2,P_3,P_4)=(25,16,9,4)`. Consequently

```text
sum_(d=1)^4 P_d/(5-d)^2
 = 25/16 + 16/9 + 9/4 + 4
 = 1381/144
 < 12 = 3(6-4)^2.
```

The shortfall is `347/144`. This is a COUNTEREXAMPLE, not an unsuccessful
search.

The old unweighted consequence `sum_(d=1)^4 P_d>=3(n-4)^2` is true, but only for
a trivial geometric reason: M1 makes the left side `sum_(d=1)^4(n-d)^2`, whose
first three summands are already at least `3(n-4)^2` for `n>=5`. The old proof
does not establish coloring information.

## 4. Exact copy multiplicities

The old proof also claimed that a fixed step-`d` L lies in exactly `(5-d)^2`
contiguous 5 by 5 blocks. That is false at the boundary. For example, in either
the 5-square or the 6-square, `L(0,0;1)` lies in exactly one such block, not 16.

For general scale, if `s` does not divide `d`, or if `r=d/s` is outside `1..4`,
then `m_s(L)=0`. Otherwise `m_s(L)<=(5-r)^2`, because there are only `5-r`
relative positions on each coordinate axis; host boundaries can reduce this
number. The exact value is obtained by counting the admissible origins directly.

**Proposition M2 (PROVED).** For every four-coloring of `[n]^2`, every scale
`s` with `4s<n`, and the copy family above,

```text
sum_L m_s(L) = 30 C_s.
```

More generally, for finitely many nonnegative scale weights `lambda_s`,

```text
sum_s lambda_s sum_L m_s(L)
 = 30 sum_s lambda_s C_s.
```

**Proof.** Each scale-`s` copy contains exactly 30 Ls. By M1, every one is
pair-tight in every four-coloring. Summing over copies counts `m_s(L)` for each
L. The weighted form follows by linearity. QED.

The identity includes every cross-block L and every boundary truncation. It is
not merely an interior asymptotic. The checkers reconstruct all `1,063`
individual multiplicity entries for `(n,s)=(5,1),(6,1),(9,1),(9,2),(10,1),
(10,2)` and agree on their canonical hashes and sums.

If one ignores M1 and uses only `q(B)>=3` together with `m_s(L)<=(5-r)^2`, one
obtains a valid weak inequality with multipliers `(5-r)^2`, not divisors. M1
shows that this inequality contains no coloring information. The exact identity
above supersedes it.

## 5. Seven-quotient incidence also has no consumer

A possible repair counts quotient-L incidences rather than distinct pair-tight
Ls. Define

```text
Q_s = sum_L |S(L)| m_s(L).
```

Applying `R_2=5` separately in each of the seven quotients gives `Q_s>=7 C_s`.
But M1 gives `|S(L)|>=1` for every L, so literally summing all 30 Ls in every
copy gives the stronger universal bound

```text
Q_s >= 30 C_s.
```

Thus the seven applications of `R_2=5` cannot improve the trivial incidence
count.

For a proper coloring, only two- or three-color Ls occur. Let `R_s` be the
copy-weighted number of three-color Ls. Since their signatures have size 1 and
two-color Ls have signature size 3,

```text
Q_s = 90 C_s - 2 R_s.
```

The seven-quotient lower bound would only imply `R_s<=(83/2) C_s`, whereas
`R_s<=30 C_s` is immediate from the 30 Ls per copy. The proposed consumer is
therefore weaker than a trivial bound even before any capacity estimate.

In the checked proper 6-square at scale 1, `C_1=4`, `Q_1=330`, and `R_1=15`,
consistent with `330=90*4-2*15`. The seven-quotient rainbow upper bound is 166,
while the trivial upper bound is 120. These numbers illustrate the general
identity; they are not extrapolated finite-search claims.

## 6. Scope and disposition

- Q1: unaffected; its cover lower bound still uses properness and `R_2=5`.
- Q2: unaffected; the stored round-1 witness still refutes universal three-L
  sufficiency.
- Old Q3a: REFUTED by the complete 6-square witness.
- Position-independent block multiplicity: REFUTED by explicit boundary Ls.
- Pair-tight and multiscale incidence identities: PROVED for all four-colorings,
  including improper ones, and hence have no Ramsey upper-bound consumer.
- Seven-quotient incidence averaging: dominated by the trivial signature bound;
  no further computation is justified.
- General multiscale methods using genuinely coloring-dependent local catalogs
  are not refuted by this package.
- `R_3` and `R_4`: no numerical change, and no conditional bound is promoted.

The next candidate must use a non-quotient statistic that distinguishes proper
from improper colorings and must name its upper-bound consumer before a larger
experiment.
