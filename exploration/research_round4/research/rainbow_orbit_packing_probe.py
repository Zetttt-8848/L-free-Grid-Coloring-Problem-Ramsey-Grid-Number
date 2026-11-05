"""Bounded discovery of disjoint rainbow sets using triangle symmetries."""
import itertools,json,threading,time
from pathlib import Path
from pysat.card import CardEnc
from pysat.solvers import Solver
root=Path(__file__).resolve().parent;n=10
cells=[(v,u) for v in range(1,n) for u in range(v)]
ix={(p,c):3*i+c+1 for i,p in enumerate(cells) for c in range(3)}
clauses=[];corners=[];flags=[];orbit={}
for p in cells:
    clauses.append([ix[p,c] for c in range(3)])
    clauses.extend([[-ix[p,a],-ix[p,b]] for a,b in itertools.combinations(range(3),2)])
for v,u in cells:
    for d in range(1,n-v):
        tr=((v,u),(v+d,u),(v+d,u+d));j=len(corners);corners.append(tr)
        f=3*len(cells)+j+1;flags.append(f)
        key=(d,tuple(sorted((u,v-u-1,n-1-v-d))))
        orbit.setdefault(key,[]).append(j)
        clauses.extend([[-ix[p,c] for p in tr] for c in range(3)])
        clauses.extend([[f]+[-ix[p,c] for p,c in zip(tr,cs)] for cs in itertools.permutations(range(3))])
clauses.append([ix[cells[0],0]])
top=flags[-1]
for key,jj in orbit.items():
    if len(jj)!=6:clauses.extend([[-flags[j]] for j in jj])
    else:
        card=CardEnc.atmost([flags[j] for j in jj],bound=1,top_id=top)
        clauses.extend(card.clauses);top=card.nv
used={(2,(1,2,3))};results=[];attempts=[];start_all=time.monotonic()
for group in range(1,5):
    answer=None
    for budget in range(1,7):
        remaining=45-(time.monotonic()-start_all)
        if remaining<=0:break
        extra=[[-flags[j]] for key in used for j in orbit[key]]
        card=CardEnc.atmost(flags,bound=budget,top_id=top)
        with Solver(name='g3',bootstrap_with=clauses+extra+card.clauses) as solver:
            timer=threading.Timer(min(3,remaining),solver.interrupt);timer.start();start=time.monotonic()
            ok=solver.solve_limited(expect_interrupt=True);timer.cancel()
            attempt=dict(group=group,budget=budget,status='literal coloring' if ok else 'raw negative' if ok is False else 'undecided',seconds=time.monotonic()-start)
            attempts.append(attempt);print(json.dumps(attempt),flush=True)
            if ok:
                model=set(solver.get_model());z={p:next(c for c in range(3) if ix[p,c] in model) for p in cells}
                rr=[j for j,tr in enumerate(corners) if len({z[p] for p in tr})==3]
                assert all(len({z[p] for p in tr})>1 for tr in corners)
                keys=[key for key,jj in orbit.items() for j in jj if j in rr]
                assert len(keys)==len(set(keys)) and all(len(orbit[key])==6 and key not in used for key in keys)
                answer=dict(rows=[''.join(str(z[v,u]) for u in range(v)) for v in range(1,n)],rainbow_orbits=keys,rainbows=[corners[j] for j in rr])
        if answer:break
    if not answer:break
    results.append(answer);used.update((d,tuple(b)) for d,b in answer['rainbow_orbits'])
    print(json.dumps(dict(successful_groups=len(results),packed_colorings_including_seed=6*(len(results)+1),used_orbits=len(used))),flush=True)
(root/'rainbow_orbit_packing_probe.json').write_text(json.dumps(dict(groups=results,attempts=attempts),indent=2),encoding='utf-8')
