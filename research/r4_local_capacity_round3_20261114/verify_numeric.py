"""Independent exact audit of rank propagation and the new R4 arithmetic.

Imports no project research functions. Finite seed UNSAT proofs must be checked
separately. The rational window coverage theorem/data provenance remain inherited.
Run this file from any directory; it writes no files and uses one process.
"""
from bisect import bisect_left, bisect_right
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement
from math import comb, isqrt
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / 'boundary_certificates_20261115'
WIDTHS = (4,8,12,18,24,35,50,70,100,140,200,280,400,600,850,1200,1800)
REF = 21975000
T = 35990


def need(ok, why):
    if not ok:
        raise ValueError(why)


def golomb_bounds(limit=600):
    g = [0, 0]
    for k in range(2, limit+1):
        bound = g[k-1]+1
        endpoint = 0
        running = 0
        for c in range(1, min(130, k-1)+1):
            running += g[c]
            endpoint += running
            H = c*k-c*(c+1)//2
            num = H*(H+1)+4*endpoint
            bound = max(bound, (num+c*(c+1)-1)//(c*(c+1)))
        g.append(bound)
    return g


def audit_spans(bounds, g, seeds, uniform):
    need(bounds[:2] == [0,0], 'span initialization')
    need(g[-1] > bounds[-1], 'Golomb sentinel')
    Q = lambda x: max(0, bisect_right(g,x)-1)
    for k in range(2, len(bounds)):
        need(bounds[k] >= bounds[k-1]+1, 'span monotonicity')
        start = max(bounds[k-1]+1, seeds.get(k,0))
        need(bounds[k] >= start, 'seed preservation')
        endpoint = [0]
        accum = 0
        for c in range(1,min(80,k-1)+1):
            accum += bounds[c]
            endpoint.append(endpoint[-1]+accum)
        # Each integer span below the claimed lower bound is excluded by
        # some rank, using only previously established smaller-cardinality bounds.
        for L in range(start,bounds[k]):
            if not uniform:
                totals = [0]
                costs = [0]
                for h in range(1,L+1):
                    v = Q(L-h)+Q(L-h-1)
                    totals.append(totals[-1]+v)
                    costs.append(costs[-1]+h*v)
            rejected = False
            for c in range(1,len(endpoint)):
                H = c*k-c*(c+1)//2
                if uniform:
                    cap = 2*Q(L-1)
                    if not cap:
                        rejected = True
                        break
                    q,r = divmod(H,cap)
                    price = cap*q*(q+1)//2+r*(q+1)
                else:
                    h = bisect_left(totals,H)
                    if h == len(totals):
                        rejected = True
                        break
                    price = costs[h-1]+h*(H-totals[h-1])
                if 2*price+4*endpoint[c] > L*c*(c+1):
                    rejected = True
                    break
            need(rejected, f'unjustified span: size {k}, span {L}')


@lru_cache(None)
def old_cap(n, binary):
    if n <= 0:
        return 0
    cap = n if binary else (1+isqrt(8*n-7))//2
    gamma = 2*old_cap(n,False) if binary else 1
    for w in WIDTHS:
        a = n+w-1
        cap = min(cap,(a+isqrt(a*a+4*w*a*gamma*(w-1)))//(2*w))
    return cap


def discrepancy(samples, alpha, bounds=None, binary=True):
    b0,b1,p1,k0,step = (1720,1820,21975000,455000,4) if binary else (15000,16600,22500000,4600,8)
    rate = F(k0)/(p1+b1*alpha)
    def cap(n):
        v = old_cap(n,binary)
        return min(v,bisect_right(bounds,n-1)-1) if bounds is not None else v
    total = F(0)
    occupied = set()
    for end,row,binno,*raw in samples:
        need((end,row,binno) not in occupied,'duplicate edge sample')
        occupied.add((end,row,binno))
        probability,g,prior,H = map(F,raw)
        for left in range(0,b0,step):
            right = min(left+step,b0)
            shortfall = H-(prior*cap(b1)+g*cap(right))/(b0*rate)
            # Evaluate every block rather than relying on an early break.
            total += probability*(right-left)*max(F(0),shortfall)**2
    return total


def inner_thresholds(den,r,alpha):
    lengths = []
    for k in range(4600,4801):
        c = F((k-1)*r[0],den)
        z = k*k*c/alpha
        center = isqrt(z.numerator//z.denominator)-c.numerator//c.denominator
        best = 0
        for B in range(max(1,center-2),center+3):
            x = F(k*k*B)/(B+c)-B*alpha
            length = -((-x.numerator)//x.denominator)+52
            p = length-1
            need(15000<=B<=16600 and 52<p<=22500000 and p-1>=400*B,'inner domain')
            need(k*k > (p+B*alpha-52)*(1+c/B),'inner strict exclusion')
            best = max(best,length)
        lengths.append(best)
    need(all(a<b for a,b in zip(lengths,lengths[1:])),'threshold order')
    return lengths


def audit_rows(rows,D,lengths,den,r,alpha):
    need(all(a[0]<b[0] and a[1]>=b[1] for a,b in zip(rows,rows[1:])),'row order')
    Q = lambda p: 4599+bisect_right(lengths,p)
    for offset,cap,B in rows:
        p,k = REF-offset,cap+1
        need(1720<=B<=1820 and D<p<=21975000 and k>=455000 and p-1>=400*B,'binary domain')
        need(lengths[0]<=p-200*B and p<lengths[-1],'Golomb table domain')
        # Sum the piecewise-linear integer correlation exactly on intervals
        # where the staggered multiplicity profile is constant. This does not
        # use the author's baseline-minus-tail-events implementation.
        rr = r+[0]
        blocks = [0]
        for j in range(200):
            blocks.append(blocks[-1]+B*(B+1)//2*rr[j]+B*(B-1)//2*rr[j+1])
        def prefix(h):
            if h < 0:
                return 0
            j,t = divmod(h,B)
            if j>=200:
                return blocks[-1]
            q = t+1
            return blocks[j]+q*B*rr[j]+q*(q-1)//2*(rr[j+1]-rr[j])
        breaks = sorted({1,200*B}|{h for x in lengths for h in (p-x,p-x+1) if 1<h<200*B})
        energy = k*B*r[0]
        for a,b in zip(breaks,breaks[1:]):
            v = Q(p-a)+Q(p-a-1)
            need(v==Q(p-b+1)+Q(p-b),'profile constant on interval')
            energy += 2*v*(prefix(b-1)-prefix(a-1))
        need(k*k*den*B*B > (p+B*alpha-D)*energy,f'binary witness {offset}')


def correlations():
    # Expand w(i)w(i+d), sum powers by telescoping (i+1)^(j+1)-i^(j+1).
    # This is independent of interpolation from ten initial correlations.
    a = [0,5*(T+1)**3,(T+1)**2,-12*(T+1),6]
    out = []
    for d in range(T):
        n = T-d
        powers = [n]
        for j in range(1,9):
            numerator = (n+1)**(j+1)-1-sum(comb(j+1,k)*powers[k] for k in range(j))
            need(numerator%(j+1)==0,'power sum divisibility')
            powers.append(numerator//(j+1))
        shifted = [sum(a[j]*comb(j,k)*d**(j-k) for j in range(k,5)) for k in range(5)]
        out.append(sum(a[j]*shifted[k]*powers[j+k] for j in range(1,5) for k in range(5)))
    need(all(x>y>0 for x,y in zip(out,out[1:])),'decreasing positive correlation')
    return out


def twenty_loss():
    previous = {(0,0,0,0):0}
    for size in range(1,21):
        current = {}
        for u in combinations_with_replacement(range(size+1),4):
            if sum(u)!=size:
                continue
            parents=[]
            for i in range(4):
                if u[i]:
                    v=list(u);v[i]-=1
                    parents.append(previous[tuple(sorted(v))])
            current[u] = max(parents)+max(u)+sum(min(3,x) for x in u)
        previous=current
    need(max(previous.values())==267,'twenty-step maximum')
    return sum(min(s,12) for s in range(1,21))-267//2


def outer(rows,n,weights,loss):
    offset=REF-n
    need(rows[0][0]<=offset+1 and rows[-1][0]>=offset+T+10,'outer coverage')
    prefix=[0]
    for x in weights:
        prefix.append(prefix[-1]+x)
    raw=-3*n*weights[0]+2*sum((n-d)*weights[d] for d in range(1,T))
    # Integrate each capacity interval and each of the twelve minimum ranks.
    for i,(a,cap,_) in enumerate(rows):
        b=rows[i+1][0]-1 if i+1<len(rows) else offset+T+11
        for j in range(12):
            lo=max(1,a-offset-j);hi=min(T-1,b-offset-j)
            if lo<=hi:
                raw-=8*cap*(prefix[hi+1]-prefix[lo])
    blocks=[];bonus=0
    for i in range(1,len(rows)-1):
        a,cap,_=rows[i];center=a-offset
        if (rows[i-1][1]==cap+1 and a-rows[i-1][0]>=20 and rows[i+1][0]-a>=12
                and center-20>=1 and center-1<T):
            blocks.append(center)
            bonus+=8*loss*min(weights[center-s] for s in range(1,21))
    need(all(b-a>=20 for a,b in zip(blocks,blocks[1:])),'disjoint outer blocks')
    return [len(blocks),raw,bonus,loss]


def main():
    data=json.loads((HERE/'transfer_results.json').read_text())
    window=json.loads((OLD/'four_window_correlations.json').read_text())
    den=int(window['denominator']);r=list(map(int,window['correlations']));alpha=F(window['table_excess'])
    need(len(r)==200 and min(r)>=0 and 2*sum(r)-r[0]==den and alpha>0,'window normalization')
    samples=json.loads((OLD/'four_window_edges.json').read_text())
    g=golomb_bounds()
    for name,record in data['variants'].items():
        seeds={int(k):v for k,v in data['seeds'].items()} if name=='nonuniform_with_finite' else {}
        audit_spans(record['binary_spans'],g,seeds,name=='uniform_inherited')
        D=discrepancy(samples,alpha,record['binary_spans'])
        need(D==F(record['D']),f'endpoint discrepancy {name}')
        print(name,'rank bounds and exact discrepancy PASS',flush=True)
    need(discrepancy(samples,alpha,binary=False)>=52,'inherited inner correction')
    thresholds=inner_thresholds(den,r,alpha)
    weights=correlations();loss=twenty_loss()
    consumer=json.loads((HERE/'consumer_results.json').read_text())
    for name,record in consumer.items():
        D=F(record['D'])
        variant='nonuniform_with_finite' if name=='finite_seeded' else 'nonuniform_no_finite'
        need(F(data['variants'][variant]['D'])>=D,'available correction')
        audit_rows(record['rows'],D,thresholds,den,r,alpha)
        parts=outer(record['rows'],record['side'],weights,loss)
        need(parts==record['outer_parts'] and parts[1]+parts[2]==record['margin']>0,'final margin')
        previous=record['previous_test'];prior=outer(record['rows'],previous['side'],weights,loss)
        need(prior[1]+prior[2]==previous['margin'],'previous-side diagnostic')
        print(name,'PASS',record['side'],record['margin'],flush=True)
    print('Scope: independent new arithmetic; seed proof checking and inherited window geometry are separate obligations.')


if __name__=='__main__':
    main()
