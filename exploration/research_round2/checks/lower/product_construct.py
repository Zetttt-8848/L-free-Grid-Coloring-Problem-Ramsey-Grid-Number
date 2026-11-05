#!/usr/bin/env python3
"""Emit the extremal 3-by-3 separated cancellative product construction."""

from pathlib import Path


def main() -> int:
    n = 9
    u = [i % 3 for i in range(n)]
    v = [(i // 3) % 3 for i in range(n)]
    grid = [[(u[x] + v[y]) % 3 + 1 for y in range(n)] for x in range(n)]
    path = Path("research_round2/certificates/lower/product_n9_matrix.txt")
    path.write_text("\n".join(" ".join(map(str, row)) for row in grid) + "\n", encoding="ascii")
    print(f"n={n}; u={u}; v={v}; output={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
