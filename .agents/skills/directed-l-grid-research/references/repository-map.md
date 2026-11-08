# 仓库、定义与证据地图

这是 2026-11-08 创建 skill 时的导航快照。后续使用时以实际提交、当前证明和有效证书为准。本文件中的项目结果表示仓库给出了相应证明或有限证据，不表示本次已完成全部证明的独立审计或文献优先权审计。

最新：[六类完成格共同计数](../../../../research/kernel_compatibility_20261108/README.md)，基础提交 `654cc044cad3d8ca6079a1931565a6ec44dcf2b5`。项目区间现为 `21≤R3≤464`。共同最小起点计数给出完整464证明；带颜色的相邻比较层路径提供进一步共同预算。用户明确当前重心是发明上界计数方式，不启动新的下界SAT搜索。下一数值目标463仍未完成。后续465、493段落保留其历史或文献基准含义。

同日后续研究见 [边界兼容性检查点](../../../../research/boundary_extension_20261108/README.md)：全源最优不保证三维块平衡的45格反例、文献20×20矩阵的四侧扩展障碍与必要内部修改数，以及2026新文献适用性核对。以下创建快照保留；续接时同时读取该检查点，不能再尝试被其确切反例否定的捷径。

更晚检查点：[三色联合约束](../../../../research/coupled_budget_20261108/README.md)，基于PR4的 `df6e35cfff68580dc78aa91bc35d4c6399a6464a`。当前项目区间更新为 `21≤R3≤465`：历史直接卷积证明的两项外部Golomb依赖已找到原始完成公告，并重建证明和独立精确核验；不依赖失效彩虹假设。本轮新联合端点引理独立给出466。主稿尚未并入这些复核。另有单缺陷21方形的半径10不可修复证书，以及局部强制失衡被外部同纤维格抵消的反例。后文493仍指创建时的文献基准。

## 1. 来源层级与版本

| 来源 | 创建时固定版本 | 用途 |
|---|---|---|
| 主分支 | `080822bb1d434b164a1f42ea159d0bf148396b71` | 当前数学主稿、已澄清的条件结果、文献与路线图 |
| [PR 1](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/pull/1) | `d6755b48f1fb6e786cc9b480b0d40139f3da2140` | 三维源的强迫边最小化与九步平衡 |
| [PR 2](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/pull/2) | `7f8e8bfc4d5c8d46664764c6ca0a534bd6a90962` | 外部单格阻塞、边界覆盖预算 |
| [PR 3](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/pull/3) | `a53970c49472813ac65d37428074e5c530134e76` | 双格修复反例、选中实例的精确八格阈值 |

创建时三个 PR 都处于 open、未合并状态，依次以上一个分支为 base；PR 3 的树包含前两个 PR 的研究文件。不要只读 main 而漏掉这些障碍，也不要直接将整个研究分支替代主分支。PR 状态是可变信息，续接时重新读取。

主稿入口：[固定版本 main.tex](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/blob/080822bb1d434b164a1f42ea159d0bf148396b71/manuscript/main.tex)。使用 LaTeX 标签定位，避免依赖会漂移的行号。

优先顺序：当前定理及完整证明／证书 → 相应来源版本与适用范围 → 最新研究分支中明确的修正 → 历史探索。历史发现可重新核验，历史“已通过”不自动覆盖当前稿。

## 2. 对象、记号及不能省略的假设

| 记号 | 精确含义 |
|---|---|
| `[n]²` | 完整方形，正文坐标为 1 至 n |
| `V(A)` | 所有 `u<v` 的实际源格 `(v,u)`，A 是有限整数集 |
| `W(A)` | 加上所有 `(u,u)` 的弱源 |
| `𝒯_m` | `V({0,…,m−1})`，含 `binom(m,2)` 格的完整严格三角形 |
| `m=|A|` | 标记数；避免与方形边长 n 混用 |
| `M(A)` | `binom(m,2)`，严格源格数 |
| `L(A)` | `max A−min A`，是跨度；区间格点数是 `L+1` |
| `F_δ(A)` | `{u:u,u+δ∈A}`，δ>0；`r_δ=|F_δ|` |
| `T(A)` | 严格源里所有几何 L 的数量，不是单色角数 |
| `E(A)` | 有序四元组满足 `a−b=c−e` 的数量，等于有序和表示数的平方和 |
| mixed corner | 平行输入异色；对二色源自动正常 |
| forcing corner | 平行输入同色；正常二色源中完成格只能取另一色 |
| rainbow | 三格颜色两两不同，仅在至少三色时可能出现 |

