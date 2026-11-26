# Unconditional three-color upper bound $R_3(\mathcal{L}) \le 138$ via full-depth physical-corner pricing and directional subtriangle packings

Every three-coloring of the full $138 \times 138$ square $S_{138} = \{0, \dots, 137\}^2$ contains a monochromatic directed equal-leg $L$ $\{(x, y), (x + h, y), (x + h, y + h)\}$ with integer step $h > 0$. This establishes

$$
R_3(\mathcal{L}) \le 138,
$$

improving the previous unconditional verified upper bound $R_3(\mathcal{L}) \le 139$ ([`weak_triangle_20261123/SIDE_139.md`](../weak_triangle_20261123/SIDE_139.md)).

Following repository governance (`AGENTS.md` and `lgrid-research`), this bound is **100% unconditional and verified** from first principles in exact integer and rational arithmetic (`int` and `fractions.Fraction`) by a standalone Python standard-library checker ([`verify.py`](verify.py)), requiring **zero new SAT/RUP proof blobs** beyond the already-certified 39-patch allowlist and low-rainbow catalogs of `SIDE_139` (vendored with SHA-256 provenance in [`inputs/`](inputs/) so `verify.py` also runs standalone outside the repository tree).

Below, **New Mechanisms**, **Technical Improvements**, **Certified Local Packings**, and **Exact Integer Contradiction & Side-137 Diagnosis** are reported separately.

---

## 1. New mechanisms

### 1.1 Full-depth asymmetric physical-corner source pricing on $S_N$

On the side-138 full square $S_{138}$, the `SIDE_139` solver setup (which restricts every source rule on $T_m \cong W_{m-1}$ to $S_3$-symmetric barycentric-orbit weights $w \in \mathbb{Z}_{\ge 0}^{|\mathcal{O}_m|}$, averages subtriangle rays symmetrically on $T_{14}$ and $T_{15}$, and uses the `local_boundary_packings_15.json` table) is Dual-LP infeasible below `1.016009 > 1`.

In $S_N = \{0, \dots, N - 1\}^2$, individual placements $W_{m-1}(x_0, y_0, d)$ near the square boundaries or straddling the main diagonal $y = x$ do not experience $S_3$-symmetric host congestion. Enforcing equal weights across all six barycentric permutations of a corner $(j, a, b, c)$ weakens local lower-bound extraction against the actual oriented catalog colorings.

Instead, we assign independent nonnegative integer weights $w \in \mathbb{Z}_{\ge 0}^{\binom{m}{3}}$ directly to the literal physical corners $(j, x_w, y_w)$ of $W_{m-1}$, paired under the square's antidiagonal involution $\rho(X, Y) = (N - 1 - Y, N - 1 - X)$ with the reflected corner weight vector

$$
w^{\mathrm{refl}}(j, a, b, c) = w(j, a, c, b),
$$

where $(a, b, c) = (x_w - y_w,\; y_w,\; m - 2 - x_w - j)$. Under $\rho$, a copy $W_{m-1}(x_0, y_0, d)$ weighted by $w$ maps bijectively onto $W_{m-1}(L_{\max} - y_0, L_{\max} - x_0, d)$ ($L_{\max} = N - 1 - d(m - 2)$) weighted by $w^{\mathrm{refl}}$, preserving every directed $L$ of $S_N$ and keeping the global accumulated load $I(X, Y, h)$ antidiagonally symmetric.

For $m \in \{11, 12, 13\}$ at placement threshold $r_{\min}$, the exact certified minimum of $\sum_e w_e r_e$ over all proper 3-colorings of $T_m$ with at least $r_{\min}$ rainbows is evaluated over the full $S_3$-closed physical-corner profile catalog (`11/6`: `51,028` physical profiles from `356,406` oriented words; `12/9`: `39,448` physical profiles from `96,360` oriented words; `13/12`: `2,112` physical profiles from `2,928` oriented words) together with the exact concave unseen-word floor

$$
F_{\mathrm{unseen}}(w, b_{\mathrm{cut}}, r_{\min}) = \sum_{i=1}^{\max(b_{\mathrm{cut}} + 1,\; r_{\min})} w_{(i)} = \max_{t \in \mathbb{R},\; u \ge 0} \left( k t - \sum_{e} u_e \;\middle|\; t - u_e \le w_e \right),
$$

where $w_{(1)} \le w_{(2)} \le \dots$ are the sorted physical corner weights and $k = \max(b_{\mathrm{cut}} + 1, r_{\min})$.

### 1.2 Oriented $T_{13}$ ambient-square survivor-set intersections

