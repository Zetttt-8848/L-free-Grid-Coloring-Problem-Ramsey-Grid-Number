# Positive-fan cycle: one forced SAT discovery (0039)

The script builds the literal source
\[
\{0,x\}\cup P\cup D\cup(x+P)\cup(x+D),
\quad x=10000,\ P=\{1000,1001,1011,1111\},\ D=\{1,10,100,111\},
\]
and includes every directed strict-source corner by the same-offset-pair completion rule.  It encodes each corner as the two clauses forbidding an all-positive or all-negative triple and submits the listed anchored signs as assumptions to one PySAT call.

The JSON retains the exact source, cells, corners, CNF clauses, forced assumptions, and raw status.  A SAT model is a raw discovery coloring; an UNSAT core, if the solver returns one, is an assumption core only.  Neither result is a universal statement about positive fans or proper sources.

The one completed call returned raw SAT, with 18 marks, 153 strict
cells, and 144 corners. These are the run's recorded counts; no solver
rerun or separate checking pass was performed. The later auxiliary
construction in POSITIVE_FAN_CYCLE_CONSTRUCTION_0039.md turns the signs
into explicit layer tables and a complete corner-type derivation.
That construction, rather than the raw verdict, is the saved finite
mathematical input delimiting the supported-graph strengthening.
