@echo off
setlocal
echo ========================================================
echo  Starting IntrusionX - Network Intrusion Detection System
echo ========================================================

cd /d "%~dp0"

set PYTHON_EXEC=python
if exist "%~dp0.venv\Scripts\python.exe" (
    set "PYTHON_EXEC=%~dp0.venv\Scripts\python.exe"
) else if exist "%~dp0.venv312\Scripts\python.exe" (
    set "PYTHON_EXEC=%~dp0.venv312\Scripts\python.exe"
)

start "" http://localhost:8501
"%PYTHON_EXEC%" -m streamlit run ui_with_wireshark.py
pause
