# Independent review G / C / L

Reviewer: `joint_astra`, GPT-6 Astra, randomized assignment in `../reviewer_assignment.json`. Date: 2026-09-10. Reviewed authors: root (G,C), lower_sol (L). No author files changed; no producer or pre-existing checker code executed or imported. No new research search was performed.

**Overall: PASS for the scoped claims below. No Major issue.** One presentation scope note: the ruler certificate's word “translations” must mean the **positive shifts prescribed in CAP-P1**, not all signed translations or all ruler pairs. CAP-P1 supplies this restriction, so the mathematical claim as frozen passes. Keep the restriction in the final report.

The endpoint calculation uses the window13 table as an **external J dependency**. I authored J and do not provide an independent verdict on that table, its certificates, or its universal lifting lemmas. Release of statements depending on J requires the separately assigned reviewers' verdicts.

## Method and provenance

I reconstructed exact expressions, geometrical clauses, source-mask families and forcing implications in `independent_audit.py` using only Python integers, Fraction, and standard-library set operations. The final six execution groups all PASS. Their `_provenance.json` files bind the source hashes and final audit-script hash. The exact-verify environment self-test returned `ENVIRONMENT OK` before claim checks. Two audit-local input interpretation failures were halted, diagnosed, and recorded in `ERRATA.md`; neither was a mathematical source failure. Those failed records remain preserved.

Reproduction: run `python independent_audit.py G`, then the groups `C_triangle`, `C_forcing`, `C_endpoint`, `C_overlap`, and `L` from this directory or supply the script's path. No SAT package is required. Universal proof verdicts below come from the derivations, not the finite diagnostic ranges.

## G — per-lemma verdicts

### G1 fixed-scale capacities — PASS

The inherited completion-closed transfer is used on the actual region. For a monochromatic source S, all completing points avoid its color. Fixing a difference gives a diagonal in that same region, partitioned into at most q−1 remaining colors. Each part has the inductive capacity, so the **integer** cap is `(q−1) floor(c_(q−1) N^alpha_(q−1))`. Applying the inherited generalized Golomb theorem to this integer and only then increasing it to a real expression is valid. Empty fibers cause no problem. No cardinality-to-square inference is present.

For q=1, two distinct source points and their completion would be a corner, so the singleton base is valid. At q=2, difference multiplicity is at most one. With z=N^(1/4), the q=2 upper bound is z²+z+1; `(17/16)z²` dominates it because `z²−16z−16>=1` for z>=17. Here k>=5 gives b=k(k−2)>=3k and z>=16k², so the required lower bound holds.

At higher q put u=N^alpha_q. The exponent identities give the leading term sqrt(C)u and error C^(1/4)sqrt(u)+1, where C=(q−1)c_(q−1)<=k². Since u>=sqrt(N)>=256k⁴, the normalized error is at most `1/(16k^(3/2))+1/(256k⁴)<=1/(8k)`. Squaring positive comparison values gives the three exact gaps `81/1600,369/1600,81/1600`; adding at most1/40 closes q=3,4,5. For q>=6, r=q−2 and C=r²−1. The positive number r−1/(2r) has square C+1/(4r²), and `1/(8k)<=1/(2r)` absorbs the error. This is a universal induction over q<=k−1, including the exceptional coefficients required at small k.

### G2 partition bound — PASS

Independently expand translated unit-weight windows. The sum of total-window squares equals `N a0+2 sum_d(N−d)a_d`; the sum of same-color squares equals `N a0+2 sum_d M_d a_d`. At each window, Cauchy gives total²<=k times the color-square sum. Each color contributes r_A(d)<=V*, hence M_d<=kV*. Substitution gives exactly `sum_d(N−d−k²V*)a_d <= (k−1)Na0/2`. Both factors of k are required and are present.

For a unit interval of integer length t, a0=t and a_d=t−d for 1<=d<t. Direct sums `sum(t−d)=t(t−1)/2` and `sum d(t−d)=t(t²−1)/6` yield the displayed contradiction criterion. With b=k(k−2), exponent subtraction gives `N^(2^(2−k))=b²`. Thus delta=1/45 for k=5, and delta=1/(k−2)² for k>=6. The weaker common lower bound `1/[5(k−2)²]` is sound.

