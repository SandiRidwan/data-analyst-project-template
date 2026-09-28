"""
explanations.py  —  NARASI "KENAPA · TUJUAN · DAMPAK"
=====================================================
STANDAR WAJIB (untuk semua project data analyst):
  Setiap chart & tabel di dashboard HARUS punya penjelasan yang menjawab:
    · KENAPA    — mengapa metrik/analisis ini dipilih (masalah & konteks)
    · TUJUAN    — pertanyaan bisnis apa yang dijawab
    · DAMPAK    — implikasi / keputusan / tindakan yang timbul
    · CARA BACA — panduan membaca grafik bila tidak intuitif

MENGAPA MODUL TERPISAH?
  - teks tetap terjaga walau kode berubah
  - konsisten lintas project (bisa disalin apa adanya)
  - mudah diterjemahkan
  - dapat diaudit: `python src/explanations.py` memverifikasi kelengkapan

CARA PAKAI
----------
Streamlit:      explanations.render("price_by_category", st=st)
README/report:  explanations.text("price_by_category")

TAMBAH ENTRI BARU: tambahkan kunci ke dict EXPLAIN dengan 3 field wajib.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Kunci = id elemen (samakan dengan id chart/tabel di dashboard).
# Nilai  = dict wajib berisi: judul, kenapa, tujuan, dampak (+baca opsional).
# ---------------------------------------------------------------------------
EXPLAIN: dict[str, dict] = {
    # -------------------- CONTOH (hapus/ganti sesuai project) -------------
    "kpi": {
        "judul": "Metrik Ringkas (KPI Band)",
        "kenapa": "Pembaca perlu konteks cepat sebelum masuk analisis detail; "
                  "angka tunggal yang tepat mencegah diskusi melebar.",
        "tujuan": "Menyajikan metrik inti project dalam satu pandangan.",
        "dampak": "Menjadi dasar cepat untuk diskusi & keputusan; perubahan "
                  "mengikuti filter menunjukkan sensitivitas.",
        "baca": "Setiap kartu = satu metrik + konteksnya.",
    },
    "main_trend": {
        "judul": "Tren Utama",
        "kenapa": "Menangkap pola jangka panjang yang tidak terlihat dari angka "
                  "ringkas; sering jadi titik masuk seluruh analisis.",
        "tujuan": "Menjawab: bagaimana besaran utama berubah sepanjang waktu?",
        "dampak": "Menentukan apakah perlu perhatian/intervensi, dan menjadi "
                  "dasar proyeksi.",
        "baca": "Sumbu-X = waktu; sumbu-Y = besaran utama. Bagian yang disorot "
                "menandai peristiwa penting.",
    },
    "distribution": {
        "judul": "Distribusi",
        "kenapa": "Rata-rata bisa menyesatkan; distribusi mengungkap sebaran, "
                  "pencilan, dan kelompok tersembunyi.",
        "tujuan": "Menjawab: bagaimana data tersebar & apakah ada anomali?",
        "dampak": "Menentukan apakah analisis lanjutan perlu segmentasi, atau "
                  "apakah ada outlier yang harus diselidiki.",
        "baca": "Batang/histogram = frekuensi per rentang nilai.",
    },
    "breakdown": {
        "judul": "Rincian per Segmen",
        "kenapa": "Membandingkan agregat menyembunyikan perbedaan antar-kelompok "
                  "yang justru paling penting.",
        "tujuan": "Menjawab: kelompok mana yang menyumbang paling besar/kecil?",
        "dampak": "Menentukan prioritas sumber daya; segmen dominan = fokus, "
                  "segmen kecil = peluang.",
        "baca": "Panjang batang = nilai per segmen, diurutkan untuk mempermudah "
                "perbandingan.",
    },
    "correlation": {
        "judul": "Korelasi Antar-Variabel",
        "kenapa": "Variabel jarang berdiri sendiri; korelasi mengungkap mana yang "
                  "bergerak bersama.",
        "tujuan": "Menjawab: variabel mana yang berhubungan, dan seberapa kuat?",
        "dampak": "Memandu hipotesis & intervensi. INGAT: korelasi ≠ kausalitas.",
        "baca": "Warna & angka = koefisien (−1 … +1); semakin jauh dari 0 "
                "semakin kuat.",
    },
    "forecast": {
        "judul": "Proyeksi",
        "kenapa": "Perencanaan butuh pandangan ke depan, bukan hanya data historis.",
        "tujuan": "Menjawab: nilai apa yang wajar diharapkan beberapa periode ke depan?",
        "dampak": "Dasar anggaran/strategi. Selalu sertakan metrik akurasi (mis. "
                  "MAPE/R²) agar tingkat kepercayaan jelas.",
        "baca": "Garis = aktual; garis putus-putus = proyeksi; pita = rentang "
                "ketidakpastian.",
    },
}


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------
def text(key: str) -> str:
    """Teks polos (untuk README / report)."""
    e = EXPLAIN.get(key)
    if not e:
        return ""
    parts = [f"**{e['judul']}**",
             f"- **Kenapa:** {e['kenapa']}",
             f"- **Tujuan:** {e['tujuan']}",
             f"- **Dampak:** {e['dampak']}"]
    if e.get("baca"):
        parts.append(f"- **Cara baca:** {e['baca']}")
    return "\n".join(parts)


def render(key: str, expanded: bool = False, st=None):
    """Kotak penjelasan Streamlit (collapsible)."""
    if st is None:
        import streamlit as st  # noqa: PLC0415
    e = EXPLAIN.get(key)
    if not e:
        return
    with st.expander(f"💡 {e['judul']} — Kenapa · Tujuan · Dampak",
                     expanded=expanded):
        st.markdown(
            f"**🔎 Kenapa** — {e['kenapa']}\n\n"
            f"**🎯 Tujuan** — {e['tujuan']}\n\n"
            f"**📈 Dampak** — {e['dampak']}")
        if e.get("baca"):
            st.caption(f"👁️ Cara baca: {e['baca']}")


def audit(verbose: bool = True) -> bool:
    """Verifikasi setiap entri punya kenapa/tujuan/dampak. True bila semua OK."""
    ok = True
    for k, v in EXPLAIN.items():
        miss = [f for f in ("kenapa", "tujuan", "dampak") if not v.get(f)]
        if miss:
            ok = False
            if verbose:
                print(f"  MISSING {k}: {miss}")
    if verbose:
        print(f"Penjelasan: {len(EXPLAIN)} | "
              f"{'SEMUA LENGKAP' if ok else 'ADA YANG KURANG'}")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if audit() else 1)
