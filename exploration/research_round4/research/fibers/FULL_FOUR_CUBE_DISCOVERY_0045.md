# Full four-cube raw discovery query (0045)

This query uses \(A=\{\sum_{i=0}^{3}\epsilon_i3^i:\epsilon_i\in\{0,1\}\}\),
with generators \(1,3,9,27\), and the full strict source triangle
\(V(A)=\{(v,u):u,v\in A,\ u<v\}\). Its 120 cells are separate Boolean
variables. For every actual positive equal-step corner contained in \(V(A)\),
the query prohibits both monochromatic Boolean assignments.

This is materially different from `research/four_factor_type_probe.json`'s
`m=2, typed=true` case: it had 120 cells but only 92 variables because its
`cellkey` deliberately identifies cells having the same binary4cube order/type
key (including the reported `common0`/`common1` collapse). This query imposes
no such cross-chart or type compatibility rule.

The adjacent JSON is one bounded raw observation only. A false or interrupted
answer is not used as a mathematical obstruction or theorem.
