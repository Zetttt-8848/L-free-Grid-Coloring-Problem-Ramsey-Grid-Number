"""Independent exhaustive support coverage, triangle witness, and RUP audit."""
from pathlib import Path
import argparse,collections,hashlib,json,platform,time
ROOT=Path(__file__).resolve().parent

def geometry(marks):
    points=sorted((u,v) for u in marks for v in marks if u>v)
    # Certificate uses y-major order; verify geometry in a different enumeration.
    certorder=sorted(points,key=lambda p:(p[1],p[0]));idmap={p:i+1 for i,p in enumerate(certorder)};edges=[]
    for x,y in points:
        for d in range(1,max(marks,default=0)-x+1):
            if (x+d,y) in idmap and (x+d,y+d) in idmap:edges.append([idmap[x,y],idmap[x+d,y],idmap[x+d,y+d]])
    return points,edges

def unit_conflict(formula,assumed,n):
    values=[None]*(n+1);pending=collections.deque(assumed)
    while True:
        while pending:
            lit=pending.popleft();v=abs(lit);b=lit>0
            if values[v] is not None and values[v]!=b:return True
            values[v]=b
        for clause in formula:
            true=False;unfixed=[]
            for lit in clause:
                val=values[abs(lit)]
                if val is None:unfixed.append(lit)
                elif val==(lit>0):true=True;break
            if true:continue
            if not unfixed:return True
            if len(unfixed)==1:pending.append(unfixed[0])
        if not pending:return False

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--width',type=int,default=13);args=pa.parse_args();path=ROOT/f'window{args.width}.json';obj=json.loads(path.read_text());w=obj['width'];assert w==args.width;start=time.time();proofs=0
    for entry in obj['minimal_bad']:
        marks=[i for i in range(w) if entry['mask']>>i&1];assert marks==entry['marks'];points,edges=geometry(marks);n=len(points);formula=[]
        for e in edges:formula.extend([e,[-t for t in e]])
        if n:formula.append([1])
        # The pin removes only interchange of the two color names.
        for clause in entry['proof']:
            assert all(type(lit) is int and 0<abs(lit)<=n for lit in clause)
            assert unit_conflict(formula,[-lit for lit in clause],n),('non-RUP',entry['mask'],proofs)
            formula.append(clause);proofs+=1
        assert entry['proof'] and entry['proof'][-1]==[]
        cnf=ROOT/f"window{w}/bad_{entry['mask']}.cnf";rup=ROOT/f"window{w}/bad_{entry['mask']}.rup"
        parsed=[]
        for line in cnf.read_text().splitlines():
            if line.startswith('p'):continue
            vals=list(map(int,line.split()));assert vals[-1]==0;parsed.append(tuple(vals[:-1]))
        base=[tuple(e) for edge in edges for e in (edge,[-t for t in edge])]+([(1,)] if n else [])
        assert collections.Counter(parsed)==collections.Counter(base)
        assert [list(map(int,line.split()[:-1])) for line in rup.read_text().splitlines()]==entry['proof']
    for entry in obj['maximal_good']:
        marks=[i for i in range(w) if entry['mask']>>i&1];assert marks==entry['marks'];points,edges=geometry(marks);colors=entry['colors'];assert len(colors)==len(points) and all(type(c) is int and c in (0,1) for c in colors)
        assert all(len({colors[v-1] for v in edge})==2 for edge in edges)
    badmasks=[e['mask'] for e in obj['minimal_bad']];goodmasks=[e['mask'] for e in obj['maximal_good']];status=[]
    for mask in range(1<<w):
        bad=any(mask&b==b for b in badmasks);good=any(mask&g==mask for g in goodmasks);assert bad!=good,('coverage gap or contradiction',mask);status.append(good)
    assert len(set(badmasks))==len(badmasks) and len(set(goodmasks))==len(goodmasks)
    assert all(all(status[b^(1<<i)] for i in range(w) if b>>i&1) for b in badmasks)
    assert all(all(not status[g|(1<<i)] for i in range(w) if not g>>i&1) for g in goodmasks)
    assert status==obj['status'];assert sum(status)==obj['good_count'];assert sum(not s for s in status)==obj['bad_count'];assert len(status)==obj['queried']+obj['pruned_by_bad_subset']
    caps={k:max(m.bit_count() for m in range(1<<k) if status[m]) for k in range(1,w+1)};assert caps=={int(k):v for k,v in obj['capacities'].items()}
    spans={s:min(k-1 for k,h in caps.items() if h>=s) for s in range(1,max(caps.values())+1)}
    out=dict(verdict='PASS',width=w,raw_masks_checked=1<<w,good_count=sum(status),bad_count=sum(not s for s in status),minimal_bad_proofs_checked=len(badmasks),rup_additions_checked=proofs,maximal_good_colorings_checked=len(goodmasks),capacities=caps,minimum_possible_span_by_size=spans,source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),runtime_seconds=time.time()-start,scope='Complete labeled support-mask classification in width13; no orbit count or wider-window exhaustion claimed')
    (ROOT/f'window{w}.check.json').write_text(json.dumps(out,indent=2)+'\n')
    log=[dict(kind='contract',universe='Every labeled subset of integer positions0 through W-1',width=w,raw_space_formula='2^W',raw_space_size=1<<w,symmetry='none'),dict(kind='coverage',method='All integer masks0 through2^W-1 once; each contains a RUP-certified minimal bad support or lies inside a fully colored maximal good support, exclusively'),dict(kind='software',python=platform.python_version()),dict(kind='result',**out)]
    (ROOT/f'window{w}.verified.log').write_text(''.join(json.dumps(row)+'\n' for row in log)+'RUN COMPLETE\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
