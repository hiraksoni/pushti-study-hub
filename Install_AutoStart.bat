@echo off
title Enable Auto-Start on Windows Boot
cd /d "%~dp0"
echo ==========================================================
echo       Setting Pushti Study Hub to Start with Windows
echo ==========================================================
echo.

powershell -Command "$ws = New-Object -COM WScript.Shell; $startup = [Environment]::GetFolderPath('Startup'); $s = $ws.CreateShortcut($startup + '\PushtiStudyHub.lnk'); $s.TargetPath = '%~dp0Start_Pushti_Tray.vbs'; $s.WorkingDirectory = '%~dp0'; $s.Save(); Write-Host '[SUCCESS] Pushti Study Hub will now start silently in system tray when Windows boots!' -ForegroundColor Green"

echo.
pause
