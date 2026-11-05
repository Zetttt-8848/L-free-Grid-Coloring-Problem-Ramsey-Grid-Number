"""Search a small explicit polynomial family for a restricted-step construction."""
import itertools,json
from pathlib import Path
ps=list(itertools.product(range(2),repeat=2)); combos=list(itertools.product(range(3),repeat=4))
answer=None
for aa in itertools.product((1,2),repeat=4):
    A=dict(zip(ps,aa))
    for bb in combos:
        B=dict(zip(ps,bb))
        for cc in combos:
            C=dict(zip(ps,cc))
            good=True
            for p,q in ps:
                par=((p,q),(1-p,q),(1-p,1-q))
                for d in (1,3):
                    for r in range(3):
                        val=sum(A[key]*(r+j*d)**2+B[key]*(r+j*d)+C[key] for j,key in enumerate(par))%3
                        if val==0: good=False;break
                    if not good:break
                if not good:break
            if good:
                answer=dict(parities=ps,A=aa,B=bb,C=cc);break
        if answer:break
    if answer:break
Path(__file__).with_suffix('.json').write_text(json.dumps(answer,indent=2),encoding='utf-8')
print(json.dumps(answer))
