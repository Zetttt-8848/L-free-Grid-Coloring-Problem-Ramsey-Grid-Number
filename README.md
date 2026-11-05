# Directed L-grid Ramsey numbers

用于协作研究正向 L 网格拉姆齐数的数学资料库。当前论文的完整证明、构造和有限证书在 [manuscript/main.tex](manuscript/main.tex)，参考文献单独保存在 [references.bib](manuscript/references.bib)。

## 问题

正向 L 是 $(x,y),(x+d,y),(x+d,y+d)$，其中 $d>0$。
$R_k(\mathcal L)$ 是使每个 $k$ 色 $[n]^2$ 着色都有单色 L 的最小 $n$。
对有限整数集 $A$，严格源为 $V(A)=\{(v,u):u<v,\ u,v\in A\}$。
本资料所引的无条件三色界为 $21\le R_3\le493$；导入未重新核查外部文献的最新界。

## 当前数学结果

以下概括不省略正文中各定理的假设，引用时请查看原定理和证明。

- 精确计数：$T=\sum_{d>0}\binom{r_d}2$，$E=2n^2-n+4T$；$T\le CM$ 蕴含 $M\le(2C+1)L$。
- 两个不交 Golomb 类的联合碰撞计数：$T\le\min(2M,M+5\rho)$，以及类大小不平衡的显式亏损与纤维矩估计。局部纤维界不能直接当作整体源界。
- 任意可正常二染色的严格源不含完整单射五维立方体；分离四维立方体的完整120格着色达到维数四。
- 单射三维立方体至少九个 mixed corners；在2-dissociation下取到等号。
- 物理源格构成的强迫图恒等式：$2T=M+2|E(\Gamma)|-\sum_d s_d^2$。
- 六标记可二染色严格源的极值为 $T=16,E=130$；全部等号类型是 $\{0,1,2,3,4,6\}$ 的平移、正整数伸缩及反射。
- 非等差 $n\ge3$ 标记集：$T\le\binom n3-(n-2)$，相应能量亏损为 $4(n-2)$。
- 完整等差积、完整直和、配对平移的能量界分别为 $9n^2-15n$、$(27n^2-25n)/2$、$22n^2-41n$，须满足各自定理的完整性、分离或不交及可染色条件。
- 双距离表示给出 $T\le6M,M\le13L$；每个中点最多三条长点对时为 $T\le2M,M\le5L$，系数二渐近最优。
- 图编码 $A_G=\{5^i+5^j:ij\in E(G)\}$ 满足 $T(A_G)=2C_4(G)$，四环允许有弦；完全图族迫使普适系数至少二。
- 无单射五维立方体的高能量构造满足 $E\ge\tfrac12n^{73/26}$。该构造没有声称具有正常源二染色。
- S21下的条件界为 $R_3\le379,R_4\le98777$；适当跨度范围的存在型G9可推出 $R_3\le361$。这些都不是已证明的无条件改进。

## 接下来攻什么

1. 是否存在所有可正常二染色严格源统一满足的 $T\le CM$？若有，必有 $C\ge2$。
2. 控制共享完成格的总体兼容性，研究强迫图预算 G9 / 存在型G9。
3. 证明或反驳 EP10、H10、S21，并精确记录跨度适用范围。
4. 缩小一般双距离系数二与六之间的差距，改善完整积常数。
5. 为当前六标记分类补齐与现有 Lean 模块之间的覆盖映射。

## 复现

```sh
cd manuscript
python verify_directed_L_manuscript.py --source main.tex --bib references.bib --output verification_results.json
latexmk -pdf main.tex
```

Python 3.10+，主核验器仅使用标准库。SAT生成与模型检查见 `manuscript/SAT_USAGE.md`。
LaTeX需要TeX Live、BibTeX、latexmk及正文所用宏包。Lean构建见 `formal/README.md`。

目录：`manuscript/` 当前证明与证书；`formal/` 形式化源码及历史覆盖记录；`exploration/` 历史探索、反例和失败路线；`docs/` 协作与状态说明。

完整论文中的个人信息、封面、致谢、辅助披露和答辩材料未导入。保留数学来源归属不等于宣称所有结果为新。此仓库不替第三方文献授予版权许可。

