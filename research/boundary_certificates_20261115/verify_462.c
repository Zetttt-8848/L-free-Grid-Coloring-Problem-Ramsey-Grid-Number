/* Checkable certificate for the directed-L three-color bound.
   Build as C99 or later with 64-bit integer support. No dependencies.
   The accompanying proof gives the correspondence between the search and the grid. */
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef uint64_t Mask;
typedef int64_t Score;

static unsigned length, layers, position[39];
static Mask forbid[3], starts[39], powers_of_three[39];
static Score weight[85], cutoff;
static uint64_t covered, remaining, visits, cuts;

static unsigned smaller(unsigned x, unsigned y) { return x < y ? x : y; }

static unsigned population(Mask x) {
    /* Parallel bit sum, including portable compilers without a popcount intrinsic. */
    x -= (x >> 1) & UINT64_C(0x5555555555555555);
    x = (x & UINT64_C(0x3333333333333333))
        + ((x >> 2) & UINT64_C(0x3333333333333333));
    x = (x + (x >> 4)) & UINT64_C(0x0f0f0f0f0f0f0f0f);
    return (unsigned)((x * UINT64_C(0x0101010101010101)) >> 56);
}

static unsigned capped_pair_count(Mask m) {
    if (m == 0) return 0;
    return (m & (m - 1)) == 0 ? 1 : 2;
}

static unsigned partial_deficit(unsigned d) {
    unsigned k = length - d, cap = smaller(6, k);
    Mask possible[3];
    unsigned color_bound = 0;
    for (unsigned c = 0; c < 3; c++) {
        /* Bit i is 1 iff neither end has already been assigned a different color. */
        possible[c] = starts[k] & ~(forbid[c] | (forbid[c] >> d));
        color_bound += capped_pair_count(possible[c]);
    }
    /* A start eligible for several colors can ultimately count only once. */
    unsigned distinct_bound = population(possible[0] | possible[1] | possible[2]);
    return cap - smaller(cap, smaller(color_bound, distinct_bound));
}

static void search(unsigned depth, uint64_t multiplicity, unsigned stop) {
    visits++;
    Score bound = 0;
    for (unsigned k = 1; k <= layers; k++) {
        unsigned d = length - k;
        bound += weight[d] * partial_deficit(d);
        if (bound >= cutoff) {
            covered += multiplicity * powers_of_three[length - depth];
            cuts++;
            return;
        }
    }
    if (depth == stop) {
        remaining += multiplicity * powers_of_three[length - depth];
        return;
    }

    Mask bit = UINT64_C(1) << position[depth];
    /* Root color can be chosen in three ways; after fixing it to 0,
       the opposite endpoint either equals it or has one of two other colors. */
    unsigned choices = depth == 0 ? 1 : (depth == 1 ? 2 : 3);
    for (unsigned c = 0; c < choices; c++) {
        uint64_t count = multiplicity;
        if (depth == 0) count *= 3;
        if (depth == 1 && c == 1) count *= 2;
        unsigned c1 = (c + 1) % 3, c2 = (c + 2) % 3;
        forbid[c1] |= bit;
        forbid[c2] |= bit;
        search(depth + 1, count, stop);
        forbid[c1] ^= bit;
        forbid[c2] ^= bit;
    }
}

/* Direct evaluation, independent of the masks and pruning routine. */
static Score evaluate(const char *word, unsigned count, int with_shape) {
    if (strlen(word) != length) { fprintf(stderr, "Wrong witness length\n"); exit(1); }
    Score sum = 0;
    for (unsigned k = 1; k <= count; k++) {
        unsigned d = length - k;
        unsigned matches[3] = {0, 0, 0};
        for (unsigned i = 0; i < k; i++)
            if (word[i] == word[i+d]) matches[(unsigned)(word[i]-'0')]++;
        unsigned t = 0;
        for (unsigned c = 0; c < 3; c++) t += smaller(2, matches[c]);
        if (with_shape && k >= 3 && k <= 6) t = smaller(t, k-1);
        sum += weight[d] * (smaller(6, k)-t);
    }
    return sum;
}