The chosen t=10k(k−2)² is integral and <=N, since N>=b⁴ and b⁴/t=k³(k−2)²/10>1. The margin is strictly greater than `kN−t²/3`, itself at least `[k⁵−(100/3)k²](k−2)^4>0` for all k>=5. All signs and strictness are justified. Therefore `R5<=15^16` and the stated first general family follow unconditionally from the inherited lemmas.

### G3 uniform improvement — PASS

For k>=5 the inequality `2^(k−1)>=(k−1)(k−2)` starts at16>=12 and propagates because `2(k−2)>=k`. Integer-exponent Bernoulli gives `(k/(k−2))^(2^(k−2))>=k`; squaring proves the desired ratio of bases is at least k². The separate inherited comparisons are `465<=3^6=729` and `22006246<=4^14=268435456`. Hence `Rk<=k^(2^k−2)` for every integer k>=3. No claim is silently extended to k=1,2.

### G4a refined capacities — PASS

For k>=6, b=k(k−2)−1>=3k, and z=N^(1/4)>=(3k)^8>=16k⁴. At q=2, z>=101 makes `z²−100z−100>=1`, giving coefficient101/100. The higher-level integer cap and exponent argument are the same valid transfer as G1. The normalized error is <=1/(8k³)<=1/1000.

For q=3..7, independent Fraction arithmetic gives exactly the five positive squared gaps listed below. For q>=8 let r=q−2. Direct expansion gives `C=r²−2−2/(r−1)` and `(r−1/r)²−C=1/r²+2/(r−1)>2/r`. With e=1/(8k³), subtracting 2(r−1/r)e and adding e² leaves a quantity strictly greater than `2/r−r/(4k³)>=2/k−1/(4k²)>0`. Both compared square roots are positive. This closes every required q, not merely tested small q.

### G4b minus-one base — PASS

For k=6,7 the exact differences `b²−k²(k−1)c_(k−1)` are respectively53/5 and194/5. For k>=8 polynomial expansion and cancellation give `2k²/(k−3)+4k+1`, strictly greater than1. The identity is also checked exactly at k=0,1,6,7,8,100; k=3 is outside its denominator domain, and those extra evaluations do not assert the theorem outside k>=8.

Thus delta>=1/b². The chosen t=2kb² is a positive integer and <=N because N>=b⁵ and b³>=2k. The required margin is strictly greater than `kN−t²/3>=kb⁴(b−4k/3)>0`. This proves `Rk<=[k(k−2)−1]^(2^(k−1))` for every integer k>=6. The coefficient treatment at k=6,7 is necessary and correct. The finite k=6..12 scalar file agrees exactly, digit-for-digit, but is only a diagnostic of this universal derivation.

### G5a/G5b and interpretation — PASS

For b_i=2pi+(i² mod p), residues change by at most p−1, so marks increase. Equality of positive differences forces equal index gaps: the residual correction has magnitude at most2p−2, less than2p. If the common gap is t, reducing modulo the odd prime p gives `2t(i−k)=0`; 1<=t<p and invertibility imply the pairs coincide. The largest mark is below2p².

The weak triangle on a Golomb set is completion closed directly from endpoint membership. A diagonal-color corner cannot have a nontrivial vertical edge. A strict-triangle-color corner would give equal positive differences `(x+d)−x=(y+d)−y` in the ruler with x>y, impossible. Translation by1 puts this literal region inside a positive square. Infinitely many odd primes yield capacities of order at least sqrt(N) at this first two-color level even with a complete0/1 multiplicity profile. This rules out a uniform o(sqrt(N)) replacement **for that region class**, not a tower reduction using additional full-grid geometry or jointly realizable deeper levels.

The separate density statement is a valid conditional pigeonhole implication. If the stated density inequality holds at the chosen integer N, then `N=floor(exp((Ck)^(1/a)))+1` has logN>(Ck)^(1/a), contradicting a color density at least1/k. It imports no unstated density theorem.

## C — per-lemma verdicts

### AP5 uniqueness and auxiliary encoding — PASS

