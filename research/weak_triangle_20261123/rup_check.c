/* Standalone zero-dependency C99 forward RUP proof checker (2-watched literals).
   Accepts DIMACS CNF and RUP proof (clauses terminated by 0; 'd ... 0' deletion lines allowed).
   Verifies that every step is Reverse Unit Propagation (RUP) and ends with the empty clause '0'.
*/
#include <ctype.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int size;
    int active;
    int lits_offset;
} Clause;

static int num_vars = 0;
static Clause *clauses = NULL;
static int num_clauses = 0, cap_clauses = 0;
static int *lit_pool = NULL;
static int pool_len = 0, pool_cap = 0;

/* Watch lists: lit_index(l) = 2*|l| + (l < 0 ? 1 : 0) */
static int *watch_head = NULL;
static int *watch_next = NULL; /* 2 entries per clause: 2*cid + 0, 2*cid + 1 */
static int watch_cap_clauses = 0;

static int8_t *assign = NULL; /* 0 = unassigned, 1 = true, -1 = false (indexed by var 1..num_vars) */
static int *trail = NULL;
static int trail_len = 0;

static inline int lit_idx(int l) {
    return (l > 0) ? (2 * l) : (2 * (-l) + 1);
}

static inline int is_true(int l) {
    int v = (l > 0) ? l : -l;
    int8_t a = assign[v];
    return (l > 0) ? (a == 1) : (a == -1);
}

static inline int is_false(int l) {
    int v = (l > 0) ? l : -l;
    int8_t a = assign[v];
    return (l > 0) ? (a == -1) : (a == 1);
}

static void ensure_vars(int v) {
    if (v <= num_vars) return;
    int old_v = num_vars;
    int new_v = (old_v == 0) ? 1024 : old_v;
    while (new_v < v) new_v *= 2;
    assign = (int8_t *)realloc(assign, (new_v + 1) * sizeof(int8_t));
    memset(assign + old_v + 1, 0, (new_v - old_v) * sizeof(int8_t));
    trail = (int *)realloc(trail, (new_v + 1) * sizeof(int));
    watch_head = (int *)realloc(watch_head, (2 * new_v + 4) * sizeof(int));
    for (int i = 2 * old_v + 2; i < 2 * new_v + 4; ++i) watch_head[i] = -1;
    if (old_v == 0) {
        watch_head[0] = watch_head[1] = -1;
    }
    num_vars = new_v;
}

static void add_watch(int lit, int wnode) {
    int li = lit_idx(lit);
    watch_next[wnode] = watch_head[li];
    watch_head[li] = wnode;
}

static int enqueue(int lit) {
    if (is_false(lit)) return 0; /* conflict! */
    if (is_true(lit)) return 1;
    int v = (lit > 0) ? lit : -lit;
    assign[v] = (lit > 0) ? 1 : -1;
    trail[trail_len++] = v;
    return 1;
}

static int propagate(int qhead) {
    while (qhead < trail_len) {
        int v = trail[qhead++];
        int false_lit = (assign[v] == 1) ? -v : v;
        int li = lit_idx(false_lit);
        int prev = -1;
        int wnode = watch_head[li];
        while (wnode != -1) {
            int next_wnode = watch_next[wnode];
            int cid = wnode >> 1;
            int side = wnode & 1;
            Clause *c = &clauses[cid];
            if (!c->active) {
                if (prev == -1) watch_head[li] = next_wnode;
                else watch_next[prev] = next_wnode;
                wnode = next_wnode;
                continue;
            }
            int *lits = &lit_pool[c->lits_offset];
            /* Ensure lits[side] is false_lit */
            if (lits[side] != false_lit) {
                /* Shouldn't happen if watches maintained, swap if needed */
                int tmp = lits[0]; lits[0] = lits[1]; lits[1] = tmp;
            }
            int other = lits[1 - side];
            if (is_true(other)) {
                prev = wnode;
                wnode = next_wnode;
                continue;
            }
            /* Search for replacement watch */
            int moved = 0;
            for (int k = 2; k < c->size; ++k) {
                if (!is_false(lits[k])) {
                    int nl = lits[k];
                    lits[k] = false_lit;
                    lits[side] = nl;
                    if (prev == -1) watch_head[li] = next_wnode;
                    else watch_next[prev] = next_wnode;
                    add_watch(nl, wnode);
                    moved = 1;
                    break;
                }
            }
            if (moved) {
                wnode = next_wnode;
                continue;
            }
            /* Unit or conflict! */
            if (!enqueue(other)) return 0; /* conflict! */
            prev = wnode;
            wnode = next_wnode;
        }
    }
    return 1;
}

