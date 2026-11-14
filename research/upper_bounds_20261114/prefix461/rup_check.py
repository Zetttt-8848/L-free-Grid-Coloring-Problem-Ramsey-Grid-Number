"""Forward RUP (reverse unit propagation) checker for DRUP refutations.

Semantics checked: start from the input clauses; process the proof in order;
an added clause C must be RUP with respect to the current clause set
(assigning every literal of C false and unit-propagating yields a conflict);
a deletion line 'd C' removes one copy of C.  The refutation is accepted only
if the empty clause is added (or the current set is already conflicting
under unit propagation).  Deleting clauses can only weaken the set, so
accepting deletions is sound for UNSAT.  RAT steps are not accepted.

This is a deliberately simple, slow, independent implementation (no
backward core trimming, no RAT), written for this review.
"""
from collections import defaultdict


class RUPChecker:
    def __init__(self, nvars):
        self.n = nvars
        self.clauses = {}            # id -> list of literals (watch positions 0,1)
        self.watch = defaultdict(list)
        self.units = []              # ids of unit clauses
        self.next_id = 0
        self.index = defaultdict(list)   # sorted tuple -> list of ids
        self.empty_present = False

    def add(self, lits):
        lits = list(dict.fromkeys(lits))
        cid = self.next_id
        self.next_id += 1
        self.clauses[cid] = lits
        self.index[tuple(sorted(lits))].append(cid)
        if len(lits) == 0:
            self.empty_present = True
        elif len(lits) == 1:
            self.units.append(cid)
        else:
            self.watch[lits[0]].append(cid)
            self.watch[lits[1]].append(cid)

    def delete(self, lits):
        key = tuple(sorted(dict.fromkeys(lits)))
        ids = self.index.get(key)
        if not ids:
            return False
        cid = ids.pop()
        del self.clauses[cid]      # watch lists are cleaned lazily
        if cid in self.units:
            self.units.remove(cid)
        return True

    def propagate_conflict(self, assumptions):
        """True iff assigning `assumptions` true and propagating gives a conflict."""
        val = {}
        trail = []

        def assign(l):
            v = val.get(abs(l))
            if v is None:
                val[abs(l)] = l > 0
                trail.append(l)
                return True
            return v == (l > 0)

        for l in assumptions:
            if not assign(l):
                return True
        for cid in self.units:
            if not assign(self.clauses[cid][0]):
                return True
        head = 0
        while head < len(trail):
            falsified = -trail[head]
            head += 1
            wl = self.watch[falsified]
            keep = []
            conflict = False
            i = 0
            while i < len(wl):
                cid = wl[i]
                i += 1
                cl = self.clauses.get(cid)
                if cl is None or (cl[0] != falsified and cl[1] != falsified):
                    continue           # deleted, or stale watch
                if cl[0] == falsified:
                    cl[0], cl[1] = cl[1], cl[0]
                other = cl[0]
                ov = val.get(abs(other))
                if ov is not None and ov == (other > 0):
                    keep.append(cid)
                    continue
                found = False
                for j in range(2, len(cl)):
                    lj = cl[j]
                    vj = val.get(abs(lj))
                    if vj is None or vj == (lj > 0):
                        cl[1], cl[j] = cl[j], cl[1]
                        self.watch[cl[1]].append(cid)
                        found = True
                        break
                if found:
                    continue
                keep.append(cid)
                if ov is None:
                    assign(other)
                else:
                    conflict = True
                    keep.extend(wl[i:])
                    break
            self.watch[falsified] = keep
            if conflict:
                return True
        return False


def check(nvars, clauses, proof_lines):
    """proof_lines: iterable of strings in DRAT text format."""
    ck = RUPChecker(nvars)
    for cl in clauses:
        ck.add(cl)
    added = deleted = 0
    truncated = False
    if ck.empty_present or ck.propagate_conflict([]):
        return True, added, deleted
    for line in proof_lines:
        line = line.strip()
        if not line or line.startswith("c"):
            continue
        toks = line.split()
        is_del = toks[0] == "d"
        if is_del:
            toks = toks[1:]
        lits = [int(t) for t in toks] if toks else []
        if not lits or lits[-1] != 0:
            truncated = True     # an unterminated final line is ignored (sound:
            break                # every clause kept is implied by the input)
        lits = lits[:-1]
        if is_del:
            # Deletions are ignored.  Solvers may delete clauses that are still
            # reasons for root-level units (drat-trim also skips such deletions).
            # Keeping a clause is always sound: every stored clause is implied
            # by the input formula.
            deleted += 1
            continue
        if not ck.propagate_conflict([-l for l in lits]):
            raise ValueError(f"lemma {added} is not RUP: {lits[:12]}")
        added += 1
        if not lits:
            return True, added, deleted
        ck.add(lits)
    return ck.propagate_conflict([]), added, deleted


