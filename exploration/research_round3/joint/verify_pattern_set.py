"""Independent exact check of literal set against caps and declared shapes."""
from pathlib import Path
import argparse,collections,json
TABLE=(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586)

def main():
    pa=argparse.ArgumentParser();pa.add_argument('witness');pa.add_argument('--output');args=pa.parse_args();obj=json.loads(Path(args.witness).read_text());A=obj['marks'];n=obj['n'];assert type(n) is int and len(A)==(n+2)//3 and A==sorted(set(A)) and min(A)==1 and max(A)<=n and all(type(a) is int for a in A)
    aset=set(A);counter=collections.Counter(y-x for x in A for y in A if y>x);badcaps=[]
    for d in range(1,n):
        cap=2*max(j for j,h in enumerate(TABLE) if h<=n-d)
        if counter[d]>cap:badcaps.append(dict(d=d,count=counter[d],cap=cap,excess=counter[d]-cap))
    badpatterns=[];copycounts=[]
    for p in obj['patterns']:
        assert p==sorted(set(p)) and min(p)==0
        tested=0
        # Endpoint enumeration differs from the searcher's dilation-first generation.
        for first in range(1,n+1):
            for last in range(first+max(p),n+1,max(p)):
                delta=(last-first)//max(p);tested+=1;copy=[first+delta*j for j in p]
                if all(x in aset for x in copy):badpatterns.append(copy)
        copycounts.append(tested)
    ap5s=collections.defaultdict(list);ap5checked=0
    if obj.get('ap5_unique'):
        for first in range(1,n+1):
            for last in range(first+4,n+1,4):
                d=(last-first)//4;ap5checked+=1
                if all(first+j*d in aset for j in range(5)):ap5s[d].append(first)
    badgroups={d:starts for d,starts in ap5s.items() if len(starts)>1}
    forward=[];reflected=[];h_checked=0
    if obj.get('parametric_family'):
        for h in range(1,(n-2)//11+1):
            h_checked+=1
            ls=[first for first in range(1,n-6*h+1) if all(first+j*h in aset for j in (0,1,2,4,5,6))]
            ks=[first for first in range(1,n-5*h+1) if all(first+j*h in aset for j in (0,3,4,5))]
            js=[first for first in range(1,n-5*h+1) if all(first+j*h in aset for j in (0,1,2,5))]
            forward += [dict(h=h,L_start=x,K_start=z) for x in ls for z in ks if z>x+6*h]
            reflected += [dict(h=h,J_start=y,L_start=x) for x in ls for y in js if x>y+5*h]
    score=sum(b['excess']**2 for b in badcaps)+obj.get('weight',8)*(len(badpatterns)+sum((len(starts)-1)**2 for starts in badgroups.values())+len(forward)+len(reflected));recorded=obj.get('score',obj.get('best_score'))
    out=dict(verdict='PASS' if not badcaps and not badpatterns and not badgroups and not forward and not reflected else 'FAIL',n=n,size=len(A),pair_count=sum(counter.values()),copy_counts=copycounts,all_pattern_copies_checked=sum(copycounts),badcaps=badcaps,badpatterns=badpatterns,ap5_occurrences_checked=ap5checked,ap5_counts={d:len(starts) for d,starts in ap5s.items()},bad_ap5_groups=badgroups,parametric_steps_checked=h_checked,parametric_forward_violations=forward,parametric_reflected_violations=reflected,exact_score=score,recorded_score=recorded,recorded_score_matches=None if recorded is None else score==recorded)
    if args.output:Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