源角可唯一写为 `(u+δ,u),(v+δ,u),(v+δ,v)`，其中 `u<v∈F_δ`。δ 是纤维偏移，实际 L 步长为 `v−u`，两者不可混同。

继承弱着色为 `w_δ(v,u)=z(v+δ,u)`，定义在 `W(F_δ(A))`；其两条对角色类为 Golomb 集。两色分解发生在纤维的起点集，不是自动发生在 A 上。

无进位条件也需区分：正权重 separated 指 `w_(i+1)>2Σ_(j≤i)w_j`；2-dissociated 指系数在 `{-2,-1,0,1,2}` 的零关系只能平凡；injective 只要求子集和不同。前者依次蕴含后者，逆向一般不成立。

不同朝向文献间的转置是一个问题间的对应，不是任意方形染色中都可施加的保解对称。源标记反射 `t↦c−dt` 在格点上对应 `(x,y)↦(c−dy,c−dx)`；保留 d>0。SAT 中每一个额外对称约束都需要自己的代表存在性论证。

## 3. 可重复使用的精确恒等式

正文 `prop:counts`、`cor:span`：

```math
\sum_{\delta>0}r_\delta=M,\quad
T=\sum_{\delta>0}\binom{r_\delta}{2},\quad
E=2m^2-m+4T,\quad
T\le CM\ \Longrightarrow\ M\le(2C+1)L.
```

正文 `thm:forcing` 中 z 取 ±1，`s_δ=Σ_(u∈F_δ)z(u+δ,u)`，`Φ=Σs_δ²`，Γ 的顶点是真实源格：

```math
|E(\Gamma)|=2H,\qquad
H=\frac{2T-M+\Phi}{4},\qquad
2T=M+2|E(\Gamma)|-\Phi.
```

Γ 是简单二部图，边按偏移增大定向后无环；这些必要条件本身不足以给出所需边预算。局部下降 Φ 会同时减少 H，但 `2|E(Γ)|−Φ` 在固定 A 上不变。

## 4. 学界已核查的数值起点

截至本次限定范围的原文核对，采用 `R₂=5`、`21≤R₃≤493`。这不是“已穷尽所有后续文献”的声明。

