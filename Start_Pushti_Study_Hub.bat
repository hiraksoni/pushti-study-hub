@echo off
title Pushti Study Hub - Localhost Server Starter
cd /d "%~dp0"

echo ==========================================================
echo        Pushti Study Hub - Silent Background Server
echo ==========================================================
echo.

:: Check if port 8000 is already active
netstat -ano | findstr :8000 | findstr LISTENING >nul 2>&1
if %errorlevel% equ 0 (
    echo [STATUS] Server is ALREADY running silently on port 8000!
) else (
    echo [STATUS] Initiating Silent Background Server on port 8000...
    start "" pythonw "%~dp0run_background_server.py"
    timeout /t 1 /nobreak >nul 2>&1
)

echo [STATUS] Opening Pushti Study Hub in browser...
start http://localhost:8000
echo.
echo [STATUS] Server is running in the background with ZERO windows.
echo [INFO] Cannot be closed by mistake. Use Stop_Pushti_Server.bat to stop.
timeout /t 2 /nobreak >nul 2>&1
exit
