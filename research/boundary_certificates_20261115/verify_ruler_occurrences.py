"""Check all normalized triples of occurrence starts of the optimal 24-mark ruler.

Usage: python verify_ruler_occurrences.py /path/to/drat-trim
The bundled traces prove that a proper binary strict source on the indicated
marks is impossible. Each trace is checked by the external checker in RUP mode.
"""
from hashlib import sha256
from itertools import combinations
import json
import lzma
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
RULER = (0,9,33,37,38,97,122,129,140,142,152,191,205,208,252,278,
         286,326,332,353,368,384,403,425)


def strict_source(marks):
    # Retain the archived y-major variable numbering, generate triples from
    # the coordinates of the left cell and the allowed positive step.
    cells = sorted(((x,y) for x in marks for y in marks if x>y),
                   key=lambda point:(point[1],point[0]))
    ids = {cell:j+1 for j,cell in enumerate(cells)}
    clauses = []
    for x,y in cells:
        for xp in marks:
            if xp<=x:
                continue
            last = (xp, y+xp-x)
            if last in ids:
                triple = (ids[x,y],ids[xp,y],ids[last])
                clauses.extend((triple, tuple(-v for v in triple)))
    clauses.append((1,))  # interchange of the two color names
    text = f"p cnf {len(cells)} {len(clauses)}\n"
    text += "".join(" ".join(map(str,c))+" 0\n" for c in clauses)
    return text


def checked(truth,message):
    if not truth:
        raise ValueError(message)


def main():
    if len(sys.argv)!=2:
        raise SystemExit("Usage: python verify_ruler_occurrences.py /path/to/drat-trim")
    checker = str(Path(sys.argv[1]).resolve())
    raw = lzma.decompress((HERE/"ruler_triple_proofs.json.xz").read_bytes())
    data = json.loads(raw)
    required = list(combinations(range(1,36),2))
    checked([(r[0],r[1]) for r in data]==required,"incomplete triple coverage")
    differences = {b-a for a,b in combinations(RULER,2)}
    checked(len(differences)==276 and set(range(1,36))<=differences,
            "ruler difference geometry")
    with tempfile.TemporaryDirectory() as directory:
        cnf = Path(directory)/"strict.cnf"
        proof = Path(directory)/"trace.rup"
        for a,b,marks,trace in data:
            ambient = {x+h for x in RULER for h in (0,a,b)}
            checked(len(marks)>=2 and sorted(set(marks))==marks and set(marks)<=ambient,
                    f"invalid mark set {a},{b}")
            cnf.write_text(strict_source(marks),encoding="ascii")
            proof.write_bytes(trace.encode("ascii"))
            proc = subprocess.run([checker,str(cnf),str(proof),"-U"],
                                  capture_output=True,text=True)
            checked(proc.returncode==0 and "s VERIFIED" in proc.stdout.splitlines(),
                    f"RUP verification failed at {a},{b}: {proc.stdout[-160:]}")
    print(f"Verified {len(required)} triples with positive normalized starts "
          f"up to 35. Payload SHA-256 {sha256(raw).hexdigest()}.")


if __name__=="__main__":
    main()
