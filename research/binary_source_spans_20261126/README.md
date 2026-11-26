# Exact Minimum Spans $e_k$ ($1 \le k \le 16$) and Interval Capacities $C(n)$ ($1 \le n \le 27$) for Proper Binary Strict Sources

## Summary and Status

For a finite integer set $A \subset \mathbb{Z}$, let its **strict source** be

$$
V(A) = \{(v, u) \in A \times A : u < v\}.
$$

A **proper binary coloring** of $V(A)$ is a map $\chi : V(A) \to \{0, 1\}$ with no monochromatic directed equal-leg L

$$
\bigl((v, u),\; (v + t, u),\; (v + t, u + t)\bigr) \subseteq V(A), \qquad t \in \mathbb{Z}_{>0}.
$$

Define the **minimum binary-source span** $e_k$ ($k \ge 1$) and the **interval binary-source capacity** $C(n)$ ($n \ge 1$) by

$$
e_k = \min\bigl\{\max(A) - \min(A) : A \subset \mathbb{Z},\; |A| = k,\; V(A) \text{ admits a proper binary coloring}\bigr\},
$$

$$
C(n) = \max\bigl\{|A| : A \subseteq \{0, 1, \dots, n - 1\},\; V(A) \text{ admits a proper binary coloring}\bigr\}.
$$

By translation invariance ($A \mapsto A - \min(A)$), $C(n) < k \iff e_k \ge n$, and hence $C(n) = \max\{k \ge 1 : e_k \le n - 1\}$ whenever all $e_k \le n - 1$ are determined.

- **Status**: **PROVED** (unconditional, computer-assisted, 100% self-contained in-repository, zero external inputs).
- **Domain note**: Following `lgrid-research`, these theorems hold on strict binary sources $V(A)$; they do not by themselves assert a full-square Ramsey bound, and enter four-color full-square upper bounds through the hereditary rank-neighbor span recursion on the twelve main-diagonal completion classes (`research/r4_mcf_minimax_20261126/`).

### Certified Exact Values

Previously, only $C(4) = 4, C(8) = 7, C(12) = 9, C(16) = 11$ (`codex/r4-local-capacity-round3-20261114`) and $C(20) = 13$ (`r4_disjoint_edge_bins_20261123`) were determined, leaving lower bounds $e_8 \ge 8, e_{10} \ge 12, e_{12} \ge 16, e_{14} \ge 20$ and trivial unit steps $e_{15} \ge 21, e_{16} \ge 22$. This package determines **every** $e_k$ for $1 \le k \le 16$ and **every** $C(n)$ for $1 \le n \le 27$ to exact equality:

| $k$ | Prior $e_k$ bound (`d18a965`) | Exact $e_k$ | Gain | Representative optimal $k$-set $A \subseteq \{0, \dots, e_k\}$ |
| ---: | ---: | ---: | ---: | --- |
| 1 | 0 | **0** | 0 | `[0]` |
| 2 | 1 | **1** | 0 | `[0, 1]` |
| 3 | 2 | **2** | 0 | `[0, 1, 2]` |
| 4 | 3 | **3** | 0 | `[0, 1, 2, 3]` |
| 5 | 4 | **4** | 0 | `[0, 1, 2, 3, 4]` |
| 6 | 5 | **6** | +1 | `[0, 1, 2, 3, 4, 6]` |
| 7 | 6 | **7** | +1 | `[0, 1, 2, 3, 4, 6, 7]` |
| 8 | 8 | **9** | +1 | `[0, 1, 2, 3, 4, 6, 7, 9]` |
| 9 | 9 | **10** | +1 | `[0, 1, 2, 3, 4, 6, 7, 9, 10]` |
| 10 | 12 | **12** | 0 | `[0, 1, 2, 3, 4, 6, 8, 9, 11, 12]` |
| 11 | 13 | **14** | +1 | `[0, 1, 2, 3, 5, 7, 9, 10, 12, 13, 14]` |
| 12 | 16 | **17** | +1 | `[0, 1, 2, 3, 4, 7, 8, 11, 13, 14, 16, 17]` |
| 13 | 17 | **19** | +2 | `[0, 1, 2, 3, 5, 6, 8, 9, 11, 15, 17, 18, 19]` |
| 14 | 20 | **21** | +1 | `[0, 1, 2, 4, 5, 7, 8, 10, 11, 13, 17, 19, 20, 21]` |
| 15 | 21 | **24** | +3 | `[0, 1, 2, 4, 5, 7, 8, 13, 14, 16, 19, 20, 22, 23, 24]` |
| 16 | 22 | **27** | +5 | `[0, 1, 2, 4, 5, 7, 8, 10, 14, 16, 17, 19, 23, 25, 26, 27]` |

Consequently, for $1 \le n \le 27$:

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **$C(n)$** | 1 | 2 | 3 | 4 | 5 | 5 | 6 | 7 | 7 | 8 | 9 | 9 | 10 | 10 |

| $n$ | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **$C(n)$** | 11 | 11 | 11 | 12 | 12 | 13 | 13 | 14 | 14 | 14 | 15 | 15 | 15 |

---

## 1. Mechanism and Symmetry Proofs

Following `lgrid-research`, the mathematical reductions, technical proof compression, and numerical table are separated explicitly.

### 1.1 Inductive hereditary span and sub-window restriction

