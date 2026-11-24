"""Check a weighted triangle certificate with exact integer arithmetic."""
import argparse
import json
import lzma
import subprocess
import sys
from heapq import heappush, heapreplace
from collections import Counter
from itertools import chain, permutations, product
from math import comb
from pathlib import Path

from verify_triangle_boundary import extend, listed, seed
from verify_square_patches import fits_checked_square

ROOT = Path(__file__).resolve().parent


def geometry(n):
    corners = []
    for x in range(1, n):
        for y in range(x):
            for j in range(1, n-x):
                key = (j, *sorted((x-y-1, y, n-x-j-1)))
                i = x*(x-1)//2+y
                k = (x+j)*(x+j-1)//2+y
                corners.append((key, i, k, k+j))
    multiplicity = Counter(row[0] for row in corners)
    keys = sorted(multiplicity)
    ids = {k: i for i, k in enumerate(keys)}
    assert len(corners) == comb(n, 3)
    return keys, multiplicity, [(ids[key], a, b, c) for key, a, b, c in corners]


def profile(word, corners):
    out = []
    for k, a, b, c in corners:
        x, y, z = word[a], word[b], word[c]
        assert x != y or y != z
        if x != y and x != z and y != z:
            out.append(k)
    return tuple(sorted(out))


def rebuild(n, budget, search, extender, jobs):
    first = n-budget+3
    assert 5 <= first <= n
    words = seed(search, first, 3, jobs)
    for side in range(first+1, n+1):
        bound = 3+side-first
        words = extend(extender, side-1, bound, words)
        _, shell = listed([search, str(side), "shell", str(bound), "0", "0", "list"])
        words.update(shell)
    return words


