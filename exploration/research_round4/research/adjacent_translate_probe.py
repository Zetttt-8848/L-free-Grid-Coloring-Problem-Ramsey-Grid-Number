"""Bounded discovery for one-step translations; no negative result is a theorem."""
import itertools,json,threading,time
from pathlib import Path
from pysat.solvers import Solver

root=Path(__file__).resolve().parent
rulers=json.loads((root.parent.parent/'research_round3/cap/pair_search_log.json').read_text(encoding='utf-8'))['rulers']
results=[]
for order,base in rulers.items():
    adjacent=[(a,b) for a,b in itertools.combinations(base,2) if b-a==1]
    for removed in adjacent[0]:
        B=[a for a in base if a!=removed];C=[a+1 for a in B];S=sorted(B+C);ss=set(S)
        assert len(ss)==len(S)
        cells=[(v,u) for v in S for u in S if u<=v];ix={q:i+1 for i,q in enumerate(cells)}
        corners=[]
        for d in sorted({v-u for u,v in itertools.combinations(S,2)}):
            starts=[u for u in S if u+d in ss]
            for y in starts:
                for x in starts:
                    if y<=x:corners.append(((x,y),(x+d,y),(x+d,y+d)))
        clauses=[]
        for tr in corners:
            ids=[ix[q] for q in tr];clauses.extend([ids,[-a for a in ids]])
        pins={**{(b,b):0 for b in B},**{(c,c):1 for c in C}}
        clauses.extend([[ix[q] if v else -ix[q]] for q,v in pins.items()])
        colors=dict(pins);steps=[];conflict=None
        while True:
            changed=False
            for tr in corners:
                known=[(q,colors[q]) for q in tr if q in colors]
                if len(known)==3 and len({v for q,v in known})==1:
                    conflict=tr;break
                if len(known)==2 and known[0][1]==known[1][1]:
                    q=next(q for q in tr if q not in colors);value=1-known[0][1]
                    colors[q]=value;steps.append(dict(point=q,color=value,corner=tr));changed=True
            if conflict or not changed:break
        out=dict(order=order,removed=removed,B=B,C=C,span=max(S)-min(S),source_marks=len(S))
        if conflict:
            out.update(status='forced-color conflict',steps=steps,conflict=conflict)
        else:
            with Solver(name='g3',bootstrap_with=clauses) as solver:
                timer=threading.Timer(10,solver.interrupt);timer.start();start=time.monotonic()
                ok=solver.solve_limited(expect_interrupt=True);timer.cancel()
                out.update(status='literal coloring' if ok else 'raw negative' if ok is False else 'undecided',seconds=time.monotonic()-start)
                if ok:
                    vals={abs(x):int(x>0) for x in solver.get_model()};colors={q:vals[ix[q]] for q in cells}
                    assert all(len({colors[q] for q in tr})>1 for tr in corners)
                    out['colors']=[[x,y,v] for (x,y),v in colors.items()]
        results.append(out)
        print(json.dumps({k:v for k,v in out.items() if k not in ('steps','colors','B','C')}),flush=True)
(root/'adjacent_translate_probe.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