static Score setup(unsigned n) {
    length = n - 425;
    for (unsigned i = 0; i <= 84; i++) {
        weight[i] = 0;
        for (Score j = 1; j + i <= 85; j++)
            weight[i] += j*(86-j)*(j+i)*(86-j-i);
    }
    Score gap = -(Score)n * weight[0];
    for (unsigned d = 1; d <= 84; d++) {
        unsigned extra = d < length ? smaller(6, length-d) : 0;
        gap += ((Score)n-d-3*(138+extra))*weight[d];
    }
    powers_of_three[0] = 1;
    for (unsigned j = 1; j <= length; j++) {
        powers_of_three[j] = powers_of_three[j-1]*3;
        starts[j] = (UINT64_C(1)<<j)-1;
    }
    for (unsigned j = 0; j < length; j++)
        position[j] = j % 2 == 0 ? j/2 : length-1-j/2;
    return gap;
}

static void require(int condition, const char *message) {
    if (!condition) { fprintf(stderr, "FAIL %s\n", message); exit(1); }
}

/* In the smaller test, count every full word below a chosen threshold by literal
   loops and independently by the partial-word bound and symmetry factors. */
static void self_test(void) {
    setup(432); /* shape of the search only, with 7 letters */
    layers = 6;
    cutoff = INT64_C(2000000000);
    covered = remaining = visits = cuts = 0;
    search(0, 1, length);
    uint64_t literal = 0;
    for (unsigned i = 0; i < powers_of_three[length]; i++) {
        unsigned v=i;
        char word[8];
        for (unsigned j=0; j<length; j++) {word[j]='0'+v%3; v/=3;}
        if (evaluate(word, layers, 0) < cutoff) literal++;
    }
    require(literal > 0 && literal < powers_of_three[length], "nontrivial test");
    require(literal == remaining && literal+covered == powers_of_three[length],
            "literal small instance / reflection-free color quotient");
    printf("small check: %" PRIu64 " of %" PRIu64 " words below cutoff\n",
           literal, powers_of_three[length]);
}

static void certificate(unsigned n, unsigned use_layers, Score target) {
    Score base = setup(n);
    layers = use_layers; cutoff = target;
    covered = remaining = visits = cuts = 0;
    search(0, 1, smaller(length,2*layers));
    require(covered+remaining == powers_of_three[length], "full labeled word count");
    require(remaining == 0, "a word below the stated bound exists");
    require(base+3*target > 0, "nonpositive Ramsey margin");
    printf("side=%u layers=%u word_length=%u words=%" PRIu64
           " visited=%" PRIu64 " cut_branches=%" PRIu64
           " remaining=%" PRIu64 " base=%" PRId64 " certified_loss=%" PRId64
           " margin=%" PRId64 "\n",
           n,layers,length,covered,visits,cuts,remaining,base,target,base+3*target);
}

int main(void) {
    self_test();
    certificate(463,10,INT64_C(1322324010));
    require(evaluate("00111111110000000000000000000000000011",10,0)
            == INT64_C(1322324010), "463 equality witness");
    certificate(462,36,INT64_C(2500000000));
    certificate(462,23,INT64_C(2492241107));
    require(evaluate("0002222111220111101020020020020121121",22,1)
            == INT64_C(2488214141), "22-layer negative witness");
    Score base = setup(461);
    const char *word = "000222211111100020211022002112022110";
    Score loss = evaluate(word,35,1);
    require(loss == INT64_C(3451852478) && base+3*loss == -INT64_C(1013624558),
            "461 word");
    printf("side=461 all 35 shifts with shape cap: loss=%" PRId64
           " margin=%" PRId64 " word=%s\n",loss,base+3*loss,word);
    return 0;
}
