# Evidence, Reproduction and Delivery Agreement

## 1. Minimum content of mathematical records

Save a resumable record in the current working directory, following the existing conventions of the warehouse; there is no requirement to create a new database or rewrite all history in order to run this skill.

```text
Issues/Work Packages:
Basic commits and related PRs:
Objects, coordinates, color numbers, quantifiers and ranges:
Precise propositions and upper/lower bound directions:
Status: PROVED/CONDITIONAL/CONJECTURE/COUNTEREXAMPLE/
      FINITE-CHECKED / UNDECIDED
Dependencies: original theorem tags, external source versions, unproven assumptions
Proof/Complete Witness/Unsatisfied Certificate Path:
Check: Enter SHA-256, checker version, command, actual coverage
Result: exact output, failure and incompleteness
Review: self-review, independent implementation, independent review or formalization, indicate the scope respectively
The first remaining gap and the next discriminant check:
```

The status may be hierarchical: the same general proposition has an analytical proof, and its representative instance also has FINITE-CHECKED data; the arithmetic check of the conditional value is PASS, but the dependent source lemma remains open. Don't erase these layers with a green master label.

## 2. Construct a certificate checker

Run in the root directory of the repository:

```sh
python .agents/skills/directed-l-grid-research/scripts/check_coloring.py coloring.json --output coloring_check.json
```

Only the Python standard library is required. Input must be explicit domain, k, and full rows; color numbered`0,…,k−1`. The first coordinate is the row index x, and the second coordinate is the column index y. String lines support only a single decimal color number; for larger k, use a list of integers. Omitted grid points, repeated marks, inconsistent line lengths, out-of-bounds colors or non-integers will be rejected.

It comes with a complete literature benchmark that has been matched value-for-value with the original text, which can be directly reproduced:

```sh
python .agents/skills/directed-l-grid-research/scripts/check_coloring.py .agents/skills/directed-l-grid-research/assets/paper20.json
```

You should get 400 squares, 2,470 angles, and zero monochromatic angles. Attribution and provenance versions are saved in JSON's provenance; this is a recurrence of the original lower bound.

Complete square example:

```json
{
  "domain": "square",
  "k": 2,
  "n": 2,
  "rows": [[0, 0], [1, 0]]
}
```

`rows[x][y]`is χ(x,y), starting from 0. The only geometric family checked is the forward equi-arm L for this project, other orientations are not prohibited at the same time. The legal output of an n×n square is`implied_Rk_lower_bound=n+1`; does not claim to find an optimal lower bound for k.

Strict source example (full witness of text six marks):

```json
{
  "domain": "strict-source",
  "k": 2,
  "marks": [0, 1, 2, 3, 4, 6],
  "rows": ["1", "01", "100", "0010", "11000"]
}
```

A strict source omits empty lines with the smallest token; line i has length i+1 and lists all smaller tokens. Change the weak source to`"domain":"weak-source"`, including the minimum marked row and the diagonal grid of each row. For example, a single-marked weak source can be written as`marks:[0], rows:["0"]`. The source's output T still represents the strict source angle number; the weak source enumeration total number of angles is M more than T . Source checks do not output square lower bounds.

The verifier generates L in terms of horizontal point pairs and true displacements; the source energy is recalculated from the ordered sum representation. It does not read existing CNF auxiliary variables, solver status, or old reports. Publishing important results still requires another structurally different check, such as enumerating all unordered three-point groups to determine the geometric shape; independent certificate verification does not replace the proof of universal theorems.

## 3. SAT, enumeration and precise calculation

