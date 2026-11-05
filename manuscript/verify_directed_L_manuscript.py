#!/usr/bin/env python3
"""New independent, source-bound finite verifier for the directed-L manuscript.

Python standard library only. This does not certify general proofs, establish
priority, solve the open assertions, or claim to reproduce unavailable original
SAT programs. Printed tables are read from the supplied TeX source.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
from itertools import combinations, product
import json
import math
from pathlib import Path
import platform
import re
import sys
import traceback


def enclosing(source, label, env="table"):
    marker = r"\label{" + label + "}"
    pos = source.index(marker)
    start = source.rfind(r"\begin{" + env + "}", 0, pos)
    end = source.index(r"\end{" + env + "}", pos) + len(r"\end{" + env + "}")
    assert start >= 0, (label, "no enclosing", env)
    return source[start:end]


def tabulars(block):
    return re.findall(r"\\begin\{(tabularx?)\}(.*?)\\end\{\1\}", block, re.S)


def rows(block):
    body = block.split(r"\midrule", 1)[1].split(r"\bottomrule", 1)[0]
    return [row.strip().split("&") for row in body.split(r"\\") if row.strip()]


def tex_int(cell):
    value = cell.strip().replace("$", "").replace(r"\,", "").replace(" ", "")
    assert re.fullmatch(r"-?\d+", value), ("not an integer cell", cell)
    return int(value)


def numeric_rows(block):
    return [[tex_int(cell) for cell in row] for row in rows(block)]


def cube(weights):
    return [sum(w for j, w in enumerate(weights) if mask >> j & 1)
            for mask in range(1 << len(weights))]


def direct_corners(coloring):
    """Enumerate by actual horizontal pairs, independently of difference counts."""
    by_row = defaultdict(list)
    for x, y in coloring:
        by_row[y].append(x)
    corners = []
    for y, xs in sorted(by_row.items()):
        for x, v in combinations(sorted(xs), 2):
            p, q, r = (x, y), (v, y), (v, y + v - x)
            if r in coloring:
                corners.append((p, q, r))
    assert len(corners) == len(set(corners))
    return corners


def analyze(marks, coloring, weak=False):
    marks = sorted(marks)
    assert len(marks) == len(set(marks))
    domain = {(v, u) for v in marks for u in marks if u <= v} if weak else {
        (v, u) for v in marks for u in marks if u < v}
    assert set(coloring) == domain, ("incomplete coloring", len(coloring), len(domain))
    corners = direct_corners(coloring)
    positive = Counter(v - u for u, v in combinations(marks, 2))
    signed = Counter(v - u for u in marks for v in marks)
    T = sum(math.comb(r, 2) for r in positive.values())
    E = sum(r * r for r in signed.values())
    n = len(marks)
    M = math.comb(n, 2)
    assert sum(positive.values()) == M
    assert E == 2 * n * n - n + 4 * T
    assert len(corners) == T + (M if weak else 0), (len(corners), T, weak)
    monochromatic = [cor for cor in corners if len({coloring[p] for p in cor}) == 1]
    assert not monochromatic, ("monochromatic corner", monochromatic[:3])
    mixed = sum(coloring[p] != coloring[r] for p, q, r in corners)
    rainbow = sum(len({coloring[p] for p in cor}) == 3 for cor in corners)
    report = {
        "n": n, "M": M, "span": marks[-1] - marks[0] if marks else 0,
        "cells": len(coloring), "weak_domain": weak,
        "strict_corner_count_T": T, "enumerated_corners": len(corners),
        "additive_energy_E": E, "monochromatic": 0,
        "mixed_parallel_endpoints": mixed, "rainbow": rainbow,
        "positive_difference_histogram": dict(sorted(Counter(positive.values()).items())),
    }
    if not weak and set(coloring.values()) <= {0, 1}:
        edges = set()
        forcing = 0
        per_output = Counter()
        fibers = defaultdict(list)
        for (v, u), color in coloring.items():
            fibers[v - u].append((u, color))
        Dz, Rz, Pz, K3 = 0, 0, 0, 0
        for entries in fibers.values():
            B = sorted(u for u, c in entries if c == 0)
            C = sorted(u for u, c in entries if c == 1)
            Db = {v - u for u, v in combinations(B, 2)}
            Dc = {v - u for u, v in combinations(C, 2)}
            assert len(Db) == math.comb(len(B), 2)
            assert len(Dc) == math.comb(len(C), 2)
            Dz += (len(entries) - 1) * abs(len(B) - len(C))
            Rz += len(Db & Dc)
            size, imbalance = len(entries), abs(len(B) - len(C))
            eta_twice = size * max(imbalance - 1, 0)
            assert eta_twice % 2 == 0
            eta = eta_twice // 2
            Pz += eta
            marks_in_fiber = sorted(a for a, _ in entries)
            differences_in_fiber = Counter(b - a for a, b in combinations(marks_in_fiber, 2))
            Tf = sum(math.comb(value, 2) for value in differences_in_fiber.values())
            K3 += Tf
            X = Counter(c - b for b in B for c in C if c > b)
            Y = Counter(b - c for b in B for c in C if b > c)
            Q = sum(X[h] * Y[h] for h in set(X) | set(Y))
            U = math.comb(len(B), 2) + math.comb(len(C), 2)
            assert Q <= min(U, len(B) ** 2, len(C) ** 2)
            local_M = math.comb(size, 2)
            assert 2 * Tf <= min(4 * local_M - (size - 1) * imbalance,
                                  2 * local_M + 10 * len(Db & Dc)) - 2 * eta
        for p, q, r in corners:
            if coloring[p] == coloring[r]:
                forcing += 1
                per_output[q] += 1
                assert coloring[q] != coloring[p]
                for endpoint in (p, r):
                    edge = tuple(sorted((endpoint, q)))
                    assert edge not in edges, ("edge inserted twice", edge)
                    edges.add(edge)
        s2 = sum(sum(2 * c - 1 for _, c in values) ** 2 for values in fibers.values())
        assert len(edges) == 2 * forcing
        assert 2 * T == M + 2 * len(edges) - s2
        # Independently check pointwise signed-completion and degree identities.
        degree = Counter(p for edge in edges for p in edge)
        for q, color in coloring.items():
            v, u = q
            doubled_K = 0
            for a in marks:
                d = a - u
                if not 0 < d < v - u:
                    continue
                p, r = (u + d, u), (v, v - d)
                if p in coloring and r in coloring:
                    doubled_K += 2 * coloring[p] - 1
                    doubled_K += 2 * coloring[r] - 1
            assert doubled_K % 2 == 0
            K = doubled_K // 2
            assert per_output[q] == -(2 * color - 1) * K == abs(K)
            b = sum(c == color for _, c in fibers[v - u])
            assert degree[q] == b - 1 + 2 * per_output[q]
        report.update({"forcing_corners": forcing, "forcing_graph_edges": len(edges),
                       "sum_fiber_imbalance_squared": s2,
                       "forcing_identity_checked": True, "pointwise_identity_checked": True,
                       "degree_identity_checked": True,
                       "D_z": Dz, "R_z": Rz, "P_z": Pz,
                       "K3_by_fiber_corner_count": K3,
                       "new_Q_and_eta_bounds_checked_on_tested_fibers": True})
        assert Dz % 2 == 0
        first_bound, second_bound = 2 * T - Dz // 2 - Pz, T + 5 * Rz - Pz
        assert K3 <= min(first_bound, second_bound)
        report["cube_moment_first_bound"] = first_bound
        report["cube_moment_second_bound"] = second_bound
        report["cube_moment_combined_bound"] = min(first_bound, second_bound)
    return report, corners


def verify_fourcube(source):
    blocks = tabulars(enclosing(source, "tab:fourcube"))
    assert len(blocks) == 2
    lu_rows = rows(blocks[0][1])
    L, U = {}, {}
    for row in lu_rows:
        v = tex_int(row[0]); l = row[1].strip(); u = row[2].strip()
        assert len(l) == len(u) == v and set(l + u) <= {"0", "1"}
        L[v], U[v] = l, u
    assert set(L) == set(range(1, 8))
    X = {}
    for values in numeric_rows(blocks[1][1]):
        assert len(values) == 9
        X[values[0]] = values[1:]
    assert set(X) == set(range(8))
    A = cube((1, 3, 9, 27))
    z = {}
    for v in range(16):
        for u in range(v):
            z[A[v], A[u]] = int(L[v][u] if v < 8 else U[v - 8][u - 8] if u >= 8 else X[v - 8][u])
    report, corners = analyze(A, z)
    assert (report["cells"], report["strict_corner_count_T"], report["D_z"], report["R_z"]) == (120, 200, 26, 25)
    assert report["forcing_graph_edges"] == 150
    # Validate every printed signed-support word multiplicity, not just totals.
    masks = {value: i for i, value in enumerate(A)}
    actual = defaultdict(Counter)
    for p, q, r in corners:
        if p[0] < 27 and r[0] < 27:
            family = "L"
        elif p[1] >= 27 and r[1] >= 27:
            family = "U"
        elif p[0] >= 27 and p[1] < 27 and r[0] >= 27 and r[1] < 27:
            family = "X"
        else:
            family = "Bridge"
        if family in ("L", "U", "Bridge"):
            t = (masks[p[0]] ^ masks[p[1]]).bit_count()
        else:
            t = (masks[p[0]] ^ masks[r[0]]).bit_count()
        order = (p, r, q) if family in ("L", "U") else (p, q, r)
        word = "".join(str(z[cell]) for cell in order)
        actual[family, t][word] += 1
    truth = tabulars(enclosing(source, "tab:fourtruth"))[0][1]
    printed = {}
    for row in rows(truth):
        family = row[0].strip().replace("$", "")
        t = tex_int(row[1])
        printed[family, t] = Counter({word: int(count) for word, count in re.findall(r"([01]{3})\((\d+)\)", row[2])})
    assert dict(actual) == printed, ("four-cube truth table mismatch", actual, printed)
    report["printed_word_multiplicity_rows_checked"] = len(printed)
    report["family_corner_totals"] = {f: sum(sum(c.values()) for (fam, t), c in actual.items() if fam == f)
                                      for f in ("L", "U", "X", "Bridge")}
    return report, A, z


def verify_threecube(source):
    figure = enclosing(source, "fig:cube", "figure")
    blocks = tabulars(figure)
    assert len(blocks) == 1
    printed = numeric_or_dash_array(blocks[0][1], 8)
    A = cube((1, 3, 9))
    z = {(A[v], A[u]): color for (v, u), color in printed.items()}
    for (v, u), color in printed.items():
        I, J = {i for i in range(3) if v >> i & 1}, {i for i in range(3) if u >> i & 1}
        sizes = sorted((len(I), len(J)))
        rule = sizes in ([0, 1], [0, 2], [1, 3]) or (sizes == [1, 2] and not I & J and len(I | J) == 3)
        assert color == int(rule)
    report, corners = analyze(A, z)
    assert (report["cells"], report["strict_corner_count_T"], report["mixed_parallel_endpoints"]) == (28, 24, 9)
    assert (report["forcing_corners"], report["forcing_graph_edges"], report["sum_fiber_imbalance_squared"]) == (15, 30, 40)
    records = {}
    block = tabulars(enclosing(source, "tab:threecorners"))[0][1]
    for row in rows(block):
        assert len(row) == 12
        for start in (0, 6):
            d = tex_int(row[start])
            labels = []
            for cell in row[start + 1:start + 4]:
                pair = re.fullmatch(r"\$\((\d+),(\d+)\)\$", cell.strip())
                assert pair, cell
                labels.append(tuple(map(int, pair.groups())))
            cor = tuple((A[i], A[j]) for i, j in labels)
            assert cor not in records
            assert cor[0][0] - cor[0][1] == d
            word = row[start + 4].strip()
            assert word == "".join(str(z[cell]) for cell in cor)
            mixed = z[cor[0]] != z[cor[2]]
            assert mixed == ("M" in row[start + 5])
            records[cor] = word
    assert set(records) == set(corners)
    report["printed_corner_records_checked"] = len(records)
    return report


def numeric_or_dash_array(body, size):
    result = {}
    for row in rows(body):
        v = tex_int(row[0])
        assert len(row) == size + 1
        for u, cell in enumerate(row[1:]):
            if cell.strip() == "--":
                continue
            result[v, u] = tex_int(cell)
    return result


def verify_weak(source):
    block = tabulars(enclosing(source, "tab:weak-rules"))[1][1]
    header = block.split(r"\toprule", 1)[1].split(r"\\", 1)[0].split("&")[1:]
    A = [tex_int(cell) for cell in header]
    array = numeric_or_dash_array(block, 12)
    z = {(v, A[u]): color for (v, u), color in array.items()}
    report, corners = analyze(A, z, weak=True)
    assert (len(A), report["cells"], report["strict_corner_count_T"], len(corners)) == (12, 78, 74, 140)
    assert Counter(z[a, a] for a in A) == {0: 6, 1: 6}
    assert report["positive_difference_histogram"] == {1: 1, 2: 11, 3: 8, 4: 3, 7: 1}
    certificate = tabulars(enclosing(source, "tab:weak-completions"))
    actual_groups = defaultdict(list)
    for (v, u), color in z.items():
        if v > u:
            actual_groups[v - u, color].append(u)
    actual_groups = {key: sorted(starts) for key, starts in actual_groups.items() if len(starts) >= 2}
    printed_groups = {}
    for row in rows(certificate[0][1]):
        d, c = tex_int(row[0]), tex_int(row[1])
        starts = list(map(int, re.search(r"\\\{([\d,]+)\\\}", row[2])[1].split(",")))
        completions = [tuple(map(int, pair)) for pair in re.findall(r"\((\d+),(\d+)\)", row[3])]
        expected = [(v + d, u) for u, v in combinations(starts, 2)]
        assert completions == expected
        completion_color = tex_int(row[4])
        assert all(z[cell] == completion_color == 1 - c for cell in completions)
        printed_groups[d, c] = starts
    assert printed_groups == actual_groups
    covered_offsets = set()
    for values in numeric_rows(certificate[1][1]):
        assert len(values) == 10
        for i in (0, 5):
            d, rd, bd, cd, pairs = values[i:i + 5]
            colors = [color for (v, u), color in z.items() if v - u == d]
            assert (rd, bd, cd, pairs) == (len(colors), colors.count(0), colors.count(1), math.comb(len(colors), 2))
            covered_offsets.add(d)
    assert covered_offsets == {v - u for v, u in z if v > u}
    report["positive_offset_equal_color_groups_checked"] = len(printed_groups)
    report["printed_fiber_count_records_checked"] = len(covered_offsets)
    return report


def verify_deficit(source):
    block = enclosing(source, "prop:29", "proposition")
    matches = re.findall(r"[BC]=\\\{([\d,]+)\\\}", block)
    assert len(matches) == 2
    B, C = (sorted(map(int, text.split(","))) for text in matches)
    Db = Counter(v - u for u, v in combinations(B, 2))
    Dc = Counter(v - u for u, v in combinations(C, 2))
    assert max(Db.values()) == max(Dc.values()) == 1
    X = Counter(c - b for b in B for c in C if c > b)
    Y = Counter(b - c for b in B for c in C if b > c)
    rho = len(Db.keys() & Dc.keys())
    N = sum((Db[h] + Dc[h]) * (X[h] + Y[h]) for h in set(Db) | set(Dc) | set(X) | set(Y))
    Q = sum(X[h] * Y[h] for h in set(X) | set(Y))
    assert (rho, N, Q) == (5, 29, 11)
    tables = tabulars(enclosing(source, "tab:deficit"))
    for row in numeric_rows(tables[0][1]):
        b = row[0]
        assert row[1:] == [abs(b - c) for c in C]
    for row in numeric_rows(tables[1][1]):
        h = row[0]
        assert row == [h, Db[h], Dc[h], X[h], Y[h], (Db[h] + Dc[h]) * (X[h] + Y[h]), X[h] * Y[h]]
    T = sum(math.comb(value, 2) for value in Counter(v - u for u, v in combinations(sorted(B + C), 2)).values())
    assert T == 2 * rho + N + Q == 50
    report = {"rho": rho, "N": N, "Q": Q, "T": T, "deficit": 2 * len(B) * len(C) - N,
              "all_printed_distance_and_incidence_entries_checked": True}
    if r"\textbf{The counting mechanism.}" in source:
        # These incidences are also included in the full table check above.
        # Check the newly printed explanatory examples explicitly, without
        # claiming they are new independent certificates.
        assert {0, 2, 5, 6} == set(B) and {1, 3, 4, 8} == set(C)
        assert 5 - 3 == 6 - 4 == 2 and 4 - 3 == 6 - 5 == 1
        assert 1 - 0 == 5 - 4 == 1 and 0 + 5 == 1 + 4 == 5
        assert 4 - 0 == 5 - 1 == 4
        assert 2 + 2 == 1 + 3 == 4 and 3 - 2 == 2 - 1 == 1
        assert all(token in source for token in (r"3\to5", r"4\to6", "0+5=1+4", "2+2=1+3"))
        report["worked_incidence_arithmetic_checked"] = True
        report["worked_examples_already_covered_by_complete_incidence_table"] = True
    return report


def words_coloring(words):
    z = {}
    for v, word in words.items():
        assert len(word) == v and set(word) <= {"0", "1", "2"}
        for u, color in enumerate(word):
            z[v, u] = int(color)
    return z


def verify_rainbows(source):
    if r"\label{tab:local-rainbows}" in source:
        block = tabulars(enclosing(source, "tab:local-rainbows"))[0][1]
    else:
        prop = enclosing(source, "prop:local-rainbows", "proposition")
        start = source.index(prop) + len(prop)
        end = source.index(r"\begin{proposition}", start)
        block = tabulars(source[start:end])[0][1]
    colorings = {11: {}, 12: {}}
    for row in rows(block):
        v = tex_int(row[0])
        for m, index in ((11, 1), (12, 2)):
            match = re.fullmatch(r"\\texttt\{([012]+)\}", row[index].strip())
            if match:
                colorings[m][v] = match[1]
            else:
                assert m == 11 and v == 11 and row[index].strip() == "---"
    t13 = tabulars(enclosing(source, "tab:t13literal"))
    words13 = {}
    for row in rows(t13[0][1]):
        words13[tex_int(row[0])] = re.fullmatch(r"\\texttt\{([012]+)\}", row[1].strip())[1]
    colorings[13] = words13
    expected_lists = {11: [(2, 1, 8), (6, 3, 2), (7, 3, 2)],
                      12: [(3, 2, 6), (6, 3, 2), (7, 3, 2), (8, 4, 3), (9, 8, 1), (10, 1, 1)]}
    results = {}
    z13, cor13 = None, None
    for m, words in colorings.items():
        assert set(words) == set(range(1, m))
        z = words_coloring(words)
        report, corners = analyze(range(m), z)
        rainbows = [(p[0], p[1], q[0] - p[0]) for p, q, r in corners if len({z[p], z[q], z[r]}) == 3]
        assert report["rainbow"] == {11: 3, 12: 6, 13: 14}[m]
        assert len(corners) == math.comb(m, 3)
        if m in expected_lists:
            assert sorted(rainbows) == expected_lists[m]
        report["rainbow_bases_v_u_step"] = sorted(rainbows)
        lines = defaultdict(list)
        for (v, u), color in z.items():
            lines["row", u].append(color)
            lines["column", v].append(color)
            lines["offset", v - u].append(color)
        scaled_D = sum(sum((3 * values.count(i) - len(values)) ** 2 for i in range(3))
                       for values in lines.values())
        assert scaled_D + 18 * report["rainbow"] == 9 * m * (m - 1)
        report["three_color_line_identity_checked"] = True
        report["line_variance_D_exact"] = str(Fraction(scaled_D, 9))
        results[str(m)] = report
        if m == 13:
            z13, cor13 = z, corners
    zero_records = {}
    for row in rows(t13[1][1]):
        vu = re.fullmatch(r"\$\((\d+),(\d+)\)\$", row[0].strip())
        assert vu, row
        v, u = map(int, vu.groups()); d = tex_int(row[1])
        colors = tuple(map(int, re.findall(r"\d", row[2])))
        cor = ((v, u), (v + d, u), (v + d, u + d))
        assert colors == tuple(z13[cell] for cell in cor)
        assert set(colors) == {0, 1, 2}
        zero_records[v, u, d] = colors
    assert set(zero_records) == set(results["13"]["rainbow_bases_v_u_step"])
    sum_table = tabulars(enclosing(source, "tab:t13sums"))[0][1]
    for row in rows(sum_table):
        d = tex_int(row[0]); printed_words = re.findall(r"\\texttt\{([012]+)\}", row[1])
        actual_words = ["".join(str((z13[v, u] + z13[v + d, u] + z13[v + d, u + d]) % 3)
                                for u in range(v)) for v in range(1, 13 - d)]
        assert printed_words == actual_words
        assert sum(word.count("0") for word in actual_words) == tex_int(row[2])
    results["13"]["all_286_printed_modular_sums_checked"] = True
    return results


def verify_seven(source):
    witness = enclosing(source, "eq:sevenmark-witness", "equation")
    differences = enclosing(source, "eq:sevenmark-differences", "equation")
    B = list(map(int, re.search(r"B=\\\{([\d,]+)\\\}", witness)[1].split(",")))
    listed = re.search(r"B=\\\{(.*?)\\\}", differences, re.S)
    assert listed, "Missing printed positive-difference list"
    printed = list(map(int, re.findall(r"\d+", listed[1])))
    actual = sorted(v - u for u, v in combinations(B, 2))
    assert len(B) == 7 and len(set(actual)) == 21 and actual == printed
    assert set(B) <= set(cube((1, 3, 9, 27)))
    sums = [u + v for u, v in combinations(B, 2)] + [2 * u for u in B]
    assert len(sums) == len(set(sums))
    return {"marks": B, "positive_differences": actual, "unique_sums_with_repetition": True}


def verify_structured(source, four_report, four_marks, four_z):
    assert "tab:structured-examples" in source
    reports = {"progression_product": four_report.copy(), "complete_direct_sum": four_report.copy()}
    D = {0, 1, 3, 4}
    assert set(four_marks) == {b + 9 * c for b in D for c in D}
    B = {d + 9 * p for d in D for p in (0, 1)}
    assert set(four_marks) == {b + 27 * p for b in B for p in (0, 1)}
    assert 27 > 2 * (max(B) - min(B)) and 9 > 2 * (max(D) - min(D))
    assert four_report["strict_corner_count_T"] <= 7 * four_report["M"] / 2
    z = {(1, 0): 0, (2, 0): 0, (2, 1): 1, (3, 0): 1, (3, 1): 0, (3, 2): 0}
    reports["translation_matching"], _ = analyze(range(4), z)
    for r in (4, 6, 8, 10):
        A = sorted(s * 5 ** i for i in range(r) for s in (-1, 1))
        z = {(v, u): int(v == -u) for u, v in combinations(A, 2)}
        report, _ = analyze(A, z)
        assert report["strict_corner_count_T"] == r * (r - 1)
        report["T_over_M_exact"] = f"{r - 1}/{2 * r - 1}"
        reports[f"two_distance_A_{r}"] = report
    # New two-subset family; direct enumeration checks stated instances, not all r.
    for r in (4, 6, 8, 10):
        labels = {5 ** i + 5 ** j: frozenset((i, j)) for i, j in combinations(range(r), 2)}
        A = sorted(labels)
        z = {(v, u): int(bool(labels[v] & labels[u])) for u, v in combinations(A, 2)}
        report, _ = analyze(A, z)
        assert report["n"] == math.comb(r, 2)
        assert report["strict_corner_count_T"] == 6 * math.comb(r, 4)
        assert report["strict_corner_count_T"] * (r + 1) == 2 * (r - 3) * report["M"]
        report["T_over_M_exact"] = f"{2 * (r - 3)}/{r + 1}"
        report["definition"] = "B_r={5^i+5^j:0<=i<j<r}; color is 1 iff index pairs intersect"
        reports[f"two_subset_B_{r}"] = report
    expected_rows = (four_report, four_report, reports["translation_matching"], reports["two_distance_A_4"])
    printed_rows = rows(tabulars(enclosing(source, "tab:structured-examples"))[0][1])
    assert len(printed_rows) == 4
    for row, actual in zip(printed_rows, expected_rows):
        assert [tex_int(cell) for cell in row[2:5]] == [actual["n"], actual["M"], actual["strict_corner_count_T"]]
        ratio = Fraction(row[5].strip().replace("$", ""))
        bound = Fraction(row[6].strip().replace("$", ""))
        assert ratio == Fraction(actual["strict_corner_count_T"], actual["M"])
        assert ratio <= bound
    reports["printed_four_example_rows_checked"] = 4
    reports["new_B_r_proposition_present_in_input_source"] = r"\label{prop:weight-two-family}" in source
    return reports


def verify_bound_arithmetic(source):
    results = {}
    for N, factor in ((361, 20), (379, 21)):
        marks = (N + 2) // 3
        lhs, rhs = math.comb(marks, 2), factor * (N - 1)
        assert lhs > rhs
        results[str(N)] = {"conditional_span_factor": factor, "diagonal_marks": marks,
                           "lhs_pairs": lhs, "rhs_span_budget": rhs, "strict_gap": lhs - rhs,
                           "is_conditional_only": True}
    assert "361" in enclosing(source, "cor:g9-three", "corollary")
    assert "379" in enclosing(source, "thm:s21three", "theorem")
    N, a, ell, t = 98777, 24695, 98776, 600
    statement = enclosing(source, "thm:s21four", "theorem")
    assert "98\\,777" in statement.replace(" ", "")
    assert (N + 3) // 4 == a
    assert 3 * 2035 * 2036 == 12429780
    profile = 126 * ell + 12429780 - 42 * (t + 1)
    assert profile == 24850314
    assert 2 * sum(t - h for h in range(1, t)) == t * (t - 1)
    assert 6 * sum(h * (t - h) for h in range(1, t)) == t * (t - 1) * (t + 1)
    lhs = 4070 * a * a * t
    rhs = (ell + t) * (4070 * a + (t - 1) * profile)
    gap = lhs - rhs
    assert gap == 3161813264 > 0
    gap_block = enclosing(source, "eq:four-color-gap", "equation")
    assert str(gap) in gap_block.replace(r"\,", "").replace(" ", "")
    results[str(N)] = {"conditional_on": "S21", "diagonal_marks": a,
                       "span_ell": ell, "shift_count_t": t,
                       "profile_constant": profile, "lhs_shift_mass": lhs,
                       "rhs_shift_budget": rhs, "strict_gap": gap,
                       "is_conditional_only": True}
    return results


def verify_crop(source):
    blocks = tabulars(enclosing(source, "tab:w1"))
    coloring = {}
    for row in rows(blocks[0][1]):
        x = tex_int(row[0])
        assert len(row) == 5
        for y, cell in enumerate(row[1:], 1):
            colors = re.findall("[RGB]", cell)
            assert len(colors) == 1, cell
            coloring[x, y] = colors[0]
    assert len(coloring) == 16
    corners = direct_corners(coloring)
    assert len(corners) == 14
    assert all(len({coloring[cell] for cell in cor}) > 1 for cor in corners)
    for row in rows(blocks[1][1]):
        d = tex_int(row[0])
        starts = list(map(int, re.findall(r"\d+", row[1])))
        assert [coloring[u + d, u] for u in starts] == row[2].strip().split(",")
        assert len(starts) == tex_int(row[3])
    # The new example distinguishes necessary local Golomb conditions from
    # one globally proper coloring; it is deliberately an incompatible choice.
    assert r"\label{fig:shared-completion}" in source
    marks = [0, 1, 2, 3]
    domain = {(v, u): None for u, v in combinations(marks, 2)}
    all_corners = direct_corners(domain)
    q = (3, 0)
    completed = [cor for cor in all_corners if cor[1] == q]
    assert completed == [((1, 0), q, (3, 2)), ((2, 0), q, (3, 1))]
    fixed = {(1, 0): 0, (2, 1): 1, (3, 2): 0,
             (2, 0): 1, (3, 1): 1}
    monochromatic_counts = []
    for q_color in (0, 1):
        trial = {**fixed, q: q_color}
        for offset in (1, 2, 3):
            for color in (0, 1):
                starts = sorted(u for (v, u), c in trial.items()
                                if v-u == offset and c == color)
                differences = [b-a for a, b in combinations(starts, 2)]
                assert len(differences) == len(set(differences))
        mono = [cor for cor in all_corners if len({trial[c] for c in cor}) == 1]
        assert len(mono) == 1 and mono[0][1] == q
        monochromatic_counts.append(len(mono))
    return {"cells": 16, "directed_corners": 14, "monochromatic": 0,
            "printed_fiber_lists_checked": 3,
            "shared_completion_example": {
                "marks": marks, "cells": len(domain), "corners": len(all_corners),
                "completion": list(q), "corners_at_completion": len(completed),
                "local_Golomb_conditions_for_both_choices": True,
                "monochromatic_counts_for_q_colors_0_and_1": monochromatic_counts}}


def verify_six_point(source):
    statement = enclosing(source, "prop:six-point-extremal", "corollary")
    marks_match = re.search(r"\\\{([\d,\s]+)\\\}", statement)
    assert marks_match, "Missing six-point witness set"
    A = list(map(int, re.findall(r"\d+", marks_match[1])))
    assert A == [0, 1, 2, 3, 4, 6]
    blocks = tabulars(enclosing(source, "tab:six-point-witness"))
    assert len(blocks) == 2
    coloring = {}
    covered_upper_marks = set()
    for row in rows(blocks[0][1]):
        upper = tex_int(row[0])
        match = re.fullmatch(r"\\texttt\{([01]+)\}", row[1].strip())
        assert match
        lower_marks = [a for a in A if a < upper]
        assert len(match[1]) == len(lower_marks)
        for lower, color in zip(lower_marks, match[1]):
            coloring[upper, lower] = int(color)
        covered_upper_marks.add(upper)
    assert covered_upper_marks == set(A[1:])
    report, corners = analyze(A, coloring)
    assert (report["n"], report["M"], report["strict_corner_count_T"],
            report["additive_energy_E"]) == (6, 15, 16, 130)
    differences = Counter(b - a for a, b in combinations(A, 2))
    assert [differences[d] for d in range(1, 7)] == [4, 4, 3, 2, 1, 1]
    actual_by_step = defaultdict(list)
    for cor in corners:
        p, q, r = cor
        actual_by_step[q[0] - p[0]].append((p, "".join(str(coloring[cell]) for cell in cor)))
    covered_steps = set()
    for row in rows(blocks[1][1]):
        steps = list(map(int, re.findall(r"\d+", row[0])))
        count = tex_int(row[1])
        printed_words = re.findall(r"\\texttt\{([01]{3})\}", row[2])
        for step in steps:
            actual_words = [word for base, word in sorted(actual_by_step[step])]
            assert len(actual_words) == count
            assert actual_words == printed_words, (step, actual_words, printed_words)
            covered_steps.add(step)
    assert covered_steps == set(range(1, 7))
    report["all_printed_step_color_words_checked"] = True
    classification = re.sub(r"\s+", "", enclosing(source, "eq:six-point-equality-classification", "equation"))
    assert r"A=a+dA_*" in classification and r"A=a+d(6-A_*)" in classification
    assert r"\label{eq:endpoint-equality-loss}" in source
    assert r"\label{eq:repeated-difference-extension}" in source
    def corner_count(S):
        rs = Counter(v - u for u, v in combinations(S, 2))
        return sum(math.comb(k, 2) for k in rs.values())
    def normalized_reflection_type(S):
        S = sorted(S)
        shifted = [x - S[0] for x in S]
        scale = math.gcd(*shifted)
        reduced = tuple(x // scale for x in shifted)
        reflected = tuple(sorted(reduced[-1] - x for x in reduced))
        return min(reduced, reflected)
    finite = {}
    for n in (4, 5, 6):
        checked = equality_count = 0
        target = math.comb(n, 3) - (n - 2)
        for rest in combinations(range(1, 21), n - 1):
            S = (0,) + rest
            B, L = S[:-1], S[-1]
            actual_T, base_T = corner_count(S), corner_count(B)
            rs = Counter(v - u for u, v in combinations(B, 2))
            loss = sum(k for h, k in rs.items() if L - h in B)
            assert actual_T - base_T == loss
            is_ap = len({S[i + 1] - S[i] for i in range(n - 1)}) == 1
            if not is_ap:
                assert actual_T <= target and loss <= math.comb(n - 1, 2) - 1
            if n == 4:
                p, q, s = (S[i + 1] - S[i] for i in range(3))
                predicted = ((p == s and q != p) or (p == q and s == 2 * p) or (q == s and p == 2 * q))
            else:
                template = (0, 1, 2, 3, 5) if n == 5 else (0, 1, 2, 3, 4, 6)
                predicted = normalized_reflection_type(S) == template
            assert (actual_T == target) == predicted, ("bounded equality case", S, actual_T)
            equality_count += actual_T == target
            checked += 1
        finite[str(n)] = {"sets_checked": checked, "equality_sets": equality_count,
                          "minimum": 0, "maximum_span": 20,
                          "endpoint_loss_identity_checked": True,
                          "classification_checked_only_on_this_finite_domain": True}
    transformed_count = 0
    for shift, scale, sign in product((-7, 0, 11), (1, 2, 5), (-1, 1)):
        f = lambda t: shift + sign * scale * t
        transformed = {(max(f(v), f(u)), min(f(v), f(u))): color
                       for (v, u), color in coloring.items()}
        actual, _ = analyze([f(a) for a in A], transformed)
        assert (actual["strict_corner_count_T"], actual["additive_energy_E"]) == (16, 130)
        transformed_count += 1
    report["equality_classification_support"] = {
        "printed_equality_forms_checked": True, "finite_enumeration": finite,
        "affine_and_reflected_colorings_checked": transformed_count,
        "scope": "Bounded checks and transported witnesses; the complete classification relies on the printed endpoint proof, not this enumeration."}
    report["interpretation"] = "Attainment and bounded classification checks; the universal maximum and complete equality classification use their proofs."
    return report


def verify_source_references(source, bib_text=None):
    """Check key integrity, not the truth or priority of cited literature."""
    uncommented = re.sub(r"(?<!\\)%[^\n]*", "", source)
    labels = re.findall(r"\\label\{([^}]+)\}", uncommented)
    duplicate_labels = sorted(key for key, count in Counter(labels).items() if count > 1)
    refs = []
    for match in re.finditer(r"\\(?:ref|eqref|pageref|autoref|cref|Cref)\*?\{([^}]+)\}", uncommented):
        refs.extend(key.strip() for key in match[1].split(","))
    refs.extend(re.findall(r"\\hyperref\[([^\]]+)\]", uncommented))
    missing_refs = sorted(set(refs) - set(labels))
    assert not duplicate_labels, ("Duplicate labels", duplicate_labels)
    assert not missing_refs, ("Undefined labels", missing_refs)
    cites = []
    for match in re.finditer(r"\\(?:cite|citep|citet)(?:\[[^\]]*\])*\{([^}]+)\}", uncommented):
        cites.extend(key.strip() for key in match[1].split(","))
    if bib_text is not None:
        entries = [(kind.lower(), key.strip()) for kind, key in
                   re.findall(r"(?m)^\s*@(\w+)\s*\{\s*([^,]+),", bib_text)]
        bib_keys = [key for kind, key in entries if kind not in ("comment", "preamble", "string")]
        assert len(bib_keys) == len(set(bib_keys)), "Duplicate bibliography keys"
        bibliography_kind = "external BibTeX file"
    else:
        bib_keys = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", uncommented)
        bibliography_kind = "inline bibliography" if bib_keys else "not checked; no --bib supplied"
    assert len(bib_keys) == len(set(bib_keys)), "Duplicate bibliography keys"
    bibliography_checked = bib_text is not None or bool(bib_keys)
    missing_cites = sorted(set(cites) - set(bib_keys)) if bibliography_checked else None
    if missing_cites is not None:
        assert not missing_cites, ("Undefined citation keys", missing_cites)
    return {"labels_checked": len(labels), "references_checked": len(refs),
            "duplicate_labels": duplicate_labels, "undefined_references": missing_refs,
            "citation_keys_used": len(set(cites)), "bibliography_kind": bibliography_kind,
            "bibliography_keys": len(bib_keys) if bib_keys else None,
            "undefined_citation_keys": missing_cites,
            "scope": "Key integrity only; no external literature-content or priority audit."}


def verify_printed_k4(source):
    """Bind the added explanation to the K4 case already tested exhaustively."""
    set_equation = enclosing(source, "eq:k4-worked-set", "equation")
    set_match = re.search(r"\\\{([\d,\s]+)\\\}", set_equation)
    assert set_match
    marks = list(map(int, re.findall(r"\d+", set_match[1])))
    edges = list(combinations(range(4), 2))
    expected_marks = sorted(5 ** i + 5 ** j for i, j in edges)
    assert marks == expected_marks == [6, 26, 30, 126, 130, 150]
    actual = _verify_graph_instance(4, edges)
    table = tabulars(enclosing(source, "tab:k4-worked"))
    assert len(table) == 1
    source_matchings = []
    source_pairs = []
    for row in rows(table[0][1]):
        number = tex_int(row[0])
        matching = [tuple(map(int, pair)) for pair in re.findall(r"\\\{(\d+),(\d+)\\\}", row[1])]
        assert len(matching) == 2
        assert set(matching[0]) | set(matching[1]) == set(range(4))
        assert not set(matching[0]) & set(matching[1])
        encoded = re.fullmatch(r"\$?(\d+)\+(\d+)\$?", row[2].strip().replace(" ", ""))
        assert encoded
        a, b = map(int, encoded.groups())
        assert sorted((a, b)) == sorted(5 ** i + 5 ** j for i, j in matching)
        total = tex_int(row[3])
        assert a + b == total == 156
        source_matchings.append((number, tuple(sorted(matching))))
        source_pairs.append(tuple(sorted((a, b))))
    assert [number for number, matching in source_matchings] == [1, 2, 3]
    assert len({matching for number, matching in source_matchings}) == 3
    all_sum_pairs = sorted((a, b) for a, b in combinations(marks, 2) if a + b == 156)
    assert sorted(source_pairs) == all_sum_pairs == [(6, 150), (26, 130), (30, 126)]
    counts = re.sub(r"\s+", "", enclosing(source, "eq:k4-worked-counts", "equation"))
    expected_counts = [("|A_{K_4}|", 6), ("M(A_{K_4})", 15), ("C_4(K_4)", 3),
                       ("T(A_{K_4})", 6), ("E(A_{K_4})", 90)]
    for name, value in expected_counts:
        match = re.search(re.escape(name) + r"=(\d+)", counts)
        assert match and int(match[1]) == value, (name, value)
    assert (actual["n"], actual["M"], actual["C4_unoriented_not_necessarily_induced"],
            actual["T"], actual["additive_energy_E"]) == (6, 15, 3, 6, 90)
    labels = {5 ** i + 5 ** j: frozenset((i, j)) for i, j in edges}
    coloring = {(v, u): int(not (labels[v] & labels[u])) for u, v in combinations(marks, 2)}
    moment, _ = analyze(marks, coloring)
    assert (moment["K3_by_fiber_corner_count"], moment["D_z"], moment["R_z"], moment["P_z"]) == (0, 12, 0, 6)
    assert (moment["cube_moment_first_bound"], moment["cube_moment_second_bound"]) == (0, 0)
    moment_claim = re.sub(r"\s+", "", enclosing(source, "eq:k4-moment-sharpness", "equation"))
    for name, value in [("K_3(A_{K_4})", 0), ("D_z(A_{K_4})", 12), ("R_z(A_{K_4})", 0), ("P_z(A_{K_4})", 6)]:
        match = re.search(re.escape(name) + r"=(\d+)", moment_claim)
        assert match and int(match[1]) == value, ("K4 printed moment value", name, value)
    assert r"\min\{2T-D_z/2,\T+5R_z\}=6" in moment_claim
    assert r"\min\{2T-D_z/2,\T+5R_z\}-P_z=0" in moment_claim
    return {"marks_read_from_source": marks, "source_matchings_checked": 3,
            "all_unordered_pairs_summing_to_156": [list(pair) for pair in all_sum_pairs],
            "C4": 3, "M": 15, "T": 6, "E": 90, "proper_coloring": True,
            "T_over_M_exact": "2/5",
            "moment_bound_attainment": {"K3": 0, "D_z": 12, "R_z": 0, "P_z": 6,
                                        "old_first": 6, "old_second": 6, "old_combined": 6,
                                        "new_first": 0, "new_second": 0, "new_combined": 0,
                                        "printed_source_values_checked": True,
                                        "strict_D_branch_switch": False},
            "scope": "Worked counting example already covered by exhaustive graph enumeration; sharpness uses the infinite family."}


def verify(source, bib_text=None):
    results = {}
    results["seven_mark_witness"] = verify_seven(source)
    four_report, four_marks, four_z = verify_fourcube(source)
    results["four_cube"] = four_report
    assert (four_report["P_z"], four_report["K3_by_fiber_corner_count"],
            four_report["cube_moment_first_bound"], four_report["cube_moment_second_bound"]) == (8, 120, 379, 317)
    claim = re.sub(r"\s+", "", enclosing(source, "eq:fourcube-moment-comparison", "equation"))
    for name, value in [("T", 200), ("K_3", 120), ("D_z", 26), ("R_z", 25), ("P_z", 8)]:
        match = re.search(re.escape(name) + r"=(\d+)", claim)
        assert match and int(match[1]) == value, ("Four-cube printed value", name, value)
    comparison = enclosing(source, "eq:fourcube-moment-comparison", "revision")
    comparison_rows = rows(tabulars(comparison)[0][1])
    actual_pairs = [(four_report["cube_moment_first_bound"] + four_report["P_z"], four_report["cube_moment_first_bound"]),
                    (four_report["cube_moment_second_bound"] + four_report["P_z"], four_report["cube_moment_second_bound"]),
                    (four_report["cube_moment_combined_bound"] + four_report["P_z"], four_report["cube_moment_combined_bound"])]
    assert [tuple(map(tex_int, row[1:])) for row in comparison_rows] == actual_pairs
    four_report["printed_actual_K3_and_old_new_bounds_checked"] = True
    results["four_by_four_crop"] = verify_crop(source)
    results["six_point_attainment_witness"] = verify_six_point(source)
    results["three_cube"] = verify_threecube(source)
    results["weak_twelve_mark_coloring"] = verify_weak(source)
    results["concentrated_deficit"] = verify_deficit(source)
    results["rainbow_counterexamples"] = verify_rainbows(source)
    results["structured_examples"] = verify_structured(source, four_report, four_marks, four_z)
    results["divisor_weights"] = verify_weights(source)
    results["conditional_bound_arithmetic"] = verify_bound_arithmetic(source)
    results["graph_encoded_sources"] = verify_graph_families()
    results["graph_encoded_sources"]["printed_K4_worked_example"] = verify_printed_k4(source)
    results["graph_encoded_sources"]["graph_theorem_present_in_input_source"] = r"\label{thm:graph-source}" in source
    results["graph_encoded_sources"]["midpoint_theorem_present_in_input_source"] = r"\label{thm:midpoint-three}" in source
    assert results["graph_encoded_sources"]["graph_theorem_present_in_input_source"]
    assert results["graph_encoded_sources"]["midpoint_theorem_present_in_input_source"]
    results["source_reference_keys"] = verify_source_references(source, bib_text)
    return results


def main():
    if not __debug__:
        raise RuntimeError("Run without -O; this verifier requires assertion checks to be enabled.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_positional", nargs="?", type=Path)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--bib", type=Path, help="Optional external BibTeX file for key checks and a separate SHA-256")
    parser.add_argument("--output", type=Path, default=Path("verification_results.json"))
    args = parser.parse_args()
    source_path = args.source or args.source_positional
    if source_path is None:
        parser.error("provide a source path positionally or using --source")
    raw = source_path.read_bytes()
    bib_raw = args.bib.read_bytes() if args.bib else None
    record = {"verifier_description": "New independent finite-certificate validator",
              "source_file": source_path.name, "source_sha256": hashlib.sha256(raw).hexdigest(),
              "bibliography_file": args.bib.name if args.bib else None,
              "bibliography_sha256": hashlib.sha256(bib_raw).hexdigest() if bib_raw is not None else None,
              "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "timestamp_utc": datetime.now(timezone.utc).isoformat(),
              "environment": {"python": sys.version, "platform": platform.platform(),
                              "dependencies": "Python standard library only"},
              "limitations": ["Finite enumerations do not certify proofs for arbitrary sets or generators.",
                              "This newly written verifier is not an unavailable original SAT pipeline.",
                              "No open assertion is proved and no unconditional Ramsey bound is claimed.",
                              "New B_r examples are tested at r=4,6,8,10; the all-r statement uses its proof.",
                              "No literature priority or external citation audit is performed.",
                              "Graph enumeration covers all labeled graphs through five vertices and seven six-vertex examples; arbitrary graphs use their proof.",
                              "The six-point certificate verifies attainment and bounded equality cases, not the universal maximum or full equality classification.",
                              "Bibliography checks concern key integrity, not literature accuracy or priority."]}
    try:
        record["results"] = verify(raw.decode("utf-8"), bib_raw.decode("utf-8") if bib_raw is not None else None)
        record["status"] = "passed"
        record["checklist"] = [{"check": name, "status": "passed"} for name in record["results"]]
    except Exception as exc:
        record["status"] = "failed"
        record["error"] = f"{type(exc).__name__}: {exc}"
        record["traceback"] = traceback.format_exc()
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        raise
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": record["status"], "source_sha256": record["source_sha256"],
                      "checks": len(record["checklist"]), "output": str(args.output)}, indent=2))


# The independent exact weight checker is embedded below for a single-file release.

"""Exact verification of the two printed divisor weight certificates.

