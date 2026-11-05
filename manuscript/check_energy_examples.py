"""Independent direct-cube and fiber counts for the two printed examples."""
import argparse, hashlib, itertools, json, re
from pathlib import Path

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source',type=Path,default=Path('Energy_and_forcing_semifinal_revised.tex'))
parser.add_argument('--output',type=Path,default=Path('energy_example_checks.json'))
args=parser.parse_args()
source=args.source
s=source.read_text()
block=s[s.index('\\label{tab:fourcube}'):]
first,rest=block.split('\\end{tabular}',1)
rows=re.findall(r'(\d)&([01]+)&([01]+)\\\\',first)
L={int(i):a for i,a,b in rows};U={int(i):b for i,a,b in rows}
rest=rest.split('\\end{tabular}',1)[0]
X={int(row[0]):list(map(int,row[1:])) for row in re.findall(r'(\d)&([01])&([01])&([01])&([01])&([01])&([01])&([01])&([01])\\\\',rest)}
assert set(L)==set(range(1,8)) and set(X)==set(range(8))
weights=(1,3,9,27)
lower=[sum(weights[i] for i in range(3) if mask&(1<<i)) for mask in range(8)]
A=sorted(lower+[27+a for a in lower]);z={}
for j in range(8):
    for i in range(j):
        z[lower[j],lower[i]]=int(L[j][i])
        z[27+lower[j],27+lower[i]]=int(U[j][i])
for r in range(8):
    for c in range(8):z[27+lower[r],lower[c]]=X[r][c]

def direct_positive_cubes(A):
    """Enumerate ordered positive triples of generators from the definition."""
    present=set(A);maximum=max(A);out=[]
    for x in A:
        for h1 in range(1,maximum-x):
            if x+h1 not in present:continue
            for h2 in range(1,maximum-x-h1):
                if x+h2 not in present or x+h1+h2 not in present:continue
                for h3 in range(1,maximum-x-h1-h2+1):
                    if all(x+sum(h for i,h in enumerate((h1,h2,h3)) if mask&(1<<i)) in present for mask in range(8)):
                        out.append((x,h1,h2,h3))
    return out

def counts(A,z):
    deltas=lambda F:[v-u for u,v in itertools.combinations(F,2)]
    corners=[];D=R=P=T=K3fiber=0;detail=[]
    for d in sorted({v-u for v,u in z}):
        F=[u for u in A if u+d in A]
        B=[u for u in F if z[u+d,u]==0];C=[u for u in F if z[u+d,u]==1]
        r=len(F);imb=abs(len(B)-len(C));rho=len(set(deltas(B))&set(deltas(C)))
        dD=(r-1)*imb;dP=r*max(imb-1,0)//2
        D+=dD;R+=rho;P+=dP;T+=r*(r-1)//2
        ds=deltas(F);K3fiber+=sum(ds.count(h)*(ds.count(h)-1)//2 for h in set(ds))
        detail.append({'offset':d,'r':r,'b':len(B),'c':len(C),'rho':rho,'D':dD,'P':dP})
        for u,v in itertools.combinations(F,2):corners.append((z[u+d,u],z[v+d,u],z[v+d,v]))
    assert sum(len(set(c))==1 for c in corners)==0
    K3direct=len(direct_positive_cubes(A))
    assert K3direct==K3fiber
    return {'n':len(A),'M':len(z),'T':T,'K3_fiber':K3fiber,'K3_direct':K3direct,'D':D,'R':R,'P':P,'old_branches':[2*T-D/2,T+5*R],'new_branches':[2*T-D/2-P,T+5*R-P],'fiber_details':detail}

four=counts(A,z)
assert tuple(four[k] for k in ('n','M','T','K3_direct','D','R','P'))==(16,120,200,120,26,25,8)
edges=list(itertools.combinations(range(4),2))
encoding={sum(5**i for i in edge):set(edge) for edge in edges}
graphA=sorted(encoding)
graphz={(v,u):int(not(encoding[v]&encoding[u])) for u,v in itertools.combinations(graphA,2)}
graph=counts(graphA,graphz)
assert tuple(graph[k] for k in ('n','M','T','K3_direct','D','R','P'))==(6,15,6,0,12,0,6)
report={'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'four_cube':four,'k4':{'A':graphA,**graph},'reduction_fraction':[8,325],
        'reduction_percent':100*8/325,
        'scope':'The two finite examples only; no general optimality, branch switch or classification is certified.'}
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(report,indent=2)+'\n')
for key,result in [('four_cube',four),('k4',graph)]:print(key,{k:v for k,v in result.items() if k!='fiber_details'})
print('Reduction percent:',report['reduction_percent'])