Given starts x<x+d and common positive step a, point `(x+ja+d+sigma,x+ia)` uses actual source endpoints separated by d+(j−i)a>0. It is inside the actual grid and excludes the source color. The map from `(j,i)` is injective, common positive scaling by a followed by translation, so all corners retain a positive common side length. This is the weak5 triangle; adding(1,0) maps it bijectively to strict6. The fresh exhaustive truth-table reconstruction checks all32768 binary assignments on15 points and20 corners: none works. The equivalent fiber formulation follows by ordering the two starts. Overlap between the two source APs is allowed and does not alter the proof.

The auxiliary binary y needs only `sum five x<=4+y` and `sum_x y<=1`: a fully occupied AP forces y=1; conversely choose y to be its actual AND. Therefore this is an exact existential encoding. The index range is a=1..115 and the AP count is26680. Small ambient sides do not introduce missing points; at n=6,a=d=1 the same argument specializes correctly.

### Endpoint telescope, spacing closure and profiles — PASS, with external window dependency

Independently counting a_i's coefficient in all rank-j differences for j<=c gives `min(c,i−1)−min(c,s−i)`. Regrouping this coefficient into the c outer endpoint pairs yields the claimed telescope, including overlapping endpoint blocks. Each pair equals total span minus its two endpoint spans, so its upper bound is L−2ell_i even when negative. Summation gives the stated correction. Greedily filling distance capacities from smallest d minimizes a selected H-distance sum, so the inequality direction M(H)<=T_c is correct. If the total capacity is smaller than H the set is immediately impossible. Fixed-c contradiction excludes every larger s for which c<s.

Distinct marks give ell_i=i and correction `(c³−c)/3=2 binom(c+1,3)`. A block of i+1 points with span<w fits in w consecutive positions, so h(w)<=i forces ell_i>=w. Splitting at one shared mark proves the superadditive lower-bound closure. The independent dynamic program reproduces the displayed ell table, conditional on the supplied h(w) values. I do not certify those h(w) values independently.

All684 source rows are recomputed with the corrected position-count convention v_d=2max{j:H_j<=n−d}, all admissible c, and the explicitly specified conditional cap modifications. All7181 small endpoint identities match direct summation. The n464 inherited profile excludes159 (window-assisted best c15:54666−54214=452), while158 is not excluded (best margin−90). Without window data it also gives capacity158 (c13 exclusion margin271), so that headline itself does not require J. The conditional45 profile at n454,s152 has c11 margin29414−29390=24. The conditional46-through27 with45 at d1,2,3 at n464,s155 has c10 margin25110−25091=19. Every n=6..453 remains unexcluded by the stated conditional45-plus-window procedure; ceil(n/3) is recomputed separately at each n.

These conditional descents do not prove the45/46 hypotheses. A bound known only for one particular ambient size cannot silently be reused at another size. The source correctly labels the profiles as conditional.

### Ruler-pair forcing certificates — PASS for the frozen finite family

Fresh difference sets verify the literal23- and24-mark rulers. For each ruler, the second is optionally reflected and shifted by each integer h=1..462−span. Filtering disjoint unions gives exactly60 cases, agreeing with the certificate. Each union and every source diagonal color was rebuilt from the literal ruler, reflection and shift.

For every recorded forcing step, I check that the target is a previously unassigned weak-triangle point, the three listed points form precisely a mandated positive-step corner, and the other two have the already established opposite binary color. Then I verify the final conflict has three already known identical colors. All16425 steps pass. Exactly59 unions contain no AP5. Thus all60 negative instances have direct geometrical certificates; proofless SAT-library statuses are unnecessary.

Scope note (Minor presentation, already resolved by CAP-P1): the certificate JSON's family string omits “positive.” The60-case count is correct for CAP-P1's positive shifts, and is not a classification of all signed shifts, all pairs of optimal rulers, all46/48-point sets, or the universal45-cap.

### Ordered overlap, coarse cap, Cauchy union and saturation — PASS

