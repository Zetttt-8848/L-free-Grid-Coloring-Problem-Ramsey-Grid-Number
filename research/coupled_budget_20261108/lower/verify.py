"""Standard-library independent checks of lifted cuts and saved full matrices."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PRIOR=ROOT/'research/boundary_extension_20261108/lower'


def require(ok,msg):
    if not ok:raise ValueError(msg)


def main():
    spec=importlib.util.spec_from_file_location('prior_certificate_verifier',PRIOR/'verify.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    paper=json.loads((PRIOR/'paper20.json').read_text(encoding='utf-8'))['rows']
    packed=json.loads((PRIOR/'packing_results.json').read_text(encoding='utf-8'))['placements']
    independent=set();nodes=0;cores=0
    for group in packed:
        ox,oy=group['offset']
        for core in group['cores']:
            support,n=module.check_core(paper,dict(core,cells=group['cells'],offset=group['offset']))
            nodes+=n;cores+=1
            corners=[[tuple(p) for p in rule['points']] for rule in core['core']]
            points={p for t in corners for p in t}
            for reflected in (0,1):
                raw={p:(-p[1],-p[0]) if reflected else p for p in points}
                mx=min(p[0] for p in raw.values());my=min(p[1] for p in raw.values())
                normal={p:(q[0]-mx,q[1]-my) for p,q in raw.items()}
                width=max(p[0] for p in normal.values())+1
                height=max(p[1] for p in normal.values())+1
                for sx in range(22-width):
                    for sy in range(22-height):
                        image={p:(q[0]+sx,q[1]+sy) for p,q in normal.items()}
                        require(len(set(image.values()))==len(points),'Map not injective')
                        for t in corners:
                            a,b,c=sorted(image[p] for p in t)
                            require(a[1]==b[1] and b[0]==c[0] and b[0]-a[0]==c[1]-b[1]>0,'Map changed L')
                        for color_map in itertools.permutations((0,1,2)):
                            clause=[]
                            for x,y in support:
                                u,v=image[(x,y)]
                                clause.append(-(3*(u*21+v)+color_map[paper[x-ox][y-oy]]+1))
                            independent.add(tuple(sorted(clause)))
    canonical=json.dumps([list(c) for c in sorted(independent)],separators=(',',':')).encode()
    digest=hashlib.sha256(canonical).hexdigest()
    catalog=json.loads((HERE/'cut_catalog.json').read_text(encoding='utf-8'))
    require(digest==catalog['cuts_sha256'],'Cut closure differs')
    require(len(independent)==catalog['unique_cut_count'],'Cut count differs')
    matrices=[]
    for file in sorted((HERE/'runs').glob('*.json')):
        run=json.loads(file.read_text(encoding='utf-8'))
        rows=run.get('grid')
        if rows is None:continue
        require(len(rows)==21 and all(len(r)==21 for r in rows),'Incomplete matrix')
        require(all(type(c) is int and 0<=c<3 for r in rows for c in r),'Invalid colors')
        violations=[];count=0
        for bendx in range(21):
            for bendy in range(21):
                for d in range(1,min(bendx,20-bendy)+1):
                    ps=[(bendx-d,bendy),(bendx,bendy),(bendx,bendy+d)];count+=1
                    if len({rows[x][y] for x,y in ps})==1:violations.append(ps)
        require(count==2870,'Corner coverage')
        if 'violations' in run:require(len(violations)==run['violations'],'Wrong objective')
        if run['status']=='SAT_CANDIDATE':require(not violations,'Invalid alleged SAT')
        matrices.append({'file':file.name,'monochromatic_L':len(violations),'violations':violations,
                         'sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
    result={'status':'PASS','base_cores':cores,'checked_base_tree_nodes':nodes,
        'unique_cuts':len(independent),'cuts_sha256':digest,'matrices':matrices,
        'scope':'Finite cut closure and complete saved candidates. A nonzero violation count is not a construction.',
        'inputs':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in [PRIOR/'verify.py',PRIOR/'paper20.json',PRIOR/'packing_results.json',HERE/'cut_catalog.json',Path(__file__)]}}
    (HERE/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'status':'PASS','cuts':len(independent),'matrices':matrices}))


if __name__=='__main__':main()
