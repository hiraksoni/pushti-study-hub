# Pushti Study Hub - Windows System Tray Server Controller
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

function Start-PushtiServer {
    # Check if port 8000 is listening
    $active = Get-NetTCPConnection -LocalPort 8000 -State Listen -ErrorAction SilentlyContinue
    if (-not $active) {
        $pythonw = (Get-Command pythonw.exe -ErrorAction SilentlyContinue).Source
        if (-not $pythonw) {
            $pythonw = "pythonw.exe"
        }
        $serverScript = Join-Path $scriptDir "run_background_server.py"
        Start-Process -FilePath $pythonw -ArgumentList "`"$serverScript`"" -WorkingDirectory $scriptDir -WindowStyle Hidden
    }
}

function Stop-PushtiServer {
    try {
        $conns = Get-NetTCPConnection -LocalPort 8000 -State Listen -ErrorAction SilentlyContinue
        foreach ($conn in $conns) {
            if ($conn.OwningProcess) {
                Stop-Process -Id $conn.OwningProcess -Force -ErrorAction SilentlyContinue
            }
        }
    } catch {}
}

function Open-Browser {
    Start-Process "http://localhost:8000"
}

# Start background server
Start-PushtiServer

# Create Application Context
$appContext = New-Object System.Windows.Forms.ApplicationContext

# Setup Tray Icon
$notifyIcon = New-Object System.Windows.Forms.NotifyIcon
$notifyIcon.Icon = [System.Drawing.SystemIcons]::Application
$notifyIcon.Text = "Pushti Study Hub (Port 8000)"
$notifyIcon.Visible = $true

# Double click action
$notifyIcon.add_DoubleClick({
    Open-Browser
})

# Context Menu
$contextMenu = New-Object System.Windows.Forms.ContextMenuStrip

$menuOpen = $contextMenu.Items.Add("🌐 Open Study Hub (localhost:8000)")
$menuOpen.Font = New-Object System.Drawing.Font($menuOpen.Font, [System.Drawing.FontStyle]::Bold)
$menuOpen.add_Click({ Open-Browser })

$menuLog = $contextMenu.Items.Add("📄 View Server Log")
$menuLog.add_Click({
    $logPath = Join-Path $scriptDir "server.log"
    if (-not (Test-Path $logPath)) {
        New-Item -ItemType File -Path $logPath -Force | Out-Null
    }
    Start-Process "notepad.exe" $logPath
})

$menuFolder = $contextMenu.Items.Add("📁 Open Project Folder")
$menuFolder.add_Click({
    Start-Process "explorer.exe" $scriptDir
})

$contextMenu.Items.Add("-") | Out-Null

$menuRestart = $contextMenu.Items.Add("🔄 Restart Server")
$menuRestart.add_Click({
    Stop-PushtiServer
    Start-Sleep -Milliseconds 600
    Start-PushtiServer
    $notifyIcon.ShowBalloonTip(2000, "Pushti Study Hub", "Server restarted successfully on Port 8000.", [System.Windows.Forms.ToolTipIcon]::Info)
})

$menuExit = $contextMenu.Items.Add("🛑 Stop Server & Exit")
$menuExit.add_Click({
    Stop-PushtiServer
    $notifyIcon.Visible = $false
    $notifyIcon.Dispose()
    [System.Windows.Forms.Application]::Exit()
})

$notifyIcon.ContextMenuStrip = $contextMenu

# Show initial balloon tip
$notifyIcon.ShowBalloonTip(2500, "Pushti Study Hub Active", "Server running in background on port 8000.`nDouble-click to open in browser.", [System.Windows.Forms.ToolTipIcon]::Info)

# Run message loop
[System.Windows.Forms.Application]::Run($appContext)