def parse_binary_drat(raw):
    """Parse binary DRAT bytes into text lines ('l1 l2 ... 0' / 'd ... 0')."""
    out = []
    i, n = 0, len(raw)
    while i < n:
        tag = raw[i]
        i += 1
        if tag not in (0x61, 0x64):
            raise ValueError(f"bad binary DRAT tag {tag} at byte {i-1}")
        lits = []
        while True:
            if i >= n:
                return out, True          # truncated final clause: ignored
            u, shift = 0, 0
            while True:
                if i >= n:
                    return out, True
                byte = raw[i]
                i += 1
                u |= (byte & 0x7F) << shift
                shift += 7
                if not byte & 0x80:
                    break
            if u == 0:
                break
            lits.append(-(u >> 1) if u & 1 else (u >> 1))
        out.append(("d " if tag == 0x64 else "") + " ".join(map(str, lits + [0])))
    return out, False


def solve_with_proof(nvars, clauses, name="cd19"):
    """Solve with PySAT's CaDiCaL 1.9.5 and return (sat, model or proof lines).

    The proof is read only after the native solver object has been destroyed,
    which flushes CaDiCaL's proof stream (reading it earlier truncates it).
    """
    import pysolvers  # native module shipped with python-sat
    from pysat.solvers import Solver
    assert name == "cd19"
    s = Solver(name=name, with_proof=True, bootstrap_with=clauses)
    sat = s.solve()
    if sat:
        model = s.get_model()
        s.delete()
        return True, model
    obj = s.solver
    pf = obj.prfile
    pysolvers.cadical195_del(obj.cadical, pf)
    obj.cadical = None
    pf.seek(0)
    raw = bytes(pf.read())
    pf.close()
    obj.prfile = None
    if raw[:1] in (b"a", b"d") and b"\n" not in raw[:64]:
        lines, _ = parse_binary_drat(raw)
    else:
        lines = raw.decode("ascii").splitlines()
    return False, lines


def dpll_completion(nvars, clauses, max_nodes=200000):
    """Return RUP lemmas (text lines) refuting `clauses` by a DPLL tree, or None.

    Each emitted lemma is the negation of a decision path whose extension by
    either value of the branch variable is refuted; emitted in post-order, so
    every lemma is RUP with respect to the clauses plus earlier lemmas.  The
    final lemma is the empty clause.  The lemmas are re-checked by check().
    """
    ck = RUPChecker(nvars)
    for cl in clauses:
        ck.add(cl)
    lemmas = []
    nodes = [0]

    def assigned(path):
        # unit propagation under the decision path; returns (conflict, values)
        val = {}
        for l in path:
            val[abs(l)] = l > 0
        changed = True
        while changed:
            changed = False
            for cl in ck.clauses.values():
                sat = False
                free = []
                for l in cl:
                    v = val.get(abs(l))
                    if v is None:
                        free.append(l)
                    elif v == (l > 0):
                        sat = True
                        break
                if sat:
                    continue
                if not free:
                    return True, val
                if len(free) == 1:
                    val[abs(free[0])] = free[0] > 0
                    changed = True
        return False, val

    def refute(path):
        nodes[0] += 1
        if nodes[0] > max_nodes:
            raise RuntimeError("node budget")
        if ck.propagate_conflict(list(path)):
            return
        conflict, val = assigned(path)
        if conflict:
            return
        # branch on the most frequent unassigned variable in short clauses
        score = {}
        for cl in ck.clauses.values():
            if any(val.get(abs(l)) == (l > 0) for l in cl):
                continue
            free = [l for l in cl if val.get(abs(l)) is None]
            for l in free:
                score[abs(l)] = score.get(abs(l), 0) + 2.0 ** (-len(free))
        x = max(score, key=score.get)
        for lit in (x, -x):
            refute(path + [lit])
            lemma = [-l for l in path + [lit]]
            lemmas.append(" ".join(map(str, lemma + [0])))
            ck.add(lemma)
        # now path itself is refuted by UP using the two lemmas just added

    try:
        refute([])
    except RuntimeError:
        return None
    lemmas.append("0")
    return lemmas
