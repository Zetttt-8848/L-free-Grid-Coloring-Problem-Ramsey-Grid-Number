# Full-source optimality is incompatible with three-dimensional block balancing: external field counterexamples and precise budgeting

Date: 2026-11-08. Basic submission`080822bb1d434b164a1f42ea159d0bf148396b71`.

**Results of this round:** There exists a complete strict source of normal dichromatism, which has reached the absolute minimum of the total source potential function, but its three-dimensional block is unbalanced. A legal color change of a single cell within a block can balance the block, but strictly increases the total source potential. When the external coloring is fixed, the minimum potential of the whole source is **9**, and the minimum potential after the block is required to be balanced is **13**; these two precise values ​​are jointly proved by the parity lower bound, the complete witness and the corner-by-corner verification, and do not rely on traversing all the colorings.

This eliminates the one-step reasoning of "selecting the normal coloring with the smallest global size can eliminate the local imbalance of each three-dimensional block." There is no path blocking in this example: the equilibrium final state can be reached in one step; the obstacle is the conflict between the local goal and the global goal. It complements [PR 3](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/pull/3)Fixed border path obstacles, no override results there.

The unconditional upper and lower bounds remain unchanged; no linear budgets are proven for G9, S21, or arbitrary sources. This round is a new clear counterexample and supporting expression within the project, and does not claim to have established document priority.

## 1. Definition and complete testimony

Pick

```math
Q=\{0,1,5,6,25,26,30,31\},\qquad A=Q\cup\{2,3\}.
```

Q is a separated three-dimensional cube with weights 1, 5, and 25. V(A) is all (v,u), u<v, including 45 cells; forward equal-leg L is ((x,y),(x+h,y),(x+h,y+h)), h>0, a total of 46 in this example.

Each row lists the colors in ascending order of tokens in A that are less than v. z=1−2c.

| v | c₀ | c₁ |
|---:|:---|:---|
| 1 | `0` | `0` |
| 2 | `11` | `11` |
| 3 | `001` | `001` |
| 5 | `1110` | `1110` |
| 6 | `10000` | `10001` |
| 25 | `111010` | `111010` |
| 26 | `0000001` | `0000001` |
| 30 | `00101010` | `00101010` |
| 31 | `111010000` | `111010000` |

The only color change is the inner cell (6,5), 0→1. Both complete colorations have no solid L; the outer 17 panels are identical. The original data is in [witnesses.json](witnesses.json), independent physical geometry verification in [verification.json](verification.json).

For B⊆A, let r_B(d)=|{u:u,u+d∈B}|,

```math
s_B(d)=\sum_{u,u+d\in B}(1-2c(u+d,u)),\qquad
\Phi_B(c)=\sum_{d>0}s_B(d)^2.
```

| Potential | c₀ | c₁ |
|---|---:|---:|
| Φ_Q | 8 | 4 |
| Φ_A | 9 | 13 |

## 2. Analytical proof of exact optimality

**Odd-Even Lemma. ** The sum of r ±1's has the same parity as r, so the square is at least r mod 2. Therefore every coloring (whether normal or not) satisfies

```math
\Phi_B\ge P_B:=\sum_{d>0}(r_B(d)\bmod2).
```

The odd fibers of Q in this example are exactly at d=19, 21, 29, 31, so P_Q=4. The odd fibers of A are exactly at d=2, 3, 4, 19, 21, 22, 24, 27, 31, so P_A=9. c₀ reaches Φ_A=9, so it is the global minimum among all normal colorings, and of course the minimum after fixing its external color.

The four cells of Q at d=1 are (1,0), (6,5), (26,25), and (31,30). The colors on c₀ are 0, 0, 1, 0, so s_Q(1)=2. The external homodyne lattices are (2,1) and (3,2), both of which are color 1, so the external field e(1)=−2. Therefore the total source difference of c₀ 1 fiber is already fully balanced, s_A(1)=0.

Any Q equilibrium, i.e. Φ_Q=4, must have the sum of every even-sized internal fiber equal to zero, in particular s_Q(1)=0. With the same external coloring, this forces s_A(1)=−2, contributing 4. All source fibers with a difference of 1 are even, and their parity lower bound is 0; the remaining fibers still contribute at least P_A=9. Therefore, any normal state in equilibrium with the external Q satisfies Φ_A≥13. c₁ reaches 13, and Φ_Q=4, so the restricted optimal value is exactly 13.

To sum up:

```math
\min_{c\text{ proper, fixed exterior}}\Phi_A(c)=9,
\qquad
\min_{c\text{ proper, fixed exterior},\ \Phi_Q(c)=4}\Phi_A(c)=13.
```

Therefore, under this external coloring, there is no coloring that simultaneously achieves all-source optimality and Q equilibrium. This assertion is only for the fixed exterior shown; there is no claim that changing the exterior still fails to achieve both.

## 3. General outfield lower bound and exact replacement representation

The following representation applies to any finite A, Q⊆A, not restricted to cubes. Fixed outer normal coloring, let e_d be the signed sum of the outer lattice at each difference. The interior is z and the interior fiber sum is s_d.

