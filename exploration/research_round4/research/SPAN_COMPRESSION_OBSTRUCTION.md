# A counterexample to additive compression of the two diagonal spans

Base R4-RESEARCH-0002. Root research discriminator. The proposed route was to prove

G(|B|)+G(|C|)<=span(B union C)

for every two-color corner-free weak triangle W(B union C), where B,C are its diagonal color classes and G(m) is the minimum span of an m-mark Golomb ruler. Such a theorem would sharply improve the existing separate-ruler caps. It is false.

Take B={0,4,6,7}, C={1,8,9,11}, S=B union C. The following table gives the entire coloring of W(S), with 0 blue, 1 green and a dash outside the weak triangle. Rows and columns use their actual integer labels.

| row / column | 0 | 1 | 4 | 6 | 7 | 8 | 9 | 11 |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | - | - | - | - | - | - | - |
| 1 | 0 | 1 | - | - | - | - | - | - |
| 4 | 1 | 1 | 0 | - | - | - | - | - |
| 6 | 1 | 1 | 1 | 0 | - | - | - | - |
| 7 | 1 | 0 | 1 | 1 | 0 | - | - | - |
| 8 | 1 | 0 | 0 | 0 | 0 | 1 | - | - |
| 9 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | - |
| 11 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 |

Here is a direct proof that this coloring avoids all corners. Every corner has a pair of distinct endpoints on one slope-one diagonal, followed by their unique completion. If those endpoint colors differ, that corner is already nonmonochromatic. For diagonal offset zero, the equal-color pairs are the pairs in B and in C; all cells of T(B) in the table are 1 and all cells of T(C) are 0, as required.

For positive offsets, all equal-color endpoint pairs and their completion cells are covered by the following table. An entry in the middle column lists starts of cells (u+d,u) of the indicated color; only groups of size at least two are listed. Taking every pair of starts in that group gives exactly the completion cells in the last column, all of the opposite color in the full table.

| offset d | equal-color group of starts | completions, with opposite color |
|---|---|---|
| 1 | color 0: {0,7,8} | (8,0),(9,0),(9,7), all 1 |
| 2 | color 0: {6,9} | (11,6), color 1 |
| 2 | color 1: {4,7} | (9,4), color 0 |
| 3 | color 1: {1,4,6} | (7,1),(9,1),(9,4), all 0 |
| 4 | color 0: {4,7} | (11,4), color 1 |
| 5 | color 1: {1,6} | (11,1), color 0 |
| 7 | color 1: {0,4} | (11,0), color 0 |

At offsets 6 and 8 there are two endpoints of different colors. At offsets 9,10,11 there is only one endpoint. These statements follow by listing the pairs of S at each of those differences. There are no greater offsets. Thus every possible monochromatic endpoint pair has an opposite-color completion, proving corner-freeness.

Finally G(4)=6: four marks have six distinct positive differences, so their span is at least six; {0,1,4,6} attains six. Hence G(|B|)+G(|C|)=12, but span(S)=11. This disproves the proposed inequality by a complete explicit construction. It does not disprove every bound with an error term, nor an asymptotic leading constant smaller than the separate-ruler estimate. No new upper bound is inferred from this counterexample.

## Subtracting the smaller color-class size does not repair the inequality

The weaker proposal G(|B|)+G(|C|)-min(|B|,|C|)<=span(S) is also false. Take

    B={0,1,7,10,15}, C={2,4,8,11,16}.

Here is an entire coloring of W(S), using the same color convention. In each row the listed colors correspond, in order, to the elements of S not exceeding its row label; S is ordered as 0,1,2,4,7,8,10,11,15,16.

| row | colors in increasing column order |
|---|---|
| 0 | 0 |
| 1 | 1,0 |
| 2 | 0,1,1 |
| 4 | 1,0,0,1 |
| 7 | 1,1,1,1,0 |
| 8 | 0,0,0,0,1,1 |
| 10 | 1,1,1,0,1,1,0 |
| 11 | 0,1,0,0,1,0,0,1 |
| 15 | 1,1,0,1,1,0,1,0,0 |
| 16 | 1,0,0,0,1,0,1,0,0,1 |

At offset zero, all pair completions from B have color 1, and all from C have color 0. At positive offsets, the following are exactly the groups with at least two endpoints of the same color. Each pair in a group has one of the listed completions, whose color is opposite to the group color in the full table.

| offset | group color | starts | completions |
|---|---|---|---|
| 1 | 0 | 10,15 | (16,10) |
| 1 | 1 | 0,1,7 | (2,0),(8,0),(8,1) |
| 2 | 0 | 0,2 | (4,0) |
| 3 | 0 | 1,8 | (11,1) |
| 3 | 1 | 4,7 | (10,4) |
| 4 | 0 | 4,11 | (15,4) |
| 4 | 1 | 0,7 | (11,0) |
| 5 | 1 | 2,10 | (15,2) |
| 6 | 0 | 2,4 | (10,2) |
| 6 | 1 | 1,10 | (16,1) |
| 7 | 0 | 1,4,8 | (11,1),(15,1),(15,4) |
| 8 | 0 | 0,8 | (16,0) |
| 8 | 1 | 2,7 | (15,2) |
| 9 | 1 | 1,7 | (16,1) |
| 10 | 1 | 0,1 | (11,0) |

At offsets 11 through 16 each color occurs at most once, as follows by taking the differences of the ten listed source marks. There are no larger offsets. The displayed groups therefore cover every possible monochromatic endpoint pair and prove that the coloring avoids every corner.

For completeness, G(5)=11 has a short proof. A five-mark ruler of span at most ten would have its ten distinct positive differences equal to 1,...,10. If e marks are even, the number of odd differences is e(5-e). This is one of 0,4,6, whereas the list 1,...,10 has five odd entries, a contradiction. The ruler {0,1,4,9,11} has ten distinct positive differences and span eleven, proving equality. Thus the proposed left side is 11+11-5=17, while this example has span 16.

This rules out that specific linear correction. It is not a proof that all asymptotic joint-packing improvements fail. A further twelve-mark construction was found in the bounded discovery at span 27, but no additional theorem here relies on it.
