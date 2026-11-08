# Signed convolution route

For a putative n-square, choose m=ceil(n/3) marks of one diagonal color.
Write r_h for the autocorrelation of their indicator. Its Toeplitz matrices
are positive semidefinite: for every integer vector z of length n,
`m sum z_i² + 2 sum_h r_h sum_i z_i z_(i+h) >= 0`, by summing squares of
the convolution of z with the indicator (zero extended to all integers).
This is independent of G9/S21 and retains a global realizability condition
on the difference profile.

Combine exact mass `sum r_h=binom(m,2)`, the published Golomb capacities,
and integer endpoint-capacitated window bounds. Floating LP/eigenvalue
calculations only discover candidate cuts. The integer cut inequalities are
mathematically valid, but a numerical infeasible status needs an exact dual
certificate before it can prove an upper bound. A feasible relaxed profile
does not establish a real mark set or coloring.

First target n=492; stop each exploratory invocation at its declared wall
budget. If the relaxation survives, retain a checkable exact feasible profile
or a stated numerical-only observation and the precise missing constraint.
