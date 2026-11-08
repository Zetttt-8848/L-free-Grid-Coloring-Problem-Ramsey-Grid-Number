"""Independent exact sums for the six-class capacity certificate; no solver."""
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent


def cap(p):
    assert 1<=p<=480
    return min(p, sum(24 if p-j>=426 else 23 for j in range(6)))


def main():
    n=464
    w=[i*(86-i) for i in range(1,86)]
    a=[0]*85
    for i,left in enumerate(w):
        for j,right in enumerate(w):
            if j>=i:a[j-i]+=left*right
    U=[cap(n-d) for d in range(1,85)]
    gap=sum((n-d-3*U[d-1])*a[d] for d in range(1,85))-n*a[0]
    H=[0]*(n+84)
    for x in range(n):
        for i,v in enumerate(w):H[x+i]+=v
    h_energy=sum(v*v for v in H)
    max_class_energy=n*a[0]+2*sum(u*a[d] for d,u in enumerate(U,1))
    literal_gap=h_energy-3*max_class_energy
    assert literal_gap==2*gap and gap>0
    independent_U=[144 if n-d>=426 else 138 for d in range(1,85)]
    old_gap=sum((n-d-3*u)*a[d] for d,u in enumerate(independent_U,1))-n*a[0]
    assert old_gap<=0
    contributions=[{'d':d,'p':n-d,'old_cap':old,'joint_cap':new,
                    'added_margin':3*(old-new)*a[d]}
                   for d,(old,new) in enumerate(zip(independent_U,U),1) if old!=new]
    assert gap-old_gap==sum(r['added_margin'] for r in contributions)
    record={'status':'PASS','n':n,'weight_formula':'i*(86-i), i=1,...,85',
            'weight':w,'autocorrelation':a,'capacity':U,'a0':a[0],
            'joint_margin':gap,'literal_cauchy_margin':literal_gap,
            'independent_cap_margin':old_gap,'improvement_terms':contributions,
            'external_inputs':{'Golomb_span_24_lower':425,'Golomb_span_25_lower':480},
            'scope':'Exact integer certificate; external Golomb computations not rerun',
            'sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in (Path(__file__),HERE/'SIX_CLASS_LEMMA.md')}}
    (HERE/'audit_464.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:record[k] for k in ('status','a0','joint_margin','literal_cauchy_margin','independent_cap_margin','improvement_terms')}))


if __name__=='__main__':main()
