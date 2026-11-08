"""Exact finite diagnostic for shared-prefix color compatibility.

Not a proof of the conjectured formula for arbitrary word length. Numba
accelerates finite integer enumeration; no SAT or optimization solver.
"""
import itertools
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from numba import njit

HERE=Path(__file__).resolve().parent


@njit
def solve(aa,bb,popcount,K,weights):
    best=-1;ai=-1;bi=-1
    for i in range(len(aa)):
        for j in range(len(bb)):
            score=0
            for k in range(1,K+1):
                for c in range(3):
                    score+=min(2,popcount[aa[i,c]&(bb[j,c]>>(K-k))])*weights[k-1]
            if score>best:best=score;ai=i;bi=j
    return best,ai,bi


def main():
    records=[]
    for K in range(5,10):
        start=time.monotonic();aa=[];bb=[];aws=[];bws=[]
        for w in itertools.product(range(3),repeat=K):
            masks=[sum((v==c)<<i for i,v in enumerate(w)) for c in range(3)]
            bb.append(masks);bws.append(w)
            m=-1
            for c in w:
                if c>m+1:break
                m=max(m,c)
            else:aa.append(masks);aws.append(w)
        value,ai,bi=solve(np.array(aa),np.array(bb),np.array([i.bit_count() for i in range(1<<K)]),K,np.ones(K,dtype=np.int64))
        A=aws[ai];B=bws[bi]
        # Witness evaluated with direct colors, not the accelerated bit logic.
        terms=[sum(min(2,sum(A[i]==B[K-k+i]==c for i in range(k))) for c in range(3)) for k in range(1,K+1)]
        assert sum(terms)==value
        item={'K':K,'canonical_A_words':len(aa),'B_words':len(bb),'pairs':len(aa)*len(bb),
              'maximum':value,'A':A,'B':B,'terms':terms,'elapsed_seconds':time.monotonic()-start}
        records.append(item);print(json.dumps(item),flush=True)
    N=86
    weights=np.array([(N-d)*((N-d)**2-1)*((N-d)**2+1+5*d*N)//30 for d in range(37,28,-1)],dtype=np.int64)
    value,ai,bi=solve(np.array(aa),np.array(bb),np.array([i.bit_count() for i in range(1<<K)]),K,weights)
    A=aws[ai];B=bws[bi]
    terms=[sum(min(2,sum(A[i]==B[K-k+i]==c for i in range(k))) for c in range(3)) for k in range(1,K+1)]
    assert sum(int(w)*t for w,t in zip(weights,terms))==value
    baseline=sum(min(6,k)*int(weights[k-1]) for k in range(1,K+1))
    weighted={'n':463,'K':K,'weights':weights.tolist(),'maximum':value,'scalar_baseline':baseline,
              'deficit':baseline-value,'A':A,'B':B,'terms':terms,
              'convolution_gain':3*(baseline-value),'remaining_463_gap':-3527580772+3*(baseline-value)}
    output={'status':'FINITE_ENUMERATION_DIAGNOSTIC','runs':records,'weighted_n463':weighted,
            'formula_under_investigation':'max sum T_k = 4K-10; tested only K=5,...,9 here',
            'scope':'Two arbitrary three-color words, simultaneous color relabeling normalizes A to restricted growth; no square existence conclusion.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'boundary_word_results.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8',newline='\n')


if __name__=='__main__':main()
