# 开放问题与失效路线

优先级见 [短期与长期路线图](ROADMAP.md)：先推进并解决R3，再系统研究R4。这些源界是候选路线，不是必须全部证明的终点。

当前一般性源界仍未解决。以下断言逐字摘自当前正文，全部为开放假设。不要以有条件的推论作为这些假设的证明。

最新项目区间为 `21≤R3≤465`，见 [联合约束检查点](../research/coupled_budget_20261108/README.md)。465来自已恢复依赖并独立复核的历史直接卷积证明，不使用以下开放假设。下一数值目标是找到完整21×21正常三染色或排除464×464；本轮二者均未做到。

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

2026-11-08 补充：[全源最优与局部平衡不兼容的反例](../research/boundary_extension_20261108/upper/README.md)表明全源势最小不能直接消掉各块局部不平衡；固定外部的两个精确最优值为9与13。[文献20×20样本的扩展障碍](../research/boundary_extension_20261108/lower/README.md)给出必要内部修改数，不能解释为一般21×21不可能性。G9、S21及三色精确值仍开放。

写明命题及范围，给出完整证明或可独立重算的反例。计算结果记录输入、命令、依赖版本和输出。新结果先在独立分支讨论，并在改动当前数学稿后重跑有限核验。
