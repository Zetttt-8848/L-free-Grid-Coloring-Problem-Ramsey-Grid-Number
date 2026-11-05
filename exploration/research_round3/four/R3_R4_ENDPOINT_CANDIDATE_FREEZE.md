# R3-R4 endpoint-corrected candidate freeze

Frozen after endpoint scouting and before certificate generation or
independent validation.

```text
n = 21991500
t = 36000
w_i = i*(36001-i)
Golomb Q(S) = global FM3 optimum with the distinctness endpoint correction
V_{d,h} = 2*Q(n-d-1-h)
outer candidate set = every integer c in 650..760
per-span K_d = minimum valid endpoint-corrected capacity over that set
```

The claimant scout gives the exact integer margin

```text
3572064084430380575832634176 > 0.
```

The exact improvement over `22006246` is 14746; the improvement over the
profile-only frozen candidate `21992400` is 900.  This is a **frozen
candidate, not yet a certified theorem**.  No global optimum over `c`, `n`,
windows, or weights is claimed.
