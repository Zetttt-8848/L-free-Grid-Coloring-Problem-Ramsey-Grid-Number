#Scope of this round of review

The review objectives are two specific outcomes of this catalogue, not warehouse-wide certification of correctness or novelty certification.

## Upper bound work package

**Conclusion: It is established according to the scope of the article. ** The coordinator regenerates all disordered three-point combinations from the complete 45-lattice input, identifies 46 L in the specified direction, and confirms that both states are normal and only the internal grid (6,5) changes. The discoverer or its constraint generator is not imported. [Independent results](upper_witness_audit.json)

The proof of exact optimality does not require exhaustive coloring: the square of the sum of each ±1 fiber is at least an odd and even number of fiber sizes; A has 9 odd fibers, and the initial state reaches 9. With an external field of −2 fixing an external moveout value of 1, the Q balance forces the sum of this internal fiber to 0, resulting in an additional contribution of 4 from this even-numbered all-source fiber. The remaining odd-numbered fibers contribute at least 9, for a total of at least 13; the final state reaches 13. All derivation does not assume global degradation of local color changes. The universal K_Q(e) is a lower bound obtained by minimizing each allowed symbol and term by term, without assuming that the optimal symbols can be realized simultaneously.

The result of Wolfram independent arithmetic is`{45,9,{8,4},{9,13}}`, respectively, are the grid number, odd-even lower bound, local potential and total source potential. It only checks these numbers and is not responsible for coloring legality.

## Nether work package

**Conclusion: The general geometric decomposition is proved and the specific obstacles are certified within the range of the matrix shown. ** Another researcher re-deduce the bottom/right decomposition and one-sided formula from the definition, recorded in [lower_proof_review.md](lower_proof_review.md); The five groups of small parameter exhaustions are additional cross-checks and do not replace the general proof.

The coordinator writes [audit_lower_cores.py](audit_lower_cores.py), check the physical L, fixed colors and residual variables one by one, use set domain propagation to verify the contradiction of each proof leaf and the complete coverage of each branch; check the feasible witnesses after the constraints are deleted one by one, and check the accuracy and pairwise disjointness of the original grid support of the conflict kernel. The four necessary amendments 10, 2, 14, and 8 were passed. [result](lower_cores_audit.json)

These checks do not rely on the UNSAT state of the solver; deletion minimality is derived only from core unsatisfiability together with each one-sided deletion witness, and no minimum cardinality is claimed. The original color change must hit each mutually disjoint support, so the necessary modification number is obtained; there is no guarantee that all old Ls can be kept normal or the new boundaries can be completed after modification.

## External sources and calculations

The coordinator also read the original theorem conditions and the weighting steps of the two polynomial papers in 2026. Like the difference between set weight and parameter multiplicity, it can be directly recalculated from the count definition; the literature work package also authenticated this formula in the original PDF. Only [WEIGHT_AUDIT is accepted here](literature/WEIGHT_AUDIT.md)The counterexample to the equation does not extend to an error in the final density theorem.

Upper bounds, lower bounds, and literature exact arithmetic each have Mathbox v2 lists; the status completed and hashed valid indicate that the corresponding limited run can be traced, but do not mean that universal theorems are automatically proven. The main manuscript passed 13 inspections; Lean has not been newly compiled, all main manuscripts have not been audited, and all subsequent papers have not been searched exhaustively.

Note on independence: The author of the work package, another researcher and the coordinator conducted the above inspections respectively, but they were all AI-assisted work; different implementations/roles cannot rule out common errors. The original full certificate and small standard library verifier are retained for external review.
