#!/usr/bin/env python3
"""Index every tracked blob at pinned Git refs without executing source code.

Inventory/parse success is not a proof audit or a certificate verdict. Outputs
use Git-blob bytes, so CRLF settings do not change source hashes.
"""

import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess


def git(root, *args, input=None):
    return subprocess.run(["git", "-C", str(root), *args], input=input,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          check=True).stdout


def build(root, refs):
    blobs, snapshots = {}, []
    for ref in refs:
        commit = git(root, "rev-parse", "--verify", ref + "^{commit}").decode().strip()
        tree = git(root, "ls-tree", "-r", "-z", "--full-tree", commit).split(b"\0")
        entries = []
        for entry in tree:
            if not entry:
                continue
            header, path = entry.split(b"\t", 1)
            mode, kind, oid = header.decode().split()
            path = path.decode("utf-8")
            if kind != "blob":
                raise ValueError(f"Non-blob entry requires separate review: {path}")
            blobs.setdefault(oid, {"paths": set()})["paths"].add(path)
            entries.append({"path": path, "blob": oid})
        snapshots.append(dict(ref=ref, commit=commit, file_count=len(entries), files=entries))
    ids = sorted(blobs)
    raw = git(root, "cat-file", "--batch", input=("\n".join(ids) + "\n").encode())
    pos = 0
    errors = []
    for oid in ids:
        end = raw.index(b"\n", pos)
        got, kind, size = raw[pos:end].decode().split()
        size = int(size)
        if got != oid or kind != "blob":
            raise ValueError("Unexpected cat-file response")
        data = raw[end + 1:end + 1 + size]
        pos = end + size + 2
        item = blobs[oid]
        item["paths"] = sorted(item["paths"])
        item.update(bytes=size, sha256=hashlib.sha256(data).hexdigest())
        try:
            text = data.decode("utf-8-sig")
        except UnicodeDecodeError:
            item["inspection"] = "binary-inventory-only"
            continue
        item.update(lines=len(text.splitlines()), inspection="structural-index-only")
        suffix = Path(item["paths"][0]).suffix.lower()
        try:
            if suffix == ".py":
                tree = ast.parse(text)
                item["declarations"] = [dict(name=n.name, line=n.lineno, kind=type(n).__name__)
                                        for n in ast.walk(tree)
                                        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
                item["imports"] = sorted({n.module or "" for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)}
                                          | {a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names})
            elif suffix == ".json":
                obj = json.loads(text)
                item["json_shape"] = list(obj) if isinstance(obj, dict) else dict(type=type(obj).__name__, length=len(obj) if isinstance(obj, list) else None)
            elif suffix == ".md":
                item["headings"] = [dict(line=i, text=s.strip()) for i, s in enumerate(text.splitlines(), 1)
                                    if re.match(r"^#{1,6} ", s)]
            elif suffix == ".lean":
                item["imports"] = re.findall(r"^import\s+(.*)$", text, re.M)
                item["declarations"] = [dict(kind=m.group(1), name=m.group(2), line=text.count("\n", 0, m.start()) + 1)
                                        for m in re.finditer(r"^\s*(?:private\s+|noncomputable\s+|protected\s+)*(theorem|lemma|def|structure|abbrev|axiom)\s+([^\s(:{]+)", text, re.M)]
            elif suffix == ".tex":
                item["labels"] = re.findall(r"\\label\{([^}]+)\}", text)
            elif suffix == ".cnf":
                item["dimacs_header"] = next((s for s in text.splitlines() if s.startswith("p cnf ")), None)
            elif suffix == ".cpp":
                item["includes"] = re.findall(r"^#include\s+(.*)$", text, re.M)
        except (SyntaxError, ValueError) as error:
            item["parse_error"] = str(error)
            errors.append(dict(paths=item["paths"], error=str(error)))
    counts = Counter(Path(p).suffix or "[none]" for snap in snapshots[:1] for p in (f["path"] for f in snap["files"]))
    return dict(schema_version=1, scope="Every blob indexed; no claim of line-by-line semantic review, fresh Lean build, or all historical searches rerun",
                snapshots=snapshots, unique_blob_count=len(blobs), first_snapshot_extensions=dict(sorted(counts.items())),
                parse_errors=errors, blobs=blobs)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--ref", action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = build(args.root.resolve(), args.ref)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(snapshots=[{k: v for k, v in s.items() if k != "files"} for s in report["snapshots"]],
                          unique_blobs=report["unique_blob_count"], parse_errors=report["parse_errors"]), ensure_ascii=False))


if __name__ == "__main__":
    main()
