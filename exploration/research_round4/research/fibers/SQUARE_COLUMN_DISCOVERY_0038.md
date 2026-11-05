# Square column graph discovery (0038)

The accompanying script examines only the ordinary anchored addition/column graph \(C_a\) for square roots through 300.  An edge between roots \(b<c\) means \(c^2-b^2+a\) is also a selected square.  It runs ordinary BFS odd-cycle detection and stops at the first non-bipartite anchor among \(a=1,4,9\).

The JSON output is bounded discovery data only.  It makes no source-coloring or SAT call and does not assert that an odd cycle obstructs every two-color strict-source assignment.
