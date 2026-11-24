/* A sharp two-word inequality for twelve neighboring four-color shifts.
   Compile with cc -std=c99 -O2. No solver or certificate file is needed. */
#include <stdio.h>
#include <stdlib.h>

enum { WIDTH = 12, COLORS = 4, QUOTA = 3 };
static int word[WIDTH], count;

static int row_max(const int row[COLORS]) {
    int m = row[0];
    for (int c = 1; c < COLORS; ++c) if (row[c] > m) m = row[c];
    return m;
}

static int objective(int bill, int votes[WIDTH][COLORS]) {
    for (int j = 0; j < WIDTH; ++j) bill += row_max(votes[j]);
    return bill;
}

/* A priced (s,c) contributes at most three selected matches. An unpriced
   match at (i,j) votes for its first-word color in column j. The second
   word supplies just one color per column. Any pricing gives an upper bound. */
static int at_most_48(void) {
    int votes[WIDTH][COLORS] = {{0}}, prefix[WIDTH+1][COLORS] = {{0}};
    int priced[WIDTH+1][COLORS] = {{0}}, bill = 0;
    int uncapped = 0, by_quota = 0;
    for (int j = 0; j < WIDTH; ++j) {
        for (int c = 0; c < COLORS; ++c) prefix[j+1][c] = prefix[j][c];
        ++prefix[j+1][word[j]];
        for (int c = 0; c < COLORS; ++c) {
            votes[j][c] = prefix[j+1][c];
            by_quota += prefix[j+1][c] < QUOTA ? prefix[j+1][c] : QUOTA;
        }
        uncapped += row_max(votes[j]);
    }
    if (uncapped <= 48 || by_quota <= 48) return 1;
    int best = uncapped;
    for (int round = 0; round < 6; ++round) {
        int moved = 0;
        for (int s = WIDTH; s >= 1; --s) {
            for (int c = 0; c < COLORS; ++c) {
                if (prefix[s][c] <= QUOTA) continue;
                int h = WIDTH-s, direction = priced[s][c] ? -1 : 1;
                for (int i = 0; i < s; ++i)
                    if (word[i] == c) votes[h+i][c] -= direction;
                int next = objective(bill+QUOTA*direction, votes);
                if (next < best || (round <= 1 && next == best && direction == 1)) {
                    bill += QUOTA*direction;
                    priced[s][c] += direction;
                    best = next;
                    moved = 1;
                    if (best <= 48) return 1;
                } else {
                    for (int i = 0; i < s; ++i)
                        if (word[i] == c) votes[h+i][c] += direction;
                }
            }
        }
        if (!moved) break;
    }
    return 0;
}

static int exact_score(const int *second) {
    int total = 0;
    for (int s = 1; s <= WIDTH; ++s) {
        int f[COLORS] = {0};
        for (int i = 0; i < s; ++i)
            if (word[i] == second[WIDTH-s+i]) ++f[word[i]];
        for (int c = 0; c < COLORS; ++c) total += f[c] < QUOTA ? f[c] : QUOTA;
    }
    return total;
}

static void visit(int j, int highest) {
    if (j == WIDTH) {
        ++count;
        if (!at_most_48()) {
            fprintf(stderr, "No upper certificate for first word ");
            for (int i = 0; i < WIDTH; ++i) fprintf(stderr, "%d", word[i]);
            fputc('\n', stderr);
            exit(1);
        }
        return;
    }
    for (int c = 0; c < COLORS && c <= highest+1; ++c) {
        word[j] = c;
        visit(j+1, c > highest ? c : highest);
    }
}

int main(void) {
    visit(0, -1);
    int second[WIDTH];
    for (int i = 0; i < WIDTH; ++i) {
        word[i] = i >= 3;
        second[i] = i >= 9;
    }
    int attained = exact_score(second);
    if (count != 700075 || attained != 48) return 1;
    printf("%d first words, arbitrary second word. Maximum %d of 78.\n", count, attained);
    return 0;
}
