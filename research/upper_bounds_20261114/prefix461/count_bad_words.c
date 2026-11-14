/* Count the diagonal prefix words not excluded by the PR 11 prefix inequality.

   Model (see ../proof.md, Section 3): side n, b = n - 425 prefix letters,
   weights w_i = i(W+1-i) for 1 <= i <= W, a_d their autocorrelation,
   U_d = 138 + min(6, max(0, b-d)), G_0 = -n a_0 + sum_{d=1}^{W-1} (n-d-3U_d) a_d,
   D(z) = sum_{k=1}^{K} a_{b-k} (min(k,6) - T_k(z)).
   Every proper square has a prefix with G_0 + 3 D(z) <= 0 ("bad word").
   This program enumerates bad words up to a simultaneous permutation of the
   three colors (first letter 0, first different letter 1), prints the number of
   labeled bad words, the number of orbits, and writes orbit representatives.

   Usage: count_bad_words n K W max_dump outfile
*/
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint64_t Mask;
typedef int64_t Score;

static unsigned b, K, W, order[64];
static Mask forbid[3];
static Score a[200], cutoff;
static uint64_t orbits, labeled, nodes, dumped, max_dump;
static int letter[64];
static FILE *out;

static unsigned popc(Mask x) { return (unsigned)__builtin_popcountll(x); }
static unsigned mn(unsigned x, unsigned y) { return x < y ? x : y; }

/* Lower bound on min(k,6)-T_k over all completions of the partial word. */
static unsigned deficit_lb(unsigned k) {
    unsigned d = b - k, cap = mn(6, k), cb = 0;
    Mask st = (k >= 64) ? ~(Mask)0 : (((Mask)1 << k) - 1), any = 0;
    for (unsigned c = 0; c < 3; c++) {
        Mask p = st & ~(forbid[c] | (forbid[c] >> d));
        unsigned q = popc(p);
        cb += q > 2 ? 2 : q;
        any |= p;
    }
    unsigned t = mn(cap, mn(cb, popc(any)));
    return cap - t;
}

static void rec(unsigned depth, int maxcolor) {
    nodes++;
    Score s = 0;
    for (unsigned k = 1; k <= K; k++) {
        s += a[b - k] * (Score)deficit_lb(k);
        if (s >= cutoff) return;          /* every completion is excluded */
    }
    if (depth == b) {
        /* orbit size: 3!/(stabilizer) = 3 if one color used, 6 otherwise */
        uint64_t mult = maxcolor == 0 ? 3 : 6;
        orbits++;
        labeled += mult;
        if (dumped < max_dump) {
            for (unsigned i = 0; i < b; i++) fputc('0' + letter[i], out);
            fputc('\n', out);
            dumped++;
        }
        return;
    }
    unsigned pos = order[depth];
    /* canonical labeling in order of assignment: new color = maxcolor+1 */
    int lim = maxcolor + 1 > 2 ? 2 : maxcolor + 1;
    for (int c = 0; c <= lim; c++) {
        Mask bit = (Mask)1 << pos;
        for (int e = 0; e < 3; e++) if (e != c) forbid[e] |= bit;
        letter[pos] = c;
        rec(depth + 1, c > maxcolor ? c : maxcolor);
        for (int e = 0; e < 3; e++) if (e != c) forbid[e] &= ~bit;
    }
}

int main(int argc, char **argv) {
    if (argc != 6) { fprintf(stderr, "usage\n"); return 2; }
    unsigned n = (unsigned)atoi(argv[1]);
    K = (unsigned)atoi(argv[2]);
    W = (unsigned)atoi(argv[3]);
    max_dump = strtoull(argv[4], 0, 10);
    out = fopen(argv[5], "w");
    b = n - 425;
    if (b > 63 || K > b - 1 || W >= 200) { fprintf(stderr, "range\n"); return 2; }
    for (unsigned d = 0; d < W; d++) {
        a[d] = 0;
        for (Score j = 1; j + d <= W; j++) a[d] += j * (W + 1 - j) * (j + d) * (W + 1 - j - d);
    }
    Score G0 = -(Score)n * a[0];
    for (unsigned d = 1; d < W; d++) {
        unsigned extra = d < b ? mn(6, b - d) : 0;
        G0 += ((Score)n - d - 3 * (138 + extra)) * a[d];
    }
    /* bad iff G0 + 3D <= 0 iff D <= floor(-G0/3); prune when D >= cutoff */
    Score need = (-G0) / 3 + 1;          /* G0 < 0 is checked below */
    if (G0 >= 0) { printf("G0 >= 0: excluded outright\n"); return 0; }
    cutoff = need;
    for (unsigned j = 0; j < b; j++) order[j] = j % 2 == 0 ? j / 2 : b - 1 - j / 2;
    rec(0, -1);
    printf("n=%u b=%u K=%u W=%u G0=%" PRId64 " cutoff=%" PRId64
           " nodes=%" PRIu64 " bad_orbits=%" PRIu64 " bad_labeled=%" PRIu64 "\n",
           n, b, K, W, G0, cutoff, nodes, orbits, labeled);
    fclose(out);
    return 0;
}
