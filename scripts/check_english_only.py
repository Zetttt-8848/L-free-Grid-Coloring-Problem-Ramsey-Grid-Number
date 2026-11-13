"""Reject CJK ideographs in tracked names, UTF-8 text, and decoded JSON."""
import json
from pathlib import Path
import subprocess
import sys

def contains_ideograph(text):
    return any(0x3400 <= ord(c) <= 0x9fff or 0xf900 <= ord(c) <= 0xfaff
               or 0x20000 <= ord(c) <= 0x323af for c in text)

def strings(value):
    if isinstance(value,str):
        yield value
    elif isinstance(value,dict):
        for key,item in value.items():
            yield key
            yield from strings(item)
    elif isinstance(value,list):
        for item in value:
            yield from strings(item)

def main():
    root=Path(__file__).resolve().parents[1]
    paths=subprocess.check_output(['git','ls-files','-z'],cwd=root).decode('utf-8').split('\0')[:-1]
    failures=[]
    for name in paths:
        path=root/name
        if not path.exists():
            continue
        if contains_ideograph(name):
            failures.append((name,'filename'))
        try:
            text=path.read_bytes().decode('utf-8')
        except UnicodeDecodeError:
            continue
        if contains_ideograph(text):
            failures.append((name,'text'))
        if path.suffix=='.json':
            try:
                value=json.loads(text)
            except ValueError:
                continue
            if any(contains_ideograph(s) for s in strings(value)):
                failures.append((name,'decoded JSON'))
    for name,kind in failures:
        print(json.dumps({'file':name,'location':kind},ensure_ascii=True))
    print(f'English-only check: {len(paths)} tracked files, {len(failures)} violations')
    return bool(failures)

if __name__=='__main__':
    sys.exit(main())
