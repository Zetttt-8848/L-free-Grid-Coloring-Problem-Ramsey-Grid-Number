# Open issues and failed routes

Prioritization see [Short-term vs. Long-term Roadmap](ROADMAP.md): Advance and solve R3 first, and then systematically study R4. These source realms are candidate routes, not destinations that must all be proven.

The general source world is currently unresolved. The following assertions are taken verbatim from the current text and are all open hypotheses. Do not rely on qualified inferences as proof of these assumptions.

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

## Excluded shortcuts

- The mere exclusion of the five-dimensional cube is not sufficient to derive a unified linear energy or angular number bound.
- Split each fiber into Golomb categories, and the color compatibility of the shared completion grid is not guaranteed.
- F11(5), F12(7), F13(17) already have complete counterexamples, and these premises of the old weighted route cannot be used.
- The current finite certificate gives a reachable upper bound on rainbow numbers and does not automatically prove the minimum.

## What to submit when collaborating?

State the proposition and scope, and give a complete proof or a counterexample that can be independently recalculated. Calculation results record input, commands, dependency versions, and output. The new results will be discussed in the independent branch first, and the limited verification will be rerun after the current mathematical draft is modified.
