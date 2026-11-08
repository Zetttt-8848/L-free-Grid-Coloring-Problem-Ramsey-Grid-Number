# Certified cuts and exact discrepancy repair

## 1. Lifting a finite extension obstruction

Let D be a finite set of grid cells, S⊆D a support whose colors α:S→[k] are specified. Suppose a stored complete constraint proof establishes that no coloring of D extending α avoids all of a listed collection of directed positive-step equal-leg L's. If f:D→[n]² is injective and maps every listed L to an L of the prescribed orientation, and π is any color permutation, then every proper coloring χ of [n]² satisfies

```math
\bigvee_{p\in S}\bigl(\chi(f(p))\ne\pi(\alpha(p))\bigr).
```

Proof: otherwise π⁻¹χf supplies the excluded extension of α on all of D. Every listed constraint would be satisfied because χ is proper. This contradicts the finite proof. Only cells appearing in the listed constraints need to be included in D; unused variables in the original certificate may be discarded.

Translations preserve the shape. The map H(x,y)=(-y,-x) reverses the order of its three vertices and maps an L of step d to an L of step d. Composing H with any translation also preserves it. Color permutation preserves monochromaticity. These transformations justify every cut generated here; a general rotation or coordinate swap is not silently permitted.

In the one-hot encoding, the cut is the clause of negative literals for the specified colors on f(S). It is redundant: it does not remove any proper coloring. Every discovered core used here was already accompanied by a complete finite proof tree. Newly obtained raw solver cores in adaptive runs are only heuristic guidance and are not promoted to certified hard clauses.

The generator applies these maps to 34 existing certified cores in a full 21 square and produces 22,680 distinct clauses. Its independent checker revalidates the underlying proof trees, independently reconstructs the geometric maps, and compares the exact entire clause set hash. Generic redundant-clause lifting and symmetry reuse are established logical ideas; no claim is made that these are new SAT theory.

## 2. Complete discrepancy branching around an improper candidate

Fix a complete coloring c₀:D→[k] and radius K. A search node records a set F of committed cells and colors c(p)≠c₀(p) for p∈F. Uncommitted cells currently retain c₀. The node represents every possible target c* which agrees with these commitments and differs from c₀ on at most K cells.

If the current coloring is proper, it is a valid target. Otherwise choose any monochromatic L, e. If every point of e is committed, this node has no represented proper target. If |F|=K, it likewise has none. In other cases branch over every p∈e\F and every color a≠c₀(p), committing p to a.

**Completeness proof.** A represented proper target must disagree with the current monochromatic triple somewhere. It agrees on committed cells by definition. Thus it changes some uncommitted p∈e from c₀(p) to a different color; the corresponding child still represents that target. Every child adds exactly one original-color discrepancy, so the radius counts distinct changed cells rather than number of moves. A wrong commitment is rejected by backtracking, never silently revised inside its branch. Induction on K−|F| proves complete coverage. Different branches may overlap in represented targets; this causes repeated work, not loss of coverage.

The proof certificate stores one geometric L identifier per node in preorder. At each node the checker verifies that its three current colors agree. It reconstructs all required child branches itself. A leaf must have all points committed or have exhausted K. The checker rejects missing nodes, extra nodes, invalid L identifiers, or a nonmonochromatic selected triple. Compression is lossless zlib/base64 over little-endian uint16 identifiers, accompanied by SHA-256 of the decompressed stream.

## 3. Certified application

The complete matrix in `runs/local71.json` is **INVALID as an L-free construction**: exactly one of its 2,870 L's is monochromatic, at `(14, 6),(17, 6),(17, 9)`. The final radius 10 proof tree has 1,235,525 nodes. The standalone checker validates it and the smaller-radius records. Therefore:

> Every proper three-coloring of the 21-by-21 square, if one exists, differs from this specified matrix on at least 11 cells.

This is a finite obstruction relative to a single candidate. It neither proves that a proper 21-square exists nor excludes all such squares. No attaining repair is known, so 11 is a lower bound, not an exact distance. The example disproves the informal inference that one violated geometric constraint necessarily permits a small number of recolorings; it does not establish any general lower bound based only on violation count.

The next construction neighborhood must permit at least 11 changes to this candidate, or use a substantially different candidate. Increasing a smaller-radius search without changing its radius cannot succeed. The global Ramsey lower bound remains 21.
