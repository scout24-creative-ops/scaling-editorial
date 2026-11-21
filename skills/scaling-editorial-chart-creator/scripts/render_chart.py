#!/usr/bin/env python3
"""Render exact supplied values as a simple branded editorial PNG."""
import json
import math
import sys
from decimal import Decimal
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parents[1]
SAND, INK, TEAL, BLUE = "#FBF8F6", "#333333", "#02A793", "#01A0D4"


def render(source, target):
    spec = json.loads(Path(source).read_text(encoding="utf-8"))
    for k in ("chart_type", "unit", "period", "source", "source_url", "data"):
        if k not in spec:
            raise ValueError(f"Missing {k}")
    kind, rows = spec["chart_type"], spec["data"]
    if kind not in ("bar", "line", "grouped-bar") or not isinstance(rows, list) or not 2 <= len(rows) <= 6:
        raise ValueError("Use bar, line or grouped-bar with 2–6 rows")
    if any(not isinstance(spec[k], str) or not spec[k].strip() for k in ("unit", "period", "source", "source_url")):
        raise ValueError("unit, period, source and source_url need text")
    series = spec.get("series_labels")
    if kind == "grouped-bar" and (not isinstance(series, list) or len(series) != 2 or any(not isinstance(s, str) or not s.strip() for s in series)):
        raise ValueError("Grouped bars need two named series, including a forecast label when applicable")
    labels, values = [], []
    for row in rows:
        label = row.get("label")
        if not isinstance(label, str) or not label.strip() or len(label) > 28:
            raise ValueError("Labels must contain 1–28 characters")
        value = row.get("values") if kind == "grouped-bar" else row.get("value")
        entries = value if kind == "grouped-bar" and isinstance(value, list) and len(value) == 2 else [value]
        if kind == "grouped-bar" and len(entries) != 2:
            raise ValueError("Each category needs exactly two values")
        if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in entries):
            raise ValueError("Every value must be a finite number")
        if kind in ("bar", "grouped-bar") and any(v < 0 for v in entries):
            raise ValueError("Negative bars are unsupported")
        labels.append(label)
        values.append(value)
    if len(set(labels)) != len(labels):
        raise ValueError("Duplicate labels")
    regular = ROOT / "assets/MakeItBetter-Regular.otf"
    bold = ROOT / "assets/MakeItBetter-Bold.otf"
    if not regular.exists() or not bold.exists():
        raise ValueError("Brand fonts missing")
    font, emphasis = FontProperties(fname=str(regular)), FontProperties(fname=str(bold))
    plt.rcParams.update({"text.color": INK, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK})
    fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
    fig.patch.set_facecolor(SAND)
    ax.set_facecolor(SAND)
    fig.subplots_adjust(left=.29 if kind == "grouped-bar" else (.24 if kind == "bar" else .12), right=.91, top=.82 if kind == "grouped-bar" else .87, bottom=.23)
    for edge in ("top", "right", "left"):
        ax.spines[edge].set_visible(False)
    ax.spines["bottom"].set_color(INK)
    def value_label(v):
        number = f"{Decimal(str(v)):,f}"
        return number.replace(",", "X").replace(".", ",").replace("X", ".") + " " + spec["unit"]
    if kind == "bar":
        ax.barh(range(len(rows)), values, height=.55, color=TEAL)
        ax.invert_yaxis()
        top = max(values)
        ax.set_xlim(0, top * 1.3 if top else 1)
        ax.set_yticks(range(len(rows)), labels, fontproperties=font, fontsize=30)
        ax.tick_params(axis="y", length=0, pad=14)
        ax.tick_params(axis="x", labelsize=24)
        for index, value in enumerate(values):
            ax.text(value + top * .02, index, value_label(value), va="center", fontproperties=emphasis, fontsize=27)
        ax.set_xlabel(spec["unit"], fontproperties=font, fontsize=23)
    elif kind == "grouped-bar":
        max_value = max(max(pair) for pair in values)
        for index, (first, second) in enumerate(values):
            ax.barh(index - .19, first, height=.32, color=BLUE)
            ax.barh(index + .19, second, height=.32, color=TEAL)
            ax.text(first + max_value * .015, index - .19, value_label(first), va="center", fontproperties=emphasis, fontsize=22)
            ax.text(second + max_value * .015, index + .19, value_label(second), va="center", fontproperties=emphasis, fontsize=22)
        ax.set_yticks(range(len(rows)), labels, fontproperties=font, fontsize=26)
        ax.invert_yaxis()
        ax.set_xlim(0, max_value * 1.24 if max_value else 1)
        ax.tick_params(axis="y", length=0, pad=14)
        ax.tick_params(axis="x", labelsize=22)
        ax.set_xlabel(spec["unit"], fontproperties=font, fontsize=22)
        handles = [plt.Rectangle((0, 0), 1, 1, color=BLUE), plt.Rectangle((0, 0), 1, 1, color=TEAL)]
        ax.legend(handles, series, loc="lower right", bbox_to_anchor=(1, 1.01), ncol=2, frameon=False, prop=font, fontsize=22)
    else:
        ax.plot(range(len(rows)), values, color=TEAL, linewidth=5, marker="o", markersize=14)
        ax.set_xticks(range(len(rows)), labels, fontproperties=font, fontsize=26)
        ax.tick_params(axis="y", labelsize=24)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g} {spec['unit']}"))
        spread = max(values) - min(values)
        ax.set_ylim(min(0, min(values) - spread * .2), max(values) + max(spread * .25, abs(max(values)) * .1, 1))
        for index, value in enumerate(values):
            ax.annotate(value_label(value), (index, value), xytext=(0, 18), textcoords="offset points", ha="center", fontproperties=emphasis, fontsize=25)
    fig.text(.06, .115, spec["period"], fontproperties=font, fontsize=25)
    fig.text(.06, .065, "Quelle: " + spec["source"], fontproperties=font, fontsize=24)
    dest = Path(target)
    if dest.suffix.lower() != ".png":
        raise ValueError("Output must be a PNG")
    dest.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(dest, dpi=100, facecolor=SAND)
    plt.close(fig)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: render_chart.py INPUT.json OUTPUT.png")
    render(sys.argv[1], sys.argv[2])
