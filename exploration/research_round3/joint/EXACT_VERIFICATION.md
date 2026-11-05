# Independent exact checks

The exact-verify self-test printed ENVIRONMENT OK before verdict-bearing
checks. All values below were recomputed from literal sets, mask coverage,
integer positions and the pinned table. No heuristic temperature or
floating score supplies a verdict. Timings are telemetry only.

CLAIM: total pair-indicator count at n464 | MY VALUE: 107416 | THEIR VALUE: 107416 | VERDICT: PASS | METHOD: count all integer pairs1<=i<j<=464, equivalently464*463/2.

CLAIM: number of six-APs in[464] | MY VALUE: 21298 | THEIR VALUE: 21298 | VERDICT: PASS | METHOD: independent first/last endpoint enumeration with endpoint difference divisible by5.

CLAIM: number of pairs inside the literal155-set | MY VALUE: 11935 | THEIR VALUE: 11935 | VERDICT: PASS | METHOD: independent nested literal-mark enumeration of all increasing pairs.

CLAIM: base witness violations of caps and six-AP exclusions | MY VALUE: 0 and0 | THEIR VALUE: 0 and0 | VERDICT: PASS | METHOD: verify_set.py direct pair histogram and endpoint AP enumeration.

CLAIM: maximum r_A(d) of the base witness | MY VALUE: 48 | THEIR VALUE: 48 | VERDICT: PASS | METHOD: full exact difference histogram of the literal marks.

CLAIM: first27 distances whose counts exceed45 | MY VALUE: 22 | THEIR VALUE: 22 | VERDICT: PASS | METHOD: compare the full literal difference histogram against45 at each d1..27.

CLAIM: complete width13 support counts | MY VALUE: 7147 good and1045 bad, totaling8192 | THEIR VALUE: 7147 good and1045 bad, totaling8192 | VERDICT: PASS | METHOD: independent exhaustive bitmask coverage by verified good colorings and RUP-certified bad submasks.

CLAIM: h(w) for widths1..13 | MY VALUE: (1,2,3,4,5,5,6,7,7,8,9,9,10) | THEIR VALUE: (1,2,3,4,5,5,6,7,7,8,9,9,10) | VERDICT: PASS | METHOD: independent maximization of bit_count over every certified good mask in each prefix domain.

CLAIM: minimum spans for6..10 admissible marks | MY VALUE: (6,7,9,10,12) | THEIR VALUE: (6,7,9,10,12) | VERDICT: PASS | METHOD: first width attaining each cardinality in the completely verified table, subtract1 to convert positions to span.

CLAIM: AP5 occurrences in[464] | MY VALUE: 26680 | THEIR VALUE: 26680 | VERDICT: PASS | METHOD: independent first/last enumeration where endpoint difference is divisible by4.

CLAIM: AP5 strengthened witness violations | MY VALUE: 0 cap violations,0 forbidden patterns,0 repeated-step AP5 groups | THEIR VALUE: all0 | VERDICT: PASS | METHOD: direct independent checker of ap5_600.json, all57888 patterns and26680 AP5 occurrences.

CLAIM: bounded partition candidate score | MY VALUE: 211+8*2=227 | THEIR VALUE: 227 | VERDICT: PASS | METHOD: independent sum of squared per-color cap excesses and complete count of monochromatic six-APs. This candidate FAILS feasibility.

CLAIM: normalized complete-window affine pattern count | MY VALUE: 56 shapes and543170 copies in[464] | THEIR VALUE: 56 shapes and543170 copies | VERDICT: PASS | METHOD: independent Euclidean normalization of every certified bad mask and first-endpoint copy counting.

CLAIM: strongest saved155-set violations | MY VALUE: 0 cap violations,0 among543170 forbidden copies,0 repeated-step AP5 groups | THEIR VALUE: all0 | VERDICT: PASS | METHOD: independent direct verification of witness_464_window_ap5.json.

CLAIM: uniform two-block corner identities | MY VALUE: 51 identically zero coefficient differences, all steps positive for h>=1 and b>6h | THEIR VALUE: all51 preserved corners | VERDICT: PASS | METHOD: exact coefficient subtraction, symbolic positivity through b>=6h+1, and explicit boundary/large-parameter checks.

CLAIM: initial strongest witness's parametric-family violations | MY VALUE: 7 forward and4 reflected, weighted score88 | THEIR VALUE: 11 violations, score88 | VERDICT: PASS | METHOD: independent complete enumeration of actual L,K,J starts and every forbidden start pair.

CLAIM: final parametric155-set feasibility | MY VALUE: 0 cap violations,0 among543170 window patterns,0 AP5-group violations,0 forward or reflected parametric relations | THEIR VALUE: all0 | VERDICT: PASS | METHOD: direct independent verification of witness_464_parametric.json, including every relevant h1..42 and every actual start pair.

CLAIM: final lifting core counts | MY VALUE: 9 marks,36 cells,46 corners,93 base clauses,157 RUP additions | THEIR VALUE: 9,36,46,93,157 | VERDICT: PASS | METHOD: independent reconstruction of triangle_core_v4 geometry and check of every RUP addition.

CLAIM: uniform four-mark-hook plus five-AP identities | MY VALUE: all46 coefficient differences vanish; all steps are positive for h>=1,b>4h | THEIR VALUE: all46 corner clauses persist | VERDICT: PASS | METHOD: exact affine coefficient arithmetic and symbolic positivity, with boundary and large-parameter checks.
