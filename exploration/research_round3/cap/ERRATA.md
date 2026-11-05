# CAP-E1 run-status anomaly

The first ruler-pair search emitted and saved its complete finite attempt
log but the execution wrapper reported exit1 with no visible traceback.
All negative statuses remain INTERNAL_UNSAT_UNVERIFIED. No mathematical
conclusion is promoted from that run. Preserve the script/log unchanged;
replace solver reliance for the selected pair by an explicit local forcing
derivation, and independently check every forcing step. The raw anomaly
has no established root cause yet; the solver-wrapper path is suspended.

CAP-E1 RESOLVED FOR PROOF USE: the unchanged rerun ended with native
exit status -1073740791 and empty stderr. Its native cause remains unknown,
so all original solver negatives remain quarantined. The replacement
pair_forcing_certificate.json gives60 pure Boolean forcing refutations,
with16425 steps checked by the separately implemented geometry-only
verify_pair_forcing.py, which imports no solver or generating program.
All specified disjoint translations/reflections are covered. The valid
finite conclusion now depends solely on these traces, not native status.
This is a resolved evidence-path failure, not an explanation of the crash.
