# 当前命题与证明索引

本索引指向当前数学稿。Open assertion 是未解决的假设，External theorem 是文献输入。历史 Lean 覆盖记录不能代替当前稿的逐项对应。

最新研究目录结果：[全局计数](../research/global_counting_20261108/README.md)，尚未并入主稿。区间仍为21至464。

| 状态 | 结果 | 证明 |
|---|---|---|
| PROVED | 跨原始颜色源的六格请求冲突计数；给出任意延拓必有的单色L数量下估计 | [跨源计数](../research/global_counting_20261108/completion/COUNTING.md) |
| PROVED | 所有大小层级的带颜色回归恒等式与双端匹配上限 | [全层级计数](../research/global_counting_20261108/multilayer/THEOREM.md) |
| PROVED，使用外部OGR唯一性及跨度输入 | 极端形状跨度代价，将p=428至431的六类容量各减1；跨步长平移重叠预算 | [跨度及重叠计数](../research/global_counting_20261108/multiscale/THEOREM.md) |
| UNDECIDED | 从上述全局计数推出比464更小的Ramsey上界 | [独立审阅与范围](../research/global_counting_20261108/review/REVIEW.md) |

此前已证明的[六类完成格共同计数](../research/kernel_compatibility_20261108/README.md)：

| 状态 | 结果 | 证明 |
|---|---|---|
| PROVED，使用两项已认证外部Golomb输入 | R3≤464；新计数的矛盾量477965143 | [六类几何与共同占位](../research/kernel_compatibility_20261108/geometry/SIX_CLASS_LEMMA.md)、[独立审阅](../research/kernel_compatibility_20261108/review/REVIEW.md) |
| PROVED | 带颜色的最小点计费及相邻比较层路径上限；增强464矛盾量至1199151808 | [组合证明](../research/kernel_compatibility_20261108/combinatorial_upper/THEOREM.md) |
| FINITE-CHECKED | 两个六字颜色词的受限比较计数最高14 | 同上与独立标准库枚举；不是任意长度公式，也未证明463 |

2026-11-08 上一检查点尚未并入下列主稿索引：[完整报告](../research/coupled_budget_20261108/README.md)。

| 状态 | 结果 | 证明及证据 |
|---|---|---|
| PROVED，使用已认证外部计算定理 | 恢复历史上界 R3≤465；不依赖 G9/S21/彩虹前提 | [完整推导及来源](../research/coupled_budget_20261108/numeric_upper/THEOREM.md)，[独立审阅](../research/coupled_budget_20261108/structural/UPPER_PROOF_REVIEW.md) |
| PROVED | 一般 k 类联合端点引理；三色应用 R3≤466 | 同上；优先权未作全球检索结论 |
| FINITE-CHECKED | 单缺陷21×21候选的半径10修复不可能，任意正常修复至少改变11格 | [完整候选和分支证书](../research/coupled_budget_20261108/lower/README.md)；不提高下界 |
| FINITE-CHECKED | 局部强制失衡可被外部同纤维格抵消 | [结构证书与安全计费条件](../research/coupled_budget_20261108/structural/README.md) |
| UNDECIDED | n=464联合自相关正半定约束探索 | [实际运行范围](../research/coupled_budget_20261108/spectral/README.md)；没有精确矛盾证书 |

以下为原主稿索引，保留原有命题范围。

