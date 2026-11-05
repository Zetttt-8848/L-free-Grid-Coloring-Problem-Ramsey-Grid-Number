# An algebraic obstruction on eight source marks

Root derivation, R4-RESEARCH-0014. This completes the local development
example for ordered completion duality. The example was already present
in the inherited minimal-bad-support catalog; the result here is a new
explicit derivation through cancelling pair polynomials. It is not a new
small-color Ramsey bound or a claim of historical priority.

**Theorem.** Let

    A={0,1,2,3,4,6,7,8}.

The strict triangle V(A)={(v,u):u,v in A,u<v} has no proper two-coloring
for positive equal-step corners. The same holds for any integer source
containing t+qA, where t is an integer and q is a positive integer.

The proof below uses the fixed integer polynomials in
`PAIR_POLYNOMIAL_TABLE_0014.md`. That file gives both their complete
coefficient lists and their defining cancelling transfers. All local
inequalities used here are derived algebraically below or in the cited
four-line auxiliary derivation. Neither a solver status nor a floating
value is a premise of the theorem.

## 1. Sign identities available under the contrary assumption

Suppose z:V(A)->{-1,+1} is proper. For three signs abbreviate

    K(a,b,c)=ab+ac+bc.

For any k signs, more generally write K(S) for the sum of pair products
on the k-element list S. The elementary square identity gives

    K(S)=((sum_{s in S}s)^2-k)/2 >= -floor(k/2).           (1)

In particular K(a,b,c)>=-1 for arbitrary signs. If the signs belong to
a proper two-colored triple, their sum is +1 or -1, and

    K(a,b,c)=-1.                                        (2)

We use (2) for three kinds of triples, with different justifications.

First, every original positive corner is proper by assumption.

Second, three equally spaced cells on one offset diagonal are proper.
Indeed, take starts x,x+h,x+2h in F_d. If their signs were all s, their
two adjacent-pair completions and their extreme-pair completion would
all have sign -s. Those three completions form a positive corner of step
h, a contradiction. Hence

    K(z_d(x),z_d(x+h),z_d(x+2h))=-1.                    (3)

This is the three-progression consequence of the inherited signed-fiber
Golomb condition, with its direct argument supplied here.

Third, when the source contains

    x,x+h,x+2h,x+d,x+d+h,x+d+2h,                         (4)

the reflected triple

    (x+d+h,x), (x+d+h,x+h), (x+d+2h,x+h)                (5)

is proper as well. Here is the direct source-specific forcing argument.
If the three cells in (5) have color s, the original corner with left
cell (x+d,x) forces that left cell to -s. The original corner with right
cell (x+d+2h,x+2h) forces that right cell to -s. Their common offset is
d, so they force (x+d+2h,x) to s. The first and last cells of (5) have
common offset d+h and both color s, so they force that same completion
to -s. This contradiction proves (2) for (5).

This last implication uses all the supporting marks in (4); it does not
change the problem's orientation convention or exclude arbitrary
reflected corners without those marks. The more general ordered-switch
inequality is derived in `ORDERED_SWITCH_INEQUALITY_0014.md`.

## 2. The cancelling polynomial family

The companion table defines a polynomial P_F for each nonzero line or
completion-block factor. A transfer entry (F,G,p,q,c) adds the exact term
c*z_p*z_q to P_F and subtracts it from P_G. Therefore, identically in all
cell signs,

    sum_F P_F=0.                                        (6)

The integers in the table are definitions. Their origin as five times
displayed rational candidates from a finite optimization is only discovery
history. Formula (6) follows from the displayed transfer definition, not
from an optimization output.

We will derive

    sum_{line factors} P_F >= -68,
    sum_{completion blocks} P_F >= 72.                  (7)

Together with (6), these give 0>=4, proving the contradiction.

The source has 28 cells. The table uses the following block notation:
B:d,e contains the original corners

    (x+d,x), (x+e,x), (x+e,x+e-d),

at every available start x. The variable order for each polynomial is
printed in the companion table. No variable attached to a physical cell
can change from one factor to another.

## 3. The line-polynomial lower bounds

In this section indices are one-based within each line's vertex order in
the companion table. The following positive decompositions give eight
of the bounds directly from (1):

| Factor | Polynomial decomposition | Lower bound |
|---|---|---:|
| D:1 | K(2,4,5) | -1 |
| D:2 | 2K(1,2,3,4,5)+K(1,2,5) | -5 |
| D:4 | 2K(1,3,4) | -2 |
| R:3 | 2K(1,2,3) | -2 |
| R:4 | 2K(1,2,4)+K(1,3,4) | -3 |
| R:6 | K(1,3,5)+2s1*s5 | -3 |
| R:7 | 2K(1,4,6)+2K(1,2,5)+3K(2,3,6)+K(1,2,6) | -8 |
| C:3 | 2K(1,3,4) | -2 |

