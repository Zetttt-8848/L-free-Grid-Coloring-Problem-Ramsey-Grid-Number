"""Check the rainbow lower bounds for triangles in small ambient squares."""
import argparse
import json
import lzma
from collections import namedtuple
from pathlib import Path
from tempfile import TemporaryDirectory

from verify_rectangle_lines import check
from verify_triangle_boundary import cost, orientations

HERE = Path(__file__).resolve().parent
Patch = namedtuple("Patch", "order cutoff side x y group cases stride", defaults=(1,))
PATCHES = (
    Patch(13, 11, 17, 5, 0, 126, 126),
    Patch(13, 11, 18, 0, 0, 21, 126),
    Patch(12, 7, 18, 3, 3, 30, 1578),
    Patch(12, 7, 18, 0, 0, 30, 1578),
    Patch(12, 7, 18, 7, 0, 30, 1578),
    Patch(12, 8, 18, 3, 3, 60, 11028),
    Patch(13, 11, 23, 0, 0, 21, 126, 2),
    Patch(13, 12, 18, 3, 3, 48, 2928),
    Patch(13, 12, 18, 6, 0, 48, 2928),
    Patch(13, 12, 18, 0, 0, 48, 2928),
)


def fits_checked_square(host, order, step, a, b, level, minimum=0):
    """Test the actual four edges of each candidate ambient square in the host square."""
    left, bottom = 1+a+b, b
    for patch in PATCHES[:level]:
        if order != patch.order or patch.cutoff+1 < minimum or step % patch.stride:
            continue
        unit = step//patch.stride
        gap = patch.side-1-(order-2)*patch.stride
        for x,y in ((patch.x,patch.y), (gap-patch.y,gap-patch.x)):
            x0, y0 = left-unit*x, bottom-unit*y
            last = (patch.side-1)*unit
            if 0 <= x0 and x0+last < host and 0 <= y0 and y0+last < host:
                return True
    return False


def square_formula(patch, words):
    side = patch.side
    clauses = []
    for v in range(side*side):
        colors = [1+3*v+c for c in range(3)]
        clauses.append(colors)
        clauses.extend([[-colors[i],-colors[j]] for i in range(3) for j in range(i)])
    for x in range(side):
        for y in range(side):
            for d in range(1,min(side-x,side-y)):
                triple = (x*side+y, (x+d)*side+y, (x+d)*side+y+d)
                clauses.extend([[-1-3*v-c for v in triple] for c in range(3)])
    slots = [((x-1)*patch.stride+patch.x)*side+y*patch.stride+patch.y for x in range(1,patch.order) for y in range(x)]
    flags = [3*side*side+1+i for i in range(len(words))]
    clauses.append(flags)
    for flag, word in zip(flags, words):
        clauses.extend([[-flag,1+3*v+digit-48] for v,digit in zip(slots,word)])
    header = f"p cnf {flags[-1]} {len(clauses)}\n"
    data = "".join(" ".join(map(str,row))+" 0\n" for row in clauses)
    return clauses, (header+data).encode("ascii")


def verify_group(checker, patch, words, cached):
    clauses, data = square_formula(patch, words)
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        cnf, raw, proof = root/"patch.cnf", root/"trace.drat", root/"proof.rup"
        cnf.write_bytes(data)
        if cached and cached.is_file():
            proof.write_bytes(lzma.decompress(cached.read_bytes()))
        else:
            from pysat.solvers import Solver
            with Solver(name="glucose4", bootstrap_with=clauses, with_proof=True) as solver:
                if solver.solve():
                    raise AssertionError("a listed triangle extends to this square")
                raw.write_bytes(("\n".join(solver.get_proof())+"\n").encode("ascii"))
            check(checker,cnf,raw,"-l",proof)
        check(checker,cnf,proof)
        if cached and not cached.exists():
            cached.write_bytes(lzma.compress(proof.read_bytes(),preset=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checker", type=Path, help="drat-trim executable")
    parser.add_argument("--cache", type=Path, help="save or read checked RUP proofs")
    parser.add_argument("--stride", type=int, choices=(1,2), help="check only patches with this triangle spacing")
    parser.add_argument("--cutoff", type=int, help="check only groups at this rainbow cutoff")
    args = parser.parse_args()
    catalogs = json.loads(lzma.decompress((HERE/"triangle_grid_catalogs.json.xz").read_bytes()))
    deep = lzma.decompress((HERE/"triangle_13_through_12.txt.xz").read_bytes()).decode("ascii").splitlines()
    catalogs["13/12"] = deep
    for patch in PATCHES:
        n,b,side,x,y,group,expected,stride = patch
        if (args.stride and stride!=args.stride) or (args.cutoff is not None and args.cutoff!=b):
            continue
        choices = [(int(k.split("/")[1]),v) for k,v in catalogs.items() if k.startswith(f"{n}/")]
        cutoff, words = max(choices)
        assert cutoff >= b
        forms = set()
        for word in words:
            encoded = word.encode("ascii")
            if cost(n,encoded) <= b:
                forms.update(orientations(n,encoded))
        ordered = sorted(forms)
        assert len(ordered)==expected
        folder = (f"square_patch_{n}_{b}_{side}_{x}_{y}_{group}" if stride==1 else
                  f"scale_patch_{n}_{b}_{side}_{x}_{y}_{stride}_{group}")
        cache = args.cache/folder if args.cache else None
        if cache:
            cache.mkdir(parents=True,exist_ok=True)
        for start in range(0,expected,group):
            verify_group(args.checker.resolve(),patch,ordered[start:start+group],
                         cache/f"{start}.rup.xz" if cache else None)
        print(f"Verified {expected} oriented T{n} colorings at offset ({x},{y}) in side {side} with spacing {stride}.",flush=True)


if __name__ == "__main__":
    main()
