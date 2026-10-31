# Simulasi Dynamic Voltage Restorer (DVR)

Simulasi interaktif untuk memahami cara DVR mengatasi **sag, swell, dan interupsi** tegangan pada sistem tenaga listrik. Dibuat untuk proyek PBL Kualitas Daya.

**Coba langsung:** https://USERNAME.github.io/NAMA-REPO/  *(ganti dengan link Anda)*

## Cara memakai

| Perangkat | Cara |
|---|---|
| Android | Buka link di Chrome, menu ⋮ → **Instal aplikasi** |
| Windows | Unduh `DVRSimulator.exe` di halaman [Releases](../../releases) dan jalankan. Jika muncul peringatan SmartScreen: **More info → Run anyway** |
| Komputer lain / iPhone | Buka link di browser (Chrome, Edge, Safari) |

Saat pertama dibuka, panduan 🧭 akan menuntun langkah demi langkah.

## Isi
- Simulasi gelombang dan RMS, deteksi sag/swell/interupsi, kompensasi DVR dengan batas V_max, kVA, arus, dan energi DC
- Model jaringan: gangguan 3 fasa, antar fasa, dan 1 fasa–tanah (komponen simetris)
- 11 skenario siap pakai, uji otomatis, dan laporan otomatis dengan verifikasi hitung manual

## Batasan model
Model edukatif: DVR dianggap sumber tegangan seri ideal; inverter, trafo injeksi, rugi-rugi, PLL, switching, dan lompatan fasa tidak dimodelkan. Gangguan memakai pendekatan Thevenin. **Bukan alat desain sistem nyata.**

## Struktur repositori
- `docs/` aplikasi web (PWA), sekaligus sumber GitHub Pages
- `desktop/` pembungkus Python (pywebview) untuk file `.exe`
- `.github/workflows/` build `.exe` otomatis di GitHub

## Pengembang
Jalankan lokal: buka `docs/index.html` di browser. Versi desktop: `desktop\run.bat` (Windows).