This is a newly written independent verifier, not an original companion program.
Only Python's standard library is used.
"""

import json
import math
import re
from pathlib import Path


def _weight_table(source, label):
    marker = r"\label{" + label + "}"
    pos = source.index(marker)
    start = source.rfind(r"\begin{table}", 0, pos)
    end = source.index(r"\end{table}", pos) + len(r"\end{table}")
    assert start >= 0, "Missing table around " + label
    return source[start:end]


def _weight_rows(block):
    body = block.split(r"\midrule", 1)[1].split(r"\bottomrule", 1)[0]
    return [row.strip().split("&") for row in body.split(r"\\") if row.strip()]


def _weight_int(cell):
    text = cell.strip().replace("$", "").replace(r"\,", "").replace(" ", "")
    return int(text) if re.fullmatch(r"\d+", text) else None


def _is_smooth(n):
    for p in (2, 3, 5, 7):
        while n % p == 0:
            n //= p
    return n == 1


def verify_weights(source):
    """Read source tables; raise AssertionError on any numerical mismatch."""
    rows = _weight_rows(_weight_table(source, "tab:weights"))
    printed = {}
    printed_sums = None
    compact = len(rows[0]) == 9
    for row in rows:
        if compact:
            assert len(row) == 9, row
            for start in (0, 3, 6):
                d, a11, a12 = (tex_int(cell) for cell in row[start:start + 3])
                assert d not in printed, "Duplicate dilation weight"
                printed[d] = (d, a11, a12)
            continue
        if _weight_int(row[0]) is None:
            assert r"\sum" in row[0], "Unrecognized weight-table row"
            printed_sums = (_weight_int(row[3]), _weight_int(row[6]))
            continue
        values = tuple(_weight_int(cell) for cell in row)
        assert len(values) == 7 and all(v is not None for v in values), row
        d = values[0]
        assert d not in printed, "Duplicate dilation weight"
        printed[d] = values
    assert set(printed) == set(range(1, 43)), "Weights must cover dilations 1..42"
    assert compact or printed_sums is not None, "Missing printed copy totals"

    smooth_rows = _weight_rows(_weight_table(source, "tab:smooth"))
    smooth_printed = {11: {}, 12: {}}
    for row in smooth_rows:
        assert len(row) == 9, row
        for i in (0, 3, 6):
            h = _weight_int(row[i])
            if h is None:
                assert all(not c.strip() for c in row[i:i + 3]), row
                continue
            for m, k in ((11, i + 1), (12, i + 2)):
                value = _weight_int(row[k])
                if value is None:
                    assert row[k].strip() == "--", row
                    assert m == 11 and h > 168, "Unexpected absent smooth-step load"
                else:
                    assert h not in smooth_printed[m], "Duplicate smooth-step entry"
                    smooth_printed[m][h] = value

    reports = {}
    configs = ((11, 459, 5, 168, 944436978, 5959890),
               (12, 455, 7, 210, 809226900, 578300))
    for m, host, rho, smooth_end, expected_J, expected_gap in configs:
        coeff = {j: math.comb(m - j, 2) for j in range(1, m - 1)}
        budget = 1000 * coeff[1]
        weights = {}
        for n in range(1, 43):
            numerator = budget - sum(coeff[j] * weights[n // j]
                                     for j in range(2, m - 1) if n % j == 0)
            weights[n] = numerator // coeff[1]
            assert 0 <= weights[n] <= 1000, (m, n, weights[n])

        column = 1 if m == 11 else 4
        J = 0
        for d in range(1, 43):
            copies = math.comb(host - d * (m - 2), 2)
            actual = (weights[d], copies, weights[d] * copies)
            if compact:
                assert printed[d][1 if m == 11 else 2] == weights[d], (m, d)
            else:
                assert printed[d][column:column + 3] == actual, (m, d, actual, printed[d])
            J += actual[2]
        assert J == expected_J, (m, J)
        if not compact:
            assert J == printed_sums[0 if m == 11 else 1]
        totals_block = enclosing(source, "prop:weights", "proposition")
        totals_integers = {int(token.replace(r"\,", ""))
                           for token in re.findall(r"\d+(?:\\,\d+)*", totals_block)}
        assert J in totals_integers, ("Computed J not found in source proposition", m, J)

        # Because a_d=0 for d>42 and j<=m-2, all loads above this limit vanish.
        limit = 42 * (m - 2)
        loads = {h: sum(coeff[j] * weights.get(h // j, 0)
                        for j in range(1, m - 1) if h % j == 0)
                 for h in range(1, limit + 1)}
        assert all(0 <= v <= budget for v in loads.values()), (m, max(loads.values()))
        assert all(0 <= budget - loads[h] < coeff[1] for h in range(1, 43))
        expected_smooth = {h for h in range(43, smooth_end + 1) if _is_smooth(h)}
        assert set(smooth_printed[m]) == expected_smooth, (m, "smooth-step coverage")
        for h, value in smooth_printed[m].items():
            assert loads[h] == value, (m, h, loads[h], value)

        # Lemma 'Three-color line identity': U_N = binom(N,2)-(N-1)+floor((N-1)/3).
        U = math.comb(host, 2) - (host - 1) + (host - 1) // 3
        gap = rho * J - budget * U
        assert gap == expected_gap and gap > 0, (m, gap)
        assert 42 * (m - 2) <= host - 2, "Dilation support exceeds host"
        coarse_host = 460 if m == 11 else 457
        coarse_J = sum(weights[d] * math.comb(coarse_host - d * (m - 2), 2)
                       for d in weights)
        coarse_gap = rho * coarse_J - budget * math.comb(coarse_host, 2)
        expected_coarse_gap = 1575945 if m == 11 else 8045239
        assert coarse_gap == expected_coarse_gap > 0
        reports[str(m)] = {
            "status": "passed",
            "host_N": host,
            "local_rainbow_premise": rho,
            "local_premise_is_refuted_elsewhere": True,
            "weights_read_and_recomputed": len(weights),
            "source_table_format": "compact weights only" if compact else "weights, copy factors and summands",
            "copy_factors_and_summands_recomputed": True,
            "individual_copy_factors_and_summands_printed_and_compared": not compact,
            "weights": [weights[d] for d in range(1, 43)],
            "budget_K": budget,
            "weighted_copy_total_J": J,
            "load_limit": limit,
            "all_loads_through_limit_checked": True,
            "loads_above_limit_are_zero_by_finite_support": True,
            "maximum_load": max(loads.values()),
            "maximum_load_steps": [h for h, v in loads.items() if v == max(loads.values())],
            "printed_smooth_loads_checked": len(expected_smooth),
            "rainbow_cap_U": U,
            "conditional_gap": gap,
            "coarser_host_N": coarse_host,
            "coarser_gap": coarse_gap,
        }
    return reports




"""Independent finite verification of the graph-edge integer construction.

