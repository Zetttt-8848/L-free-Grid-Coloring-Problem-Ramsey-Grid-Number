#!/usr/bin/env python3
"""Draw the verified boundary obstruction and its same-boundary repair.

Reads witness_results.json and independently checks every displayed fact.
Matplotlib is only needed for rendering, not for mathematical verification.
"""

import argparse
from collections import defaultdict
from itertools import combinations
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def proper(colors):
    """Direct horizontal-leg enumeration of positive directed Ls."""
    corners = []
    rows = defaultdict(list)
    for x, y in colors:
        rows[y].append(x)
    for y, xs in rows.items():
        for x, v in combinations(sorted(xs), 2):
            r = (v, y + v - x)
            if r in colors:
                corner = ((x, y), (v, y), r)
                if len({colors[p] for p in corner}) != 2:
                    return False, corners
                corners.append(corner)
    return True, corners


def phi_q(colors, q):
    fibers = defaultdict(int)
    for (v, u), color in colors.items():
        if v in q and u in q:
            fibers[v - u] += 1 - 2 * color
    return sum(s * s for s in fibers.values())


def checked_input(report):
    marks = report["marks"]
    q = set(report["Q"])
    if q != {0, 1, 5, 6, 25, 26, 30, 31} or marks != sorted(q | {2}):
        raise ValueError("This figure is for the specified one-mark extension")
    rows = report["trap"]["rows"]
    cells = [(v, u) for v in marks for u in marks if u < v]
    if [len(row) for row in rows] != list(range(1, len(marks))):
        raise ValueError("Incomplete witness rows")
    colors = dict(zip(cells, map(int, "".join(rows))))
    valid, corners = proper(colors)
    if not valid or len(corners) != 33 or phi_q(colors, q) != 8:
        raise ValueError("The displayed witness does not validate")

    diagrams = [((2, 1), (6, 1), (6, 5)),
                ((2, 1), (26, 1), (26, 25))]
    internal = {p: c for p, c in colors.items() if p[0] in q and p[1] in q}
    for corner in diagrams:
        if corner not in corners or [colors[p] for p in corner] != [0, 0, 1]:
            raise ValueError("Displayed blocking corner is absent")
        proposed = internal.copy()
        proposed[corner[-1]] ^= 1
        if not proper(proposed)[0] or phi_q(proposed, q) != 4:
            raise ValueError("Displayed flip is not an internal descent")
        proposed = colors.copy()
        proposed[corner[-1]] ^= 1
        if proper(proposed)[0]:
            raise ValueError("Displayed flip is not blocked by the boundary")

    swapped = colors.copy()
    if [colors[p] for p in ((26, 1), (30, 5), (26, 25))] != [0, 1, 1]:
        raise ValueError("Displayed repair color labels do not match the witness")
    for p in ((26, 1), (30, 5)):
        swapped[p] ^= 1
    if not proper(swapped)[0] or phi_q(swapped, q) != 8:
        raise ValueError("Simultaneous swap does not preserve properness")
    repaired = swapped.copy()
    repaired[26, 25] ^= 1
    if not proper(repaired)[0] or phi_q(repaired, q) != 4:
        raise ValueError("Final descent does not reach balance")
    if any(colors[p] != repaired[p] for p in colors if p not in internal):
        raise ValueError("Displayed repair changed the boundary")
    return colors, diagrams


