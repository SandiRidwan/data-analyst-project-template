"""
Dashboard — TEMPLATE Streamlit (mengikuti standar portofolio).

Standar yang sudah DIPASANG:
  ✅ Setiap chart/tabel diberi penjelasan "Kenapa · Tujuan · Dampak"
     (via `explanations.render(...)`).
  ✅ Tema konsisten (warna dari config.py).
  ✅ Aman-terhadap-skema: bila kolom tidak ada, tampilkan pesan alih-alih crash.
  ✅ KPI band + sidebar filter + tab.

Jalankan: streamlit run app/dashboard.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import analysis as A                          # noqa: E402
import explanations as X                      # noqa: E402
from config import DATA_PROC, REPORTS, COLORS as C   # noqa: E402

st.set_page_config(page_title="Data Analyst Dashboard",
                   page_icon="📊", layout="wide",
                   initial_sidebar_state="expanded")


# ---------------------------------------------------------------------------
@st.cache_data(show_spinner="Memuat data...")
def load() -> pd.DataFrame:
    fp = DATA_PROC / "clean.csv"
    if not fp.exists():
        st.error("Data belum ada. Jalankan: `python src/collect_data.py` "
                 "lalu `python src/run_analysis.py`.")
        st.stop()
    return pd.read_csv(fp)


def style(fig, h: int = 430):
    fig.update_layout(
        height=h, margin=dict(l=10, r=10, t=54, b=10),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#D5DBE1"),
        title=dict(font=dict(size=16, color="#fff")),
        legend=dict(bgcolor="rgba(0,0,0,0)"))
    fig.update_xaxes(gridcolor="#2A3038", zeroline=False)
    fig.update_yaxes(gridcolor="#2A3038", zeroline=False)
    return fig


def kpi(col, label: str, value: str, sub: str, color: str) -> None:
    col.markdown(
        f"""<div style="background:#1A1F2B;border-left:4px solid {color};
        padding:14px 16px;border-radius:10px;height:112px;">
        <div style="color:#9AA7B4;font-size:.76rem;text-transform:uppercase;
        letter-spacing:.06em;">{label}</div>
        <div style="color:{color};font-size:1.7rem;font-weight:700;
        margin-top:6px;">{value}</div>
        <div style="color:#6B7885;font-size:.75rem;">{sub}</div></div>""",
        unsafe_allow_html=True)


# ---------------------------------------------------------------------------
df = load()

# ---- sidebar (TODO: sesuaikan filter dengan kolom datamu) ----------------
st.sidebar.markdown("### 🎛️ Filters")
st.sidebar.caption("TODO: tambahkan filter sesuai kolom data.")
st.sidebar.markdown("---")
st.sidebar.caption("Sumber data: TODO. Dokumentasikan keterbatasan di sini.")

# ---- header --------------------------------------------------------------
st.markdown(
    f"""<div style="background:linear-gradient(100deg,{C['primary']},{C['blue']});
    padding:22px 26px;border-radius:14px;margin-bottom:18px;">
    <div style="font-size:1.7rem;font-weight:800;color:white;">
    📊 [Judul Project]</div>
    <div style="color:#D7E4DC;font-size:.9rem;margin-top:4px;">
    [Deskripsi singkat] · by <b>Sandi Ridwan</b></div></div>""",
    unsafe_allow_html=True)

# ---- KPI band ------------------------------------------------------------
X.render("kpi", st=st)
k1, k2, k3, k4, k5 = st.columns(5)
_ins = A.key_insights(df)
kpi(k1, "Baris data", f"{len(df):,}", "total record", C["primary"])
# TODO: ganti 4 KPI berikut dengan metrik project
kpi(k2, "Kolom", f"{df.shape[1]}", "jumlah fitur", C["blue"])
kpi(k3, "—", "—", "TODO", C["accent"])
kpi(k4, "—", "—", "TODO", C["red"])
kpi(k5, "—", "—", "TODO", C["dark"])
st.write("")

# ---- tabs ----------------------------------------------------------------
t1, t2 = st.tabs(["📈 Overview", "🔍 Detail"])

with t1:
    # Setiap chart WAJIB didahului penjelasan: X.render("<key>", st=st)
    X.render("main_trend", st=st)
    st.info("TODO: isi chart tren utama di sini (plotly). "
            "Jangan lupa registrasi penjelasannya di src/explanations.py.")

with t2:
    X.render("distribution", st=st)
    st.info("TODO: isi chart/ tabel detail di sini.")

# ---- footer --------------------------------------------------------------
st.markdown(
    f"""<hr style="border-color:#2A3038;">
    <div style="color:{C['grey']};font-size:.8rem;text-align:center;">
    📊 [Judul Project] · data: TODO · dibuat dengan Streamlit + Plotly ·
    oleh <b>Sandi Ridwan</b><br>
    ⚠️ Sertakan disclaimer / keterbatasan di sini.</div>""",
    unsafe_allow_html=True)
