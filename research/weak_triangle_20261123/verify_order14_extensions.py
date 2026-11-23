"""Verify the sharp order-14 extension minima for low-rainbow subtriangles."""

import argparse
import json
import lzma
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / "boundary_certificates_20261115"
sys.path.insert(0, str(BASE))
from verify_triangle_boundary import cost, orientations


def subtriangle(word, m, a, b):
    return bytes(word[(x + a + b) * (x + a + b - 1) // 2 + y + b]
                 for x in range(1, m) for y in range(x))


def write_oriented_words(path, order, canonical):
    forms = {}
    for item in canonical:
        word = item.encode("ascii")
        score = cost(order, word)
        for oriented in orientations(order, word):
            if oriented in forms:
                raise ValueError("The supplied catalog repeats an orbit")
            forms[oriented] = score
    with path.open("wb") as stream:
        for word in sorted(forms):
            stream.write(str(forms[word]).encode("ascii") + b" " + word + b"\n")


def verify_row(row, executable, path):
    m, cutoff, best = (row[key] for key in ("source_order", "cutoff", "minimum"))
    word = row["witness"].encode("ascii")
    if set(word) - set(b"012") or cost(14, word) != best:
        raise ValueError("Invalid upper-bound witness")
    scores = [cost(m, subtriangle(word, m, a, b))
              for a in range(15 - m) for b in range(15 - m - a)]
    if min(scores) > cutoff:
        raise ValueError("The witness does not contain the required subtriangle")
    result = subprocess.run([executable, "14", str(m), str(cutoff), str(best - 1), path],
                            check=True, capture_output=True, text=True).stdout.split()
    expected = [str(row["oriented_words"]), str({11: 3, 12: 2}[m])]
    if len(result) != 4 or result[0] != "EXCLUDED" or result[1:3] != expected:
        raise ValueError(f"Incomplete lower-bound search for order {m}, cutoff {cutoff}: {result}")
    if int(result[3]) <= 0:
        raise ValueError("The lower-bound search did not visit any nodes")
    print(f"T{m} through {cutoff}: minimum {best}, {result[1]} oriented words, "
          f"{result[2]} placements, {result[3]} nodes", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("search", type=Path, help="compiled fixed_subtriangle.cpp")
    parser.add_argument("--source-order", type=int, choices=(11, 12))
    args = parser.parse_args()
    rows = json.loads((HERE / "data/order14_extension_minima.json").read_bytes())
    if [(r["source_order"], r["cutoff"]) for r in rows] != (
            [(11, k) for k in range(3, 7)] + [(12, k) for k in range(6, 10)]):
        raise ValueError("Unexpected or incomplete list of cases")
    catalogs = json.loads(lzma.decompress((BASE / "triangle_grid_catalogs.json.xz").read_bytes()))
    with TemporaryDirectory() as cache:
        for order, top in ((11, 6), (12, 9)):
            if args.source_order is not None and order != args.source_order:
                continue
            path = Path(cache) / f"oriented-{order}.txt"
            write_oriented_words(path, order, catalogs[f"{order}/{top}"])
            for row in rows:
                if row["source_order"] == order:
                    verify_row(row, args.search.resolve(), path)


if __name__ == "__main__":
    main()