```math
\Phi_A(z)=\sum_d(s_d+e_d)^2
=\Phi_Q(z)+2\sum_de_ds_d+\sum_de_d^2.
```

If Q reaches its odd-even lower bound P_Q, then s_d=0 when r_Q(d) is even and s_d∈{−1,1} when it is odd. r_Q(d)=0 also counts as an even number. Therefore for all such internal equilibrium states we have

```math
\Phi_A\ge
K_Q(e):=
\sum_{r_Q(d)\text{ even}} e_d^2
+\sum_{r_Q(d)\text{ odd}} (|e_d|-1)^2.
```

The sum simply covers the differences in A. It is proved that minimizing the square fiber-by-fiber is sufficient; it is not assumed that these fiber-by-fiber optimal choices can simultaneously constitute normal coloring, so only the lower bound is given here. In this example, K_Q(e)=13, and c₁ is obtained.

**Complete replacement signature. ** When fixing the outside, in addition to all internal ternary NAE (non-congruent) constraints, each cross-boundary L is processed according to the internal grid number:

- One internal grid and two external grids of the same color c: the internal grid cannot take c; there is no constraint for the two external grids of different colors.
- Two internal cells, one external cell of color c: two internal cells cannot take c at the same time.
- Zero internal cells: must be normal; three internal cells: covered by original internal NAE constraints.

This is an exhaustive classification of all geometries L, so the internal shading satisfies these constraints if and only if all sources are normal after replacement. If the set of cross-boundary units and binary forbidden color constraints is recorded as Σ, and let Z(Σ) be the coloring set that satisfies the internal and residual constraints, then

```math
\min_{z\in Z(\Sigma)}\Phi_A(z)
=\|e\|^2+
\min_{z\in Z(\Sigma)}\left[\Phi_Q(z)+2\langle e,s(z)\rangle\right].
```

The minimum value of the empty feasible set is defined as +∞. Therefore, the "complete residual constraint Σ+external field e" is sufficient to accurately calculate the legality and full source potential changes. For a fixed non-empty Z(Σ), the optimal value minus ||e||² is the pointwise minimum of a finite number of affine functions and is therefore a piecewise linear concave function. e is treated here as a formal parameter; there is no claim that any parameter can be implemented by actual external normal shading.

This part is an explicit application of standard constrained elimination and square expansion to this problem, and no separate claims of originality are made. The actual counterexample shows that only optimizing Φ_Q will still choose the wrong global direction even with complete legality checks.

## 4. Reproduction, verification and scope of evidence

discovery command (requires`python-sat`;This round is 1.9.dev15, Glucose4):

```sh
python research/boundary_extension_20261108/upper/discover.py
```

The discovery program simultaneously encodes non-congruent constraints for all real L's before and after a single cell changes color, and enumerates color signatures on a difference fiber. Experimenting with two stated (Q,A), no counterexample was found for the first one; this negation does not have a UNSAT certificate attached, so there is no conclusion by inaction.

Standalone verification command (Python 3.10+ standard library):

```sh
python research/boundary_extension_20261108/upper/verify.py
```

The validator does not call the discovery program and does not import SAT. It enumerates all disordered grid point triples, and then directly identifies the forward equi-arm L; recalculates all 45 grids, 46 angles, two-state normality, external invariance, single grid color change, fiber sum, odd-even bounds and balanced external field bounds. Output PASS. Actual execution environment Python 3.13.5; input and script SHA-256 are saved with the results.

The finite leaf of the proof is the corner-by-corner legality of these two complete colorings; optimality comes from the parity argument from the previous section that holds for arbitrary colorings, not "the solver didn't find the smaller". The parent task additionally performs an independent unordered three-point verification from the original witness, which is recorded one level above this directory.

## 5. Specific constraints on the next round

1. The local budget of global minimum shading must preserve external fields or equivalent cross terms. All improvement items within the block cannot automatically disappear just because Φ_A is minimal.
2. When studying repairable blocks, the residual constraints Σ, external fields e, and the legal status of each fiber sum should be recorded at the same time; only the local potential or insufficient path radius should be recorded.
3. Overcharging K_Q(e)−P_A can be attempted, but the outer homodyne lattice will be reused by multiple blocks. Multiplicity control for global summation is currently lacking; this example does not provide it natively.
4. The cheapest next judgment is to construct two overlapping blocks that share the same batch of external difference grids and test whether the separately calculated outfield costs can be charged repeatedly; then look for provable amortization with labels or fractional weights.
5. The three-color source cannot directly use the ±1 odd-even square bound; it can be replaced by a color count vector, but the constraints and optimal goals must be re-derived.

Status: Counterexamples and exact optimal values ​​above **PROVED (with full finite certificates)**; universal replacement representation **PROVED**; global amortization, G9/S21 and R₃ numerical improvements still open. Scope of review: Author's self-review and parent task independent witness recalculation; does not claim Lean formalization or full manuscript audit.
