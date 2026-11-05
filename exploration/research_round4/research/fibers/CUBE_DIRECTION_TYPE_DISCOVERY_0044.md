# Boolean-3-cube direction types: raw discovery (0044)

The exact type query was not found in the targeted existing-file search. One fresh SAT call was made for the first requested triple on

    A={0,1,4,5,16,17,20,21},

using all 28 strict cells and the 24 directed source corners generated from this source.

The triple (N,N,N), where each direction has a 3+1 color split among its four parallel cube-edge cells, returned raw SAT. Its complete 28-cell assignment and the three four-edge direction arrays are retained in CUBE_DIRECTION_TYPE_DISCOVERY_0044.json.

This is a direct discovery counterexample candidate to “at least two P directions”: it has no P directions. The pass stopped immediately under the requested rule. No additional type triples were called, and no validation or mathematical conclusion beyond the raw solver status is asserted.
