/* Portable ISO C99 verifier for compact binary LGB1 decision-tree certificates.
 * Reads uncompressed LGB1 stream from file path (argv[1]) or stdin ("-").
 * Uses zero external libraries, zero floating-point arithmetic, and < 32 MB RAM.
 *
 * Verifies from first principles:
 *   1. Every 2-color decision-tree lemma (m, mask, T) by confluent unit propagation
 *      on the strict source V(U) = {(v, u) in U^2 : u < v}.
 *   2. Every inductive UNSAT span (k, L) across hereditary-span + reflection orbits,
 *      requiring every unpruned branch to belong to the verified lemma hash set.
 *   3. Every exact-span witness (witness_A, witness_col) against all physical
 *      directed equal-leg Ls ((v, u), (v+t, u), (v+t, u+t)) with integer t > 0.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static void die(const char *msg) {
    fprintf(stderr, "VERIFY FAILED: %s\n", msg);
    exit(1);
}

static void fread_exact(uint8_t *dst, size_t n, FILE *fp) {
    if (n > 0 && fread(dst, 1, n, fp) != n) {
        die("unexpected EOF in LGB1 stream");
    }
}

static uint8_t read_u8(FILE *fp) {
    uint8_t b = 0;
    fread_exact(&b, 1, fp);
    return b;
}

static uint32_t read_u32_le(FILE *fp) {
    uint8_t b[4];
    fread_exact(b, 4, fp);
    return (uint32_t)b[0]
         | ((uint32_t)b[1] << 8)
         | ((uint32_t)b[2] << 16)
         | ((uint32_t)b[3] << 24);
}

static uint64_t read_u64_le(FILE *fp) {
    uint8_t b[8];
    fread_exact(b, 8, fp);
    uint64_t v = 0;
    for (int i = 0; i < 8; ++i) {
        v |= ((uint64_t)b[i] << (8 * i));
    }
    return v;
}

#define HT_BITS 21
#define HT_SIZE (1U << HT_BITS)
static uint64_t ht_keys[HT_SIZE];

static void ht_insert(uint64_t key) {
    if (key == 0) die("zero hash key");
    uint32_t h = (uint32_t)((key * UINT64_C(11400714819323198485)) >> (64 - HT_BITS));
    while (ht_keys[h] != 0 && ht_keys[h] != key) {
        h = (h + 1U) & (HT_SIZE - 1U);
    }
    ht_keys[h] = key;
}

static int ht_contains(uint64_t key) {
    uint32_t h = (uint32_t)((key * UINT64_C(11400714819323198485)) >> (64 - HT_BITS));
    while (ht_keys[h] != 0) {
        if (ht_keys[h] == key) return 1;
        h = (h + 1U) & (HT_SIZE - 1U);
    }
    return 0;
}

static uint64_t to_mask(const int *arr, int m) {
    uint64_t mask = 0;
    int base = arr[0];
    for (int i = 0; i < m; ++i) {
        int shift = arr[i] - base;
        if (shift < 0 || shift >= 56) die("shift out of [0, 55]");
        mask |= (UINT64_C(1) << shift);
    }
    return mask;
}

static uint64_t reflect_mask(uint64_t mask, int span) {
    uint64_t r = 0;
    for (int b = 0; b <= span; ++b) {
        if ((mask >> b) & 1ULL) {
            r |= (UINT64_C(1) << (span - b));
        }
    }
    return r;
}

typedef struct { uint16_t y, z; } AdjPair;
static int g_head[257];
static AdjPair g_adj[16384];
static int g_num_cells;
static const int16_t *g_T;
static uint32_t g_T_len, g_T_pos;

/* Eager-assignment unit propagation on V(U): each cell is queued at most once (<= g_num_cells <= 256). */
static int prop_2col(int8_t *val, int start_x, int start_b) {
    int8_t cur_start = val[start_x];
    if (cur_start != -1) {
        return cur_start == (int8_t)start_b;
    }
    uint16_t queue[256];
    int qh = 0, qt = 0;
    val[start_x] = (int8_t)start_b;
    queue[qt++] = (uint16_t)start_x;

    while (qh < qt) {
        int x = queue[qh++];
        int8_t bx = val[x];
        int8_t opp = (int8_t)(1 - bx);
        for (int idx = g_head[x]; idx < g_head[x + 1]; ++idx) {
            int y = g_adj[idx].y;
            int z = g_adj[idx].z;
            int8_t vy = val[y];
            int8_t vz = val[z];
            if (vy == bx) {
                if (vz == bx) return 0;
                if (vz == -1) {
                    val[z] = opp;
                    queue[qt++] = (uint16_t)z;
                }
            } else if (vz == bx) {
                if (vy == -1) {
                    val[y] = opp;
                    queue[qt++] = (uint16_t)y;
                }
            }
        }
    }
    return 1;
}

