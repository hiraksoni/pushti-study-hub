@echo off
title Disable Auto-Start on Windows Boot
cd /d "%~dp0"
echo ==========================================================
echo       Removing Pushti Study Hub from Windows Startup
echo ==========================================================
echo.

powershell -Command "$startup = [Environment]::GetFolderPath('Startup'); $target = $startup + '\PushtiStudyHub.lnk'; if (Test-Path $target) { Remove-Item $target -Force; Write-Host '[SUCCESS] Auto-start shortcut removed successfully.' -ForegroundColor Yellow } else { Write-Host '[INFO] No auto-start shortcut was found.' -ForegroundColor Cyan }"

echo.
pause
