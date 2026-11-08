"""Exact discrepancy search around a complete candidate using violated L's.

Every accepted assignment differs from the input on at most K cells. Each
branch commits a previously uncommitted cell to a color different from input.
Proof trees cover every possible repair in the specified radius.
"""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import time
import struct
import zlib
from adaptive_repair import encode,write


def solve(rows,k,seconds,node_cap,retain):
    initial=sum(rows,[]); colors=initial[:];_,edges=encode(len(rows));n=len(rows)
    adjacent=[[] for _ in colors]
    for e,ps in enumerate(edges):
        for v in ps:adjacent[v].append(e)
    bad={e for e,t in enumerate(edges) if len({colors[v]for v in t})==1}
    used=set();nodes=0;start=time.monotonic();solution=None;codes=[]

    def search():
        nonlocal nodes,solution
        nodes+=1
        if nodes>node_cap or (nodes%128==0 and time.monotonic()-start>seconds):raise TimeoutError()
        if not bad:
            solution=[colors[x*n:(x+1)*n] for x in range(n)];return {'sat':True}
        e=min(bad,key=lambda e:(sum(v not in used for v in edges[e]),e))
        if retain:codes.append(e)
        choices=[v for v in edges[e] if v not in used]
        if not choices:return {'locked':e}
        if len(used)==k:return {'radius':e}
        for v in choices:
            old=colors[v];used.add(v)
            saved={f for f in adjacent[v] if f in bad}
            for col in range(3):
                if col==initial[v]:continue
                colors[v]=col
                for f in adjacent[v]:
                    if len({colors[u]for u in edges[f]})==1:bad.add(f)
                    else:bad.discard(f)
                child=search()
                if solution is not None:return child
            colors[v]=old;used.remove(v)
            for f in adjacent[v]:bad.discard(f)
            bad.update(saved)
        return {}

    try:
        tree=search();status='SAT_CANDIDATE' if solution is not None else 'EXHAUSTED_RADIUS'
    except TimeoutError:tree=None;status='UNDECIDED_LIMIT'
    certificate=None
    if retain and status=='EXHAUSTED_RADIUS':
        raw=struct.pack('<'+'H'*len(codes),*codes)
        certificate={'codec':'zlib+base64 of little-endian uint16 preorder edge ids',
            'nodes':len(codes),'raw_sha256':hashlib.sha256(raw).hexdigest(),
            'data':base64.b64encode(zlib.compress(raw,9)).decode('ascii')}
    return {'radius':k,'status':status,'nodes':nodes,'seconds':time.monotonic()-start,
            'certificate':certificate,'grid':solution}


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--max-radius',type=int,default=12);p.add_argument('--per-radius-seconds',type=float,default=15)
    p.add_argument('--node-cap',type=int,default=200000);p.add_argument('--tree-through',type=int,default=4)
    args=p.parse_args()
    if args.output.exists():raise ValueError('Fresh output required')
    rows=json.loads(args.input.read_text(encoding='utf-8'))['grid']
    record={'input_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest(),'input_grid':rows,
        'per_radius_seconds':args.per_radius_seconds,'per_radius_nodes':args.node_cap,'tree_through':args.tree_through,
        'runs':[],'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'non_claim':'Radius exclusion is relative to this one complete candidate, not all21 grids.'}
    for k in range(1,args.max_radius+1):
        result=solve(rows,k,args.per_radius_seconds,args.node_cap,k<=args.tree_through)
        record['runs'].append(result);write(args.output,record)
        print(json.dumps({key:result[key]for key in ('radius','status','nodes','seconds')}),flush=True)
        if result['status']=='SAT_CANDIDATE':break


if __name__=='__main__':main()
