Add-Type -AssemblyName System.Runtime.WindowsRuntime
$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]
Function Await($WinRtTask, $ResultType) {
    $asTask = $asTaskGeneric.MakeGenericMethod($ResultType)
    $netTask = $asTask.Invoke($null, @($WinRtTask))
    $netTask.Wait(-1) | Out-Null
    $netTask.Result
}
[Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Storage.StorageFile, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null

$ocrEngine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage([Windows.Globalization.Language]::new("en-US"))
if ($null -eq $ocrEngine) {
    $ocrEngine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
}

$images = @(
    "C:\Users\expor\.gemini\antigravity\brain\84652ad5-70a2-4ee0-9a71-b959099e1f37\.user_uploaded\media_1791637339215_40ca9111.jpg",
    "C:\Users\expor\.gemini\antigravity\brain\84652ad5-70a2-4ee0-9a71-b959099e1f37\.user_uploaded\media_1791637339241_2a30b2c5.jpg",
    "C:\Users\expor\.gemini\antigravity\brain\84652ad5-70a2-4ee0-9a71-b959099e1f37\.user_uploaded\media_1791637339271_dfbb981f.jpg",
    "C:\Users\expor\.gemini\antigravity\brain\84652ad5-70a2-4ee0-9a71-b959099e1f37\.user_uploaded\media_1791637339302_1760ec61.jpg",
    "C:\Users\expor\.gemini\antigravity\brain\84652ad5-70a2-4ee0-9a71-b959099e1f37\.user_uploaded\media_1791637339311_dc7b8b7f.jpg"
)

$outText = ""

for ($i = 0; $i -lt $images.Count; $i++) {
    $img = $images[$i]
    $outText += "`n========================================`n"
    $outText += "IMAGE $($i+1): $img`n"
    $outText += "========================================`n"
    
    if (-not (Test-Path $img)) {
        $outText += "File not found: $img`n"
        continue
    }

    try {
        $fileTask = [Windows.Storage.StorageFile]::GetFileFromPathAsync($img)
        $file = Await $fileTask ([Windows.Storage.StorageFile])
        $streamTask = $file.OpenAsync([Windows.Storage.FileAccessMode]::Read)
        $stream = Await $streamTask ([Windows.Storage.Streams.IRandomAccessStream])
        
        $decoderTask = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)
        $decoder = Await $decoderTask ([Windows.Graphics.Imaging.BitmapDecoder])
        
        $bitmapTask = $decoder.GetSoftwareBitmapAsync()
        $bitmap = Await $bitmapTask ([Windows.Graphics.Imaging.SoftwareBitmap])
        
        $ocrTask = $ocrEngine.RecognizeAsync($bitmap)
        $ocrResult = Await $ocrTask ([Windows.Media.Ocr.OcrResult])
        
        foreach ($line in $ocrResult.Lines) {
            $outText += $line.Text + "`n"
        }
    } catch {
        $outText += "Error processing $img : $_`n"
    }
}

$outText | Out-File -FilePath "scripts/exam_paper_ocr.txt" -Encoding utf8
Write-Host "OCR complete. Saved to scripts/exam_paper_ocr.txt"
