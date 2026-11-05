# Moving a fan to an existing source column

Root derivation, continuation 0038. The missing-label and missing-target
terms in the fixed-anchor fan budget can be avoided by moving the charge
to a later physical column. This replaces holes by an explicit incoming
multiplicity. It is not a linear energy bound.

Let A be a finite integer source with one proper strict two-coloring z.
For a in A, define its positive suffix labels B_a={t-a:t in A,t>a},
its anchored colors f_a(x)=z(a+x,a), and its addition graph J_a as in
ANCHORED_SUM_PEELING_0037.md. Take x in B_a and

    0<y<z, y,z,x+y,x+z in B_a,
    f_a(x)=f_a(x+y)=f_a(x+z)=c.                      (1)

The monochromatic anchored fan (1) forces

    z(a+x+y,a+y)=z(a+x+z,a+z)=-c,
    z(a+x+z,a+y)=c.                                 (2)

Put b=a+y and h=z-y. Then b,b+h,b+x,b+x+h are all actual source
marks. Consequently J_b contains the arc

    x -> x+h,                                       (3)

and (2) gives its two anchored colors -c and c. Thus every fan pair
at a supplies an opposite-color addition arc at the strictly later
anchor b, whether or not h or x+h belongs to the old label set B_a.
No mark is added to A in this transport.

## 1. Exact incoming multiplicity

Fix an opposite-color arc (3) at b, with

    f_b(x)=-c, f_b(x+h)=c.

Its incoming anchor set is precisely

    U_(b,x,h)={a in A:a<b, a+x in A,
       z(a+x,a)=z(b+x,a)=z(b+x+h,a)=c}.              (4)

For a in this set the unique original labels are y=b-a and z=b+h-a.
They satisfy (1). Conversely every fan transported to the given arc
has those labels and satisfies (4). Hence there is an exact identity

    sum_(a in A) sum_(x in B_a) binom(k_(a,x),2)
      =sum_(opposite arcs (b,x,h)) |U_(b,x,h)|,       (5)

where k_(a,x) is the size of the same-color forward fan at a,x.
This identity replaces the fixed-anchor defects by actual source
incidences. The right side is weighted by their multiplicity, not
just the number of arcs.

## 2. Restrictions on one incoming set

Every U=U_(b,x,h) lies in a single actual signed offset-x fiber,
because z(a+x,a)=c for all its starts. Therefore U is Golomb.
It has the additional exclusion

    U intersect (U-h) is empty.                     (6)

Indeed, suppose a,a+h both belong to U. The three actual cells

    (b+x,a), (b+x+h,a), (b+x+h,a+h)

form a positive corner of step h. The first two have color c from
membership of a in (4), and the last has color c from membership
of a+h. This contradicts properness. All coordinates are supported
by (4) and the target arc; no old-anchor hole is filled.

Two incoming anchors a<a' also generate an earlier opposite-color
addition arc. Their offset-x cells have color c, so their completion
(a'+x,a) has color -c. Since a',a'+x are source marks, J_a has

    x -> x+(a'-a),                                  (7)

whose anchored endpoint colors are c,-c. By (6), its step a'-a
cannot equal the target step h. For a fixed incoming set U, each
pair a<a' determines its own arc in (7). This does not assert
injectivity across different target arcs or different incoming sets.

## 3. Remaining budget

Equations (5)-(7) retain both directions of the forced coupling:
fan pairs move to a later column, while pairs of incoming anchors
produce opposite-color arcs in an earlier column. The incoming sets
are Golomb and have no pair at the target step, but their cardinalities
need not be bounded by those facts alone.

Thus (5) cannot be replaced by an unweighted opposite-arc count.
The same earlier arc in (7) may serve several later targets with
different steps. An eventual amortized argument must retain this
reuse, or exploit a further compatibility among those targets.
The transport offers an alternative to charging absent labels; it
does not yet pay either type of cost by a constant per source mark.
EP10, H10, and S21 remain open for general proper sources.
