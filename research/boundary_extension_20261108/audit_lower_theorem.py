"""Independent finite cross-check of explicit extension formulas.

Reads no author's implementation. Direct geometry tests each complete rectangle.
"""
from itertools import product
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def proper(matrix):
    h,w=len(matrix),len(matrix[0])
    return all(len({matrix[x][y],matrix[x+d][y],matrix[x+d][y+d]})>1
        for x in range(h) for y in range(w) for d in range(1,min(h-x,w-y)))

def main():
    results=[]
    for n,k in [(1,2),(2,2),(3,2),(1,3),(2,3)]:
        count_old=0; tested={'bottom_right':0,'single_bottom':0,'single_left':0}
        for word in product(range(k),repeat=n*n):
            c=[list(word[i*n:(i+1)*n]) for i in range(n)]
            if not proper(c): continue
            count_old+=1
            for new in product(range(k),repeat=2*n+1):
                b=new[:n+1]; r=new[n+1:]
                full=[row+[r[i]] for i,row in enumerate(c)]+[list(b)]
                unary=all(r[i] not in {c[i-d][n-d] for d in range(1,i+1)
                    if c[i-d][n-d]==c[i][n-d]} for i in range(n))
                pairs=all(not(b[j]==b[l]==c[n-l+j][j]) for j in range(n+1) for l in range(j+1,n+1))
                if proper(full)!=(unary and pairs): raise ValueError('Bottom-right formula fails')
                tested['bottom_right']+=1
            for edge in product(range(k),repeat=n):
                full=c+[list(edge)]
                pairs=all(not(edge[j]==edge[l]==c[n-l+j][j]) for j in range(n) for l in range(j+1,n))
                if proper(full)!=pairs: raise ValueError('Bottom formula fails')
                tested['single_bottom']+=1
                full=[[edge[i]]+row for i,row in enumerate(c)]
                pairs=all(not(edge[j]==edge[l]==c[l][l-j-1]) for j in range(n) for l in range(j+1,n))
                if proper(full)!=pairs: raise ValueError('Left formula fails')
                tested['single_left']+=1
        results.append({'n':n,'k':k,'proper_old_matrices':count_old,'complete_assignments_checked':tested})
    result={'status':'PASS','scope':'Five explicit (n,k) pairs; all proper old matrices and every new-layer assignment; does not replace general proof.', 'results':results}
    (HERE/'lower_theorem_audit.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
