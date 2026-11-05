#!/usr/bin/env python3
"""Write the reproducibility and hash manifest for this independent review."""

from hashlib import sha256
import json
import platform
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def tree_digest(directory: Path) -> str:
    h = sha256()
    for path in sorted(p for p in directory.rglob("*") if p.is_file()):
        h.update(path.relative_to(directory).as_posix().encode("utf-8"))
        h.update(b"\0")
        h.update(bytes.fromhex(digest(path)))
    return h.hexdigest()


def main():
    review_files = [
        HERE / "audit_joint.py",
        HERE / "audit_four.py",
        HERE / "selftest.py",
        HERE / "make_manifest.py",
        HERE / "joint_audit.json",
        HERE / "four_audit.json",
        HERE / "REPORT.md",
    ]
    frozen_inputs = [
        ROOT / "joint" / "REPORT.md",
        ROOT / "joint" / "property.md",
        ROOT / "joint" / "PARAMETRIC_MODEL.md",
        ROOT / "joint" / "witness_464.json",
        ROOT / "joint" / "witness_464_window_ap5.json",
        ROOT / "joint" / "witness_464_parametric.json",
        ROOT / "joint" / "patterns_window13.json",
        ROOT / "joint" / "window13.json",
        ROOT / "four" / "R3_R4_REPORT.md",
        ROOT / "four" / "R3_R4_OBJECTIVE.md",
        ROOT / "four" / "r4_profile_endpoint_21991300.json",
    ]
    for suffix in ("", "_v2", "_v3", "_v4"):
        for ext in (".json", ".cnf", ".rup"):
            frozen_inputs.append(ROOT / "joint" / f"triangle_core{suffix}{ext}")
    manifest = {
        "reviewer": "lower_sol",
        "assignment": ["J", "F"],
        "verdicts": {"J": "PASS", "F": "PASS"},
        "python": sys.version,
        "platform": platform.platform(),
        "commands": [
            r"LOCAL_RESEARCH_ROOT\anaconda3\python.exe research_round3\audits\lower_sol\selftest.py",
            r"LOCAL_RESEARCH_ROOT\anaconda3\python.exe research_round3\audits\lower_sol\audit_joint.py",
            r"LOCAL_RESEARCH_ROOT\anaconda3\python.exe research_round3\audits\lower_sol\audit_four.py",
        ],
        "review_file_sha256": {str(p.relative_to(ROOT)): digest(p) for p in review_files},
        "principal_input_sha256": {str(p.relative_to(ROOT)): digest(p) for p in frozen_inputs},
        "window13_external_files": {
            "count": sum(1 for p in (ROOT / "joint" / "window13").iterdir() if p.is_file()),
            "tree_sha256": tree_digest(ROOT / "joint" / "window13"),
        },
    }
    (HERE / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "verdicts": manifest["verdicts"],
        "review_files": len(review_files),
        "principal_inputs": len(frozen_inputs),
        "window13_files": manifest["window13_external_files"]["count"],
    }, indent=2))


if __name__ == "__main__":
    main()
