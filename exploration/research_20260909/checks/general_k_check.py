"""Exact arithmetic and bounded geometry checks for the general-k route.

Contract: verify arithmetic and finite instances only.  Universal reductions
are proved separately in routes/general_k.md.  Uses Python integer arithmetic
and fractions; no optimizer, floating point, randomness, or external package.
"""
from fractions import Fraction
from itertools import combinations, product
from math import isqrt
import json


def tri(points):
    pts = sorted(points)
    assert len({x-y for x, y in pts}) <= 1
    return {(b[0], a[1]) for a, b in combinations(pts, 2)}


def corners(n):
    return [((x,y),(x+d,y),(x+d,y+d))
            for d in range(1,n) for x in range(n-d) for y in range(n-d)]


def capacities(n, q):
    f = [0]+[1]*n
    layers = [f]
    for colors in range(2,q+1):
        total = 0
        g = [0]
        for m in range(1,n+1):
            # Before m, total is sum_{1 <= r < m} f[r].
            v = (1+isqrt(1+8*(colors-1)*total))//2
            g.append(min(m,v))
            total += f[m]
        layers.append(g)
        f = g
    return layers


def upper(k):
    a = Fraction(4*k+1,2*k)
    ds = [Fraction(k)]
    for i in range(1,k):
        ds.append(a*(k-i)*ds[-1]**2)
    val=2*ds[-1]
    n=(val.numerator+val.denominator-1)//val.denominator
    assert n/ds[-1] >= 2
    for d in ds[:-1]:
        assert n/d >= 4*k+1
    product_val=Fraction(2*k**(2**(k-1))) * a**(2**(k-1)-1)
    for r in range(1,k):
        product_val *= r**(2**(r-1))
    assert val == product_val
    assert n <= (2*k)**(2**k)
    es=[k]
    for i in range(1,k):
        es.append(2*k*es[-1]**2)
    vn=2*es[-1]
    assert vn==2**(2**(k-1))*k**(2**k-1)
    for i,e in enumerate(es[:-1],start=1):
        assert Fraction(vn,e)>=Fraction(k,i)
    return n


def main():
    nesting_sets=nesting_pairs=sidon_sets=0
    for n in range(1,9):
        for bits in product((0,1), repeat=n):
            s={(i,i) for i,b in enumerate(bits) if b}
            t=tri(s)
            nesting_sets+=1
            for d in range(1,n):
                fiber={(x,y) for x,y in t if x-y==d}
                tt=tri(fiber)
                assert tt<=t
                nesting_pairs+=len(tt)
            # T(S) is monochromatically corner-free iff S is Golomb.
            differences=[b[0]-a[0] for a,b in combinations(sorted(s),2)]
            golomb=len(differences)==len(set(differences))
            no_corner=not any(set(c)<=t for c in corners(n))
            assert golomb==no_corner
            sidon_sets+=1
            if golomb:
                m=n
                # Exact weaker bound s <= sqrt(m)+m^(1/4)+1 checked
                # via a rational upper bound using integer roots.
                c=max(1,isqrt(isqrt(max(0,m-1))))
                while c**4 < m-1:
                    c+=1
                if len(s)>c:
                    h=c*len(s)-c*(c+1)//2
                    assert h*(h+1)<=(m-1)*c*(c+1)

    exhaustive=[]
    for n,k in ((2,1),(2,2),(3,2),(4,2),(3,3)):
        cc=[[x*n+y for x,y in c] for c in corners(n)]
        fs=capacities(n,k)[-1]
        free=0
        for coloring in product(range(k),repeat=n*n):
            if any(coloring[a]==coloring[b]==coloring[c] for a,b,c in cc):
                continue
            free+=1
            for d in range(n):
                for color in range(k):
                    s=sum(coloring[(y+d)*n+y]==color for y in range(n-d))
                    assert s<=fs[n-d]
        exhaustive.append(dict(n=n,k=k,colorings=k**(n*n),corner_free=free))

    z=91
    n=z**4
    s=(n+3)//4
    rhs=Fraction(28,5)*z**7+4*z**6+6*z**5+Fraction(18,5)*z**4
    lhs=s*(s-1)
    margin=lhs-rhs
    assert margin>0
    # Rational coefficient checks used by the analytic inequalities.
    assert Fraction(49,30)**2>Fraction(8,3)
    assert Fraction(8,5)**2<Fraction(8,3) # (8/5)/sqrt(8/3) < 1
    assert Fraction(2,1)**2<Fraction(5,4)**2*Fraction(8,3)
    assert Fraction(1,8)**2<Fraction(1,10)**2*Fraction(8,3)
    result=dict(
        exact_upper_bounds={str(k):str(upper(k)) for k in range(1,9)},
        r4=dict(n=n,s=s,lhs=str(lhs),rhs=str(rhs),margin=str(margin)),
        nesting_sets=nesting_sets,nesting_pairs=nesting_pairs,
        golomb_equivalence_sets=sidon_sets,exhaustive_colorings=exhaustive,
        status="All exact arithmetic and bounded finite checks passed; universal claims depend on the written proofs."
    )
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
