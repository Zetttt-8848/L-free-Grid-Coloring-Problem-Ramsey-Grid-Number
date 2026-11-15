/* Enumerate proper triangle colorings with a specified set of new rainbow corners.
   Reference modes: all, shell, or a literal coloring. The optional final
   argument list emits witnesses. In shell or free mode, stream [PREFIX]
   emits each canonical word once on stdout and the branch statistics on stderr. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum { MAX_CELLS=110, MAX_EDGES=460, MAX_INC=45, QUEUE=512 };
enum { EXACTLY_TWO, PROPER, RAINBOW };
static int shell_mode, budget, list_all, stream, interior[MAX_EDGES];
static int global_mode, orbit_weight=1, coord_x[MAX_CELLS],coord_y[MAX_CELLS];
static int edge_id[16][16][16], symmetry[6][MAX_EDGES];
static int cell_count, edge_count, vertices[MAX_EDGES][3], index_at[16][16];
static int incident[MAX_CELLS][MAX_INC], degree[MAX_CELLS];
static int reference[MAX_CELLS], old_rain[MAX_EDGES], rule[MAX_EDGES];
static unsigned char support[3][8][8][8][3], colors[MAX_CELLS];
static int edited[3*MAX_CELLS], old_domain[3*MAX_CELLS], edit_count;
static int pending[QUEUE], queued[MAX_EDGES], head, tail;
static unsigned long long histogram[MAX_EDGES], visits, cases;

static int color_count(int mask) {
    return (mask&1)+((mask>>1)&1)+((mask>>2)&1);
}

static void prepare_supports(void) {
    for (int type=0; type<3; ++type)
        for (int a=1; a<8; ++a) for (int b=1; b<8; ++b) for (int c=1; c<8; ++c)
            for (int x=0; x<3; ++x) if (a&(1<<x))
                for (int y=0; y<3; ++y) if (b&(1<<y))
                    for (int z=0; z<3; ++z) if (c&(1<<z)) {
                        int k=color_count((1<<x)|(1<<y)|(1<<z));
                        if (k<2 || (type==EXACTLY_TWO && k!=2) || (type==RAINBOW && k!=3)) continue;
                        unsigned char *out=support[type][a][b][c];
                        out[0]|=1<<x; out[1]|=1<<y; out[2]|=1<<z;
                    }
}

static void prepare_triangle(int side, const char *word) {
    for (int x=1; x<side; ++x) for (int y=0; y<x; ++y) {
        index_at[x][y]=cell_count;
        coord_x[cell_count]=x; coord_y[cell_count]=y;
        reference[cell_count]=global_mode ? 0 : word[cell_count]-'0';
        ++cell_count;
    }
    for (int x=1; x<side; ++x) for (int y=0; y<x; ++y)
        for (int d=1; x+d<side; ++d) {
            edge_id[x][y][d]=edge_count;
            int *v=vertices[edge_count];
            v[0]=index_at[x][y]; v[1]=index_at[x+d][y]; v[2]=index_at[x+d][y+d];
            int mask=0;
            for (int j=0; j<3; ++j) {
                incident[v[j]][degree[v[j]]++]=edge_count;
                mask|=1<<reference[v[j]];
            }
            if (!global_mode && color_count(mask)<2) { fprintf(stderr,"Improper reference coloring\n"); exit(2); }
            old_rain[edge_count++]=(color_count(mask)==3);
        }
}

static void prepare_symmetry(int side) {
    const int order[6][3]={{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
    for (int s=0; s<6; ++s) for (int e=0; e<edge_count; ++e) {
        int low=side, high=0, base_y=0;
        for (int j=0; j<3; ++j) {
            int v=vertices[e][j],x=coord_x[v],y=coord_y[v];
            int bary[3]={x-y-1,y,side-x-1};
            int yy=bary[order[s][1]],xx=1+yy+bary[order[s][0]];
            if (xx<low) { low=xx; base_y=yy; }
            if (xx>high) high=xx;
        }
        symmetry[s][e]=edge_id[low][base_y][high-low];
    }
}

/* Every orbit is searched at its lexicographically least support. */
static int support_orbit(int first,int second,int third) {
    if (!global_mode || first<0) return 1;
    int members[3]={first,second,third};
    int count=third>=0 ? 3 : (second>=0 ? 2 : 1);
    int keys[6], distinct=0;
    for (int s=0; s<6; ++s) {
        int a[3]={0,0,0},key=0;
        for (int j=0; j<count; ++j) {
            a[j]=symmetry[s][members[j]];
            for (int k=j; k>0 && a[k]<a[k-1]; --k) {
                int v=a[k]; a[k]=a[k-1]; a[k-1]=v;
            }
        }
        for (int j=0; j<count; ++j) key=512*key+a[j];
        if (s && key<keys[0]) return 0;
        int i=0;
        while (i<distinct && keys[i]!=key) ++i;
        if (i==distinct) keys[distinct++]=key;
    }
    return distinct;
}