For placements $W_{12}(x_0, y_0, d) \subset S_N$ whose effective threshold remains $\le 12$, every dilated $s_{\mathrm{sq}} \times s_{\mathrm{sq}}$ square ($s_{\mathrm{sq}} \in \{16, 17, 18\}$) containing $W_{12}(x_0, y_0, d)$ inside $S_N$ restricts the coloring of $W_{12}(x_0, y_0, d)$ to the recorded subset of surviving oriented `13/12` words in `order13_side{16,17,18}_profiles.json.xz` (and their antidiagonal images under $\sigma$). Intersecting these survivor sets across all fitting offsets inside $S_N$ upgrades placements with empty intersection directly to $r \ge 13$ and prices any remaining placement over its exact surviving oriented word subset.

### 1.3 Directional single-subtriangle rays on $T_{14} \dots T_{18}$ and upgraded local packings through order 40

Let $T_s^{(u_0, v_0, w_0)} \subset T_m$ ($14 \le m \le 18$, $s \in \{11, 12, 13\}$, $u_0 + v_0 + w_0 = m - s$) be a single unit-step translated subtriangle. Because $u_0 + v_0 + w_0 \ge 14 - s$, reducing $(u_0, v_0, w_0)$ coordinatewise to sum $14 - s$ exhibits an intermediate $T_{14}^{(F)}$ with $T_s^{(u_0, v_0, w_0)} \subset T_{14}^{(F)} \subset T_m$, so monotonicity and $r_m \ge m + 1$ (`ORDER14_MIN15.md`) give

$$
r_m \ge \max\bigl(m + 1,\; \operatorname{ext}_{14}(s, r_s^{(u_0, v_0, w_0)})\bigr),
$$

where $\operatorname{ext}_{14}(s, k)$ is the certified $T_{14}$ extension lower bound (`(11, 3)->20, (11, 4)->19, (11, 5..6)->17, (11, >=7)->15`; `(12, 6)->19, (12, 7)->18, (12, 8..9)->17, (12, >=10)->15`; `(13, 11)->19, (13, 12)->17, (13, >=13)->15`). Finite case partitioning over $r_s^{(u_0, v_0, w_0)}$ immediately proves 19 individual directional subtriangle inequalities (checked exhaustively inside `verify.py`):

- **$m = 14$**: $r_{14} + 2 r_{13}^{(u)} \ge 41$, $r_{14} + r_{12}^{(u)} \ge 25$, $r_{14} + r_{11}^{(u)} \ge 22$, $2 r_{14} + 3 r_{11}^{(u)} \ge 49$;
- **$m = 15$**: $r_{15} + r_{13}^{(u)} \ge 29$, $r_{15} + 2 r_{13}^{(u)} \ge 41$, $2 r_{15} + r_{12}^{(u)} \ge 42$, $r_{15} + r_{12}^{(u)} \ge 25$, $2 r_{15} + r_{11}^{(u)} \ge 39$, $3 r_{15} + 2 r_{11}^{(u)} \ge 61$;
- **$m = 16$**: $r_{16} + r_{13}^{(u)} \ge 29$, $r_{16} + 2 r_{13}^{(u)} \ge 41$, $r_{16} + r_{12}^{(u)} \ge 25$, $r_{16} + r_{11}^{(u)} \ge 22$, $2 r_{16} + r_{11}^{(u)} \ge 39$;
- **$m = 17$**: $r_{17} + r_{13}^{(u)} \ge 30$, $r_{17} + r_{12}^{(u)} \ge 25$, $r_{17} + r_{11}^{(u)} \ge 23$;
- **$m = 18$**: $r_{18} + r_{11}^{(u)} \ge 23$.

Using these directional rays both directly as global LP rules on $S_{138}$ and as Chvatal-Gomory local packing columns raises the certified unconditional local rainbow floors at every order $19 \dots 32$ by $+2$ to $+4$ (`local_packings.json.xz`, verified on literal physical corners in exact `Fraction` arithmetic):

