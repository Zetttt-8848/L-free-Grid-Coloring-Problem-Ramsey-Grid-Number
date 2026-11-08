"""Published Golomb input, in occupied-position convention.

Mammel--Smith--Yerger arXiv:2502.05162v1 Algorithm 3. Entry g[m]
is one plus the minimum span of an m-mark Golomb ruler (entry zero is 0).
Only capacities for length <=585 positions are supported here.
This file does not independently prove the externally tabulated optima.
"""
from bisect import bisect_right

MIN_POSITIONS = (0, 1, 2, 4, 7, 12, 18, 26, 35, 45, 56, 73, 86,
                 107, 128, 152, 178, 200, 217, 247, 284, 334, 357,
                 373, 426, 481, 493, 554, 586)


def golomb_capacity(positions):
    if not 0 <= positions < MIN_POSITIONS[-1]:
        raise ValueError('Outside published table coverage')
    return bisect_right(MIN_POSITIONS, positions) - 1


def difference_cap(n, d):
    """r_d(A) for one diagonal color class in an n-square."""
    if not 1 <= d < n:
        raise ValueError('Positive difference strictly below side required')
    return min(n-d, 2*golomb_capacity(n-d))
