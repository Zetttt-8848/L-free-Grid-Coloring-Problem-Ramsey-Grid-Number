# R3-SETUP frozen predictions (pre-execution)

Frozen before any claimant or checker program is run.  Base contract:
`R3-CP0`.  This setup route treats the accepted Round-2 theorem and its
position-count convention as inherited inputs and does not rederive them.

1. **Indexing.**  I predict the accepted convention is the only consistent
   one: a fiber with `n-d` possible integer positions has span `n-d-1`, so
   its Golomb order is `q(n-d)`.  The Round-3 mandate's literal
   `q(n-1-d)` will fail its own `n=465,d=39` threshold by one Golomb order.
2. **Uniform capacities at `L=463`.**  I predict exact best bounds
   `159` for `V=48` (witness parameter `c=7`), `154` for `V=45`
   (`c=8`), and `156` for `V=46` (expected best parameter `c=8`).
3. **Partial low-distance profile at `n=464`.**  I predict the stated
   `V_d=45` for `d<=27`, inherited `2q(n-d)` elsewhere, excludes a set of
   size `155` at `c=8`, with `H=1204`, one-sided minimum `16713`, and
   doubled comparison `33426>33336`.  Replacing `45` by `46` through
   distance `27` will give `H=1204`, minimum `16362`, and
   `32724<33336`, so it will not exclude size `155`.
4. **Distance sensitivity.**  I predict the `c=8` minimum under the
   45-profile exhausts 26 full distance classes and only part of distance
   27.  Thus the stated band through 27 is sufficient but is probably not
   a minimal componentwise hypothesis.  Starting from cap 46 through 27,
   I predict fewer than 18 distinct one-unit cap shaves cannot cross the
   strict threshold if each distance may be shaved by at most one; the
   earliest 18 should cross it.  If reductions may concentrate at one
   distance, I predict 12 total units at distance 1 suffice and 11 do not.
5. **Downward ladder.**  I predict the same 45-profile closes `n=463`
   (best advertised witness `c=7`), does not close `n=462`, and likely
   closes exactly `n=463,464,465` within the requested range `450..465`.
   The exact best capacity at every rung is left to the independent run.
6. **Dual bracket.**  I predict only the exact endpoint
   `sup S_464/a_0 <= -16` is certified from the inherited rational dual.
   Without a literal feasible vector and exact score, the decimal
   `-17.29` is heuristic and cannot certify the other endpoint of a
   rigorous bracket.

Honesty label: **CONJECTURE / frozen quantitative prediction** until the
separate claimant and checker calculations complete.
