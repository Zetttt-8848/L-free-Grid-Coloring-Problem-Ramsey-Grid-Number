# Colored boundary-resource contract

Base commit: 654cc044cad3d8ca6079a1931565a6ec44dcf2b5.
Date: 2026-11-08. Work package: combinatorial_upper.

Task was initially a lower-bound construction investigation, but the user
steered the team toward new pure mathematical upper-bound counting. Only
prior files had been read; no lower-bound searches were started. This package
therefore contains only the redirected upper-bound work.

Object: full n-square with at most three colors, avoiding precisely
(x,y),(x+d,y),(x+d,y+d), d>0. Aim: control interaction among different
diagonal shifts, beyond treating six Golomb classes independently.

New object: capped same-color matches between two boundary words. The
key universal step charges every 24-mark Golomb class to a distinct actual
boundary pair, retaining its original diagonal color. Adjacent match
layers form a path, creating a new shared-resource inequality.

External inputs: G(24)>=425 and G(25)>=480, in span convention, as
authenticated in the parent checkpoint. Local arithmetic does not replay
those external exhaustive searches.

Success evidence: readable universal counting proofs; exact integer check
of the resulting convolution margin. Small word enumeration is only a
separately labeled finite diagnostic, not a substitute for those proofs.
No SAT solver or large square-coloring search is used.
