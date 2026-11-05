"""One-pass all-fibers-Golomb profile of the saved window-13 bad catalog.

The catalog's bad labels are inherited data.  This script neither runs SAT nor
reads any stored coloring; it only computes the new difference-fiber property.
"""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve()
ROOT = HERE.parents[3]
CATALOG = ROOT / "research_round3" / "joint" / "window13.json"
OUT = HERE.with_name("CUBE_FREE_CATALOG_DISCOVERY_0029.json")


def fiber_data(A: list[int]):
    source = set(A)
    output = {}
    for d in range(1, A[-1] - A[0] + 1):
        starts = [x for x in A if x + d in source]
        if not starts:
            continue
        seen, repeated = set(), []
        for x_index, x in enumerate(starts):
            for y in starts[x_index + 1:]:
                h = y - x
                if h in seen:
                    repeated.append(h)
                seen.add(h)
        output[str(d)] = {"starts": starts, "is_golomb": not repeated,
                          "repeated_positive_start_differences": repeated}
    return output


def main() -> None:
    if not CATALOG.exists():
        result = {"catalog_found": False, "requested_catalog": str(CATALOG),
                  "scope": "No catalog was rebuilt or searched by solver."}
    else:
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
        entries = []
        for item in data["minimal_bad"]:
            A = item["marks"]
            fibers = fiber_data(A)
            entries.append({"catalog_mask": item["mask"], "marks": A,
                            "span": A[-1] - A[0], "fibers": fibers,
                            "all_nonzero_difference_fibers_golomb": all(x["is_golomb"] for x in fibers.values())})
        passing = [x for x in entries if x["all_nonzero_difference_fibers_golomb"]]
        result = {"catalog_found": True, "catalog": str(CATALOG),
                  "catalog_minimal_bad_count": len(entries), "entries": entries,
                  "all_fibers_golomb_inherited_bad_supports": passing,
                  "scope": "The minimal_bad labels are inherited catalog inputs. No SAT, coloring inspection, or validation was performed; any listed support needs a new symbolic obstruction before use."}
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"catalog_found": result["catalog_found"],
                      "count": len(result.get("entries", [])),
                      "passing": len(result.get("all_fibers_golomb_inherited_bad_supports", []))}))


if __name__ == "__main__":
    main()
