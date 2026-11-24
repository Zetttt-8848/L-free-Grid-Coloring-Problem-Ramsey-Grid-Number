/* Check whether a disjunction system has a solution with at most K true edits. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

enum { CELLS = 441, MAX_CLAUSES = 18000, MAX_LENGTH = 256, WORDS = 7 };
static int budget, clause_count;
static int length[MAX_CLAUSES], literals[MAX_CLAUSES][MAX_LENGTH];
static int satisfied[MAX_CLAUSES], violation_slot[MAX_CLAUSES];
static int violations[MAX_CLAUSES], violation_count;
static int *occurrences[CELLS], occurrence_count[CELLS];
/* An available edit is 0, an applied edit is 1, an excluded earlier choice is -1. */
static int edit_state[CELLS];
static unsigned long long nodes;

static void add_violation(int clause) {
    violation_slot[clause] = violation_count;
    violations[violation_count++] = clause;
}

static void remove_violation(int clause) {
    int position = violation_slot[clause];
    int moved = violations[--violation_count];
    violations[position] = moved;
    violation_slot[moved] = position;
}

static void change_edit(int cell, int direction) {
    for (int j = 0; j < occurrence_count[cell]; ++j) {
        int occurrence = occurrences[cell][j];
        int clause = abs(occurrence) - 1;
        int delta = occurrence > 0 ? direction : -direction;
        if (satisfied[clause] == 0) remove_violation(clause);
        satisfied[clause] += delta;
        if (satisfied[clause] == 0) add_violation(clause);
    }
}

static int possible(int remaining) {
    ++nodes;
    if (violation_count == 0) return 1;
    if (remaining == 0) return 0;
    int selected = -1, smallest = MAX_LENGTH + 1, packed = 0;
    uint64_t covered[WORDS] = {0};
    for (int index = 0; index < violation_count; ++index) {
        int clause = violations[index], available = 0, overlaps = 0;
        for (int j = 0; j < length[clause]; ++j) {
            int cell = abs(literals[clause][j]) - 1;
            if (edit_state[cell]) continue;
            ++available;
            if ((covered[cell/64] >> (cell%64)) & 1) overlaps = 1;
        }
        if (!available) return 0;
        if (available < smallest) {
            smallest = available;
            selected = clause;
        }
        /* Pairwise disjoint violated clauses need different additional edits. */
        if (!overlaps) {
            if (++packed > remaining) return 0;
            for (int j = 0; j < length[clause]; ++j) {
                int cell = abs(literals[clause][j]) - 1;
                if (!edit_state[cell]) covered[cell/64] |= UINT64_C(1) << (cell%64);
            }
        }
    }
    int choices[MAX_LENGTH], count = 0;
    for (int j = 0; j < length[selected]; ++j) {
        int cell = abs(literals[selected][j]) - 1;
        if (!edit_state[cell]) choices[count++] = cell;
    }
    /* Partition all continuations by their first edit among these choices. */
    for (int j = 0; j < count; ++j) {
        int cell = choices[j];
        edit_state[cell] = 1;
        change_edit(cell, 1);
        if (possible(remaining-1)) return 1;
        change_edit(cell, -1);
        edit_state[cell] = -1;
    }
    for (int j = 0; j < count; ++j) edit_state[choices[j]] = 0;
    return 0;
}

int main(int argc, char **argv) {
    if (argc != 2) return 2;
    FILE *input = fopen(argv[1], "r");
    if (!input) return 2;
    if (fscanf(input,"%d%d",&budget,&clause_count)!=2 || budget<0 || budget>CELLS
        || clause_count<1 || clause_count>MAX_CLAUSES) return 2;
    for (int c=0; c<clause_count; ++c) {
        unsigned char seen[CELLS] = {0};
        if (fscanf(input,"%d",&length[c])!=1 || length[c]<1 || length[c]>MAX_LENGTH) return 2;
        for (int j=0; j<length[c]; ++j) {
            int v;
            if (fscanf(input,"%d",&v)!=1 || v==0 || v < -CELLS || v > CELLS) return 2;
            int cell = abs(v)-1;
            if (seen[cell]) return 2;
            seen[cell] = 1;
            literals[c][j] = v;
            ++occurrence_count[cell];
            if (v<0) ++satisfied[c];
        }
        if (satisfied[c]==0) add_violation(c);
    }
    for (int cell=0; cell<CELLS; ++cell) {
        occurrences[cell] = malloc((occurrence_count[cell]+1)*sizeof(int));
        if (!occurrences[cell]) return 2;
        occurrence_count[cell]=0;
    }
    for (int c=0; c<clause_count; ++c)
        for (int j=0; j<length[c]; ++j) {
            int v=literals[c][j], cell=abs(v)-1;
            occurrences[cell][occurrence_count[cell]++] = v>0 ? c+1 : -c-1;
        }
    fclose(input);
    int found = possible(budget);
    printf("%s budget %d, %d clauses, %llu nodes\n",
           found ? "SAT" : "UNSAT",budget,clause_count,nodes);
    return found;
}
