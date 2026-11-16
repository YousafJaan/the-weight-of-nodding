import os
import shutil
import time
import win32com.client
import pythoncom

docx_path = r"C:\Users\Huzaifa Mahi\.gemini\antigravity\worktrees\remote-workspace\write_new_book\urdu_novel\Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.docx"
pdf_path = r"C:\Users\Huzaifa Mahi\.gemini\antigravity\worktrees\remote-workspace\write_new_book\urdu_novel\Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.pdf"
downloads_pdf = r"C:\Users\Huzaifa Mahi\Downloads\Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.pdf"

# Remove existing PDF if present to prevent overwrite prompts
if os.path.exists(pdf_path):
    try:
        os.remove(pdf_path)
    except Exception as e:
        print(f"Could not remove old pdf: {e}")

print("Initializing Word COM...")
pythoncom.CoInitialize()
word = None
try:
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    
    print("Opening DOCX document...")
    doc = word.Documents.Open(docx_path, ReadOnly=True)
    
    print("Exporting to PDF...")
    # 17 = wdFormatPDF
    doc.SaveAs(pdf_path, FileFormat=17)
    doc.Close(False)
    print(f"Exported PDF successfully to {pdf_path}")
    
    shutil.copy2(pdf_path, downloads_pdf)
    print(f"Copied PDF to {downloads_pdf}")
finally:
    if word:
        try:
            word.Quit()
        except:
            pass
    pythoncom.CoUninitialize()

print("PDF export complete.")
