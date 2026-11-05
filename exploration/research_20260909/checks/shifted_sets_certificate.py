"""Standard-library, exact-integer certificate for R_3(L) <= 465.

External mathematical inputs, from the supplied MSY PDF Algorithm 3:
every 24-mark Golomb ruler has span >= 425, and every 25-mark
Golomb ruler has span >= 480. No floating-point arithmetic is used.
Run: python research_20260909/checks/shifted_sets_certificate.py
"""
from itertools import combinations, product
import json

N = 465
H = 47
WEIGHTS = [min(i, 2*H-i) for i in range(1,2*H)]

def autocorrelation(w):
    return [sum(w[i]*w[i+d] for i in range(len(w)-d))
            for d in range(len(w))]

def a_formula(h,d):
    if d <= h:
        return (2*h**3+h)//3-h*d*d+(d**3-d)//2
    x=2*h-d
    return (x**3-x)//6

def is_corner(points):
    a,b,c=points
    delta=b[0]-a[0]
    return delta>0 and b[1]==a[1] and c==(b[0],b[1]+delta)

def check_forcing_geometry():
    witnesses=0
    for n in range(2,11):
        for d in range(1,n):
            for r in range(3,n-d+1):
                for B in combinations(range(1,n-d+1),r):
                    by_gap={}
                    for u,v in combinations(B,2):
                        gap=v-u
                        if gap not in by_gap:
                            by_gap[gap]=(u,v)
                            continue
                        s,t=u,v
                        u,v=by_gap[gap]
                        assert u<s and v<t and v-u==t-s
                        Q1=(v+d,u)
                        Q2=(t+d,s)
                        Z=(t+d,u)
                        assert is_corner(((u+d,u),Q1,(v+d,v)))
                        assert is_corner(((s+d,s),Q2,(t+d,t)))
                        assert is_corner(((u,u),Q1,(v+d,v+d)))
                        assert is_corner(((s,s),Q2,(t+d,t+d)))
                        assert is_corner(((u,u),Z,(t+d,t+d)))
                        assert is_corner(((u+d,u),Z,(t+d,t)))
                        assert is_corner((Q1,Z,Q2))
                        assert all(1<=x<=n and 1<=y<=n for x,y in (Q1,Q2,Z))
                        witnesses+=1
    return witnesses

def check_word_identity():
    tested=0
    for n in range(1,8):
        for word in product(range(3),repeat=n):
            # Deliberately asymmetric weights test orientation and indexing.
            w=[1,3,2][:min(3,n)]
            aa=autocorrelation(w)
            counts=[[0]*(n+len(w)-1) for _ in range(3)]
            for pos,c in enumerate(word):
                for i,weight in enumerate(w):
                    counts[c][pos+i]+=weight
            exact=sum(x*x for row in counts for x in row)
            pair_counts=[sum(word[i]==word[i+d] for i in range(n-d))
                         for d in range(len(w))]
            expansion=n*aa[0]+2*sum(aa[d]*pair_counts[d] for d in range(1,len(w)))
            assert exact==expansion
            total_square=sum(sum(counts[c][j] for c in range(3))**2 for j in range(n+len(w)-1))
            total_expansion=n*aa[0]+2*sum(aa[d]*(n-d) for d in range(1,len(w)))
            assert total_square==total_expansion
            assert 3*exact>=total_square
            tested+=1
    return tested

def main():
    a=autocorrelation(WEIGHTS)
    assert a==[a_formula(H,d) for d in range(2*H-1)]
    a0=a[0]
    P=sum(a[1:40])
    Q=sum(a[40:])
    D=sum(d*a[d] for d in range(1,len(a)))
    assert sum(WEIGHTS)==H*H
    assert a0==(2*H**3+H)//3
    assert P==39*a0-H*(39*40*79//6)+((39*40//2)**2-39*40//2)//2
    assert P+Q==(H**4-a0)//2
    assert D==H*(H-1)*(H+1)*(7*H*H+2)//30
    required=N*(P+Q)-D
    permitted=N*a0+432*P+414*Q
    assert required-permitted==285630>0
    print(json.dumps({
        'claim':'R_3(L) <= 465, conditional only on the two supplied exact Golomb minima',
        'arithmetic':'Python arbitrary-precision integers; no numerical solver',
        'external_inputs':{'G(24)_lower_bound':425,'G(25)_lower_bound':480},
        'n':N,'h':H,'weight_formula':'w_i = min(i, 94-i), 1 <= i <= 93',
        'a0':a0,'P_sum_d1_to39':P,'Q_sum_d40_to92':Q,'D_sum_d_times_a_d':D,
        'required':required,'permitted':permitted,'contradiction_margin':required-permitted,
        'geometry_witnesses_n2_to10':check_forcing_geometry(),
        'all_3_color_words_lengths1_to7':check_word_identity(),
        'checks':'All assertions passed; bounded tests supplement the written universal proof.'
    },indent=2))

if __name__=='__main__':main()
