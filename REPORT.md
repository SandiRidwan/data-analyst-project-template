# 📊 [Judul Project] — Laporan Analitik

> Ganti judul & isi sesuai project. Struktur ini mengikuti standar portofolio.

---

## 1. Ringkasan Eksekutif

[Dalam 3–5 baris: apa yang dianalisis, temuan terpenting, dan rekomendasi utama.]

**3 temuan utama:**
1. …
2. …
3. …

---

## 2. Data & Metodologi

| Aspek | Detail |
|-------|--------|
| Sumber | [URL/penyedia + lisensi] |
| Periode/Ukuran | [rentang / jumlah baris] |
| Pembersihan | [langkah utama yang dilakukan] |
| Metode analisis | [statistik/ML yang dipakai] |

> Dokumentasikan **setiap** keputusan pembersihan data — jangan ada yang tersembunyi.

---

## 3. Temuan

Untuk **setiap** chart/tabel, tulis tiga hal (sama seperti di dashboard):
**Kenapa · Tujuan · Dampak.**

### 3.1 [Nama Analisis]

![chart](../reports/figures/01_example.png)

- **Kenapa:** [mengapa metrik ini dipilih]
- **Tujuan:** [pertanyaan bisnis yang dijawab]
- **Dampak:** [implikasi / keputusan]

---

## 4. Rekomendasi

| # | Rekomendasi | Dasar | Ekspektasi dampak |
|---|-------------|-------|-------------------|
| R1 | … | … | … |
| R2 | … | … | … |

---

## 5. Keterbatasan (Jujur)

1. [Batasan data — mis. kolom hilang, sampel kecil, snapshot tunggal]
2. [Batasan metode — mis. proxy, asumsi]
3. [Hal yang belum tercakup]

> Menyembunyikan keterbatasan menurunkan kredibilitas. Tulis apa adanya.

---

## 6. Reproduksibilitas

```bash
python src/collect_data.py
python src/run_analysis.py
python src/make_charts.py
streamlit run app/dashboard.py
```

---

*Dibuat oleh Sandi Ridwan · [tanggal] · sumber data: [sumber]*
