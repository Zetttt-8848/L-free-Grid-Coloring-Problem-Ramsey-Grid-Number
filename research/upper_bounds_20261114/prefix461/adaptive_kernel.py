"""Word-adaptive kernels for the three-color prefix inequality.

For a proper n-square with diagonal prefix z of length b = n-425 and any
nonnegative integer vector w = (w_0, ..., w_{W-1}), with a_d = sum_i w_i w_{i+d},

    Q_z(w) = -2n a_0 + 2 sum_{d>=1} (n - d - 3 Uhat_d(z)) a_d  <=  0,

where Uhat_d(z) = 138 + min(6, b-d) - delta_{b-d}(z) for 1 <= d <= b-1 and
Uhat_d = 138 for d >= b, and delta_k(z) = min(k,6) - T_k(z),
T_k(z) = sum_c min(2, #{i<k : z_i = z_{i+b-k} = c}).
(Proof: see ../proof.md, Section 3.)  Hence a word z is excluded as soon as
some w >= 0 gives Q_z(w) > 0.  This script searches for such w numerically
and certifies it by exact integer evaluation.
"""
import numpy as np


def deficits(z, b):
    out = {}
    for k in range(1, b):
        d = b - k
        m = [0, 0, 0]
        for i in range(k):
            if z[i] == z[i + d]:
                m[int(z[i])] += 1
        t = sum(min(2, x) for x in m)
        out[d] = min(k, 6) - t
    return out


def coeffs(z, n, W):
    b = n - 425
    dl = deficits(z, b)
    c = [0] * W
    c[0] = -2 * n
    for d in range(1, W):
        U = 138 + (min(6, b - d) - dl[d] if d < b else 0)
        c[d] = n - d - 3 * U
    return c


def exact_Q(c, w):
    """c[0] a_0 + 2 sum_{d>=1} c[d] a_d, exact integers (w nonnegative integers)."""
    W = len(w)
    assert all(x >= 0 for x in w)
    tot = 0
    for d in range(W):
        ad = sum(w[i] * w[i + d] for i in range(W - d))
        tot += (c[0] if d == 0 else 2 * c[d]) * ad
    return tot


def toeplitz(c):
    W = len(c)
    T = np.empty((W, W))
    for i in range(W):
        for j in range(W):
            d = abs(i - j)
            T[i, j] = c[0] if d == 0 else c[d]
    return T


def best_nonneg(c, iters=3000, seed_w=None):
    """Projected power iteration for max w^T T w on {w >= 0, |w| = 1}."""
    T = toeplitz(c)
    W = len(c)
    sigma = np.abs(T).sum(axis=1).max()
    if seed_w is None:
        i = np.arange(1, W + 1)
        w = i * (W + 1 - i) * 1.0
    else:
        w = np.array(seed_w, dtype=float)
    w /= np.linalg.norm(w)
    for _ in range(iters):
        v = np.maximum(T @ w + sigma * w, 0)
        nv = np.linalg.norm(v)
        if nv == 0:
            break
        w = v / nv
    return w, float(w @ T @ w)


def certify(z, n, W=120, scale=10 ** 6):
    c = coeffs(z, n, W)
    w, val = best_nonneg(c)
    wi = [int(round(x * scale)) for x in w]
    q = exact_Q(c, wi)
    return q, val, wi
