"""Independent recomputation of the decisive inequalities in README.md.

Written separately from sensitivity.py: caps are found by integer bisection on
the defining inequality, sums are evaluated term by term, and nothing is
imported from the search script.  Exact integer arithmetic only.
"""
import json
from pathlib import Path


def pair_cap(q, span):
    """Largest integer s with s*(s-1) <= 2*q*span, by bisection."""
    lo, hi = 1, 2
    while hi * (hi - 1) <= 2 * q * span:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid * (mid - 1) <= 2 * q * span:
            lo = mid
        else:
            hi = mid
    return lo


def conditional_margin(n, q, t):
    a = (n + 3) // 4
    l = n - 1
    total = 0
    for h in range(1, t):
        total += (t - h) * 3 * pair_cap(q, l - h)
    return a * a * t * t - (l + t) * (a * t + 2 * total)


def violates(s, span, w, t):
    """True when s marks with all difference multiplicities <= w contradict lem:shift at t."""
    return s * s * t > (span + t) * (s + w * (t - 1))


def main():
    data = json.loads(Path(__file__).with_name("results.json").read_text(encoding="utf-8"))
    report = {"conditional": [], "status": "PASS"}
    for row in data["conditional_table"]:
        m = conditional_margin(row["certified_side"], row["q"], row["t"])
        ok = m == row["margin"] and m > 0
        report["conditional"].append({"q": row["q"], "side": row["certified_side"], "margin_positive": ok})
        if not ok:
            report["status"] = "FAIL"
    th = data["threshold"]
    m = conditional_margin(th["side"], th["largest_q_with_positive_margin"], th["t"])
    report["threshold_margin_positive"] = m == th["margin"] and m > 0
    el = data["elementary_unconditional"]
    span = el["n"] - 1
    g, b, c = el["golomb_cap"], el["binary_cap"], el["ternary_cap"]
    tg, tb, tt = el["t"]
    report["elementary"] = {
        "golomb_cap_plus_one_excluded": violates(g + 1, span, 1, tg),
        "binary_cap_plus_one_excluded": violates(b + 1, span, 2 * g, tb),
        "ternary_cap_plus_one_excluded": violates(c + 1, span, 3 * b, tt),
        "pigeonhole_class_size": (el["n"] + 3) // 4,
        "pigeonhole_exceeds_ternary_cap": (el["n"] + 3) // 4 >= c + 1,
    }
    if not (report["threshold_margin_positive"] and all(
            v for k, v in report["elementary"].items() if k != "pigeonhole_class_size")):
        report["status"] = "FAIL"
    print(json.dumps(report, indent=2))
    Path(__file__).with_name("check_results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report["status"] != "PASS"


if __name__ == "__main__":
    raise SystemExit(main())
