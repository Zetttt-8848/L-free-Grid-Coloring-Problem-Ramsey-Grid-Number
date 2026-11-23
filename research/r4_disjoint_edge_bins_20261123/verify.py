"""Recompute the strengthened discrepancy, binary intervals, and outer margin."""

import argparse
import hashlib
import json
import sys
from bisect import bisect_right
from fractions import Fraction as F
from pathlib import Path


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--round3", type=Path, required=True, help="checkout containing the archived round-3 files")
parser.add_argument("--window", type=Path, required=True, help="the pinned upstream asymptotic directory")
args = parser.parse_args()
r4 = args.round3.resolve() / "research/r4_local_capacity_round3_20261114"
old = r4.parent / "boundary_certificates_20261115"
sys.path[:0] = [str(r4), str(old)]
import verify_numeric as audit
from verify_four_window import load_window

data = json.loads(Path(__file__).with_name("certificate.json").read_bytes())
tables = args.window.resolve()
den, r, alpha = load_window(tables)
assert data["width"] == audit.T


def matrix(name):
    path = tables / f"{name}.txt"
    assert hashlib.sha256(path.read_bytes()).hexdigest() == data["rational_window_inputs"][path.name]
    return [[F(value) for value in line.split(",")] for line in path.read_text().splitlines()]


spans = data["binary_spans"]
seeds = {int(k): v for k, v in data["seeds"].items()}
audit.audit_spans(spans, audit.golomb_bounds(), seeds, False)


def cap(positions):
    return min(audit.old_cap(positions, True), bisect_right(spans, positions - 1) - 1)


g, h, (pi,) = matrix("G"), matrix("H"), matrix("p")
global_local_cap = cap(1820)
lambda_den_over_width = (21_975_000 + 1820 * alpha) / (455_000 * 1720)
small_caps = [cap(k) for k in range(1, 1721)]
total_scaled = 0
for index in range(6):
    mass = sum(g[index])
    for side in (0, 1):
        score = 0
        for bin_no in range(150):
            if side:
                normalized_bin = g[index][-1 - bin_no] / mass
                preceding = sum(g[index][len(g[index]) - bin_no:]) / mass
                target = h[index][-1 - bin_no]
            else:
                normalized_bin = g[index][bin_no] / mass
                preceding = sum(g[index][:bin_no]) / mass
                target = h[index][bin_no]
            first = target - lambda_den_over_width * (preceding * global_local_cap + normalized_bin * small_caps[0])
            if first <= 0:
                continue
            slope = lambda_den_over_width * normalized_bin
            constant = target - lambda_den_over_width * preceding * global_local_cap
            variance = sum(max(F(0), constant - slope * q) ** 2 for q in small_caps)
            score += (variance * pi[index] * 10**9).__floor__()
        expected = next(row for row in data["samples"] if row["row"] == index and row["reverse"] == bool(side))
        assert score == expected["variance_floor_nanos"]
        total_scaled += score

discrepancy = F(total_scaled, 10**9)
assert discrepancy == F(data["discrepancy_lower_bound"])
thresholds = audit.inner_thresholds(den, r, alpha)
audit.audit_rows(data["rows"], discrepancy, thresholds, den, r, alpha)
weights = audit.correlations()
loss = audit.twenty_loss()
for side, key in ((data["side"], "result"), (data["side"] - 1, "preceding_side_result")):
    blocks, raw, bonus, loss_check = audit.outer(data["rows"], side, weights, loss)
    assert {"blocks": blocks, "raw": raw, "bonus": bonus, "loss": loss_check, "margin": raw + bonus} == data[key]
    print(f"Independent R4 check, side {side}: exact margin {raw + bonus}.")
assert data["result"]["margin"] > 0
