# Forcing-graph core discovery (0045)

This one raw graph invariant uses the saved unrestricted 120-cell coloring in
**FULL_FOUR_CUBE_DISCOVERY_0045.json**. It does not run a coloring solver and
does not recheck properness.

For every actual positive equal-step corner whose two parallel endpoint cells
have the same saved color, the graph has its outer completion as a vertex
joined to each of those endpoint cells. Repeated physical pairs are collapsed,
so the result is a simple graph on all 120 strict cells.

The adjacent JSON records the exact active-corner count, simple-edge count,
minimum-degree peeling order and removal-degree histogram, and separately
computed core number for every vertex. The separate core calculation matters:
a removal degree in a minimum-degree peeling is not automatically that
vertex's core number.

This is a one-model discovery metric for the proposed universal
9-degeneracy question. It is not a colorability, Ramsey, or universal graph
claim.

