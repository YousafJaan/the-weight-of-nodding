# -*- coding: utf-8 -*-
"""
Compile Final Publication-Grade Word (.docx) and PDF (.pdf)
Novel: 'رجاء: ایک بیٹی کی سچی آپ بیتی'
Complete 61 Episodes Edition | Two-Column Digest Layout | Jameel Noori Nastaleeq
Strict Plain Writing: ZERO em-dashes (—) or en-dashes (–).
"""

import os
import sys
import json
import shutil
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml import parse_xml

novel_dir = r"C:\Users\Huzaifa Mahi\remote-workspace\novel"
data_js = os.path.join(novel_dir, "novel_data.js")

with open(data_js, "r", encoding="utf-8") as f:
    text = f.read()

import re
m = re.search(r'const NOVEL_CHAPTERS\s*=\s*(\[[\s\S]*\]);', text)
chapters = json.loads(m.group(1))
print(f"Loaded {len(chapters)} clean master episodes.")

total_words = sum(ch["word_count"] for ch in chapters)
print(f"Total word count: {total_words:,}")

doc = docx.Document()

# Set up Normal style
style = doc.styles['Normal']
font = style.font
font.name = 'Jameel Noori Nastaleeq'
font.size = Pt(13.5)
font.color.rgb = RGBColor(25, 25, 25)

