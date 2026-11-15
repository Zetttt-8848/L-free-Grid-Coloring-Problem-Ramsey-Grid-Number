"""Compute the least rainbow count of a proper order-14 extension of each order-13 minimizer."""
import argparse
import json
import lzma
from collections import Counter
from itertools import combinations
from pathlib import Path

from verify_triangle_boundary import cost, orientations

HERE = Path(__file__).resolve().parent


def minimum_extension(word):
    n = 13
    parent_score = cost(n,word)
    best = None
    witness = None
    for parent in orientations(n,word):
        assert cost(n,parent)==parent_score
        # For final-row positions i < j, the old cell that completes their L is at (n-j+i,i).
        apex = {(i,j):parent[(n-j+i)*(n-j+i-1)//2+i] for i,j in combinations(range(n),2)}
        row = bytearray()

        def visit(extra):
            nonlocal best,witness
            j = len(row)
            if best is not None and parent_score+extra>=best:
                return
            if j==n:
                witness = parent+bytes(row)
                best = parent_score+extra
                assert cost(n+1,witness)==best
                return
            for color in b"012":
                gained = 0
                for i,first in enumerate(row):
                    colors = {first,color,apex[i,j]}
                    if len(colors)==1:
                        break
                    gained += len(colors)==3
                else:
                    row.append(color)
                    visit(extra+gained)
                    row.pop()

        visit(0)
    assert witness is not None
    return best,witness


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through-12",action="store_true",help="also check the 467 twelve-rainbow parent classes")
    args=parser.parse_args()
    if args.through_12:
        all_words=lzma.decompress((HERE/"triangle_13_through_12.txt.xz").read_bytes()).splitlines()
        assert len(set(all_words))==len(all_words)==488
        parents=[w for w in all_words if cost(13,w)==12]
        assert len(parents)==467
        by_score=Counter(minimum_extension(w)[0] for w in parents)
        assert by_score=={17:4,18:10,19:36,20:103,21:172,22:128,23:11,24:3}
        print(f"Twelve-rainbow parent extension minima: {dict(sorted(by_score.items()))}.")
    words = json.loads((HERE/"triangle_13_minimizers.json").read_text())
    assert len(set(words))==len(words)==21
    results=[minimum_extension(w.encode("ascii")) for w in words]
    by_minimum=Counter(v for v,_ in results)
    assert by_minimum=={19:6,20:8,21:7}
    assert min(v for v,_ in results)==19
    print(f"Minimum extension counts over the 21 geometric and palette classes: {dict(sorted(by_minimum.items()))}.")
    print("An order-14 coloring attaining 19:",min(w for v,w in results if v==19).decode("ascii"))


if __name__=="__main__":
    main()
