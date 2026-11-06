# Directed L-grid Ramsey numbers

用于协作研究正向 L 网格拉姆齐数的数学资料库。当前论文的完整证明、构造和有限证书在 [manuscript/main.tex](manuscript/main.tex)，参考文献单独保存在 [references.bib](manuscript/references.bib)。

先读 [命题与证明索引](docs/RESULTS_INDEX.md)、[开放问题与失效路线](docs/OPEN_PROBLEMS.md) 和 [协作约定](docs/CONTRIBUTING.md)。

## 问题

正向 L 是 $`(x,y),(x+d,y),(x+d,y+d)`$，其中 $`d>0`$。
$`R_k(\mathcal L)`$ 是使每个 $`k`$ 色 $`[n]^2`$ 着色都有单色 L 的最小 $`n`$。
对有限整数集 $`A`$，严格源为 $`V(A)=\{(v,u):u<v,\ u,v\in A\}`$。
本次核查的核心原始文献给出 $`21\le R_3(\mathcal L)\le493`$。文献版本、证明位置和适用范围见 [学界已有成果](literature/KNOWN_RESULTS.md)。这是已核查的基准，不声称已穷尽所有后续工作。

## 本项目当前数学结果

以下概括不省略正文中各定理的假设，引用时请查看原定理和证明。

- 精确计数：$`T=\sum_{d>0}\binom{r_d}{2}`$，$`E=2n^2-n+4T`$；$`T\le CM`$ 蕴含 $`M\le(2C+1)L`$。
- 两个不交 Golomb 类的联合碰撞计数：$`T\le\min(2M,M+5\rho)`$，以及类大小不平衡的显式亏损与纤维矩估计。局部纤维界不能直接当作整体源界。
- 任意可正常二染色的严格源不含完整单射五维立方体；分离四维立方体的完整120格着色达到维数四。
- 单射三维立方体至少九个 mixed corners；在2-dissociation下取到等号。
- 物理源格构成的强迫图恒等式：$`2T=M+2|E(\Gamma)|-\sum_d s_d^2`$。
- 六标记可二染色严格源的极值为 $`T=16,E=130`$；全部等号类型是 $`\{0,1,2,3,4,6\}`$ 的平移、正整数伸缩及反射。
- 非等差 $`n\ge3`$ 标记集：$`T\le\binom{n}{3}-(n-2)`$，相应能量亏损为 $`4(n-2)`$。
- 完整等差积、完整直和、配对平移的能量界分别为 $`9n^2-15n`$、$`(27n^2-25n)/2`$、$`22n^2-41n`$，须满足各自定理的完整性、分离或不交及可染色条件。
- 双距离表示给出 $`T\le6M,M\le13L`$；每个中点最多三条长点对时为 $`T\le2M,M\le5L`$，系数二渐近最优。
- 图编码 $`A_G=\{5^i+5^j:ij\in E(G)\}`$ 满足 $`T(A_G)=2C_4(G)`$，四环允许有弦；完全图族迫使普适系数至少二。
- 无单射五维立方体的高能量构造满足 $`E\ge\tfrac12n^{73/26}`$。该构造没有声称具有正常源二染色。
- S21下的条件界为 $`R_3\le379,R_4\le98777`$；适当跨度范围的存在型G9可推出 $`R_3\le361`$。这些都不是已证明的无条件改进。

## 研究目标：先 R3，后 R4

长期主线是同时提高 R3(L) 的下界、降低其上界，最终以匹配的构造和不可能性证明确定精确值。完成 R3(L) 后，再启动 R4(L) 的系统攻关。现有 R4 条件推论保留为背景，不作为当前主攻任务。

短期先核清文献基准、复现代表性证书、找出局部估计无法全局拼接的具体障碍，再提出能够解释共享完成格兼容性的结构引理。每轮工作应交付一个完整证明或明确反例，而不只是更大的搜索规模。

原创方法是核心目标。已有对角线、区间和 Golomb 方法作为比较基准；SAT、枚举和 Lean 用于发现、反驳和核验。仅调整旧方法的参数或扩大暴力搜索，不单独作为原创机制的完成标准。

详细分期、上下界两条路线及验收标准见 [研究路线图](docs/ROADMAP.md)。

新研究记录：[三维立方体源的最少强迫边与九步平衡](research/three_cube_forcing/README.md)。给出正的 2-dissociated 三维源族内的完整证明、独立枚举和最多九次合法单格改色的规则；尚不推出一般源界或新的 Ramsey 数值界。

## 学界成果与项目成果分开查阅

- [学界已有成果与原始出处](literature/KNOWN_RESULTS.md)：两色精确值、三色已知界、密度定理和相关输入。
- [文献数据库](literature/references.bib)：相关文献条目，含本轮补充的两色结果来源。
- [本项目命题与证明索引](docs/RESULTS_INDEX.md)：论文中的结果与证明，不能据此自动认定优先权。
- [开放假设与失效路线](docs/OPEN_PROBLEMS.md)：避免把条件界或已被否定的前提当作现有上界。

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
