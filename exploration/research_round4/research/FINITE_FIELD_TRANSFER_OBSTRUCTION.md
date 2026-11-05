# Why the stronger finite-field exponent is not an integer-grid bound

Base R4-RESEARCH-0001. A direct obstruction to a tempting transfer, derived during the current research.

The 2025 theorem gives exponent 1/178 over F_2^m, stronger than its general-abelian exponent 1/600. Encoding binary vectors as ordinary integers does not preserve its corners.

For the standard binary encoding phi(a0,a1)=a0+2a1, take x=(0,1), y=(1,0), and d=(1,1) in F_2^2. The standard group corner is

(x,y), (x+d,y), (x,y+d).

Its integer image is {(2,1),(1,1),(2,2)}. At the shared corner base (2,1), the two increments are -1 and +1. They are unequal as integers, although they both come from the same nonzero group vector d. There is no signed standard corner on these three image points: (2,1) is the only point that shares both a row and a column with the other two, and its two increments differ. Translation into a positive square does not change that fact.

More generally, on each active bit the integer increment is positive when the old bit is zero and negative when it is one. The row and column old bits can differ, so matching group increments need not give matching integer increments. A half-turn changes both signs together and cannot repair opposite signs.

Thus the finite-field exponent cannot replace 600 in GENERAL_BOUND.md by this encoding. A further structural theorem selecting suitable directions would be necessary. The cyclic embedding used there avoids this problem because equality modulo 2N between the two bounded integer differences forces actual equality.

This rules out only the stated direct encoding, not every possible finite-field transfer and not an improved exponent by another argument.
