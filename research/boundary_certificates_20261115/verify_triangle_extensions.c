/* Extend one representative per geometric and palette orbit by every last row. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum { LIMIT=120, MAXN=15 };
static const int perm[6][3]={{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
static int transform[MAXN+1][6][LIMIT], side, budget, fixed_cost, apex[MAXN][MAXN];
static char base[LIMIT+1], row[MAXN];

static int index_at(int x,int y) { return x*(x-1)/2+y; }

static void prepare(int n) {
    for (int x=1; x<n; ++x) for (int y=0; y<x; ++y) {
        int bary[3]={x-y-1,y,n-x-1};
        for (int g=0; g<6; ++g) {
            int a=bary[perm[g][0]], b=bary[perm[g][1]];
            transform[n][g][index_at(x,y)]=index_at(a+b+1,b);
        }
    }
}

static void image(int n,const char *word,int g,char *out) {
    int size=index_at(n,0), seen=0;
    char map[3]={0,0,0};
    for (int i=0; i<size; ++i) {
        int c=word[transform[n][g][i]]-'0';
        if (!map[c]) map[c]=(char)('0'+seen++);
        out[i]=map[c];
    }
    out[size]=0;
}

static int rainbow_cost(int n,const char *w) {
    int rain=0;
    for (int x=1; x<n; ++x) for (int y=0; y<x; ++y)
        for (int d=1; x+d<n; ++d) {
            char a=w[index_at(x,y)],b=w[index_at(x+d,y)],c=w[index_at(x+d,y+d)];
            if (a==b && a==c) return -1;
            rain+=a!=b && a!=c && b!=c;
        }
    return rain;
}

static void extend(int pos,int cost) {
    if (pos==side) {
        char word[LIMIT+1], best[LIMIT+1], candidate[LIMIT+1];
        memcpy(word,base,index_at(side,0));
        memcpy(word+index_at(side,0),row,side);
        image(side+1,word,0,best);
        for (int g=1; g<6; ++g) {
            image(side+1,word,g,candidate);
            if (strcmp(candidate,best)<0) strcpy(best,candidate);
        }
        printf("%d %s\n",cost,best);
        return;
    }
    for (char color='0'; color<='2'; ++color) {
        int next=cost, valid=1;
        for (int i=0; i<pos; ++i) {
            int a=apex[i][pos], b=row[i];
            if (a==b && b==color) { valid=0; break; }
            next+=a!=b && a!=color && b!=color;
        }
        if (valid && next<=budget) { row[pos]=color; extend(pos+1,next); }
    }
}

int main(int argc,char **argv) {
    if (argc!=3) return 2;
    side=atoi(argv[1]); budget=atoi(argv[2]);
    if(side<4 || side>=MAXN || budget<0) return 2;
    prepare(side); prepare(side+1);
    char input[LIMIT+4];
    while (fgets(input,sizeof(input),stdin)) {
        input[strcspn(input,"\r\n")]=0;
        if ((int)strlen(input)!=index_at(side,0) || strspn(input,"012")!=strlen(input)) return 2;
        fixed_cost=rainbow_cost(side,input);
        if (fixed_cost<0) return 3;
        if (fixed_cost>budget) continue;
        char seen[6][LIMIT+1];
        for (int g=0; g<6; ++g) {
            image(side,input,g,base);
            int same=0;
            for (int h=0; h<g; ++h) if (strcmp(seen[h],base)==0) same=1;
            strcpy(seen[g],base);
            if (same) continue;
            for (int i=0; i<side; ++i) for (int j=i+1; j<side; ++j)
                apex[i][j]=base[index_at(side-(j-i),i)];
            extend(0,fixed_cost);
        }
    }
    return ferror(stdin) || ferror(stdout);
}
