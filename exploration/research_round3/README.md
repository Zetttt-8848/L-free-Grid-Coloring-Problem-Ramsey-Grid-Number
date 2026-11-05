# Round 3 research checkpoint

Start with `round3_report.pdf` (the ten-section English mathematical report)
or its complete source `round3_report.tex` and included `report_*.tex` files.
Final independent review status is recorded in `audits/final_review_matrix.json`.
The release builder requires two distinct passing reviewers per core,
including an Astra reviewer, and verifies their evidence hashes.

The primary three-color interval remains **21 <= R_3(L) <= 465**. The
side-21 grid and strengthened ternary partition are undecided. No document
in this checkpoint should be read as a claim of global research exhaustion.

The new results are R_4(L)<=21,991,300,
R_5(L)<=15^16, and R_k(L)<=[k(k-2)-1]^(2^(k-1)) for k>=6, together with
the exact155-set YES and the stated geometric/finite certificates. Their
proofs and exact scope are in the report. Every conditional45/46-cap target
is explicitly conditional; it is not a three-color Ramsey improvement.

## Contents

- `joint/`: literal155-set witnesses, full window13 classification, four
  triangle RUP refutations, two uniform parameter families, bounded search
  artifacts, and append-only route history. The latest positive witness
  predates the last hook/AP5 exclusion and does not lift to a full triangle.
- `cap/`: AP5 uniqueness, endpoint inequality, exact conditional scans,
  and60 literal ruler-pair forcing certificates.
- `four/`: the561-run exact four-color certificate, complete proof,
  parameter freezes, independent arithmetic checker, and tested descent.
- `general/`: separate universal proof versions, exact scalar data,
  first-level Golomb obstruction and explicit conditional density statement.
- `overlap/`: ordered collision identity, cap bounds, exact finite checks,
  and local saturation example.
- `lower/`: side21 CNF, exact81-cube partition,33 direct unit refutations,
  all48 unresolved portfolio records, construction-family results and logs.
- `audits/`: fresh author-independent reimplementations and review reports,
  frozen reviewer assignment, manifests, and final review/release records.
- `ERRATA.md` and route correction files: preserved errors and repairs.

## Reproduction

Run commands from the package's top directory (the directory containing
`research_round3` and the inherited `research_round2`). The local audit code
uses Python3.13; some exploratory producers additionally use NumPy, SciPy,
PySAT and OR-Tools. Solver packages are not needed merely to read the
proofs and literal certificates. Individual independent review scripts
state any additional library requirements in their imports and reports.

`python research_round3/audits/root_checks.py` reproduces the root's bounded
finite checks. It is an author check, not a replacement for the distinct
reviewer implementations under `audits/`. The final review matrix identifies
the independent scripts supporting each released core result.

To rebuild the PDF, run a local LaTeX installation twice on
`round3_report.tex` from its own directory, with shell escape disabled.
No network theorem lookup is required to verify any new proof.

The release archive incorporates the exact files of the previously supplied
Round2 release, including the three source PDFs, so relative inherited
dependencies remain available. Its release manifest hashes every included
scientific file. Historical author-stage labels such as 'candidate' or
'pending review' are intentionally frozen; the final report and independent
review records govern the released status.

No discovery runtime, score, empty proof trace, interrupted solve, or raw
UNSAT response is a mathematical nonexistence certificate. The scope of
every verified negative statement is its literal instance or proved family.
