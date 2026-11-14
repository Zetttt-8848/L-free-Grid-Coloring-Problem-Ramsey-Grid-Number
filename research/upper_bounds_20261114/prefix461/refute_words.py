"""Test each bad prefix word: is the prefix triangle (or block) properly colorable?

For every word w (one line of the input file), build the CNF of triangle_cnf.py
with diagonal w, solve it with CaDiCaL 1.9.5 (PySAT), and
  * if SAT: decode the model, verify the coloring directly, record the word as
    SURVIVING (the local test cannot exclude it);
  * if UNSAT: obtain the DRUP proof, complete it by a DPLL tree if needed, and
    check the whole refutation with the independent forward RUP checker.
Writes a JSON-lines record per word.

Usage: python refute_words.py words.txt out.jsonl [region=tri] [m=len(word)] [limit]
"""
import json
import sys
import time

from triangle_cnf import build, sha
from rup_check import check, solve_with_proof, dpll_completion


def verify_coloring(word, m, region, model, ncells_map=None):
    """Decode a model and check directly that no directed L is monochromatic."""
    pos = set(l for l in model if l > 0)
    cells = []
    if region == "tri":
        cells = [(x, y) for y in range(m) for x in range(y, m)]
    else:
        cells = [(x, y) for y in range(m) for x in range(m)]
    color = {}
    for idx, cell in enumerate(cells):
        cs = [c for c in range(3) if 3 * idx + c + 1 in pos]
        color[cell] = cs[0]
    for i in range(min(len(word), m)):
        assert color[(i, i)] == int(word[i])
    for (x, y) in cells:
        for d in range(1, m):
            p2, p3 = (x + d, y), (x + d, y + d)
            if p2 in color and p3 in color:
                assert not (color[(x, y)] == color[p2] == color[p3]), (x, y, d)
    return True


def main():
    words = [w.strip() for w in open(sys.argv[1]) if w.strip()]
    out = open(sys.argv[2], "a")
    region = sys.argv[3] if len(sys.argv) > 3 else "tri"
    m = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] != "-" else None
    limit = int(sys.argv[5]) if len(sys.argv) > 5 else len(words)
    for w in words[:limit]:
        mm = len(w) if m is None else m
        nv, cls, nL = build(w, mm, region)
        t = time.time()
        sat, res = solve_with_proof(nv, cls)
        rec = {"word": w, "region": region, "m": mm, "vars": nv, "clauses": len(cls),
               "cnf_sha256": sha(nv, cls)}
        if sat:
            verify_coloring(w, mm, region, res)
            rec.update(status="SAT-verified", solve_s=round(time.time() - t, 3))
        else:
            proof = res
            ok, added, _ = check(nv, cls, proof)
            comp = 0
            if not ok:
                lem = [[int(x) for x in l.split()[:-1]] for l in proof if not l.startswith("d")]
                extra = dpll_completion(nv, cls + lem)
                if extra is None:
                    rec.update(status="UNSAT-unchecked")
                    out.write(json.dumps(rec) + "\n"); out.flush()
                    continue
                proof = proof + extra
                comp = len(extra)
                ok, added, _ = check(nv, cls, proof)
            rec.update(status="UNSAT-RUP-checked" if ok else "UNSAT-check-failed",
                       lemmas=added, completion_lemmas=comp,
                       solve_check_s=round(time.time() - t, 3))
        out.write(json.dumps(rec) + "\n")
        out.flush()
        print(rec["status"], w, flush=True)


if __name__ == "__main__":
    main()
