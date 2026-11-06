"""Render the verified fixed-boundary repair threshold as a static figure.

Matplotlib is needed only for rendering. All displayed values are read from
verification_results.json; reachable counts and balanced counts stay separate.
"""

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_series(report, key):
    data = report[key]
    radii = sorted(map(int, data))
    counts = []
    balanced = []
    for radius in radii:
        entry = data[str(radius)]
        count = entry["state_count"]
        targets = entry["phi_histogram"].get("4", 0)
        require(count == len(entry["q_words"]), "Reachable count disagrees with state list")
        require(count == sum(entry["phi_histogram"].values()), "Histogram total mismatch")
        require(bool(targets) == entry["contains_balanced_state"], "Balanced flag mismatch")
        counts.append(count)
        balanced.append(targets)
    return radii, counts, balanced


def panel(ax, radii, counts, balanced, title, ymax, yticks, total=None):
    navy = "#294c60"
    orange = "#bf612e"
    ax.axvspan(7.5, 8.45, color="#faeee5", zorder=0)
    ax.plot(radii, counts, color=navy, linewidth=2, zorder=3)
    ax.scatter(radii[:-1], counts[:-1], color=navy, s=42, zorder=4)
    ax.scatter([radii[-1]], [counts[-1]], color=orange, s=64, zorder=5)
    for x, y in zip(radii, counts):
        ax.annotate(f"{y:,}", (x, y), xytext=(0, 10), textcoords="offset points",
                    ha="center", fontsize=11, weight="semibold",
                    color=orange if x == 8 else navy)
    if total is not None:
        ax.axhline(total, color="#aab5bc", linestyle=(0, (4, 4)), linewidth=1, zorder=1)
        ax.text(1.02, total + 0.032 * ymax, f"All {total:,} legal states",
                fontsize=10, color="#65747d")
    ax.text(0.0, 1.12, title, transform=ax.transAxes, fontsize=14, weight="semibold")
    ax.set(xlim=(.65, 8.45), ylim=(0, ymax), xticks=radii, yticks=yticks)
    ax.set_ylabel("Reachable legal states", fontsize=11, labelpad=14)
    ax.tick_params(axis="both", labelsize=10, length=0, pad=7, colors="#52646e")
    ax.grid(axis="y", color="#e6ebee", linewidth=.7)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color("#c4cdd2")
    # Balanced counts are a separate statement, never the y-series.
    require(balanced[:-1] == [0] * (len(balanced) - 1), "An earlier radius reaches balance")
    ax.text(.02, .13 if total is not None else .83,
            "r = 1–7: no balanced state reached", transform=ax.transAxes,
            fontsize=10, color="#52646e", bbox={"facecolor": "white", "edgecolor": "none", "alpha": .95})
    ax.text(.985, .13, f"r = 8: {balanced[-1]} balanced states reached", transform=ax.transAxes,
            fontsize=10, color=orange, ha="right",
            bbox={"facecolor": "#faeee5", "edgecolor": "none", "alpha": .95})


def main():
    directory = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=directory / "verification_results.json")
    parser.add_argument("--output-dir", type=Path, default=directory)
    args = parser.parse_args()
    report = json.loads(args.input.read_text())
    require(report["status"] == "FINITE-CHECKED", "Verification did not pass")
    total = report["counts"]["same_boundary_legal_count"]
    targets = report["counts"]["balanced_count"]
    require(total == len(report["all_legal_q_words"]), "Group total mismatch")
    unrestricted = read_series(report, "unrestricted_components_by_max_block_size")
    monotone = read_series(report, "monotone_closures_by_max_block_size")
    require(unrestricted[0] == monotone[0] == list(range(1, 9)), "Unexpected radius range")
    require(unrestricted[2][-1] == monotone[2][-1] == targets, "Target count mismatch")
    path = report["shortest_minimum_radius_monotone_path"]
    potentials = [s["phi_Q"] for s in path["states"]]
    sizes = path["block_sizes"]
    require(potentials == [8, 8, 4] and sizes == [4, 8], "Unexpected displayed repair path")
    require([(a["q_word"] ^ b["q_word"]).bit_count()
             for a, b in zip(path["states"], path["states"][1:])] == sizes,
            "Path Hamming distances disagree with block sizes")

    plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": "#243945",
                         "axes.labelcolor": "#52646e", "svg.fonttype": "none"})
    fig = plt.figure(figsize=(12.2, 10.2), facecolor="white")
    fig.text(.08, .955, "An eight-cell move is necessary", fontsize=25,
             weight="semibold", va="top")
    fig.text(.08, .908, "For this fixed boundary and starting coloring",
             fontsize=13, color="#52646e")
    fig.text(.08, .874, f"{total:,} legal colorings share the boundary; {targets} are balanced ($\\Phi_Q=4$).",
             fontsize=12, color="#52646e")

    upper = fig.add_axes([.10, .565, .83, .23])
    lower = fig.add_axes([.10, .245, .83, .23])
    panel(upper, *unrestricted, "Potential may rise between moves", 1500,
          [0, 500, 1000, 1500], total=total)
    panel(lower, *monotone, "Potential never rises between moves", 180,
          [0, 50, 100, 150])
    lower.set_xlabel("Maximum number r of internal cells flipped simultaneously per move",
                     fontsize=11, labelpad=12)

    fig.text(.08, .158, "Verified path at the minimum radius", fontsize=13, weight="semibold")
    xpos = [.42, .64, .87]
    for x, p in zip(xpos, potentials):
        fig.text(x, .105, f"$\\Phi_Q={p}$", ha="center", fontsize=21,
                 color="#bf612e" if p == 4 else "#294c60")
    for x1, x2, size in zip(xpos, xpos[1:], sizes):
        fig.add_artist(FancyArrowPatch((x1 + .07, .116), (x2 - .07, .116),
                                      transform=fig.transFigure, arrowstyle="->",
                                      color="#7d8b94", mutation_scale=13, linewidth=1.2))
        fig.text((x1 + x2) / 2, .141, f"flip {size} cells", ha="center", fontsize=10, color="#52646e")
    fig.text(.08, .105, "Every intermediate coloring\nremains legal; the boundary stays fixed.",
             fontsize=10, color="#52646e", linespacing=1.45)
    fig.text(.08, .040,
             "Each plotted value counts all states reachable from the fixed starting coloring, including the start itself.\n"
             "The two panels use different vertical scales. These are exact finite-witness results, not universal repair bounds.",
             fontsize=9.5, color="#65747d", linespacing=1.5)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for extension in ("png", "svg"):
        target = args.output_dir / f"repair_barrier.{extension}"
        fig.savefig(target, dpi=210, bbox_inches="tight", pad_inches=.22, facecolor="white")
        print(target)
    plt.close(fig)


if __name__ == "__main__":
    main()
