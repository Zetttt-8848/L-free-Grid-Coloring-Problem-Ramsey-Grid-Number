# Transferring the reflected-middle binary core through actual source fibers

Let \(A\subseteq[0,L]\cap\mathbb Z\), and let \(z\) be a proper
two-coloring of its strict source triangle \(V(A)\). For \(d>0\), put
\[
F_d=\{x:x,x+d\in A\},\qquad
F_d^\sigma=\{x\in F_d:z(x+d,x)=\sigma\}.
\tag{1}
\]
The cells
\[
w_d(v,u)=z(v+d,u),\qquad u\le v,\quad u,v\in F_d,
\tag{2}
\]
form a proper weak triangle \(W(F_d)\), and its two diagonal classes are
\(F_d^+\) and \(F_d^-\). In particular, both signed classes are Golomb.

This note transfers the reflected-middle alternative of
TWO_POINT_BINARY_NORMAL_FORM_0043.md to these actual fibers. The result is
an injective charge to a signed source pair together with an interior missing
translation edge. It gives an exact aggregate ledger, though not a lower
bound on how often the cores occur.

## 1. The two oriented core seeds

Fix \(d>0\), a sign \(\tau\), a pair
\[
r,r+h\in F_d^\tau,\qquad h>0,
\tag{3}
\]
and write \(\sigma=-\tau\).

An **upper core seed** consists of a parameter \(0<p<h\) for which
\[
r+p,\quad r+h+p,\quad r+2h\in F_d^\sigma.
\tag{4}
\]
The reflected-middle rule in the proper weak triangle \(W(F_d)\) gives
\[
x=r+h-p\notin F_d.                               \tag{5}
\]

The direction-preserving reflected seed is the **lower core seed**
\[
r-h,\quad r-p,\quad r+h-p\in F_d^\sigma,
\qquad 0<p<h,
\tag{6}
\]
and it gives
\[
x=r+p\notin F_d.                                 \tag{7}
\]

Both holes lie strictly inside the opposite-color pair:
\[
r<x<r+h.                                         \tag{8}
\]
The assertions (5) and (7) are stronger than saying that \(x\) has the
wrong diagonal sign. They say that the start \(x\) is absent from the whole
actual fiber. By (1),
\[
x\notin F_d
\quad\Longleftrightarrow\quad
x\notin A\ \hbox{ or }\ x+d\notin A.             \tag{9}
\]
Thus every seed witnesses an actual missing translation edge
\((x,x+d)\), while all five seed starts and their \(d\)-translates belong
to \(A\).

## 2. Injection into signed pair-hole incidences

For fixed \(d,\tau\), define
\[
\mathcal G_d^\tau=
\{(r,s,x):r<s,\ r,s\in F_d^\tau,\ r<x<s,\ x\notin F_d\}.
\tag{10}
\]

**Injection lemma.** Sending either core seed to
\[
(r,r+h,x)\in\mathcal G_d^\tau                   \tag{11}
\]
is injective.

For a fixed image, an upper seed must have
\[
p=r+h-x,
\tag{12}
\]
and a lower seed must have
\[
p=x-r.
\tag{13}
\]
Thus there is at most one seed of each orientation.

It remains to exclude one upper and one lower seed with the same image.
After substituting (12), the upper seed supplies the \(h\)-pair
\[
\{2r+h-x,\ 2r+2h-x\}\subseteq F_d^\sigma.
\tag{14}
\]
After substituting (13), the lower seed supplies the \(h\)-pair
\[
\{2r-x,\ 2r+h-x\}\subseteq F_d^\sigma.           \tag{15}
\]
These are distinct pairs of difference \(h\); they share the endpoint
\(2r+h-x\). Hence simultaneous upper and lower seeds would violate
Golombness of \(F_d^\sigma\). This includes the midpoint case
\(x=r+h/2\). The map (11) is injective.

The point of retaining \(\tau\) and the pair \(\{r,r+h\}\) is that many
different signed pairs may straddle the same bare hole \(x\). The lemma does
not identify those charges.

## 3. Exact aggregate gap-hole ledger

