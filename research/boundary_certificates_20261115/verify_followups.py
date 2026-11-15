"""Independent literal checks of the follow-up words, partial colorings and endpoint matching.

Run using Python 3.10+. The witness is adjacent; the four-color input is in the repository archive.
"""
from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def scores(word):
    n = 425 + len(word)
    weights = [i * (86-i) for i in range(1,86)]
    corr = [sum(x*y for x,y in zip(weights, weights[d:])) for d in range(85)]
    gap = -n * corr[0]
    loss = 0
    for d in range(1,85):
        overlap = max(0, len(word)-d)
        base = min(6,overlap)
        gap += (n-d-3*(138+base))*corr[d]
        pairs = Counter(left for left,right in zip(word,word[d:]) if left==right)
        contribution = sum(min(2, qty) for qty in pairs.values())
        if 3 <= overlap <= 6:
            contribution = min(overlap-1, contribution)
        loss += (base-contribution)*corr[d]
    return loss, gap+3*loss


def triple_iterator(side):
    for d in range(1,side):
        for x,y in product(range(side-d),repeat=2):
            yield ((x,y),(x+d,y),(x+d,y+d))


def triangle(word, rows):
    n = len(word)
    assert len(rows)==n and all(len(row)==i+1 for i,row in enumerate(rows))
    digits = {p: rows[p[0]][p[1]] for p in ((x,y) for x in range(n) for y in range(x+1))}
    assert all(digits[i,i]==word[i] for i in range(n))
    known = {p for p in digits if word[p[0]]==word[p[1]]}
    assert all(digits[x,y] in '012' and (x==y or digits[x,y]!=word[x]) for x,y in known)
    return digits, known


def check_prescription(entry):
    word = entry["word"]
    n = len(word)
    digits, known = triangle(word,entry["triangle_rows"])
    assert all(v in '012' for v in digits.values())
    counts = Counter()
    for tri in triple_iterator(n):
        if not all(p in digits for p in tri):
            continue
        k = sum(p in known for p in tri)
        counts[k] += 1
        if k>=2:
            assert len({digits[p] for p in tri})>=2
    print(f"word length {n}: {len(known)} prescribed cells, {counts[3]} triples with three prescribed,"
          f" {counts[2]} with two; all pass")
    if n in (36,37):
        loss, gap = scores(word)
        assert (loss,gap)=={36:(3501823174,-863712470),37:(3325904997,2500991673)}[n]
        print(f"  all-shift shape-adjusted loss {loss:,}, margin {gap:,}")
    if "upstream_sources" in entry:
        old, _ = triangle(word,entry["upstream_sources"])
        q = (8,3)
        all_requests=[]
        for tri in triple_iterator(n):
            if all(p in known for p in tri):
                assert len({old[p] for p in tri})>=2
            if q not in tri:
                continue
            pair=tuple(p for p in tri if p!=q)
            if all(p in known for p in pair) and old[pair[0]]==old[pair[1]]:
                all_requests.append((old[pair[0]],pair))
        expected = {('0',((9,3),(9,4))), ('1',((7,2),(8,2))), ('2',((6,1),(8,1)))}
        assert expected <= set(all_requests)
        print("  original order-10 source requests at (8,3):",sorted(expected))


def check_endpoints():
    raw = (HERE.parents[1]/"exploration/research_round3/four/r4_profile_endpoint_21991300.json").read_bytes()
    assert sha256(raw.replace(b"\r\n",b"\n")).hexdigest() == "c5811711bb5d023a45db39855add03b49cf197a96c5bd83f4228dd1ecf943b42"
    archive=json.loads(raw)
    side=21991246
    t=archive["t"]
    m=12
    levels=[0]
    for row in archive["runs"]:
        assert row["lo"]==len(levels)
        levels += [row["K"]]*(row["hi"]-row["lo"]+1)
    shift=archive["n"]-side
    levels += [levels[-1]]*(shift+2*m)
    strict=0
    total=0
    def weight(d):
        r=t+1-d
        return r*(r*r-1)*(r*r+1+5*d*(t+1))//30
    for d in range(1,t):
        i=shift+d
        window=levels[i:i+2*m-1]
        assert all(v-u in (0,-1) for u,v in zip(window,window[1:]))
        assert window[0]-window[-1] <= 1
        # For a single threshold, reverse the first s ranks, permuting a block
        # of s starting and ending ranks. All those sums are s-1.
        s=min(m,window.count(window[0]))
        permutation=list(range(s-1,-1,-1))+list(range(s,m))
        assert sorted(permutation)==list(range(m))
        both=sum(window[j+q] for j,q in enumerate(permutation))
        first=sum(window[:m])
        assert both<=first
        strict += int(both<first)
        total += (side-d-4*both)*weight(d)
    gap=2*total-3*side*weight(0)
    assert strict==0 and gap==-15150556292665326284166784
    print(f"R4 side {side}: {t-1} lags, {strict} strict two-end savings, margin {gap:,}")


if __name__=="__main__":
    cases=json.loads((HERE/"completion_witnesses.json").read_text())
    for n in ("10","36","37"):
        check_prescription(cases[n])
    check_endpoints()
