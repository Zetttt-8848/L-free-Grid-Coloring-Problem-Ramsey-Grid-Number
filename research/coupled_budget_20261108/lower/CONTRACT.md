# Core-guided interior repair for a full 21-square

Base `df6e35cfff68580dc78aa91bc35d4c6399a6464a`. Target: a complete proper three-coloring of the 21-by-21 square, forbidding only `(x,y),(x+d,y),(x+d,y+d)`, d>0. A positive full matrix checked at all 2,870 L's would prove R3>=22. Budget exhaustion, raw UNSAT, or a nearly proper matrix imply no Ramsey bound.

Input: prior attributed paper20.json and independently certified disjoint support cores from `boundary_extension_20261108/lower/`. New interaction: the cells released from the interior must hit known support obstructions; later frozen-color cores select additional cells using geometry and overlap. Permanent CNF remains the complete unrestricted square formula. No core-derived hard cut is trusted without proof certification.

Primary discriminator: matched core-guided and random-thaw runs from the same old matrix, offset and wall budget. Each run is an externally bounded child process; completed rounds are checkpointed. No claim of speedup from a single seed or one pair. Alternative: whole-square local search followed by exact repair of actual conflict supports.

Deliver full source, run status and actual coverage, input and program hashes, independently checked positive/near matrices if any, and the first remaining construction gap. Core guidance uses known implicit-hitting-set ideas; the new experiment is the explicit geometric support design for this seed, not a new general SAT algorithm. The route remains open if finite experiments do not decide existence.
