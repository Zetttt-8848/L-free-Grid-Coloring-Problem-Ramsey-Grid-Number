from bisect import bisect_left
from itertools import combinations
from pathlib import Path
import json

OUT=Path(__file__).parent
H_TABLE=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]
WINDOW=[0,1,2,3,4,5,5,6,7,7,8,9,9,10]

def spacing(top,window):
    ell=[0]
    for i in range(1,top+1):
        primitive=max([i]+([w for w in range(1,14) if WINDOW[w]<=i] if window else []))
        ell.append(max([primitive]+[ell[j]+ell[i-j] for j in range(1,i)]))
    return ell

def audit(n,profile,window,s=None):
    s=(n+2)//3 if s is None else s
    caps=[0]+[2*sum(h<=n-d for h in H_TABLE[1:]) for d in range(1,n)]
    if profile!='inherited':
        for d in range(1,min(27,n-1)+1): caps[d]=min(caps[d],45 if profile=='45' else 46)
        if profile.startswith('46+'):
            for d in range(1,int(profile[3:])+1): caps[d]=min(caps[d],45)
    counts=[0]; masses=[0]
    for d in range(1,n):
        counts.append(counts[-1]+caps[d]);masses.append(masses[-1]+d*caps[d])
    ell=spacing(s-1,window)
    totalell=0;weighted=0;best=None
    for c in range(1,s):
        totalell+=ell[c-1];weighted+=totalell
        size=c*s-c*(c+1)//2
        upper=(n-1)*c*(c+1)//2-2*weighted
        if size>counts[-1]:
            row={'c':c,'H':size,'reason':'capacity','margin':counts[-1]-size}
            return {'n':n,'s':s,'profile':profile,'window':window,'excluded':True,'best':row}
        d=bisect_left(counts,size)
        minimum=masses[d-1]+d*(size-counts[d-1])
        row={'c':c,'H':size,'minimum':minimum,'upper':upper,'margin':minimum-upper,'last_distance':d,'correction':2*weighted}
        if best is None or row['margin']>best['margin']: best=row
    return {'n':n,'s':s,'profile':profile,'window':window,'excluded':best['margin']>0,'best':best}

def main():
    tests=0
    for n in range(2,11):
        for s in range(2,n+1):
            for a in combinations(range(n),s):
                for c in range(1,s):
                    direct=sum(a[h+j]-a[h] for j in range(1,c+1) for h in range(s-j))
                    endpoint=sum((c-i)*(a[s-1-i]-a[i]) for i in range(c))
                    bound=(a[-1]-a[0])*c*(c+1)//2-c*(c*c-1)//3
                    assert direct==endpoint and direct<=bound,(a,c)
                    tests+=1
    rows=[audit(n,p,w) for n in range(450,466) for p in ['inherited','45','46','46+1','46+2','46+3','46+4'] for w in [False,True]]
    bounds=[]
    for w in [False,True]:
        first=next(s for s in range(155,180) if audit(464,'inherited',w,s)['excluded'])
        bounds.append({'window':w,'maximum_not_excluded':first-1,'first_exclusion':audit(464,'inherited',w,first)})
    result={'status':'PASS','small_set_identity_checks':tests,'ell_window':spacing(30,True),'rows':rows,'bounds_at464':bounds}
    (OUT/'endpoint_exact.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'small_checks':tests,'ell':result['ell_window'][:15],'bounds':bounds,'conditional45':[r['n'] for r in rows if r['profile']=='45' and r['window'] and r['excluded']],'three_shaves':audit(464,'46+3',True)},indent=2))

if __name__=='__main__':main()
