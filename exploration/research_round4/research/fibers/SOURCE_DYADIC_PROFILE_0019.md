# Dyadic source profile: bounded discovery scope

The accompanying JSON reuses stored proper-source candidate records and makes
no solver call or coloring check.  It counts only

\[
T_H=\sum_d\sum_{H\le h<2H}|F_d\cap(F_d-h)|,
\]

where `h` is the translation between fiber starts.  Among 100 saved inputs,
no band had \(T_H>M\).  The largest raw sampled ratio was
\(29/36\), for the stored window-13 candidate
\(A=\{0,1,2,5,6,7,8,11,12\}\) at \(H=4\).

Thus this list does not immediately refute a coefficient-one dyadic band
bound, but it does exceed the proposed \(0.6M\) scale target.  The separate
five-mark interval calibration \(T_H/M=3/5\) is copied from
`DYADIC_CHARGING_0016.md`; it was not checked here.  These observations are
bounded discovery data, not universal statements.
