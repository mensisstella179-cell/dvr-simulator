@echo off
if not exist ..\docs\index.html ( echo Folder docs tidak ditemukan & pause & exit /b 1 )
xcopy /E /I /Y ..\docs app >nul
if not exist .venv ( py -m venv .venv )
call .venv\Scripts\activate
pip install -r requirements.txt
python main.py
