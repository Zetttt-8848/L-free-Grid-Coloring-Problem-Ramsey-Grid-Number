"""Check literal triangle colorings and conditional weighted embedding inequalities."""
import json
from math import comb
from pathlib import Path

def main():
    root=Path(__file__).resolve().parent
    examples=json.loads((root/"triangle_literal_examples.json").read_text())
    for order,rows in examples.items():
        n=int(order)
        assert len(rows)==n-1 and all(len(row)==i for i,row in enumerate(rows,1))
        assert set("".join(rows))==set("012")
        counts=[0,0,0,0]
        for x in range(1,n):
            for y in range(x):
                for d in range(1,n-x):
                    colors={rows[x-1][y],rows[x+d-1][y],rows[x+d-1][y+d]}
                    counts[len(colors)]+=1
        assert sum(counts)==comb(n,3) and not counts[1]
        assert counts[3]=={13:11,14:17}[n]
        print(f"T_{n}: {comb(n,3)} corners, zero monochromatic, {counts[3]} rainbow.")
    cases=json.loads((root/"weighted_rainbow_routes.json").read_text())
    for row in cases:
        n,m,k=row["host"],row["marks"],row["assumed_minimum"]
        weights=[0]+row["weights"]
        assert len(weights)==1+(n-2)//(m-2) and all(type(v)==int and v>=0 for v in weights)
        copies=sum(weights[d]*comb(n-d*(m-2),2) for d in range(1,len(weights)))
        incidence=max(sum(comb(m-j,2)*weights[h//j] for j in range(1,m-1)
                      if h%j==0 and h//j<len(weights)) for h in range(1,n-1))
        upper=comb(n,2)-(n-1)+(n-1)//3
        margin=k*copies-incidence*upper
        assert margin>0
        print(f"If T_{m} has at least {k} rainbows in every proper coloring, "
              f"R3 <= {n}. Integer margin {margin:,}.")

if __name__=="__main__":main()
