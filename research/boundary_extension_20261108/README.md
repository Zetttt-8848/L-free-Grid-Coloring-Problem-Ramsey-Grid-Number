# 边界兼容性研究：局部平衡反例、扩展障碍与新文献

2026-11-08；基础提交 `080822bb1d434b164a1f42ea159d0bf148396b71`。目标与工作包见 [CONTRACT.md](CONTRACT.md)。本轮完成了两个方向的明确数学检查点，**没有改善无条件区间 `21≤R₃≤493`，也没有确定 R₃**。

## 1. 上界方向：全局最优不保证局部平衡

在 `Q={0,1,5,6,25,26,30,31}`、`A=Q∪{2,3}` 的完整严格源上，给出两份正常二染色。只改内部格 `(6,5)`，块内势 `Φ_Q:8→4`，全源势却 `Φ_A:9→13`。

奇偶下界证明 9 已经是全源的绝对最小值；固定所示外部颜色且要求 Q 平衡时，最小值恰为13。这是目标冲突，不是找不到合法修复路径。它排除了借全局极小性直接假设局部平衡的推理；不否定 G9/S21 本身。

- [完整证明、45格见证及外场下界](upper/README.md)
- [发现代码](upper/discover.py)、[独立核验器](upper/verify.py)、[计算清单](upper/computation_manifest.json)
- [协调者独立物理三点核验](upper_witness_audit.json)、[Wolfram 精确算术交叉检查](wolfram_crosscheck.json)

一般替换必须同时保存跨界禁色约束和外部纤维和 e；正确的目标含 `2⟨e,s_Q⟩`。通用表示是约束消元与平方展开，不单独宣称原创性。新贡献是使局部/全局失配成为完整、可复核的反例及精确受限最优值。

## 2. 下界方向：文献样本必须修改内部才能扩展

证明了任意 n、k 下固定旧方形、增加底行和右列的精确分解：右列的独立禁色列表，加上底行的带颜色标签点对约束。一般放置则保留所有一元、二元和三元跨界约束。[通用定理与证明](lower/THEOREM.md)

对文献的完整20×20三染色，本轮证明四侧都不能保持内部不变而追加单行/单列。下侧有41条约束组成的删除极小核，左侧有38条；分别附完整24节点、18节点的分支证明及每条约束删除后的可行见证。“删除极小”不表示约束数最少。

进一步找到内部支撑互不相交的冲突核。若把原矩阵放到21×21方形偏移位置 `(ox,oy)`，任何合法扩展至少要修改下列数量的原400格颜色：

| 偏移 | (0,0) | (0,1) | (1,0) | (1,1) |
|---|---:|---:|---:|---:|
| 已证明的必要修改数下界 | 10 | 2 | 14 | 8 |

这些数不是最优修复距离；没有提供达到它们的21×21构造。它们只针对这份给定矩阵及四个连续放置位置，不排除任何一般21×21构造。

- [计算结果与复现说明](lower/README.md)
- [完整有限证书](lower/extension_results.json)、[互不相交支撑证书](lower/packing_results.json)
- [标准库核验器](lower/verify.py)、[协调者第二份证书检查](lower_cores_audit.json)
- [独立通用证明审阅](lower_proof_review.md)、[五组小参数穷尽交叉检查](lower_theorem_audit.json)

## 3. 最新文献核对及自己的推论

[文献报告](literature/README.md)记录了实际检索词、原始版本、逐篇阅读深度和不适用条件，覆盖直接数值论文、准多项式 corners 方法，以及2026年的多项式 corners 进展。没有把摘要阅读记作全文审计，也没有声称穷尽全部后续文献。

新近的独立多项式结果不允许直接令两条腿相同。对另一篇2026预印本，发现了均匀像集权重与参数重数混用的问题，并给出精确有理数/分圆多项式检查。[窄范围诊断](literature/WEIGHT_AUDIT.md)只反驳所指的等式，不声称最终密度定理已被否定。

文献启发与本轮反例共同指向：保留实际可实现状态、外场、颜色和资源重数，避免先对它们各自取粗界再拼接。尚缺的是适用于任意源、可全局求和的预算，因此没有从这些观察得到新的 Ramsey 上界。

Wiley Scholar Gateway 本轮需要重新认证，未贡献文献证据。Wolfram 已用于精确算术，Mathbox 用于来源、证明和计算审查流程；它们不构成额外的普遍定理认证。

## 4. 已执行检查和复现

发现阶段部分程序需要 `python-sat`；下列证书核验均只用 Python 标准库。从仓库根目录执行：

```sh
python .agents/skills/directed-l-grid-research/scripts/check_coloring.py .agents/skills/directed-l-grid-research/assets/paper20.json
python research/boundary_extension_20261108/upper/verify.py
python research/boundary_extension_20261108/lower/verify.py --output /path/to/fresh/lower_check.json
python research/boundary_extension_20261108/audit_upper_witness.py
python research/boundary_extension_20261108/audit_lower_cores.py
python research/boundary_extension_20261108/audit_lower_theorem.py
python research/boundary_extension_20261108/literature/check_polynomial_weight.py --output /path/to/fresh/weight_check.json
```

已重跑主稿核验器：13项通过，[本轮报告](manuscript_checks.json)。完整20×20证书核验覆盖400格、2470个L，零单色角，[报告](paper20_check.json)。这不等于全文证明审计或 Lean 新编译。各报告绑定相应输入/代码；主要计算的 v2 清单包含运行状态和前后哈希。

[审阅范围](AUDIT.md)；计算清单：[上界](upper/computation_manifest.json)、[下界](lower/checked_run/manifest.json)、[文献权重诊断](literature/weight_run/manifest.json)。

## 5. 可续接状态

- **上界路线仍开放：** 新反例要求预算保留外场。下一步用两个重叠块检查外场代价的重复收费，先找反例，再寻找带标签的分数摊销。不再尝试由全源极小性直接推出各块平衡。
- **下界路线仍开放：** 用互不相交冲突核约束解冻选择，比较满足必要修改数的候选与普通修复。尚未完成有对照的性能实验，也未找到21×21合法构造。
- **独立替代路线仍开放：** 把已证明的真实几何小核用于发现禁型；任何跨实例推广都要重新证明颜色、坐标和覆盖条件，不能把样本核当作普遍禁型。
- **文献依赖：** 2026多项式预印本的权重修正仍未完成；独立多项式定理到等臂情形的直接替换不可用。Wiley 覆盖待重新连接后补查。
- **推广条件：** 下界约束分解对一般 k 成立；上界 ±1 奇偶势依赖二色源，推广到三色源须重新推导颜色向量预算。暂未系统攻关 R₄。

项目专用 skill 及其创建快照随本分支导入。`docs/RESEARCH_SKILL_*` 是此前筹备阶段的历史记录，未被当作本轮新增核验证据；原未提交的 `lfree_sat/` 未整体导入或认证。当前成果的文献优先权未确立。
