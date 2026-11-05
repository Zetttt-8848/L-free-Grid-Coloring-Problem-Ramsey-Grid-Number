# MapleCM worker disposition

The file `n21_stage2_maplecm.json` is an interrupted checkpoint, not a completed
worker result.  It contains five fully returned 60-second records.  During the
sixth target, MapleCM failed to honor the live interrupt and the process was
stopped under R3-R5-E3.  Therefore its top-level `mathematical_status` remains
the checkpoint value `RUNNING`; no sixth record exists and no conclusion is
attached to the stopped call.

The final portfolio merge consumes only those five complete records.  Glucose3
starts at shard-1 target index 5 and supplies the other 19 records.  The merge
audit checks that the resulting `24+5+19=48` records match the immutable hard-
cube order set exactly, with neither omission nor duplication.

