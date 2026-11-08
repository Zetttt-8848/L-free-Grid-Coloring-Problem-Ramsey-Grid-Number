"""Bounded full-square SAT discovery with support-aware interior thawing.

This script never certifies an UNSAT result. Only an explicit full matrix can
change the lower bound, after separate geometric verification.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import platform
import random
import subprocess
import sys
import time
import pysat
from pysat.solvers import Solver

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PRIOR=ROOT/'research/boundary_extension_20261108/lower'


def write(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix('.tmp')
    tmp.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
    tmp.replace(path)


def encode(n):
    clauses=[]
    for v in range(n*n):
        ids=[3*v+c+1 for c in range(3)]
        clauses.append(ids)
        clauses.extend([[-ids[a],-ids[b]] for a in range(3) for b in range(a+1,3)])
    triples=[]
    for d in range(1,n):
        for x in range(n-d):
            for y in range(n-d):
                t=[x*n+y,(x+d)*n+y,(x+d)*n+y+d]
                triples.append(t)
                clauses.extend([[-(3*v+c+1) for v in t] for c in range(3)])
    return clauses,triples


def worker(args):
    start=time.monotonic(); rng=random.Random(args.seed)
    paper_path=PRIOR/'paper20.json'; packing_path=PRIOR/'packing_results.json'
    paper=json.loads(paper_path.read_text(encoding='utf-8'))['rows']
    offset=tuple(map(int,args.offset.split(','))); ox,oy=offset
    n=21; old={(x+ox)*n+y+oy:paper[x][y] for x in range(20) for y in range(20)}
    clauses,triples=encode(n)
    geometry=Counter(v for t in triples if any(v not in old for v in t) for v in t if v in old)
    packed=json.loads(packing_path.read_text(encoding='utf-8'))['placements']
    record=next(p for p in packed if tuple(p['offset'])==offset)
    supports=[{x*n+y for x,y in c['support']} for c in record['cores']]
    order=list(old); rng.shuffle(order); tie={v:i for i,v in enumerate(order)}
    thaw=set()
    if args.method=='guided':
        pending=supports[:]
        while pending:
            counts=Counter(v for s in pending for v in s)
            v=max(counts,key=lambda v:(counts[v],geometry[v],-tie[v]))
            thaw.add(v); pending=[s for s in pending if v not in s]
    priority=sorted(old,key=lambda v:(-geometry[v],tie[v])) if args.method=='guided' else order
    for v in priority:
        if len(thaw)>=32: break
        thaw.add(v)
    grid=[[old.get(x*n+y,rng.randrange(3)) for y in range(n)] for x in range(n)]
    result={'status':'RUNNING','method':args.method,'seed':args.seed,'offset':offset,
        'seconds_budget':args.seconds,'initial_thaw':sorted(thaw),'known_supports_hit':sum(bool(thaw&s) for s in supports),
        'known_supports':len(supports),'n':n,'k':3,'variables':1323,'clauses':len(clauses),'corners':len(triples),
        'rounds':[],'grid':None,'nonexistence_certified':False,
        'inputs':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (paper_path,packing_path)},
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'software':{'python':platform.python_version(),'python_sat':pysat.__version__,'solver':'Glucose4'},
        'claim':'Discovery only; learned cores guide thawing and do not establish nonexistence.'}
    write(args.output,result)
    core_counts=Counter()
    with Solver(name='g4',bootstrap_with=clauses) as sat:
        sat.set_phases([3*(x*n+y)+grid[x][y]+1 for x in range(n) for y in range(n)])
        while time.monotonic()-start<args.seconds:
            frozen=[v for v in old if v not in thaw]
            assumptions=[3*v+old[v]+1 for v in frozen]
            sat.conf_budget(15000)
            tick=time.monotonic(); status=sat.solve_limited(assumptions=assumptions)
            duration=time.monotonic()-tick
            row={'round':len(result['rounds']),'thawed':len(thaw),'frozen':len(frozen),
                 'status':'SAT' if status else 'UNSAT_UNCERTIFIED' if status is False else 'UNKNOWN',
                 'seconds':duration,'elapsed':time.monotonic()-start,'core_old_cells':[]}
            if status is True:
                positive=set(sat.get_model())
                result['grid']=[[next(c for c in range(3) if 3*(x*n+y)+c+1 in positive) for y in range(n)] for x in range(n)]
                result['status']='SAT_CANDIDATE'; result['rounds'].append(row); break
            if status is False:
                core=sat.get_core() or []
                if not core:
                    result['status']='UNSAT_UNCERTIFIED'; result['rounds'].append(row); break
                eligible={(lit-1)//3 for lit in core}
                row['core_old_cells']=sorted(eligible)
                core_counts.update(eligible)
                if args.method=='guided':
                    selected=sorted(eligible,key=lambda v:(-core_counts[v],-geometry[v],tie[v]))[:4]
                else:
                    selected=rng.sample(frozen,min(4,len(frozen)))
            else:
                if args.method=='guided':
                    selected=sorted(frozen,key=lambda v:(-core_counts[v],-geometry[v],tie[v]))[:12]
                else:
                    selected=rng.sample(frozen,min(12,len(frozen)))
            thaw.update(selected); row['released']=selected
            result['rounds'].append(row)
            result['elapsed_seconds']=time.monotonic()-start
            write(args.output,result)
        result['stats']=sat.accum_stats()
    if result['status']=='RUNNING': result['status']='UNDECIDED_BUDGET'
    result['elapsed_seconds']=time.monotonic()-start
    result['final_thaw']=sorted(thaw)
    write(args.output,result)


def main():
    p=argparse.ArgumentParser(); p.add_argument('--worker',action='store_true')
    p.add_argument('--method',choices=['guided','random'],default='guided')
    p.add_argument('--seed',type=int,default=17);p.add_argument('--offset',default='0,1')
    p.add_argument('--seconds',type=float,default=60);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    if args.worker: worker(args); return
    if args.output.exists(): raise ValueError('Output must be fresh')
    command=[sys.executable,str(Path(__file__).resolve()),'--worker','--method',args.method,
        '--seed',str(args.seed),'--offset',args.offset,'--seconds',str(args.seconds),'--output',str(args.output)]
    tick=time.monotonic()
    try:
        proc=subprocess.run(command,timeout=args.seconds+3,capture_output=True,text=True)
        termination='completed' if proc.returncode==0 else 'failed'; stdout,stderr=proc.stdout,proc.stderr
    except subprocess.TimeoutExpired as exc:
        termination='external_timeout';stdout=exc.stdout or '';stderr=exc.stderr or ''
    data=json.loads(args.output.read_text(encoding='utf-8')) if args.output.exists() else {'status':'NO_CHECKPOINT'}
    if termination=='external_timeout':data['status']='UNDECIDED_EXTERNAL_TIMEOUT'
    data['runner']={'termination':termination,'wall_seconds':time.monotonic()-tick,'hard_timeout':args.seconds+3,
        'stdout':str(stdout),'stderr':str(stderr),'scope':'Single worker process; no solver descendants.'}
    write(args.output,data)
    print(json.dumps({k:data.get(k) for k in ('status','method','seed','offset','elapsed_seconds')}))


if __name__=='__main__': main()
