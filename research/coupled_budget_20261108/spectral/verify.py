"""Exact formula checks and integrity audit; no LP/SDP solver is imported."""
import hashlib
import itertools
import json
from pathlib import Path
import platform

HERE = Path(__file__).resolve().parent


def audit():
    checked = 0
    for n in range(1, 8):
        for word in itertools.product(range(3), repeat=n):
            corr = [sum(word[x] == word[x+h] for x in range(n-h)) for h in range(n)]
            q = [2*n] + [3*corr[h]-(n-h) for h in range(1, n)]
            for z in itertools.product((-1, 0, 1), repeat=3):
                lhs = sum(z[i]*z[j]*q[abs(i-j)] for i in range(3) for j in range(3) if abs(i-j) < n)
                rhs = 0
                for c, d in ((0, 1), (0, 2), (1, 2)):
                    for x in range(-2, n):
                        v = sum(z[i]*((word[x+i] == c)-(word[x+i] == d)) for i in range(3) if 0 <= x+i < n)
                        rhs += v*v
                assert lhs == rhs and lhs >= 0
                checked += 1
    runs = []
    for stem, script, expected_n in (('scout492', 'scout.py', 492), ('joint464', 'joint_scout.py', 464)):
        source = HERE/script
        path = HERE/(stem+'.json')
        data = json.loads(path.read_text(encoding='utf-8'))
        assert data['script_sha256'] == hashlib.sha256(source.read_bytes()).hexdigest()
        assert data['n'] == expected_n
        assert data['status'] in ('SCOUT_ONLY', 'UNDECIDED_FLOATING_SCOUT')
        for z in data['integer_cut_vectors']:
            assert len(z) == expected_n and any(z)
            assert all(type(v) is int for v in z)
        runs.append({'path':path.name, 'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                     'source_sha256':data['script_sha256'], 'n':expected_n,
                     'integer_cuts':len(data['integer_cut_vectors']),
                     'elapsed_seconds':data['elapsed_seconds'],
                     'status':'UNDECIDED'})
    return {'status':'PASS', 'scope':'Exact identity and artifact integrity only; no bound improvement',
            'identity_cases':checked, 'runs':runs, 'python':platform.python_version(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == '__main__':
    result = audit()
    (HERE/'verification.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps(result))
