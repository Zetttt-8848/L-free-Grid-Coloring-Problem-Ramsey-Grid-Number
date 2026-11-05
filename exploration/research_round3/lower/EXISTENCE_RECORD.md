# Existence Bounds Record

## Scope

- Formal property: a three-coloring `chi:[n]^2->{1,2,3}` has no monochromatic
  `((x,y),(x+d,y),(x+d,y+d))` with integer `d>=1` and all cells in `[n]^2`.
- Object universe and size parameter: all labeled three-colorings of the full
  `n` by `n` grid; colors are labeled for certificates, with color permutation
  used only as proved solver symmetry.
- Extremal quantity: `R_3(L)`, the least `n` for which every such coloring has
  a monochromatic directed equal-arm corner.
- Bound monotonicity: restriction of a valid coloring to the leading `m` by
  `m` subgrid is valid, so an `n` witness yields witnesses for every `m<=n`.
- Record scope: project-local best known, with inherited certified endpoints.
- Last audited date: 2026-09-10.

## Current bounds

| Side | Certified bound | Exact meaning | Last movement date | Route | Evidence path | Verification |
|---|---:|---|---|---|---|---|
| Construction lower bound | 21 | an inherited corner-free coloring exists at side 20 | inherited | prior campaign | inherited Round-2 release | inherited independent direct check of all 2470 corners |
| Impossibility upper bound | 465 | every side-465 three-coloring contains a corner | inherited | weighted diagonal argument | inherited Round-2 release | inherited theorem audit |

- Exact integer gap (`465-21`): `444`.
- Exact endpoint ratio (`465/21`): `155/7`.
- Status: open.

## Movement history

Append a row only after the cited certificate verifies. Do not delete earlier rows.

| Date | Side | Previous bound | New bound | Route | Certificate/evidence | Independent verification |
|---|---|---:|---:|---|---|---|

## Exact-value trigger

If the certified bounds meet, stop exploratory search, mark the status
`two-sided audit required`, notify the orchestrator, and verify both
certificates before changing the status to `exact value proved`.
