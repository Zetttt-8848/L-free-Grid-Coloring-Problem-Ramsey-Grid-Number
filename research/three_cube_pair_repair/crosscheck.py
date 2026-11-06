"""Cross-check the C++ search and independent Python certificate reports.

No all-boundary search is rerun. The selected boundary's state list is
validated, its one/two-cell closures are reconstructed, and every pair across
the reported 750/564 cut is checked. All saved paths are repository filenames.
"""

import argparse
from datetime import datetime, timezone
import hashlib
from itertools import combinations
import json
from pathlib import Path
import platform
import subprocess


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(directory):
    search_path = directory / "search_results.json"
    verification_path = directory / "verification_results.json"
    search = json.loads(search_path.read_text())
    verified = json.loads(verification_path.read_text())
    require(search["status"] == verified["status"] == "FINITE-CHECKED", "Reports did not pass")
    require(search["Q"] == verified["Q"], "Cube marks differ")
    require(search["marks"] == verified["marks"], "Source marks differ")
    provenance = verified["provenance"]
    require(provenance["verifier_sha256"] == digest(directory / "verify.py"), "Stale Python verifier report")
    require(provenance["witness_sha256"] == digest(directory / "witness.json"), "Stale witness report")

    example = search["counterexample"]
    require(example is not None, "No counterexample in search report")
    groups = {row["boundary_word"]: row for row in search["group_counts"]}
    require(len(groups) == len(search["group_counts"]) == 256, "Incomplete boundary statistics")
    require(set(groups) == set(range(256)), "Incorrect boundary indices")
    boundary = example["boundary_word"]
    group = groups[boundary]
    counts = verified["counts"]
    require(group["proper"] == counts["same_boundary_legal_count"], "Selected-group proper count differs")
    require(group["balanced"] == counts["balanced_count"], "Selected-group balanced count differs")
    require(search["source_corner_count"] == counts["source_corners"], "Corner count differs")
    require(example["initial"] == verified["trap"], "Initial colorings differ")
    require(sum(g["proper"] for g in groups.values()) == search["source_proper_coloring_count"],
            "Search total does not equal group totals")
    require(sum(g["unreachable_with_balanced_target"] for g in groups.values())
            == search["unreachable_states_in_groups_with_balanced_targets"], "Failure totals differ")

    marks, q_marks = verified["marks"], verified["Q"]
    cells = [(v, u) for v in marks for u in marks if u < v]
    q_cells = [(v, u) for v in q_marks for u in q_marks if u < v]
    require(cells == [tuple(c) for c in verified["cells"]], "Unexpected cell ordering")
    index = {cell: i for i, cell in enumerate(cells)}
    internal_map = [index[cell] for cell in q_cells]
    external_cells = [tuple(c) for c in search["external_cell_order"]]
    fixed_colors = [[*cell, (boundary >> i) & 1] for i, cell in enumerate(external_cells)]
    require(fixed_colors == verified["fixed_boundary_colors"], "Fixed boundary differs")
    fixed_word = sum(color << index[v, u] for v, u, color in fixed_colors)
    fiber_masks = {}
    for i, (v, u) in enumerate(q_cells):
        fiber_masks[v - u] = fiber_masks.get(v - u, 0) | (1 << i)

    def phi(word):
        return sum((mask.bit_count() - 2 * (mask & word).bit_count()) ** 2
                   for mask in fiber_masks.values())

    def full_word(word):
        return fixed_word | sum(((word >> i) & 1) << j for i, j in enumerate(internal_map))

    # Reconstruct physical directed Ls independently of either saved corner list.
    corner_masks = []
    for first, (x, y) in enumerate(cells):
        for step in range(1, marks[-1] - x + 1):
            middle, last = index.get((x + step, y)), index.get((x + step, y + step))
            if middle is not None and last is not None:
                corner_masks.append((1 << first) | (1 << middle) | (1 << last))
    require(len(corner_masks) == counts["source_corners"], "Reconstructed corner count differs")
    listed = verified["all_legal_q_words"]
    all_states = set(listed)
    require(len(all_states) == len(listed) == group["proper"], "Incomplete or repeated selected-group list")
    for word in all_states:
        require(0 <= word < (1 << len(q_cells)), "Out-of-range coloring word")
        full = full_word(word)
        require(all(0 < (full & mask) < mask for mask in corner_masks), "Listed coloring is improper")
    potentials = {word: phi(word) for word in all_states}
    goals = {word for word in all_states if potentials[word] == 4}
    require(len(goals) == group["balanced"], "Recomputed balanced count differs")
    initial = example["initial"]["q_word"]
    require(initial in all_states, "Initial word is missing")
    require(full_word(initial) == example["initial"]["full_word"], "Initial full word differs")
    require(potentials[initial] == counts["trap_phi_Q"], "Initial potential differs")
    # The discovery search and exposition may select different members of the
    # same 64-state target set. Each must independently encode a valid target.
    for target in (example["balanced_same_boundary"], verified["balanced_witness"]):
        word = target["q_word"]
        require(word in goals and target["phi_Q"] == 4, "Invalid balanced target")
        full = full_word(word)
        require(full == target["full_word"], "Balanced target full word differs")
        target_rows = [
            "".join(str((full >> i) & 1) for i, (v, _) in enumerate(cells) if v == mark)
            for mark in marks[1:]
        ]
        require(target_rows == target["rows"], "Balanced target rows differ")

    flip_masks = [sum(1 << i for i in chosen)
                  for size in (1, 2) for chosen in combinations(range(len(q_cells)), size)]

    def closure(monotone):
        reached = {initial}
        queue = [initial]
        for word in queue:
            for flip in flip_masks:
                neighbor = word ^ flip
                if neighbor not in all_states or neighbor in reached:
                    continue
                if monotone and potentials[neighbor] > potentials[word]:
                    continue
                reached.add(neighbor)
                queue.append(neighbor)
        return reached

    monotone = closure(True)
    search_closure = example["closure_q_words"]
    python_closure = verified["monotone_closures_by_max_block_size"]["2"]["q_words"]
    require(len(set(search_closure)) == len(search_closure), "Duplicate C++ closure word")
    require(monotone == set(search_closure) == set(python_closure), "Entire monotone closure differs")
    require(len(monotone) == example["closure_size"] == counts["two_flip_nonincreasing_closure"],
            "Monotone closure count differs")
    require(not monotone & goals, "Monotone closure reaches a balanced state")
    component = closure(False)
    claimed_component = verified["unrestricted_components_by_max_block_size"]["2"]["q_words"]
    require(component == set(claimed_component), "Unrestricted component differs")
    require(not component & goals, "Unrestricted component contains a balanced state")
    complement = all_states - component
    require(component and complement, "The proposed cut is trivial")
    minimum, left, right = min(
        ((a ^ b).bit_count(), a, b) for a in component for b in complement
    )
    certificate = verified["cut_certificate"]
    require(minimum == certificate["minimum_cross_cut_hamming"], "Cut distance differs")
    require(len(component) == certificate["side_count"], "Cut side size differs")
    require(len(complement) == certificate["complement_count"], "Cut complement size differs")
    require(len(component) * len(complement) == certificate["all_cross_cut_pairs_checked"],
            "Cross-cut pair count differs")
    for radius in range(1, minimum):
        require(set(verified["unrestricted_components_by_max_block_size"][str(radius)]["q_words"])
                == component, "Smaller-radius component differs from the cut")
    disclosed = json.loads((directory / "discovered_witness.json").read_text())
    require(disclosed["Q"] == q_marks and disclosed["added_mark"] == search["added_mark"],
            "Discovered witness uses different marks")
    require(disclosed["trap_rows"] == example["initial"]["rows"], "Discovered initial rows differ")
    require(disclosed["balanced_rows"] == example["balanced_same_boundary"]["rows"],
            "Discovered balanced rows differ")

    try:
        version = subprocess.run(["clang++", "--version"], check=True, text=True,
                                 capture_output=True).stdout.splitlines()[:3]
        compiler = {"command": ["clang++", "--version"], "observed_version_lines": version}
    except (OSError, subprocess.CalledProcessError):
        compiler = {"command": ["clang++", "--version"], "available": False}
    filenames = [
        "search.cpp", "search_results.json", "verify.py", "verification_results.json",
        "witness.json", "discovered_witness.json", "crosscheck.py",
    ]
    return {
        "status": "PASS",
        "scope": "Selected boundary only; all-boundary search is not rerun by this cross-check",
        "boundary_word": boundary,
        "checks": {
            "selected_group_proper_count": len(all_states),
            "selected_group_balanced_count": len(goals),
            "entire_initial_witness_matches": True,
            "both_balanced_witnesses_valid_for_same_boundary": True,
            "balanced_witnesses_identical": example["balanced_same_boundary"] == verified["balanced_witness"],
            "search_balanced_q_word": example["balanced_same_boundary"]["q_word"],
            "verification_balanced_q_word": verified["balanced_witness"]["q_word"],
            "all_listed_selected_group_colorings_are_proper": True,
            "entire_monotone_two_cell_closure_matches": True,
            "monotone_two_cell_closure_size": len(monotone),
            "unrestricted_two_cell_component_size": len(component),
            "cut_complement_size": len(complement),
            "balanced_targets_on_component": len(component & goals),
            "all_cross_cut_pairs_rechecked": len(component) * len(complement),
            "minimum_cross_cut_hamming": minimum,
            "one_minimum_cross_cut_q_word_pair": [left, right],
            "every_reported_unrestricted_radius_below_cut_matches_component": True,
        },
        "coverage_note": "The selected state list contains exactly the number of distinct proper states reported independently by the C++ search. The 423000 cross-cut distances and both selected closures are recomputed here.",
        "provenance": {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "python": platform.python_version(),
            "sha256": {name: digest(directory / name) for name in filenames},
            "python_report_embedded_hashes_verified": ["witness_sha256", "verifier_sha256"],
            "search_report_has_embedded_source_hash": False,
            "search_binding_note": "Hashes bind the current search source and stored search report as cross-checked artifacts. This invocation does not rebuild or rerun the C++ search.",
            "compiler_probe_at_crosscheck_time": compiler,
            "compiler_probe_scope": "Identifies the currently available compiler, not a reconstruction of prior binary provenance.",
            "search_reproduction_commands": [
                "clang++ -O3 -std=c++17 -Wall -Wextra -pedantic search.cpp -o /tmp/cube_pair_search",
                "/tmp/cube_pair_search --mark 2 --output search_results.json",
            ],
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("crosscheck_results.json"))
    args = parser.parse_args()
    report = check(Path(__file__).resolve().parent)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "checks": report["checks"]}))


if __name__ == "__main__":
    main()
