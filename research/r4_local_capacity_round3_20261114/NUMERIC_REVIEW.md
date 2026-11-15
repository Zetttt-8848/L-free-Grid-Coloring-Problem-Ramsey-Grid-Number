# Independent review of the new numerical integration

Reviewer: internal theory/arithmetic reviewer, separate from the discovery author.
This review does not claim external peer review or Lean formalization.

## Mathematical integration

No defect was found in the following reviewed steps:

- The finite encoding uses one mark bit per position, one binary color per
  potential strict-source cell, both nonmonochromatic clauses for every
  physical directed L, and guards by all distinct marks used by that L.
  The cardinality recurrence is exactly z iff p or (a and q). Unused cells
  are free, and no unjustified geometric symmetry constraint is introduced.
- Exclusions of eight marks in eight positions, ten in twelve, twelve in
  sixteen, and fifteen in twenty imply minimum spans 8, 12, 16, and 20.
  The proof objects for these exclusions require separate replay; this review
  of the encoding does not replace proof checking.
- The rank recurrence uses only already certified smaller-cardinality spans.
  At tested span L the multiplicity profile is Q(L-h)+Q(L-h-1), with Q on
  spans and Q(negative)=0. Ordering distinct minima justifies the second term.
  The least available difference cost is a lower bound for every selected
  rank-neighbor difference multiset. Each rejected integer span has a strict
  inequality witness, or insufficient total difference capacity.
- Hereditary restriction makes every propagated local cardinality bound valid
  for every short interval in the large binary source. Propagation also
  improves the cap used at the whole coarse-bin length 1820; the benefit is
  not limited to the initially certified small intervals.
- Lowering either local cap in the endpoint discrepancy expression preserves
  its direction. The seven endpoint samples remain disjoint within each row,
  and the existing parameter domain separates the two ends. The lower bound
  on lambda remains valid. The discrepancy correction may be rational;
  no step requires rounding it down to an integer.
- The updated correction must be inserted into the binary witness inequality
  with its actual p-dependent difference profile. The consumer does this,
  rather than assuming each extra unit of correction automatically shifts a
  binary capacity interval by one position.
- The appended equal-cap row supplies hereditary coverage. It is not treated
  as a capacity decrease. Every interval row, including this sentinel row,
  is rechecked. The twenty-shift losses are charged only on disjoint blocks.

## Independent numerical implementation

`verify_numeric.py` imports no project research functions. It checks every
recorded rank lower bound by excluding each intervening integer span,
reconstructs the endpoint discrepancy, verifies the 201 inner thresholds,
and checks every new binary interval witness.

For binary witness energy it integrates the piecewise-constant multiplicity
profile against piecewise-linear correlations, rather than using the author's
constant baseline minus correlation tails. For the outer weights it expands
the quartic polynomial and sums integer powers, rather than interpolating
from initial correlations. It charges the twelve capacity ranks by interval
integration, rather than looking them up separately at every outer lag.
The twenty-shift recurrence is reconstructed by cardinality layers.

The reviewer wrote this checker without executing numerical jobs. Successful
execution must be established by the coordinating agent and recorded with
the delivered results. The checker also verifies the reported arithmetic at
the preceding tested side; a negative margin there is not a lower bound or
an optimality claim.

## Inherited scope and limits

The reviewed mathematical consumer is the existing chain documented in
FOUR_COLOR.md, FOUR_COLOR_WINDOW.md, FOUR_COLOR_DOUBLE_WINDOW.md,
FOUR_COLOR_EDGE_VARIANCE.md, and FOUR_COLOR_TWENTY.md under
`research/boundary_certificates_20261115/`.

The checker reads the existing rational correlation and endpoint tables.
Their agreement with the original rational matrices and all coarse coverage
checks must be retained from a separately documented replay. This independent
implementation does not regenerate those source tables, formally verify the
discrete coverage theorem, or replace independent checking of the finite seed
refutations. Its result is independent verification of the new numerical
integration, subject to those explicitly identified inputs.
