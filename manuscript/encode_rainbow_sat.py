#!/usr/bin/env python3
"""Encode finite directed-L rainbow searches and validate explicit models.

Standard-library only. This program does not invoke a SAT solver and does not
claim an UNSAT result or a minimum rainbow count. Coordinates are (v,u),
0 <= u < v < size; the forbidden corner is (v,u),(v+d,u),(v+d,u+d).
"""

import argparse
import itertools
import json
from pathlib import Path
import sys


class CNF:
    def __init__(self):
        self.variables = []
        self.clauses = []

    def variable(self, **description):
        self.variables.append(description)
        return len(self.variables)

    def add(self, *literals):
        self.clauses.append(tuple(literals))


def at_most(cnf, inputs, cap):
    """Sinz's sequential counter; return {(prefix_length,threshold): id}."""
    count = len(inputs)
    if cap < 0:
        cnf.add()  # An empty clause represents a false constraint.
        return {}
    if cap >= count:
        return {}
    if cap == 0:
        for value in inputs:
            cnf.add(-value)
        return {}
    counter = {
        (i, j): cnf.variable(kind="counter", prefix=i, threshold=j)
        for i in range(1, count)
        for j in range(1, cap + 1)
    }
    cnf.add(-inputs[0], counter[1, 1])
    for j in range(2, cap + 1):
        cnf.add(-counter[1, j])
    for i in range(2, count):
        cnf.add(-inputs[i - 1], counter[i, 1])
        cnf.add(-counter[i - 1, 1], counter[i, 1])
        for j in range(2, cap + 1):
            cnf.add(-inputs[i - 1], -counter[i - 1, j - 1], counter[i, j])
            cnf.add(-counter[i - 1, j], counter[i, j])
        cnf.add(-inputs[i - 1], -counter[i - 1, cap])
    cnf.add(-inputs[-1], -counter[count - 1, cap])
    return counter


def encode(size, cap):
    cnf = CNF()
    cells = [(v, u) for v in range(1, size) for u in range(v)]
    color_ids = {
        (cell, color): cnf.variable(kind="color", cell=list(cell), color=color)
        for cell in cells
        for color in range(3)
    }
    for cell in cells:
        cnf.add(*(color_ids[cell, color] for color in range(3)))
        for a, b in itertools.combinations(range(3), 2):
            cnf.add(-color_ids[cell, a], -color_ids[cell, b])
    corner_data = []
    for step in range(1, size - 1):
        for v in range(1, size - step):
            for u in range(v):
                points = ((v, u), (v + step, u), (v + step, u + step))
                rainbow = cnf.variable(kind="rainbow", base=[v, u], step=step)
                corner_data.append((points, rainbow))
                for color in range(3):
                    cnf.add(*(-color_ids[p, color] for p in points))
                for colors in itertools.permutations(range(3)):
                    cnf.add(*(-color_ids[p, c] for p, c in zip(points, colors)), rainbow)
                # If rainbow is true, each of the three colors must occur.
                # With exactly one color per cell, these clauses give the converse.
                for color in range(3):
                    cnf.add(-rainbow, *(color_ids[p, color] for p in points))
    at_most(cnf, [variable for _, variable in corner_data], cap)
    return cnf


def write_dimacs(cnf, path, size, cap):
    with path.open("w", encoding="ascii") as stream:
        stream.write("c Directed positive L on the complete strict triangle\n")
        stream.write(f"c size {size}; rainbow cap {cap}; no symmetry restrictions\n")
        stream.write("c sequential-counter encoding: Sinz, CP 2005, DOI 10.1007/11564751_73\n")
        stream.write(f"p cnf {len(cnf.variables)} {len(cnf.clauses)}\n")
        for clause in cnf.clauses:
            stream.write(" ".join(map(str, clause)) + (" " if clause else "") + "0\n")


def read_model(path):
    assignment = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith(("c", "s", "#")):
            continue
        if line in ("SAT", "SATISFIABLE"):
            continue
        if line in ("UNSAT", "UNSATISFIABLE"):
            raise ValueError("An UNSAT status is not a satisfying-assignment certificate.")
        if line.startswith("v ") or line == "v":
            line = line[1:]
        for token in line.split():
            literal = int(token)
            if literal == 0:
                continue
            variable, value = abs(literal), literal > 0
            if variable in assignment and assignment[variable] != value:
                raise ValueError(f"Conflicting values for variable {variable}.")
            assignment[variable] = value
    return assignment


def read_coloring(path, size):
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data["rows"] if isinstance(data, dict) else data
    if len(rows) != size - 1:
        raise ValueError(f"Expected {size - 1} row words.")
    colors = {}
    for v, word in enumerate(rows, 1):
        if not isinstance(word, str) or len(word) != v or any(c not in "012" for c in word):
            raise ValueError(f"Row {v} must be a {v}-character word over 0,1,2.")
        for u, color in enumerate(word):
            colors[v, u] = int(color)
    return colors


def geometric_check(colors, size, cap):
    """Re-enumerate from coordinate displacements, without encoder corner lists."""
    expected = {(x, y) for x in range(size) for y in range(x)}
    if set(colors) != expected or any(c not in (0, 1, 2) for c in colors.values()):
        raise ValueError("The model must define one valid color at every physical cell.")
    monochromatic, rainbow, total = [], [], 0
    for x, y in sorted(expected):
        for d in range(1, size):
            middle, last = (x + d, y), (x + d, y + d)
            if middle not in expected or last not in expected:
                continue
            total += 1
            values = (colors[x, y], colors[middle], colors[last])
            if len(set(values)) == 1:
                monochromatic.append([x, y, d])
            elif len(set(values)) == 3:
                rainbow.append([x, y, d])
    return {
        "cells": len(expected), "corners": total,
        "monochromatic_count": len(monochromatic), "rainbow_count": len(rainbow),
        "monochromatic_corners": monochromatic, "rainbow_corners": rainbow,
        "proper": not monochromatic, "within_cap": len(rainbow) <= cap,
        "geometrically_valid": not monochromatic and len(rainbow) <= cap,
    }


