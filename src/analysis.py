"""
analysis.py — TEMPLATE analisis (logika MURNI, tanpa plotting).

PRINSIP:
  - Setiap fungsi mengembalikan DataFrame/skalar (siap dipakai ulang).
  - Tidak ada kode plotting di sini (dipisah ke make_charts.py).
  - Setiap fungsi diberi docstring yang jelas: apa & mengapa.
  - Data → proses → hasil; jejak dapat diaudit.

Ganti  # TODO  dengan analisis yang relevan bagi datamu.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import DATA_RAW, DATA_PROC  # noqa: E402

RAW_FILE = DATA_RAW / "raw_data.csv"


# ---------------------------------------------------------------------------
# 1. Load & bersihkan
# ---------------------------------------------------------------------------
def load() -> pd.DataFrame:
    """
    Muat data mentah dan lakukan pembersihan dasar.

    Langkah: buang duplikat, tangani nilai hilang, perbaiki tipe.
    Dokumentasikan SETIAP pembersihan agar dapat diaudit (jangan silent).
    """
    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"{RAW_FILE} tidak ada. Jalankan dulu: python src/collect_data.py")
    df = pd.read_csv(RAW_FILE)

    n0 = len(df)
    df = df.drop_duplicates()
    # TODO: pembersihan spesifik project
    # df["tanggal"] = pd.to_datetime(df["tanggal"], errors="coerce")
    # df = df.dropna(subset=["nilai_utama"])

    print(f"[load] {n0:,} baris mentah → {len(df):,} setelah pembersihan")
    return df


# ---------------------------------------------------------------------------
# 2. Analisis (contoh — ganti sesuai project)
# ---------------------------------------------------------------------------
def summary_metric(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """
    Ringkas metrik per grup: jumlah, median, rata-rata, sebaran.

    Median dipakai (bukan hanya rata-rata) karena lebih tahan terhadap
    pencilan — praktik standar untuk perbandingan antar-kelompok.
    """
    g = df.groupby(group_col)[value_col]
    out = pd.DataFrame({
        "jumlah": g.size(),
        "median": g.median().round(2),
        "rata2": g.mean().round(2),
        "p10": g.quantile(0.10).round(2),
        "p90": g.quantile(0.90).round(2),
    }).sort_values("median", ascending=False)
    return out


def trend(df: pd.DataFrame, time_col: str, value_col: str) -> pd.DataFrame:
    """Agregasi nilai per waktu (untuk chart tren)."""
    d = df.copy()
    d[time_col] = pd.to_datetime(d[time_col], errors="coerce")
    d = d.dropna(subset=[time_col])
    out = (d.groupby(d[time_col].dt.to_period("M"))[value_col]
           .sum().reset_index())
    out[time_col] = out[time_col].astype(str)
    return out


def correlation_matrix(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """Matriks korelasi Pearson antar kolom numerik terpilih."""
    cols = [c for c in cols if c in df.columns]
    return df[cols].corr(numeric_only=True).round(2)


def key_insights(df: pd.DataFrame) -> dict:
    """Ringkasan insight untuk laporan (hitung metrik kunci)."""
    return {
        "jumlah_baris": int(len(df)),
        "jumlah_kolom": int(df.shape[1]),
        # TODO: tambah metrik inti project, mis.:
        # "total_nilai": round(float(df["nilai"].sum()), 2),
        # "median": round(float(df["nilai"].median()), 2),
    }


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    df = load()
    print("\n=== INSIGHT ===")
    for k, v in key_insights(df).items():
        print(f"  {k:20}: {v}")
