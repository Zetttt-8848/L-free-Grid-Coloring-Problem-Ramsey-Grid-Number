"""Check the literal rectangle and classify fixed-rectangle extensions by one row."""
from itertools import combinations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def extend_at_end(rows, holes):
    height, width = len(rows), len(rows[0])
    active = set(range(width)) - set(holes)
    # An equal pair at y<z in the new row is forbidden in precisely one color.
    adjacent = [[[] for _ in range(3)] for _ in range(width)]
    for y,z in combinations(sorted(active),2):
        d = z-y
        if d<=height:
            c = int(rows[height-d][y])
            adjacent[y][c].append(z)
            adjacent[z][c].append(y)

    def visit(domains):
        if not domains:
            return {}
        y = min(domains, key=lambda i:(domains[i].bit_count(), -sum(map(len,adjacent[i]))))
        mask = domains[y]
        for c in range(3):
            if not mask & (1<<c):
                continue
            remaining = domains.copy()
            del remaining[y]
            for z in adjacent[y][c]:
                if z in remaining:
                    remaining[z] &= ~(1<<c)
                    if not remaining[z]:
                        break
            else:
                result = visit(remaining)
                if result is not None:
                    result[y]=c
                    return result
        return None

    return visit({i:7 for i in active})


def check_geometry(rows):
    height,width = len(rows),len(rows[0])
    checked = 0
    for x in range(height):
        for y in range(width):
            for d in range(1,min(height-x,width-y)):
                a,b,c = rows[x][y], rows[x+d][y], rows[x+d][y+d]
                if a==b==c and a!=".":
                    raise ValueError(f"monochromatic L at {(x,y,d)}")
                checked += 1
    return checked


def main():
    rows = json.loads((HERE/"rectangle_20_21.json").read_text())
    if len(rows)!=20 or any(len(row)!=21 or not set(row)<=set("012") for row in rows):
        raise ValueError("literal rectangle domain")
    if check_geometry(rows)!=2660:
        raise ValueError("geometry count")
    first = []
    for y in range(21):
        forbidden = {rows[d-1][y] for d in range(1,21-y) if rows[d-1][y]==rows[d-1][y+d]}
        if len(forbidden)==3:
            first.append(y)
    if first!=[0,1,2,4,5,7,8,9,11,13]:
        raise ValueError("blocked positions in the preceding row")
    counts = []
    for k in range(5):
        count = 0
        for holes in combinations(range(21),k):
            colors = extend_at_end(rows,holes)
            if colors is not None:
                partial = "".join(str(colors[i]) if i in colors else "." for i in range(21))
                check_geometry(rows+[partial])
                count += 1
        counts.append(count)
    if counts!=[0,0,0,0,16]:
        raise ValueError(f"counts of feasible hole sets: {counts}")
    print("20 by 21, 2,660 directed Ls checked. Ten forced holes before. "
          "After the rectangle, four holes suffice in exactly 16 position sets.")


if __name__ == "__main__":
    main()
