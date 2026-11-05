"""Fixed-seed bounded discovery for cube-free integer sources.

Each generated source is required to have every positive difference fibre
Golomb.  Each retained source receives exactly one time-limited SAT call for
the complete directed strict-source triangle encoding.  The stored statuses
are discovery outputs only.
"""

from __future__ import annotations

import json
import random
import threading
import time
from collections import defaultdict
from pathlib import Path

from pysat.solvers import Solver


OUT = Path(__file__).with_name("CUBE_FREE_COLOR_DISCOVERY_0031.json")
SEED = 310031
LIMIT = 80
SAT_SECONDS = 2.0
WALL_SECONDS = 240.0
SPANS = (32, 64, 128, 256)
SIZE_CAP = 40


def fibres(A: list[int]) -> dict[int, list[int]]:
    answer: dict[int, list[int]] = defaultdict(list)
    for i, x in enumerate(A):
        for y in A[i + 1:]:
            answer[y - x].append(x)
    return answer


def is_golomb(X: list[int]) -> bool:
    seen = set()
    for i, x in enumerate(X):
        for y in X[i + 1:]:
            delta = y - x
            if delta in seen:
                return False
            seen.add(delta)
    return True


def all_fibres_golomb(A: list[int]) -> bool:
    return all(is_golomb(starts) for starts in fibres(A).values())


def corner_count(A: list[int]) -> int:
    return sum(len(starts) * (len(starts) - 1) // 2
               for starts in fibres(A).values())


def greedy_source(span: int, rng: random.Random) -> list[int]:
    """Build one new source, choosing among random legal additions by corners."""
    A = [0]
    if rng.random() < 0.65:
        A.append(span)
    while len(A) < SIZE_CAP:
        available = [x for x in range(1, span) if x not in A]
        rng.shuffle(available)
        legal = []
        for x in available[:24]:
            trial = sorted(A + [x])
            if all_fibres_golomb(trial):
                legal.append(trial)
        if not legal:
            break
        scores = [corner_count(trial) for trial in legal]
        best = max(scores)
        A = rng.choice([trial for trial, score in zip(legal, scores) if score == best])

    # A small randomized deletion/re-addition is part of the new construction
    # family; every re-addition is still checked against the fibre condition.
    if len(A) > 7:
        delete_count = rng.randrange(0, min(4, len(A) - 5))
        interior = A[1:-1] if A[-1] == span else A[1:]
        for x in rng.sample(interior, min(delete_count, len(interior))):
            A.remove(x)
        for _ in range(20):
            x = rng.randrange(1, span)
            if x not in A and len(A) < SIZE_CAP:
                trial = sorted(A + [x])
                if all_fibres_golomb(trial):
                    A = trial
    return sorted(A)


def strict_corners(A: list[int]):
    # A fibre start pair u<v for difference d gives the directed triangle
    # ((u+d,u), (v+d,u), (v+d,v)).  This covers all source pairs directly.
    result = []
    for d, starts in fibres(A).items():
        for i, u in enumerate(starts):
            for v in starts[i + 1:]:
                result.append(((u + d, u), (v + d, u), (v + d, v)))
    return result


def sat_once(A: list[int]):
    corners = strict_corners(A)
    cells = sorted({cell for tri in corners for cell in tri})
    index = {cell: i + 1 for i, cell in enumerate(cells)}
    clauses = []
    for tri in corners:
        lits = [index[cell] for cell in tri]
        clauses.extend((lits, [-lit for lit in lits]))
    with Solver(name="g3", bootstrap_with=clauses) as solver:
        timer = threading.Timer(SAT_SECONDS, solver.interrupt)
        began = time.monotonic()
        timer.start()
        try:
            raw = solver.solve_limited(expect_interrupt=True)
            elapsed = time.monotonic() - began
            if raw is None:
                return "UNKNOWN", None, elapsed, len(corners), len(cells)
            if not raw:
                return "UNSAT", None, elapsed, len(corners), len(cells)
            model = set(solver.get_model())
            colors = {f"{v},{u}": int(index[(v, u)] in model) for v, u in cells}
            return "SAT", colors, elapsed, len(corners), len(cells)
        finally:
            timer.cancel()
            solver.clear_interrupt()


def main() -> None:
    rng, started = random.Random(SEED), time.monotonic()
    records, seen, witness = [], set(), None
    proposal = 0
    while len(records) < LIMIT and time.monotonic() - started < WALL_SECONDS:
        span = SPANS[proposal % len(SPANS)]
        proposal += 1
        A = greedy_source(span, rng)
        key = tuple(A)
        if len(A) < 3 or key in seen:
            continue
        seen.add(key)
        # This is a generation filter, not a later verification of any
        # stored source or of a solver output.
        if not all_fibres_golomb(A):
            continue
        status, colors, seconds, corners, cells = sat_once(A)
        record = {
            "proposal": proposal, "construction": "fixed_seed_greedy_add_delete",
            "span_parameter": span, "A": A, "size": len(A),
            "actual_span": A[-1] - A[0], "all_nonzero_fibres_golomb": True,
            "corner_count": corners, "cell_count": cells,
            "sat_status": status, "sat_seconds": seconds, "color_array": colors,
        }
        records.append(record)
        if status == "UNSAT":
            witness = record
            break
    result = {
        "purpose": "bounded new cube-free strict-source coloring discovery",
        "seed": SEED, "source_limit": LIMIT, "wall_time_limit_seconds": WALL_SECONDS,
        "per_source_sat_limit_seconds": SAT_SECONDS,
        "encoding": "all directed source corners from each difference-fibre start pair u<v; each triangle is constrained to be non-monochromatic",
        "records": records, "first_raw_UNSAT_lead": witness,
        "scope": "Each retained new source had one SAT call only. SAT arrays and UNSAT/UNKNOWN statuses are raw discovery data; no old coloring was read, replayed, or validated, and this bounded run proves no general statement.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"sources": len(records), "raw_statuses": [r["sat_status"] for r in records],
                      "first_raw_UNSAT": witness is not None, "elapsed": time.monotonic() - started}))


if __name__ == "__main__":
    main()
