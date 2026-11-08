# 有向 L 研究 skill：来源与检查范围

整理日期：2026-11-08。交付目标是形成可持续使用的项目研究工作流；本次没有声称解决 R₃、获得新的无条件界或完成全仓库证明的独立审计。

## 交付文件

- [SKILL.md](../.agents/skills/directed-l-grid-research/SKILL.md)：精确问题、上下界并行、方法筛选、反例约束、证据状态和推广条件。
- [研究地图](../.agents/skills/directed-l-grid-research/references/repository-map.md)：主稿、文献、开放依赖、研究 PR 与历史代码的定位。
- [路线与障碍](../.agents/skills/directed-l-grid-research/references/routes.md)：上界五组路线、下界四组路线，各有首个缺口、判别实验及成功条件；这些分组是候选菜单，不要求逐一穷尽。
- [证据与复现](../.agents/skills/directed-l-grid-research/references/evidence.md)：证书格式、核验命令、SAT／Lean 范围、跨会话记录。
- [文献完整基准](../.agents/skills/directed-l-grid-research/assets/paper20.json)：带原始出处的正常 20×20 三染色。
- [构造核验器](../.agents/skills/directed-l-grid-research/scripts/check_coloring.py) 与 [源码索引器](../.agents/skills/directed-l-grid-research/scripts/index_repository.py)：均仅依赖 Python 标准库。
- [全源码索引](RESEARCH_SKILL_SOURCE_INDEX.json) 与 [本次检查记录](RESEARCH_SKILL_CHECKS.json)。