Only Python's standard library is used. These checks cover the explicitly
enumerated finite graphs and do not replace the proof for arbitrary graphs.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, combinations_with_replacement
import json
from math import comb


def _verify_graph_instance(vertex_count, edges):
    edges = sorted(tuple(sorted(edge)) for edge in edges)
    assert len(edges) == len(set(edges))
    assert all(0 <= i < j < vertex_count for i, j in edges)
    neighbors = [set() for _ in range(vertex_count)]
    for i, j in edges:
        neighbors[i].add(j)
        neighbors[j].add(i)

    # A simple unoriented 4-cycle is counted at its two opposite vertex pairs.
    twice_C4 = sum(comb(len(neighbors[i] & neighbors[j]), 2)
                   for i, j in combinations(range(vertex_count), 2))
    assert twice_C4 % 2 == 0
    C4 = twice_C4 // 2

    labels = {5 ** i + 5 ** j: frozenset((i, j)) for i, j in edges}
    assert len(labels) == len(edges), "The graph-edge integer map must be injective"
    marks = sorted(labels)
    n = len(marks)
    M = comb(n, 2)
    positive_differences = Counter(v - u for u, v in combinations(marks, 2))
    T = sum(comb(value, 2) for value in positive_differences.values())
    assert T == 2 * C4
    assert T <= 2 * M
    span = marks[-1] - marks[0] if marks else 0
    assert M <= 5 * span

    # Enumerate geometrically by horizontal source-cell pairs, independently
    # of the positive-difference multiplicity count above.
    colors = {(v, u): int(len(labels[v] & labels[u]) == 1)
              for u, v in combinations(marks, 2)}
    corners = []
    color_words = Counter()
    for row_index, u in enumerate(marks):
        for x, v in combinations(marks[row_index + 1:], 2):
            p, q, r = (x, u), (v, u), (v, u + v - x)
            if r not in colors:
                continue
            word = (colors[p], colors[q], colors[r])
            assert len(set(word)) == 2, ("Monochromatic corner", edges, p, q, r)
            # Every actual corner has two intersecting-edge inputs and a
            # disjoint-edge completion under this construction.
            assert word == (1, 0, 1)
            color_words["".join(map(str, word))] += 1
            corners.append((p, q, r))
    assert len(corners) == len(set(corners)) == T

    # The long pairs are pairs of graph edges with four distinct endpoints.
    # A midpoint sum with four 1-digits can have at most the three perfect
    # matchings on those four vertices. Repeated-mark pair sums are also
    # checked, but they are not counted as long pairs.
    all_pair_sums = defaultdict(list)
    scalar_to_vector, vector_to_scalar = {}, {}
    long_pair_sums = defaultdict(list)
    for a, b in combinations_with_replacement(marks, 2):
        all_pair_sums[a + b].append((a, b))
        vector_sum = tuple(int(i in labels[a]) + int(i in labels[b]) for i in range(vertex_count))
        assert scalar_to_vector.setdefault(a + b, vector_sum) == vector_sum
        assert vector_to_scalar.setdefault(vector_sum, a + b) == a + b
        if not labels[a] & labels[b]:
            long_pair_sums[a + b].append((a, b))
    maximum_all_multiplicity = max(map(len, all_pair_sums.values()), default=0)
    maximum_long_multiplicity = max(map(len, long_pair_sums.values()), default=0)
    assert maximum_all_multiplicity <= 3
    assert maximum_long_multiplicity <= 3
    for pairs in all_pair_sums.values():
        if len(pairs) > 1:
            assert all(not labels[a] & labels[b] for a, b in pairs)
            supports = {labels[a] | labels[b] for a, b in pairs}
            assert len(supports) == 1 and len(next(iter(supports))) == 4
    assert sum(comb(len(pairs), 2) for pairs in long_pair_sums.values()) == C4

    signed_differences = Counter(v - u for u in marks for v in marks)
    energy = sum(value * value for value in signed_differences.values())
    assert energy == 2 * n * n - n + 4 * T
    assert energy == 2 * n * n - n + 8 * C4
    return {
        "graph_vertices": vertex_count,
        "graph_edges": [list(edge) for edge in edges],
        "n": n,
        "span": span,
        "M": M,
        "T": T,
        "C4_unoriented_not_necessarily_induced": C4,
        "T_over_M_exact": str(Fraction(T, M)) if M else None,
        "additive_energy_E": energy,
        "proper_coloring": True,
        "enumerated_geometric_corners": len(corners),
        "corner_color_words": dict(color_words),
        "long_pair_midpoint_groups": len(long_pair_sums),
        "maximum_long_pair_midpoint_multiplicity": maximum_long_multiplicity,
        "maximum_pair_sum_multiplicity_including_repetitions": maximum_all_multiplicity,
    }


