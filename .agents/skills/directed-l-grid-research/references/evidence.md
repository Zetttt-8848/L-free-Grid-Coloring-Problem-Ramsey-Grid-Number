# 证据、复现与交付约定

## 1. 数学记录的最小内容

在当前工作目录保存一个可续接记录，沿用仓库现有约定；不要求为了运行本 skill 新建数据库或改写全部历史。

```text
问题／工作包：
基础提交及相关 PR：
对象、坐标、颜色数、量词和范围：
精确命题及上／下界方向：
状态：PROVED / CONDITIONAL / CONJECTURE / COUNTEREXAMPLE /
      FINITE-CHECKED / UNDECIDED
依赖：原定理标签、外部来源版本、未证假设
证明／完整见证／不可满足证书路径：
检查：输入 SHA-256、检查器版本、命令、实际覆盖范围
结果：确切输出，失败与未完成情况
审阅：自审、独立实现、独立审阅或形式化，分别注明范围
首个剩余缺口与下一次判别检查：
```

状态可能分层：同一条普遍命题有解析证明，其代表实例另有 FINITE-CHECKED 数据；条件数值的算术可核对为 PASS，而依赖的源引理仍开放。不要用一个绿色总标签抹掉这些层次。

## 2. 构造证书检查器

在仓库根目录运行：

```sh
python .agents/skills/directed-l-grid-research/scripts/check_coloring.py coloring.json --output coloring_check.json
```

仅需 Python 标准库。输入必须明确 domain、k 和完整 rows；颜色编号为 `0,…,k−1`。第一坐标为行索引 x，第二坐标为列索引 y。字符串行仅支持单个十进制颜色数字；k 更大时使用整数列表。省略格点、重复标记、行长不符、越界颜色或非整数均拒绝。

附带已与原文逐值匹配的完整文献基准，可直接复现：

```sh
python .agents/skills/directed-l-grid-research/scripts/check_coloring.py .agents/skills/directed-l-grid-research/assets/paper20.json
```

应得到 400 格、2,470 个角、零单色角。归属与来源版本保存在 JSON 的 provenance 中；这是原有下界的复现。

完整方形示例：

```json
{
  "domain": "square",
  "k": 2,
  "n": 2,
  "rows": [[0, 0], [1, 0]]
}
```

`rows[x][y]` 是 χ(x,y)，从 0 开始。检查的唯一几何族是本项目的正向等臂 L，不同时禁止其他朝向。合法 n×n 方形的输出中有 `implied_Rk_lower_bound=n+1`；不声称找到该 k 的最优下界。

严格源示例（正文六标记完整见证）：

```json
{
  "domain": "strict-source",
  "k": 2,
  "marks": [0, 1, 2, 3, 4, 6],
  "rows": ["1", "01", "100", "0010", "11000"]
}
```

严格源略去最小标记的空行；第 i 条行词长度为 i+1，列为所有较小标记。弱源改成 `"domain":"weak-source"`，包括最小标记行及每行对角格，例如单标记的弱源可写成 `marks:[0], rows:["0"]`。源的输出 T 仍表示严格源角数；弱源枚举总角数比 T 多 M。源检查不输出方形下界。

核验器按水平点对和真实位移生成 L；源能量另从有序和表示数重算。它不读取已有 CNF 辅助变量、求解器状态或旧报告。发布重要结果时仍需另一种结构不同的检查，例如枚举所有无序三点组后判定几何形状；独立证书核验不替代普遍定理的证明。

## 3. SAT、枚举与精确计算

