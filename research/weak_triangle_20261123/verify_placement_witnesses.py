"""Check the square colorings and complete offset coverage claimed in PLACEMENTS.md."""

from verify_143 import DATA, read_json


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


def main():
    records = read_json(DATA / "placement_witnesses.json.xz")
    observed = set()
    for record in records:
        check(record)
        spec = tuple(record["spec"])
        if spec in observed:
            raise ValueError("Duplicate placement")
        observed.add(spec)
    expected = set()
    for order, cutoff, side in ((11, 5, 16), (12, 8, 16), (13, 12, 16), (13, 12, 17)):
        gap = side - order + 1
        expected.update((order, cutoff, side, x, y, 1)
                        for x in range(gap + 1) for y in range(gap + 1)
                        if (x, y) <= (gap - y, gap - x))
    expected.add((13, 12, 18, 3, 2, 1))
    if observed != expected:
        raise ValueError(f"Incorrect placement coverage: {observed ^ expected}")
    print(f"Verified {len(records)} placements and literal full-square witnesses.")


if __name__ == "__main__":
    main()
