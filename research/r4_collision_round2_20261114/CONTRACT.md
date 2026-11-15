# Round 2: binary collision geometry

Base: fb33871768bd94fd8e88452ac62ac2789eb0e882.
The owner authorized this round before Claude's completion and authorized
pushing progress and results. This supersedes the previous wait-for-integration
boundary; it does not change the level-based division of work.

Codex retains binary-source lane A. External Claude retains ternary lane B.
One computational worker and 1 GiB are reserved for Codex. Internal helpers
perform theory/review only. Each computational pilot is bounded by 15 minutes.

## Candidate R2-C1

Limitation: round 1 bounds collisions by cardinality, which is too large for
the weighted consumer. The reflected-Golomb family rules out an absolute cap.

Mechanism: retain the positions and colors of both arms requesting one cell;
study the extra restrictions on its symmetric set of intermediate marks.

Statement to test: in a proper binary strict source, at target (u+t,u), can
the request offsets be partitioned into two Golomb sets? This would give
m <= 2 Q(t-1 positions). This is a candidate, not an established lemma.

Cheapest test: coordinate proof attempt and exact small-source enumeration,
including every admissible coloring in the explicitly recorded finite domain.
A checked proper source whose offset set has no two-Golomb partition refutes
the statement; a search with no counterexample proves only its finite coverage.

Consequence: a span-based collision bound could enter the weighted Cauchy
interface from round 1. Demand and consumer strength must still be established.
Even the proposed square-root cap may reproduce the existing exponent; test
this before claiming an improvement.

## Parallel theory route R2-C2

Derive an exact color-independent request/energy identity or deficit inequality
that retains shared cells. Test whether it follows already from per-fiber
Golomb caps. A result implied by existing inequalities is not a new mechanism.
Any near-extremality premise must be quantitative and justified by the consumer.

Classification: modified collision approach. No worldwide novelty claim.
Only the binary level of the four-color recursion is in scope. No new bound
is assumed. Keep current certificate files and the shared manuscript unchanged.

## Stop and delivery

Stop a disproved candidate immediately. Deliver a proof or an explicit
counterexample, actual finite coverage, exact reproduction commands, a review,
and the remaining consumer gap. Push the completed package on this round's
branch. Integration with external Claude remains pending its actual report.
