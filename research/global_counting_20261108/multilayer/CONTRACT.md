# All-level colored recurrence counting

Base: `5b5db22c3c65123193cb31f2aa5bd949b3075e1a`.

Object: a diagonal word of a hypothetical directed equal-leg L-free
three-color square. Coordinates are zero-based and the forbidden triple is
`(x,y),(x+d,y),(x+d,y+d)`, with positive integer d.

The new resource is the first two returns of each **diagonal color at each
lag**, shared by all Golomb cardinality levels, together with the last two
returns. The old scalar count forgets their colors and retains only one
cardinality threshold. Desired conclusion: a universal upper bound for
the resulting weighted nonlinear word functional strong enough to reduce
the side-464 upper bound substantially.

This package proves the resource inequalities and their exact convolution
bridge. It does not solve the final universal word extremum, and does not
claim a new Ramsey number. No lower-bound SAT search is performed.

First uncertain step: simultaneously maximizing the all-level capped
colored autocorrelations of the nested prefixes/suffixes of **one** word.
Separate maxima for each lag or cardinality level are not a solution.

Checks: exhaustive short interval Golomb partitions validate the endpoint
transport specialization; independent literal layercake reconstruction
validates the all-level recurrence identity. Finite checks audit formulas,
not the general proof and not the external large Golomb lower bounds.
