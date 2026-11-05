"""One raw SAT discovery instance for the positive-fan monotone-cycle question.

The instance consists of every directed strict-source corner on the literal
independent-scale source and the listed forced anchored signs.  It is a
single discovery solve only; no validation or second solve is performed.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

OUT = Path(__file__).with_suffix(".json")


def build_source():
    x = 10_000
    P = [1000, 1001, 1011, 1111]
    D = [1, 10, 100, 111]
    A = sorted({0, x, *P, *D, *(x + y for y in P), *(x + h for h in D)})
    return x, P, D, A


def run():
    x, P, D, A = build_source()
    cells = [(v, u) for i, u in enumerate(A) for v in A[i + 1 :]]
    cell_id = {q: i + 1 for i, q in enumerate(cells)}
    fibers = defaultdict(list)
    for i, u in enumerate(A):
        for v in A[i + 1 :]:
            fibers[v - u].append(u)

    corners = []
    for d, starts in sorted(fibers.items()):
        for i, u in enumerate(starts):
            for v in starts[i + 1 :]:
                corners.append(((u + d, u), (v + d, u), (v + d, v)))

    clauses, clause_meta = [], []
    for triple in corners:
        ids = [cell_id[q] for q in triple]
        clauses.append(ids)
        clause_meta.append({"kind": "corner_not_all_negative", "triple": [list(q) for q in triple], "literals": ids})
        clauses.append([-q for q in ids])
        clause_meta.append({"kind": "corner_not_all_positive", "triple": [list(q) for q in triple], "literals": [-q for q in ids]})

    forced = [(cell_id[(x, 0)], +1, "f(x)=+")]
    for y in P:
        forced.extend([(cell_id[(x + y, y)], +1, f"z(x+{y},{y})=+"),
                       (cell_id[(x + y, 0)], -1, f"f(x+{y})=-")])
    for h in D:
        forced.extend([(cell_id[(x + h, h)], -1, f"z(x+{h},{h})=-"),
                       (cell_id[(x + h, 0)], +1, f"f(x+{h})=+")])
    assumptions = [sign * var for var, sign, _ in forced]

    result = {
        "scope": "one fresh pysat solve; all directed strict-source corners on the stated literal source; discovery only, no validation pass",
        "scale_symbols": {"alpha": 1, "beta": 10, "gamma": 100, "w": 1000, "x": x},
        "source": A, "P": P, "D": D,
        "cell_variables": [{"id": cell_id[q], "cell": list(q)} for q in cells],
        "corner_count": len(corners), "corners": [[list(q) for q in triple] for triple in corners],
        "clauses": clause_meta,
        "forced_conditions": [{"cell": list(cells[var - 1]), "literal": sign * var, "description": desc}
                              for var, sign, desc in forced],
    }
    try:
        from pysat.solvers import Glucose4
    except Exception as exc:
        result.update({"raw_status": "UNAVAILABLE", "runtime_error": repr(exc)})
        OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        print(result["raw_status"])
        return

    with Glucose4(bootstrap_with=clauses) as solver:
        sat = solver.solve(assumptions=assumptions)
        result["raw_status"] = "SAT" if sat else "UNSAT"
        if sat:
            model = set(solver.get_model())
            result["raw_witness_signs"] = [{"cell": list(q), "sign": "+" if cell_id[q] in model else "-"} for q in cells]
        else:
            core = solver.get_core()
            result["raw_assumption_core"] = core
            result["raw_core_conditions"] = [item for item in result["forced_conditions"] if item["literal"] in set(core or [])]
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"raw_status": result["raw_status"], "source_size": len(A), "cell_count": len(cells),
                      "corner_count": len(corners), "core_size": len(result.get("raw_assumption_core") or [])}, indent=2))


if __name__ == "__main__":
    run()