static int add_clause(const int *buf, int len, int base_qhead) {
    /* Deduplicate and check tautology under root assignment? Do raw dedup + tautology check */
    int tmp[4096];
    int n = 0;
    int *arr = (len <= 4096) ? tmp : (int *)malloc(len * sizeof(int));
    for (int i = 0; i < len; ++i) {
        int l = buf[i];
        int v = (l > 0) ? l : -l;
        ensure_vars(v);
        int dup = 0;
        for (int j = 0; j < n; ++j) {
            if (arr[j] == l) { dup = 1; break; }
            if (arr[j] == -l) { if (arr != tmp) free(arr); return 1; } /* tautology */
        }
        if (!dup) arr[n++] = l;
    }
    if (n == 0) {
        if (arr != tmp) free(arr);
        return 0; /* empty clause */
    }
    if (n == 1) {
        int ok = enqueue(arr[0]) && propagate(base_qhead);
        if (arr != tmp) free(arr);
        return ok ? 1 : 0;
    }
    /* Move up to two non-false literals to indices 0 and 1 */
    int placed = 0;
    for (int i = 0; i < n && placed < 2; ++i) {
        if (!is_false(arr[i])) {
            int t = arr[placed]; arr[placed] = arr[i]; arr[i] = t;
            ++placed;
        }
    }
    if (num_clauses >= cap_clauses) {
        cap_clauses = (cap_clauses == 0) ? 8192 : cap_clauses * 2;
        clauses = (Clause *)realloc(clauses, cap_clauses * sizeof(Clause));
    }
    if (cap_clauses > watch_cap_clauses) {
        watch_cap_clauses = cap_clauses;
        watch_next = (int *)realloc(watch_next, 2 * watch_cap_clauses * sizeof(int));
    }
    if (pool_len + n > pool_cap) {
        pool_cap = (pool_cap == 0) ? 65536 : pool_cap * 2;
        while (pool_cap < pool_len + n) pool_cap *= 2;
        lit_pool = (int *)realloc(lit_pool, pool_cap * sizeof(int));
    }
    int cid = num_clauses++;
    clauses[cid].size = n;
    clauses[cid].active = 1;
    clauses[cid].lits_offset = pool_len;
    memcpy(&lit_pool[pool_len], arr, n * sizeof(int));
    pool_len += n;
    add_watch(lit_pool[clauses[cid].lits_offset + 0], 2 * cid + 0);
    add_watch(lit_pool[clauses[cid].lits_offset + 1], 2 * cid + 1);
    if (arr != tmp) free(arr);

    if (placed == 0) return 0; /* falsified under root! */
    if (placed == 1) {
        int u = lit_pool[clauses[cid].lits_offset + 0];
        if (!enqueue(u) || !propagate(base_qhead)) return 0;
    }
    return 1;
}

