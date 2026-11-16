$docxPath = "C:\Users\Huzaifa Mahi\.gemini\antigravity\worktrees\remote-workspace\write_new_book\urdu_novel\Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.docx"
$pdfPath  = "C:\Users\Huzaifa Mahi\.gemini\antigravity\worktrees\remote-workspace\write_new_book\urdu_novel\Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.pdf"
$dlPdf    = "C:\Users\Huzaifa Mahi\Downloads\Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.pdf"

Write-Host "Starting Word COM application..."
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
    Write-Host "Opening document: $docxPath"
    $doc = $word.Documents.Open($docxPath, $false, $true) # Open ReadOnly
    
    Write-Host "Exporting to PDF: $pdfPath"
    # 17 = wdExportFormatPDF
    $doc.ExportAsFixedFormat($pdfPath, 17)
    
    $doc.Close([ref]$false)
    Write-Host "Successfully exported PDF!"
    
    Copy-Item -Path $pdfPath -Destination $dlPdf -Force
    Write-Host "Copied PDF to Downloads folder: $dlPdf"
}
catch {
    Write-Error "Error during PDF export: $_"
}
finally {
    $word.Quit([ref]$false)
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}
