@echo off
title Launch Hindi Chapters - Pushti Study Hub
cd /d "%~dp0"

echo ================================================================
echo           PUSHTI STUDY HUB - HINDI CHAPTERS LAUNCHER
echo ================================================================
echo.

:: Auto-verify requirements silently
python -m pip install -q -r requirements.txt >nul 2>&1

:: Check if server is already running on port 8443
powershell -NoProfile -Command "$t = New-Object Net.Sockets.TcpClient; try { $t.Connect('127.0.0.1', 8443); Write-Output 'RUNNING' } catch { Write-Output 'STOPPED' } finally { $t.Dispose() }" > "%TEMP%\psh_check.txt"
set /p STATUS=<"%TEMP%\psh_check.txt"
del "%TEMP%\psh_check.txt"

if "%STATUS%"=="STOPPED" (
    echo [INFO] Starting background server on https://localhost:8443 and http://localhost:8000...
    start "Pushti Study Hub Server" /min python https_server.py
    timeout /t 2 >nul
) else (
    echo [OK] Pushti Study Hub Server is already active.
)

echo.
echo Opening Hindi Chapter 1 in default browser...
start https://localhost:8443/chapters/hindi/hindi_ch1.html

echo.
echo [DIRECT LINKS]
echo   पाठ १: https://localhost:8443/chapters/hindi/hindi_ch1.html
echo   पाठ २: https://localhost:8443/chapters/hindi/hindi_ch2.html
echo   पाठ ३: https://localhost:8443/chapters/hindi/hindi_ch3.html
echo.
echo [ZERO-WARNING HTTP ALTERNATIVES]
echo   पाठ १: http://localhost:8000/chapters/hindi/hindi_ch1.html
echo   पाठ २: http://localhost:8000/chapters/hindi/hindi_ch2.html
echo   पाठ ३: http://localhost:8000/chapters/hindi/hindi_ch3.html
echo ================================================================
timeout /t 5