static void check_tree_rec(const int8_t *parent_val, int cell, int col, int depth) {
    if (depth > g_num_cells + 1) die("decision tree exceeds cell count depth");
    int8_t vcopy[256];
    memcpy(vcopy, parent_val, (size_t)g_num_cells);
    int ok = prop_2col(vcopy, cell, col);
    if (g_T_pos >= g_T_len) die("unexpected end of decision tree");
    int op = g_T[g_T_pos++];
    if (op == -1) {
        if (ok) die("claimed unit-propagation conflict did not occur");
        return;
    }
    if (!ok || op < 0 || op >= g_num_cells || vcopy[op] != -1) {
        die("invalid internal branch cell in decision tree");
    }
    check_tree_rec(vcopy, op, 0, depth + 1);
    check_tree_rec(vcopy, op, 1, depth + 1);
}

static int verify_lemma_mask(int k, uint64_t mask, const int16_t *T, uint32_t T_len) {
    if (k < 2 || k > 22 || !(mask & 1ULL)) die("invalid lemma cardinality or origin");
    if ((mask >> 56) != 0ULL) die("lemma span exceeds 55");
    int U[32];
    int cnt = 0;
    for (int b = 0; b < 56; ++b) {
        if ((mask >> b) & 1ULL) {
            if (cnt >= k) die("mask popcount exceeds m");
            U[cnt++] = b;
        }
    }
    if (cnt != k) die("mask popcount less than m");
    int maxU = U[k - 1];
    int present[64];
    for (int i = 0; i <= maxU; ++i) present[i] = -1;
    for (int i = 0; i < k; ++i) present[U[i]] = i;

    g_num_cells = k * (k - 1) / 2;
    int deg[256];
    memset(deg, 0, sizeof(deg));
    uint16_t ta[4096], tb[4096], tc[4096];
    int n_tr = 0;
    for (int u_i = 0; u_i < k; ++u_i) {
        for (int v_i = u_i + 1; v_i < k; ++v_i) {
            uint16_t c1 = (uint16_t)(v_i * (v_i - 1) / 2 + u_i);
            for (int t = 1; U[v_i] + t <= maxU; ++t) {
                int ut_i = present[U[u_i] + t];
                int vt_i = present[U[v_i] + t];
                if (ut_i >= 0 && vt_i >= 0) {
                    if (n_tr >= 4096) die("L-triple buffer overflow");
                    uint16_t c2 = (uint16_t)(vt_i * (vt_i - 1) / 2 + u_i);
                    uint16_t c3 = (uint16_t)(vt_i * (vt_i - 1) / 2 + ut_i);
                    ta[n_tr] = c1; tb[n_tr] = c2; tc[n_tr] = c3;
                    ++n_tr;
                    deg[c1]++; deg[c2]++; deg[c3]++;
                }
            }
        }
    }
    g_head[0] = 0;
    for (int i = 0; i < g_num_cells; ++i) g_head[i + 1] = g_head[i] + deg[i];
    if (g_head[g_num_cells] > 16384) die("adjacency buffer overflow");
    int cur[256];
    memcpy(cur, g_head, (size_t)g_num_cells * sizeof(int));
    for (int i = 0; i < n_tr; ++i) {
        uint16_t a = ta[i], b = tb[i], c = tc[i];
        g_adj[cur[a]++] = (AdjPair){b, c};
        g_adj[cur[b]++] = (AdjPair){a, c};
        g_adj[cur[c]++] = (AdjPair){a, b};
    }

    if (T_len < 2 || T[0] < 0 || T[0] >= g_num_cells) die("invalid tree root cell");
    g_T = T;
    g_T_len = T_len;
    g_T_pos = 1;
    int8_t init_val[256];
    memset(init_val, -1, (size_t)g_num_cells);
    check_tree_rec(init_val, T[0], 0, 1);
    if (g_T_pos != g_T_len) die("trailing tokens in decision tree");
    return maxU;
}

