# A proper thirteen-triangle coloring with fourteen rainbows

Root construction, continuing checkpoint R4-RESEARCH-0012. This refutes F13. It does not improve a full-grid Ramsey bound or assert that fourteen is the local minimum.

## Explicit coloring

Let T_13={(v,u):0<=u<v<13}. A directed corner is ((v,u),(v+d,u),(v+d,u+d)), with d>=1 and v+d<13. Assign colors in F3 by the following row words, whose positions u start at zero.

| v | c(v,0)...c(v,v-1) |
|---:|:---|
| 1 | `1` |
| 2 | `00` |
| 3 | `020` |
| 4 | `2022` |
| 5 | `21021` |
| 6 | `121000` |
| 7 | `2000202` |
| 8 | `21110021` |
| 9 | `121212210` |
| 10 | `1021221102` |
| 11 | `01122022111` |
| 12 | `010120120121` |

## Complete corner-sum calculation

Put g_d(v,u)=c(v,u)+c(v+d,u)+c(v+d,u+d) in F3. Three colors sum to zero exactly when they are monochromatic or all distinct: a repeated pair a,a and a different b has sum b-a, which is nonzero. Thus it suffices to identify every zero in the following complete table and show that its three colors are distinct.

For each step d, the successive slash-separated words are g_d(v,0)...g_d(v,v-1) for v=1,...,12-d. Every permitted corner appears once, because its step d and base (v,u) are unique. Each word is the componentwise sum modulo three of the corresponding three substrings of the displayed coloring.

| d | all corner sums by base row v | number of zeros |
|---:|:---|---:|
| 1 | `1 / 22 / 211 / 2112 / 21121 / 021222 / 2221222 / 21110122 / 211222122 / 2222112121 / 12221121211` | 2 |
| 2 | `1 / 12 / 221 / 1202 / 11222 / 112121 / 1121201 / 22210001 / 221121212 / 1212212121` | 5 |
| 3 | `2 / 12 / 111 / 1221 / 22122 / 121122 / 1212222 / 11221121 / 221122121` | 0 |
| 4 | `1 / 12 / 122 / 1121 / 12022 / 111221 / 1101212 / 12212121` | 2 |
| 5 | `2 / 22 / 222 / 2111 / 22002 / 121001 / 2221221` | 4 |
| 6 | `2 / 12 / 021 / 1112 / 11221 / 221211` | 1 |
| 7 | `1 / 22 / 221 / 1212 / 12121` | 0 |
| 8 | `2 / 12 / 112 / 2211` | 0 |
| 9 | `1 / 12 / 121` | 0 |
| 10 | `2 / 22` | 0 |
| 11 | `2` | 0 |

The zeros and their actual colors, in corner order, are:

| base (v,u) | step d | three colors |
|:---|---:|:---|
| (3, 0) | 6 | (0, 1, 2) |
| (4, 2) | 2 | (2, 1, 0) |
| (5, 2) | 4 | (0, 1, 2) |
| (5, 2) | 5 | (0, 2, 1) |
| (5, 3) | 5 | (2, 1, 0) |
| (6, 0) | 1 | (1, 2, 0) |
| (6, 3) | 5 | (0, 2, 1) |
| (6, 4) | 5 | (0, 2, 1) |
| (7, 2) | 4 | (0, 1, 2) |
| (7, 5) | 2 | (0, 2, 1) |
| (8, 4) | 1 | (0, 1, 2) |
| (8, 4) | 2 | (0, 2, 1) |
| (8, 5) | 2 | (0, 2, 1) |
| (8, 6) | 2 | (2, 1, 0) |

Every listed triple has colors 0,1,2 in some order. The sum table contains exactly 2+5+0+2+4+1+0+0+0+0+0=14 zeros, all included in the second table. Consequently no corner is monochromatic, and exactly fourteen corners are rainbow. This is a direct finite construction proof; no solver optimality or negative search output is used.

## How the affine freedom produced the construction

The initial array had fourteen zero-sum corners, but twelve were monochromatic. Adding v-2u-1 in F3 to every cell preserves all corner sums, since its sum on a directed corner is 3(v-2u-1)=0. The resulting lift has one monochromatic corner, ((4,2),(10,2),(10,8)), and thirteen rainbow corners. The final coloring changes only cell (10,8) from 2 to 0.

The complete list of corners containing this cell is below. It follows directly by putting (10,8) in each of the three corner positions: as the first vertex there are steps 1,2; as the middle vertex the only allowed step is 1; as the last vertex there are steps 1 through 8. These eleven corners are distinct.

| base (v,u) | d | colors before repair | colors after repair |
|:---|---:|:---|:---|
| (2, 0) | 8 | 012 | 010 |
| (3, 1) | 7 | 202 | 200 |
| (4, 2) | 6 | 222 | 220 |
| (5, 3) | 5 | 212 | 210 |
| (6, 4) | 4 | 022 | 020 |
| (7, 5) | 3 | 022 | 020 |
| (8, 6) | 2 | 212 | 210 |
| (9, 7) | 1 | 112 | 110 |
| (9, 8) | 1 | 022 | 002 |
| (10, 8) | 1 | 211 | 011 |
| (10, 8) | 2 | 202 | 002 |

The repair removes the sole monochromatic corner, removes one rainbow, and creates two rainbows. Every other corner is unchanged. The complete sum table above independently specifies the final object and its mathematical properties; the discovery route is not a proof premise.

## Consequences for the current amplification route

F13 claimed that every proper three-coloring of T_13 has at least seventeen rainbow corners. The displayed proper coloring has fourteen, so F13 is false. More generally, any uniform lower count rho for all proper T_13 colorings must satisfy rho<=14.

LARGER_TRIANGLE_AMPLIFICATION.md proves that the uniform family of all allowed T_13 homothetic embeddings into T_464 has copy count 1455419 and exact maximum corner multiplicity 223. The proper host rainbow budget is binom(464,2)=107416. Even the largest local count compatible with this construction gives

    14 * 1455419 = 20375866
                  < 23953768 = 223 * 107416.

The gap is 3577902 in the wrong direction. Therefore this uniform whole-corner scalar amplification cannot prove R3<=464, even with the exact boundary-sensitive multiplicity. Different local weights, embedding weights, or inequalities coupled to the host coloring are outside this conclusion.

The earlier fixed-class theorem remains valid: FIXED_CLASS_PACKING_INSTANCE.md holds one particular color-2 set fixed and proves its minimum is 21. The new coloring has a different class, for example at (3,1), which has color 2 here but color 0 in that seed. It therefore neither contradicts nor extends that fixed-class theorem.

The source-size target S_11 for R4 remains open and is unaffected by this local construction. The actual full-grid bounds remain 21<=R3<=465 and R4<=21991300.
