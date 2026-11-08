"""Standalone certificate checker for bounded-Hamming nonrepairability.

No solver, search implementation, or local-search code is imported. The proof
stream chooses a violated geometric L at every node; branching is reconstructed
by the checker and must cover every still-uncommitted endpoint and both colors.
"""
import base64
import hashlib
import json
from pathlib import Path
import struct
import time
import zlib

HERE=Path(__file__).resolve().parent


def require(ok,message):
    if not ok:raise ValueError(message)


def decode_edge(index,n):
    require(type(index) is int and 0<=index<sum(s*s for s in range(1,n)),'Bad edge id')
    for d in range(1,n):
        side=n-d
        if index<side*side:
            x,y=divmod(index,side)
            return (x*n+y,(x+d)*n+y,(x+d)*n+y+d)
        index-=side*side
    raise ValueError('No edge')


def check(record):
    rows=record['input_grid'];n=len(rows)
    require(n==21 and all(len(r)==n for r in rows),'Incomplete21 input')
    require(all(type(c) is int and c in (0,1,2) for r in rows for c in r),'Bad colors')
    initial=sum(rows,[]);outputs=[]
    edges=[decode_edge(i,n) for i in range(2870)]
    for run in record['runs']:
        cert=run.get('certificate')
        if cert is None:continue
        require(run['status']=='EXHAUSTED_RADIUS','Certificate with wrong status')
        raw=zlib.decompress(base64.b64decode(cert['data'],validate=True))
        require(hashlib.sha256(raw).hexdigest()==cert['raw_sha256'],'Proof hash')
        require(len(raw)==2*cert['nodes']==2*run['nodes'],'Proof size')
        codes=[x[0]for x in struct.iter_unpack('<H',raw)]
        pos=0;values=initial[:];used=set();k=run['radius'];tick=time.monotonic()

        def visit():
            nonlocal pos
            require(pos<len(codes),'Missing proof node')
            e=codes[pos];pos+=1
            require(e<len(edges),'Invalid edge index')
            t=edges[e]
            require(len({values[v]for v in t})==1,'Chosen corner is not violated')
            eligible=[v for v in t if v not in used]
            if not eligible or len(used)==k:return
            require(len(used)<k,'Radius exceeded')
            for v in eligible:
                used.add(v)
                for color in range(3):
                    if color==initial[v]:continue
                    values[v]=color;visit()
                values[v]=initial[v];used.remove(v)

        visit();require(pos==len(codes),'Unused proof nodes')
        outputs.append({'radius':k,'status':'CERTIFIED_NO_REPAIR','nodes':pos,'seconds':time.monotonic()-tick})
    return outputs


def main():
    path=HERE/'defect_certified.json';data=json.loads(path.read_text(encoding='utf-8'))
    candidate=HERE/'runs/local71.json'
    require(data['input_sha256']==hashlib.sha256(candidate.read_bytes()).hexdigest(),'Candidate hash differs')
    require(data['input_grid']==json.loads(candidate.read_text(encoding='utf-8'))['grid'],'Candidate matrix differs')
    checked=check(data)
    require([r['radius'] for r in checked]==list(range(1,11)),'Missing expected radius certificate')
    result={'status':'PASS','checks':checked,'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'No proper21-square exists within the listed Hamming radii of this fixed complete improper candidate; no general21 impossibility.'}
    (HERE/'defect_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(result))


if __name__=='__main__':main()
