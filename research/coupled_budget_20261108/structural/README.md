# Rigid source, cancellation, and valid overlap accounting

Base `df6e35cfff68580dc78aa91bc35d4c6399a6464a`; date 2026-11-08.
The numerical upper-bound audit is in [UPPER_PROOF_REVIEW.md](UPPER_PROOF_REVIEW.md).
This document concerns a separate structural experiment and does not prove
an additional Ramsey bound.

## Exact finite result

Let `B={0,1,2,3,4,6,7,9,10}` and use its **complete** strict source
`V(B)={(v,u):u<v, u,v in B}`. The forbidden triple is
`((x,y),(x+h,y),(x+h,y+h))`, `h>0`.

There are 36 cells, 60 physical triples, and exactly **four** proper binary
colorings. Up to global color exchange, the two colorings differ only at
cell `(3,1)`. Every other cell's color relative to `(1,0)` is forced.
In particular, `(9,1)` and `(10,2)`, the two cells of difference 8, always
have the same color.

For signs `z=1-2c`, write `s_d=sum_(x-y=d) z(x,y)`,
`Phi=sum_d s_d^2`, and `P=sum_d (r_d mod 2)`. Every proper coloring of
this source has `Phi=8`, whereas `P=4`. The only excess occurs at
difference 8. Thus no choice of a proper coloring makes every fiber
simultaneously attain its parity minimum. This refutes that assertion for
arbitrary full strict sources, without any fixed exterior.

[balance_certificate.json](balance_certificate.json) lists all four
colorings. [balance_branch_proof.json](balance_branch_proof.json) covers
the entire `2^36` assignment domain, using the safe global-complement
symmetry to pin the first cell to zero. It contains 93 branching nodes,
45 contradictory leaves, two successful pinned leaves, and 406 justified
NAE unit propagations. [check_branch_proof.py](check_branch_proof.py)
reconstructs the physical triples independently and checks every
propagation, conflict, both branches, and complete leaf. It does not
search or invoke SAT. Its result is
[balance_proof_check.json](balance_proof_check.json).

## Cancellation in a larger full source

The stronger local obstruction still cannot be summed as a global excess.
Set `A=B union {14}`. The explicit 45-cell coloring in
[extension_discovery.json](extension_discovery.json) is proper and has

| Restriction | Phi | Parity floor |
|---|---:|---:|
| V(B) | 8 | 4 |
| V(A) | 7 | 7 |

At difference 8 the two B cells have color 0, while the added cell `(14,6)`
has color 1. Thus the signed fiber sum changes from 2 to 1. Every whole
fiber attains its parity floor in this full coloring, proving that its
global potential is minimal. The independent physical triple checker
[verify_extension.py](verify_extension.py) proves the displayed claims.

Consequently `Phi_A-P_A >= Phi_B-P_B` is false even for an intrinsically
frustrated B whose every proper coloring has positive local excess.
This strengthens the need to keep outside contributions, rather than
repairing local balance or counting local obstructions without them.

## Two valid general lemmas

The following are elementary constraints that remain sound under arbitrary
overlap. They are useful representations, not new general source budgets.

**Equality-component lower bound.** Suppose a graph on the cells of a
whole fiber joins pairs proved to have equal colors in every allowed
coloring. Let its connected component sizes be `w_1,...,w_t`, including
isolated vertices. Then

`s_d^2 >= beta_d := min_(epsilon_i in {-1,1}) (sum_i epsilon_i*w_i)^2`.

Indeed each component is monochromatic, so the actual fiber sum is one
of these signed sums. No assertion is made that every sign choice extends
to a proper source coloring; minimizing over a superset is a valid lower
bound. In particular `beta_d >= r_d mod 2`. Equality relations remain
valid when a certified small source is embedded by `a -> t+h*a`, `h>0`,
in any larger source: properness restricts to that smaller source. The
other cells of each whole fiber must nevertheless be included.

For B at d=8 the component sizes are `[2]`, so beta is 4. For its extension
A the sizes are `[2,1]`, so beta is 1, exactly capturing the cancellation.
The 35 forced cells also supply direct equal/opposite-color constraints
for search on any affine copy of B. This is a safe reusable consequence
of the finite certificate.

