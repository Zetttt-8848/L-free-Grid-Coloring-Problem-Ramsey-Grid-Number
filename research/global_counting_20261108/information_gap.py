"""Exact search for information discarded by scalar diagonal correlations."""
from bisect import bisect_right
from itertools import product
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
POSITIONS=(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481)

def cap(p):
    return bisect_right(POSITIONS,max(p,0))-1

def transport(s):
    if len(s)<2:
        return len(s)
    return max(cap(s[-1]-s[0]+1)+cap(s[-2]-s[1]+1),
               cap(s[-2]-s[0]+1)+cap(s[-1]-s[1]+1))

def statistics(word):
    n=len(word)
    r=[];left=[];right=[];both=[]
    for d in range(1,n):
        p=n-d; starts=[[u for u in range(p) if word[u]==word[u+d]==c] for c in range(3)]
        r.append(sum(map(len,starts)))
        left.append(sum(cap(p-u) for s in starts for u in s[:2]))
        right.append(sum(cap(u+1) for s in starts for u in s[-2:]))
        both.append(sum(transport(s) for s in starts))
    return tuple(r),tuple(left),tuple(right),tuple(both)

def run():
    seen={}; examined=0;answer=None
    for tail in product(range(3),repeat=8):
        word=(0,)+tail
        # Fixing only the first color preserves at least one global relabeling.
        examined+=1
        stat=statistics(word)
        if stat[0] in seen:
            old,oldstat=seen[stat[0]]
            if oldstat[3]!=stat[3]:
                answer={'word1':old,'word2':word,'correlations':stat[0],
                        'word1_caps':oldstat[1:],'word2_caps':stat[1:]}
                break
        else:seen[stat[0]]=(word,stat)
    assert answer is not None
    assert statistics(answer['word1'])[0]==statistics(answer['word2'])[0]
    assert statistics(answer['word1'])[3]!=statistics(answer['word2'])[3]
    output={'status':'EXACT_WITNESS','scope':'two diagonal words only; neither is asserted to extend to a proper square',
            'search_domain':'length9 ternary words with firstcolor0; terminated at first witness',
            'examined':examined,**answer,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'information_gap.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(output))

if __name__=='__main__':run()