| 类型 | 标题 | 标签与正文位置 |
|---|---|---|
| lemma | Transposition | [lem:transpose](../manuscript/main.tex#L179) |
| proposition | Exact source counts | [prop:counts](../manuscript/main.tex#L226) |
| lemma | Diagonal exclusion and weak restriction | [lem:restriction](../manuscript/main.tex#L260) |
| lemma | Golomb classes and pair sums | [lem:golomb](../manuscript/main.tex#L286) |
| corollary | Energy to span | [cor:span](../manuscript/main.tex#L311) |
| theorem | Two-Golomb accounting | [thm:energy](../manuscript/main.tex#L399) |
| corollary | Unequal class sizes | [cor:imbalance](../manuscript/main.tex#L478) |
| corollary | Fibers and cube moments | [cor:moments](../manuscript/main.tex#L534) |
| proposition | When the shared-difference bound is stronger | [prop:small-class-deficit-dominance](../manuscript/main.tex#L620) |
| proposition | A weak-source sharpness limit | [prop:74](../manuscript/main.tex#L674) |
| proposition | Failure of a separate linear deficit | [prop:29](../manuscript/main.tex#L698) |
| lemma | Pair capacities | [lem:capacity](../manuscript/main.tex#L726) |
| corollary | Cube occupancy | [cor:occupancy](../manuscript/main.tex#L804) |
| theorem | A separated four-cube coloring | [thm:fourcube](../manuscript/main.tex#L824) |
| corollary | Exact attainable cube dimension | [cor:cube-threshold](../manuscript/main.tex#L880) |
| proposition | A limit of cube exclusion | [prop:cube-free-energy](../manuscript/main.tex#L895) |
| theorem | The sharp three-cube cost | [thm:nine](../manuscript/main.tex#L967) |
| theorem | Signed completion and physical forcing | [thm:forcing](../manuscript/main.tex#L1089) |
| assertion | G9 | [open:g9](../manuscript/main.tex#L1158) |
| proposition | Conditional consequence of G9 | [prop:g9](../manuscript/main.tex#L1163) |
| assertion | Existential G9 | [open:g9-exists](../manuscript/main.tex#L1180) |
| proposition | Consequences of selecting a coloring | [prop:g9-exists](../manuscript/main.tex#L1184) |
| lemma | Endpoint deficit and the six-term obstruction | [lem:small](../manuscript/main.tex#L1222) |
| lemma | A single failed pair | [lem:endpoint-equality](../manuscript/main.tex#L1251) |
| lemma | Five-mark equality sets | [lem:five-mark-equality](../manuscript/main.tex#L1292) |
| proposition | Six-mark equality sets | [prop:six-mark-classification](../manuscript/main.tex#L1327) |
| corollary | The exact six-mark maximum | [prop:six-point-extremal](../manuscript/main.tex#L1353) |
| theorem | Complete progression products | [thm:progression](../manuscript/main.tex#L1433) |
| theorem | Complete direct sums | [thm:direct](../manuscript/main.tex#L1462) |
| lemma | Complete overlap restrictions | [lem:rectangles](../manuscript/main.tex#L1470) |
| theorem | Translation matchings | [thm:matching](../manuscript/main.tex#L1528) |
| theorem | Two-distance representations | [thm:two_distance](../manuscript/main.tex#L1600) |
| theorem | Midpoint multiplicity at most three | [thm:midpoint-three](../manuscript/main.tex#L1684) |
| theorem | Sources encoded by graph edges | [thm:graph-source](../manuscript/main.tex#L1699) |
| corollary | Corner density approaching two | [prop:weight-two-family](../manuscript/main.tex#L1776) |
| assertion | S21 | [open:s21](../manuscript/main.tex#L1802) |
| proposition | From span to three colors | [prop:span-r3](../manuscript/main.tex#L1806) |
| corollary | Three colors under G9 | [cor:g9-three](../manuscript/main.tex#L1817) |
| theorem | Three colors under S21 | [thm:s21three](../manuscript/main.tex#L1824) |
| lemma | Finite shift count | [lem:shift](../manuscript/main.tex#L1832) |
| theorem | Four colors under S21 | [thm:s21four](../manuscript/main.tex#L1851) |
| lemma | Three-color line identity | [lem:variance](../manuscript/main.tex#L2198) |
| lemma | Weighted embedding implication | [lem:weighted](../manuscript/main.tex#L2238) |
| proposition | Refutation of the two local rainbow bounds | [prop:local-rainbows](../manuscript/main.tex#L2258) |
| proposition | Refutation of $`\mathsf{F}_{13}(17)`$ | [prop:t13](../manuscript/main.tex#L2268) |
| proposition | Integer weight certificates | [prop:weights](../manuscript/main.tex#L2407) |
| proposition | Arithmetic of a rejected numerical route | [thm:weighted](../manuscript/main.tex#L2446) |
| lemma | First-coordinate reflection | [lem:H](../manuscript/main.tex#L2560) |
| lemma | Half-turn and paired colors | [lem:J](../manuscript/main.tex#L2567) |
| lemma | Cyclic embedding without wraparound | [lem:embed](../manuscript/main.tex#L2574) |
| external | Jaber et al., Theorem 1.1~\cite{JLLOS25} | [eq:appendix-result-8](../manuscript/main.tex#L2586) |
| theorem | General bound from the external corners theorem | [thm:general](../manuscript/main.tex#L2593) |
| lemma | Exact endpoint deletion | [lem:deletion](../manuscript/main.tex#L2674) |
| lemma | A sharp restricted endpoint bound | [lem:anchor](../manuscript/main.tex#L2685) |
| assertion | EP10 | [open:ep](../manuscript/main.tex#L2716) |
| assertion | H10 | [open:h](../manuscript/main.tex#L2722) |
| proposition | Conditional endpoint reduction | [prop:peel](../manuscript/main.tex#L2726) |