- The coding should explain which real grid points the variables correspond to, exactly one color per grid, all L constraints, and the bidirectional semantics of the continuation of the auxiliary variables.
- Can be used for impossibilities only if symmetry constraints are proven to preserve at least one orbital representation. Mere preferences for aesthetic, periodic or reflective structures belong to a restricted family of constructions.
- SAT output first restores all true colors, and then verifies them frame by frame. Both input and full model hashes are preserved.
- UNSAT output needs to be checked for proof trace; splitting also requires complete coverage, consistent branch assumptions, and certificates for each branch. Using unchecked cut changes the original problem.
- Exhaustion must clearly state the total domain, symmetry quotient, pruning completeness, branch coverage and actual end state. The scope of partial verification is listed separately; completion records are not replaced by prediction runtime.
- Verification of final thresholds, strict inequalities and LP duality certificates with integers/rational numbers. Floating-point optimization is responsible for reconnaissance, rounding and rational reconstruction after rechecking all constraints.
- The optimal value must have both a feasible certificate and a corresponding impossibility/lower bound proof. A low rainbow witness only gives an upper bound on the minimum number of rainbows.

The dependencies, paths, and output locations of older programs may not be appropriate for your current system. Read the code and parameters first and generate new reports in the quarantine directory; no need to blindly run all historical batches, publish/archive procedures or long searches. Keep source files and old reports to record adaptation differences.

## 4. Limited verification and formalization of the main manuscript

From the repository root, specify the output path so as not to overwrite old records:

```sh
python manuscript/verify_directed_L_manuscript.py --source manuscript/main.tex --bib manuscript/references.bib --output /path/to/new-run/manuscript_checks.json
python manuscript/encode_rainbow_sat.py --size 11 --rainbow-cap 4 --check-model manuscript/sat_examples/rainbow_11_cap4.model
python manuscript/encode_rainbow_sat.py --size 12 --rainbow-cap 6 --check-model manuscript/sat_examples/rainbow_12_cap6.model
```

Will`/path/to/new-run`Change to an actual writable directory. The main validator uses assert and actively rejects`python -O`;Do not bypass this check. The small checker included with this skill does not rely on assert. The meaning of passing the main verification is based on`manuscript/README_verification.md`The item-by-item scope shall prevail and shall not be expanded to the full text to prove that it has been audited.

Lean entrance is at`formal/README.md`, the toolchain and mathlib are fixed by the current project file. When formalization is really needed, check the objects, assumptions, mappings, and axiom dependencies of the target declaration, and then build according to the instructions; do not force the installation of the entire environment for ordinary reading. The historical coverage mapping corresponds to the earlier text version, and the current new certifications and three research PRs cannot automatically inherit their certifications. Nor does a new compilation automatically prove that the artificial text and the formal declaration are exactly the same.

## 5. Novelty and literature bridge

Record the title, author, exact edition, theorem number, link to the original text, and date of retrieval. Separately examine "the source actually states this", "the assumptions that the theorem holds" and "the bridge of application to this project". Priority is given to original journal texts, author preprints and official source code.

The numerical basis of small color numbers, the direction of standard corners and directed L, and the conversion of finite fields to integers all need to be checked one by one. The search scope can be expanded from existing numerical papers and citations; the terms also search equal-leg L, right isosceles triangle, corners, Golomb/Sidon, ordered matching and actual candidate invariants.

New methods can be marked as "new attempts" within the project. If you want to claim it as original to the outside world, compare the corresponding documents and limit it to "within the search range"; no match found does not prove global priority. Do not add the full text of paid literature or third-party caches to the research repository.

## 6. Source code index refresh

Run when you need to compare new versions:

```sh
python .agents/skills/directed-l-grid-research/scripts/index_repository.py --root . --ref <full-commit> --output /path/to/new-run/source_index.json
```

`--ref`Repeatable, using confirmed commit number. Indexes are read from Git blob raw bytes to avoid Windows CRLF changing cross-platform hashes. It reads all included files, parses the text structure, and preserves navigation information such as declarations/titles. It does not execute warehouse scripts or verify proofs or historical solution results. A snapshot is created for existing indexes. When updated, a new version is generated and indicates which dependencies need to be reviewed.

## 7. Results for users

Report whether the unconditional upper and lower bounds have changed, and state separately the following results: new structural theorems, conditional inferences, finite constructions, counterexamples, checked impossibilities, method generalizations, and still open dependencies. Briefly identify the decisive mechanism and next gap, linking to actual proofs, certificates, and reports; do not represent research completion in terms of number of tools, conflicts, or documents.
