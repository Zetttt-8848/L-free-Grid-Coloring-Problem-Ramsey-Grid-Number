"""Reproduce the local directed-L calculations with Python 3.10+ and integer arithmetic.

The archived JSON is the upstream four-color interval-capacity certificate.
See README.md for the geometry, the enumeration domain, and input provenance.
"""
from hashlib import sha256
from pathlib import Path
import json


def kernel(side):
    """Literal autocorrelations of w_i=i(86-i) and the six-class baseline gap."""
    w = [i * (86 - i) for i in range(1, 86)]
    a = [sum(x * y for x, y in zip(w, w[d:])) for d in range(len(w))]
    b = side - 425
    gap = sum(
        (side - d - 3 * (138 + min(6, max(0, b - d)))) * a[d]
        for d in range(1, len(a))
    ) - side * a[0]
    return a, gap


def exclusions(left, right, length, use_shape):
    # left[i] is z[i], right[i] is z[b-1-i]. Layer k pairs i with k-1-i.
    matches = [0, 0, 0]
    for i in range(length):
        if left[i] == right[length - 1 - i]:
            matches[left[i]] += 1
    capacity = sum(min(2, count) for count in matches)
    if use_shape and 3 <= length <= 6:
        capacity = min(capacity, length - 1)
    return min(6, length) - capacity


def minimum_word_loss(side, depth, use_shape=False):
    b = side - 425
    assert 2 * depth <= b
    a, base_gap = kernel(side)
    # This explicit legal word pair supplies an initial upper bound on the minimum.
    left = [int(i >= 2) for i in range(depth)]
    right = [int(i < 2) for i in range(depth)]
    best = sum(
        exclusions(left, right, k, use_shape) * a[b - k]
        for k in range(1, depth + 1)
    )
    witness = (tuple(left), tuple(right))

    def visit(filled, loss):
        nonlocal best, witness
        # Every future contribution is nonnegative, and the first 'filled'
        # layers only read letters already assigned.
        if loss >= best:
            return
        if filled == depth:
            best = loss
            witness = (tuple(left), tuple(right))
            return
        k = filled + 1
        for x in range(3):
            left[filled] = x
            for y in range(3):
                right[filled] = y
                visit(k, loss + a[b - k] * exclusions(left, right, k, use_shape))

    # Simultaneous color permutation fixes the first left letter to 0
    # and the first right letter to 0 or 1 (equal or different).
    left[0] = 0
    for first_right in (0, 1):
        right[0] = first_right
        visit(1, a[b - 1] * exclusions(left, right, 1, use_shape))
    return best, base_gap + 3 * best, witness


def check_three():
    assert kernel(464)[1] == 477_965_143
    assert kernel(463)[1] == -3_527_580_772
    for depth, shape, expected_loss, expected_gap in (
        (9, False, 1_122_003_552, -161_570_116),
        (9, True, 1_203_174_642, 81_943_154),
        (10, False, 1_322_324_010, 439_391_258),
    ):
        loss, gap, witness = minimum_word_loss(463, depth, shape)
        assert (loss, gap) == (expected_loss, expected_gap)
        print(f"R3 side 463, layers={depth}, shape={shape}: loss={loss:,}, margin={gap:,}")

    z = tuple(map(int, "0002222111212111101000020020022012211"))
    assert len(z) == 37
    a, gap = kernel(462)
    assert gap == -7_476_723_318
    loss = sum(a[37 - k] * exclusions(z, z[::-1], k, True) for k in range(1, 21))
    assert loss == 2_294_135_933
    print(f"R3 side 462, first 20 layers, explicit word: margin={gap + 3*loss:,}")


def four_color():
    source = (Path(__file__).resolve().parents[2] / "exploration/research_round3/four/r4_profile_endpoint_21991300.json")
    raw = source.read_bytes()
    digest = sha256(raw.replace(b"\r\n", b"\n")).hexdigest()
    assert digest == "c5811711bb5d023a45db39855add03b49cf197a96c5bd83f4228dd1ecf943b42"
    doc = json.loads(raw)
    old_side, t = doc["n"], doc["t"]
    assert (old_side, t, len(doc["runs"])) == (21_991_300, 36_000, 561)
    caps = [0]
    for row in doc["runs"]:
        assert row["lo"] == len(caps) and row["lo"] <= row["hi"]
        caps.extend([row["K"]] * (row["hi"] - row["lo"] + 1))
    assert len(caps) == t

    def correlation(d):
        m = t + 1 - d
        return m * (m*m - 1) * (m*m + 1 + 5*d*(t+1)) // 30

    a = [correlation(d) for d in range(t)]
    assert (a[0], a[1], a[-1]) == (doc["a0"], doc["a1"], doc["a_last"])

    def margin(side, stagger):
        total = 0
        for d in range(1, t):
            index = old_side - side + d
            # The last known cap remains valid for every shorter interval.
            if stagger:
                cap = sum(caps[min(t - 1, index + j)] for j in range(12))
            else:
                cap = 12 * caps[min(t - 1, index)]
            total += (side - d - 4 * cap) * a[d]
        return 2 * total - 3 * side * a[0]

    assert margin(old_side, False) == doc["doubled_margin"]
    candidates = (
        (21_991_247, False, -249_084_824_594_960_116_300_176_576),
        (21_991_247, True, 19_425_438_581_938_424_787_936),
        (21_991_246, True, -15_150_556_292_665_326_284_166_784),
    )
    for side, stagger, expected in candidates:
        value = margin(side, stagger)
        assert value == expected
        print(f"R4 side {side:,}, distinct minima={stagger}: margin={value:,}")


if __name__ == "__main__":
    check_three()
    four_color()
