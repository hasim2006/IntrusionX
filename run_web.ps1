Write-Host "========================================================" -ForegroundColor Cyan
Write-Host " Starting IntrusionX - Network Intrusion Detection System" -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan

$ProjectDir = $PSScriptRoot
Set-Location $ProjectDir

$PythonExe = "python"
if (Test-Path "$PSScriptRoot\.venv\Scripts\python.exe") {
    $PythonExe = "$PSScriptRoot\.venv\Scripts\python.exe"
} elseif (Test-Path "$PSScriptRoot\.venv312\Scripts\python.exe") {
    $PythonExe = "$PSScriptRoot\.venv312\Scripts\python.exe"
}

Start-Process "http://localhost:8501"
& $PythonExe -m streamlit run ui_with_wireshark.py
