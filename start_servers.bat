@echo off
title Pushti Study Hub - Local Development Server
echo ================================================================
echo Starting Pushti Study Hub HTTPS Development Server...
echo ================================================================
echo.
echo Local URLs:
echo   [HTTPS] https://localhost:8443/
echo   [HTTP]  http://localhost:8000/
echo.
echo Serving directory: %~dp0
echo.
cd /d "%~dp0"
python https_server.py
pause