**Fractional packing of whole-fiber certificates.** Put
`q_d=s_d^2-(r_d mod 2)`, which is nonnegative. Suppose valid inequalities
for the **same full source and allowed coloring domain** are

`sum_d a_(j,d)*q_d >= delta_j`, with `a_(j,d)>=0`.

For any nonnegative weights lambda satisfying
`sum_j lambda_j*a_(j,d)<=1` for every d, one has

`Phi >= P + sum_j lambda_j*delta_j`.

Proof: multiply the certificate inequalities by lambda and sum. The left
side is at most `sum_d q_d` by nonnegativity and the per-fiber capacity.
This also allows certificates with overlapping difference sets, with no
double counting. A simpler special case has `a_(j,d)` equal to the
indicator of a certified set of differences. Equality components produce
singleton certificates `q_d>=beta_d-(r_d mod 2)`.

Certificates for a subsource's local squared sums are not certificates
for these whole-fiber quantities. The explicit A extension shows why that
replacement would invalidate the lemma's hypotheses.

## Exact bridge and first missing step

Let `M=sum_d r_d` and `T=sum_d binom(r_d,2)`. Define E to count ordered
same-color pairs of distinct cells in the same fiber. Then expansion gives

`2*T = M + 2*E - Phi`.

If the fractional certificate yields excess B0, it follows only that
`2*T <= M+2*E-P-B0`. To obtain an upper bound on T, one still needs an
independent upper bound on E that holds for the **same** permitted coloring.
Forced equalities can increase E as well as Phi, and the displayed
identity is independent of coloring once A is fixed. This work supplies
no such upper bound and therefore no universal `T/M` or `M/span` bound.

The first unresolved implication is a uniform joint control of
`2*E-Phi`, using source geometry rather than only local frustration. The
positive lemmas above specify sound inputs to such a program; they do not
complete it. Two-color equality/complement is essential to this version;
three-color sources would require new constraints.

## Discovery correction and evidence limits

The first raw discovery program had an auxiliary-variable allocation bug:
after a trivial cardinality encoding with zero clauses, assigning
`top=encoding.nv` could decrease the variable-ID high-water mark to zero.
Later auxiliary variables could then collide with source variables.
Its initial raw UNSAT for `{0,1,2,5,6,9,10}` is **INVALIDATED: IMPLEMENTATION
ERROR**, not an obstruction and not an unproved mathematical conjecture.
That raw status is excluded from all claims here.

An independent exhaustive check of all `2^21` assignments of that seven-mark
source found 6558 proper colorings, minimum Phi 5 equal to parity 5, and
1088 minimizers. [frustration_results.json](frustration_results.json) is
retained as a regression record of the false positive. Both cardinality
encodings now update `top=max(top,encoding.nv)`. The corrected bounded
scan checked 808 candidate mark sets before finding B; negative SAT
returns in that scan are discovery observations, not nonexistence proofs.

The separated four-cube was also tested informally and admitted a parity-
balanced coloring; it was not a useful obstruction and is not a certified
result of this package. No negative result is inferred from that probe.

Run the following from this directory:

```text
python scan_balance.py
python enumerate_frustration.py
python certify_balance.py
python check_branch_proof.py
python discover_extension.py
python verify_extension.py
python audit_joint_bound.py
python audit_convolution.py
```

Only discovery uses `python-sat`; all displayed finite verification and
arithmetic scripts use Python's standard library. Discovery, exact finite
classification, written general lemmas, external mathematical inputs,
and the unresolved global budget are separate evidence classes.

The six verification programs were rerun together through the Mathbox
bounded runner. [verification_001/manifest.json](verification_001/manifest.json)
has `run.status=completed`, before/after input hashes, exact command,
Python version, elapsed time, and hashed result snapshots. Its schema and
current input/output hashes passed the Mathbox manifest validator. The
finite result assertions and their limitations are in
[computation_contract.json](computation_contract.json); successful process
execution does not itself prove the general lemmas.
