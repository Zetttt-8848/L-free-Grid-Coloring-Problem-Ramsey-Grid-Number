# Computational provenance

The complete proof checker is the upstream
[DRAT-trim repository](https://github.com/marijnheule/drat-trim), pinned at
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`. It was compiled from unchanged
upstream source with GCC in the local MSYS2 UCRT64 toolchain:

```text
gcc -O2 -Dgetc_unlocked=getc -o drat-trim.exe drat-trim.c
```

The macro maps unlocked character input to ordinary character input for this
Windows build. It changes no proof rule. The executable SHA-256 is recorded
in finite_audit_results.json. No executable or tool installation is committed.
On other platforms use the upstream build instructions and record the resulting
executable hash; hashes need not agree across compiler/platform builds.

The final `.drat.xz` archives contain complete proof traces. The audit program
streams their expansion to a temporary directory and calls the full standard
checker, requiring both successful exit and `s VERIFIED`. It does not implement
or accept a partial DRAT rule set. Original and independently repeated logs
are retained. CNFs use canonical LF line endings; archive hashes identify the
original expanded proof bytes, including any platform line endings.

The discovery solver is PySAT's Glucose4 binding, one worker, with a
100,000-conflict limit per call. UNKNOWN is recorded as UNDECIDED. Both Windows
C runtimes are flushed after every solver call and before deleting its proof
file handle; without this, buffered output from earlier calls can contaminate
a later trace. The standard checker caught the initial bad trace, which was
replaced by fresh runs. Only successfully checked final traces are used.

Tool versions, source/data hashes, and Git-normalized artifact hashes are in
manifest.json. The exact external window matrices and their original pinned
URLs remain in ../r4_binary_compatibility_20261114/external_windows/.
