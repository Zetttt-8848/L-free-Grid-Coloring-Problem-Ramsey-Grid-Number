#!/usr/bin/env python3
"""Independent audit checker; shares no code with audit_incidence.py."""

import argparse
import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path


def independent_sides():
    full = set(range(4))
    answer = []
    for mask in range(1, 15):
        side = {c for c in range(4) if (2 ** c) & mask}
        if min(side) == 0:
            answer.append(side)
    assert len(answer) == 7
    return [(side, full - side) for side in answer]


def independent_signature(colors, partitions):
    used = set(colors)
    return {i for i, (left, right) in enumerate(partitions)
            if used.issubset(left) or used.issubset(right)}


def independent_multiplicity(n, s, x, y, d):
    if d % s:
        return 0
    r = d // s
    if not 1 <= r <= 4:
        return 0
    axes = []
    for t in (x, y):
        count = 0
        for i in range(5 - r):
            origin = t - s * i
            if 0 <= origin and origin + 4 * s < n:
                count += 1
        axes.append(count)
    return axes[0] * axes[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("witness", type=Path)
    parser.add_argument("results", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    witness = json.loads(args.witness.read_text(encoding="utf-8"))
    data = json.loads(args.results.read_text(encoding="utf-8"))
    grid = witness["rows"]
    partitions = independent_sides()

    histogram = {}
    for code in range(64):
        colors = (code % 4, (code // 4) % 4, (code // 16) % 4)
        used = len(set(colors))
        size = len(independent_signature(colors, partitions))
        assert size == 2 ** (4 - used) - 1
        key = f"{used}_colors_signature_{size}"
        histogram[key] = histogram.get(key, 0) + 1
    assert histogram == data["signature_word_counts"]

    host = []
    for d in range(1, 6):
        for x in range(6 - d):
            for y in range(6 - d):
                host.append((x, y, d))
    assert len(host) == 55
    counts = {d: 0 for d in range(1, 5)}
    actual_q = 0
    actual_r = 0
    for x, y, d in host:
        triple = ((x, y), (x + d, y), (x + d, y + d))
        colors = tuple(grid[a][b] for a, b in triple)
        assert len(set(colors)) >= 2
        sig = independent_signature(colors, partitions)
        assert len(sig) in (1, 3)
        if d <= 4:
            counts[d] += 1
        m = independent_multiplicity(6, 1, x, y, d)
        actual_q += len(sig) * m
        actual_r += m * (len(set(colors)) == 3)
    assert counts == {d: (6 - d) ** 2 for d in range(1, 5)}
    assert counts == {int(d): v for d, v in data["proper_witness"]["P_d"].items()}
    lhs = sum((Fraction(counts[d], (5 - d) ** 2) for d in range(1, 5)),
              Fraction(0))
    assert lhs == Fraction(1381, 144) < 12
    assert lhs == Fraction(data["proper_witness"]["old_Q3a_lhs"])
    assert Fraction(data["proper_witness"]["shortfall"]) == 12 - lhs
    assert sum(counts.values()) == 54  # Step 5 contributes the remaining L.

    for entry in data["position_independent_multiplicity_counterexamples"]:
        x, y, d = entry["L"]
        assert independent_multiplicity(entry["n"], 1, x, y, d) == 1
        assert entry["actual_multiplicity"] == 1
        assert entry["old_claimed_multiplicity"] == 16

    checked_multiplicities = 0
    for row in data["scale_identities"]:
        n, s = row["n"], row["scale"]
        entries = []
        for d in range(1, n):
            for x in range(n - d):
                for y in range(n - d):
                    m = independent_multiplicity(n, s, x, y, d)
                    entries.append((x, y, d, m))
        digest = hashlib.sha256(json.dumps(
            sorted(entries), separators=(",", ":")).encode("ascii")).hexdigest()
        assert digest == row["multiplicity_sha256"]
        assert sum(item[3] for item in entries) == 30 * (n - 4 * s) ** 2
        assert row["copies"] == (n - 4 * s) ** 2
        assert row["host_Ls"] == len(entries)
        assert row["total_copy_L_incidences"] == 30 * row["copies"]
        checked_multiplicities += len(entries)

    for improper in (False, True):
        block_counts = []
        for a in range(2):
            for b in range(2):
                count = 0
                for x, y, d in host:
                    if not (a <= x and x + d < a + 5
                            and b <= y and y + d < b + 5):
                        continue
                    colors = ((0, 0, 0) if improper else
                              (grid[x][y], grid[x + d][y], grid[x + d][y + d]))
                    if independent_signature(colors, partitions):
                        count += 1
                block_counts.append(count)
        assert block_counts == [30] * 4
        key = ("improper_6_block_pair_tight_counts" if improper else
               "proper_6_block_pair_tight_counts")
        assert block_counts == data[key]

    qdata = data["quotient_incidence_6_scale_1"]
    assert actual_q == qdata["actual"]
    assert actual_r == qdata["rainbow_incidence"]
    assert actual_q == 90 * 4 - 2 * actual_r
    assert actual_q >= 30 * 4 > 7 * 4
    assert Fraction(qdata["seven_quotient_rainbow_upper"]) == 166
    assert qdata["trivial_rainbow_upper"] == 120

    result = {
        "status": "PASS",
        "python": platform.python_version(),
        "independent_implementation": True,
        "checked_color_words": 64,
        "checked_proper_witness_Ls": 55,
        "checked_scale_rows": len(data["scale_identities"]),
        "checked_multiplicity_entries": checked_multiplicities,
        "old_Q3a_lhs": str(lhs),
        "old_Q3a_rhs": 12,
        "conclusion": "Q3a is false; Q1 and Q2 are not refuted by this audit",
        "ramsey_bound_change": False,
    }
    encoded = json.dumps(result, indent=2) + "\n"
    args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")


if __name__ == "__main__":
    main()
