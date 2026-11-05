# R3-R4 exact candidate freeze

Frozen after bounded scouting and before certificate generation or independent
validation.

```text
n = 21992400
t = 36000
w_i = i*(36001-i)
Golomb cap = globally optimized FM3 neighbor cap Q(S)
outer candidate set = every integer c in 650..740
per-span K_d = minimum valid capacity over that outer candidate set
```

The claimant scout reports the exact integer margin

```text
1662886283267098650268325184 > 0.
```

The candidate improves the inherited `22006246` by the exact integer 13846.
This is a **frozen candidate, not yet a certified theorem**.  Global
optimality over outer `c`, `n`, windows, or weight profiles is not claimed.
The neighboring scout point `n=21992200` has negative margin
`-1345765756081380412929801408`; no monotonicity inference is made.