- 编码要说明变量对应哪些真实格点、每格恰一色、所有 L 约束，以及辅助变量可延拓的双向语义。
- 只有经证明保留至少一个轨道代表的对称约束，才能用于不可能性。仅仅对美观、周期或反射结构的偏好属于受限构造族。
- SAT 输出先还原全部真实颜色，再逐格逐角核验。输入和完整模型哈希都保留。
- UNSAT 输出需检查 proof trace；拆分时还需无遗漏覆盖、分支假设一致，以及每一分支的证书。使用未经核验的 cut 会改变原问题。
- 穷尽要写清总域、对称商、剪枝完备性、分支覆盖和实际结束状态。部分核验的范围单列；不以预测运行时替代完成记录。
- 用整数／有理数验证最终阈值、严格不等式和 LP 对偶证书。浮点优化负责侦察，舍入与有理重构后重新检查全部约束。
- 最优值要同时有可行证书和对应不可能性／下界证明。一个低彩虹见证仅给出彩虹最小数的上界。

旧程序的依赖、路径和输出位置可能不适合当前系统。先读代码及参数，在隔离目录生成新报告；无需盲目运行全部历史批处理、发布／封存程序或长时间搜索。保留源文件与旧报告，记录适配差异。

## 4. 主稿有限核验及形式化

从仓库根目录，明确输出路径以免覆盖旧记录：

```sh
python manuscript/verify_directed_L_manuscript.py --source manuscript/main.tex --bib manuscript/references.bib --output /path/to/new-run/manuscript_checks.json
python manuscript/encode_rainbow_sat.py --size 11 --rainbow-cap 4 --check-model manuscript/sat_examples/rainbow_11_cap4.model
python manuscript/encode_rainbow_sat.py --size 12 --rainbow-cap 6 --check-model manuscript/sat_examples/rainbow_12_cap6.model
```

将 `/path/to/new-run` 换为实际可写目录。主核验器使用 assert 并主动拒绝 `python -O`；不要绕过这一检查。本 skill 附带的小检查器不依赖 assert。主核验通过的含义以 `manuscript/README_verification.md` 的逐项范围为准，不扩大为全文证明已审计。

Lean 入口在 `formal/README.md`，工具链与 mathlib 由当前项目文件固定。真正需要形式化时，核查目标声明的对象、假设、映射和公理依赖，再按该说明构建；不要为普通阅读强制安装整套环境。历史覆盖映射对应较早正文版本，当前新增证明与三个研究 PR 不能自动继承其认证。一次新编译也不自动说明人工文本和形式声明完全一致。

## 5. 新颖性与文献桥梁

记录题名、作者、准确版本、定理编号、原文链接和检索日期。将“来源确实如此表述”“该定理成立的假设”“对本项目的应用桥梁”分开检查。优先期刊原文、作者预印本与正式源码。

小色数的数值基准、standard corner 与有向 L 的方向、有限域到整数的转化都需逐项核查。检索范围可从现有数值论文及引文向前后扩展；术语也检索 equal-leg L、right isosceles triangle、corners、Golomb/Sidon、ordered matching 和实际候选不变量。

新方法可在项目内部标为“新尝试”。若要对外称原创，另作相应文献比对并限定“在已检索范围内”；未找到匹配不证明全局优先权。不要把付费文献全文或第三方缓存加入研究仓库。

## 6. 源码索引刷新

需要比较新版本时运行：

```sh
python .agents/skills/directed-l-grid-research/scripts/index_repository.py --root . --ref <full-commit> --output /path/to/new-run/source_index.json
```

`--ref` 可重复，使用已确认的提交号。索引从 Git blob 原字节读取，避免 Windows CRLF 改变跨平台哈希。它读取所有列入的文件、解析文本结构并保留声明／标题等导航信息，不执行仓库脚本，也不验证证明或历史求解结果。已有索引是创建快照，更新时生成新版本并说明哪些依赖需复核。

## 7. 给用户的结果

报告无条件上下界是否改变，并把以下成果分开陈述：新结构定理、条件推论、有限构造、反例、已核验不可能性、方法推广及仍开放的依赖。简要指出决定性的机制和下一处缺口，链接实际证明、证书和报告；不以工具次数、冲突数或文件数代表研究完成度。
