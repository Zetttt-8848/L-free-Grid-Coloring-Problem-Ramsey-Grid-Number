"""Lift certified finite boundary obstructions to redundant full-square cuts.

All translations, color permutations and antidiagonal reflections preserve the
specified directed positive-step L. Proof validity is inherited only from the
stored independently checked core certificates, not from a fresh raw UNSAT.
"""
import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import platform
import subprocess
import sys
import time
import pysat
from pysat.solvers import Solver
from adaptive_repair import encode,write,PRIOR,HERE


def generate(n=21):
    paper=json.loads((PRIOR/'paper20.json').read_text(encoding='utf-8'))['rows']
    pack=json.loads((PRIOR/'packing_results.json').read_text(encoding='utf-8'))
    cuts=set(); orbit_counts=[]
    for placement in pack['placements']:
        ox,oy=placement['offset']
        for index,core in enumerate(placement['cores']):
            support=[(x,y,paper[x-ox][y-oy]) for x,y in core['support']]
            geometry={tuple(p) for rule in core['core'] for p in rule['points']}
            start=len(cuts); candidates=0
            for reflect in (False,True):
                transform=(lambda x,y:(-y,-x)) if reflect else (lambda x,y:(x,y))
                pts=[transform(x,y) for x,y in geometry]
                lowx=min(x for x,y in pts);highx=max(x for x,y in pts)
                lowy=min(y for x,y in pts);highy=max(y for x,y in pts)
                for dx in range(-lowx,n-highx):
                    for dy in range(-lowy,n-highy):
                        for perm in itertools.permutations(range(3)):
                            clause=[]
                            for x,y,c in support:
                                u,v=transform(x,y);u+=dx;v+=dy
                                clause.append(-(3*(u*n+v)+perm[c]+1))
                            cuts.add(tuple(sorted(clause)));candidates+=1
            orbit_counts.append({'offset':[ox,oy],'core':index,'generated_candidates':candidates,'new_unique':len(cuts)-start})
    clauses=[list(t) for t in sorted(cuts)]
    canonical=json.dumps(clauses,separators=(',',':')).encode()
    report={'n':n,'base_cores':len(orbit_counts),'unique_cut_count':len(clauses),
        'literal_count':sum(map(len,clauses)),'length_distribution':dict(Counter(map(len,clauses))),
        'cuts_sha256':hashlib.sha256(canonical).hexdigest(),'orbits':orbit_counts,
        'source_inputs':{name:hashlib.sha256((PRIOR/name).read_bytes()).hexdigest() for name in ('paper20.json','packing_results.json')},
        'claim':'Every generated clause is redundant for the complete directed L-free 3-color square formula, by the stored core proof and a shape-preserving injective map.'}
    return clauses,report


def worker(args):
    begin=time.monotonic(); clauses,triples=encode(21)
    cuts,metadata=generate()
    if args.cuts:clauses.extend(cuts)
    paper=json.loads((PRIOR/'paper20.json').read_text(encoding='utf-8'))['rows']
    record={'status':'RUNNING','cut_mode':args.cuts,'budget_seconds':args.seconds,
        'base_clauses':10374,'added_clauses':len(cuts) if args.cuts else 0,'cut_metadata':metadata,
        'rounds':[],'grid':None,'software':{'python':platform.python_version(),'python_sat':pysat.__version__,'solver':'Glucose4'},
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'nonexistence_certified':False}
    write(args.output,record)
    with Solver(name='g4',bootstrap_with=clauses) as sat:
        phases=[3*(x*21+y)+paper[x][y-1]+1 for x in range(20) for y in range(1,21)]
        sat.set_phases(phases)
        while time.monotonic()-begin<args.seconds:
            sat.conf_budget(30000)
            tick=time.monotonic();status=sat.solve_limited()
            record['rounds'].append({'elapsed':time.monotonic()-begin,'seconds':time.monotonic()-tick,
                                    'status':'SAT' if status else 'UNSAT_UNCERTIFIED' if status is False else 'UNKNOWN'})
            if status is True:
                pos=set(sat.get_model());record['grid']=[[next(c for c in range(3) if 3*(x*21+y)+c+1 in pos) for y in range(21)] for x in range(21)]
                record['status']='SAT_CANDIDATE';break
            if status is False:record['status']='UNSAT_UNCERTIFIED';break
            record['elapsed_seconds']=time.monotonic()-begin;write(args.output,record)
        record['stats']=sat.accum_stats()
    if record['status']=='RUNNING':record['status']='UNDECIDED_BUDGET'
    record['elapsed_seconds']=time.monotonic()-begin;write(args.output,record)


def main():
    p=argparse.ArgumentParser();p.add_argument('--worker',action='store_true');p.add_argument('--cuts',action='store_true')
    p.add_argument('--catalog',action='store_true');p.add_argument('--seconds',type=float,default=120)
    p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    if args.catalog:
        clauses,report=generate();write(args.output,report);print(json.dumps({k:v for k,v in report.items() if k!='orbits'}));return
    if args.worker:worker(args);return
    if args.output.exists():raise ValueError('Fresh output required')
    cmd=[sys.executable,str(Path(__file__).resolve()),'--worker','--seconds',str(args.seconds),'--output',str(args.output)]
    if args.cuts:cmd.append('--cuts')
    begin=time.monotonic()
    try:
        proc=subprocess.run(cmd,capture_output=True,text=True,timeout=args.seconds+3)
        status='completed' if proc.returncode==0 else 'failed';error=proc.stderr
    except subprocess.TimeoutExpired:
        status='external_timeout';error=''
    record=json.loads(args.output.read_text(encoding='utf-8')) if args.output.exists() else {'status':'NO_CHECKPOINT'}
    if status=='external_timeout':record['status']='UNDECIDED_EXTERNAL_TIMEOUT'
    record['runner']={'status':status,'seconds':time.monotonic()-begin,'hard_timeout_seconds':args.seconds+3,'error':error}
    write(args.output,record);print(json.dumps({'status':record['status'],'cuts':args.cuts,'runner':status}))


if __name__=='__main__':main()
