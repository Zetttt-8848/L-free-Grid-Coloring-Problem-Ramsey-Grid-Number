# Anchored addition graph: bounded primary-source inputs (0038)

## Exact target being compared

In the notation of `ANCHORED_FAN_ARC_BUDGET_0037.md`, let \(B\) be a finite positive integer set and orient the addition graph by \(x\to x+y\) whenever \(x,y,x+y\in B\).  The vertex color is the anchored source-cell color \(f(x)=z(x,0)\), inherited from a proper strict-source coloring on \(\{0\}\cup B\).  The desired external input would control the same-color and opposite-color arc counts, monochromatic forward fans, or their missing-support defects.  The exact local relation currently available is
\[
 \sum_x {k_x\choose2}\le e_o+D,
 \qquad \sum_x {k_x\choose2}\ge {e_s^2\over2|B|}-{e_s\over2},
\]
with the definitions and the additional reversed-sum incidence \(R\) in that note.

The search below used two focused query batches and the two primary reads listed; it is a source comparison, not a transfer or proof check.

## 1. Integral sum graphs: matching input pairs, not the same graph

V. Vilfred Kamalappan, Lowell W. Beineke, L. Mary Florida, and Julia K. Abraham, [*A study on edge coloring and edge sum coloring of integral sum graphs*](https://arxiv.org/abs/2203.00409), define the integral sum graph \(G^+(S)\) by putting an undirected edge \(uv\) exactly when \(u+v\in S\).  Their Theorem 2.1 organizes its edges by their sum labels: the nonempty edge-sum classes partition the edge set, and each fixed-sum class is a matching (an independent edge set).

For positive \(B\), each output \(w\in B\) does index a matching of
distinct input pairs \(x+y=w\). However this sum graph is not the
underlying graph of the anchored addition graph. A sum-graph edge
\(\{x,y\}\) with output \(w\) gives two anchored arcs \(x\to w\) and
\(y\to w\); an equal-summand relation supplies one additional anchored
arc. For example, at \(B=\{1,2,3\}\) the loopless sum graph has just
the edge \(\{1,2\}\), while the anchored graph has arcs \(1\to2\),
\(1\to3\), and \(2\to3\). The exact connection is this expansion
of each relation, not a graph isomorphism or an orientation of the
same edge set.

The paper's edge coloring is instead the forced many-valued sum label of an edge.  It does not color the vertices by the inherited two-color function \(f\), and it does not state a cut estimate for \(e_s,e_o\), a monochromatic-forward-fan bound, local Golomb-neighborhood information, or a relation to the defect terms \(D\) and \(R\).  Consequently, the matching partition alone does not provide the required global edge bound.

## 2. Monochromatic Schur-triple optimization: relevant vertex-color language, wrong ambient object

Manuel Kauers and Thomas Wong, [*Exact Lower Bounds for Monochromatic Schur Triples and Generalizations*](https://arxiv.org/abs/1904.01925), study two-colorings of the full interval \([n]\) and give exact lower bounds for monochromatic generalized Schur triples \((x,y,x+ay)\) for \(a=1,2,3,4\).  At \(a=1\), the counted configuration is a monochromatic vertex relation \(f(x)=f(y)=f(x+y)\).

This is closer in language to the anchored model because \(f\) is a vertex coloring, but the hypotheses do not match.  The result assumes the complete interval \([n]\) and measures all monochromatic Schur triples of an arbitrary coloring.  Here \(B\) may be sparse, \(f\) is constrained through a distinct strict-source cell coloring, and the desired quantities distinguish same/opposite endpoint arcs and charge forward fans to missing arithmetic support.  The source has no deletion-defect, local-Sidon, or cut-deficit formulation from which the required \(R+D\) coupling follows.

## Scoped outcome

Among these bounded leads, the sum-graph matching decomposition describes
the input pairs of each addition relation. It does not identify the
anchored graph or its cut. Neither source supplies a theorem controlling
the anchored two-color cut, fan multiplicities, or arithmetic missing-
support defects. This is a scoped mismatch after the stated searches,
not a novelty claim.
