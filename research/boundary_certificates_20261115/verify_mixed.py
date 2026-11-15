"""Rebuild and verify the fixed-word one-source-cell obstruction.

Usage: python verify_mixed.py /path/to/drat-trim
Python reconstructs the geometric CNF and checks the input digests.
The external checker accepts the supplied compact proof in RUP-only mode.
"""
from hashlib import sha256
from pathlib import Path
import lzma
import subprocess
import sys
import tempfile

WORD="122120100110100020212021121202210012"
HERE=Path(__file__).resolve().parent


def clauses(word):
    n=len(word)
    coords=[(x,y) for x in range(n) for y in range(x+1)]
    var={q:1+3*i for i,q in enumerate(coords)}
    cnf=[]
    for (x,y),v in var.items():
        cnf.extend([[v,v+1,v+2],[-v,-v-1],[-v-1,-v-2],[-v,-v-2]])
        if x==y:
            cnf.append([v+int(word[x])])
        elif word[x]==word[y]:
            cnf.append([-v-int(word[x])])
    for x,y in coords:
        for d in range(1,n-x):
            points=((x,y),(x+d,y),(x+d,y+d))
            if any(word[i]==word[j] for i,j in points):
                for c in range(3):
                    cnf.append([-var[p]-c for p in points])
    return 3*len(coords),cnf


def main():
    if len(sys.argv)!=2:
        raise SystemExit("Usage: python verify_mixed.py /path/to/drat-trim")
    dims,formula=clauses(WORD)
    cnf=(f"p cnf {dims} {len(formula)}\n"
         +''.join(' '.join(map(str,c))+' 0\n' for c in formula)).encode('ascii')
    proof=lzma.decompress((HERE/'mixed_461.rup.xz').read_bytes())
    if sha256(cnf).hexdigest()!='2a2ab39b7ba6df6993a456c536cad9207537f4106604c6e585cbb4754094f461' or sha256(proof).hexdigest()!='1f817af873c2e64d944780b2dea22becbd2f29a61706932ad977195416f26122':
        raise ValueError('certificate digest mismatch')
    with tempfile.TemporaryDirectory() as tmp:
        cn=Path(tmp)/'word.cnf'; pf=Path(tmp)/'word.rup'
        cn.write_bytes(cnf);pf.write_bytes(proof)
        run=subprocess.run([sys.argv[1],str(cn),str(pf),'-U'],
                           capture_output=True,text=True)
        if run.returncode!=0 or 's VERIFIED' not in run.stdout.splitlines():
            raise RuntimeError(run.stdout+run.stderr)
    print(f"Verified fixed-word refutation: {dims} variables, {len(formula)} clauses, "
          "36-letter triangle, at least one prescribed vertex per constraint.")


if __name__=='__main__':
    main()
