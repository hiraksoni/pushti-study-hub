@echo off
title Stop Pushti Study Hub Server
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

if "%FOUND%"=="1" (
    echo [SUCCESS] Localhost server stopped successfully!
) else (
    echo [INFO] No active server found on port 8000.
)

ping -n 3 127.0.0.1 >nul
