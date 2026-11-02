"""Simulasi Dynamic Voltage Restorer (DVR) - pembungkus desktop (pywebview).

Menjalankan app/index.html di jendela aplikasi sendiri (Edge WebView2 di Windows).
Jalankan:  python main.py
"""
import os
import sys
from pathlib import Path

import webview

JUDUL = "Simulasi Dynamic Voltage Restorer (DVR)"


def sumber(rel: str) -> Path:
    """Lokasi berkas, baik saat dijalankan biasa maupun setelah di-build PyInstaller."""
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return base / rel


def folder_data() -> Path:
    """Tempat penyimpanan data aplikasi (agar pengaturan dan status panduan tersimpan)."""
    root = Path(os.environ.get("LOCALAPPDATA") or Path.home())
    p = root / "DVRSimulator"
    p.mkdir(parents=True, exist_ok=True)
    return p


def main() -> None:
    index = sumber("app/index.html")
    if not index.exists():
        sys.exit(f"Berkas tidak ditemukan: {index}")

    try:  # izinkan unduhan (ekspor CSV/PNG) bila versi pywebview mendukung
        webview.settings["ALLOW_DOWNLOADS"] = True
    except Exception:
        pass

    webview.create_window(
        JUDUL,
        url=index.as_uri(),
        width=1280,
        height=800,
        min_size=(900, 600),
    )
    # private_mode=False + storage_path: localStorage tersimpan antar sesi
    webview.start(private_mode=False, storage_path=str(folder_data()))


if __name__ == "__main__":
    main()
