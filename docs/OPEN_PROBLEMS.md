# 开放问题与失效路线

优先级见 [短期与长期路线图](ROADMAP.md)：先推进并解决R3，再系统研究R4。这些源界是候选路线，不是必须全部证明的终点。

当前一般性源界仍未解决。以下断言逐字摘自当前正文，全部为开放假设。不要以有条件的推论作为这些假设的证明。

最新项目区间为 `21≤R3≤464`，见 [六类共同计数检查点](../research/kernel_compatibility_20261108/README.md)。464由新的共同起点计数推出，不使用以下开放假设。当前按用户要求集中发明上界计数方式，下一数值目标为463或更小；下界保持21。

新的未决计数问题：对同一边界颜色词产生的多层比较，严格控制“每色每层至多两个贡献”的联合总量。相邻层路径计数已有组合证明，但仍不足以排除463。长度5至9的有限词对极值只在其实际枚举范围成立，不能当作任意长度公式。

续接应优先区分三项缺口：将联合自相关约束转成精确矛盾证书；在候选构造中同时修复跨块约束；对完整纤维的失衡与强迫边给出独立总预算。某个单缺陷21×21候选已证明半径10内不可修复，不能继续把单色角数当作修复距离。局部源的强制失衡也可能被同纤维外部格抵消，不能直接累加为全源代价。

```latex
\begin{assertion}[G9]\label{open:g9}
For every finite $A\subset\Z$ and every proper two-coloring of $V(A)$,
the forcing graph satisfies $|E(\Gamma)|\le9M(A)$.
\end{assertion}
```

```latex
\begin{assertion}[Existential G9]\label{open:g9-exists}
\rev{For every finite $A\subset\Z$ with $\mathcal Z(A)\ne\varnothing$, some $z\in\mathcal Z(A)$ satisfies $|E(\Gamma_z)|\le9M(A)$.} Denote this assertion by $\mathrm{G9}^{\exists}$.
\end{assertion}
```

```latex
\begin{assertion}[S21]\label{open:s21}
Every finite $A\subset\Z$ with $L(A)\le99\,994$ whose strict source admits a proper two-coloring satisfies $M(A)\le21L(A)$.
\end{assertion}
```

```latex
\begin{assertion}[EP10]\label{open:ep}
Every finite integer set $A$ with $|A|\ge2$ and properly two-colored $V(A)$ has an endpoint $a\in\{\min A,\max A\}$ such that
\begin{equation}\label{eq:ep10}
T(A)-T(A\setminus\{a\})\le10(|A|-1).
\end{equation}
\end{assertion}
```

```latex
\begin{assertion}[H10]\label{open:h}
Every finite integer set $A$ admitting a proper two-coloring of $V(A)$ satisfies $T(A)\le10M(A)$.
\end{assertion}
```

## 已排除的捷径

- 仅排除五维立方体不足以推出统一线性能量或角数界。
- 将各纤维分别拆成 Golomb 类，不保证共享完成格的颜色兼容。
- F11(5)、F12(7)、F13(17) 已有完整反例，旧加权路线的这些前提不能使用。
- 当前有限证书给出彩虹数的可达上界，不自动证明最小值。

## 合作时提交什么

2026-11-08 [全局计数检查点](../research/global_counting_20261108/README.md)新增三个具体开放桥梁：

- 对三个实际对角颜色源，证明跨源请求代价 `sum_q min(V^a,H^b,H^e+V^e)` 的统一正下界；目前只证明该代价是任意延拓的必有单色L数量下界，并给出严格区分见证。
- 对同一个长对角词，统一控制所有层级的截断自相关及首尾匹配容量；不能把各层分别最大化后当作相容状态。
- 极端尺出现次数的全局上限已降至56（假设正常463阶方形）；还须把近极端跨度的代价与足够强的出现次数下估计联系起来。四个局部容量下降不能直接变成新的Ramsey数值界。

这些计数与原有边界亏损可能重叠，合并时须保留共同对象，不能直接相加各自的数值收益。

2026-11-08 补充：[全源最优与局部平衡不兼容的反例](../research/boundary_extension_20261108/upper/README.md)表明全源势最小不能直接消掉各块局部不平衡；固定外部的两个精确最优值为9与13。[文献20×20样本的扩展障碍](../research/boundary_extension_20261108/lower/README.md)给出必要内部修改数，不能解释为一般21×21不可能性。G9、S21及三色精确值仍开放。

写明命题及范围，给出完整证明或可独立重算的反例。计算结果记录输入、命令、依赖版本和输出。新结果先在独立分支讨论，并在改动当前数学稿后重跑有限核验。
