@echo off
title Stop Pushti Study Hub Server
cd /d "%~dp0"

echo ==========================================================
echo       Stopping Pushti Study Hub Server on Port 8000
echo ==========================================================
echo.

set FOUND=0
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000 ^| findstr LISTENING') do (
    set FOUND=1
    echo Terminating PID %%a on port 8000...
    taskkill /f /pid %%a >nul 2>&1
)

:: Terminate any running tray controller
powershell -Command "Get-CimInstance Win32_Process -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like '*tray_controller*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }" >nul 2>&1

if "%FOUND%"=="1" (
    echo [SUCCESS] Localhost server stopped successfully!
) else (
    echo [INFO] No active server found on port 8000.
)

timeout /t 2 /nobreak >nul 2>&1
