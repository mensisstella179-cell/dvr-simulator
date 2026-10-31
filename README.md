# Simulasi Dynamic Voltage Restorer (DVR)

Simulasi interaktif untuk memahami cara DVR mengatasi **sag, swell, dan interupsi** tegangan pada sistem tenaga listrik. Dibuat untuk proyek PBL Kualitas Daya.

**Buka langsung:** https://mensisstella179-cell.github.io/dvr-simulator/

## Cara memakai (pilih salah satu)

### 1. Link web atau aplikasi terpasang (disarankan)
Paling mudah dan paling kecil risikonya. Tidak perlu mengunduh file apa pun.

| Perangkat | Langkah |
|---|---|
| **Android** | Buka link di Chrome, ketuk menu ⋮, lalu **Instal aplikasi** |
| **Windows** | Buka link di Chrome atau Edge, lalu klik ikon instal di kotak alamat |
| **iPhone / Mac / lainnya** | Buka link di browser (Safari, Chrome, Edge) |

Setelah dibuka sekali, aplikasi bisa dipakai tanpa internet.

### 2. Pintasan Windows (offline, tanpa instalasi)
1. Buka halaman [Releases](../../releases) dan unduh `dvr-windows-launcher.zip`.
2. Klik kanan zip, pilih **Extract All**.
3. Klik dua kali `Buka-DVR-Simulator.bat`. Simulasi terbuka di jendela aplikasi Edge atau Chrome.

### 3. Aplikasi desktop `.exe` (eksperimen)
1. Di halaman [Releases](../../releases), unduh `DVRSimulator-windows.zip`.
2. Ekstrak, lalu jalankan `DVRSimulator.exe` di dalam folder.
3. Jika Windows menampilkan peringatan SmartScreen: **More info → Run anyway**.

Jika `.exe` diblokir antivirus atau gagal terbuka (error `Python.Runtime`), pakai cara 1 atau 2. Versi ini bergantung pada komponen .NET dan tidak berjalan di semua komputer.

## Isi aplikasi
- Simulasi gelombang dan RMS, deteksi sag/swell/interupsi, kompensasi DVR dengan batas V_max, kVA, arus, dan energi DC
- Model jaringan: gangguan 3 fasa, antar fasa, dan 1 fasa–tanah (komponen simetris)
- 11 skenario siap pakai, uji otomatis, dan laporan otomatis dengan verifikasi hitung manual
- Panduan interaktif 🧭 untuk pengguna baru

## Batasan model
Model edukatif: DVR dianggap sumber tegangan seri ideal. Inverter, trafo injeksi, rugi-rugi, PLL, switching, dan lompatan fasa tidak dimodelkan. Gangguan memakai pendekatan Thevenin (arus sebelum gangguan diabaikan). Hasil belum dibandingkan dengan simulator rangkaian seperti Simulink atau PSCAD. **Bukan alat desain sistem nyata.**

## Struktur repositori
- `docs/` aplikasi web (PWA), sekaligus sumber GitHub Pages
- `desktop/` pembungkus Python (pywebview) untuk `.exe`
- `.github/workflows/` pembangunan `.exe` otomatis di GitHub

## Pengembang
- Jalankan lokal: buka `docs/index.html` di browser.
- Versi desktop: `desktop\run.bat` (Windows).
- Setelah mengubah `docs/index.html`, naikkan nama cache di `docs/sw.js` (misalnya `dvr-v7-5` menjadi `dvr-v7-6`) agar pengguna yang sudah memasang mendapat versi terbaru.
