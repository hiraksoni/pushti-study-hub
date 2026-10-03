' Pushti Study Hub - Silent Background Server Starter
Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")
strDir = objFSO.GetParentFolderName(WScript.ScriptFullName)
objShell.CurrentDirectory = strDir

' Run Python server completely in background (0 = hide window)
objShell.Run "python https_server.py", 0, False
