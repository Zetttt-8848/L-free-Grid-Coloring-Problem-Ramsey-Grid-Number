# Provenance and scope

Base654cc044cad3d8ca6079a1931565a6ec44dcf2b5; date2026-11-08.
All artifacts are under this work package. No global environment package
was installed or changed. The Python exact-verification environment test
printed `ENVIRONMENT OK` before checking the final arithmetic.

## Exact proof artifact

`certificate.py` reconstructs the autocorrelation with the polynomial
formula, compares it against direct products for N=2,...,30 and86, and
evaluates the necessary inequality at464 and463 using Python integers.
There are520 formula/product comparisons. `certificate.json` records
the exact sums, gain over the independent capacities, and source hash.
The parallel geometry agent independently obtained the same N=86 kernel
and gap. Root independently reviewed the geometry and arithmetic.

Only the two external span bounds G24>=425 and G25>=480 are needed by
this proof. The complete argument is in README.md; reading those sources
and the earlier proof does not constitute a new distributed OGR replay.
No open conjecture is used by the464 implication.

## Actual discovery runs, not theorem inputs

- `fourier_scout.py`: n464,463,462,460 with separate capacities, then464
  and463 with the distinct-minimum cap;4097 frequencies,20s LP limit per
  case. The four separate-capacity cases and the joint463 case returned
  numerically feasible. Joint464 reached its time limit. All are labeled
  UNDECIDED; even the finite-frequency feasible status says nothing about
  an actual coloring or continuum Fourier feasibility. Earlier inline
  runs covered the same four separate-capacity cases.
- `kernel_scout.py`: top-eigenvector discovery at sides460,...,465 and
  support lengths50,...,120; float outputs remain discovery only. The
  positive464 value suggested a simple family. Exact scans then tried
  tents and parabolas of lengths60,...,110, plus shifted parabolas with
  integer shift parameter0,...,10. The N=86 parabola is a sufficient
  hand-checkable certificate, not a claimed globally optimal weight.
- `boundary_word_scout.py`: exact finite diagnostics on two three-color
  words, lengths5,...,9. Simultaneous palette renaming makes the first
  word a restricted-growth word, while the second is unrestricted. All
  pairs are visited, using integer masks and a population-count table;
  Numba is only a loop accelerator. Direct color comparisons check each
  maximizing witness. Maxima10,14,18,22,26 support a conjectured formula
  in this finite range, not a proof for arbitrary lengths. At K9 the
  n463 polynomial weights give deficit1122003552 and remaining gap
  -161570116; this does not prove463.

For the boundary-word diagnostic, let
`T_k=sum_c min(2,#{i<k:A_i=B_(K-k+i)=c})`. The tested objective is either
sum T_k or its stated weighted version. Such quantities bound large-ruler
minima because the same original diagonal color word supplies all the
prefixes. These additional finite observations were communicated to the
boundary-coherence route to motivate a purely combinatorial proof. They
are not dependencies of the464 proof.

An informal proposed three-color maximizing pattern was checked by the
other agent and found incorrect; it is not used or asserted here. The
stored two-color maximizing witnesses were evaluated explicitly.

Reproduction from repository root:

```text
python research/kernel_compatibility_20261108/kernel_upper/certificate.py
python research/kernel_compatibility_20261108/kernel_upper/kernel_scout.py
python research/kernel_compatibility_20261108/kernel_upper/boundary_word_scout.py
python research/kernel_compatibility_20261108/kernel_upper/fourier_scout.py --output research/kernel_compatibility_20261108/kernel_upper/fourier_results.json
```

Exact certificate checking needs only the Python standard library.
Scouts used CPython3.13.5, NumPy2.1.0 and SciPy1.16.3; the boundary scout
also uses Numba0.61.0. `OPENBLAS_NUM_THREADS=1` was set for recorded final scout
runs. Per-file source hashes are saved in the result records. Run times
are actual observations, not controlled speed benchmarks. No C++/SAT
proof, general extremal formula or global novelty claim is made.
