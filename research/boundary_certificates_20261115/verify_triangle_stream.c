/* Enumerate boundary extensions without storing intermediate orbit catalogs.
   Input words are canonical under geometry and palette. Each output has a
   unique parent obtained by deleting its first eligible oriented last row. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum { MAX_SIDE = 15, MAX_CELLS = MAX_SIDE * (MAX_SIDE - 1) / 2, MAX_BUDGET = 63 };
static const int perm[6][3] = {
    {0,1,2}, {0,2,1}, {1,0,2}, {1,2,0}, {2,0,1}, {2,1,0}
};
static int image_index[MAX_SIDE+1][6][MAX_CELLS], last_face[6];
static int first, first_budget, target, save_from;
static uint64_t histogram[MAX_SIDE+1][MAX_BUDGET+1];

typedef struct {
    char word[MAX_CELLS+1], images[6][MAX_CELLS+1], apex[MAX_SIDE][MAX_SIDE];
    int parent_cost;
} Layer;
static Layer layer[MAX_SIDE+1];

static int index_at(int x, int y) {
    return x*(x-1)/2+y;
}

static void prepare(void) {
    for (int g=0; g<6; ++g) {
        for (int j=0; j<3; ++j)
            if (perm[g][j]==2) last_face[g]=1<<j;
        for (int n=3; n<=target; ++n) {
            for (int x=1; x<n; ++x) for (int y=0; y<x; ++y) {
                int t[3]={x-y-1,y,n-1-x};
                int a=t[perm[g][0]], b=t[perm[g][1]];
                image_index[n][g][index_at(x,y)]=index_at(1+a+b,b);
            }
        }
    }
}

static void orient(int n, const char *word, int g, char *out) {
    char labels[3]={0}, next='0';
    int size=index_at(n,0);
    for (int i=0; i<size; ++i) {
        int color=word[image_index[n][g][i]]-'0';
        if (!labels[color]) labels[color]=next++;
        out[i]=labels[color];
    }
    out[size]=0;
}

static int inspect(int n, const char *word, int *faces) {
    int cost=0;
    *faces=0;
    for (int x=1; x<n; ++x) for (int y=0; y<x; ++y) for (int d=1; x+d<n; ++d) {
        char a=word[index_at(x,y)], b=word[index_at(x+d,y)], c=word[index_at(x+d,y+d)];
        if (a==b && b==c) return -1;
        if (a!=b && b!=c && c!=a) {
            ++cost;
            if (x-y==1) *faces |= 1;
            if (y==0) *faces |= 2;
            if (x+d==n-1) *faces |= 4;
        }
    }
    return cost;
}

static void visit(int n, const char *word, int cost, int faces);

static void finish_row(int n, int cost, int faces) {
    Layer *current=&layer[n];
    if (cost==current->parent_cost) return;
    current->word[index_at(n+1,0)]=0;
    char candidate[MAX_CELLS+1], best[MAX_CELLS+1];
    strcpy(best,current->word);
    for (int g=1; g<6; ++g) {
        orient(n+1,current->word,g,candidate);
        if ((faces & last_face[g]) && strcmp(candidate,current->word)<0) return;
        if (strcmp(candidate,best)<0) strcpy(best,candidate);
    }
    int canonical_faces;
    if (inspect(n+1,best,&canonical_faces)!=cost) exit(4);
    visit(n+1,best,cost,canonical_faces);
}

static void append_row(int n, int pos, int cost, int faces, int quota) {
    if (pos==n) {
        finish_row(n,cost,faces);
        return;
    }
    Layer *current=&layer[n];
    int base=index_at(n,0);
    for (char color='0'; color<='2'; ++color) {
        int new_cost=cost, new_faces=faces, valid=1;
        for (int i=0; i<pos; ++i) {
            char a=current->apex[i][pos], b=current->word[base+i];
            if (a==b && b==color) { valid=0; break; }
            if (a!=b && b!=color && color!=a) {
                if (++new_cost>quota) { valid=0; break; }
                new_faces |= 4;
                if (i==0) new_faces |= 2;
                if (pos==n-1) new_faces |= 1;
            }
        }
        if (valid) {
            current->word[base+pos]=color;
            append_row(n,pos+1,new_cost,new_faces,quota);
        }
    }
}

static void visit(int n, const char *word, int cost, int faces) {
    ++histogram[n][cost];
    if (n>=save_from) printf("%d %d %s\n",n,cost,word);
    if (n==target) return;
    Layer *current=&layer[n];
    current->parent_cost=cost;
    for (int g=0; g<6; ++g) {
        char *image=current->images[g];
        orient(n,word,g,image);
        int duplicate=0;
        for (int k=0; k<g; ++k) if (strcmp(current->images[k],image)==0) duplicate=1;
        if (duplicate) continue;
        strcpy(current->word,image);
        int oriented_faces=0;
        for (int j=0; j<3; ++j) if (faces & (1<<j)) oriented_faces |= 1<<perm[g][j];
        for (int i=0; i<n; ++i) for (int j=i+1; j<n; ++j)
            current->apex[i][j]=image[index_at(n-(j-i),i)];
        /* The old last row is interior in the child. The two lateral faces persist. */
        append_row(n,0,cost,oriented_faces & 3,first_budget+n+1-first);
    }
}

int main(int argc, char **argv) {
    if (argc!=5) return 2;
    first=atoi(argv[1]); first_budget=atoi(argv[2]); target=atoi(argv[3]); save_from=atoi(argv[4]);
    if (first<5 || target<first || target>MAX_SIDE || first_budget<0 ||
        first_budget+target-first>MAX_BUDGET) return 2;
    prepare();
    char word[MAX_CELLS+4];
    while (fgets(word,sizeof(word),stdin)) {
        word[strcspn(word,"\r\n")]=0;
        if ((int)strlen(word)!=index_at(first,0) || strspn(word,"012")!=strlen(word)) return 2;
        int faces, cost=inspect(first,word,&faces);
        if (cost<0 || cost>first_budget) return 3;
        visit(first,word,cost,faces);
    }
    for (int n=first; n<=target; ++n) for (int k=0; k<=MAX_BUDGET; ++k)
        if (histogram[n][k]) fprintf(stderr,"%d %d %llu\n",n,k,(unsigned long long)histogram[n][k]);
    return ferror(stdin) || ferror(stdout) || ferror(stderr);
}