def complete_from_coloring(cnf, colors):
    """Build a candidate total assignment, not a search or a solver result."""
    assignment, rainbow_values = {}, []
    for variable, description in enumerate(cnf.variables, 1):
        kind = description["kind"]
        if kind == "color":
            value = colors[tuple(description["cell"])] == description["color"]
        elif kind == "rainbow":
            x, y = description["base"]
            d = description["step"]
            value = len({colors[x, y], colors[x + d, y], colors[x + d, y + d]}) == 3
            rainbow_values.append(value)
        else:
            value = sum(rainbow_values[:description["prefix"]]) >= description["threshold"]
        assignment[variable] = value
    return assignment


def evaluate_cnf(cnf, assignment):
    missing = [v for v in range(1, len(cnf.variables) + 1) if v not in assignment]
    failures = []
    unresolved = []
    for index, clause in enumerate(cnf.clauses, 1):
        if any(abs(lit) in assignment and assignment[abs(lit)] == (lit > 0) for lit in clause):
            continue
        if any(abs(lit) not in assignment for lit in clause):
            unresolved.append(index)
        else:
            failures.append(index)
    return {
        "complete_assignment": not missing, "missing_variable_count": len(missing),
        "false_clause_count": len(failures), "unresolved_clause_count": len(unresolved),
        "first_false_clauses": failures[:20],
        "cnf_satisfied": not missing and not failures and not unresolved,
    }


def check_assignment(cnf, assignment, size, cap):
    colors = {}
    for cell in ((v, u) for v in range(1, size) for u in range(v)):
        selected = []
        for variable, desc in enumerate(cnf.variables, 1):
            if desc["kind"] == "color" and tuple(desc["cell"]) == cell:
                if variable not in assignment:
                    raise ValueError(f"Missing color-variable assignment for cell {cell}.")
                if assignment[variable]:
                    selected.append(desc["color"])
        if len(selected) != 1:
            raise ValueError(f"Cell {cell} has {len(selected)} selected colors.")
        colors[cell] = selected[0]
    result = geometric_check(colors, size, cap)
    result.update(evaluate_cnf(cnf, assignment))
    result["valid"] = result["geometrically_valid"] and result["cnf_satisfied"]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, required=True, help="number of triangle marks, at least 3")
    parser.add_argument("--rainbow-cap", type=int, required=True, help="nonnegative rainbow upper bound")
    parser.add_argument("--output", type=Path, help="write DIMACS CNF")
    parser.add_argument("--mapping", type=Path, help="mapping JSON; defaults to OUTPUT.map.json")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check-model", type=Path, help="validate a total DIMACS-style SAT model")
    mode.add_argument("--coloring", type=Path, help="JSON list of row words; generate and check a candidate model")
    parser.add_argument("--write-model", type=Path, help="write the candidate total assignment from --coloring")
    args = parser.parse_args()
    if args.size < 3 or args.rainbow_cap < 0:
        parser.error("--size must be at least 3 and --rainbow-cap nonnegative")
    if not (args.output or args.check_model or args.coloring):
        parser.error("provide --output, --check-model, or --coloring")
    if args.write_model and not args.coloring:
        parser.error("--write-model requires --coloring")
    cnf = encode(args.size, args.rainbow_cap)
    report = {
        "size": args.size, "rainbow_cap": args.rainbow_cap,
        "variables": len(cnf.variables), "clauses": len(cnf.clauses),
        "no_unsat_or_minimality_claim": True,
    }
    if args.output:
        write_dimacs(cnf, args.output, args.size, args.rainbow_cap)
        mapping = args.mapping or args.output.with_suffix(".map.json")
        mapping.write_text(json.dumps({
            "size": args.size, "rainbow_cap": args.rainbow_cap,
            "variables": {str(i): desc for i, desc in enumerate(cnf.variables, 1)},
        }, indent=2) + "\n", encoding="utf-8")
        report.update(cnf_file=str(args.output), mapping_file=str(mapping))
    try:
        assignment = None
        if args.coloring:
            assignment = complete_from_coloring(cnf, read_coloring(args.coloring, args.size))
            if args.write_model:
                with args.write_model.open("w", encoding="ascii") as stream:
                    stream.write("c Candidate assignment derived from supplied coloring\n")
                    for start in range(1, len(cnf.variables) + 1, 20):
                        values = [i if assignment[i] else -i for i in range(start, min(start + 20, len(cnf.variables) + 1))]
                        stream.write("v " + " ".join(map(str, values)) + " 0\n")
                report["model_file"] = str(args.write_model)
        elif args.check_model:
            assignment = read_model(args.check_model)
        if assignment is not None:
            report.update(check_assignment(cnf, assignment, args.size, args.rainbow_cap))
    except (ValueError, KeyError) as error:
        report.update(valid=False, error=str(error))
    print(json.dumps(report, indent=2))
    return 0 if report.get("valid", True) else 1


if __name__ == "__main__":
    sys.exit(main())
