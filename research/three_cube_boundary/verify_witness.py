"""Independently verify the complete fixed-boundary coloring certificate.

Python standard library only. Run from any directory:
    python3 verify_witness.py [witness.json] [--output witness_results.json]

The default input and output are beside this script. A supplied witness uses
the same schema as witness.json. This program performs no unbounded search:
it verifies two full colorings, closes the finite nonincreasing single-flip
component, and tests all smaller Hamming distances before accepting a repair.
Assertions are intentionally avoided so Python -O cannot skip the checks.
"""

import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def geometry(marks):
    """Generate corners in two independent ways and require exact agreement."""
    cells = [(v, u) for v in marks for u in marks if u < v]
    index = {cell: i for i, cell in enumerate(cells)}
    fibers = {}
    for i, (v, u) in enumerate(cells):
        fibers.setdefault(v - u, []).append(i)
    paired = []
    for offset, indices in fibers.items():
        ordered = sorted(indices, key=lambda i: cells[i][1])
        for first, third in itertools.combinations(ordered, 2):
            u, v = cells[first][1], cells[third][1]
            paired.append((first, index[v + offset, u], third))
    direct = []
    for first, (x, y) in enumerate(cells):
        for step in range(1, marks[-1] - x + 1):
            second = index.get((x + step, y))
            third = index.get((x + step, y + step))
            if second is not None and third is not None:
                direct.append((first, second, third))
    require(len(set(paired)) == len(paired), "Duplicate paired corner")
    require(set(paired) == set(direct), "The two geometric enumerations disagree")
    return cells, index, sorted(paired)


def parse_rows(rows, marks, cells):
    require(len(rows) == len(marks) - 1, "Wrong number of source rows")
    for i, row in enumerate(rows, 1):
        require(isinstance(row, str), "Every source row must be a string")
        require(len(row) == i and not set(row) - {"0", "1"}, "Invalid source row")
    colors = [int(char) for row in rows for char in row]
    require(len(colors) == len(cells), "Incomplete source coloring")
    return sum(color << i for i, color in enumerate(colors))


