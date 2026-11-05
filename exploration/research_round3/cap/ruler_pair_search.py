"""Literal two-ruler coupling search; SAT outputs must be checked separately."""
from pathlib import Path
from itertools import combinations
from threading import Timer
import json,time,hashlib
from pysat.solvers import Solver

OUT=Path(__file__).resolve().parent
RULERS={
23:[0,6,22,24,43,56,95,126,137,146,172,173,201,213,258,273,281,306,311,355,365,369,372],
24:[0,9,33,37,38,97,122,129,140,142,152,191,205,208,252,278,286,326,332,353,368,384,403,425],
}
for size,r in RULERS.items():
    assert len(r)==size and len(set(r))==size and r==sorted(r)
    diffs=[b-a for a,b in combinations(r,2)]
    assert len(set(diffs))==len(diffs)

def model_for(F,blue,green,strict=False,fiber_step=None):
    pts=[(x,y) for x in F for y in F if (x>y if strict else x>=y)]
    ids={p:i+1 for i,p in enumerate(pts)}
    cnf=[]; corners=[]
    fs=set(F)
    for x,y in pts:
        for z in F:
            d=z-x
            if d>0 and y+d in fs and (z,y+d) in ids:
                triple=((x,y),(z,y),(z,y+d))
                a,b,c=[ids[p] for p in triple]
                corners.append(triple);cnf.extend(([a,b,c],[-a,-b,-c]))
    for color,S in ((0,blue),(1,green)):
        for u in S:
            point=(u,u) if fiber_step is None else (u+fiber_step,u)
            assert point in ids
            cnf.append([ids[point] if color else -ids[point]])
    return pts,cnf,corners

def solve(pts,cnf,seconds):
    with Solver(name='g3',bootstrap_with=cnf,with_proof=True) as solver:
        timer=Timer(seconds,solver.interrupt); timer.start()
        t=time.monotonic()
        try: ans=solver.solve_limited(expect_interrupt=True)
        finally: timer.cancel()
        stats=solver.accum_stats();elapsed=time.monotonic()-t
        if ans is True:
            positive={v for v in solver.get_model() if v>0}
            return 'SAT_CANDIDATE', [[x,y,int(i+1 in positive)] for i,(x,y) in enumerate(pts)],stats,elapsed
        return ('INTERNAL_UNSAT_UNVERIFIED' if ans is False else 'UNDECIDED'),None,stats,elapsed

# Domain regressions: full weak triangle on{0} admits the prescribed color;
# the two diagonal endpoints at0,1 with equal color force the off-diagonal opposite.
for F,B,G in (([0],[0],[]),([0,1],[0,1],[])):
    pts,cnf,cs=model_for(F,B,G)
    status,witness,_,_=solve(pts,cnf,5)
    assert status=='SAT_CANDIDATE'
    colors={(x,y):c for x,y,c in witness}
    assert all(len({colors[p] for p in corner})>1 for corner in cs)

log=[];budget_start=time.monotonic();positive=None
for size,r in RULERS.items():
    for reflected in (False,True):
        rr=[r[-1]-x for x in reversed(r)] if reflected else r
        for shift in range(1,463-r[-1]):
            if time.monotonic()-budget_start>120 or positive:break
            blue=list(r);green=[x+shift for x in rr]
            if set(blue)&set(green):continue
            F=sorted(blue+green)
            pts,cnf,corners=model_for(F,blue,green)
            status,witness,stats,elapsed=solve(pts,cnf,5)
            row={'order':size,'reflected':reflected,'shift':shift,'marks':len(F),
                 'span':F[-1]-F[0],'variables':len(pts),'corners':len(corners),
                 'status':status,'stats':stats,'elapsed_seconds_telemetry':str(elapsed)}
            log.append(row);print(json.dumps(row),flush=True)
            if witness:
                positive={'scope':'two-color weak triangle on F; not a complete square',
                          'F':F,'blue':blue,'green':green,'points':witness}
                (OUT/'pair_triangle_candidate.json').write_text(json.dumps(positive,indent=2)+'\n')
        if positive or time.monotonic()-budget_start>120:break
    if positive or time.monotonic()-budget_start>120:break
(OUT/'pair_search_log.json').write_text(json.dumps({'rulers':RULERS,'attempts':log,'positive_candidate':bool(positive)},indent=2)+'\n')
if positive:
    A=sorted(set(positive['F'])|{x+1 for x in positive['F']})
    pts,cnf,corners=model_for(A,positive['blue'],positive['green'],strict=True,fiber_step=1)
    status,witness,stats,elapsed=solve(pts,cnf,5)
    result={'status':status,'A':A,'blue':positive['blue'],'green':positive['green'],
            'variables':len(pts),'corners':len(corners),'stats':stats,'elapsed_seconds_telemetry':str(elapsed)}
    if witness:result['points']=witness
    (OUT/'source_triangle_candidate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('points','A','blue','green')}),flush=True)
