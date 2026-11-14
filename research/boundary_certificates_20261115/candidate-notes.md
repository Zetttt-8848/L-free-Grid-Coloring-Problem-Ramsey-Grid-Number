# Research log, 15 November 2026

## Four colors and explicit finite Sidon estimates

The rank bounds currently estimate the inner positive-difference multiplicities from scratch. The October 2026 Carter, O'Bryant and Tao preprint proves an explicit finite diameter inequality for sets of bounded difference multiplicity, including the non-unit case. The question is whether imposing this inequality at the Golomb and binary-source levels gives a positive integer upper-bound margin below 21,987,409. A cheap test uses their cardinality bound directly against the same square convolution. The projected upper bound will be recorded after a second implementation checks the constants and the hypotheses on size and multiplicity. This route inherits the source partition and uses a new external premise. The earlier elementary certificate remains independently available. The finite-diameter and one-class value routes are also compared against interval-dependent rank constraints.

## Three colors and both boundaries at 461

An extremal class gives a pair of full-diagonal occurrences of the same oriented optimal ruler. Independent choices for its color and orientation at different distances discard this fact. Fix both orientation colors across all distances, and test extremal endpoint equality only in those colors. For each distance at most one exact class of each orientation can occur. A second constraint uses the explicit contribution to the convolution variance at the two ends, where the prefix or suffix already determines the color sums. The implication to a new bound requires exhaustive coverage. The immediate falsification test is to search for a pair of 36-letter words surviving both conditions and measure how much of a preliminary single-end list is excluded.

The single-class exclusion supersedes this search at side 461. See the [forced-color count](NO_OPTIMAL_461.md) and the [complete boundary certificate](THREE_COLOR_461.md). The four-color calculation above gives [21,953,510](FOUR_COLOR_SIDON.md).
