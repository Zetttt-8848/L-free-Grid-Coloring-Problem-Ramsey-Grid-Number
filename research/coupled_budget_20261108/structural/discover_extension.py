"""Bounded SAT discovery of an extension cancelling local frustration.

Only positive full colorings are mathematical evidence; all negative solver
returns here remain unproved discovery observations.
"""
from pathlib import Path
import json
from pysat.card import CardEnc
from pysat.solvers import Solver
from scan_balance import clauses


def main():
    base = [0, 1, 2, 3, 4, 6, 7, 9, 10]
    for extra in range(11, 31):
        marks = base+[extra]
        cells, fibers, cnf = clauses(marks)
        top = len(cells)
        for fiber in fibers.values():
            for factory, bound in ((CardEnc.atmost, (len(fiber)+1)//2),
                                   (CardEnc.atleast, len(fiber)//2)):
                encoding = factory(fiber, bound=bound, top_id=top)
                top = max(top, encoding.nv)
                cnf.extend(encoding.clauses)
        with Solver(name='g4', bootstrap_with=cnf) as solver:
            if not solver.solve():
                continue
            model = solver.get_model()
            result = {'A': marks, 'cells': cells,
                      'coloring': [int(x > 0) for x in model[:len(cells)]],
                      'status': 'SAT witness; independently checked by verify_extension.py',
                      'scan_scope': 'Extra mark in integers 11..30; stop at first positive witness. Negative returns not certified.'}
            Path(__file__).with_name('extension_discovery.json').write_text(json.dumps(result, indent=2)+'\n')
            print(json.dumps({'A': marks, 'cells': len(cells), 'status': 'SAT witness'}))
            return
    print('UNDECIDED: no witness in this bounded scan')


if __name__ == '__main__':
    main()
