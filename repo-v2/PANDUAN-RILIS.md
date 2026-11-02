# Panduan rilis: dari ZIP sampai bisa diunduh orang lain

Tidak perlu memasang apa pun di komputer. Semua bisa lewat browser.

## A. Buat repositori GitHub
1. Daftar/masuk di github.com.
2. Klik **+ → New repository**. Nama: `dvr-simulator`. Pilih **Public**. Klik **Create repository**.
3. Ekstrak `dvr-simulator-repo.zip` di komputer.
4. Di halaman repositori klik **uploading an existing file**, lalu seret **isi** folder (docs, desktop, .github, README.md, .gitignore, PANDUAN-RILIS.md). Pastikan folder `.github` ikut terunggah. Jika folder tersembunyi tidak ikut terseret, pakai GitHub Desktop atau `git push`.
5. Klik **Commit changes**.

## B. Aktifkan link web (GitHub Pages)
1. **Settings → Pages**.
2. Source: **Deploy from a branch**. Branch: **main**, folder: **/docs**. Klik **Save**.
3. Tunggu 1–2 menit. Link muncul: `https://USERNAME.github.io/dvr-simulator/`
4. Buka di HP (Chrome) lalu uji **Instal aplikasi**.
5. Ganti `USERNAME` dan `NAMA-REPO` di `README.md` dengan link Anda.

## C. Buat file .exe otomatis (tanpa Windows)
1. Tab **Actions**: jika diminta, klik **I understand my workflows, enable them**.
2. Pilih **Build DVRSimulator.exe → Run workflow** untuk uji coba. Setelah hijau (±3–5 menit), unduh dari **Artifacts**.
3. Untuk rilis resmi: **Releases → Draft a new release → Choose a tag**, ketik `v7.3.0`, **Create new tag**, lalu **Publish release**. Workflow berjalan dan melampirkan `DVRSimulator.exe` ke halaman rilis.
4. Bagikan link halaman Releases ke pengguna.

## D. Memperbarui aplikasi
1. Ganti `docs/index.html` dengan versi baru (edit file di GitHub atau unggah ulang).
2. Naikkan nama cache di `docs/sw.js` (mis. `dvr-v7-5` → `dvr-v7-6`) agar pengguna PWA mendapat versi terbaru.
3. Untuk `.exe` baru, buat Release dengan tag baru (`v7.3.1`, dst.).

## E. Masalah yang sering muncul
- **SmartScreen memperingatkan .exe:** wajar untuk aplikasi tanpa tanda tangan digital. Beri tahu pengguna: More info → Run anyway.
- **Antivirus menandai .exe:** hapus `--onefile` pada perintah build, bagikan hasil folder `dist` dalam zip.
- **Jendela kosong di Windows:** pasang Microsoft Edge WebView2 Runtime.
- **Link Pages 404:** pastikan folder yang dipilih `/docs` dan `index.html` ada di dalamnya.
- **Tombol Instal tidak muncul di Android:** pastikan membuka lewat `https://` dan memakai Chrome.
