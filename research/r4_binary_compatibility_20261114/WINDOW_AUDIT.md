# Window-chain audit, round 1

Pinned project revision: 726998b9da3edd36247a6e2a5c487ba25b0a7297.
This is a source/dependency review plus a numerical reproduction, not Lean
formalization or an exhaustive independent reimplementation of every checker.

## What was established in this session

- The elementary verifier re-proved 608 rank witnesses and reproduced margin
  2727455661705377936113840 at side 21987409.
- The EDGE verifier reproduced the reported margin
  903981917166788568505391154986854794983918064 at side 21947877.
- The original G, H, and p rational matrices were downloaded from commit
  ff5b032fc3745140549777a96a9ec3ba7f8dd954 of dcartermath/sidon-error.
  URLs and SHA-256 hashes are in external_windows/provenance.json.
- Running EDGE with that directory regenerated its correlations and table
  excess, checked all 401 coarse coverage alignments against those matrices,
  checked the seven endpoint coefficients, and passed all 201 inner thresholds,
  565 binary bounds, and 561 disjoint twenty-shift blocks.

## Actual dependency chain

Exact rational tables -> discrete coverage/correlations -> window-derived
Golomb thresholds with correction 52 -> binary capacities with correction 213
-> twenty-shift deficit -> outer contradiction.

The rounded Sidon constants 0.94304 and 0.44466 belong to the older SIDON
route. EDGE does not call that function even though its module is imported.
EDGE also does not need the older twelve-shift exhaustive C certificate.
Its external input is reusable exact data whose required properties are
checked, not an unproved conjecture or a black-box use of the rounded theorem.

Primary provenance reviewed by the read-only audit helper:
[original paper, Appendix A.3](https://arxiv.org/html/2610.36207v1#A3) and
[pinned data README](https://raw.githubusercontent.com/dcartermath/sidon-error/ff5b032fc3745140549777a96a9ec3ba7f8dd954/README.md).

## Mathematical steps reviewed

The read-only review found no defect in replication/interpolation of coverage,
the table norm p+B*alpha, the lambda lower bound in the squared discrepancy,
right-edge indexing, disjointness of the seven samples, threshold rounding,
or the two estimates combined in the twenty-shift recurrence.

At the right edge, if the output length is H=p+200B, reflection gives
S(H-1-q)=S_rev(q-1). Using q instead of q-1 in the capacity bound is an
overestimate and therefore safe. Distinct probabilistic rows add with their
probabilities; disjointness is needed within each row. The parameter condition
p-1>=400B separates the left and right bands.

## Exposition issue, not an identified numerical defect

FOUR_COLOR_EDGE_VARIANCE.md says to take twice the Golomb cap for a binary
source. This must refer to **difference multiplicity**, not source cardinality.
The implementation uses it correctly as gamma in the rectangular-window
inequality. Proposed clarification for a later reviewed edit:

> For a properly two-colored strict source, each positive difference has
> multiplicity at most 2Q(u), by its two Golomb start classes. Apply the
> rectangular-window inequality with gamma=2Q(u) to bound source cardinality.

No shared proof file was edited in this round.

## Limits

The full existing geometry/reduction chain was not independently rewritten,
nor were all implementation lines audited independently. The successful runs
use the author's checker. They establish more than cached-data consistency,
but do not justify a claim of complete independent formal certification.
Claude's review of new contributions and integration remains required.
