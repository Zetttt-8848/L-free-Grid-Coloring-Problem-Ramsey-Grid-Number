"""Independent direct partition score and feasibility audit."""
from pathlib import Path
import collections,json
ROOT=Path(__file__).resolve().parent
H=(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586)
obj=json.loads((ROOT/'partition600.json').read_text());word=obj['word'];n=obj['n'];assert len(word)==n and all(type(c) is int and c in (0,1,2) for c in word)
bad=[];aps=[];counts=[collections.Counter() for c in range(3)]
for i in range(n):
    for j in range(i+1,n):
        if word[i]==word[j]:counts[word[i]][j-i]+=1
for c in range(3):
    for d in range(1,n):
        cap=2*max(k for k,v in enumerate(H) if v<=n-d)
        if counts[c][d]>cap:bad.append(dict(color=c,d=d,count=counts[c][d],cap=cap,excess=counts[c][d]-cap))
checked=0
for first in range(n):
    for last in range(first+5,n,5):
        checked+=1;step=(last-first)//5
        if len({word[first+j*step] for j in range(6)})==1:aps.append([first+1+j*step for j in range(6)])
score=sum(b['excess']**2 for b in bad)+obj['weight']*len(aps)
out=dict(verdict='PASS' if not bad and not aps else 'FAIL',sizes=[word.count(c) for c in range(3)],distance_caps_checked=3*(n-1),aps_checked=checked,bad_caps=bad,bad_aps=aps,cap_excess_square_sum=sum(b['excess']**2 for b in bad),exact_score=score,recorded_score=obj['best_score'],recorded_score_matches=score==obj['best_score'])
(ROOT/'partition600.check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v if k not in ('bad_caps','bad_aps') else len(v) for k,v in out.items()},indent=2))
