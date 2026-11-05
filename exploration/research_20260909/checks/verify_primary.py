"""Exact independent certificate verification; Python standard library only.

This checks arithmetic, the energy expansion on all 3^n words for n<=7,
and all 2^15 two-colorings of the six-mark strict triangle. It does not prove
the supplied Golomb lower bounds. The report supplies the universal reduction.
"""
from itertools import product
from pathlib import Path
import json


def correlations(w):
    return [sum(w[i]*w[i+d] for i in range(len(w)-d))
            for d in range(len(w))]


def main():
    n = 465
    w = [min(i, 94-i) for i in range(1, 94)]
    a = correlations(w)
    score = sum((n-d-18*(24 if d<=39 else 23))*a[d]
                for d in range(1, 93)) - n*a[0]
    weighted = dict(n=n, length=len(w), sum_weights=sum(w), a0=a[0],
                    total_positive_correlations=sum(a[1:]),
                    distance_moment=sum(d*a[d] for d in range(1, 93)),
                    short_correlations=sum(a[1:40]), score=score)
    assert weighted == dict(n=465,length=93,sum_weights=2209,a0=69231,
        total_positive_correlations=2405225,distance_moment=53496528,
        short_correlations=2038439,score=285630)
    # Separate arithmetic route: expand the entire support of W, without a_d.
    total = [0]*(n+len(w)-1)
    for x in range(n):
        for j, v in enumerate(w):
            total[x+j] += v
    energy_lower_numerator = sum(v*v for v in total)
    energy_upper = n*a[0] + 12*sum((24 if d<=39 else 23)*a[d]
                                  for d in range(1, 93))
    assert energy_lower_numerator == 2162058609
    assert energy_upper == 720495783
    assert energy_lower_numerator - 3*energy_upper == 2*score
    assert energy_lower_numerator//3 == 720686203
    # Check the identity and Cauchy inequality exhaustively on small words.
    words = 0
    test_weights = ([1],[1,1],[1,2,1],[1,0,2,3])
    for size in range(1,8):
        for word in product(range(3), repeat=size):
            words += 1
            for ww in test_weights:
                aa = correlations(ww)
                ff = [[0]*(size+len(ww)-1) for _ in range(3)]
                for x,c in enumerate(word):
                    for j,v in enumerate(ww):
                        ff[c][x+j] += v
                direct = sum(v*v for row in ff for v in row)
                pair = size*aa[0]+2*sum(aa[d]*sum(word[x]==word[x+d]
                    for x in range(size-d)) for d in range(1,min(size,len(ww))))
                ww_energy = sum(sum(ff[c][s] for c in range(3))**2
                    for s in range(size+len(ww)-1))
                assert direct == pair
                assert 3*direct >= ww_energy
    # Strict lower triangles: all geometry comes from the stated corner.
    triangle_counts = {}
    for size in range(2,7):
        points = [(i,j) for i in range(size) for j in range(i)]
        index = {p:i for i,p in enumerate(points)}
        edges=[]
        for i,j in points:
            for d in range(1,size-i):
                edges.append(tuple(index[p] for p in
                    [(i,j),(i+d,j),(i+d,j+d)]))
        free=0
        for word in product(range(2),repeat=len(points)):
            if all(not(word[u]==word[v]==word[z]) for u,v,z in edges):
                free += 1
        triangle_counts[size] = dict(points=len(points),corners=len(edges),free=free)
    assert triangle_counts[5]['free'] == 36
    assert triangle_counts[6]['free'] == 0
    out=dict(weighted_certificate=weighted,
        energy_lower=energy_lower_numerator//3,energy_upper=energy_upper,
        energy_gap=energy_lower_numerator//3-energy_upper,
        exhaustive_word_count=words,weights_per_word=len(test_weights),
        triangles=triangle_counts,
        external_inputs={'G(24) lower bound':425,'G(25) lower bound':480})
    target=Path(__file__).with_name('primary_result.json')
    target.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
