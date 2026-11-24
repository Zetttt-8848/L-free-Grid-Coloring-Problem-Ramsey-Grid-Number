/* Exhaustive test for the three-color modular-affine family on the 21-square.
   Build with a GCC or Clang target supporting unsigned 128-bit integers. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned __int128 Mask;
static Mask third[128][128], neighbors[128], all_residues;
static int modulus, incidence[128];
static unsigned long long nodes;

static int first_bit(Mask bits) {
    uint64_t low=(uint64_t)bits;
    return low ? __builtin_ctzll(low) : 64+__builtin_ctzll((uint64_t)(bits>>64));
}
static int size(Mask bits) {
    return __builtin_popcountll((uint64_t)bits)+__builtin_popcountll((uint64_t)(bits>>64));
}
static int gcd(int a,int b) {
    while (b) { int r=a%b; a=b; b=r; }
    return a;
}

static int build(int m,int a,int b) {
    memset(third,0,sizeof third);
    memset(neighbors,0,sizeof neighbors);
    memset(incidence,0,sizeof incidence);
    modulus=m;
    all_residues=m==128 ? ~(Mask)0 : (((Mask)1<<m)-1);
    for (int d=1; d<21; ++d)
        for (int x=0; x<21-d; ++x) for (int y=0; y<21-d; ++y) {
            int u=(a*x+b*y)%m, v=(u+a*d)%m, w=(v+b*d)%m;
            if (u==v && v==w) return 0;
            if (u==v || v==w || u==w) {
                int other=(u!=v ? v : w);
                neighbors[u]|=(Mask)1<<other;
                neighbors[other]|=(Mask)1<<u;
            } else {
                int t[3]={u,v,w};
                for (int j=0; j<3; ++j) {
                    int left=t[j], right=t[(j+1)%3], last=t[(j+2)%3];
                    third[left][right]|=(Mask)1<<last;
                    third[right][left]|=(Mask)1<<last;
                }
            }
        }
    for (int i=0; i<m; ++i) {
        incidence[i]=10*size(neighbors[i]);
        for (int j=0; j<m; ++j) incidence[i]+=size(third[i][j]);
    }
    return 1;
}

typedef struct {
    Mask assigned[3], allowed[3], uncolored;
} State;

static void assign(State *s,int v,int color) {
    Mask forbidden=neighbors[v], previous=s->assigned[color], bit=(Mask)1<<v;
    while (previous) {
        int u=first_bit(previous);
        previous&=previous-1;
        forbidden|=third[v][u];
    }
    s->assigned[color]|=bit;
    s->allowed[color]&=~forbidden;
    s->uncolored^=bit;
}

static int colorable(State s) {
    ++nodes;
    while (s.uncolored) {
        Mask a=s.allowed[0], b=s.allowed[1], c=s.allowed[2];
        if (s.uncolored & ~(a|b|c)) return 0;
        Mask forced=s.uncolored & ~((a&b)|(b&c)|(a&c));
        if (forced) {
            int v=first_bit(forced);
            Mask bit=(Mask)1<<v;
            assign(&s,v,(a&bit)?0:((b&bit)?1:2));
            continue;
        }
        Mask choices=s.uncolored & ~(a&b&c);
        if (!choices) choices=s.uncolored;
        int selected=-1, best_score=-1;
        while (choices) {
            int v=first_bit(choices);
            choices&=choices-1;
            int score=incidence[v]+2*size(neighbors[v]&s.uncolored);
            if (score>best_score) { best_score=score; selected=v; }
        }
        Mask bit=(Mask)1<<selected;
        int tried_new=0;
        for (int color=0; color<3; ++color) {
            if (!(s.allowed[color]&bit)) continue;
            if (!s.assigned[color] && tried_new) continue;
            if (!s.assigned[color]) tried_new=1;
            State child=s;
            assign(&child,selected,color);
            if (colorable(child)) return 1;
        }
        return 0;
    }
    return 1;
}

int main(int argc,char **argv) {
    if (argc!=1 && argc!=3) return 2;
    int lo=(argc==3 ? atoi(argv[1]) : 21);
    int hi=(argc==3 ? atoi(argv[2]) : 128);
    if (lo<21 || hi>128 || lo>hi) return 2;
    unsigned long long pairs=0, orbits=0, sum=0;
    for (int m=lo; m<=hi; ++m) {
        unsigned char done[128][128]={{0}};
        int count=0;
        for (int a=0; a<m; ++a) for (int b=0; b<m; ++b) {
            if (gcd(gcd(a,b),m)!=1) continue;
            ++pairs;
            if (done[a][b]) continue;
            for (int u=1; u<m; ++u) if (gcd(u,m)==1) {
                int left=(a*u)%m, right=(b*u)%m;
                done[left][right]=done[right][left]=1;
            }
            ++count; ++orbits; nodes=0;
            if (build(m,a,b)) {
                State initial={{0,0,0},{all_residues,all_residues,all_residues},all_residues};
                assign(&initial,0,0);
                if (colorable(initial)) {
                    printf("Colorable projection at %d %d %d\n",m,a,b);
                    return 1;
                }
            }
            sum+=nodes;
        }
        printf("m=%d, %d orbits\n",m,count);
        fflush(stdout);
    }
    printf("Excluded %llu primitive pairs in %llu orbits, %llu nodes.\n",pairs,orbits,sum);
    return 0;
}
