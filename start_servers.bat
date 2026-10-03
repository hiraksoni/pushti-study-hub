@echo off
title Pushti Study Hub - Development Server
cd /d "%~dp0"

echo ================================================================
echo    PUSHTI STUDY HUB - AUTOMATED ENVIRONMENT & SERVER LAUNCHER
echo ================================================================
echo.

:: 1. Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python was not found in your system PATH!
    echo Please install Python 3 from https://www.python.org/ or the Microsoft Store.
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

:: 2. Auto-install / verify dependencies from requirements.txt
echo [1/2] Verifying Python requirements...
python -m pip install -q -r requirements.txt
if %errorlevel% neq 0 (
    echo [WARNING] Some dependencies could not be installed automatically.
    echo Retrying with verbose output...
    python -m pip install -r requirements.txt
) else (
    echo [OK] All required dependencies verified.
)

echo.
echo [2/2] Starting Pushti Study Hub Dual-Protocol Server...
echo ================================================================
echo.

:: 3. Run the dual server (HTTPS: 8443 and HTTP: 8000)
python https_server.py
pause
