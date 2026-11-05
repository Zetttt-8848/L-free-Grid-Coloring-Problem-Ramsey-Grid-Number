"""Exact local repair attempt; successful output requires separate verification."""
from pathlib import Path
import collections,json,time
ROOT=Path(__file__).resolve().parent
H=(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586)

def main():
    obj=json.loads((ROOT/'window_ap5_600.snapshot.json').read_text());A=obj['marks'];aset=set(A);n=obj['n'];patterns=obj['patterns'];caps=[0]+[2*max(j for j,h in enumerate(H) if h<=n-d) for d in range(1,n)];r=[0]*n
    for i,a in enumerate(A):
        for b in A[i+1:]:r[b-a]+=1
    blockers=collections.defaultdict(list)
    for p in patterns:
        for d in range(1,(n-1)//p[-1]+1):
            for first in range(1,n-p[-1]*d+1):
                edge={first+t*d for t in p};missing=edge-aset
                if len(missing)==1:blockers[next(iter(missing))].append(edge)
                assert missing,'snapshot has a forbidden pattern'
    oldfive=collections.defaultdict(list);newfive=collections.defaultdict(list)
    for d in range(1,(n-1)//4+1):
        for first in range(1,n-4*d+1):
            edge={first+j*d for j in range(5)};missing=edge-aset
            if not missing:oldfive[d].append(edge)
            elif len(missing)==1:newfive[next(iter(missing))].append((d,edge))
    assert all(len(edges)<=1 for edges in oldfive.values())
    proposals=0;cap_pass=0;pattern_pass=0;start=time.time();found=None
    for u in A[1:]:
        base=r[:]
        for a in A:
            if a!=u:base[abs(a-u)]-=1
        for v in range(1,n+1):
            if v in aset:continue
            proposals+=1;rr=base[:]
            for a in A:
                if a!=u:rr[abs(a-v)]+=1
            if any(rr[d]>caps[d] for d in range(1,n)):continue
            cap_pass+=1
            if any(u not in edge for edge in blockers[v]):continue
            pattern_pass+=1;gc={d:sum(u not in edge for edge in edges) for d,edges in oldfive.items()}
            for d,edge in newfive[v]:
                if u not in edge:gc[d]=gc.get(d,0)+1
            if any(c>1 for c in gc.values()):continue
            found=dict(n=n,size=len(A),marks=sorted((aset-{u})|{v}),patterns=patterns,ap5_unique=True,weight=obj['weight'],best_score=0,repair=dict(remove=u,add=v));break
        if found:break
    out=dict(proposals=proposals,cap_pass=cap_pass,pattern_pass=pattern_pass,success=found is not None,runtime_seconds=time.time()-start,scope='single-swap neighborhood of a fixed snapshot only')
    if found:(ROOT/'window_ap5_repair.json').write_text(json.dumps(found,indent=2)+'\n')
    (ROOT/'single_swap_repair.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
