# Ordered one-sided matching-block input (0046)

## Exact translation

Let the selected bipartite graph have left part \(I\), right part \(B\),
and order \(I\) in *decreasing* numerical order. A label class \(M_d\)
is a matching. If it contains
\[
(a,b),\ (a',b'),\qquad a<a',\quad b<b',
\]
the retained forcing rule forbids the cross edge \((a,b')\). In the
decreasing left order, \((a',b')\) comes before \((a,b)\), and the
forbidden cross edge joins the later left endpoint \(a\) to the earlier
right endpoint \(b'\).

Thus each label class is exactly a **semi-induced matching** for this
specified order of the left part: for matching edges \((u_i,x)\) and
\((u_j,y)\) with \(i<j\), the edge \((u_j,x)\) is absent. This condition
does not forbid the other cross edge, matching the retained source rule.

## One targeted primary-source pass

R. Gandhi, R. Gandhi, M. Harchol-Balter, and M. Henzinger,
[*Radio aggregation scheduling*](https://par.nsf.gov/servlets/purl/10210278),
*Theoretical Computer Science* 840 (2020), 143--153, Definition 1, defines
a semi-induced matching in a bipartite graph \(G=(U,V,E)\) with an order
\(u_1,\ldots,u_n\) on \(U\) as a matching for which, whenever
\((u_i,a)\) and \((u_j,b)\) belong to it with \(i<j\), there is no edge
\((u_j,a)\). This is the exact one-cross-edge condition above after the
order reversal.

The paper defines \(\operatorname{Sim}(G)\), the largest size of such a
matching, and uses it in approximation-hardness reductions. Its displayed
quantitative comparisons concern constructed graphs and
\(\operatorname{Sim}(B_e(G^k))\); they do **not** bound the number of
semi-induced matching classes needed to partition an arbitrary ordered
bipartite graph in terms of \(|I|,|B|\), or the number of numerical
difference labels.

## Quantitative hypothesis comparison

With \(p=|I|\), \(q=|B|\), and \(\ell\) labels, the directly available
matching count is only
\[
|E|\le \ell\min\{p,q\},\qquad |E|\le pq.
\tag{1}
\]
In the actual partial-block model the label is the output
\(c=u+b-a\in A\). Thus the common \(m\)-mark source gives the stronger
\[
\ell\le m.
\tag{2}
\]
Neither (1) nor (2) uses the one-sided exclusion.

The corrected label budget still does not yield an \(O(m)\) edge bound from
the one-sided rule alone. The project-local abstract construction in
`fibers/SEMI_INDUCED_BLOCK_DENSITY_0046.md` has \(\ell\le m\), every label
in \(A\), and \(\Omega(m^{1+\log_3 2})\) selected edges. It is a
partial-block construction, not a full proper-source coloring.

## Bounded conclusion

The located primary notion matches the retained one-sided prohibition
exactly, but the source's quantitative theorems have a different target
and do not provide the requested explicit extremal relation among
\(|I|,|B|\), and the number of labels. Any use in the root mechanism
would require an additional numerical-source hypothesis beyond the
one-sided ordered matching condition.
