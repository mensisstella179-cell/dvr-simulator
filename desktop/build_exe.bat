@echo off
xcopy /E /I /Y ..\docs app >nul
if not exist .venv ( py -m venv .venv )
call .venv\Scripts\activate
pip install -r requirements.txt
pyinstaller --noconsole --onefile --name DVRSimulator --icon app.ico --add-data "app;app" main.py
echo Selesai: dist\DVRSimulator.exe
pause