Equality of outputs forces the same lower endpoint u and upper starts separated by Delta=e−d. Thus an intersection output is uniquely `(q+e,u)` with u in Bd intersect Be, q in Be intersect(Bd−Delta), and u<q. The converse uses Delta>0 to ensure u<q+Delta. This is a genuine bijection. The three source marks defining each of X and Y give injective maps into each of the difference classes d,e,Delta, proving both cardinality bounds. The intersection is also bounded by either single-shift image, each injective. Hence every entry of the minimum in O2 is valid.

Writing m(z) for output multiplicity gives sum m=M and sum m²=M+2O. Cauchy gives union size >=M²/(M+2O), and replacing O by a larger Obar weakens the lower bound in the correct direction. Ceiling is legal because the union size is integral. M=0 is treated separately. The two-color closure forces the third color and the position count on output diagonal ell is n−ell; no sparse region is substituted for a square.

Fresh set enumeration on n=1..7 verifies all26104 independent source/fiber cases and sums3491 pair intersections. Separately, the inherited literal21-point region is read as original witness data: completion closure and all its corners pass, the blue fibers are precisely B3={1,18} and B7={1,14}, and both images equal{(21,1)}. Thus M=2,O=1,union=1 genuinely saturates the bound in the local completion-closed setting. It makes no full-grid coloring claim.

## L — per-lemma verdicts

### CNF semantics, symmetry and cube cover — PASS

The independent geometry loops over x,y in0..20 and d=1..min(20−x,20−y). It generates2870 corners, equivalently sum_(d=1)^20(21−d)². Each cell's positive ternary and three negative binary clauses give exactly one color. A negative corner clause for each color forbids exactly a monochromatic mandated corner. The full geometrical clause multiset agrees with the source file.

Color permutations preserve the predicate. Relabel the origin's color as0; of the two residual colors, call the first one to appear in row-major order color1. This retains a representative even if one or both residual colors are absent. The source symmetry clauses are `[1]` and, for cell p=1..440, `[-(3p+3), 3q+2 for 1<=q<p]`. The missing q=0 literal is forced false by the fixed-origin clauses. The first such clause is therefore the correct unit[-6]. There are441 symmetry clauses,10815 total clauses,1323 variables, and the file hash matches the logged hash.

The split has four distinct cells and all3^4=81 color tuples exactly once. The literal map agrees on every cube. Exactly-one semantics make these cubes disjoint and exhaustive, irrespective of whether individual cubes are inconsistent with symmetry. No spatial symmetry quotient was used.

###33 easy refutations and48 unresolved cubes — PASS

A fresh occurrence-list unit propagator, with each cube's four positive literals inserted as units, derives contradiction for exactly the33 recorded easy orders. Every assignment records a source-clause reason; a second direct replay checks those reasons against prior assignments and checks a final falsified clause. The33 new audit traces are saved as `up_cube_XX.json`, with zero-based indices into the original CNF. This is a certificate of each scoped refutation and does not depend on empty external proof files.

The remaining48 orders are exactly the merged hard set. All81 stage1 records and all cube assumptions agree. The stage2 merge equals the original worker records, not just their order labels:24 Glucose4 records,5 returned MapleCM records,19 recovery Glucose3 records, each once. The MapleCM file's RUNNING label is an interrupted checkpoint; its unreturned sixth attempt is not counted as a result. Every merged hard status is INTERRUPTED_UNDECIDED. Recorded conflict sums are26973522,4910445,23114131. Those are exact sums of telemetry, not independent validation of solver behavior or evidence of nonexistence.

Consequently33+48=81 is complete bookkeeping, while global side21 existence remains **UNDECIDED**. No new Ramsey endpoint follows. Actual elapsed-time claims and installed-tool behavior are historical telemetry; this audit does not reconstruct external runtime from the records.

### Difference-circulant ceiling and affine scan scope — PASS

For any i<j<n the actual corner `(i,0),(j,0),(j,j−i)` is inside the grid and has residues −i,−j,−i modulo m. The first and last colors coincide, forcing pairwise distinct f(−i) over all n indices. Therefore n<=3, even when residues repeat. Equality is the literal3-by-3 matrix `1 2 3 / 3 1 2 / 2 3 1`, checked on all five corners with balanced counts3,3,3. This family theorem says nothing about unrestricted side21 colorings.