static int read_int(FILE *fp, int *out, int *is_del) {
    int c;
    *is_del = 0;
    for (;;) {
        c = getc_unlocked(fp);
        if (c == EOF) return 0;
        if (c == 'c' || c == 'p') {
            while (c != '\n' && c != EOF) c = getc_unlocked(fp);
            continue;
        }
        if (c == 'd') {
            int nxt = getc_unlocked(fp);
            if (nxt == ' ' || nxt == '\t' || nxt == '\r' || nxt == '\n') {
                *is_del = 1;
                return 1;
            }
            ungetc(nxt, fp);
        }
        if (isspace(c)) continue;
        break;
    }
    int sign = 1;
    if (c == '-') { sign = -1; c = getc_unlocked(fp); }
    else if (c == '+') { c = getc_unlocked(fp); }
    if (!isdigit(c)) {
        fprintf(stderr, "Unexpected char '%c' in input\n", c);
        exit(2);
    }
    int val = 0;
    while (isdigit(c)) {
        val = val * 10 + (c - '0');
        c = getc_unlocked(fp);
    }
    if (c != EOF) ungetc(c, fp);
    *out = sign * val;
    return 1;
}

int main(int argc, char **argv) {
    if (argc < 3 || argc > 4 || (argc == 4 && strcmp(argv[3], "-U") != 0)) {
        fprintf(stderr, "Usage: %s <formula.cnf> <proof.rup> [-U]\n", argv[0]);
        return 2;
    }
    FILE *fcnf = fopen(argv[1], "rb");
    if (!fcnf) { perror("fopen cnf"); return 2; }
    int cap_buf = 4096, len = 0;
    int *buf = (int *)malloc(cap_buf * sizeof(int));
    int root_unsat = 0;
    int val, is_del;
    while (read_int(fcnf, &val, &is_del)) {
        if (is_del) continue;
        if (val == 0) {
            int qh = trail_len;
            if (!add_clause(buf, len, qh)) root_unsat = 1;
            len = 0;
        } else {
            if (len >= cap_buf) { cap_buf *= 2; buf = (int *)realloc(buf, cap_buf * sizeof(int)); }
            buf[len++] = val;
        }
    }
    fclose(fcnf);
    if (root_unsat) {
        printf("c trivial root UNSAT\ns VERIFIED\n");
        free(buf);
        return 0;
    }

    FILE *fprf = fopen(argv[2], "rb");
    if (!fprf) { perror("fopen proof"); free(buf); return 2; }
    len = 0;
    int del_mode = 0;
    long steps = 0;
    while (read_int(fprf, &val, &is_del)) {
        if (is_del) { del_mode = 1; len = 0; continue; }
        if (val == 0) {
            if (del_mode) {
                /* Deletion is optional in RUP soundness; ignore safely for maximal soundness! */
                del_mode = 0;
                len = 0;
                continue;
            }
            ++steps;
            /* Check RUP: assume negation of every literal in buf[0..len-1] */
            int saved_trail = trail_len;
            int conflict = 0;
            for (int i = 0; i < len; ++i) {
                int neg = -buf[i];
                int v = (neg > 0) ? neg : -neg;
                ensure_vars(v);
                if (!enqueue(neg)) { conflict = 1; break; }
            }
            if (!conflict && !propagate(saved_trail)) conflict = 1;
            /* Backtrack to saved_trail */
            while (trail_len > saved_trail) {
                int v = trail[--trail_len];
                assign[v] = 0;
            }
            if (!conflict) {
                fprintf(stderr, "RUP FAILED at step %ld (len=%d)\n", steps, len);
                fclose(fprf);
                free(buf);
                return 1;
            }
            if (len == 0) {
                printf("c %ld RUP steps\ns VERIFIED\n", steps);
                fclose(fprf);
                free(buf);
                return 0;
            }
            int qh = trail_len;
            if (!add_clause(buf, len, qh)) {
                /* Derived unit conflict at root -> next empty clause will succeed */
                printf("c %ld RUP steps (root conflict)\ns VERIFIED\n", steps);
                fclose(fprf);
                free(buf);
                return 0;
            }
            len = 0;
        } else {
            if (len >= cap_buf) { cap_buf *= 2; buf = (int *)realloc(buf, cap_buf * sizeof(int)); }
            buf[len++] = val;
        }
    }
    fclose(fprf);
    free(buf);
    fprintf(stderr, "Proof ended without deriving empty clause!\n");
    return 1;
}
