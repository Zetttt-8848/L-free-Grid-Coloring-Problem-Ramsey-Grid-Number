#!/usr/bin/env python3
"""Reproduce every generated result in a temporary copy and compare bytes."""

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parents[2]
OUT = ROOT / "reproduction.json"
OUTPUTS = [
    "energy_results.json", "energy_verification.json",
    "kernel_results.json", "kernel_verification.json",
    "consumer_results.json", "consumer_verification.json",
    "kernel_3.json", "kernel_4.json", "kernel_5.json",
    "standard_3.json", "standard_4.json", "standard_5.json",
]


def main():
    for name in OUTPUTS:
        assert (ROOT / name).is_file(), name
    with tempfile.TemporaryDirectory(prefix=".tmp-kimi-r4-energy-",
                                     dir=WORKSPACE) as temporary:
        copy = Path(temporary) / "package"
        shutil.copytree(ROOT, copy)
        commands = [
            [sys.executable, "energy_probe.py"],
            [sys.executable, "verify_energy.py"],
            [sys.executable, "enumerate_kernels.py"],
            [sys.executable, "verify_kernels.py"],
            [sys.executable, "consumer_audit.py"],
            [sys.executable, "verify_consumer.py"],
        ]
        for command in commands:
            subprocess.run(command, cwd=copy, check=True,
                           stdout=subprocess.DEVNULL)
        checker = WORKSPACE / ".agents" / "skills" / "directed-l-grid-research" / "scripts" / "check_coloring.py"
        assert checker.is_file()
        for m in (3, 4, 5):
            subprocess.run([
                sys.executable, str(checker), str(copy / f"kernel_{m}.json"),
                "--output", str(copy / f"standard_{m}.json"),
            ], cwd=WORKSPACE, check=True, stdout=subprocess.DEVNULL)
        hashes = {}
        for name in OUTPUTS:
            expected = (ROOT / name).read_bytes()
            actual = (copy / name).read_bytes()
            assert actual == expected, name
            hashes[name] = hashlib.sha256(actual).hexdigest()
        assert copy.is_dir()
    removed = not Path(temporary).exists()
    assert removed
    result = {
        "status": "PASS",
        "python": sys.version.split()[0],
        "temporary_copy_reproduction": True,
        "byte_identical_output_files": OUTPUTS,
        "output_count": len(OUTPUTS),
        "temporary_directory_removed": removed,
        "sha256": hashes,
        "scope": "Clean-copy recomputation of all package outputs",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps({"status": "PASS", "byte_identical_outputs": len(OUTPUTS),
                      "temporary_directory_removed": removed}, indent=2))


if __name__ == "__main__":
    main()
