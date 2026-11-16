# Consumer erratum: valid square copies inside the host triangle

The original `CONTRACT.md` wrote the square-copy count as

```text
J=sum_s a_s*(N-s*(m-1))^2
```

for a consumer charged to rainbow Ls in the host strict triangle `T_N`.
That formula is not valid for this consumer: it counts copies whose local
strict lower triangle is not contained in `T_N`.

For example, at `N=4,m=3,s=1`, the unrestricted formula gives four origins.
The origin `(a,b)=(0,1)` is invalid for the host-triangle consumer: its local
strict cell `(i,j)=(1,0)` maps to `(1,1)`, which is not in `T_4`. Only three
origins are valid.

No experiment or proof used the erroneous count to claim a Ramsey bound. The
error was found during the consumer audit before any positive local minimum was
accepted.

## Correct statement

For a scale-`s` square copy with origin `(a,b)`, every cell of its local strict
lower triangle lies in host `T_N` exactly when

```text
a-b+s>=1.
```

With `q=N-1-(m-1)s` and `t=min(s-1,q)`, the corrected number of origins for
`q>=0` is

```text
A(N,m,s)=C(q+2,2)+t(q+1)-C(t+1,2).
```

Thus the corrected total copy weight is `J=sum_s a_s*A(N,m,s)`. The incidence
bound in the contract remains an upper bound after restricting to these valid
origins. The exact proof, asymptotic threshold, and independent checks are in
`THEOREM.md`, `consumer_audit.py`, and `verify_consumer.py`.

The contract and this erratum are both preserved for auditability. The corrected
consumer remains CONDITIONAL on a positive local `rho_m`; all three tested
orders have `rho_m=0`, and the uniform asymptotic consumer is dominated for
every `m>=6`. No numerical bound changed.