The extra edge in R:6 is at least -2. Every other entry is a sum of
clique polynomials, with the displayed lower bound following by addition.
These eight lower bounds sum to -26.

The remaining four line bounds are

    P_R8>=-14, P_C0>=-15, P_C1>=-7, P_C2>=-6.            (8)

Their complete coefficient lists and algebraic derivations are in
`fibers/PAIR_LINE_DERIVATIONS_0014.md`. To specify the chain of reasoning:
R:8 decomposes into twice a five-variable clique and six weighted triangle
types, giving -4-10=-14. C:1 and C:2 decompose into triangles of total
weights seven and six. For C:0, global sign reversal sets its fourth sign
to one; eliminating two independent signs gives two absolute values,
and the displayed eight-case table on the remaining three signs has
minimum -15. That note writes every absolute-value expression and case.
It is a mathematical input with its full derivation, not a solver claim.

Adding (8) to -26 gives -26-14-15-7-6=-68. Line polynomials omitted from
the table are zero, proving the first assertion of (7).

## 4. Blocks that use only original corners

Whenever a block polynomial is a sum of terms -w*K(a,b,c) with w>=0
and (a,b,c) an original corner, (2) makes its value exactly the sum of
the weights. Reading the explicitly listed triples in the coefficient
table gives the following values:

| Block | Original-corner weights | Value |
|---|---|---:|
| B:1,3 | 2,2 | 4 |
| B:1,5 | 3,2 | 5 |
| B:1,8 | 4 | 4 |
| B:2,7 | 3 | 3 |
| B:2,8 | 4 | 4 |
| B:3,6 | 2 on its second corner | 2 |
| B:3,7 | 2 | 2 |
| B:4,5 | 2 on its second corner | 2 |
| B:4,7 | 2 | 2 |
| B:4,8 | 3 | 3 |
| B:5,7 | 2 | 2 |
| B:6,8 | 5 | 5 |
| B:7,8 | 2 | 2 |

These values sum to 40. B:3,5 has the zero polynomial and contributes
zero. The remaining eleven blocks are handled in the next sections.

## 5. Two original corners with six distinct cells

For each of B:1,6, B:1,7, and B:2,6, use the companion table's order
a,b,c,d,e,f. The original corners are (a,c,d) and (b,e,f). Their
polynomials have the following decompositions:

    P_16=-4K(a,c,d)-4K(b,e,f)+K(a,b,d)+2K(a,b,f),
    P_26=-3K(a,c,d)-3K(b,e,f)+K(a,b,f),
    P_17=-3K(a,c,d)-4K(b,e,f)+2K(a,d,f)
            +c(a+e)+b(e-a).                             (9)

Here the last two clique types need not be corners; (1) applies to any
three signs. If a=e, the last bracket in P_17 equals 2ac; if a=-e,
it equals -2ab. It is therefore always +2 or -2. Equations (1)--(2)
and (9) give

    P_16>=8-1-2=5,
    P_26>=6-1=5,
    P_17>=7-2-2=3.                                     (10)

These lower bounds need no claim about independent coloring choices in
the two corners; the same signs a,...,f are used throughout.

Two further blocks have simple nonnegative costs. In B:2,5, in table
order a,b,c, the original corner is proper and

    P_25=-2a(b+c)=2+2bc>=0.                             (11)

In B:3,4, use its six table variables a,b,c,d,e,f. Its first original
corner is (a,b,c), and

    P_34=2(a+c)(f-b)>=0.                                (12)

If a=-c this is zero. Otherwise a=c=t and properness gives b=-t;
the expression is 4(1+tf), which is nonnegative.

## 6. Chains with three inner cells

For B:1,4, B:2,3, B:4,6, B:5,6, and B:6,7 use the five variables
a,b,c,d,e in the table order. In each case (a,b,c) and (c,d,e) are
the two original corners with successive starts separated by h=e_offset
-d_offset. The cells a,c,e are three equally spaced inner-offset cells.
The cells b,c,d are the supported reflected triple. Hence, putting

    T1=K(a,b,c), T2=K(c,d,e), I=K(a,c,e), M=K(b,c,d),

we have T1=T2=I=M=-1 by Sections 1 and 2. The complete source lists
supporting these statements are obtained respectively from

    (d_offset,h,x)=(1,3,0), (2,1,0), (4,2,0),
                    (5,1,1), (6,1,0).

