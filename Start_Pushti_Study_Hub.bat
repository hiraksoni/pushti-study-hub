@echo off
title Pushti Study Hub - Localhost Server (Port 8000)
cd /d "d:\Users\expor\Downloads\Codes"

echo ==========================================================
echo        Pushti Study Hub - Localhost Server Starter
echo ==========================================================
echo.

:: Check if port 8000 is already active
netstat -ano | findstr :8000 | findstr LISTENING >nul 2>&1
if %errorlevel% equ 0 (
    echo [STATUS] Python server is ALREADY running on port 8000!
) else (
    echo [STATUS] Initiating Python HTTP Server on port 8000...
    start "Pushti Study Hub Server" /min cmd /c "python -m http.server 8000"
    ping -n 3 127.0.0.1 >nul
)

echo [STATUS] Opening Pushti Study Hub in browser...
start http://localhost:8000
echo.
echo ==========================================================
echo   Hub is live at: http://localhost:8000
echo ==========================================================
ping -n 3 127.0.0.1 >nul