Let \(K\) be the total number of upper and lower core seeds over all
\(d,\tau,r,h,p\). The injection lemma gives
\[
K\le\mathcal G:=
\sum_{d=1}^{L}\sum_{\tau\in\{+,-\}}|\mathcal G_d^\tau|.
\tag{17}
\]
There are two useful exact expansions of the right side. Put
\[
\lambda_d^\tau(x)=|\{r\in F_d^\tau:r<x\}|,\qquad
\rho_d^\tau(x)=|\{s\in F_d^\tau:s>x\}|.
\tag{18}
\]
Counting first by the missing translation edge gives
\[
\mathcal G=
\sum_{d=1}^{L}
\sum_{x\in[0,L-d]\setminus F_d}
\sum_{\tau}\lambda_d^\tau(x)\rho_d^\tau(x).
\tag{19}
\]
Counting first by the signed source pair gives
\[
\mathcal G=
\sum_{d=1}^{L}\sum_{\tau}
\sum_{\substack{r<s\\r,s\in F_d^\tau}}
\left((s-r-1)-|F_d\cap(r,s)|\right).
\tag{20}
\]
Indeed, the parenthesis is exactly the number of integer starts strictly
between \(r,s\) that are absent from \(F_d\).

Equations (19)-(20) are the desired no-reuse accounting. A hole may occur
many times, but its multiplicity is exactly the number of monochromatic
signed pairs crossing it. Equivalently, a fixed signed source pair of length
\(h\) receives at most \(h-1\) charges, with one deducted for every actual
fiber start in its open interval.

## 4. A finite-span bound

For fixed \(d,\tau,x\), the crossing pairs counted by
\(\lambda_d^\tau(x)\rho_d^\tau(x)\) have distinct positive differences,
because \(F_d^\tau\) is Golomb. All those differences lie in
\(\{1,\ldots,L-d\}\). Therefore
\[
\lambda_d^\tau(x)\rho_d^\tau(x)\le L-d.
\tag{21}
\]
Summing the two signs in (19) yields the explicit bound
\[
\boxed{
K\le\mathcal G
\le2\sum_{d=1}^{L}(L-d)\bigl(L+1-d-|F_d|\bigr).
}
\tag{22}
\]
Here \(L+1-d-|F_d|\) is exactly the number of missing translation edges of
length \(d\) in the ambient interval.

Since every unordered pair of ambient marks is either an \(A\)-pair or a
missing translation edge,
\[
\sum_{d=1}^{L}\bigl(L+1-d-|F_d|\bigr)
=\binom{L+1}{2}-\binom{|A|}{2}.                  \tag{23}
\]
Consequently the coarser closed form is
\[
K\le
2(L-1)\left(\binom{L+1}{2}-\binom{|A|}{2}\right).
\tag{24}
\]

One may instead charge to missing marks. Assign \((d,x)\) canonically to
\(x\) when \(x\notin A\), and otherwise to \(x+d\notin A\). A missing mark
\(q\) is incident with at most one candidate translation edge of each
length on either side. Using (21), its total tagged charge is at most
\[
2\sum_{d=1}^{L-q}(L-d)+2\sum_{d=1}^{q}(L-d)
=L(L-1)+2q(L-q).                                 \tag{25}
\]
Thus
\[
K\le
\sum_{q\in[0,L]\setminus A}
\bigl(L(L-1)+2q(L-q)\bigr).                      \tag{26}
\]
The edge-weighted bound (22) is generally sharper; (26) records an explicit
missing-mark multiplicity without asserting that a bare hole is used only
constantly often.

## 5. Exterior doubling and the remaining limitation

The exterior anchored-doubling pattern is already impossible inside each
actual \(W(F_d)\) by the supported-fan sum-free rule. Its incomplete data do
not select one canonical missing start: failure may occur at an endpoint of
either representing signed pair or at one of the two opposite-color anchors.
Without fixing all but one of those memberships, charging an exterior
pattern to a particular absent translation edge would be a disjunctive
choice, not an injection. No such charge is added to (17).

The reflected-middle ledger is also one-sided. It bounds the number of
fully witnessed seeds by available signed pair-hole incidences, but it does
not lower-bound the number \(K\) from the energy of \(A\). Sparse sources can
avoid these particular five-present-start patterns. Therefore (22) is a
finite-span consequence of actual source colors, not a uniform source-size
or energy bound. A global application still needs a mechanism forcing many
core seeds, or a second identity that pays high-energy fibers when \(K\) is
small.
