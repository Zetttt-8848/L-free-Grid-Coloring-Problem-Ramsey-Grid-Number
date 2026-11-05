# Finite directed-L SAT encoding

`encode_rainbow_sat.py` uses only Python 3's standard library. It generates a
DIMACS CNF and a JSON variable map; it does not invoke a SAT solver. The domain is
the complete strict triangle of cells `(v,u)` with `0 <= u < v < m`.

The encoding includes exactly one of three colors at each cell, excludes every
positive monochromatic directed L, makes each rainbow variable equivalent to
the corresponding corner being rainbow, and bounds their sum by `k` using
Sinz's sequential counter (CP 2005, DOI 10.1007/11564751_73). No symmetry
restriction is imposed.

Generate the manuscript's two finite searches:

```bash
python encode_rainbow_sat.py --size 11 --rainbow-cap 4 --output rainbow_11_cap4.cnf
python encode_rainbow_sat.py --size 12 --rainbow-cap 6 --output rainbow_12_cap6.cnf
```

The companion maps are named `rainbow_11_cap4.map.json` and
`rainbow_12_cap6.map.json`. Variable numbering is deterministic for the given
size and cap. These instances have respectively 986 variables / 3672 clauses
and 1732 variables / 5745 clauses.

Check the printed row-word colorings and construct explicit total assignments:

```bash
python encode_rainbow_sat.py --size 11 --rainbow-cap 4 --coloring rainbow_11_coloring.json --write-model rainbow_11_cap4.model
python encode_rainbow_sat.py --size 12 --rainbow-cap 6 --coloring rainbow_12_coloring.json --write-model rainbow_12_cap6.model
```

A coloring JSON contains `{"rows": ["2", "20", ...]}`; row `v` must have
exactly `v` characters from `0`, `1`, `2`. `--write-model` constructs a candidate
assignment directly from this explicit coloring, including counter variables;
it performs no SAT search. The known colorings have zero monochromatic corners
and respectively 3 and 6 rainbow corners.

Validate a total model emitted by a SAT solver, or one generated above:

```bash
python encode_rainbow_sat.py --size 11 --rainbow-cap 4 --check-model rainbow_11_cap4.model
python encode_rainbow_sat.py --size 12 --rainbow-cap 6 --check-model rainbow_12_cap6.model
```

Models may contain signed integer literals with optional DIMACS `v` lines and
`0` terminators. Assign every variable of the corresponding formula. The
validator checks the CNF clauses and, separately, reconstructs the physical cell
colors and enumerates directed Ls by their coordinates, without reading TEX or
trusting auxiliary rainbow indicators. Exit status 0 means the model passed;
1 means it was rejected. JSON output gives the counts and rejection details.

`sat_encoding_checks.json` records exhaustive finite tests of the counter's
existential-auxiliary semantics for 1 through 4 inputs, and checks the two
printed colorings at feasible and restrictive caps. Rejecting a particular
coloring under a smaller cap does **not** establish that the formula is UNSAT.
No UNSAT certificate or exact minimum rainbow count is claimed by this package.