# FRONT MATTER SECTION (Single Column)
sect_front = doc.sections[0]
sect_front.top_margin = Inches(0.8)
sect_front.bottom_margin = Inches(0.8)
sect_front.left_margin = Inches(0.8)
sect_front.right_margin = Inches(0.8)
sect_front._sectPr.append(parse_xml(r'<w:bidi xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))

def add_p(text="", size=13.5, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=5, line_spacing=1.45, color=(25,25,25)):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    
    pPr = p._p.get_or_add_pPr()
    pPr.append(parse_xml(r'<w:bidi xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))
    
    if text:
        run = p.add_run(text)
        run.font.name = 'Jameel Noori Nastaleeq'
        run.font.size = Pt(size)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = RGBColor(*color)
        rPr = run._r.get_or_add_rPr()
        rPr.append(parse_xml(r'<w:rFonts xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:ascii="Jameel Noori Nastaleeq" w:hAnsi="Jameel Noori Nastaleeq" w:cs="Jameel Noori Nastaleeq"/>'))
    return p

# TITLE PAGE
add_p("بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ", size=20, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=72, space_after=36, color=(16, 85, 154))
add_p("رجاء: ایک بیٹی کی سچی آپ بیتی", size=36, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14, color=(15, 32, 67))
add_p("ماؤں کے دکھ، اپنوں کا وار اور قرآن کا سہارا", size=20, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=30, color=(80, 95, 110))
add_p(f"جامع ادبی شاہکار ایڈیشن : 6 سیزنز | 61 اقساط | {total_words:,} الفاظ", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=48, color=(140, 30, 30))

add_p("مرکزی کردار: رجاء (Rija)", size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
add_p("مصنفہ: انعم سجاد (Anam Sajjad)", size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=48)
add_p("بہاء الدین زکریا یونیورسٹی ملتان", size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6, color=(90, 90, 90))

doc.add_page_break()

# DEDICATION
add_p("انتساب", size=26, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=48, space_after=24, color=(16, 85, 154))
add_p("ان تمام معصوم اور باہمت بیٹیوں کے نام", size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_p("جن کے خوابوں اور تمناؤں کا گلا ان کے اپنے خونی آنگنوں میں روایتی انا اور جھوٹی غیرت کے نام پر گھونٹ دیا جاتا ہے، مگر وہ راکھ سے اٹھ کر اپنے مقدر کا سورج خود طلوع کرتی ہیں۔", size=14.5, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=36)

add_p("اور میری صابر و شاکر ماں کے نام", size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_p("جس کے خاموش آنسوؤں نے تہمت کی جلتی آگ کو گلزار بنایا، اور جس کی دی ہوئی پرانی مخمل کی جائے نماز نے مجھے ہر تاریک موڑ پر ثابت قدم رکھا۔", size=14.5, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=48)

doc.add_page_break()

# FOREWORD
add_p("حرفِ آغاز : اعترافِ حق", size=24, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24, space_after=18, color=(15, 32, 67))
add_p("""یہ ناول کوئی خیالی داستان یا سستا افسانہ نہیں ہے، یہ جنوبی پنجاب کے دیہی اور شہری تضادات کے درمیان گھری ایک ایسی بیٹی کی سچی آپ بیتی ہے جس نے بہاء الدین زکریا یونیورسٹی ملتان کی دہلیز پر قدم رکھنے سے لے کر خاندانی پنچایتوں، رشتے کے بازار، اور کردار کشی کی سازشوں کا اکیلے مقابلہ کیا۔

اس آپ بیتی کا ایک ایک لفظ حقیقت پر مبنی ہے۔ یہ داستان ثابت کرتی ہے کہ عورت کمزور نہیں ہوتی، کمزور وہ سماج ہوتا ہے جو بیٹی کی کامیابی سے خوفزدہ ہو جاتا ہے۔ جب بیٹی اپنے رب کے ساتھ سچا تعلق قائم کر لے اور قرآن کے اصولوں پر ڈٹ جائے تو وہ راکھ سے اٹھ کر ایوانِ صدر تک اپنا لوہا منوا سکتی ہے۔""", size=14, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=24)

doc.add_page_break()

# TABLE OF CONTENTS
add_p("فہرستِ اقساط (مکمل 61 اقساط)", size=24, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24, space_after=20, color=(16, 85, 154))
for ep in chapters:
    add_p(f"قسط {ep['id']:02d} : {ep['title']} ({ep['season_name']})", size=12.5, space_after=3, align=WD_ALIGN_PARAGRAPH.RIGHT)

doc.add_page_break()

# NOVEL BODY SECTION (Two Columns)
sect_body = doc.add_section(WD_SECTION.NEW_PAGE)
sect_body.top_margin = Inches(0.75)
sect_body.bottom_margin = Inches(0.75)
sect_body.left_margin = Inches(0.75)
sect_body.right_margin = Inches(0.75)

sectPr_body = sect_body._sectPr
sectPr_body.append(parse_xml(r'<w:bidi xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))
# Two columns with 0.5 inch (720 dxa) spacing
sectPr_body.append(parse_xml(r'<w:cols xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:num="2" w:space="720"/>'))

# Running header/footer
header = sect_body.header
hp = header.paragraphs[0]
hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
hrun = hp.add_run("رجاء : ایک بیٹی کی سچی آپ بیتی")
hrun.font.name = 'Jameel Noori Nastaleeq'
hrun.font.size = Pt(10)
hrun.font.color.rgb = RGBColor(120, 120, 120)

footer = sect_body.footer
fp = footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
frun = fp.add_run("صفحہ ")
frun.font.name = 'Jameel Noori Nastaleeq'
frun.font.size = Pt(10)
frun.font.color.rgb = RGBColor(100, 100, 100)
fldSimple = parse_xml(r'<w:fldSimple xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:instr="PAGE"/>')
fp._p.append(fldSimple)

current_season = None

for ep in chapters:
    if ep["season"] != current_season:
        current_season = ep["season"]
        add_p(f"❖ {ep['season_name']} ❖", size=18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=16, space_after=12, color=(140, 30, 30))
    
    add_p(f"قسط نمبر {ep['id']} : {ep['title']}", size=15.5, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=14, space_after=4, color=(15, 32, 67))
    add_p(ep["subtitle"], size=12, italic=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=8, color=(70, 85, 100))
    add_p(f"خلاصہ : {ep['synopsis']}", size=11, italic=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=10, color=(100, 60, 60))
    add_p("◆   ◆   ◆", size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10, color=(160, 160, 160))
    
    paras = [p.strip() for p in ep["content"].split("\n\n") if p.strip()]
    for p_text in paras:
        if p_text.startswith("◆") or p_text.startswith("---") or p_text.startswith("#"):
            continue
        add_p(p_text, size=13, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=5, line_spacing=1.45)
    
    add_p("❖   ❖   ❖", size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=16, color=(16, 85, 154))

output_docx = os.path.join(novel_dir, "Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.docx")
doc.save(output_docx)
print(f"Saved complete publication-grade Word doc to {output_docx} ({os.path.getsize(output_docx)} bytes)")

dl_docx = r"C:\Users\Huzaifa Mahi\Downloads\Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.docx"
shutil.copyfile(output_docx, dl_docx)
print(f"Copied to Downloads: {dl_docx}")

# Export to PDF via Word COM
print("Starting Word COM export to PDF...")
import win32com.client

output_pdf = os.path.join(novel_dir, "Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.pdf")
word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
word.DisplayAlerts = 0

try:
    wdoc = word.Documents.Open(os.path.abspath(output_docx))
    wdoc.SaveAs2(os.path.abspath(output_pdf), FileFormat=17) # 17 = wdFormatPDF
    wdoc.Close(False)
    print(f"Successfully exported PDF to {output_pdf} ({os.path.getsize(output_pdf)} bytes)")
except Exception as e:
    print(f"Error during Word PDF export: {e}")
finally:
    word.Quit()

dl_pdf = r"C:\Users\Huzaifa Mahi\Downloads\Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.pdf"
if os.path.exists(output_pdf):
    shutil.copyfile(output_pdf, dl_pdf)
    print(f"Copied to Downloads: {dl_pdf}")
