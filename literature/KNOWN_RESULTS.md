# 学界已有成果与本项目的关系

核查日期：2026-11-05。以下是已核查的核心原始文献地图，不是对全部文献的穷尽调查。数值界更新必须有可核查原始出处、版本和证明位置。

项目最新结果为 [六类共同计数的464上界](../research/kernel_compatibility_20261108/README.md)，区别于本页的已发表493比较基准。[新计数与既有文献的关系](../research/kernel_compatibility_20261108/COUNTING_COMPARISON.md)核对了不交Golomb尺研究及2026差值装填论文；标记不交不等于差值集不交，后者的定理不能直接移植。没有全球优先权或穷尽文献声明。

2026-11-08 的增量检索与精读见 [新文献及适用性报告](../research/boundary_extension_20261108/literature/README.md)。检索到2026年多项式 corners 预印本及较新的稳定性论文；未核实可直接替换下述三色数值基准的后续结果。报告明确区分已读章节、未审计证明及不适用的等臂/有限域假设。

同日后续：[本项目重新核实的465上界](../research/coupled_budget_20261108/numeric_upper/THEOREM.md)是项目历史卷积证明，区别于下列已发表493基准。它仅需 Golomb 跨度下界 G(24)≥425、G(25)≥480；原始输入分别核对了 [OGR-24完成公告](https://blogs.distributed.net/2004/11/) 和 [OGR-25完成公告](https://blogs.distributed.net/2008/10/)。本轮未本地重跑这些外部穷尽计算，也不主张465的全球优先权。

## 先统一问题约定

本项目固定正步长、等长两条腿的定向 L：

```math
\mathcal L(x,y;d)=\{(x,y),(x+d,y),(x+d,y+d)\},\qquad d>0.
```

部分文献写成另一个朝向，坐标转置把两者对应，因此其正步长 L 数相同。一般三点直角形、允许任意长宽的角、密度版本及三维 corners 不能直接混同。方向转换证明见本项目正文的 Transposition 引理。

## 1. 两色精确值：已解决的基准

```math
R_2(\mathcal L)=5.
```

来源：Maria Axenovich 与 Jacob Manske，*On monochromatic subsets of a rectangular grid*，Integers 8 (2008), A21。[期刊原文](https://math.colgate.edu/~integers/i21/i21.pdf)。另可与下面 Canakci 等文献的 Theorem 2.2 交叉核对。

用途：核验方向、索引和小规模实现。不能将两色证明直接视为三色答案。

## 2. 三色下界与早期上界

Canakci、Christenson、Fleischman、Gasarch、McNabb、Smolyak 的 [2023 预印本 v1](https://arxiv.org/html/2312.01159v1) 在 Theorem 2.3 给出上界2593，Theorem 3.1 给出区间21至2593。下界来自完整20×20正常三染色，而不是搜索未找到反例。

```math
21\le R_3(\mathcal L)\le2593.
```

研究价值：对角线消色、强迫关系及 SAT 构造。2593是历史上界，已被下一项改进，不应在项目首页标为当前基准上界。

## 3. 三色已核查的更强上界

Mammel、Smith、Yerger，*Ramsey Theory on the Integer Grid: The “L” Problem*，Integers 25 (2025), A21，Theorem 6：

```math
R_3(\mathcal L)\le493.
```

[期刊原文](https://math.colgate.edu/~integers/z21/z21.pdf)；[arXiv版本](https://arxiv.org/abs/2502.05162)。方法使用区间计数和 Golomb 尺约束。论文致谢将772与493的证明归功于审稿人。期刊版与预印本对中间数值有表述差别，本库只将最终 Theorem 6 的493作为比较基准。arXiv版另外讨论下界及搜索策略。

合并已核查上下界，协作的无条件数值起点是：

```math
21\le R_3(\mathcal L)\le493.
```

该区间仍不等于精确值。本次定向检索未核实更强的后续无条件界，不能据此断言不存在后续文献。该文提出的22×22正常着色猜测也不应当成已存在的构造。

## 4. 一般密度工具：准多项式 corners 定理

Jaber、Liu、Lovett、Ostuni、Sawhney，*Quasipolynomial bounds for the corners theorem*，[完整版本 v2，Theorem 1.1](https://arxiv.org/html/2504.07006v2)。对于无非零步长 standard corner 的有限阿贝尔群平方子集，有绝对常数 c>0，使

```math
|A|\le |G|^2\exp\!\left(-c(\log |G|)^{1/600}\right).
```

标准角为 (x,y)、(x+d,y)、(x,y+d)。该定理本身不是本项目定向 L 的小色数数值界。正步长处理、反射、配对颜色及无绕回嵌入需要另证。本项目附录给出一条转化，导出关于颜色数的一般增长界，但不直接把493改小。

## 5. 相关数学输入与阅读顺序

- Graham–Solymosi，*Monochromatic equilateral right triangles on the integer grid* (2006)：该网格着色问题的重要背景。[出版者 DOI](https://doi.org/10.1007/3-540-33700-8_7)。本轮未重新审计其全部定量推导。
- Ajtai–Szemerédi 的经典 corners 工作：密度路线的背景输入，具体版本见 bibliography 中 AS74。
- Sidon/Golomb 理论：用于单色纤维约束；binary Sidon 输入和 Wood 的 no-carry 转化与立方体讨论相关。[Wood原文入口](https://arxiv.org/abs/math/0509455)。具体容量与权重假设须回到项目正文和其引用，不能由普通 Sidon 定义自动推出全局源界。

建议先读 L 问题的两篇数值文献，再沿“全局完成格兼容性”与“密度/结构增量”两个方向读背景。已有理论是检验新机制的基准，不等于禁止使用前人的定理。

## 6. 不得混入学界数值基准的项目结论

本项目的源计数、Golomb 联合计数、六标记分类和结构化源界见当前数学正文。它们的优先权未由本次导入自动确认。

S21下379及98777、存在型G9下361，都是保留未证假设的条件推论。五维立方体排除只是一项必要条件。F11(5)、F12(7)、F13(17)已被项目中的完整着色证书否定。上述数字或失败前提均不能替换学界无条件区间。
