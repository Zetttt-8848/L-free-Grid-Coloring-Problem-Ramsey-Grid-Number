# English-only repository policy

All tracked documentation, research notes, code comments, user-facing strings,
metadata, and filenames must use English. Mathematical symbols and established
names remain permitted. Run `python scripts/check_english_only.py` before
committing. The same check runs on pushes and pull requests, including decoded
JSON strings so Unicode escapes cannot conceal untranslated content.

The November 13, 2026 language conversion preserves the mathematical claims,
formulas, explicit coloring certificates, and numerical outcomes. Historical
manifests and source inventories still identify their original Git revisions:
their hashes are historical evidence, not fresh checks of translated prose.
Use the parent Git revision when reproducing those historical hash checks.
The English-only conversion does not assert a new mathematical result or a
fresh Lean build. The legacy witness cache helper now accepts its input path
as a command-line argument rather than an obsolete machine-specific path.

Git history is preserved. This policy applies to current tracked snapshots;
it does not rewrite earlier commits or their original evidence.