def unpack(rule, N):
    n, d, weights, *band = rule
    Q = N-2-d*(n-2)
    if len(band) == 3:
        kind, lo, hi = band
    else:
        kind = "min"
        lo, hi = band if band else (0, Q//3+1)
    assert kind in ("min", "max", "both")
    if kind == "both":
        lo, hi = tuple(lo), tuple(hi)
        assert len(lo)==len(hi)==2
        limits = (Q//3+1, Q+1)
        assert all(type(v) is int and type(w) is int and 0<=v<w<=z for v,w,z in zip(lo,hi,limits))
    else:
        bound = Q//3+1 if kind == "min" else Q+1
        assert type(lo) is int and type(hi) is int and 0 <= lo < hi <= bound
    return n, d, weights, kind, lo, hi, Q


def in_band(kind, lo, hi, a, b, c):
    if kind=="both":
        return lo[0]<=min(a,b,c)<hi[0] and lo[1]<=max(a,b,c)<hi[1]
    value = min(a,b,c) if kind=="min" else max(a,b,c)
    return lo<=value<hi


def translation_terms(Q, kind, lo, hi):
    """Signed lower-coordinate restrictions for the indicated translation band."""
    terms = Counter()
    if kind == "min":
        terms[lo, lo, lo] += 1
        terms[hi, hi, hi] -= 1
    else:
        min_thresholds = ((0,1),) if kind=="max" else ((lo[0],1),(hi[0],-1))
        max_lo, max_hi = (lo,hi) if kind=="max" else (lo[1],hi[1])
        for smallest, min_sign in min_thresholds:
            for threshold, sign in [(max_hi,1),(max_lo,-1)]:
                for bits in product((0,1),repeat=3):
                    corner = tuple(max(smallest,threshold) if bit else smallest for bit in bits)
                    terms[corner] += min_sign*sign*(-1)**sum(bits)
    return [(a, b, c, v) for (a, b, c), v in terms.items() if v and a+b+c <= Q]


def exact_incidence(N, rules, sources, keep=0, caps=()):
    """Count placements at every host corner using independent row interval additions."""
    placements = {}
    for rule in rules:
        n, d, weights, kind, lo, hi, Q = unpack(rule, N)
        terms = translation_terms(Q, kind, lo, hi)
        _, keys, _, _ = sources[n]
        look = dict(zip(keys, weights))
        for j in range(1, n-1):
            shifts = placements.setdefault(j*d, Counter())
            for a in range(n-j-1):
                for b in range(n-j-1-a):
                    c = n-j-2-a-b
                    w = look[(j, *sorted((a, b, c)))]
                    if w:
                        for u, v, t, sign in terms:
                            shifts[d*a+u, d*b+v, d*c+t] += sign*w
    cap_cost = 0
    for i,j,k,weight in caps:
        assert all(type(t) is int and t >= 0 for t in (i,j,k,weight))
        assert i <= j <= k and i+j+k <= N-3
        order = N-i-j-k
        bound = comb(order,2)-(order-1)+(order-1)//3
        shifts = set(permutations((i,j,k)))
        cap_cost += weight*len(shifts)*bound
        for h in range(1,order-1):
            bucket = placements.setdefault(h, Counter())
            for position in shifts:
                bucket[position] -= weight
    maximum = 0
    top = []
    for h, shifts in placements.items():
        L = N-h-2
        differences = [[0]*(L-A+2) for A in range(L+1)]
        for (a, b, c), w in shifts.items():
            for A in range(a, L-b-c+1):
                differences[A][b] += w
                differences[A][L-A-c+1] -= w
        for row in differences:
            running = 0
            for change in row[:-1]:
                running += change
                assert caps or running >= 0
                maximum = max(maximum, running)
                if keep and running > 0:
                    if len(top) < keep:
                        heappush(top, running)
                    elif running > top[0]:
                        heapreplace(top, running)
            assert running+row[-1] == 0
    return maximum, sum(top)+cap_cost


def verify(cert, catalogs):
    N = cert["host"]
    patch_level = cert.get("square_patches", 0)
    assert patch_level in (0, 1, 2, 3, 5, 6, 7, 9, 10)
    sources = {}
    for n, b in cert["sources"]:
        keys, multiplicity, corners = geometry(n)
        words = catalogs[f"{n}/{b}"]
        assert len(words) == len(set(words))
        assert all(len(w) == comb(n, 2) and set(w) <= set("012") for w in words)
        profiles = {profile(w, corners) for w in words}
        assert all(len(p) <= b for p in profiles)
        sources[n] = b, keys, multiplicity, profiles
    incidence = Counter()
    copy_counts = {}
    total = 0
    for rule in cert["rules"]:
        n, d, weights, kind, lo, hi, Q = unpack(rule, N)
        b, keys, multiplicity, profiles = sources[n]
        assert 1 <= d <= (N-2)//(n-2) and len(weights) == len(keys)
        assert all(type(v) is int and v >= 0 for v in weights)
        floor = min(chain([(b+1)*min(weights)], (sum(weights[i] for i in p) for p in profiles)))
        terms = translation_terms(Q, kind, lo, hi)
        copies = sum(sign*comb(Q-u-v-t+2, 2) for u, v, t, sign in terms)
        region = Q, kind, lo, hi
        if region not in copy_counts:
            copy_counts[region] = sum(
                in_band(kind,lo,hi,a,b,Q-a-b)
                for a in range(Q+1) for b in range(Q-a+1)
            )
        assert copies == copy_counts[region]
        total += floor*copies
        patch_minimum = 12 if n==13 and patch_level else 8 if n==12 and patch_level>=3 else 0
        thresholds = [patch_minimum] if patch_minimum else []
        if patch_level >= 9 and n==13:
            thresholds.append(13)
        if patch_level >= 6 and n==12:
            thresholds.append(9)
        previous = floor
        for threshold in thresholds:
            patch_floor = threshold*min(weights)
            if patch_level >= 5:
                unseen_floor = max(b+1,threshold)*min(weights)
                patch_floor = min(chain([unseen_floor], (
                    sum(weights[i] for i in p) for p in profiles if len(p) >= threshold
                )))
            extra = patch_floor - previous
            if extra > 0:
                covered = sum(
                    fits_checked_square(N,n,d,a,b,patch_level,threshold)
                    for a in range(Q+1) for b in range(Q-a+1)
                    if in_band(kind,lo,hi,a,b,Q-a-b)
                )
                total += extra*covered
            previous = max(previous,patch_floor)
        for (j, a, c, e), w in zip(keys, weights):
            incidence[j*d] += multiplicity[j, a, c, e]*w
    upper = comb(N, 2)-(N-1)+(N-1)//3
    ranked = cert.get("mode") == "ranked"
    if cert.get("mode") in ("exact", "bands", "ranked", "regions"):
        K, heaviest = exact_incidence(N, cert["rules"], sources, upper if ranked else 0, cert.get("upper_caps", ()))
    else:
        K, heaviest = max(incidence.values()), 0
    ceiling = heaviest if ranked else K*upper
    margin = total-ceiling
    assert margin > 0
    print(f"Side {N}, weighted lower total {total:,}, maximum incidence {K:,}, "
          f"global rainbow ceiling {upper:,}, weighted ceiling {ceiling:,}, contradiction margin {margin:,}.")
    return margin


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rebuild", nargs=2, metavar=("SEARCH", "EXTEND"),
                        help="re-enumerate every archived low-rainbow catalog")
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--stream-extend", type=Path, help="compiled verify_triangle_stream.c for larger catalog cutoffs")
    parser.add_argument("--rup-checker", type=Path, help="drat-trim for rebuilding empty catalogs above order 15")
    args = parser.parse_args()
    cert = json.loads((ROOT/"triangle_grid_certificate.json").read_text())
    catalogs = json.loads(lzma.decompress((ROOT/"triangle_grid_catalogs.json.xz").read_bytes()))
    if args.rebuild:
        search, extender = (str(Path(p).resolve()) for p in args.rebuild)
        sources = {tuple(row) for row in cert["sources"]}
        improved = sources & {(15,14),(16,15),(17,16),(18,17)}
        higher = {(n,b) for n,b in sources if n>15} | improved
        if higher:
            if not args.rup_checker:
                parser.error("--rebuild needs --rup-checker for the interior and boundary proofs")
            assert higher <= {(16,14),(17,15),(18,16)} | improved
            assert all(catalogs[f"{n}/{b}"]==[] for n,b in higher)
            checker = str(args.rup_checker.resolve())
            subprocess.run([sys.executable,str(ROOT/"verify_order16_interior.py"),checker],check=True)
            if improved:
                subprocess.run([sys.executable,str(ROOT/"verify_minimizer_extensions.py"),"--through-12"],check=True)
                subprocess.run([sys.executable,str(ROOT/"verify_order16_interior.py"),checker,"--improved"],check=True)
            if any(n>=17 for n,_ in higher):
                subprocess.run([sys.executable,str(ROOT/"verify_rainbow_boundary_layers.py"),checker],check=True)
        deeper = {(13,12),(14,13)} & sources
        if deeper or improved:
            if not args.stream_extend:
                parser.error("--rebuild needs --stream-extend for the order-13-through-12 enumeration")
            subprocess.run([sys.executable,str(ROOT/"verify_triangle_stream.py"),search,
                            str(args.stream_extend.resolve()),"--jobs",str(args.jobs),"--order-13-through-12"],check=True)
            if (13,12) in deeper:
                complete = set(lzma.decompress((ROOT/"triangle_13_through_12.txt.xz").read_bytes()).decode("ascii").splitlines())
                assert complete == set(catalogs["13/12"])
            if (14,13) in deeper:
                assert catalogs["14/13"]==[]
        for n, b in cert["sources"]:
            if (n,b) in higher or (n,b) in deeper:
                continue
            words = rebuild(n, b, search, extender, args.jobs)
            assert {w.decode() for w in words} == set(catalogs[f"{n}/{b}"])
            print(f"Reproduced T{n} through {b} rainbows, {len(words):,} orbits.", flush=True)
    result = verify(cert, catalogs)
    assert result == cert["margin"]


if __name__ == "__main__":
    main()
