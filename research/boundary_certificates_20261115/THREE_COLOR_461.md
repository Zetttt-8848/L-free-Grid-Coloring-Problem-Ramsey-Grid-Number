# The three-color square at side 461

Every three-coloring of the 461 by 461 square has a monochromatic triple $(x,y),(x+d,y),(x+d,y+d)$ for some integer $d>0$. This gives **$21\le R_3\le461$**. The order-24 and order-25 Golomb thresholds and the order-24 uniqueness theorem are the external inputs. The lower bound comes from the known 20 by 20 coloring. [Order-24 input](https://blogs.distributed.net/2004/11/) · [Order-25 input](https://blogs.distributed.net/2008/10/) · [Lower-bound construction](https://arxiv.org/html/2312.01159v1)

## Why the boundary changed

In a hypothetical proper square of this side, each class of starts at positive shift $d$ is a Golomb set on $461-d$ positions. A completion class with 24 marks must have span at least 425. In the [forced-color argument](NO_OPTIMAL_461.md), every span-425 class restricts its original color to at most 95 diagonal positions, while each color needs at least 135. The span of every 24-mark class in this particular square must therefore be at least **426**. This assertion concerns realizable completion classes, and the Golomb optimum itself stays 425.

Set $b=461-426=35$ and let $z$ be the 35-letter initial diagonal word. A size-24 class at shift $d$ has its minimum in the first $k=b-d$ positions of the start interval. Such a minimum must satisfy $z_i=z_{i+d}$. Each original color supplies at most two completion classes and every class has a different minimum. For $1\le d<35$ define

$$
T_d(z)=\sum_{c=0}^2\min\bigl(2,\#\{0\le i<35-d:z_i=z_{i+d}=c\}\bigr).
$$

The six-class bound on the total number of equal-color pairs at this shift is $138+T_d(z)$. For $35\le d\le84$ it is 138. The old prefix model used 36 letters at side 461. Its counterexample does not survive the change in allowable span.

## Integer contradiction

Use $w_i=i(86-i)$ for $1\le i\le85$ and $a_d=\sum_i w_iw_{i+d}$. Relative to the baseline capacity $138+\min(6,\max(0,35-d))$, the kernel margin at side 461 is $G_0=-9{,}822{,}511{,}181$. The [diagonal convolution calculation](README.md) requires

$$
G_0+3 D(z)\le0,\qquad
D(z)=\sum_{d=1}^{34}a_d\bigl(\min(6,35-d)-T_d(z)\bigr).
$$

An exhaustive count over all $3^{35}=50{,}031{,}545{,}098{,}999{,}707$ labeled words gives $D(z)\ge3{,}274{,}170{,}394$. The integer margin is at least **1**. This proves the claim. We use the threshold sufficient for a contradiction, without asserting it is the exact minimum loss.

## Reproduce

1. Run **python verify_no_optimal.py** to check the binary forced-color exclusions and diagonal frequencies.
2. Compile **verify_462.c** as described in [the directory instructions](README.md). Run **./verify_462 --461** for the 35-letter count. The executable first checks a seven-letter case against literal enumeration. The existing no-argument invocation reproduces the previous checkpoint.

The GPU discovery recount used a separate implementation and 122 six-letter prefix batches. A CPU recount split the same space into 122 branches, multiplying by the number of choices for every newly introduced color. The release checker uses different initial color symmetries, literal autocorrelation sums and portable integer arithmetic.
