# Dilation-weight LP discovery (0043)

Raw floating-point discovery only. The script and JSON are fibers/DILATION_WEIGHT_DISCOVERY_0043.py and fibers/DILATION_WEIGHT_DISCOVERY_0043.json. No value below is an exact LP optimum, rational inequality, or local rainbow lower bound.

For N=464, M_host=binom(464,2), and each m=10,...,18, the run maximized

    sum_(d=1)^D C_d w_d,
    D=floor(462/(m-2)), C_d=binom(464-d(m-2),2),

subject to w_d>=0 and, for h=1,...,462,

    sum_d A_(h,d) w_d <= 1,
    A_(h,d)=binom(m-h/d,2)

when d divides h and 1<=h/d<=m-2, and A_(h,d)=0 otherwise. These are the requested safe boundary-discarding host rows.

The “uniform” comparison assigns every dilation one common largest feasible weight under these same rows. It is only a comparison baseline.

| m | D | raw LP objective | raw conditional rho threshold M_host/objective | uniform baseline | raw gain | nonzero reported weights |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 57 | 31750.751431 | 3.383101 | 18888.485981 | 1.680958 | 57 |
| 11 | 51 | 21802.530488 | 4.926768 | 12521.748252 | 1.741173 | 51 |
| 12 | 46 | 15612.007690 | 6.880345 | 8682.437838 | 1.798113 | 46 |
| 13 | 42 | 11547.871198 | 9.301801 | 6246.433476 | 1.848714 | 42 |
| 14 | 38 | 8744.348870 | 12.284048 | 4617.131944 | 1.893892 | 36 |
| 15 | 35 | 6738.881774 | 15.939737 | 3495.400000 | 1.927929 | 33 |
| 16 | 33 | 5266.635458 | 20.395564 | 2702.245823 | 1.948985 | 31 |
| 17 | 30 | 4167.945157 | 25.771932 | 2127.787879 | 1.958816 | 28 |
| 18 | 28 | 3338.032452 | 32.179436 | 1702.671280 | 1.960468 | 28 |

Within this nine-case run, m=18 has the largest raw multiplicative gain over the safe uniform baseline, about 1.960468. Its conditional threshold is nevertheless about 32.179436. The complete raw candidate support, weights, C_d values, LP status text, and active host steps are retained in the JSON for symbolic/rational follow-up.

Every HiGHS call returned its floating-point “optimal” status and maximum row load at floating tolerance near one. That is a solver report only; this discovery note deliberately makes no certification or universal conclusion.
