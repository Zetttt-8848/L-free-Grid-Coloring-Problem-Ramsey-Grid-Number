"""Exact, dependency-free audit of completion and three-direction counts.

Run from the repository root:
    python research/global_counting_20261108/completion/verify.py

This enumerates binary strict sources, not three-color square colorings.
No solver, floating arithmetic, or sampled properness oracle is used.
"""

from collections import defaultdict
from itertools import combinations
import hashlib
import json
from math import comb
from pathlib import Path


def geometry(marks):
    cells = [(v, u) for v in marks for u in marks if u < v]
    index = {p: i for i, p in enumerate(cells)}
    rows, columns, offsets = defaultdict(list), defaultdict(list), defaultdict(list)
    for i, (v, u) in enumerate(cells):
        rows[u].append(i)
        columns[v].append(i)
        offsets[v - u].append(i)
    triples, demands = [], defaultdict(list)
    for q, (v, u) in enumerate(cells):
        for d in range(1, v - u):
            p, r = (u + d, u), (v, v - d)
            if p in index and r in index:
                triples.append((index[p], q, index[r]))
                demands[q].append((d, index[p], index[r]))
    missing = []
    for line in rows.values():
        for i, j in combinations(line, 2):
            (a, u), (v, _) = cells[i], cells[j]
            if a > v:
                a, v = v, a
            third = (v, u + v - a)
            if third not in index:
                missing.append((i, j))
    for line in columns.values():
        for i, j in combinations(line, 2):
            (v, a), (_, b) = cells[i], cells[j]
            low, high = sorted((a, b))
            third = (v - high + low, low)
            if third not in index:
                missing.append((i, j))
    assert len(triples) == sum(comb(len(fiber), 2) for fiber in offsets.values())
    assert len(missing) == 2 * comb(len(marks), 3) - 2 * len(triples)
    return cells, rows, columns, offsets, triples, demands, missing


def count(marks, signs, data):
    cells, rows, columns, offsets, triples, demands, missing = data
    M, T = len(cells), len(triples)
    phi = sum(sum(signs[i] for i in line) ** 2 for line in offsets.values())
    row_square = sum(sum(signs[i] for i in line) ** 2 for line in rows.values())
    col_square = sum(sum(signs[i] for i in line) ** 2 for line in columns.values())
    missing_signed = sum(signs[i] * signs[j] for i, j in missing)
    mono = sum(signs[i] == signs[q] == signs[j] for i, q, j in triples)
    collision, force, fourth_minus_second, force_edges = 0, 0, 0, set()
    for q, requests in demands.items():
        hplus = sum(signs[i] == signs[j] == 1 for d, i, j in requests)
        hminus = sum(signs[i] == signs[j] == -1 for d, i, j in requests)
        h = hplus + hminus
        twice_k = sum(signs[i] + signs[j] for d, i, j in requests)
        assert twice_k % 2 == 0
        kz = twice_k // 2
        collision += hplus * hminus
        force += h
        fourth_minus_second += h * h - kz * kz
        # Literal four-cell opposite-request enumeration, not just moments.
        direct_conflicts = 0
        for (_, p1, r1), (_, p2, r2) in combinations(requests, 2):
            assert len({p1, r1, p2, r2}) == 4
            direct_conflicts += signs[p1] == signs[r1] and signs[p2] == signs[r2] and signs[p1] != signs[p2]
        assert direct_conflicts == hplus * hminus
        for d, i, j in requests:
            if signs[i] == signs[j]:
                force_edges.add(tuple(sorted((i, q))))
                force_edges.add(tuple(sorted((j, q))))
    assert 4 * collision == fourth_minus_second
    assert 8 * mono == 2 * T + phi + row_square + col_square - 3 * M - 2 * missing_signed
    assert len(force_edges) == 2 * force
    # This aggregate identity holds for improper assignments as well.
    assert 2 * T == M + 2 * len(force_edges) - phi
    if mono == 0:
        assert collision == 0
        assert 6 * T + phi + row_square + col_square <= 3 * M + 4 * comb(len(marks), 3)
        # Directly check every axis-aligned rectangular forcing four-cycle.
        index = {p: i for i, p in enumerate(cells)}
        for a, v in combinations(marks, 2):
            for u, b in combinations(marks, 2):
                points = ((a, b), (v, b), (v, u), (a, u))
                if all(p in index for p in points):
                    ids = [index[p] for p in points]
                    edges = [tuple(sorted((ids[i], ids[(i + 1) % 4]))) for i in range(4)]
                    assert not all(edge in force_edges for edge in edges)
    return {
        "M": M, "T": T, "Phi": phi, "row_square": row_square,
        "column_square": col_square, "missing_pairs": len(missing),
        "missing_signed": missing_signed, "monochromatic_L": mono,
        "collision": collision, "force": force, "force_edges": len(force_edges),
    }