static void verify_witness(int k, int L, const uint8_t *A, const uint8_t *col) {
    if (k < 2 || L < 1 || L >= 64) die("witness domain");
    if (A[0] != 0 || A[k - 1] != (uint8_t)L) die("witness endpoints");
    for (int i = 0; i + 1 < k; ++i) {
        if (A[i] >= A[i + 1]) die("witness marks not strictly increasing");
    }
    int nc = k * (k - 1) / 2;
    for (int i = 0; i < nc; ++i) {
        if (col[i] > 1U) die("witness color outside {0, 1}");
    }
    int present[64];
    for (int i = 0; i <= L; ++i) present[i] = -1;
    for (int i = 0; i < k; ++i) present[A[i]] = i;
    for (int u_i = 0; u_i < k; ++u_i) {
        for (int v_i = u_i + 1; v_i < k; ++v_i) {
            int c1 = col[v_i * (v_i - 1) / 2 + u_i];
            for (int t = 1; (int)A[v_i] + t <= L; ++t) {
                int ut_i = present[(int)A[u_i] + t];
                int vt_i = present[(int)A[v_i] + t];
                if (ut_i >= 0 && vt_i >= 0) {
                    int c2 = col[vt_i * (vt_i - 1) / 2 + u_i];
                    int c3 = col[vt_i * (vt_i - 1) / 2 + ut_i];
                    if (c1 == c2 && c2 == c3) die("monochromatic L in witness");
                }
            }
        }
    }
}

static int g_e[32];
static int g_cur[32];
static int g_k, g_L;
static uint64_t g_leaves_checked;

static int pruned_at(int idx) {
    const int ms[3] = {12, 13, 14};
    for (int mi = 0; mi < 3; ++mi) {
        int m = ms[mi];
        if (g_k > m && idx >= m - 1 && g_cur[idx] - g_cur[idx - m + 1] <= m + 10) {
            uint64_t key = ((uint64_t)m << 56) | to_mask(&g_cur[idx - m + 1], m);
            if (ht_contains(key)) return 1;
        }
    }
    return 0;
}

static void walk_unsat(int idx) {
    if (idx == g_k - 1) {
        for (int i = 1; i < g_k - 1; ++i) {
            if (g_L - g_cur[i] < g_e[g_k - i]) return;
        }
        if (pruned_at(g_k - 1)) return;
        for (int i = 0; i < g_k; ++i) {
            int r = g_L - g_cur[g_k - 1 - i];
            if (g_cur[i] < r) break;
            if (g_cur[i] > r) return;
        }
        uint64_t key = ((uint64_t)g_k << 56) | to_mask(g_cur, g_k);
        if (!ht_contains(key)) die("uncovered candidate in UNSAT span");
        ++g_leaves_checked;
        return;
    }
    int lo = g_cur[idx - 1] + 1;
    for (int i = 0; i < idx; ++i) {
        int bound = g_cur[i] + g_e[idx - i + 1];
        if (bound > lo) lo = bound;
    }
    int hi = g_L - g_e[g_k - idx];
    for (int v = lo; v <= hi; ++v) {
        g_cur[idx] = v;
        if (!pruned_at(idx)) walk_unsat(idx + 1);
    }
}

