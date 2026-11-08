"""Conflict-specific repair of a complete, possibly improper 21-square."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import subprocess
import sys
from threading import Timer
import time
from pysat.solvers import Solver
from adaptive_repair import encode,write
from certified_cuts import generate


def worker(args):
    start=time.monotonic();rng=random.Random(args.seed)
    grid=json.loads(args.input.read_text(encoding='utf-8'))['grid']
    colors=sum(grid,[]);clauses,triples=encode(21)
    bad=[t for t in triples if len({colors[v] for v in t})==1]
    thaw={v for t in bad for v in t};cl,meta=generate();clauses.extend(cl)
    allcells=list(range(441));rng.shuffle(allcells);tie={v:i for i,v in enumerate(allcells)}
    counts=Counter();result={'status':'RUNNING','input_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest(),
        'seed':args.seed,'initial_violations':len(bad),'initial_thaw':sorted(thaw),'rounds':[],'grid':None,
        'method':'core-guided full-candidate repair with certified lifted cuts','per_call_wall_seconds':2,
        'nonexistence_certified':False,'cuts_sha256':meta['cuts_sha256'],
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    write(args.output,result)
    with Solver(name='g4',bootstrap_with=clauses) as sat:
        sat.set_phases([3*v+c+1 for v,c in enumerate(colors)])
        while time.monotonic()-start<args.seconds:
            frozen=[v for v in allcells if v not in thaw]
            sat.clear_interrupt();timer=Timer(2,sat.interrupt);timer.daemon=True
            tick=time.monotonic();timer.start()
            try:status=sat.solve_limited(assumptions=[3*v+colors[v]+1 for v in frozen],expect_interrupt=True)
            finally:timer.cancel();timer.join()
            duration=time.monotonic()-tick
            row={'round':len(result['rounds']),'thawed':len(thaw),'status':'SAT' if status else 'UNSAT_UNCERTIFIED' if status is False else 'UNKNOWN',
                 'seconds':duration,'elapsed':time.monotonic()-start,'core':[]}
            if status is True:
                pos=set(sat.get_model());result['grid']=[[next(c for c in range(3) if 3*(x*21+y)+c+1 in pos) for y in range(21)]for x in range(21)]
                result['status']='SAT_CANDIDATE';result['rounds'].append(row);break
            if status is False:
                core={(lit-1)//3 for lit in sat.get_core() or []};row['core']=sorted(core)
                if not core:result['status']='UNSAT_UNCERTIFIED';result['rounds'].append(row);break
                counts.update(core)
                release=sorted(core,key=lambda v:(-counts[v],tie[v]))[:2]
            else:
                release=sorted(frozen,key=lambda v:(-counts[v],tie[v]))[:10]
            thaw.update(release);row['released']=release;result['rounds'].append(row)
            result['elapsed_seconds']=time.monotonic()-start;write(args.output,result)
        result['stats']=sat.accum_stats()
    if result['status']=='RUNNING':result['status']='UNDECIDED_BUDGET'
    result['elapsed_seconds']=time.monotonic()-start;write(args.output,result)


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--seconds',type=float,default=90);p.add_argument('--seed',type=int,default=91);p.add_argument('--worker',action='store_true')
    args=p.parse_args()
    if args.worker:worker(args);return
    if args.output.exists():raise ValueError('Fresh output required')
    cmd=[sys.executable,str(Path(__file__).resolve()),'--worker','--input',str(args.input),'--output',str(args.output),'--seconds',str(args.seconds),'--seed',str(args.seed)]
    tick=time.monotonic()
    try:
        r=subprocess.run(cmd,capture_output=True,text=True,timeout=args.seconds+3)
        state='completed' if r.returncode==0 else 'failed';stderr=r.stderr
    except subprocess.TimeoutExpired:state='external_timeout';stderr=''
    result=json.loads(args.output.read_text(encoding='utf-8')) if args.output.exists() else {'status':'NO_CHECKPOINT'}
    if state=='external_timeout':result['status']='UNDECIDED_EXTERNAL_TIMEOUT'
    result['runner']={'status':state,'wall_seconds':time.monotonic()-tick,'hard_cap':args.seconds+3,'stderr':stderr}
    write(args.output,result);print(json.dumps({'status':result['status'],'rounds':len(result.get('rounds',[]))}))


if __name__=='__main__':main()
