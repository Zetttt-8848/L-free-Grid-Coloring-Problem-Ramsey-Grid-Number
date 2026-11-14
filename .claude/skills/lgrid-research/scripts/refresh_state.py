"""Compare the repository with the pinned research snapshot.

Read-only except for an optional `git fetch`. Prints what moved since the
snapshot recorded in ../references/pins.json so that a session rereads only
affected evidence. Standard library only.

    python .claude/skills/lgrid-research/scripts/refresh_state.py [--fetch] [--json]

Exit status 0 means every pin matches; 1 means a pin moved, disappeared, or
an unpinned branch carries new commits, so the corresponding lines of
references/state.md must be re-derived before they are relied on. Notices
(for example a working tree that is behind the checkpoint) do not change the
exit status: the snapshot is still valid, but local files may predate it.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]


def git(root, *args, check=True):
    done = subprocess.run(["git", *args], cwd=root, capture_output=True,
                          text=True, encoding="utf-8", errors="replace")
    if check and done.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {done.stderr.strip()}")
    return done.returncode, done.stdout.strip()


def rev(root, ref):
    code, out = git(root, "rev-parse", "--verify", "--quiet", ref + "^{commit}", check=False)
    return out if code == 0 else None


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--fetch", action="store_true", help="run git fetch --all --prune first")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    _, root = git(SKILL_DIR, "rev-parse", "--show-toplevel")
    pins = json.loads((SKILL_DIR / "references" / "pins.json").read_text(encoding="utf-8"))
    remote = pins["remote"]
    if args.fetch:
        git(root, "fetch", "--all", "--prune", check=False)

    report = {"snapshot_date": pins["snapshot_date"], "stale": [], "notices": []}
    head = rev(root, "HEAD")
    _, branch = git(root, "rev-parse", "--abbrev-ref", "HEAD")
    _, dirty = git(root, "status", "--porcelain")
    report["head"] = {"branch": branch, "commit": head,
                      "uncommitted_entries": len(dirty.splitlines())}

    checkpoint = pins["research_checkpoint"]
    tip = rev(root, checkpoint["ref"])
    code, _ = git(root, "merge-base", "--is-ancestor", checkpoint["commit"], "HEAD", check=False)
    report["head"]["contains_pinned_checkpoint"] = code == 0
    if code != 0:
        report["notices"].append(
            "HEAD does not contain the pinned research checkpoint: files in this "
            "working tree may predate the recorded results (state.md describes the "
            "checkpoint, not this tree). Read evidence with "
            f"`git show {checkpoint['commit'][:12]}:<path>` or use a worktree on the checkpoint.")

    moved = []
    for ref, pinned in pins["refs"].items():
        now = rev(root, ref)
        if now is None:
            moved.append({"ref": ref, "pinned": pinned, "now": None})
            report["stale"].append(f"{ref}: pinned ref no longer exists (deleted or renamed).")
        elif now != pinned:
            entry = {"ref": ref, "pinned": pinned, "now": now}
            code, _ = git(root, "merge-base", "--is-ancestor", pinned, now, check=False)
            entry["fast_forward"] = code == 0
            _, names = git(root, "diff", "--name-only", pinned, now, "--", *pins["watched_paths"], check=False)
            entry["changed_watched_files"] = names.splitlines()
            moved.append(entry)
            report["stale"].append(
                f"{ref}: moved {pinned[:12]} -> {now[:12]} "
                f"({'fast-forward' if entry['fast_forward'] else 'history diverged'}); "
                f"{len(entry['changed_watched_files'])} watched files changed.")
    report["moved_refs"] = moved

    _, listing = git(root, "for-each-ref", "--format=%(refname:short) %(objectname)",
                     f"refs/remotes/{remote}")
    new_refs = []
    for line in listing.splitlines():
        name, commit = line.rsplit(" ", 1)
        if name.endswith("/HEAD") or name == remote or name in pins["refs"]:
            continue
        code, _ = git(root, "merge-base", "--is-ancestor", commit, checkpoint["commit"], check=False)
        new_refs.append({"ref": name, "commit": commit, "already_in_checkpoint": code == 0})
        if code != 0:
            report["stale"].append(f"{name}: unpinned remote branch at {commit[:12]} with commits "
                                   "outside the pinned checkpoint; inspect before relying on state.md.")
    report["unpinned_remote_refs"] = new_refs

    if tip and tip != checkpoint["commit"]:
        report["stale"].append("The research checkpoint ref has moved: the baseline in state.md "
                               "must be re-derived from the changed files listed above.")

    skill_branch = pins.get("skill_branch")
    if skill_branch and rev(root, skill_branch):
        # Compare contents directly so that untracked copies (a working tree on
        # a branch that does not track the skills) are handled; whitespace and
        # line endings are ignored.
        _, names = git(root, "ls-tree", "-r", "--name-only", skill_branch, "--", *pins["skill_paths"])
        differing = []
        for name in names.splitlines():
            done = subprocess.run(["git", "show", f"{skill_branch}:{name}"], cwd=root, capture_output=True)
            local = Path(root) / name
            here = local.read_bytes() if local.is_file() else None
            if here is None or here.split() != done.stdout.split():
                differing.append(name)
        report["skill_copy_differs_from_branch"] = differing
        if differing:
            report["notices"].append(
                f"Skill files in this working tree differ from {skill_branch}: "
                + ", ".join(differing[:8]) + ". Reconcile before editing either copy.")

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        h = report["head"]
        print(f"Snapshot pinned on {report['snapshot_date']}")
        print(f"HEAD   {h['branch']} {h['commit']}  ({h['uncommitted_entries']} uncommitted entries)")
        print(f"       contains pinned research checkpoint: {h['contains_pinned_checkpoint']}")
        print(f"Checkpoint {checkpoint['ref']} pinned at {checkpoint['commit']}")
        for entry in moved:
            print(f"MOVED  {entry['ref']}: {entry['pinned'][:12]} -> {str(entry['now'])[:12]}")
            for name in entry.get("changed_watched_files", [])[:40]:
                print(f"         reread: {name}")
        for entry in new_refs:
            flag = "merged into checkpoint" if entry["already_in_checkpoint"] else "NOT in checkpoint"
            print(f"NEW    {entry['ref']} {entry['commit'][:12]} ({flag})")
        for line in report["notices"]:
            print(f"NOTICE {line}")
        if report["stale"]:
            print("\nSTALE - treat the affected lines of references/state.md as unverified:")
            for line in report["stale"]:
                print(f"  - {line}")
        else:
            print("\nAll pins match. state.md reflects the pinned evidence (still dated).")
    return 1 if report["stale"] else 0


if __name__ == "__main__":
    sys.exit(main())