The larger modular-affine parameter count is sum_(m=2)^50 m²=42924. The three epoch counters join consecutively to26103 attempted parameters, leaving16821. All recorded negatives lack proofs and are correctly treated as raw telemetry. Neither the attempted portion nor the full parameter family receives an UNSAT verdict.

## Exact claim lines

CLAIM: R5 displayed numerical bound | MY VALUE: 6568408355712890625 | THEIR VALUE: 6568408355712890625 | VERDICT: PASS | METHOD: integer15^16 plus G1/G2 universal proof.

CLAIM: original three coefficient squared gaps | MY VALUE: 81/1600,369/1600,81/1600 | THEIR VALUE: 81/1600,369/1600,81/1600 | VERDICT: PASS | METHOD: independent rational squaring.

CLAIM: refined five coefficient squared gaps | MY VALUE: 243/31250,5761/1000000,8641/1000000,32401/1000000,230401/1000000 | THEIR VALUE: 243/31250,5761/1000000,8641/1000000,32401/1000000,230401/1000000 | VERDICT: PASS | METHOD: Fraction arithmetic from the displayed coefficients.

CLAIM: refined k6 bound | MY VALUE: 37608910510519071039902074217516707306379521 | THEIR VALUE: 37608910510519071039902074217516707306379521 | VERDICT: PASS | METHOD: integer23^32 and G4 proof.

CLAIM: refined k6 partition margin | MY VALUE: 68925828964323664149419624101576583553901223087/15 | THEIR VALUE: 68925828964323664149419624101576583553901223087/15 | VERDICT: PASS | METHOD: exact unit-window sums with t6348 and delta53/2645.

CLAIM: inherited n464 endpoint capacity | MY VALUE: 158 | THEIR VALUE: 158 | VERDICT: PASS | METHOD: literal distance multiset minimum versus endpoint telescope;159 excluded,158 unexcluded by this test.

CLAIM: conditional45 n454 margin | MY VALUE: 24 | THEIR VALUE: 24 | VERDICT: PASS | METHOD:29414−29390, c11; depends on conditional cap and external window table.

CLAIM: conditional46-plus-three n464 margin | MY VALUE: 19 | THEIR VALUE: 19 | VERDICT: PASS | METHOD:25110−25091, c10; depends on conditional cap and external window table.

CLAIM: AP5 occurrence count at464 | MY VALUE: 26680 in115 groups | THEIR VALUE: 26680 in115 groups | VERDICT: PASS | METHOD: sum_(a=1)^115(464−4a).

CLAIM: frozen ruler-family coverage and forcing | MY VALUE: 60 cases,16425 steps,59 AP5-free unions | THEIR VALUE: 60 cases,16425 steps,59 AP5-free unions | VERDICT: PASS | METHOD: positive-shift family enumeration and direct corner forcing.

CLAIM: overlap finite audit counts | MY VALUE: 26104 cases,3491 intersections | THEIR VALUE: 26104 cases,3491 intersections | VERDICT: PASS | METHOD: fresh independent set and ordered-pair enumeration.

CLAIM: side21 encoding | MY VALUE: 1323 variables,2870 corners,10815 clauses | THEIR VALUE: 1323 variables,2870 corners,10815 clauses | VERDICT: PASS | METHOD: exact geometry and full clause-multiset reconstruction.

CLAIM: side21 cube disposition | MY VALUE: 81=33 certified refutations+48 UNDECIDED | THEIR VALUE: 81=33 certified refutations+48 UNDECIDED | VERDICT: PASS | METHOD: exact tuple cover, fresh direct unit propagation, and record reconciliation.

CLAIM: difference-circulant ceiling | MY VALUE: 3, attained | THEIR VALUE: 3, attained | VERDICT: PASS | METHOD: pairwise-distinct color proof and literal five-corner witness check.

CLAIM: modular-affine accounting | MY VALUE: 42924=26103 attempted raw+16821 unattempted | THEIR VALUE: 42924=26103 attempted raw+16821 unattempted | VERDICT: PASS | METHOD: exact parameter sum and consecutive epoch counts; no negative mathematical verdict.
