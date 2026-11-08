"""Independently enumerate proper colorings using physical NAE triples."""
from collections import Counter,defaultdict
from itertools import combinations
from pathlib import Path
import json,hashlib,time

def require(ok,msg):
    if not ok:raise ValueError(msg)

def main():
    start=time.monotonic();a=[0,1,2,3,4,6,7,9,10]
    cells=sorted((v,u) for u,v in combinations(a,2));ids={p:i for i,p in enumerate(cells)}
    ts=[]
    for pts in combinations(cells,3):
        p,q,r=sorted(pts)
        if p[1]==q[1] and q[0]==r[0] and q[0]-p[0]==r[1]-q[1]>0:
            ts.append(sum(1<<ids[x] for x in pts))
    fs=defaultdict(int)
    for i,(x,y) in enumerate(cells):fs[x-y]|=1<<i
    sizes={d:m.bit_count() for d,m in fs.items()};floor=sum(r%2 for r in sizes.values())
    degrees=Counter(i for t in ts for i in range(len(cells)) if t>>i&1)
    allmask=(1<<len(cells))-1; nodes=0;count=0;dist=Counter();badsets=Counter();bestphi=10**9;best=None;models=[]
    def walk(ones,zeros):
        nonlocal nodes,count,best,bestphi
        nodes+=1
        if nodes%4096==0 and time.monotonic()-start>60:raise TimeoutError('60 second enumeration cap')
        record={'propagation':[]};changed=True
        while changed:
            changed=False
            for t in ts:
                if t&ones==t or t&zeros==t:
                    record['conflict']=t;return record
                unknown=t&~(ones|zeros)
                if unknown and unknown.bit_count()==1:
                    if (t&ones).bit_count()==2:
                        zeros|=unknown;changed=True;record['propagation'].append([t,unknown,0])
                    elif (t&zeros).bit_count()==2:
                        ones|=unknown;changed=True;record['propagation'].append([t,unknown,1])
        free=allmask&~(ones|zeros)
        if not free:
            count+=1;models.append(ones);phi=0;bad=[]
            for d,m in fs.items():
                s=sizes[d]-2*(ones&m).bit_count();phi+=s*s
                if s*s>sizes[d]%2:bad.append(d)
            dist[phi]+=1;badsets[tuple(sorted(bad))]+=1
            if phi<bestphi:bestphi,best=phi,ones
            record['model']=ones;return record
        v=max((i for i in range(len(cells)) if free>>i&1),key=lambda i:degrees[i])
        record['branch_variable']=v
        record['one']=walk(ones|1<<v,zeros);record['zero']=walk(ones,zeros|1<<v)
        return record
    # Complement is a fixed-point-free bijection; pin first cell zero.
    tree=walk(0,1)
    ds=sorted(d for d,r in sizes.items() if r>1);cores=[]
    for k in range(1,len(ds)+1):
        for sub in combinations(ds,k):
            if any(set(c)<=set(sub) for c in cores):continue
            if all(set(sub)&set(b) for b in badsets):cores.append(sub)
    out={'status':'PASS','A':a,'cells':cells,'corners':len(ts),'full_binary_domain':1<<len(cells),
         'symmetry':'First cell pinned zero; global complement gives all remaining colorings.',
         'search_nodes':nodes,'proper_count':2*count,'parity_floor':floor,'minimum_phi':bestphi,
         'minimizer':[int(best>>i&1) for i in range(len(cells))], 'fiber_sizes':sizes,
         'all_proper_colorings':[[int(mask>>i&1) for i in range(len(cells))]
                                  for mask in sorted(models+[allmask^x for x in models])],
         'phi_distribution':{k:2*v for k,v in sorted(dist.items())},
         'frustration_sets':[{'differences':list(k),'count':2*v} for k,v in sorted(badsets.items())],
         'minimal_balance_cores':cores,'elapsed_seconds':time.monotonic()-start,
         'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'scope':'Complete assignment domain for one listed source; does not prove a universal source bound.'}
    Path(__file__).with_name('balance_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    Path(__file__).with_name('balance_branch_proof.json').write_text(json.dumps({
        'A':a,'cells':cells,'pinned_zero_variable':0,'tree':tree},indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('cells','minimizer','frustration_sets')}))
if __name__=='__main__':main()
