"""Independent integer audit of the joint-diagonal 466 contradiction.

The Golomb thresholds below are external mathematical inputs, transcribed from
Mammel--Smith--Yerger arXiv:2502.05162v1 Algorithm 3. No researcher code imported.
"""
from pathlib import Path
import hashlib,json,math

THRESHOLDS=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,
            200,217,247,284,334,357,373,426,481,493,554,586]

def compute(n,k):
    caps=[]
    for d in range(1,n):
        available=n-d
        capacity=max(i for i,t in enumerate(THRESHOLDS) if t<=available)
        caps.append(min(available,2*capacity))
    total=sum(caps);maxclass=max(m for m in range(n+1) if m*(m-1)//2<=total)
    minclass=n-2*maxclass
    if minclass<2*k:raise ValueError('Rank coefficient saturation not established')
    count=k*n-3*k*(k+1)//2
    # Explicitly fill distance slots; this is the independent rearrangement
    # lower bound, with an exchange proof in the audit document.
    remaining=count;minimum=0;filled=[]
    for d,cap in enumerate(caps,1):
        use=min(remaining,3*cap)
        if use:filled.append([d,use]);minimum+=d*use
        remaining-=use
    if remaining:raise ValueError('Insufficient capacity')
    # Construct coefficients by rank for every feasible size triple.
    maxima=set();triples=0
    for a in range(minclass,maxclass+1):
        for b in range(minclass,maxclass+1):
            c=n-a-b
            if not minclass<=c<=maxclass:continue
            weights=[]
            for m in (a,b,c):
                weights.extend(min(k,r)-min(k,m-1-r) for r in range(m))
            weights.sort()
            maxima.add(sum((i+1)*v for i,v in enumerate(weights)))
            triples+=1
    closed=3*k*(k+1)*(n-2*k-1)//2
    if maxima!={closed}:raise ValueError('Coefficient formula disagreement')
    return {'n':n,'k':k,'sum_per_color_difference_caps':total,
            'max_color_class':maxclass,'min_color_class':minclass,
            'rank_pairs':count,'lower_distance_sum':minimum,'upper_distance_sum':closed,
            'contradiction_margin':minimum-closed,'size_triples_checked':triples,
            'distance_fill':filled}

def main():
    result={'status':'PASS','external_input':'arXiv:2502.05162v1 Algorithm3, occupied-position thresholds',
            'table':THRESHOLDS,'checks':[compute(465,22),compute(466,22)],
            'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Exact arithmetic plus every feasible diagonal size triple for the two stated n; external ruler optima not independently proved.'}
    Path(__file__).with_name('joint_bound_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({**result,'checks':[{k:v for k,v in x.items() if k!='distance_fill'} for x in result['checks']]}))
if __name__=='__main__':main()
