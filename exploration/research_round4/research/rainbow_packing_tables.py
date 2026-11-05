"""Format the literal arrays and their F3 corner sums for the construction proof."""
import json
from pathlib import Path
root=Path(__file__).resolve().parent
rows=[['0','10','120','0002','01111','222210','0021102','01022111','200120122']]
rows += [a['rows'] for a in json.loads((root/'rainbow_orbit_packing_probe.json').read_text())['groups']]
out=['| row v | A | B | C | D | E |','|---|---|---|---|---|---|']
for v in range(1,10):out.append('| '+str(v)+' | '+' | '.join(z[v-1] for z in rows)+' |')
out+=['','| coloring | step d | corner-sum rows |','|---|---|---|']
zeros=[]
for label,rr in zip('ABCDE',rows):
    z={(v,u):int(rr[v-1][u]) for v in range(1,10) for u in range(v)}
    for d in range(1,9):
        chunks=[]
        for v in range(1,10-d):
            chars=[]
            for u in range(v):
                tr=((v,u),(v+d,u),(v+d,u+d)); cs=[z[p] for p in tr];s=sum(cs)%3
                chars.append(str(s))
                if s==0:zeros.append((label,v,u,d,''.join(map(str,cs)),(d,tuple(sorted((u,v-u-1,9-v-d))))))
            chunks.append(''.join(chars))
        out.append('| '+label+' | '+str(d)+' | '+' / '.join(chunks)+' |')
out+=['','| coloring | (v,u;d) | three labels | step and sorted base gaps |','|---|---|---|---|']
for label,v,u,d,cs,key in zeros:out.append(f'| {label} | ({v},{u};{d}) | {cs} | {key} |')
text='\n'.join(out)+'\n'
(root/'rainbow_packing_tables.md').write_text(text,encoding='utf-8')
print(text)