def draw_corner(ax, corner, colors, title):
    dark = "#253f50"
    muted = "#56656e"
    accent = "#ba5b30"
    xy = ((.12, .19), (.77, .19), (.77, .83))
    ax.plot([xy[0][0], xy[1][0], xy[2][0]],
            [xy[0][1], xy[1][1], xy[2][1]], color="#a7b2b9", lw=2.4, zorder=1)
    for pos, cell in zip(xy, corner):
        color = colors[cell]
        external = cell == (2, 1)
        ax.scatter(*pos, s=1150, facecolor=dark if color else "#eef1f3",
                   edgecolor=accent if external else "#a7b2b9",
                   linewidth=2.8 if external else 1, zorder=3)
        ax.text(*pos, str(color), ha="center", va="center", fontsize=19,
                color="white" if color else dark, zorder=4)
    ax.text(.12, -.035, "(2, 1)", ha="center", color=accent, fontsize=12)
    ax.text(.12, -.165, "external cell", ha="center", color=accent, fontsize=10)
    ax.text(.77, -.035, str(corner[1]), ha="center", color=muted, fontsize=12)
    ax.text(.77, 1.00, str(corner[2]), ha="center", color=dark, fontsize=12)
    ax.text(.56, .83, "1 → 0", ha="right", va="center", color=accent,
            fontsize=16, weight="semibold")
    ax.text(.56, .69, "proposed flip", ha="right", color=muted, fontsize=10)
    step = corner[1][0] - corner[0][0]
    ax.text(.445, .26, f"step {step}", ha="center", color=muted, fontsize=10)
    ax.set_title(title, loc="left", fontsize=15, weight="semibold", pad=18)
    ax.set_xlim(-.02, 1.02)
    ax.set_ylim(-.22, 1.11)
    ax.axis("off")


def main():
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=root / "witness_results.json")
    parser.add_argument("--output-dir", type=Path, default=root)
    args = parser.parse_args()
    report = json.loads(args.input.read_text())
    colors, diagrams = checked_input(report)
    plt.rcParams.update({"font.family": "DejaVu Sans", "svg.fonttype": "none",
                         "text.color": "#20323e", "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(12, 8.2), facecolor="white")
    fig.text(.07, .95, "One extra mark blocks descent", fontsize=25,
             weight="semibold", va="top")
    fig.text(.07, .895, "$Q = \\{0,1,5,6,25,26,30,31\\}$    |    Add mark 2    |    $\\Phi_Q = 8$",
             fontsize=12, color="#56656e")
    left = fig.add_axes([.07, .49, .39, .31])
    right = fig.add_axes([.57, .49, .39, .31])
    draw_corner(left, diagrams[0], colors, "Blocked descent at (6, 5)")
    draw_corner(right, diagrams[1], colors, "Blocked descent at (26, 25)")
    fig.text(.07, .43,
             "Either proposed flip would make its displayed L entirely color 0.",
             fontsize=12, color="#56656e")
    fig.add_artist(plt.Line2D([.07, .95], [.385, .385], transform=fig.transFigure,
                             color="#d8dee2", lw=1))
    fig.text(.07, .34, "Repair while keeping every external cell fixed", fontsize=17,
             weight="semibold")
    fig.text(.07, .28, "1  Swap simultaneously", fontsize=14, weight="semibold")
    fig.text(.07, .233, "(26, 1):  0 → 1     AND     (30, 5):  1 → 0", fontsize=12)
    fig.text(.07, .185, "$\\Phi_Q: 8 \\;\\to\\; 8$", fontsize=18, weight="semibold")
    fig.text(.60, .28, "2  Flip one cell", fontsize=14, weight="semibold")
    fig.text(.60, .233, "(26, 25):  1 → 0", fontsize=12)
    fig.text(.60, .185, "$\\Phi_Q: 8 \\;\\to\\; 4$", fontsize=18, weight="semibold")
    fig.text(.07, .105,
             "Both repair states are proper on all 36 source cells. The potential shown is for Q only.",
             fontsize=10.5, color="#56656e")
    fig.text(.07, .058,
             "L diagrams are normalized schematics, not to scale; labels give actual coordinates.\n"
             "Node labels are colors 0 and 1. Orange outlines identify the same external cell (2, 1).",
             fontsize=10, color="#56656e", linespacing=1.6)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "svg"):
        path = args.output_dir / ("boundary_obstruction." + ext)
        fig.savefig(path, dpi=220, bbox_inches="tight", pad_inches=.25)
        print(path)
    plt.close(fig)


if __name__ == "__main__":
    main()
