from pathlib import Path
from collections import defaultdict,deque
from itertools import combinations
import json
OUT=Path(__file__).parent
data=json.loads((OUT/'pair_search_log.json').read_text())
answers=[]
for order_str,r in data['rulers'].items():
    order=int(order_str)
    for reflect in [False,True]:
        rr=[r[-1]-x for x in reversed(r)] if reflect else r
        for shift in range(1,463-r[-1]):
            green=[x+shift for x in rr]
            if set(r)&set(green):continue
            F=sorted(r+green);fs=set(F)
            dp=defaultdict(list)
            for a,b in combinations(F,2):dp[b-a].append(a)
            corners=[]
            for d,starts in dp.items():
                for y in starts:
                    for x in starts:
                        if x>=y: corners.append(((x,y),(x+d,y),(x+d,y+d)))
            incident=defaultdict(list)
            for i,tri in enumerate(corners):
                for p in tri:incident[p].append(i)
            colors={(x,x):0 for x in r};colors.update({(x,x):1 for x in green})
            queue=deque(range(len(corners)));steps=[];conflict=None
            while queue:
                tri=corners[queue.popleft()]
                known=[p for p in tri if p in colors]
                if len(known)==3:
                    if len({colors[p] for p in known})==1:conflict=tri;break
                elif len(known)==2 and colors[known[0]]==colors[known[1]]:
                    p=next(p for p in tri if p not in colors);v=1-colors[known[0]]
                    colors[p]=v;steps.append({'point':p,'color':v,'corner':tri});queue.extend(incident[p])
            aps=[(x,d) for d in range(1,(F[-1]-F[0])//4+1) for x in F if x+4*d<=F[-1] and all(x+j*d in fs for j in range(1,5))]
            answers.append({'order':order,'reflected':reflect,'shift':shift,'F':F,'five_ap_count':len(aps),'steps':steps,'conflict':conflict})
            assert conflict is not None,(order,reflect,shift)
result={'rulers':data['rulers'],'family':'equal-order disjoint reflected or unreflected translations with span<=462; first ruler fixed at0','cases':answers}
(OUT/'pair_forcing_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps({'cases':len(answers),'forcing_steps':sum(len(x['steps']) for x in answers),'AP5_free_unions':sum(x['five_ap_count']==0 for x in answers),'status':'CANDIDATE_CERTIFICATES'},indent=2))
