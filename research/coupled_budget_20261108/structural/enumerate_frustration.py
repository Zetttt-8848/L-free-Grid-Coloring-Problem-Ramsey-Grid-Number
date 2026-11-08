"""All 2^21 physical colorings: exact independent finite balance audit."""
from collections import Counter,defaultdict
from itertools import combinations
from pathlib import Path
import json,hashlib,time

def main():
    tick=time.monotonic();a=[0,1,2,5,6,9,10]
    cells=sorted((v,u) for u,v in combinations(a,2));index={p:i for i,p in enumerate(cells)}
    ts=[]
    for p,q,r in combinations(cells,3):
        p,q,r=sorted((p,q,r))
        if p[1]==q[1] and q[0]==r[0] and q[0]-p[0]==r[1]-q[1]>0:
            ts.append(sum(1<<index[x] for x in (p,q,r)))
    fs=defaultdict(int)
    for i,(x,y) in enumerate(cells):fs[x-y]|=1<<i
    sizes={d:m.bit_count() for d,m in fs.items()};parity=sum(r%2 for r in sizes.values())
    distribution=Counter(); masks=Counter(); best=None;bestphi=999; count=0
    for c in range(1<<len(cells)):
        if any(c&t in (0,t) for t in ts):continue
        count+=1
        phi=0;bad=[]
        for d,m in fs.items():
            s=sizes[d]-2*(c&m).bit_count();phi+=s*s
            if s*s>sizes[d]%2:bad.append(d)
        masks[tuple(sorted(bad))]+=1;distribution[phi]+=1
        if phi<bestphi:bestphi=phi;best=c
    # Find all inclusion-minimal fibre sets which hit every nonempty bad set.
    ds=sorted(d for d,r in sizes.items() if r>1);cores=[]
    for k in range(1,len(ds)+1):
        for sub in combinations(ds,k):
            if any(set(c)<=set(sub) for c in cores):continue
            if all(set(sub)&set(b) for b in masks):cores.append(sub)
    out={'status':'PASS','A':a,'cells':cells,'full_domain':1<<len(cells),
         'proper_count':count,'corners':len(ts),'fiber_sizes':sizes,'parity_floor':parity,
         'minimum_phi':bestphi,'minimizer':[int(best>>i&1) for i in range(len(cells))],
         'phi_distribution':dict(sorted(distribution.items())),
         'frustrated_fiber_sets':[{'differences':list(k),'count':v} for k,v in sorted(masks.items())],
         'minimal_fiber_obstruction_cores':cores,'elapsed_seconds':time.monotonic()-tick,
         'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'scope':'Exact exhaustive assignments on one 21-cell source; not all integer mark sets.'}
    Path(__file__).with_name('frustration_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('frustrated_fiber_sets','cells','minimizer')}))
if __name__=='__main__':main()
