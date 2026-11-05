"""Independent exact checker: parses literal positions, no generator imports."""
import argparse,collections,hashlib,json
from pathlib import Path
TABLE=[0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586]

def main():
    pa=argparse.ArgumentParser();pa.add_argument('witness');pa.add_argument('--output');args=pa.parse_args();path=Path(args.witness);obj=json.loads(path.read_text());n=obj['n'];marks=obj['marks'];size=(n+2)//3
    if not(type(n) is int and n>=1 and isinstance(marks,list) and len(marks)==size and all(type(x) is int and 1<=x<=n for x in marks) and len(set(marks))==size and marks==sorted(marks) and min(marks)==1):raise ValueError('invalid literal set representation')
    counts=collections.Counter(b-a for a in marks for b in marks if a<b);caps={d:2*max(j for j,h in enumerate(TABLE) if h<=n-d) for d in range(1,n)}
    badcaps=[dict(d=d,count=counts[d],cap=caps[d],excess=counts[d]-caps[d]) for d in range(1,n) if counts[d]>caps[d]]
    A=set(marks);badaps=[];ap_checked=0
    # Distinct endpoint-based enumeration, not the generator's d-first AP list.
    for first in range(1,n+1):
        for last in range(first+5,n+1,5):
            d=(last-first)//5;ap_checked+=1
            if all(first+j*d in A for j in range(6)):badaps.append([first+j*d for j in range(6)])
    weight=obj.get('weight',8);score=sum(b['excess']**2 for b in badcaps)+weight*len(badaps)
    out=dict(witness=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),n=n,size=size,pairs_checked=sum(counts.values()),distances_checked=n-1,aps_checked=ap_checked,bad_caps=badcaps,bad_aps=badaps,cap_excess_sum=sum(b['excess'] for b in badcaps),cap_excess_square_sum=sum(b['excess']**2 for b in badcaps),weight=weight,exact_score=score,verdict='PASS' if not badcaps and not badaps else 'FAIL')
    if 'score' in obj:out['recorded_score_matches']=score==obj['score']
    if 'best_score' in obj:out['recorded_score_matches']=score==obj['best_score']
    text=json.dumps(out,indent=2)+'\n';print(text)
    if args.output:Path(args.output).write_text(text)

if __name__=='__main__':main()
