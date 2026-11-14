"""Check the span-425 exclusion at side 461 with the Python standard library.

Every propagation step colors the last cell of a directed triple whose other
two colors are known and equal. A contradiction forbids one candidate mark.
"""

RULER = (0,9,33,37,38,97,122,129,140,142,152,191,205,208,252,278,
         286,326,332,353,368,384,403,425)
SIDE = 461


def frequency_bounds():
    window = [i*(86-i) for i in range(1,86)]
    corr = [sum(a*b for a,b in zip(window,window[d:])) for d in range(85)]
    total = sum(window)
    nonzero = 2*sum((48 if SIDE-d>=426 else 46)*corr[d] for d in range(1,85))
    possible = [s for s in range(SIDE+1)
                if s*s*total*total <= (SIDE+84)*(s*corr[0]+nonzero)]
    return SIDE-2*max(possible), max(possible)


def forbidden(starts, lag, extra):
    marks = set(starts)
    marks.add(extra)
    source = {}
    queue = [(x+lag,x,1) for x in RULER]
    while queue:
        x,y,color = queue.pop()
        old = source.get((x,y))
        if old is not None:
            if old!=color:
                return True
            continue
        source[x,y] = color
        # Three choices of the role of (x,y). Generate partner coordinates
        # from one marked row or column, require both other cells in the source.
        def check(a,b,c,d):
            if a<=b or c<=d or a not in marks or b not in marks or c not in marks or d not in marks:
                return
            if source.get((a,b))==color:
                queue.append((c,d,1-color))
            if source.get((c,d))==color:
                queue.append((a,b,1-color))
        for t in marks:
            if t>x:
                h=t-x
                check(t,y,t,y+h)
            if t<x:
                h=x-t
                check(t,y,x,y+h)
            if t<y:
                h=y-t
                check(x-h,t,x,t)
    return False


def main():
    low,high = frequency_bounds()
    print(f"Three-color diagonal frequencies lie in [{low}, {high}].",flush=True)
    limits = []
    for d in range(1,36):
        compulsory = set(RULER) | {x+d for x in RULER}
        # At a given start s the diagonal positions relative to it are
        # [-s,460-s]. All starts have 0<=s<=35-d.
        # Check every physical position allowed by at least one placement.
        first = d-35
        excluded = {v for v in range(first, SIDE)
                    if v not in compulsory and forbidden(compulsory,d,v)}
        most = max(SIDE-sum(-s<=x<SIDE-s for x in excluded) for s in range(36-d))
        limits.append(most)
        if most>=low:
            raise ValueError(f"unresolved optimal source at shift {d}: {most}")
        print(f"lag {d:2d}, at most {most} diagonal positions in its original color",flush=True)
    if max(limits) != 95 or (low,high) != (135,163):
        raise ValueError("margin regression")
    print(f"All 35 lags excluded. Largest eligible count {max(limits)}.",flush=True)


if __name__=="__main__":
    main()