| Order $n$ | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SIDE_139` unconditional | 21 | 24 | 29 | 33 | 38 | 44 | 49 | 54 | 61 | 67 | 73 | 80 | 87 | 96 |
| **Upgraded unconditional** | **23** | **27** | **31** | **36** | **41** | **46** | **51** | **57** | **63** | **69** | **76** | **83** | **91** | **99** |
| **Upgraded 7-step clearance** | **24** | **27** | **32** | **37** | **42** | **47** | **52** | **58** | **64** | **70** | **77** | **85** | **92** | **100** |

Through order 40 (`n = 33..40`), the certified unconditional floors continue `108, 118, 128, 140, 154, 168, 182, 197` (and `110, 120, 130, 142, 156, 170, 185, 200` with 7-step clearance).

---

## 2. Technical improvements

1. **Transposed box-bounded Dual LP (`A_dual = A^T`) with lazy cutting-plane pricing**:
   Formulating the barrier LP on the transposed fractional-coloring dual (with box-bounded orbit variables $0 \le \pi_i \le \mu_i$ and ~6,000--12,000 working rule/cap constraints) avoids dense $45{,}000 \times 45{,}000$ normal equations, while pricing all 30,000+ master rules in milliseconds via OpenMP adjoint operators and generating violated physical-corner cuts on demand.
2. **Fast $S_3$ corner-permutation profile verification**:
   `verify.py` verifies properness and rainbow cutoffs on every canonical word in `11/6`, `12/9`, and `13/12`, verifies all `26,345` ambient-square $T_{13}$ witness colorings (`16x16`, `17x17`, `18x18`), and applies exact precomputed $S_3$ barycentric corner permutations directly to the rainbow corner index tuples (cross-checked against byte-level orientation expansion on `13/12`), completing full dual independent exact-integer verification in ~40 seconds on pure Python stdlib.

---

## 3. Numerical bound, exact integer contradiction & side-137 diagnosis

### 3.1 Layered status & exact side-138 integer numbers

Both independent exact-integer verifiers in [`verify.py`](verify.py) -- **Verifier 1** (explicit 3D physical square array `host_I[h][X][Y]` on $S_{138} = \{0, \dots, 137\}^2$ evaluating both $(x_0, y_0, w)$ and $(L_{\max} - y_0, L_{\max} - x_0, w^{\mathrm{refl}})$ separately) and **Verifier 2** (signed-gap antidiagonal-orbit counter `orbit_sum` without grid coordinates) -- produce the exact same integers on [`certificate.json.xz`](certificate.json.xz):

| Claim / Quantity | Exact value | Status | Verified by |
| --- | ---: | --- | --- |
| Unconditional 3-color upper bound $R_3(\mathcal{L})$ | **$138$** | **Verified** | `python3 verify.py` |
| Weighted lower score $J_{\mathrm{lower}}$ at $N = 138$ | `999,999,932,278` | **Verified** | Verifier 1 & Verifier 2 |
| Weighted upper score $V_{\mathrm{upper}}$ at $N = 138$ | `998,339,965,644` | **Verified** | Verifier 1 & Verifier 2 |
| Exact integer margin $J_{\mathrm{lower}} - V_{\mathrm{upper}}$ | **`+1,659,966,634`** (`+0.1660%`) | **Verified** | Verifier 1 & Verifier 2 |
| Upgraded local triangle floors ($19 \le n \le 40$) | See table above & `local_packings.json.xz` | **Verified** | `python3 verify.py` (`Fraction`) |

### 3.2 Bottleneck diagnosis at $N = 138$ and $N = 137$

- **At $N = 138$**: Under the `SIDE_139` rule/packing pool, the dual LP lower bound is `1.016009 > 1`, with global lower-bound share concentrated on `(m=12, d=1)` (`12.17%`), `(m=14, d=9)` (`8.33%`), `(m=13, d=11)` (`8.31%`), and `(m=13, d=5)` (`7.63%`). Activating directional $T_{14}\dots T_{18}$ rays, upgraded `m = 19..38` packings, and full-depth (`11/6`, `12/9`, `13/12`) asymmetric physical-corner rules pushes the exact global ratio down to `V / J = 0.99834003 < 1` (`+0.1660%` relative margin, nearly twice the `+0.0889%` relative margin of `SIDE_139` at $N = 139$) using `3,108` rules across orders `{11, 12, 13, 14, 15, 16, 19}` and `23` upper caps.
- **At $N = 137$ (exploratory dual diagnosis, uncertified)**: Shrinking $N - 1$ from $137$ to $136$ triggers discrete dilation-boundary losses across high-leverage patches (for example, side-18 patches at dilation $d = 8$ have span $17 \times 8 = 136 = N - 1$, collapsing from a $2 \times 2$ translation box in $S_{138}$ to the single point $(0, 0)$ in $S_{137}$ and vanishing completely at $N = 136$). Under the `SIDE_139` setup, `N = 137` had `LP_LB = 1.071890` (`V = 1.220591`). With all new mechanisms above (plus nine exploratory side-18 `(12, 7, 18, ox, oy, 1)` RUP exclusions tested in scratch), the `N = 137` Dual LP reaches working-set lower bound `W_LB = 1.049678 > 1` (`V = 1.075048` at iteration 3), cutting the excess above `1.0` substantially while showing a genuine ~5% barrier that points toward unconditional $r_{15} \ge 17$ or deeper $m \in \{13, 14\}$ catalogs as the next local inputs needed for $N \le 137$.

---

## 4. Self-contained reproduction & SHA-256 manifest

Run the standalone standard-library verifier from the repository root or from any standalone copy of this directory:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 research/r3_side138_20261126/verify.py
```