static void restrict_domain(int v, int mask) {
    edited[edit_count]=v;
    old_domain[edit_count++]=colors[v];
    colors[v]=mask;
    for (int i=0; i<degree[v]; ++i) {
        int edge=incident[v][i];
        if (!queued[edge]) {
            queued[edge]=1;
            pending[tail++%QUEUE]=edge;
        }
    }
}

static int propagate_domains(void) {
    while (head<tail) {
        int edge=pending[head++%QUEUE];
        queued[edge]=0;
        int *v=vertices[edge];
        const unsigned char *allowed=support[rule[edge]][colors[v[0]]][colors[v[1]]][colors[v[2]]];
        if (!allowed[0]) return 0;
        for (int j=0; j<3; ++j)
            if (colors[v[j]]!=allowed[j]) restrict_domain(v[j],allowed[j]);
    }
    return 1;
}

/* If the forced interior rainbows exhaust the quota, every other corner
   must still admit two colors. Revisit any shortened domains. */
static int propagate(void) {
    for (;;) {
        if (!propagate_domains()) return 0;
        if (!shell_mode) return 1;
        int forced=0;
        for (int e=0; e<edge_count; ++e) if (interior[e]) {
            int *v=vertices[e];
            if (!support[EXACTLY_TWO][colors[v[0]]][colors[v[1]]][colors[v[2]]][0]) ++forced;
        }
        if (forced>budget) return 0;
        if (forced<budget) return 1;
        for (int e=0; e<edge_count; ++e) if (interior[e]) {
            int *v=vertices[e];
            const unsigned char *ok=support[EXACTLY_TWO][colors[v[0]]][colors[v[1]]][colors[v[2]]];
            if (!ok[0]) continue;
            for (int j=0; j<3; ++j) if (ok[j]!=colors[v[j]]) restrict_domain(v[j],ok[j]);
        }
        if (head==tail) return 1;
    }
}

static void restore(int size) {
    while (head<tail) queued[pending[head++%QUEUE]]=0;
    head=tail=0;
    while (edit_count>size) {
        --edit_count;
        colors[edited[edit_count]]=old_domain[edit_count];
    }
}

