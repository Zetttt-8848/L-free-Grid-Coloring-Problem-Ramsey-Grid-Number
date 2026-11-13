# GitHub Math Typesetting Conventions

Complex inline formulas use the dollar sign plus backtick delimited format officially supported by GitHub, and key formulas use independent math fences. Avoid writing formulas containing vertical bars directly in Markdown tables, and set curly braces must retain LaTeX escapes. Project custom commands such as \F should expand into standard commands in Markdown. Historical tex/latex code fences are source code displays and should not be mistaken for rendering failures.

Based on: [GitHub Mathematical Expression Official Description](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions). Check against the repository page, other clients may not support the same syntax.