| File | Bytes | SHA-256 | Description |
| --- | ---: | --- | --- |
| [`verify.py`](verify.py) | `30,642` | `8b4c34836e1f2087612fc4ca3eb8412d1629965cb35a5c50737c3e3407c0e59c` | Standalone Python 3 stdlib exact verifier (`int` + `Fraction`, Dual Verifiers 1 & 2, zero writes) |
| [`certificate.json.xz`](certificate.json.xz) | `119,492` | `46489be57d00b0bcbb1da8f73e9dad317ad70ebd1a12e057ffe490f3e8ea5598` | Exact integer full-square certificate for $N = 138$ (`3,108` rules, `23` upper caps) |
| [`local_packings.json.xz`](local_packings.json.xz) | `12,592` | `db59e28610ed070eb86f6faade78b1ffa29e4c21530dcda86a766d97f8bebb99` | Exact Chvatal-Gomory local boundary packings for orders `14..40` |
| [`inputs/provenance.json`](inputs/provenance.json) | `2,599` | `282420b32442b0782cc65654deb5b0a3a5a2baa4bbb99b000be26b7b62b34134` | Upstream repository provenance & SHA-256 digests for vendored certified inputs |
| [`inputs/triangle_grid_catalogs.json.xz`](inputs/triangle_grid_catalogs.json.xz) | `140,236` | `60af8c7b79d362a35eaeb3b0494e34bd2820ebc7d3fc23fd5ec8bcd5f72b48d6` | Certified low-rainbow canonical catalogs (`11/6`, `12/9`, `13/12`) |
| [`inputs/order13_side16_profiles.json.xz`](inputs/order13_side16_profiles.json.xz) | `640,708` | `88ad7ce92a7131f51154e96c8c78182c4d041e6fc6524c1a50e607c0dd2acaaf` | Certified `T_13` (`<= 12` rainbows) survivor profiles & witnesses in $16 \times 16$ |
| [`inputs/order13_side17_profiles.json.xz`](inputs/order13_side17_profiles.json.xz) | `145,860` | `c9be93f04f08b8773d5b0e6fff150d24bdb5d0d5cf6db4dd8cb0553c4e99fcb5` | Certified `T_13` (`<= 12` rainbows) survivor profiles & witnesses in $17 \times 17$ |
| [`inputs/order13_side18_profiles.json.xz`](inputs/order13_side18_profiles.json.xz) | `55,436` | `1ec346c036a58c0397822eb184f632cf8d7d47f113b40465960df8c4f3820ac5` | Certified `T_13` (`<= 12` rainbows) survivor profiles & exclusions in $18 \times 18$ |
| [`inputs/order14_extension_minima.json`](inputs/order14_extension_minima.json) | `1,652` | `c80d36a4f4de445074d4f352cdfa59c7c7759c6e95c6ea78cec22d7c52098496` | Certified `T_14` subtriangle extension minima & 91-cell witnesses |
| [`inputs/order12_side18_0_1.json.xz`](inputs/order12_side18_0_1.json.xz) | `111,376` | `a129d91abdcf56726ed02f00938c5d137b6b009c620415dfb04f2a3f7b59dd46` | Certified `(12, 9, 18, 0, 1, 1)` proof manifest |
| [`inputs/stride2_order12_21_manifest.json.xz`](inputs/stride2_order12_21_manifest.json.xz) | `2,760` | `0efe9c0a6eff4d75e9586602a10f26d94b19eaf46ccbe11bb21c3cab68ac3cc3` | Certified `(12, 6, 21, 0, 0, 2)` stride-2 proof manifest |
| [`inputs/side_141_patches.json`](inputs/side_141_patches.json) | `108` | `07f1fc1f74efabc715616aa3e081894775e4e3aeeb18526299df542a4885816b` | Certified side-141 square patch list |
| [`inputs/side_140_patches.json`](inputs/side_140_patches.json) | `108` | `f9ddeae10ef298a3f8ffe59e757ee38472aa2ac332f181dc3b7ab2166822c8b1` | Certified side-140 square patch list |