int main(int argc, char **argv) {
    clock_t t0 = clock();
    FILE *fp = (argc > 1 && strcmp(argv[1], "-") != 0) ? fopen(argv[1], "rb") : stdin;
    if (!fp) {
        perror("fopen");
        return 2;
    }

    uint8_t magic[4];
    fread_exact(magic, 4, fp);
    if (memcmp(magic, "LGB1", 4) != 0) die("bad LGB1 magic header");

    uint32_t n_lem = read_u32_le(fp);
    if (n_lem > (HT_SIZE / 3U)) die("too many lemmas for hash table");

    uint32_t raw_cap = 131072;
    uint8_t *raw_t = (uint8_t *)malloc((size_t)raw_cap * 2U);
    int16_t *T_buf = (int16_t *)malloc((size_t)raw_cap * sizeof(int16_t));
    if (!raw_t || !T_buf) die("out of memory");

    for (uint32_t i = 0; i < n_lem; ++i) {
        uint8_t m = read_u8(fp);
        uint64_t mask = read_u64_le(fp);
        uint32_t tl = read_u32_le(fp);
        if (tl < 2U || tl > 1048576U) die("invalid tree length");
        if (tl > raw_cap) {
            raw_cap = tl * 2U;
            raw_t = (uint8_t *)realloc(raw_t, (size_t)raw_cap * 2U);
            T_buf = (int16_t *)realloc(T_buf, (size_t)raw_cap * sizeof(int16_t));
            if (!raw_t || !T_buf) die("out of memory");
        }
        fread_exact(raw_t, (size_t)tl * 2U, fp);
        for (uint32_t j = 0; j < tl; ++j) {
            uint16_t u = (uint16_t)raw_t[2U * j] | ((uint16_t)raw_t[2U * j + 1U] << 8);
            T_buf[j] = (int16_t)u;
        }
        int span = verify_lemma_mask((int)m, mask, T_buf, tl);
        ht_insert(((uint64_t)m << 56) | mask);
        ht_insert(((uint64_t)m << 56) | reflect_mask(mask, span));
    }
    free(raw_t);
    free(T_buf);

    printf("[C99 LGB1] Verified %u 2-color decision-tree lemmas in %.3fs.\n",
           n_lem, (double)(clock() - t0) / CLOCKS_PER_SEC);

    uint32_t n_st = read_u32_le(fp);
    if (n_st == 0U || n_st > 20U) die("invalid step count");

    g_e[1] = 0;
    for (uint32_t s = 0; s < n_st; ++s) {
        uint8_t k = read_u8(fp);
        uint8_t lb = read_u8(fp);
        uint8_t exact = read_u8(fp);
        uint8_t nu = read_u8(fp);
        if ((int)k != (int)s + 2) die("non-sequential k in steps");
        if (nu > 31U) die("nu > 31");
        uint8_t unsat_L[32];
        if (nu) fread_exact(unsat_L, (size_t)nu, fp);

        int exp_L = g_e[k - 1] + 1;
        g_leaves_checked = 0;
        for (uint8_t i = 0; i < nu; ++i) {
            if ((int)unsat_L[i] != exp_L) die("non-contiguous unsat_L");
            g_k = (int)k;
            g_L = exp_L;
            g_cur[0] = 0;
            g_cur[k - 1] = exp_L;
            walk_unsat(1);
            ++exp_L;
        }
        if ((int)lb != exp_L) die("lower_bound mismatch");

        if (exact) {
            uint8_t win_A[32], win_col[512];
            fread_exact(win_A, (size_t)k, fp);
            fread_exact(win_col, (size_t)(k * (k - 1) / 2), fp);
            verify_witness((int)k, exp_L, win_A, win_col);
        } else if (exact != 0U) {
            die("invalid exact flag");
        }
        g_e[k] = exp_L;
        printf("  verified k=%2d: e_%d %s %2d (full_leaves=%llu)\n",
               (int)k, (int)k, exact ? "=" : ">=", exp_L,
               (unsigned long long)g_leaves_checked);
    }

    if (fgetc(fp) != EOF) die("trailing bytes after LGB1 stream");
    if (fp != stdin) fclose(fp);

    printf("[C99 LGB1] ALL %u STEPS VERIFIED in %.3fs!\n",
           n_st, (double)(clock() - t0) / CLOCKS_PER_SEC);
    return 0;
}