def verify_graph_families():
    """Check every labeled graph on up to five vertices and selected six-graphs."""
    summaries = {}
    all_records_digest = sha256()
    total = 0
    for vertex_count in range(6):
        candidate_edges = list(combinations(range(vertex_count), 2))
        graph_count = 1 << len(candidate_edges)
        largest_ratio = Fraction(0, 1)
        largest_ratio_mask = 0
        maximum_T = 0
        maximum_midpoint = 0
        for mask in range(graph_count):
            edges = [edge for j, edge in enumerate(candidate_edges) if mask >> j & 1]
            actual = _verify_graph_instance(vertex_count, edges)
            ratio = Fraction(actual["T"], actual["M"]) if actual["M"] else Fraction(0, 1)
            if ratio > largest_ratio:
                largest_ratio, largest_ratio_mask = ratio, mask
            maximum_T = max(maximum_T, actual["T"])
            maximum_midpoint = max(maximum_midpoint, actual["maximum_long_pair_midpoint_multiplicity"])
            record = {"r": vertex_count, "edge_mask": mask,
                      "n": actual["n"], "M": actual["M"], "T": actual["T"],
                      "C4": actual["C4_unoriented_not_necessarily_induced"],
                      "max_long_k": actual["maximum_long_pair_midpoint_multiplicity"]}
            all_records_digest.update((json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode())
        summaries[str(vertex_count)] = {
            "graphs_checked": graph_count,
            "all_labeled_simple_graphs_checked": True,
            "maximum_T": maximum_T,
            "maximum_T_over_M_exact": str(largest_ratio),
            "maximum_ratio_witness_edge_mask": largest_ratio_mask,
            "maximum_long_midpoint_multiplicity": maximum_midpoint,
        }
        total += graph_count
    assert total == 1100

    six_graphs = {
        "complete_K6": list(combinations(range(6), 2)),
        "cycle_C6": [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5)],
        "complete_bipartite_K3_3": [(i, j) for i in range(3) for j in range(3, 6)],
        "path_P6": [(i, i + 1) for i in range(5)],
        "star_K1_5": [(0, i) for i in range(1, 6)],
        "empty": [],
        "perfect_matching_3K2": [(0, 1), (2, 3), (4, 5)],
    }
    representatives = {name: _verify_graph_instance(6, edges)
                       for name, edges in six_graphs.items()}
    return {
        "status": "passed",
        "construction": "A_G={5^i+5^j:{i,j} in E(G)}",
        "color_rule": "1 for index-edge intersection size 1; 0 for disjoint index edges",
        "cycle_convention": "simple unoriented 4-cycles, not required to be induced; K4 contains 3",
        "independent_cycle_formula": "C4=(1/2)*sum_{i<j} binom(|N(i) intersect N(j)|,2)",
        "midpoint_convention": "k counts long unordered pairs, whose two index edges are disjoint",
        "all_graphs_up_to_five_vertices": summaries,
        "total_exhaustive_graphs_checked": total,
        "deterministic_exhaustive_record_sha256": all_records_digest.hexdigest(),
        "six_vertex_representatives": representatives,
        "identities_checked": ["T=2*C4", "direct corner enumeration equals difference count",
                               "no monochromatic corner", "long midpoint k<=3", "T<=2M",
                               "C4=sum_midpoints binom(k,2)", "E=2*n^2-n+8*C4",
                               "M<=5L", "pair sums preserved in both directions including repetitions"],
        "limitation": "Finite coverage only; the theorem for arbitrary simple graphs uses its proof.",
    }




if __name__ == "__main__":
    main()
