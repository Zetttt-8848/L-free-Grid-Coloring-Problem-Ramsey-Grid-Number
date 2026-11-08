# Geometric joint-capacity contract

Base `654cc044cad3d8ca6079a1931565a6ec44dcf2b5`; date 2026-11-08.
Object: a complete proper three-color square with forbidden positive-step
directed equal-leg L, and its actual main-diagonal/completion color labels.

Target: a new shared-resource bound on total same-color diagonal difference
counts, stronger than adding six independent Golomb cardinality bounds.
Use it in an exact weighted count to exclude side464.

Key distinction: the six ordered color-pair classes live in the SAME
subdiagonal and are disjoint. Counting their minimum positions couples
their feasible spans. This is unrelated to adding local imbalance costs.

Success requires a complete geometry-to-disjoint-Golomb proof, an arbitrary
q-class packing lemma, exact integer contradiction, and independent root
review. The external Golomb lower bounds G(24)>=425 and G(25)>=480 remain
cited computational theorems; they are not rerun locally.

No global novelty claim is made for disjoint Golomb rulers or endpoint
packing. The project consequence and its comparison with the earlier
separate-capacity proof are the claims to establish here.
