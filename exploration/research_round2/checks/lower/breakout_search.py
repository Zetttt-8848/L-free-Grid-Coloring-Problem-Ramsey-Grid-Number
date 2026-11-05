#!/usr/bin/env python3
"""Bounded dynamic-weight local search for directed equal-arm L colorings."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np


def triples(n: int) -> np.ndarray:
    data = [
        (x * n + y, (x + d) * n + y, (x + d) * n + y + d)
        for d in range(1, n)
        for x in range(n - d)
        for y in range(n - d)
    ]
    out = np.asarray(data, dtype=np.int32)
    exact = (n - 1) * n * (2 * n - 1) // 6
    if len(out) != exact:
        raise AssertionError((len(out), exact))
    return out


def incidence(n: int, ts: np.ndarray) -> tuple[list[np.ndarray], list[tuple[np.ndarray, np.ndarray]]]:
    ids: list[list[int]] = [[] for _ in range(n * n)]
    pairs: list[list[tuple[int, int]]] = [[] for _ in range(n * n)]
    for q, (a, b, c) in enumerate(ts.tolist()):
        ids[a].append(q); pairs[a].append((b, c))
        ids[b].append(q); pairs[b].append((a, c))
        ids[c].append(q); pairs[c].append((a, b))
    return (
        [np.asarray(v, dtype=np.int32) for v in ids],
        [
            (
                np.asarray([a for a, _ in p], dtype=np.int32),
                np.asarray([b for _, b in p], dtype=np.int32),
            )
            for p in pairs
        ],
    )


class BadSet:
    def __init__(self, size: int) -> None:
        self.items: list[int] = []
        self.pos = np.full(size, -1, dtype=np.int32)

    def add(self, q: int) -> None:
        if self.pos[q] < 0:
            self.pos[q] = len(self.items)
            self.items.append(q)

    def discard(self, q: int) -> None:
        p = int(self.pos[q])
        if p >= 0:
            last = self.items[-1]
            self.items[p] = last
            self.pos[last] = p
            self.items.pop()
            self.pos[q] = -1


def load_matrix(path: Path, transpose: bool) -> np.ndarray:
    rows = [[int(t) - 1 for t in line.split()] for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    if not rows or any(len(row) != len(rows) for row in rows):
        raise ValueError("matrix must be square")
    data = np.asarray(rows, dtype=np.int8)
    if transpose:
        data = data.T.copy()
    return data


def load_checkpoint(path: Path, transpose: bool) -> np.ndarray:
    record = json.loads(path.read_text(encoding="utf-8"))
    n = int(record["n"])
    data = np.asarray(record["best_grid"], dtype=np.int8).reshape((n, n)) - 1
    if np.any((data < 0) | (data > 2)):
        raise ValueError("checkpoint colors must serialize in {1,2,3}")
    if transpose:
        data = data.T.copy()
    return data


def seed_grid(n: int, rng: np.random.Generator, matrix: np.ndarray | None) -> np.ndarray:
    grid = rng.integers(0, 3, size=n * n, dtype=np.int8)
    if matrix is not None:
        if np.any((matrix < 0) | (matrix > 2)):
            raise ValueError("initial internal colors must lie in {0,1,2}")
        m = min(n, matrix.shape[0])
        view = grid.reshape((n, n))
        view[:m, :m] = matrix[:m, :m]
    return grid


def conflict_mask(grid: np.ndarray, ts: np.ndarray) -> np.ndarray:
    return (grid[ts[:, 0]] == grid[ts[:, 1]]) & (grid[ts[:, 0]] == grid[ts[:, 2]])


def render_grid(grid: np.ndarray, n: int) -> str:
    return "\n".join(" ".join(str(int(v) + 1) for v in grid[r * n:(r + 1) * n]) for r in range(n)) + "\n"


def run(n: int, seed: int, wall_seconds: float, initial: np.ndarray | None, walk_probability: float) -> dict[str, object]:
    rng = np.random.default_rng(seed)
    ts = triples(n)
    inc, other = incidence(n, ts)
    started = time.perf_counter()
    deadline = started + wall_seconds
    best_count = len(ts) + 1
    best_grid: np.ndarray | None = None
    improvements: list[dict[str, int | float]] = []
    restarts = 0
    moves = 0
    initial_conflicts = None

    while time.perf_counter() < deadline and best_count:
        if restarts == 0:
            grid = seed_grid(n, rng, initial)
        elif best_grid is not None and restarts % 3 != 2:
            grid = best_grid.copy()
            perturb = max(3, (n * n * min(20, 3 + restarts)) // 200)
            cells = rng.choice(n * n, size=perturb, replace=False)
            grid[cells] = (grid[cells] + rng.integers(1, 3, size=perturb, dtype=np.int8)) % 3
        else:
            grid = seed_grid(n, rng, initial if restarts % 2 == 0 else None)

        bad_mask = conflict_mask(grid, ts)
        bad = BadSet(len(ts))
        for q in np.flatnonzero(bad_mask):
            bad.add(int(q))
        weights = np.ones(len(ts), dtype=np.int32)
        if initial_conflicts is None:
            initial_conflicts = len(bad.items)
        if len(bad.items) < best_count:
            best_count = len(bad.items)
            best_grid = grid.copy()
            improvements.append({"move": moves, "conflicts": best_count, "restart": restarts, "wall_millis": int(1000 * (time.perf_counter() - started))})

        plateau = 0
        while bad.items and time.perf_counter() < deadline:
            # Prefer a high-weight conflict among a fixed-size random sample.
            sample_size = min(8, len(bad.items))
            sampled = rng.choice(len(bad.items), size=sample_size, replace=False)
            q = max((bad.items[int(p)] for p in sampled), key=lambda z: int(weights[z]))
            tri = ts[q]
            candidates: list[tuple[int, int, int, int]] = []
            for cell0 in tri:
                cell = int(cell0)
                ids = inc[cell]
                o1, o2 = other[cell]
                old_weight = int(weights[ids][bad_mask[ids]].sum())
                old_count = int(bad_mask[ids].sum())
                current = int(grid[cell])
                for color in range(3):
                    if color == current:
                        continue
                    new_bad = (grid[o1] == color) & (grid[o2] == color)
                    delta_weight = int(weights[ids][new_bad].sum()) - old_weight
                    delta_count = int(new_bad.sum()) - old_count
                    candidates.append((delta_weight, delta_count, cell, color))

            if rng.random() < walk_probability:
                chosen = candidates[int(rng.integers(len(candidates)))]
            else:
                best_key = min((dw, dc) for dw, dc, _, _ in candidates)
                tied = [item for item in candidates if item[:2] == best_key]
                chosen = tied[int(rng.integers(len(tied)))]

            if chosen[0] >= 0:
                # Breakout step: unsatisfied clauses become more expensive.
                weights[np.asarray(bad.items, dtype=np.int32)] += 1
                plateau += 1
            else:
                plateau = max(0, plateau - 1)

            _, _, cell, color = chosen
            grid[cell] = color
            for q0 in inc[cell]:
                z = int(q0)
                a, b, c = ts[z]
                is_bad = bool(grid[a] == grid[b] and grid[a] == grid[c])
                bad_mask[z] = is_bad
                if is_bad:
                    bad.add(z)
                else:
                    bad.discard(z)
            moves += 1

            if len(bad.items) < best_count:
                best_count = len(bad.items)
                best_grid = grid.copy()
                improvements.append({"move": moves, "conflicts": best_count, "restart": restarts, "wall_millis": int(1000 * (time.perf_counter() - started))})
                plateau = 0
            if not bad.items:
                break
            if plateau >= 5000 or int(weights.max()) >= 10000:
                break
        restarts += 1

    elapsed = time.perf_counter() - started
    assert best_grid is not None
    if np.any((best_grid < 0) | (best_grid > 2)):
        raise AssertionError("search produced an out-of-domain color")
    best_text = render_grid(best_grid, n)
    return {
        "schema": "round2_lower_breakout_v1",
        "status": "SAT_WITNESS_PENDING_INDEPENDENT_VERIFICATION" if best_count == 0 else "UNDECIDED",
        "non_claims": ["A positive conflict count at the wall limit does not imply UNSAT"],
        "n": n,
        "colors": 3,
        "orientation": "(x,y),(x+d,y),(x+d,y+d)",
        "generator": "numpy.random.Generator(PCG64)",
        "seed": seed,
        "wall_cap_seconds": wall_seconds,
        "wall_seconds": elapsed,
        "moves": moves,
        "restarts": restarts,
        "geometric_triples": len(ts),
        "initial_conflicts": initial_conflicts,
        "best_conflicts": best_count,
        "improvements": improvements,
        "best_grid": [int(v) for v in best_grid],
        "canonical_best_matrix_sha256": hashlib.sha256(best_text.encode("ascii")).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--wall-seconds", type=float, required=True)
    parser.add_argument("--walk-probability", type=float, default=0.03)
    parser.add_argument("--initial-matrix", type=Path)
    parser.add_argument("--checkpoint-json", type=Path)
    parser.add_argument("--transpose-initial", action="store_true")
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--witness", type=Path, required=True)
    args = parser.parse_args()
    if not (0 < args.wall_seconds <= 60):
        raise ValueError("wall epoch must lie in (0,60] seconds")
    if args.initial_matrix and args.checkpoint_json:
        raise ValueError("choose one initial input")
    initial = None
    if args.initial_matrix:
        initial = load_matrix(args.initial_matrix, args.transpose_initial)
    elif args.checkpoint_json:
        initial = load_checkpoint(args.checkpoint_json, args.transpose_initial)
    record = run(args.n, args.seed, args.wall_seconds, initial, args.walk_probability)
    if record["best_conflicts"] == 0:
        grid = np.asarray(record["best_grid"], dtype=np.int8)
        args.witness.parent.mkdir(parents=True, exist_ok=True)
        args.witness.write_text(render_grid(grid, args.n), encoding="ascii")
        record["witness"] = str(args.witness)
    else:
        record["witness"] = None
    args.result.parent.mkdir(parents=True, exist_ok=True)
    args.result.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: record[key] for key in ("status", "n", "geometric_triples", "initial_conflicts", "best_conflicts", "moves", "restarts", "wall_seconds", "witness")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