def verify(witness):
    require(witness.get("schema_version") == 1, "Unsupported witness schema")
    q_marks = witness["Q"]
    added = witness["added_marks"]
    require(q_marks == sorted(set(q_marks)), "Q must contain sorted distinct marks")
    require(not set(q_marks) & set(added), "Added marks must lie outside Q")
    require(len(set(added)) == len(added), "Repeated added mark")
    require(all(type(mark) is int for mark in q_marks + added), "Marks must be integers")
    marks = sorted(q_marks + added)
    cells, index, corners = geometry(marks)
    q_set = set(q_marks)
    internal = [i for i, (v, u) in enumerate(cells) if v in q_set and u in q_set]
    internal_set = set(internal)
    external = [i for i in range(len(cells)) if i not in internal_set]
    q_corners = [corner for corner in corners if set(corner) <= internal_set]
    boundary_corners = [corner for corner in corners if not set(corner) <= internal_set]
    q_fibers = {}
    for i in internal:
        v, u = cells[i]
        q_fibers.setdefault(v - u, []).append(i)

    def phi(word):
        return sum(
            sum(1 - 2 * ((word >> i) & 1) for i in fiber) ** 2
            for fiber in q_fibers.values()
        )

    def bad(word, domain=corners):
        return [corner for corner in domain if len({(word >> i) & 1 for i in corner}) == 1]

    def rows(word):
        return [
            "".join(str((word >> i) & 1) for i, (v, _) in enumerate(cells) if v == mark)
            for mark in marks[1:]
        ]

    def coordinates(indices):
        return [list(cells[i]) for i in indices]

    def describe(word):
        return {"word": word, "rows": rows(word), "phi_Q": phi(word)}

    trap = parse_rows(witness["trap_rows"], marks, cells)
    balanced = parse_rows(witness["balanced_rows"], marks, cells)
    require(not bad(trap), "Trap coloring has a monochromatic L")
    require(not bad(balanced), "Balanced coloring has a monochromatic L")
    require(all(((trap ^ balanced) >> i) & 1 == 0 for i in external), "Boundary changed")
    parity_lower_bound = sum(len(fiber) % 2 for fiber in q_fibers.values())
    require(phi(balanced) == parity_lower_bound, "Balanced witness does not attain the parity bound")
    require(phi(trap) > phi(balanced), "Trap is already optimal")

    decreasing = [i for i in internal if phi(trap ^ (1 << i)) < phi(trap)]
    internally_legal = [i for i in decreasing if not bad(trap ^ (1 << i), q_corners)]
    require(internally_legal, "There is no internally legal descent to obstruct")
    require(all(bad(trap ^ (1 << i)) for i in decreasing), "An internal descent is legal on the full source")
    require(
        all(bad(trap ^ (1 << i), boundary_corners) for i in internally_legal),
        "An I_Q candidate has no boundary blocker",
    )
    candidate_report = []
    for i in decreasing:
        changed = trap ^ (1 << i)
        candidate_report.append(
            {
                "cell": cells[i],
                "delta_phi_Q": phi(changed) - phi(trap),
                "belongs_to_I_Q": i in internally_legal,
                "internal_blocking_corners": [coordinates(c) for c in bad(changed, q_corners)],
                "boundary_blocking_corners": [coordinates(c) for c in bad(changed, boundary_corners)],
            }
        )

    # This queue visits the entire reachable closure: all legal internal flips
    # with nonpositive change in Phi_Q are considered from every reached word.
    reached = {trap}
    queue = [trap]
    for word in queue:
        for i in internal:
            neighbor = word ^ (1 << i)
            if neighbor in reached or phi(neighbor) > phi(word) or bad(neighbor):
                continue
            reached.add(neighbor)
            queue.append(neighbor)
    require(all(phi(word) > phi(balanced) for word in reached), "A nonincreasing path escapes the trap")

    repair_stages = []
    word = trap
    for block in witness["block_repair"]:
        indices = [index[tuple(cell)] for cell in block]
        require(len(indices) == len(set(indices)) and indices, "Invalid repair block")
        require(set(indices) <= internal_set, "A repair block changes an external cell")
        before_phi = phi(word)
        for i in indices:
            word ^= 1 << i
        require(not bad(word), "A simultaneous repair block makes a monochromatic L")
        require(phi(word) <= before_phi, "A repair block increases Phi_Q")
        repair_stages.append({"simultaneously_flipped_cells": block, **describe(word)})
    require(word == balanced, "Block repair does not reach the supplied balanced coloring")

    # The supplied balanced coloring bounds the search. Exhaust every smaller
    # distance; one witness at the first successful distance certifies equality.
    supplied_distance = (trap ^ balanced).bit_count()
    hamming_checked = {}
    minimum_distance = None
    nearest_witness = None
    nearest_changes = None
    for distance in range(1, supplied_distance + 1):
        checked = 0
        for changed_cells in itertools.combinations(internal, distance):
            checked += 1
            word = trap
            for i in changed_cells:
                word ^= 1 << i
            if phi(word) == parity_lower_bound and not bad(word):
                minimum_distance = distance
                nearest_witness = word
                nearest_changes = coordinates(changed_cells)
                break
        hamming_checked[str(distance)] = checked
        if minimum_distance is not None:
            break
    require(minimum_distance is not None, "No balanced coloring found within the supplied witness distance")

    unlock_index = index[tuple(witness["external_unlock_cell"])]
    require(unlock_index in external, "Unlock cell must be external")
    unlocked = trap ^ (1 << unlock_index)
    require(not bad(unlocked), "The external unlock is not legal")
    require(phi(unlocked) == phi(trap), "An external flip changed Phi_Q")
    unlocked_descents = [
        i for i in internal
        if phi(unlocked ^ (1 << i)) < phi(unlocked) and not bad(unlocked ^ (1 << i))
    ]
    require(unlocked_descents, "External flip failed to unlock an internal descent")

    observed = {
        "source_cells": len(cells),
        "source_corners": len(corners),
        "cube_cells": len(internal),
        "cube_corners": len(q_corners),
        "trap_phi_Q": phi(trap),
        "balanced_phi_Q": phi(balanced),
        "energy_decreasing_internal_flip_count": len(decreasing),
        "internally_legal_decreasing_flip_count": len(internally_legal),
        "nonincreasing_internal_closure_size": len(reached),
        "minimum_internal_hamming_distance_to_balance": minimum_distance,
        "unlocked_legal_decreasing_flip_count": len(unlocked_descents),
    }
    for key, expected in witness["expected"].items():
        require(key in observed and observed[key] == expected, f"Unexpected result for {key}")
    return {
        "status": "FINITE-CHECKED",
        "scope": "This complete finite witness; no claim that arbitrary frozen boundaries admit a balanced extension",
        "marks": marks,
        "Q": q_marks,
        "cells": cells,
        "state_encoding": "Bit i is the color of cells[i], ordered by v then u",
        "counts": observed,
        "cube_fiber_parity_lower_bound": parity_lower_bound,
        "trap": describe(trap),
        "fixed_boundary_colors": [[*cells[i], (trap >> i) & 1] for i in external],
        "candidate_definition": "I_Q consists only of internal single-cell flips that strictly lower Phi_Q and preserve properness on V(Q)",
        "energy_decreasing_internal_flips": candidate_report,
        "I_Q": coordinates(internally_legal),
        "all_I_Q_blocked_by_boundary": True,
        "balanced_same_boundary": describe(balanced),
        "nonincreasing_internal_closure": [describe(word) for word in sorted(reached)],
        "nonincreasing_internal_path_to_balance": False,
        "block_repair": repair_stages,
        "minimum_hamming_distance": {
            "distance": minimum_distance,
            "candidates_checked_by_distance": hamming_checked,
            "coverage": "Every smaller distance was exhausted; the first successful distance needs only the displayed witness",
            "changed_cells": nearest_changes,
            "balanced_witness": describe(nearest_witness),
        },
        "external_unlock": {
            "flipped_cell": cells[unlock_index],
            "new_color": (unlocked >> unlock_index) & 1,
            "unlocked_legal_decreasing_flips": coordinates(unlocked_descents),
            **describe(unlocked),
        },
    }


def main():
    directory = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("witness", nargs="?", type=Path, default=directory / "witness.json")
    parser.add_argument("--output", type=Path, default=directory / "witness_results.json")
    args = parser.parse_args()
    raw = args.witness.read_bytes()
    report = verify(json.loads(raw))
    report["provenance"] = {
        "python": platform.python_version(),
        "witness_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "counts": report["counts"], "output": str(args.output)}))


if __name__ == "__main__":
    main()
