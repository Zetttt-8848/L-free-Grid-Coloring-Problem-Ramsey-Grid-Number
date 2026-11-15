"""Independently verify color-membership repair obstructions for the 21-square seed."""
from pathlib import Path
import json
import lzma
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
CELLS = 441
SIDE = 21


def directed_triples():
    return [(x*SIDE+y,(x+d)*SIDE+y,(x+d)*SIDE+y+d)
            for d in range(1,SIDE) for x in range(SIDE-d) for y in range(SIDE-d)]


def two_colorable(vertices, triples):
    index = {v:i for i,v in enumerate(vertices)}
    partners = [[] for _ in vertices]
    masks = []
    for triple in triples:
        if all(v in index for v in triple):
            a,b,c = (index[v] for v in triple)
            masks.append((1<<a)|(1<<b)|(1<<c))
            partners[a].append((1<<b)|(1<<c))
            partners[b].append((1<<a)|(1<<c))
            partners[c].append((1<<a)|(1<<b))
    all_bits = (1<<len(vertices))-1

    def search(red,blue,red_queue,blue_queue):
        while red_queue or blue_queue:
            swap = not red_queue
            if swap:
                red,blue,red_queue,blue_queue = blue,red,blue_queue,red_queue
            bit = red_queue & -red_queue
            red_queue ^= bit
            if bit & blue:
                return False
            if not bit & red:
                red |= bit
                for pair in partners[bit.bit_length()-1]:
                    if pair & blue:
                        continue
                    available = pair & ~red
                    if not available:
                        return False
                    if available != pair:
                        blue_queue |= available
            if swap:
                red,blue,red_queue,blue_queue = blue,red,blue_queue,red_queue
        free = all_bits & ~(red|blue)
        if not free:
            return True
        weights = {}
        for mask in masks:
            if mask&red and mask&blue:
                continue
            rest = mask & free
            weight = 5 if mask & (red|blue) else 1
            while rest:
                bit = rest & -rest
                rest ^= bit
                weights[bit] = weights.get(bit,0)+weight
        if not weights:
            return True
        choice = max(weights,key=weights.get)
        return search(red,blue,choice,0) or search(red,blue,0,choice)

    first = max(range(len(vertices)),key=lambda i:len(partners[i]))
    return search(0,0,1<<first,0)


def main():
    if len(sys.argv)!=2:
        raise SystemExit("Usage: python verify_projected_repair.py ./verify_repair_master")
    checker = Path(sys.argv[1]).resolve()
    seed = HERE.parent/"coupled_budget_20261108"/"lower"/"runs"/"local71.json"
    rows = json.loads(seed.read_text())["grid"]
    if len(rows)!=SIDE or any(len(row)!=SIDE or not set(row)<={0,1,2} for row in rows):
        raise ValueError("incorrect seed")
    original = sum(rows,[])
    triples = directed_triples()
    bad = [t for t in triples if len({original[i] for i in t})==1]
    if bad!=[(300,363,366)] or len(triples)!=2870:
        raise ValueError("initial defect coordinates")
    groups = json.loads(lzma.decompress((HERE/"repair_21_cores.json.xz").read_bytes()))
    budget = 11
    expected = [1450,1668,821]
    with tempfile.TemporaryDirectory() as tmp:
        for c,cores in enumerate(groups):
            if len(cores)!=expected[c]:
                raise ValueError("core count")
            clauses = [[i+1 if original[i]==c else -(i+1) for i in triple] for triple in triples]
            for core in cores:
                if not core or sorted(set(core))!=core or core[0]<0 or core[-1]>=CELLS:
                    raise ValueError("bad geometric core")
                if two_colorable(core,triples):
                    raise ValueError("a purported three-color requirement is two-colorable")
                clauses.append([-(i+1) if original[i]==c else i+1 for i in core])
            filename = Path(tmp)/f"master{c}.txt"
            with filename.open("w",encoding="ascii") as handle:
                print(budget,len(clauses),file=handle)
                for clause in clauses:
                    print(len(clause),*clause,file=handle)
            result = subprocess.run([str(checker),str(filename)],capture_output=True,text=True)
            if result.returncode!=0 or not result.stdout.startswith("UNSAT budget 11,"):
                raise ValueError(result.stdout+result.stderr)
            print(f"Color {c}, {len(cores)} independently checked cores. {result.stdout.strip()}",flush=True)
    if len(groups)!=3:
        raise ValueError("missing color")
    print("Each color needs at least 12 changed memberships. The grid needs at least 18 cell changes.")


if __name__ == "__main__":
    main()