/* The list output collapses both the geometric and palette symmetries. */
static int cell_image[6][MAX_CELLS];
static void prepare_cell_images(int side) {
    const int order[6][3]={{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
    for (int v=0; v<cell_count; ++v) for (int g=0; g<6; ++g) {
        int x=coord_x[v],y=coord_y[v],bary[3]={x-y-1,y,side-x-1};
        int a=bary[order[g][0]],b=bary[order[g][1]];
        cell_image[g][v]=index_at[1+a+b][b];
    }
}

static void emit_witness(void) {
    char best[MAX_CELLS+1]={0}, word[MAX_CELLS+1];
    for (int g=0; g<6; ++g) {
        char labels[8]={0},next='0';
        for (int v=0; v<cell_count; ++v) {
            int color=colors[cell_image[g][v]];
            if (!labels[color]) labels[color]=next++;
            word[v]=labels[color];
        }
        word[cell_count]=0;
        if (!g || strcmp(word,best)<0) strcpy(best,word);
    }
    if (stream) {
        for (int v=0; v<cell_count; ++v) {
            int digit=colors[v]==1 ? 0 : (colors[v]==2 ? 1 : 2);
            if (best[v]!='0'+digit) return;
        }
        puts(best);
    } else {
        fprintf(stderr,"witness %s\n",best);
    }
}

static void count_colorings(void) {
    ++visits;
    if (!propagate()) return;
    int chosen=-1, highest=-100000;
    for (int i=0; i<cell_count; ++i) {
        int k=color_count(colors[i]);
        if (k==1) continue;
        int priority=-10000*k+degree[i];
        for (int j=0; j<degree[i]; ++j) {
            int *p=vertices[incident[i][j]];
            int sum=color_count(colors[p[0]])+color_count(colors[p[1]])+color_count(colors[p[2]]);
            if (sum<=5) priority+=40;
            else if (sum==6) priority+=12;
            else if (sum==7) priority+=3;
        }
        if (priority>highest) { highest=priority; chosen=i; }
    }
    if (chosen<0) {
        int count=0;
        for (int e=0; e<edge_count; ++e) {
            int *v=vertices[e];
            int distinct=color_count(colors[v[0]]|colors[v[1]]|colors[v[2]]);
            if (distinct<2 || (rule[e]==EXACTLY_TWO && distinct!=2)
                           || (rule[e]==RAINBOW && distinct!=3)) exit(3);
            count+=distinct==3;
        }
        if (global_mode && (list_all || !histogram[count])) emit_witness();
        histogram[count]+=orbit_weight;
        return;
    }
    int original=colors[chosen],checkpoint=edit_count;
    for (int bit=1; bit<=4; bit<<=1) if (original&bit) {
        restrict_domain(chosen,bit);
        count_colorings();
        restore(checkpoint);
    }
}

static void enumerate_case(int first, int second, int third) {
    orbit_weight=support_orbit(first,second,third);
    if (!orbit_weight) return;
    for (int e=0; e<edge_count; ++e) rule[e]=old_rain[e]?PROPER:EXACTLY_TWO;
    memset(colors,7,cell_count);
    if (first<0) {
        restrict_domain(0,1);
    } else {
        rule[first]=RAINBOW;
        if (second>=0) rule[second]=RAINBOW;
        if (third>=0) rule[third]=RAINBOW;
        for (int j=0; j<3; ++j) restrict_domain(vertices[first][j],1<<j);
    }
    cases+=orbit_weight;
    count_colorings();
    restore(0);
}

int main(int argc,char **argv) {
    if (argc<6 || argc>8) return 2;
    stream=argc>=7 && strcmp(argv[6],"stream")==0;
    list_all=stream || (argc==7 && strcmp(argv[6],"list")==0);
    if (argc>=7 && !list_all) return 2;
    int side=atoi(argv[1]), number=atoi(argv[3]), lo=atoi(argv[4]), hi=atoi(argv[5]);
    int unrestricted=strcmp(argv[2],"free")==0;
    shell_mode=unrestricted || strcmp(argv[2],"shell")==0;
    global_mode=shell_mode || strcmp(argv[2],"all")==0;
    if (side<5 || side>15 || number<0 || (!shell_mode && number>3) || lo<0 || hi<lo) return 2;
    if (stream && !shell_mode) return 2;
    if (!global_mode && ((int)strlen(argv[2])!=side*(side-1)/2 ||
        strspn(argv[2],"012")!=strlen(argv[2]))) return 2;
    prepare_supports();
    prepare_triangle(side,argv[2]);
    if (global_mode) prepare_cell_images(side);
    if (shell_mode) {
        budget=number;
        for (int e=0; e<edge_count; ++e) {
            interior[e]=1;
            for (int j=0; j<3; ++j) {
                int v=vertices[e][j], x=coord_x[v], y=coord_y[v];
                if (x-y==1 || y==0 || x==side-1) interior[e]=0;
            }
            if (unrestricted) interior[e]=1;
            rule[e]=interior[e]?PROPER:EXACTLY_TWO;
        }
        memset(colors,7,cell_count);
        restrict_domain(0,1);
        restrict_domain(1,3);
        if (argc==8) {
            int length=(int)strlen(argv[7]);
            if (length>cell_count-2 || strspn(argv[7],"012")!=(size_t)length) return 2;
            for (int i=0; i<length; ++i) restrict_domain(i+2,1<<(argv[7][i]-'0'));
        }
        count_colorings();
        cases=1;
    } else {
        if (global_mode) prepare_symmetry(side);
        int outside[MAX_EDGES], total=0;
        for (int e=0; e<edge_count; ++e) if (!old_rain[e]) outside[total++]=e;
        if (number==0) enumerate_case(-1,-1,-1);
        else for (int i=lo; i<=hi && i<total; ++i) {
            if (number==1) enumerate_case(outside[i],-1,-1);
            else for (int j=i+1; j<total; ++j) {
                if (number==2) enumerate_case(outside[i],outside[j],-1);
                else for (int k=j+1; k<total; ++k) enumerate_case(outside[i],outside[j],outside[k]);
            }
        }
    }
    FILE *stats=stream ? stderr : stdout;
    fprintf(stats,"%llu %llu",cases,visits);
    for (int i=0; i<=edge_count; ++i) if (histogram[i]) fprintf(stats," %d:%llu",i,histogram[i]);
    fputc('\n',stats);
    return ferror(stats) || (stream && ferror(stdout));
}
