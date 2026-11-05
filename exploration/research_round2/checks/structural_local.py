"""P2b/P5 finite local audits; no universal extrapolation from this enumeration."""
from itertools import product
from pathlib import Path
import json
out=[]
for n in (6,7,8):
    count=0; vectors=set()
    for w in product(range(3),repeat=n):
        if any(len({w[x+j*d] for j in range(6)})==1
               for d in range(1,(n-1)//5+1) for x in range(n-5*d)):continue
        count+=1
        vectors.add(tuple(sum(w[i]==w[i+d] for i in range(n-d)) for d in range(1,n)))
    out.append({'n':n,'words':count,'correlation_vectors':len(vectors),
                'min_total_pairs':min(map(sum,vectors)),
                'max_total_pairs':max(map(sum,vectors)),
                'max_adjacent_pairs':max(v[0] for v in vectors)})
assert out[0]['max_total_pairs']==10 and out[0]['max_adjacent_pairs']==4
Path('research_round2/checks/structural_local.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
