<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=38&duration=3000&pause=1000&color=1F5C3D&center=true&vCenter=true&width=900&height=70&lines=DATA+ANALYST+PROJECT+TEMPLATE" alt="Template" />

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-1F5C3D?style=for-the-badge&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-0D1117?style=for-the-badge)

</div>

---

## 🎯 Apa ini?

**Boilerplate project data analyst** yang mengemas standar kualitas dari 4 project
portofolio nyata (Morrisons, Indonesia Economy, Horse Racing, Options). Gunakan
sebagai titik awal project baru agar **langsung mengikuti standar** — tidak perlu
mengulang keputusan struktur dari awal.

### Standar yang sudah tertanam

| # | Standar | Di mana |
|---|---------|---------|
| 1 | **Setiap chart/tabel punya penjelasan Kenapa · Tujuan · Dampak** | `src/explanations.py` + `app/dashboard.py` |
| 2 | **Analisis & presentasi dipisah** | `analysis.py` (murni) vs `make_charts.py`/`dashboard.py` |
| 3 | **Konfigurasi terpusat** (path, warna) | `src/config.py` |
| 4 | **Data mentah tak diubah** → diproses ke `data/processed/` | `collect_data.py` → `run_analysis.py` |
| 5 | **Dashboard tahan-skema** (tak crash bila kolom beda) | guard di `dashboard.py` |
| 6 | **Insight ringkas otomatis** (`summary.json`) | `run_analysis.py` |
| 7 | **Audit kelengkapan penjelasan** | `python src/explanations.py` |

---

## 📁 Struktur

```
data-analyst-project-template/
├── app/
│   ├── dashboard.py            # ⭐ dashboard Streamlit (standar terpasang)
│   └── .streamlit/config.toml
├── src/
│   ├── config.py               # path + palet warna (satu sumber kebenaran)
│   ├── collect_data.py         # TEMPLATE pengumpulan data
│   ├── analysis.py             # TEMPLATE analisis (murni)
│   ├── explanations.py         # WAJIB: narasi Kenapa-Tujuan-Dampak
│   ├── run_analysis.py         # orkestrator end-to-end
│   └── make_charts.py          # TEMPLATE visualisasi PNG
├── data/{raw,processed}/
├── reports/{figures,tables}/
├── docs/
│   └── DEPLOY_CHECKLIST.md     # ⚠️ baca sebelum deploy
├── REPORT.md
└── requirements.txt
```

---

## 🚀 Cara Pakai

```bash
# 1. Salin template
git clone <template> project-baru && cd project-baru

# 2. (opsional) mulai git baru
rm -rf .git && git init

# 3. Sesuaikan
#    - src/collect_data.py  -> sumber data project
#    - src/analysis.py      -> analisis
#    - src/explanations.py  -> narasi setiap chart/tabel   << JANGAN DILEWATKAN
#    - src/make_charts.py   -> visualisasi
#    - app/dashboard.py     -> dashboard
#    - README.md            -> ganti judul & temuan

# 4. Jalankan
python src/collect_data.py
python src/run_analysis.py
python src/make_charts.py
python src/explanations.py          # audit: semua entri lengkap?
streamlit run app/dashboard.py
```

---

## ✅ Checklist Sebelum Publish

- [ ] Setiap chart/tabel punya entri di `explanations.py`
- [ ] `python src/explanations.py` → "SEMUA LENGKAP"
- [ ] README berisi temuan nyata (bukan placeholder)
- [ ] `REPORT.md` diisi (termasuk **keterbatasan jujur**)
- [ ] Data yang diperlukan dashboard **sudah ter-commit** (lihat docs/DEPLOY_CHECKLIST.md)
- [ ] Tidak ada kredensial di repo (`.gitignore` memblokir)
- [ ] Dashboard diuji: **buka SETIAP tab** (jangan hanya tab pertama)

---

## 📖 Standar Penjelasan (Kenapa · Tujuan · Dampak)

Setiap visual WAJIB menjawab:

| Pertanyaan | Arti |
|-----------|------|
| **🔎 Kenapa** | Mengapa metrik/analisis ini dipilih (masalah & konteks) |
| **🎯 Tujuan** | Pertanyaan bisnis apa yang dijawab |
| **📈 Dampak** | Implikasi / keputusan / tindakan yang timbul |
| **👁️ Cara baca** | Panduan bila grafik tidak intuitif |

Tanpa ini, chart hanya "angka cantik" yang tidak bisa dipakai mengambil keputusan.

---

## 👤 Author

<div align="center">

**Sandi Ridwan** — Data Analyst · Data Automation Engineer

[GitHub](https://github.com/SandiRidwan) · [LinkedIn](https://linkedin.com/in/sandi-ridwan)

</div>

---

## 📄 License

MIT License.