skill 按项目目录放在 `.agents/skills/directed-l-grid-research/`，可在项目会话中以 `$directed-l-grid-research` 调用；发现行为及目录约定参见 [OpenAI 官方说明](https://developers.openai.com/api/reference/cli)。当前会话的预加载技能列表不一定热更新，必要时在本项目新会话调用。

## GitHub 范围

通过 GitHub 连接器取得仓库元数据、根目录、Issue／PR 查询与 PR 状态；随后本地克隆以支持全文件索引和有限核验。创建工作分支 `codex/directed-l-research-skill`。未提交、推送、合并或修改任何远程 PR。

| 固定输入 | 提交 | 树内文件数 |
|---|---|---:|
| main | `080822bb1d434b164a1f42ea159d0bf148396b71` | 1,082 |
| PR 1 head | `d6755b48f1fb6e786cc9b480b0d40139f3da2140` | 1,091 |
| PR 2 head | `7f8e8bfc4d5c8d46664764c6ca0a534bd6a90962` | 1,102 |
| PR 3 head | `a53970c49472813ac65d37428074e5c530134e76` | 1,114 |

创建时 PR 1–3 均未合并，呈串联依赖。索引保留每棵树的所有路径并按相同 blob 去重；同一路径不同版本分别记录。它不是只按文件名列目录：读取了所有原始 blob 字节，对 Python／JSON 作语法解析，抽取 Lean 声明、Markdown 标题、LaTeX 标签和 CNF 头，未发现相应的解析错误。语法通过不说明程序逻辑或数学证明正确。

## 阅读深度

精读范围包括项目 README、全部协作／目标／开放问题／文献说明，主数学稿的定义与主要证明链、条件数值传递、失败彩虹前提及证书说明，当前核验／编码的几何与约束逻辑，形式化范围和版本记录，以及三个 PR 的完整研究说明、证明与反例。历史阅读重点是下界编码与未决记录、局部可行集不能延拓的障碍、全局计费的重数问题、源跨度压缩反例、能量方法及有限域转化的失效边界。

其余历史文档和代码完成全文件结构索引，并按研究机制定位；**未逐行人工审阅全部历史程序和全部历史证明**。本次也未重跑所有历史搜索、重新构建 Lean 或证明当前全文与历史形式化逐项一致。后续使用 skill 时按工作包读取原证明与实现，不能将本报告当作全库正确性证书。

工作区还存在不属于固定 GitHub 提交的未跟踪目录 `lfree_sat/`。本次只作相关只读定位，从中找到文献矩阵，随后独立与原始论文重新匹配。该目录保持原样，不属于本次新增文件或全库 Git 索引的覆盖对象。

## 实际验证

1. 主稿核验器重新运行通过全部 13 组有限检查。它验证列明的表格、构造、部分等号情形与数值算术，不认证任意规模的全部定理。
2. 11、12 标记的两个完整 SAT 模型通过 CNF 和独立几何检查；仍只证明指定染色可行，不证明彩虹数最小。
3. PR 3 的选中固定边界从原始见证重新穷尽，复现合法状态、平衡状态、修复闭包及精确八格阈值。没有重跑全外部边界 C++ 搜索。
4. 新构造检查器与“遍历所有无序三点组后判定几何”的另一实现比较，覆盖边长至多 3 的全部二色方形，并检查方向区分、弱源／空源、非法输入和既有三角形证书。
5. 文献 20×20 矩阵与 arXiv:2502.05162v1 HTML 的 Figure 3 全部值匹配，再由两种几何枚举检查；完整基准已写入本 skill。
6. 条件 q=20、21、27 的整数阈值算术已重算；全局势与局部势的交叉项记账式作精确多项式展开及有理取值核对。未证源预算仍未证。
7. skill 结构校验通过，配套链接、文件、说明与脚本接口作自审；没有声称进行了独立代理的行为评测。

完整主稿复现报告和 PR 3 复现报告保留在此次会话的工作成果目录；便于随仓库使用的摘要、输入／检查器摘要及实际范围记录在 [RESEARCH_SKILL_CHECKS.json](RESEARCH_SKILL_CHECKS.json)。Git blob 哈希使用仓库原字节；运行核验器的 SHA-256 使用实际输入文件，Windows 换行可能使两者不同，不能混用。

## 独立精确复核的核心条目

下列 PASS 只覆盖写明的有限证书与算术，不覆盖普遍最优性、开放前提或文献优先权。独立检查前已运行精确计算环境自检并得到 `ENVIRONMENT OK`。

CLAIM: 20×20 文献矩阵的几何角数与单色角数 | MY VALUE: (2470,0) | THEIR VALUE: (2470,0) | VERDICT: PASS | METHOD: 从完整矩阵枚举无序三点组并判定指定方向和等臂条件，与按水平点对检查交叉比较

CLAIM: 十一标记给定三角形的单色角数与彩虹角数 | MY VALUE: (0,3) | THEIR VALUE: (0,3) | VERDICT: PASS | METHOD: 从原始行词重建所有格点，遍历三点组判定几何与颜色

CLAIM: 十二标记给定三角形的单色角数与彩虹角数 | MY VALUE: (0,6) | THEIR VALUE: (0,6) | VERDICT: PASS | METHOD: 从原始行词重建所有格点，遍历三点组判定几何与颜色

CLAIM: 六标记给定源的角数与加性能量 | MY VALUE: (16,130) | THEIR VALUE: (16,130) | VERDICT: PASS | METHOD: 从完整格点逐角计数，并由所有有序标记和的表示数平方和重算能量

CLAIM: q=20、21、27 的对角矛盾严格余量 | MY VALUE: (60,63,81) | THEIR VALUE: (60,63,81) | VERDICT: PASS | METHOD: 直接重算 ceil((18q+1)/3) 个标记的点对数减 q(18q)；仅算术，不证明源预算

CLAIM: 局部势展开中的交叉项为 2eΔs | MY VALUE: 0 | THEIR VALUE: 0 | VERDICT: PASS | METHOD: 对两边差作精确多项式展开，并在 0、1、1000000、2/3 参数处精确比较

## 数学编辑自审

检查范围仅为新写的 skill、三个参考文件和本报告中的数学记号与交叉引用。正文 `manuscript/main.tex`、原有数学证明、历史状态与证书均未修改。没有对旧稿作数学 token 改动；新写的条件例子仍显式保留条件，未将其记为新的数值成果。
