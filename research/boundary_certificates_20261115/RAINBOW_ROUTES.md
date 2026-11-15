# Two finite rainbow targets for larger three-color improvements

Let \(T_m=\{(x,y):0\le y<x<m\}\). A proper coloring has no monochromatic directed L. A rainbow L uses all three colors.

| Local triangle | Checked coloring | Local lower bound that would be needed | Conditional grid upper bound |
|---|---:|---:|---:|
| \(T_{13}\), 78 cells, 286 Ls | 11 rainbow Ls | At least 10 in every proper coloring | 431 |
| \(T_{13}\) | Same coloring | At least 11 in every proper coloring | 392 |
| \(T_{14}\), 91 cells, 364 Ls | 17 rainbow Ls | At least 13 in every proper coloring | 438 |

The colorings in **triangle_literal_examples.json** exhibit the indicated counts. Each row string lists increasing \(y\) at one fixed \(x\). The previous [explicit 13-triangle coloring](../../exploration/research_round4/research/THIRTEEN_TRIANGLE_FOURTEEN_RAINBOW.md) has fourteen rainbows. For determining the true Ramsey number, the next finite decision on the 13-triangle route is whether a proper coloring with at most **nine** rainbows exists. The 11-rainbow example narrows this question and provides a reference for a constructive search.

The conditional implications are exact arithmetic consequences of the [manuscript's weighted embedding lemma and line identity](../../manuscript/main.tex). For nonnegative integer weights \(w_d\), define
\[
 J=\sum_{d} w_d {N-d(m-2)\choose2},
 \qquad K=\max_{1\le h\le N-2}\sum_{\substack{j\mid h\\ 1\le j\le m-2}}
                 {m-j\choose2}\,w_{h/j},
 \qquad U_N={N\choose2}-(N-1)+\lfloor(N-1)/3\rfloor .
\]
Weights beyond their support are zero. If every proper coloring of \(T_m\) has at least \(\rho\) rainbows, counting copies of \(T_m\) in the larger triangle gives \(\rho J\le K U_N\). For the three rows above the supplied weights give, respectively, \(\rho J-KU_N=208,610,242\), \(182,579,936\) and \(55,162,590\). Each would prove the stated bound if its local hypothesis is established. The unconditional three-color upper bound in this directory is [461](THREE_COLOR_461.md).

Run **python verify_rainbow_routes.py** for the literal colorings and all three integer inequalities. The independent manuscript validator also checked both assignments against the complete coordinate model, with zero violated clauses.
