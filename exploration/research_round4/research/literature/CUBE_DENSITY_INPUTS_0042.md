# Cube-density inputs for strict sources (0042)

Scope: bounded local retrieval. Here K3(A) allows ordered positive generators, including repeated generators and coincident subset sums, exactly as in the active cube route. No general corners-density transfer is included.

## 1. Exact fiber/cube identities and the saved color-sensitive cube bound

WEAK_FIBER_CUBE_BALANCE_0041.md, Sections 1--3, records the bijective identities

    K1(A)=M,  K2(A)=T(A),  K3(A)=sum_(d>0) T(F_d),

with F_d=A intersect (A-d). Since every actual weak fiber is a union of two Golomb diagonal classes, its saved two-Golomb theorem gives

    T(F_d)<=2 binom(r_d,2),  K3(A)<=2T(A).

The full signed cube count is recorded exactly as

    C3(A)=m+6M+12T(A)+8K3(A),

and hence C3(A)<=m+6M+28T(A). This is a project-local identity plus the local weak-source theorem, not an imported U3 theorem.

More specifically, the same note preserves the color-dependent defect

    2T(A)-K3(A)=sum_d delta_d,

where each delta_d has three named nonnegative two-Golomb resources. It explicitly does not identify those resources across different fibers. Thus it is sharper than ambient cube monotonicity only within each fiber, not yet globally.

## 2. Finite windows retain total cube span

WEAK_FIBER_CUBE_BALANCE_0041.md, Section 4, gives the exact window identity

    K_j^(t)(A)=sum_(u in Z) K_j(A intersect [u,u+t-1])

for the weight (t-h_1-...-h_j)_+, and deduces

    K3^(t)(A)<=2K2^(t)(A).

This is applicable to repeated positive generators. Its stated limitation is essential: it weights a whole cube by the sum of all generators and does not license arbitrary separate direction weights.

## 3. The saved finite-support fourth-moment inequality

WEAK_FIBER_CUBE_BALANCE_0041.md, Section 5, applies Cauchy--Schwarz to pair-sum representations inside each fiber of span at most L-d, obtaining

    sum_(1<=d<=L) r_d^4/[2(L-d)+1]
      <=sum_d E(F_d)
      <=6sum_d r_d^2-5sum_d r_d
      =M+12T(A).

This is the direct saved relation involving source span, fiber sizes, and the two-Golomb energy theorem. It has no K3 term; combining it effectively with the cube balance remains new work.

## 4. Existing finite shifted-window energy transfer needs a uniform fiber cap

literature/FINITE_SPAN_FIBER_MOMENT_INPUTS_0041.md, Section 2, records the existing shift count: for a mark set D of span at most L, if every positive difference multiplicity is at most W, then

    |D|^2 t <= (L+t)[|D|+W(t-1)].

This is a universal finite support/moment inequality. Its hypothesis is a uniform multiplicity cap; the note expressly says the prior transfer does not sum E(F_d), T(F_d), or cube counts across d. It is a possible final conversion only after an additional global cube/fiber estimate.

## 5. Saved external higher-energy lead: hypothesis mismatch

literature/SIDON_OVERLAP_FAMILY_INPUTS_0029.md, Section 2, records I. D. Shkredov, [Energies and structure of additive sets](https://arxiv.org/abs/1405.3132), as a primary higher-energy source. The saved characterization is that its decompositions and structural consequences start from quantitative global higher-energy or sumset/difference-set assumptions for one set (including E_3). The local two-Sidon decomposition of each changing fiber F_d, and the resulting K3<=2T, do not furnish that premise. No theorem from this source therefore transfers to an upper bound on K3(A), E(A), or m here.

## 6. Other saved local structures do not close the cube sum

The same FINITE_SPAN_FIBER_MOMENT_INPUTS_0041.md maps two possible refinements: supported-difference holes in one weak fiber and the cross-class reflection first moment K<=floor(bc/2). Both have an explicit overlap warning: missing positions/outputs can recur across anchors or fibers. GRAM_BAND_SOURCE_MODELS_0022.md proves a band-energy bound for dissociated graph-sum sources via an actual trace-bounded Gram representation, but explicitly says that representation is unavailable for arbitrary proper sources.

## Bounded conclusion

The local library contains exact cube identities, a finite weighted-window identity, and the decreasing-span fourth-fiber-moment inequality above. It contains no saved primary theorem sharper than these which converts K3(A)=sum_d T(F_d), with repeated generators, into a global energy/cardinality bound from span alone under the present weak-fiber hypotheses. The named higher-energy literature has a global-premise mismatch; this is a bounded gap, not an absence or novelty claim.
