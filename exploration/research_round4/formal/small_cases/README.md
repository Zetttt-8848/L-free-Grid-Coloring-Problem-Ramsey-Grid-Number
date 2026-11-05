# Formal small cases

`SmallCases.lean` uses Lean 4.19.0 with its bundled `Std.Tactic.BVDecide`. It defines the actual positive-step directed corner on a finite square, proves that every Boolean coloring of the side-5 square has a corner, and proves that the displayed side-4 coloring has none. Restriction to smaller squares and monotonicity therefore give the exact existing result R₂(L)=5. This is verification of a baseline result, not a research improvement.

The universal side-5 statement is obtained from a Boolean tautology containing all 30 actual geometric corners, instantiated at the 25 cell colors. `bv_decide` obtains and checks an LRAT proof; it is not accepting a raw SAT-solver status. Its proof reflection uses `Lean.ofReduceBool`, so the Lean compiler is part of the trusted computing base. The side-4 proof explicitly enumerates coordinate cases using `omega` and simplification and does not use that native-reduction axiom.

The literal side-4 witness, with `false=0` and `true=1`, is:

```
0 0 0 0
0 1 0 1
1 0 0 1
0 0 1 1
```

The source compiles with exit code 0. The unused-variable warning for the isolated cell (0,4) is harmless. The actual `#print axioms` outputs and source/executable hashes are captured in `../compilation_gate_0001/`. No named theorem depends on `sorryAx`. The general-k and four-color proofs have not been formalized by this file.

R₁(L)=2 has the direct written proof: a side-1 board has no positive-step corner; the side-2 board contains C(0,0;1), which is necessarily monochromatic in one color. No finite computation is needed for this baseline.