In every case the six marks in (4) lie in A. The listed polynomials
decompose as

    P_14=-3T1-2T2-I = 6,
    P_23=-2T1-2I = 4,
    P_46=-2T1-3T2+M+I = 3,
    P_67=-4T1-3T2+M+4I = 2,
    P_56=-2T2-M+2I-2c(a+b) >= 1.                       (13)

For the last line, the first four terms give 2+1-2=1. Properness of
(a,b,c) gives -2c(a+b)=2+2ab>=0. This supplies the last inequality.

## 7. The four-inner-cell chain B:2,4

Use its table variables a,b,c,d,e,f,g. The inner-offset cells are
a,c,e,g. Set

    T1=K(a,b,c), T2=K(c,d,e), T3=K(e,f,g),
    M1=K(b,c,d), M2=K(d,e,f), I1=K(a,c,e).

The T triples are the original corners. The M triples are reflected
triples supported by (d_offset,h,x)=(2,2,0) and (2,2,2), whose source
marks are among 0,2,4,6,8. The I triple is an equally spaced inner-fiber
triple. Thus all six displayed clique sums equal -1. The polynomial is

    P_24=-2T1-3T2-2T3+M1+I1+2M2=3.                    (14)

This is an exact value under the contrary properness assumption.

## 8. The ten-cell block B:1,2

Use actual fiber notation here, to make all shared cells explicit:

    a_i=z_1(i), i=0,1,2,3,
    u=z_1(6), v=z_1(7),
    b_i=z_2(i), i=0,1,2,6,
    S=a_0+a_1+a_2+a_3.

The four original corners have endpoint/completion triples

    (a_0,b_0,a_1), (a_1,b_1,a_2),
    (a_2,b_2,a_3), (u,b_6,v).                           (15)

The supported reflected triple (b_0,a_1,b_1) is also proper. Combining
its identity with the first two identities in (15) gives

    -a_0b_0+b_0b_1-a_1b_1-2a_2b_1
       =2+a_0a_1+2a_1a_2.                              (16)

For example, substitute b_0b_1=-1-a_1(b_0+b_1), then use
-b_0(a_0+a_1)=1+a_0a_1 and
-2b_1(a_1+a_2)=2+2a_1a_2. The third original corner gives

    -b_2(a_2+a_3)=1+a_2a_3.                            (17)

The inner triples (a_0,a_1,a_2) and (a_1,a_2,a_3) are equally spaced
fiber triples. Adding their identities yields

    S^2=2(a_0a_3-a_1a_2),
    S in {-2,0,2}.                                     (18)

The second assertion follows because S is an even integer and the right
side of the first lies between -4 and 4.

Substitute (16)--(18) into the B:1,2 polynomial displayed in the table.
Collecting the inner pair terms gives the following compact expression:

    P_12=2S^2+2S(u+v)-2uv-2vb_6.                       (19)

For clarity, before using (18) those inner terms and the constants from
(16)--(17) combine to

    4(a_0a_3-a_1a_2)+2S(u+v)-2uv-2vb_6,

which gives (19) directly. If u=v=t, the last original corner in (15)
gives b_6=-t. The last two terms in (19) cancel, leaving
2S(S+2t)>=0 for S in {-2,0,2}. If u=-v, (19) becomes
2S^2+2-2vb_6>=0. Thus

    P_12>=0.                                           (20)

No enumeration of the eleven first-fiber words is needed in this proof.

## 9. Summation and scope

The thirteen original-corner-only blocks contribute 40. The remaining
nonzero lower values, grouped by their inner offset, are

    d=1: 0+6+5+3 =14,
    d=2: 4+3+0+5 =12,
    d=3: 0,
    d=4: 3,
    d=5: 1,
    d=6: 2.

Their sum is 32, so the total block lower bound is 40+32=72. Together
with the line lower bound -68 and the cancelling identity (6), this
gives

    0=sum_F P_F >= -68+72=4,

the required contradiction. This proves the theorem on A. A translation
and positive integer dilation preserve all displayed source incidences
and multiply every positive corner step by q. Restricting a purported
proper coloring of a larger source to that affine copy proves the final
assertion of the theorem.

This derivation illustrates how shared relative colors and supported
reflected-corner identities can be converted into a global algebraic
obstruction. Its local target was already known from the inherited
catalog. The independently optimized line budget had been reported as
41 against 44 corners, and a maximal-clique LP supplied no strict
contradiction; those finite observations motivated the example but are
not used in the proof above.

The all-source quantitative implication S11 remains unproved. Neither
R3<465 nor R4<100000 follows from this local obstruction alone. The
campaign's original superior-method objective is therefore still open.
