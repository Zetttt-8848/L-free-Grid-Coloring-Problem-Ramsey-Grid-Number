# Kernel and compatibility research contract

Date: 2026-11-08. Base: `654cc044cad3d8ca6079a1931565a6ec44dcf2b5`
(PR5, open at start). Adopted project interval: `21 <= R3 <= 465`.
Geometry: `(x,y),(x+d,y),(x+d,y+d)`, integer d>0, full square,
at most three colors. Preserve the distinction between square colorings,
two-colored strict sources and one-dimensional diagonal relaxations.

Target as clarified by the user: invent a new counting mechanism that
improves the mathematical upper bound below465. The user explicitly
prioritizes innovation in counting over SAT-based lower-bound search or
proof exposition. No new lower search was started before this steering.
Computations may discover or check an inequality; the central deliverable
is its mathematical counting argument and numerical consequence.

Work packages:

1. `kernel_upper/`: direct positive-semidefinite or Fourier-dual treatment
   of three-class correlations, signed kernels and exact certificate
   extraction. Floating status alone is UNDECIDED.
2. `combinatorial_upper/`: count the shared colored boundary pairs across
   different difference fibers, beyond independently optimized capacities.
3. `geometry/`: derive genuinely additional cross-fiber constraints or
   exact small forbidden motifs, then test their global counting bridge.
4. Coordinator: compare positioned windows and summed correlations,
   independently audit load-bearing proofs, reconcile all statuses, and
   publish the work and code on a new branch.

The preceding one-defect candidate is certified unrepairable within10
changes. Local source frustration may cancel in a larger fiber. Those
facts must inform new hypotheses. The465 proof is restored historical
work, while the466 endpoint lemma is a separate weaker proof.

Every route records actual inputs, commands, deterministic certificates
where possible, finite domains, hashes, negative and interrupted runs,
and the first unresolved implication. No new global originality claim
without a source comparison. No main-manuscript changes until justified.
