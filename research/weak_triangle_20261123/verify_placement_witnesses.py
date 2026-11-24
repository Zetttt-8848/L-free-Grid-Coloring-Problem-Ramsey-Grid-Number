"""Check the square colorings and complete offset coverage claimed in PLACEMENTS.md."""

from collections import Counter

from verify_143 import BASELINE_PATCHES, DATA, read_json


def corners(side):
    for x in range(side):
        for y in range(side):
            for d in range(1, min(side - x, side - y)):
                yield ((x, y), (x + d, y), (x + d, y + d))


def check(record):
    order, cutoff, side, ox, oy, stride = record["spec"]
    square = record["square"]
    if len(square) != side or any(len(column) != side or set(column) - set("012") for column in square):
        raise ValueError("Invalid square coloring")
    if any(len({square[x][y] for x, y in corner}) == 1 for corner in corners(side)):
        raise ValueError("Monochromatic L in square")
    if min(ox, oy) < 0 or max(ox, oy) + stride * (order - 2) >= side:
        raise ValueError("Triangle does not fit in square")
    count = sum(
        len({square[ox + stride * x][oy + stride * y] for x, y in corner}) == 3
        for corner in corners(order - 1) if corner[0][1] <= corner[0][0]
    )
    if not count == record["rainbows"] <= cutoff:
        raise ValueError("Incorrect rainbow count")


def excluded_by_patch(spec, patches):
    order, cutoff, side, x, y, step = spec
    for m, bound, outer, px, py, spacing in patches:
        if m != order or bound < cutoff or step % spacing:
            continue
        scale = step // spacing
        gap = outer - 1 - (m - 2) * spacing
        for ox, oy in ((px, py), (gap - py, gap - px)):
            left, bottom = x - scale * ox, y - scale * oy
            if min(left, bottom) >= 0 and max(left, bottom) + (outer - 1) * scale < side:
                return True
    return False


def verify_plan(coverage, thresholds):
    patches = set(BASELINE_PATCHES)
    patches.update(map(tuple, read_json(DATA / "side_141_patches.json")))
    patches.update(map(tuple, read_json(DATA / "side_140_patches.json")))
    patches.update(tuple(row["patch"]) for row in read_json(DATA / "order12_side18_0_1.json.xz"))
    for row in read_json(DATA / "order13_side18_profiles.json.xz")["placements"]:
        if not row["survivors"]:
            patches.add((13, 12, 18, *row["offset"], 1))
    expected = {16: (113, 0, 0), 17: (149, 0, 0), 18: (29, 33, 128),
                21: (0, 0, 14), 23: (0, 1, 42)}
    for side, step in ((16, 1), (17, 1), (18, 1), (21, 2), (23, 2)):
        counts = Counter()
        for m, cutoffs in thresholds.items():
            gap = side - 1 - step * (m - 2)
            for cutoff in cutoffs:
                for x in range(gap + 1):
                    for y in range(gap + 1 - x):
                        witness = step == 1 and (m, cutoff, side, x, y) in coverage
                        excluded = excluded_by_patch((m, cutoff, side, x, y, step), patches)
                        if witness and excluded:
                            raise ValueError("A witnessed placement is also claimed to be excluded")
                        counts["witness" if witness else "excluded" if excluded else "open"] += 1
        totals = tuple(counts[key] for key in ("witness", "excluded", "open"))
        if totals != expected[side]:
            raise ValueError(f"Plan totals at side {side} differ from the published table: {totals}")
        print(f"Side {side}: {totals[0]} witnessed, {totals[1]} excluded, {totals[2]} open.")


def main():
    records = read_json(DATA / "placement_witnesses.json.xz")
    thresholds = {11: (5, 6), 12: (8, 9), 13: (12,)}
    coverage = set()
    placements = set()
    for record in records:
        check(record)
        m, cutoff, side, x, y, step = record["spec"]
        gap = side - m + 1
        if (side not in (16, 17, 18) or step != 1 or cutoff not in thresholds[m]
                or (x, y) > (gap - y, gap - x)):
            raise ValueError("Unexpected placement or threshold")
        key = (m, side, x, y)
        if key in placements:
            raise ValueError("Duplicate placement")
        placements.add(key)
        for test in thresholds[m]:
            if cutoff <= test:
                coverage.add((m, test, side, x, y))

    for side in (16, 17):
        for m, cutoffs in thresholds.items():
            gap = side - m + 1
            expected = {(m, cutoff, side, x, y) for cutoff in cutoffs
                        for x in range(gap + 1) for y in range(gap + 1 - x)}
            if not expected <= coverage:
                raise ValueError(f"Missing side-{side} witness at {min(expected - coverage)}")
    side18 = {(m, cutoff): sum(1 for row in coverage if row[:3] == (m, cutoff, 18))
              for m, cutoffs in thresholds.items() for cutoff in cutoffs}
    if side18 != {(11, 5): 8, (11, 6): 12, (12, 8): 0, (12, 9): 8, (13, 12): 1}:
        raise ValueError("Unexpected side-18 witness count")
    if (13, 12, 18, 3, 2) not in coverage:
        raise ValueError("Missing order-13 witness at (3, 2)")
    print(f"Verified {len(records)} literal square colorings across {len(coverage)} cutoff/offset cases.")
    verify_plan(coverage, thresholds)


if __name__ == "__main__":
    main()
