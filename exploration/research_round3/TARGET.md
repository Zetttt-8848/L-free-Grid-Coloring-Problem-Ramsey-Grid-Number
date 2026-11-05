# Round3 target contract — R3-CP0

Base: the accepted Round2 release and its pinned source/certificate files.
Primary target: move 21 <= R3(L) <=465, ideally determine R3(L).
Orientation: C(x,y;d)={(x,y),(x+d,y),(x+d,y+d)}, d>=1.

The seven routes and ten-section output are governed by MANDATE.txt.
Inherited theorems are inputs, not new results and not to be re-derived.
New numerical claims require independent exact checks; solver timeouts are
UNDECIDED. Any candidate bound triggers a downward iteration and slack audit.
The exact value or global exhaustion must never be inferred from a checkpoint.

Index convention pending initial source audit: H counts possible positions,
so a diagonal of n-d points has span n-d-1 and capacity max{j:H_j<=n-d}.
The mandate's q(n-1-d) notation appears inconsistent with its stated48/46
thresholds. Dependent computations will use the audited convention, with
the discrepancy recorded explicitly before execution.

Allowed writes: research_round3 only, except user-authorized final root archive.
Earlier research folders are frozen read-only mathematical inputs.
