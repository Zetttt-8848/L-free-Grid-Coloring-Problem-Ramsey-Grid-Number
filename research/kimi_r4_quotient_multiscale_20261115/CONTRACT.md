# Contract: quotient colors and multiscale subsquares

Date: 2026-11-15. Author: Kimi. Branch:
`kimi/r4-quotient-multiscale-20261115`. Base:
`codex/r4-local-capacity-round3-20261114` at
`14647e607c2525b0cd12081b03899827d306a030`.

## Object and coordinates

An arbitrary proper four-coloring of the full zero-based `[n]^2` square. The
forbidden configurations are exactly `(x,y),(x+d,y),(x+d,y+d)` for integer
`d>0`. A combinatorial 5 by 5 subsquare is selected by five not necessarily
consecutive rows and five not necessarily consecutive columns.

## Information retained

The incumbent capacity chain starts from one main-diagonal color class and
discards most off-diagonal and mixed-color cells. This candidate retains all
seven nontrivial bipartitions of the four-color palette and all combinatorial
5 by 5 subsquares.

## Exact candidate statements

Q1 (lower cover bound). In every proper four-coloring of a full 5 by 5 square,
at least three distinct geometric Ls are needed to witness the monochromatic-L
conclusion of all seven two-color palette quotients.

Q2 (sharpness conjecture to falsify). Three such Ls always suffice.

Q3 (consumer). Multiscale averaging of Q1 yields a constraint strong enough to
enter the existing R_4 contradiction.

## Cheapest discriminating tests and stop conditions

1. Prove Q1 by signature cardinality and validate the implementation on known
   two-color positive and negative instances.
2. Restart the probe from a clean implementation. Sample deterministic proper
   four-colorings and compute exact minimum quotient-cover sizes. A sample
   requiring four Ls refutes Q2. Samples requiring only three do not prove Q2.
3. Derive the exact subsquare-averaging inequality and its asymptotic density.
   Stop Q3 if it supplies only an O(n^-5) density on all geometric Ls with no
   additional capacity interface.

No larger search is authorized after a decisive counterexample or failed
consumer. Timeouts and unsuccessful searches are UNDECIDED.

## Success evidence and non-claims

A numerical R_4 improvement would require a fresh contradiction for every
coloring of a specified full square. Finite samples cannot establish Q2. This
package will explicitly state "No new Ramsey bound" unless that chain closes.
