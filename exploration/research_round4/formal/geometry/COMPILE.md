# Lean compilation record

Date: 2026-09-10

Toolchain: Lean 4.19.0, `x86_64-w64-windows-gnu`, release commit
`6caaee842e94`.

Portable archive SHA-256 supplied by the root task:
`2c197a74b6d9c4d46363e34e06591165ed848237ba66de849f8b8d5539eb3895`.

Executable SHA-256:
`f59b0c515f65dbf96526279d77fb43152f76bdd77f5fb94f387b75139fafe68c`.

Source: `research_round4/formal/geometry/Geometry.lean`

Source SHA-256:
`5d6e04997fd34a9fc8785d69e944d6582c11d04b530ff12d385d80b291893503`.

Command, from the workspace root:

```powershell
& 'research_round4\tools\lean-4.19.0-windows\bin\lean.exe' 'research_round4\formal\geometry\Geometry.lean'
```

Result: native exit code `0`, empty stderr, and the following deliberate
`#print axioms` output:

```text
'Round4.Geometry.completion_avoids_source_color_on' depends on axioms: [propext, Quot.sound]
'Round4.Geometry.completion_avoids_source_color' depends on axioms: [propext, Quot.sound]
'Round4.Geometry.strictTriangle_completionClosed' depends on axioms: [propext, Quot.sound]
'Round4.Geometry.ordered_overlap_bijection' depends on axioms: [propext, Quot.sound]
'Round4.Geometry.w5_corner_list_exact' depends on axioms: [Lean.ofReduceBool]
'Round4.Geometry.w5_two_color_obstruction' depends on axioms: [propext, Lean.ofReduceBool]
```

The `Lean.ofReduceBool` dependency is the explicit trust boundary introduced
by `native_decide` for the two finite computations.  The universal geometry
theorems use only Lean's standard `propext` and quotient soundness axioms.

The file imports only `Std` and contains no `sorry`.  It formalizes:

1. positive-step color exclusion inside an arbitrary corner-free,
   completion-closed region, deriving completion membership from closure;
2. the global integer-plane color-exclusion corollary;
3. completion closure of the strict triangle `T(S)` over integer coordinates;
4. the pointwise equivalence underlying the ordered-overlap bijection;
5. the row-major 15-cell encoding of `W5`, derivation of exactly its 20
   geometric corners, and the all-`32768`-mask obstruction.

The endpoint telescope, the conversion from AP5 pairs to `W5`, the cardinality
bounds following the overlap bijection, and the inherited window-profile
certificate are not formalized here.  They remain paper proofs or independently
checked finite arithmetic, as specified in the audit report.
