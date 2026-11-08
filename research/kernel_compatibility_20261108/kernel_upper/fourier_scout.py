"""Exploratory Fourier relaxation; no floating status is a mathematical proof."""
import argparse
from bisect import bisect_right
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from scipy.optimize import linprog

# Occupied-position convention, from M25 Algorithm3; used only by the scout.
G = (0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,217,247,284,334,357,373,426,481,493,554,586)


def run(n, joint, samples, seconds):
    assert 2 <= n <= 480
    started = time.monotonic()
    ds = np.arange(1,n)
    caps = np.minimum(n-ds, 6*np.array([bisect_right(G,n-int(d))-1 for d in ds]))
    if joint:
        caps = np.minimum(caps, [138+min(6,max(0,n-int(d)-425)) for d in ds])
    angles = np.linspace(0,np.pi,samples)
    cosines = np.cos(angles[:,None]*ds[None,:])
    # q0=2n, qd=3Rd-(n-d); q0+2sum qd*cos(d theta) >=0.
    answer = linprog(np.zeros(n-1), A_ub=-3*cosines,
                     b_ub=n-cosines@(n-ds), bounds=list(zip(np.zeros(n-1),caps)),
                     method='highs', options={'time_limit':seconds})
    return {'n':n, 'joint_minimum_cap':joint, 'samples':samples,
            'solver_status':int(answer.status), 'message':answer.message,
            'elapsed_seconds':time.monotonic()-started,
            'relaxed_R':None if answer.x is None else answer.x.tolist(),
            'evidence_status':'UNDECIDED_FLOATING_SCOUT'}


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    records=[]
    for n,joint in ((464,False),(463,False),(462,False),(460,False),(464,True),(463,True)):
        item=run(n,joint,4097,20)
        records.append(item)
        print(json.dumps({k:v for k,v in item.items() if k!='relaxed_R'}),flush=True)
    args.output.write_text(json.dumps({'runs':records,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2)+'\n',encoding='utf-8',newline='\n')
