"""Lane B round 2, NTSD-F attempt: the configuration G1+(t) for translate pairs.

Claim (proved by hand in NTSD_F_ATTEMPT.md, Proposition G1+). Let A be a Sidon set with
no positive difference in [1, 2t], and let B = A + t. Suppose there are x < z in A,
b in A with x < b < z and x+z+t-b in A, and d in A with x < d < z-t and x+z-t-d in A.
Then (A, B) carries no TSD coloring. The mixed cell (x+t, z) is forced to 1 from lag
g1 = z-b and to 0 from lag g2 = z-t-d: a type II conflict.

This script checks the claim on random instances (soundness: every instance with a
G1+ configuration must be uncolorable). It also measures how many uncolorable translate
instances are explained by G1+ alone, by type I/II (conflict_check.analyse), and by
unit propagation.

Usage: python g1plus_check.py [seconds]
"""
import json
import random
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ntsd_search as ns      # noqa: E402
import conflict_check as cc   # noqa: E402


def g1plus(A, t):
    """Return one G1+ configuration (x, z, b, d) or None."""
    S = set(A)
    A = sorted(A)
    for i, x in enumerate(A):
        for z in A[i + 1:]:
            mid = [b for b in A if x < b < z]
            if not any((x + z + t - b) in S for b in mid):
                continue
            for d in mid:
                if d < z - t and (x + z - t - d) in S:
                    b = next(b for b in mid if (x + z + t - b) in S)
                    return (x, z, b, d)
    return None


def random_sidon_no_small(m, t, rng):
    A = []
    for x in rng.sample(range(m + 1), m + 1):
        if all(abs(x - a) > 2 * t for a in A) and ns.is_sidon(A + [x]):
            A.append(x)
    return sorted(A)


def main():
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 600
    rng = random.Random(20261123)
    t0 = time.time()
    rows = []
    # (a) Bose-derived translate instances, as in pilot 2
    for q in (13, 17, 19, 23):
        for t in (1, 2, 3):
            for _ in range(15):
                A, B, _ = cc.make_instance(q, t, rng)
                rows.append(("bose", q, t, A))
    # (b) random greedy Sidon sets without small differences (soundness stress test)
    while time.time() - t0 < budget / 3:
        m = rng.randrange(40, 160)
        t = rng.choice((1, 2, 3))
        A = random_sidon_no_small(m, t, rng)
        if len(A) >= 4:
            rows.append(("random", m, t, A))
    out = []
    unsound = 0
    for fam, p, t, A in rows:
        if time.time() - t0 > budget:
            break
        B = [x + t for x in A]
        conf = g1plus(A, t)
        col = ns.colorable(A, B)
        if col is not None:
            assert ns.check_tsd(A, B, col)
        if conf is not None and col is not None:
            unsound += 1
        an = cc.analyse(A, B)
        prop = None
        if col is None:
            prop = cc.propagation_and_search(A, B)["refuted_by_propagation"]
        out.append({"family": fam, "param": p, "t": t, "size": len(A), "colorable": col is not None,
                    "g1plus": conf, "typeI": an["type_I"], "typeII": an["type_II"],
                    "propagation_refutes": prop})
    unc = [r for r in out if not r["colorable"]]
    summ = {
        "instances": len(out), "colorable": len(out) - len(unc), "uncolorable": len(unc),
        "unsound_g1plus_on_colorable": unsound,
        "g1plus_instances": sum(r["g1plus"] is not None for r in out),
        "uncolorable_explained_by_g1plus": sum(r["g1plus"] is not None for r in unc),
        "uncolorable_with_typeI_or_II": sum(r["typeI"] + r["typeII"] > 0 for r in unc),
        "uncolorable_refuted_by_propagation": sum(bool(r["propagation_refutes"]) for r in unc),
        "bose_uncolorable": sum(r["family"] == "bose" for r in unc),
        "bose_uncolorable_g1plus": sum(r["family"] == "bose" and r["g1plus"] is not None for r in unc),
        "elapsed_s": round(time.time() - t0, 1),
    }
    (HERE / "g1plus_results.json").write_text(json.dumps({"summary": summ, "rows": out}, indent=1) + "\n")
    print(summ)


if __name__ == "__main__":
    main()