Suppose $e_1, \dots, e_{k-1}$ are already certified and every $k$-element source of span strictly less than $L$ ($L \ge e_{k-1} + 1$) has been refuted. Let $B \subset \mathbb{Z}$ be any $k$-element set of span $\max(B) - \min(B) = L$ admitting a proper binary coloring $\chi$ of $V(B)$. Translating to $A = B - \min(B) = \{0 = a_0 < a_1 < \dots < a_{k-1} = L\}$ preserves all pairwise differences and therefore preserves all directed equal-leg Ls.

For every $0 \le i < j < k$ with $(i, j) \ne (0, k - 1)$, the contiguous mark slice $A_{i..j} = \{a_i, a_{i+1}, \dots, a_j\}$ has cardinality $m = j - i + 1 < k$ and satisfies $V(A_{i..j}) \subseteq V(A)$, so $\chi|_{V(A_{i..j})}$ is proper. By induction:

1. **Span inequality**: $a_j - a_i \ge e_{j - i + 1}$ for all $0 \le i < j < k$ with $j - i + 1 < k$.
2. **Sub-window colorability**: the translated slice $U = \{a_i - a_i, \dots, a_j - a_i\}$ cannot belong to any already certified family of uncolorable $m$-element mark sets.

### 1.2 Order-reversing reflection symmetry on $V(A)$

For $A \subseteq \{0, \dots, L\}$ with $0, L \in A$, put $A' = \{L - x : x \in A\}$. Define $\Phi : V(A) \to V(A')$ by

$$
\Phi(v, u) = (L - u,\; L - v) \qquad (u < v \iff L - v < L - u).
$$

For any $u < v$ in $A$ and integer $t > 0$ with $u + t, v + t \in A$, set $u' = L - (v + t)$ and $v' = L - (u + t)$. Then $u' < v'$ lie in $A'$, $u' + t = L - v \in A'$, $v' + t = L - u \in A'$, and

$$
\Phi(v, u) = (v' + t, u' + t), \qquad \Phi(v + t, u) = (v' + t, u'), \qquad \Phi(v + t, u + t) = (v', u').
$$

Hence $\Phi$ maps the set of directed equal-leg Ls of $V(A)$ bijectively onto that of $V(A')$ (reversing the order of the two equal-step endpoints while fixing the corner $(v + t, u) \mapsto (v' + t, u')$). Consequently:

- Every uncolorable $m$-set $U$ with $\min(U) = 0$ and $\max(U) = s$ certifies uncolorability of $\max(U) - U$ as well.
- Among $k$-tuples $0 = a_0 < \dots < a_{k-1} = L$, it suffices to check representatives satisfying $A \le_{\text{lex}} (L - a_{k-1}, L - a_{k-2}, \dots, L - a_0)$.

### 1.3 Palette-swap symmetry and unit-propagation confluence

Global color negation $\chi \mapsto 1 - \chi$ preserves properness on $V(U)$, so any chosen root cell $c_0 \in V(U)$ ($|U| \ge 2$) may be fixed to color $0$. Under any partial assignment $\text{val} : V(U) \to \{-1, 0, 1\}$, an L-triple $\{x, y, z\}$ with $\text{val}(x) = b \in \{0, 1\}$ reduces to the binary clause $(\text{val}(y) \ne b) \lor (\text{val}(z) \ne b)$: if $\text{val}(y) = b$ and $\text{val}(z) = b$ a monochromatic L is present; if $\text{val}(y) = b$ and $\text{val}(z) = -1$ then $\text{val}(z) = 1 - b$ is forced. Because unit implication on a fixed set of unit and binary clauses is monotone on the lattice of partial assignments, whether unit propagation reaches a conflict -- and the resulting forced assignment when no conflict occurs -- is **confluent and independent of propagation order**.

---

## 2. Technical Certificate Structure (`LGB1` Binary Format)

To keep the repository archive compact (`16.36 MiB`, zero solver dependency at verification time), `seed_trees_k16.bin.xz` uses MOMS + 1-step failed-literal variable selection to encode `257,255` explicit 2-color binary refutation trees (`LGB1` stream):

- `4 B`: ASCII magic `"LGB1"`.
- `uint32_le num_lemmas` (`257,255`), followed by `num_lemmas` records:
  - `uint8 m`, `uint64_le mask` (bitmask of $U$ with bit $0$ set and popcount $m$), `uint32_le t_len`, and `int16_le T[t_len]` (`T[0]` = root cell assigned $0$, followed by preorder tokens: `-1` = immediate unit-propagation conflict leaf; `cell_id >= 0` = branch `cell_id = 0` then `cell_id = 1`).
- `uint32_le num_steps` (`15`, covering $k = 2, \dots, 16$), followed by `num_steps` records:
  - `uint8 k`, `uint8 lower_bound`, `uint8 exact` (`1`), `uint8 num_unsat`, `uint8 unsat_L[num_unsat]`, `uint8 witness_A[k]`, and `uint8 witness_col[k(k-1)/2]`.

---

## 3. Artifact Digests and Reproduction

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `seed_trees_k16.bin.xz` | `17,157,184` | `5d6ebb6ad405bcf43997afff4e5732864ceff1aa62e50cc01ad8c6e2eaebf85f` |
| *(decompressed `LGB1` stream)* | `59,565,682` | `f7e4a687e4b0395aa0e2c8c0d7f941c341d128d75b387560d3c57d9139943548` |
| `witnesses_k2_k16.json` | `45,251` | `03e229624c8919ec046769cc14ec4d575de25967c480d3e79776d44efb3069ea` |

Run from the repository root (zero files are written inside the repository):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 research/binary_source_spans_20261126/verify.py
PYTHONDONTWRITEBYTECODE=1 python3 research/binary_source_spans_20261126/verify.py --pure-python
```
