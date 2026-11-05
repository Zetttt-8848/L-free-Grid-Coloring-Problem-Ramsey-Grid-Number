# Cooperative coloring of two forests: source input (0042)

## Exact notion

For graphs (F_1,F_2) on a common vertex set (V), a cooperative coloring is a choice of independent sets (I_i) in (F_i) whose union is (V). Since a cover can be made disjoint by assigning an overlap to either set, this is equivalent to a binary assignment in which the vertices assigned to (i) induce no edge of (F_i).

Thus the proposed mixed-cell problem matches this notion after swapping family labels if necessary: an edge of the (B)-derived forest forbidding two (C)-assignments says that the (C)-part is independent in that forest, and similarly for the other family. The row/column clauses and interval-order restrictions are additional structure not present in the general definition.

## Primary input: two forests do *not* always cooperate

R. Aharoni, E. Berger, M. Chudnovsky, F. Havet, and Z. Jiang, [*Cooperative colorings of trees and of bipartite graphs*](https://arxiv.org/abs/1806.06267), Electronic Journal of Combinatorics 27 (2020), P1.41, defines (m_{mathcal G}(d)) as the least number of graphs from a class (mathcal G), each of maximum degree at most (d), which always has a cooperative coloring. Their Theorem 2 states
[
m_{mathcal P}(2)=3
]
for the class (mathcal P) of paths. In the proof they explicitly begin with a system (T_2) of two paths having no cooperative coloring, and recursively construct larger forest/tree obstructions. Consequently, the unrestricted assertion “every two forests admit a cooperative 2-coloring” is false, already for two path forests.

Their Theorem 3 further gives, for maximum degree (dge2),
[
log_2log_2 dle m_{mathcal T}(d)le(1+o(1))log_{4/3}d,
]
and records (m_{mathcal F}(d)=m_{mathcal T}(d)) for forests when (dge2). These degree-only results do not exploit a common interval order, a monotone root orientation, or roots fixed by internal reflections.

## Adapted edge-coloring translation

P. Bradshaw, [*Cooperative Colorings of Forests*](https://doi.org/10.37236/11461), Electronic Journal of Combinatorics 30 (2023), P1.23, Section 2, records the exact equivalent edge-colored formulation: an adapted coloring of an edge-colored multigraph has no edge whose edge-color equals both endpoint colors. Coloring the edges of each (F_i) by (i) translates cooperative coloring of the family into adapted coloring. This directly fits the two families of “forbid both in this family-color” clauses.

Bradshaw proves that bounded maximum degree alone remains far from a two-family guarantee: for large (d), there are ((1+o(1))log d/loglog d) star forests of maximum degree (d) without a cooperative coloring, and this is asymptotically sharp for star forests. This supplies no theorem for two forests; it reinforces that the desired conclusion must use the special simultaneous interval/row-column structure.

## Scoped consequence

The primary literature supplies a precise negative answer to the bare two-forest question and an exact translation to adapted coloring. No primary result found in this bounded search treats two forests with both families oriented toward a common strictly increasing interval order, with at most one outgoing edge per vertex per family, or with the stated internal-reflection roots and extra row/column constraints. Those are the necessary additional hypotheses for a project-specific lemma; they are not consequences of cooperative forest coloring in general.
