# Formalization sources

Lean 4.19.0, with mathlib pinned in `lakefile.lean`. Run `lake update`,
`lake exe cache get`, then `lake build`. No Lean or mathlib distribution is vendored.

These sources and historical evidence correspond to the earlier 47-result
manuscript, not an automatic certification of every statement in the current
51-result manuscript. In particular the later six-mark equality classification
requires a new coverage mapping. The external density theorem remains an input;
S21, G9, existential G9, EP10 and H10 remain hypotheses of conditional results.
Read `historical_records/SCOPE.md` for the exact scope. Historical hashes and
paths refer to the original local run, prior to this export and sanitization.
No fresh Lean build is claimed by this import. Check each theorem's assumptions
and printed axiom dependencies before using it as a certified dependency.
