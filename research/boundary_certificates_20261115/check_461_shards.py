"""Run the portable 461 verifier on disjoint six-letter prefix classes."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import argparse
import re
import subprocess

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("checker",type=Path)
    parser.add_argument("--jobs",type=int,default=4)
    args=parser.parse_args()
    if args.jobs<1:parser.error("jobs must be positive")
    binary=str(args.checker.resolve(strict=True))
    words=[]
    def extend(digits,used):
        if len(digits)==6:
            words.append(digits)
            return
        for c in range(min(3,used+1)):
            extend(digits+(c,),max(used,c+1))
    extend((),0)
    def shard(index):
        out=subprocess.run([binary,"--461-shard",str(index)],capture_output=True,text=True,check=True).stdout
        match=re.search(r"^shard=(\d+) covered=(\d+) remaining=(\d+) nodes=(\d+)$",out,re.M)
        if not match:raise ValueError((index,out))
        shard_id,covered,remaining,nodes=map(int,match.groups())
        used=len(set(words[index]))
        multiplicity=3 if used==1 else 6
        if (shard_id,covered,remaining)!=(index,multiplicity*3**29,0):raise ValueError(out)
        return covered,nodes
    covered=nodes=0
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures=[pool.submit(shard,i) for i in range(len(words))]
        for done,f in enumerate(as_completed(futures),1):
            c,n=f.result()
            covered+=c;nodes+=n
            if done%20==0:print(f"{done} of {len(words)} shards",flush=True)
    if len(words)!=122 or covered!=3**35:raise ValueError("incomplete global count")
    print(f"All {covered:,} labeled words excluded in {nodes:,} visited nodes.")
if __name__=="__main__":main()
