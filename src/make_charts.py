"""
make_charts.py — TEMPLATE visualisasi statis (PNG untuk laporan/slide).

Pisahkan presentasi dari analisis. Setiap chart diberi judul yang
menjelaskan TEMUAN, bukan sekadar judul deskriptif.

Jalankan: python src/make_charts.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analysis as A                          # noqa: E402
from config import FIGURES, COLORS as C       # noqa: E402

plt.rcParams.update({
    "figure.dpi": 130, "savefig.dpi": 130, "font.size": 10,
    "axes.titlesize": 12, "axes.titleweight": "bold",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.edgecolor": "#CCCCCC", "axes.grid": True, "grid.color": "#EEEEEE",
    "figure.facecolor": "white",
})


def _save(fig, name: str) -> None:
    fp = FIGURES / f"{name}.png"
    fig.tight_layout()
    fig.savefig(fp, bbox_inches="tight")
    plt.close(fig)
    print(f"  [fig] {fp.name}")


# ---------------------------------------------------------------------------
# TODO: ganti dengan chart sesuai project. Beri judul yang berisi temuan.
# ---------------------------------------------------------------------------
def chart_example_bar(df: pd.DataFrame, group_col: str, value_col: str) -> None:
    """Bar horizontal — perbandingan antar-kategori."""
    t = A.summary_metric(df, group_col, value_col).head(12).sort_values("median")
    fig, ax = plt.subplots(figsize=(9, 6))
    bars = ax.barh(t.index, t["median"], color=C["primary"], zorder=3)
    for b, v in zip(bars, t["median"]):
        ax.text(v + t["median"].max() * 0.01,
                b.get_y() + b.get_height() / 2, f"{v:,.1f}",
                va="center", fontsize=8, color=C["dark"])
    ax.set_xlabel(value_col)
    ax.set_title(f"{value_col} per {group_col}\n(median — tahan pencilan)")
    ax.grid(axis="y", visible=False)
    _save(fig, "01_example_bar")


def build_all() -> None:
    df = A.load()
    print("Membuat visualisasi...")
    # TODO: panggil chart-chart di sini
    # if "kategori" in df.columns and "harga" in df.columns:
    #     chart_example_bar(df, "kategori", "harga")
    print(f"[OK] {FIGURES}")


if __name__ == "__main__":
    build_all()