def mixed_witness():
    classes = ({1, 2, 6, 7, 8}, {3, 4, 9}, {0, 5})
    diagonal = {i: c for c, marks in enumerate(classes) for i in marks}
    source = {
        (2, 1): 2, (6, 1): 2, (6, 2): 2, (7, 1): 2, (7, 2): 1,
        (7, 6): 1, (8, 1): 2, (8, 2): 1, (8, 6): 2, (8, 7): 1,
        (4, 3): 0, (9, 3): 0, (9, 4): 0, (5, 0): 0,
    }
    expected = {(v, u) for marks in classes for v in marks for u in marks if u < v}
    assert set(source) == expected
    source_L_counts = []
    for c, marks in enumerate(classes):
        data = geometry(sorted(marks))
        assert all(source[p] != c for p in data[0])
        assert all(not (source[data[0][i]] == source[data[0][q]] == source[data[0][j]]) for i, q, j in data[4])
        source_L_counts.append(len(data[4]))
    prescribed = dict(source)
    prescribed.update({(i, i): c for i, c in diagonal.items()})
    prescribed_Ls = []
    for x in range(10):
        for y in range(10):
            for d in range(1, 10 - max(x, y)):
                triple = ((x, y), (x + d, y), (x + d, y + d))
                if all(p in prescribed for p in triple):
                    prescribed_Ls.append(triple)
                    assert len({prescribed[p] for p in triple}) > 1
    total_conflicts, records = 0, []
    unavoidable, request_family, minimizing_choice = 0, [], {}
    for v in range(10):
        for u in range(v):
            a, b = diagonal[v], diagonal[u]
            if a == b:
                continue
            e = 3 - a - b
            horizontal, vertical = defaultdict(list), defaultdict(list)
            for h in range(1, u + 1):
                if u - h in classes[a] and v - h in classes[a]:
                    pair = ((v - h, u - h), (v, u - h))
                    if source[pair[0]] == source[pair[1]]:
                        horizontal[source[pair[0]]].append(pair)
            for k in range(1, 10 - v):
                if u + k in classes[b] and v + k in classes[b]:
                    pair = ((v + k, u), (v + k, u + k))
                    if source[pair[0]] == source[pair[1]]:
                        vertical[source[pair[0]]].append(pair)
            h, w = horizontal, vertical
            demand_by_color = {c: len(h[c]) + len(w[c]) for c in range(3)}
            local_min = min(demand_by_color.values())
            unavoidable += local_min
            minimizing_choice[(v, u)] = min(demand_by_color, key=demand_by_color.get)
            assert (v, u) not in prescribed
            for c in range(3):
                for pair in h[c] + w[c]:
                    assert all(p in prescribed for p in pair)
                    request_family.append(((v, u), pair, c))
            product = len(w[a]) * len(h[b]) * (len(h[e]) + len(w[e]))
            direct = 0
            for forbid_a in w[a]:
                for forbid_b in h[b]:
                    for forbid_e in h[e] + w[e]:
                        inputs = forbid_a + forbid_b + forbid_e
                        assert len(set(inputs)) == 6
                        direct += 1
                        for chosen_color in range(3):
                            bad = 0
                            for pair in (forbid_a, forbid_b, forbid_e):
                                bad += source[pair[0]] == source[pair[1]] == chosen_color
                            assert bad == 1
            assert product == direct
            total_conflicts += product
            if product:
                records.append({
                    "cell": [v, u], "diagonal_endpoint_colors": [a, b],
                    "H_by_color": {str(c): len(h[c]) for c in range(3)},
                    "V_by_color": {str(c): len(w[c]) for c in range(3)},
                    "conflict_count": product,
                })
    assert any(r["cell"] == [8, 3] for r in records)
    assert total_conflicts > 0
    assert len({tuple(sorted((q,) + pair)) for q, pair, c in request_family}) == len(request_family)
    assert sum(minimizing_choice[q] == c for q, pair, c in request_family) == unavoidable
    return {
        "n": 10, "classes": [sorted(marks) for marks in classes],
        "complete_source_prescription": [{"cell": p, "color": c} for p, c in sorted(source.items())],
        "source_L_counts": source_L_counts,
        "all_sources_proper": True,
        "all_fully_prescribed_Ls_proper": True,
        "fully_prescribed_L_count": len(prescribed_Ls),
        "mixed_conflict_count": total_conflicts,
        "minimum_monochromatic_Ls_in_listed_request_family": unavoidable,
        "listed_monochromatic_input_request_count": len(request_family),
        "conflict_cells": records,
        "scope": "Proper partial coloring has no full-square extension; not universal impossibility at n=10",
    }


