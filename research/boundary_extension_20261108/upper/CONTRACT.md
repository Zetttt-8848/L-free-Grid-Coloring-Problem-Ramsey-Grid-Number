# Target contract: boundary fields and repair

Base: main `080822bb1d434b164a1f42ea159d0bf148396b71`.
Relevant earlier evidence: PR 3 `a53970c49472813ac65d37428074e5c530134e76`.

For finite integer marks A, V(A) contains every cell (v,u) with u<v.
Legal means no monochromatic ((x,y),(x+d,y),(x+d,y+d)), d>0.
For Q contained in A, define signed fiber sums s_Q(d), signs 1-2c,
and Phi_Q=sum_d s_Q(d)^2. Fixed exterior means all cells V(A) minus V(Q).

Route U-field: seek a complete pair of legal colorings, with identical exterior,
for which a legal single-cell internal move decreases Phi_Q but increases
Phi_A. First uncertain step: realizability of a sufficiently opposing external
field under all geometric L constraints. A complete coloring pair suffices
for a counterexample; a failed bounded search does not prove impossibility.

Route U-response: prove an exact necessary and sufficient signature for the
legality and energy of replacing a block under fixed exterior, and determine
whether boundary legality alone loses energy information. Generic algebra alone
is not a Ramsey bound. The unresolved bridge is a globally summable budget on
all realizable signatures, avoiding repeated use of the same external resource.

Deliverables: proofs, physical coloring certificates, reproducible discovery and
independent verification, explicit provenance and remaining upper-bound gap.
This package does not claim G9/S21 or a new value of R3.
