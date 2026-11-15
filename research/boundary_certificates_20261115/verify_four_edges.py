"""Check the endpoint variance bound from seven coarse table entries."""
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import Path
import json
import sys

from verify_four_double import sidon_length
from verify_four_twenty import outer_twenty
from verify_four_window import HERE, REFERENCE, load_window, require, verify_profile

SIDE = 21_947_877
WIDTH = 35_990
SAMPLES = [(0,0,90), (0,2,76), (1,1,82), (1,0,90), (0,1,89), (1,2,96), (1,0,91)]
INNER = (15_000, 16_600, 22_500_000, 4_600, 8, 52)
BINARY = (1_720, 1_820, 21_975_000, 455_000, 4, 213)


def read_samples(folder=None):
    samples = json.loads((HERE / "four_window_edges.json").read_text())
    require([tuple(r[:3]) for r in samples] == SAMPLES, "coarse edge indices")
    if folder is not None:
        def matrix(name):
            return [[Fraction(v) for v in line.split(",")]
                    for line in (folder / (name + ".txt")).read_text().splitlines()]
        g, h, prob = matrix("G"), matrix("H"), matrix("p")[0]
        for end, i, j, *raw in samples:
            row = g[i][::-1] if end else g[i]
            table = h[i][::-1] if end else h[i]
            mass = sum(row)
            expect = [prob[i], row[j]/mass, sum(row[:j])/mass, table[j]]
            require(list(map(Fraction, raw)) == expect, "authors' endpoint coefficients")
    return samples


@lru_cache(None)
def local_cap(n, binary):
    if n < 1:
        return 0
    gamma = 2 * local_cap(n, False) if binary else 1
    cap = n if binary else (1 + isqrt(1 + 8*(n-1))) // 2
    for width in (4,8,12,18,24,35,50,70,100,140,200,280,400,600,850,1200,1800):
        a = n + width - 1
        radical = a*a + 4*width*a*gamma*(width-1)
        cap = min(cap, (a + isqrt(radical)) // (2*width))
    return cap


def variance_certificate(samples, alpha, domain, binary):
    bmin, bmax, pmax, kmin, step, saving = domain
    rate = Fraction(kmin, 1) / (pmax + bmax*alpha)
    total = Fraction(0)
    for end, i, j, *raw in samples:
        pr, g, prior, h = map(Fraction, raw)
        require(pr>0 and min(g, prior, h)>=0, "nonnegative endpoint data")
        old = prior * local_cap(bmax,binary)
        for lo in range(0,bmin,step):
            hi = min(bmin,lo+step)
            shortfall = h - (g*local_cap(hi,binary)+old)/(bmin*rate)
            if shortfall <= 0:
                break
            total += pr*(hi-lo)*shortfall**2
    require(total >= saving, "insufficient endpoint variance")
    return total


def domain_check(domain, k, p, width):
    bmin, bmax, pmax, kmin, _, saving = domain
    require(bmin<=width<=bmax and saving<p<=pmax and k>=kmin, "variance parameter range")


def quartic_correlations(t):
    def weight(i):
        u = i*(t+1-i)
        return u*(5*(t+1)**2+6*u)
    first = [sum(weight(i)*weight(i+t-x) for i in range(1,x+1)) for x in range(10)]
    differences = []
    while first:
        differences.append(first[0])
        first = [b-a for a,b in zip(first,first[1:])]
    result = []
    for _ in range(t+1):
        result.append(differences[0])
        for j in range(9):
            differences[j] += differences[j+1]
    result.reverse()
    require(result[-1]==0 and all(a>b for a,b in zip(result,result[1:])),
            "positive decreasing quartic correlations")
    for d in (0,1,19,t//2,t-117):
        require(result[d]==sum(weight(i)*weight(i+d) for i in range(1,t-d+1)),
                "literal quartic correlation")
    return result


def main():
    folder = Path(sys.argv[1]) if len(sys.argv)>1 else None
    den,r,alpha = load_window(folder)
    samples = read_samples(folder)
    for domain,binary in ((INNER,False),(BINARY,True)):
        variance_certificate(samples,alpha,domain,binary)
    def inner_domain(k,p,b):
        domain_check(INNER,k,p,b)
    thresholds = [sidon_length(k,den,r,alpha,INNER[-1],inner_domain)
                  for k in range(4600,4801)]
    rows = json.loads((HERE/"four_edge_runs.json").read_text())
    for v,cap,b in rows:
        domain_check(BINARY,cap+1,REFERENCE-v,b)
    verify_profile(rows,den,r,alpha,thresholds,BINARY[-1])
    a = quartic_correlations(WIDTH)
    count,raw,bonus,loss = outer_twenty(rows,SIDE,WIDTH,lambda t,d:a[d])
    require((count,raw,bonus)==(561,
            -8994733962487986521984660222886550382497049520,
            9898715879654775090490051377873405177480967584), "outer sums")
    require(raw+bonus>0, "positive final margin")
    print(f"Edge savings {INNER[-1]} and {BINARY[-1]}, {len(rows)} binary bounds, "
          f"{count} blocks of loss {loss}, side {SIDE:,}, margin {raw+bonus:,}.")


if __name__ == "__main__":
    main()