def main():
    cases, assignments, proper = 0, 0, 0
    six_min, six_witness = None, None
    size_counts = defaultdict(lambda: {"sets": 0, "colorings": 0, "proper": 0})
    for size in range(7):
        for marks in combinations(range(6), size):
            data = geometry(marks)
            cases += 1
            size_counts[size]["sets"] += 1
            for mask in range(1 << len(data[0])):
                signs = tuple(1 if mask >> i & 1 else -1 for i in range(len(data[0])))
                counts = count(marks, signs, data)
                assignments += 1
                size_counts[size]["colorings"] += 1
                if counts["monochromatic_L"] == 0:
                    proper += 1
                    size_counts[size]["proper"] += 1
                if size == 6 and (six_min is None or counts["monochromatic_L"] < six_min):
                    six_min, six_witness = counts["monochromatic_L"], list(signs)
    marks = (0, 1, 2, 3)
    data = geometry(marks)
    signs = (1, -1, 1, 1, -1, 1)
    distinguishing = count(marks, signs, data)
    assert distinguishing["collision"] == 1
    assert distinguishing["monochromatic_L"] == 1
    assert distinguishing["M"] + 2 * distinguishing["force_edges"] - distinguishing["Phi"] == 2 * distinguishing["T"]
    result = {
        "status": "PASS",
        "domain": "Every subset A of {0,...,5}, every sign coloring of strict V(A)",
        "sets": cases, "binary_colorings": assignments, "proper_colorings": proper,
        "by_cardinality": dict(size_counts),
        "six_mark_interval_minimum_monochromatic_L": six_min,
        "six_mark_interval_minimizer": {
            "cells": geometry(tuple(range(6)))[0], "signs": six_witness,
        },
        "aggregate_identity_does_not_detect_conflict": {
            "marks": marks, "cells": data[0], "signs": signs, "counts": distinguishing,
        },
        "proper_sources_with_incompatible_mixed_completion": mixed_witness(),
        "claims_checked": [
            "exact monochromatic L line-square identity for all assignments",
            "second-moment collision identity and literal four-cell enumeration",
            "exact missing-completion cardinality",
            "aggregate forcing identity also holds for improper assignments",
            "proper coloring necessary inequality and rectangle exclusion",
            "complete proper partial coloring and exact cross-source six-cell demand conflicts",
        ],
        "unchanged_R3_interval": [21, 464],
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "command": ["python", "research/global_counting_20261108/completion/verify.py"],
    }
    target = Path(__file__).with_name("verification.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("status", "sets", "binary_colorings", "proper_colorings", "six_mark_interval_minimum_monochromatic_L")}))


if __name__ == "__main__":
    main()