| 原始来源及版本 | 可用结论与定位 | 使用边界 |
|---|---|---|
| Axenovich–Manske, Integers 8 (2008), A21，[期刊文](https://math.colgate.edu/~integers/i21/i21.pdf) | 两色精确基准；与 Canakci 等 Theorem 2.2 交叉核对 | 先转换其 L 约定，不能套到任意直角三点 |
| Canakci 等，[arXiv:2312.01159v1](https://arxiv.org/html/2312.01159v1)，2023-12-02 | Theorem 3.1 与 Figure 1：完整 20×20 正常三染色，因此 `R₃≥21` | 计算构造证明存在，不证明 21×21 不存在 |
| Mammel–Smith–Yerger, Integers 25 (2025), A21，[期刊文](https://math.colgate.edu/~integers/z21/z21.pdf) | Theorem 6，PDF 第 10–11 页：`R₃≤493`，Algorithm 3 | 区分 Golomb 跨度与可用位置数；摘要与正文的早期中间界有差异 |
| Jaber–Liu–Lovett–Ostuni–Sawhney，[arXiv:2504.07006v2](https://arxiv.org/html/2504.07006v2)，2025-07-14 | Theorem 1.1，有限阿贝尔群 standard corners 密度界，指数 `1/600` | 是非零群步长版本；转为本项目需方向和无绕回桥梁 |

`literature/KNOWN_RESULTS.md` 与两份 BibTeX 提供更广的文献入口，不等于其中每个结果都在本次重新审计。一般 corners 输入经主稿 `lem:H`、`lem:J`、`lem:embed` 转化后有 `R_k≤exp(O((log(2k))^600))`；常数未指定，不给出可用的三色数值改进。有限域模型的更强指数不能经普通二进制编码直接替换该指数。

原主分支未包含独立的 20×20 全矩阵证书；`exploration/research_round2/checks/cache_legacy20.py` 引用未导入的旧本机文件。本 skill 新附带 `assets/paper20.json`：从本地补充材料取得矩阵，再与 [Mammel 等 v1 的 Figure 3](https://arxiv.org/html/2502.05162v1#S3) 全部 400 个值逐项匹配，按本项目方向检查全部 2,470 个角，单色角为零。它是既有文献构造的复现，不是新下界，也没有依赖 4×4 裁剪来证明完整方形存在。

## 5. 项目已有结论与开放依赖

| 项目对象 | 主稿定位 | 可用内容／限制 |
|---|---|---|
| 两个不交 Golomb 集的并 | `thm:energy`、`cor:imbalance` | `T≤min(2M,M+5ρ)` 及不平衡亏损；应用前核对整集合确有两 Golomb 分解 |
| 实际纤维 | `cor:moments` | 求和控制 `K₃=ΣT(F_δ)`；并非整体 T 的同一估计 |
| 立方体 | `lem:capacity`、`cor:occupancy`、`thm:fourcube` | 五维单射立方体排除；分离四维源存在完整正常二染色 |
| 三维 mixed 极值 | `thm:nine` | 最少 mixed 为 9，2-dissociation 下取到；不是最少 forcing |
| 六标记极值与分类 | `prop:six-point-extremal`、`prop:six-mark-classification` | 正常二色源最高 T=16、E=130；全等号类型由证明分类，有限枚举只作支持 |
| 完整积、完整直和 | `thm:progression`、`thm:direct` | 必须有完整性与分离；补齐稀疏缺格可能破坏可染性 |
| 配对平移 | `thm:matching` | 需要两个平移集不交，不要求差值范围分离 |
| 二距离几何 | `thm:two_distance`、`thm:midpoint-three` | 需包括重复标记的和关系保持及精确距离比；非所有源都满足 |
| 图编码源 | `thm:graph-source`、`prop:weight-two-family` | `A_G={5^i+5^j:ij∈E(G)}`，`T=2C₄(G)`；四环允许有弦。完整图族迫使普适 T/M 系数至少为 2 |
| 无五维立方体高能量例 | `prop:cube-free-energy` | 没有声称该族存在正常二色源染色；只否定“排立方体就够了” |

开放链：`EP10 ⇒ H10 ⇒ S21`；`G9 ⇒ G9^exists ⇒ M≤20L`。G9 与存在型 G9 不是同一量词：后者只需为每个可染源选择一种着色。S21 的正文范围是 `L≤99,994`。

主稿条件数值为：S21 下 `R₃≤379`、`R₄≤98,777`；适当跨度内存在型 G9 下 `R₃≤361`。这些数字不替代无条件起点。历史465已在上述联合约束检查点逐条恢复直接卷积证明及外部输入，可按其明确证据范围使用。459、455、454、四色情形的旧数值及旧一般k色目标仍须逐条恢复依赖；不能因为465恢复就连带恢复其他数字，也不能因彩虹路线失效而一概否定独立证明。

## 6. 三个研究分支的关键补充

| 文件（在各自提交的树中） | 新信息 | 下一步必须保留的边界 |
|---|---|---|
| `research/three_cube_forcing/README.md` | 正 2-dissociated 三维源中 Φ 最小为 4，forcing 角最少 6、强迫边最少 12；内部至多九次合法单格下降 | 主稿的 mixed 最小 9 仍正确；两个极值目标相反。直接四色维度延伸的具体规则失效 |
| `research/three_cube_boundary/README.md` | 固定外部颜色可阻断全部内部不增单格路径；有边界覆盖不等式及局部预算 | 解析系数 8 与枚举结合约束同构的系数 6 分开标注；预算针对块内 Φ_Q |
| `research/three_cube_pair_repair/README.md` | 双格不增修复被六格不变量否定；选中固定边界的完整状态图给出最小单步半径 8 | 直接到平衡的最小 Hamming 距离是 12；与路径最大单步 8 不同。8 非任意边界通用上界 |

边界记录使用 `Q={0,1,5,6,25,26,30,31}`、`A=Q∪{2}`。两个阻塞记录的外部着色不同，不可混作同一见证。全边界 C++ 搜索汇总与选中边界的独立 Python 穷尽覆盖范围不同。

## 7. 按问题定位代码与历史

- 当前证书：`manuscript/verify_directed_L_manuscript.py`；附加矩：`manuscript/check_energy_examples.py`。
- 彩虹 CNF 与总模型核验：`manuscript/encode_rainbow_sat.py`、`manuscript/SAT_USAGE.md`。该工具不运行求解器，也不是一般完整方形求解器。
- 下界：`exploration/research_round3/lower/ENCODING.md`、`SUBTASK_REPORT.md`、`build_instance.py`、`check_rup_proofs.py`。历史 side-21 工作仍有未决分支，不能从局部 UNSAT 合成全局结论。
- 局部条件不足的全局实例：`exploration/research_round3/joint/REPORT.md` 及其 `triangle_core*.json`。一维可行标记集未必有完整三角形延拓。
- 全局计费：`exploration/research_round4/research/ANCHORED_REFLECTED_PRODUCT_FORCING_0045.md`、`fibers/PARTIAL_FORCING_BLOCK_LABELS_0046.md`、`fibers/SEMI_INDUCED_BLOCK_DENSITY_0046.md`、`fibers/COMPANION_FORCING_CUBE_SLOTS_0046.md`。
- 失效路线：`SPAN_COMPRESSION_OBSTRUCTION.md`、`THREE_COLOR_ENERGY_BARRIER.md`、`FINITE_FIELD_TRANSFER_OBSTRUCTION.md`，都在同一 round4 research 目录下；具体反例只约束各自断言。
- 历史形式化：`formal/README.md`、`formal/historical_records/SCOPE.md`、`coverage.json`、`manuscript_revision_crosswalk.json`。当前模块与对应检查入口见 `formal/lakefile.lean`、`AllAxioms.lean`、`CountingAxiomAudit.lean`。
- 原导入范围：`docs/IMPORT_SCOPE.md`、`exploration/README.md`。旧脚本含本机路径、缺少的外部文件和可选依赖；先在隔离输出目录适配再运行，保留原始输入。

创建过程中还发现本地未跟踪的 `lfree_sat/`，它不属于上述固定 GitHub 提交。本次只读取其说明、问题契约、核验器入口和文献矩阵，不修改或整体认证该目录。其 README 将核心反馈、击中集修复及同预算消融列为探索工作，并明确未展示提速、未找到 21×21 合法构造；使用这些历史实验前仍须核查对应输入、源码和报告。部署本 skill 不依赖该本地目录，完整基准已经另行核验并规范化保存。

完整索引包含每个固定版本的全部路径、Git blob、SHA-256，以及 Python 声明／导入、Lean 声明／导入、Markdown 标题、JSON 顶层结构和 CNF 头。正文与数学审阅的实际范围见 `docs/RESEARCH_SKILL_REVIEW.md`。

## 8. 全局计数续接检查点

`research/global_counting_20261108/README.md` 记录基于提交
`5b5db22c3c65123193cb31f2aa5bd949b3075e1a` 的新一轮并行上界研究。
跨源颜色请求的六格冲突计数与定量必有L代价、全层级回归及双端匹配、
极端形状的共同跨度代价和跨步长平移重叠矩，均有独立证明及审阅。
在假设正常463阶方形下，跨度425完成类的整体数量至多56，优于逐步长74；
尚未取得与之矛盾的统一下估计。当前区间仍21至464。
用户本阶段要求优先发明有较大压缩潜力的纯数学上界计数，未开展下界SAT搜索。
详情与未决桥梁以该目录当前证明和审阅为准；不将本导航当作证明证书。
