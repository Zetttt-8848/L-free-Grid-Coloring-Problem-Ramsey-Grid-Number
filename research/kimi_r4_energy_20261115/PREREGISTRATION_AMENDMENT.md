# Preregistration amendment: zero witnesses before exhaustive enumeration

Written before any Route F coloring enumeration was run.

For `rho_m=0`, one completely checked proper four-coloring of the full `m by m`
square with no rainbow L in its strict lower triangle is already a proof of the
exact minimum. The search will stop at that witness. It will not enumerate all
proper colorings or list all minimizers for that order.

If no zero witness is found, a positive value of `rho_m` requires the complete
canonical enumeration and independent coverage check stated in the contract.
A partial search without such a witness changes nothing and is UNDECIDED.

Orders are tested as `m=3,4,5`, in that order. The wall-clock budget is 120
seconds per order and 300 seconds for the complete Route F search, with one
worker and no parallel jobs. A timeout stops the route; it does not authorize
order 6 or a larger repeated search. This amendment changes neither the
upper-bound consumer nor the acceptance standards.
