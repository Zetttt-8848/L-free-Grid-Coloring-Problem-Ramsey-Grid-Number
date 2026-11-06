"""Render the two verified complete source colorings as static index tables.

Run after verify.py has produced results.json. Requires matplotlib; the
mathematical verification itself does not depend on this presentation script.
"""

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def draw_table(ax, marks, coloring, title):
    rows = coloring["rows"]
    if len(rows) != len(marks) - 1 or any(
        len(row) != i + 1 or set(row) - {"0", "1"}
        for i, row in enumerate(rows)
    ):
        raise ValueError("Rows must give every strict-source cell exactly once")
    size = len(rows)
    for row_index, row in enumerate(rows):
        for column_index, color in enumerate(row):
            dark = color == "1"
            ax.add_patch(
                Rectangle(
                    (column_index - 0.5, row_index - 0.5),
                    1,
                    1,
                    facecolor="#253f50" if dark else "#edf0f1",
                    edgecolor="white",
                    linewidth=2.0,
                )
            )
            ax.text(
                column_index,
                row_index,
                color,
                ha="center",
                va="center",
                fontsize=16,
                weight="medium",
                color="white" if dark else "#253f50",
            )
    ax.set_xlim(-0.5, size - 0.5)
    ax.set_ylim(size - 0.5, -0.5)
    ax.set_aspect("equal")
    ax.set_xticks(range(size), marks[:-1])
    ax.set_yticks(range(size), marks[1:])
    ax.xaxis.tick_top()
    ax.tick_params(axis="both", length=0, labelsize=11, pad=9, colors="#384954")
    ax.set_xlabel("Column mark $u$", fontsize=11, color="#52616a", labelpad=11)
    ax.xaxis.set_label_position("top")
    ax.set_ylabel("Row mark $v$", fontsize=11, color="#52616a", labelpad=12)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.figure.text(
        ax.get_position().x0, 0.835, title, fontsize=15, weight="semibold"
    )


def main():
    directory = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=directory / "results.json")
    parser.add_argument("--output-dir", type=Path, default=directory)
    args = parser.parse_args()
    report = json.loads(args.input.read_text())
    old = report["manuscript_coloring"]
    new = report["optimal_symbolic_coloring"]
    marks = report["marks"]
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "text.color": "#20323e",
            "svg.fonttype": "none",
            "savefig.facecolor": "white",
        }
    )
    fig = plt.figure(figsize=(12.4, 8.4), facecolor="white")
    fig.text(
        0.075,
        0.948,
        "Same source, fewer forcing relations",
        ha="left",
        va="top",
        fontsize=25,
        weight="semibold",
    )
    fig.text(
        0.075,
        0.893,
        "$A = \\{0, 1, 5, 6, 25, 26, 30, 31\\}$"
        f"     |     {report['M']} source cells, {report['T']} directed Ls",
        fontsize=12,
        color="#52616a",
    )
    left = fig.add_axes([0.075, 0.245, 0.365, 0.50])
    right = fig.add_axes([0.565, 0.245, 0.365, 0.50])
    draw_table(left, marks, old, "Manuscript construction")
    draw_table(right, marks, new, "Minimum-forcing construction")

    metrics = [
        ("FORCING EDGES", "forcing_edges"),
        ("SQUARED IMBALANCE  $\\Phi$", "phi"),
        ("MIXED CORNERS", "mixed_corners"),
    ]
    for x, (label, key) in zip([0.075, 0.39, 0.705], metrics):
        fig.text(x, 0.18, label, fontsize=10, color="#52616a")
        fig.text(
            x,
            0.13,
            f"{old[key]}  →  {new[key]}",
            fontsize=25,
            weight="semibold",
        )
    fig.text(
        0.075,
        0.065,
        "Complete index tables: row $v$, column $u$, with $u < v$. "
        "Equal table spacing does not represent geometric distance.",
        fontsize=10,
        color="#52616a",
    )
    fig.text(
        0.075,
        0.033,
        "Cell labels are colors 0 and 1. Both colorings contain no monochromatic directed L.",
        fontsize=10,
        color="#52616a",
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for extension in ("png", "svg"):
        target = args.output_dir / f"colorings.{extension}"
        fig.savefig(target, dpi=220, bbox_inches="tight", pad_inches=0.25)
        print(target)
    plt.close(fig)


if __name__ == "__main__":
    main()
