@echo off
title Stop Pushti Study Hub Server
echo Stopping Pushti Study Hub server on ports 8443 and 8000...

powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort 8443,8000 -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }"

echo Server stopped.
timeout /t 2 >nul
