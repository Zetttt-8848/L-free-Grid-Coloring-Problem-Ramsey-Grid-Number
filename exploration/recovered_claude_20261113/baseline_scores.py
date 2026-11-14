"""Plan-side calibration only (exact integers). Baseline single-diagonal inequality
   sum_{d>0} (n-d-18*cap(n,d)) a_d <= n a_0, cap = 24 if n-1-d>=425 else 23
   (inputs G(24)>=425, G(25)>=480; valid for n<=480). Not a proof artifact."""
from fractions import Fraction
def corr(w): return [sum(w[i]*w[i+d] for i in range(len(w)-d)) for d in range(len(w))]
def cap(n,d): return 24 if n-1-d>=425 else 23
def score(n,w,red=Fraction(0)):
    a=corr(w)
    return sum((n-d-18*(cap(n,d)-red))*a[d] for d in range(1,len(w)))-n*a[0]
tent=lambda h:[min(i,2*h-i) for i in range(1,2*h)]
para=lambda L:[i*(L-i) for i in range(1,L)]
print("tent47", {n:score(n,tent(47)) for n in range(462,467)})
print("para86", {n:score(n,para(86)) for n in range(462,467)})
# best over families at each n with uniform per-class cap reduction 'red'
def best(n,red):
    b=None
    for L in range(20,140):
        for nm,w in (("para",para(L)),):
            a=corr(w); s=Fraction(score(n,w,red),a[0])
            if b is None or s>b[0]: b=(s,nm,L)
    return b
for n in (464,463,460,455,450,440,430,420,400,380):
    # minimal uniform reduction (in units of 1/8 mark per class) making some parabola positive
    r=Fraction(0); 
    while best(n,r)[0]<=0: r+=Fraction(1,8)
    print(n,"min uniform per-class cap reduction ~",float(r),"best",best(n,r)[1:], "frac of 24: %.3f"%(float(r)/24))
