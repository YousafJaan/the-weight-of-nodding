# -*- coding: utf-8 -*-
"""
Master Publisher Script for Rija (رجاء: ایک بیٹی کی سچی آپ بیتی)
Author: Anam Sajjad | Protagonist: Rija (رجاء)
Generates:
1. Markdown files (episodes & consolidated novel)
2. Professional RTL Word (.docx) manuscript
3. Native PDF (.pdf) via Microsoft Word
4. Web Reader JS dataset for reader_app
"""

import os
import sys
import shutil
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

# Add urdu_novel directory to path
base_dir = r"C:\Users\Huzaifa Mahi\.gemini\antigravity\worktrees\remote-workspace\write_new_book"
sys.path.insert(0, os.path.join(base_dir, "urdu_novel"))

import season_1_data
import season_2_data
import season_3_data

all_episodes = (
    season_1_data.SEASON_1_EPISODES +
    season_2_data.SEASON_2_EPISODES +
    season_3_data.SEASON_3_EPISODES
)

print(f"Loaded {len(all_episodes)} total episodes.")

# Sanitize text - Plain writing check: NO em-dashes (—) or en-dashes (–)
def sanitize_plain_writing(text):
    if not text:
        return text
    # Replace em-dash and en-dash with colon or comma
    text = text.replace("\u2014", " : ").replace("\u2013", " : ")
    # Normalize multiple colons/spaces
    text = text.replace("  ", " ")
    return text

for ep in all_episodes:
    ep["title"] = sanitize_plain_writing(ep["title"])
    ep["subtitle"] = sanitize_plain_writing(ep["subtitle"])
    ep["synopsis"] = sanitize_plain_writing(ep["synopsis"])
    ep["content"] = sanitize_plain_writing(ep["content"])

# Ensure output directories exist
episodes_dir = os.path.join(base_dir, "urdu_novel", "episodes")
os.makedirs(episodes_dir, exist_ok=True)
reader_app_dir = os.path.join(base_dir, "reader_app")
os.makedirs(reader_app_dir, exist_ok=True)

# 1. Write Markdown Episode Files
def write_season_md(episodes, filename, season_num, season_title):
    path = os.path.join(episodes_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# سیزن {season_num}: {season_title}\n\n")
        f.write(f"*ناول: رجاء: ایک بیٹی کی سچی آپ بیتی | مصنفہ: انعم سجاد*\n\n---\n\n")
        for ep in episodes:
            f.write(f"## قسط {ep['id']}: {ep['title']}\n")
            f.write(f"### {ep['subtitle']}\n\n")
            f.write(f"> **خلاصہ:** {ep['synopsis']}\n\n")
            f.write(f"{ep['content']}\n\n---\n\n")
    print(f"Wrote {path}")

s1_eps = [e for e in all_episodes if e["season"] == 1]
s2_eps = [e for e in all_episodes if e["season"] == 2]
s3_eps = [e for e in all_episodes if e["season"] == 3]

write_season_md(s1_eps, "season_1_episodes_01_to_11.md", 1, "دہلیز اور بیڑیاں")
write_season_md(s2_eps, "season_2_episodes_12_to_22.md", 2, "کردار، رسوائی اور زہر")
write_season_md(s3_eps, "season_3_episodes_23_to_33.md", 3, "جنون، قرآن اور نئی صبح")

# 2. Write Consolidated Master Markdown
master_md_path = os.path.join(base_dir, "urdu_novel", "RIJA_COMPLETE_EPISODIC_NOVEL.md")
with open(master_md_path, "w", encoding="utf-8") as f:
    f.write("""# رجاء: ایک بیٹی کی سچی آپ بیتی

### ماؤں کے دکھ، اپنوں کا وار اور قرآن کا سہارا
**مکمل شاہکار ادبی ایڈیشن: 3 سیزنز | 33 اقساط**

*مرکزی کردار: رجاء | قلمی نام و مصنفہ: انعم سجاد*
*بہاء الدین زکریا یونیورسٹی ملتان کے ہوسٹل سے لے کر بین الاقوامی ایوارڈ تک ایک باہمت بیٹی کا سفر*

---

## انتساب
یہ کتاب ان تمام بیٹیوں کے نام ہے جن کے پر معاشرے کے جھوٹے رواجوں نے کاٹ دیے،
جنہوں نے راتوں کے اندھیرے میں تکیوں پر آنسو بہائے مگر صبح سجدے میں سر جھکا کر دوبارہ جینے کی ہمت باندھی۔
اور میری ماں کے نام، جس کا ایک آنسو زمانے کے ہر زہر کا تریاق تھا۔

---

## پیش لفظ
یہ محض ایک افسانہ نہیں ہے، یہ دل کے خون سے لکھی گئی وہ سچی داستان ہے جو ملتان کی تپتی ہوئی سڑکوں، عائشہ ہال کے کمرہ نمبر بیالیس کی دیواروں، اور خاندانی فیصلوں کے زہریلے کمروں سے گزری ہے۔ جب اپنوں نے کہا کہ 'تم سے کچھ نہیں ہوگا'، تو اس ایک جملے نے اندر وہ آگ جلائی جس نے جہالت کے ہر بت کو خاکستر کر دیا۔ قرآن کی آیات نے رہنمائی کی اور قلم نے گواہی دی۔

---

""")
    for s_idx, (s_num, s_title, eps) in enumerate([
        (1, "دہلیز اور بیڑیاں (The Threshold and The Iron Gate)", s1_eps),
        (2, "کردار، رسوائی اور زہر (Slander, Betrayal & The Crucible)", s2_eps),
        (3, "جنون، قرآن اور نئی صبح (The Passion, Divine Guidance & The New Dawn)", s3_eps)
    ], 1):
        f.write(f"\n\n# سیزن {s_num}: {s_title}\n\n---\n\n")
        for ep in eps:
            f.write(f"## قسط نمبر {ep['id']}: {ep['title']}\n")
            f.write(f"### {ep['subtitle']}\n\n")
            f.write(f"> **خلاصہِ قسط:** {ep['synopsis']}\n\n")
            f.write(f"{ep['content']}\n\n---\n\n")

print(f"Wrote master markdown to {master_md_path}")

# 3. Build Web Reader Dataset (reader_app/ur_chapters_data.js)
web_data_path = os.path.join(reader_app_dir, "ur_chapters_data.js")
import json

chapters_payload = []
for ep in all_episodes:
    # calculate approx word count & read time
    words = len(ep["content"].split())
    read_mins = max(3, round(words / 150))
    season_name = (
        "سیزن 1: دہلیز اور بیڑیاں" if ep["season"] == 1 else
        "سیزن 2: کردار، رسوائی اور زہر" if ep["season"] == 2 else
        "سیزن 3: جنون، قرآن اور نئی صبح"
    )
    chapters_payload.append({
        "id": ep["id"],
        "season": ep["season"],
        "season_name": season_name,
        "title": ep["title"],
        "subtitle": ep["subtitle"],
        "synopsis": ep["synopsis"],
        "reading_time": f"{read_mins} منٹ",
        "word_count": words,
        "content": ep["content"].replace("\n\n", "\n")
    })

with open(web_data_path, "w", encoding="utf-8") as f:
    f.write("// رجاء: ایک بیٹی کی سچی آپ بیتی - مکمل 33 اقساط کا ڈیٹاسیٹ\n")
    f.write("const UR_BOOK_METADATA = {\n")
    f.write('  title: "رجاء: ایک بیٹی کی سچی آپ بیتی",\n')
    f.write('  subtitle: "ماؤں کے دکھ، اپنوں کا وار اور قرآن کا سہارا",\n')
    f.write('  author: "انعم سجاد (Anam Sajjad)",\n')
    f.write('  protagonist: "رجاء (Rija)",\n')
    f.write('  seasons: 3,\n')
    f.write('  total_episodes: 33,\n')
    f.write('  language: "ur",\n')
    f.write('  direction: "rtl"\n')
    f.write("};\n\n")
    f.write("const UR_CHAPTERS = ")
    f.write(json.dumps(chapters_payload, ensure_ascii=False, indent=2))
    f.write(";\n")

print(f"Wrote Web Reader dataset to {web_data_path}")

# 4. Generate Professional RTL Word Document (.docx)
def set_cell_rtl(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(r'<w:bidi xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))

def set_p_rtl(p):
    pPr = p._p.get_or_add_pPr()
    pPr.append(parse_xml(r'<w:bidi xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))

doc = docx.Document()

# Configure page margins (1 inch = 72pt)
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    section.page_width = Inches(8.5)
    section.page_height = Inches(11.0)
    
    # Configure RTL in section
    sectPr = section._sectPr
    sectPr.append(parse_xml(r'<w:bidi xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))

# Configure styles for Urdu
# Normal style
normal_style = doc.styles['Normal']
normal_style.font.name = 'Jameel Noori Nastaleeq'
normal_style.font.size = Pt(13)
normal_style.font.color.rgb = RGBColor(30, 30, 30)

# Helper to add RTL paragraph with Urdu font
def add_urdu_p(text, size=13, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=6, color=(30,30,30)):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.35
    set_p_rtl(p)
    run = p.add_run(text)
    run.font.name = 'Jameel Noori Nastaleeq'
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(*color)
    
    # Set complex script font in oxml
    rPr = run._r.get_or_add_rPr()
    rFonts = parse_xml(r'<w:rFonts xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:ascii="Jameel Noori Nastaleeq" w:hAnsi="Jameel Noori Nastaleeq" w:cs="Jameel Noori Nastaleeq"/>')
    rPr.append(rFonts)
    return p

# --- COVER PAGE ---
doc.add_paragraph()
doc.add_paragraph()
add_urdu_p("بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ", size=18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24, color=(16, 85, 154))
add_urdu_p("رجاء: ایک بیٹی کی سچی آپ بیتی", size=32, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12, color=(15, 32, 67))
add_urdu_p("ماؤں کے دکھ، اپنوں کا وار اور قرآن کا سہارا", size=18, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24, color=(90, 105, 120))
add_urdu_p("مکمل شاہکار ادبی اشاعت: 3 سیزنز | 33 اقساط", size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=36, color=(120, 40, 40))

add_urdu_p("مرکزی کردار: رجاء (Rija)", size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_urdu_p("مصنفہ: انعم سجاد (Anam Sajjad)", size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=48)
add_urdu_p("بہاء الدین زکریا یونیورسٹی ملتان", size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6, color=(100, 100, 100))
add_urdu_p("2026ء", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24, color=(120, 120, 120))

doc.add_page_break()

# --- INTRO & DEDICATION ---
add_urdu_p("انتساب", size=20, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=12, color=(15, 32, 67))
add_urdu_p("یہ کتاب ان تمام بیٹیوں کے نام ہے جن کے پر معاشرے کے جھوٹے رواجوں نے کاٹ دیے، جنہوں نے راتوں کے اندھیرے میں تکیوں پر آنسو بہائے مگر صبح سجدے میں سر جھکا کر دوبارہ جینے کی ہمت باندھی۔ اور میری ماں کے نام، جس کا ایک آنسو زمانے کے ہر زہر کا تریاق تھا۔", size=14, italic=True, space_after=24)

add_urdu_p("پیش لفظ", size=20, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=12, color=(15, 32, 67))
add_urdu_p("یہ محض ایک افسانہ نہیں ہے، یہ دل کے خون سے لکھی گئی وہ سچی داستان ہے جو ملتان کی تپتی ہوئی سڑکوں، عائشہ ہال کے کمرہ نمبر بیالیس کی دیواروں، اور خاندانی فیصلوں کے زہریلے کمروں سے گزری ہے۔ جب اپنوں نے کہا کہ 'تم سے کچھ نہیں ہوگا'، تو اس ایک جملے نے اندر وہ آگ جلائی جس نے جہالت کے ہر بت کو خاکستر کر دیا۔ قرآن کی آیات نے رہنمائی کی اور قلم نے گواہی دی۔", size=14, space_after=24)

doc.add_page_break()

# --- TABLE OF CONTENTS ---
add_urdu_p("فہرستِ ابواب و اقساط", size=22, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=18, color=(15, 32, 67))

for ep in all_episodes:
    season_tag = f"سیزن {ep['season']}"
    line = f"{ep['id']}. {ep['title']} : {ep['subtitle']} ({season_tag})"
    add_urdu_p(line, size=12, space_after=4, color=(40, 40, 40))

doc.add_page_break()

# --- SEASONS & EPISODES ---
current_season = 0
season_titles = {
    1: "سیزن 1: دہلیز اور بیڑیاں (The Threshold and The Iron Gate)",
    2: "سیزن 2: کردار، رسوائی اور زہر (Slander, Betrayal & The Crucible)",
    3: "سیزن 3: جنون، قرآن اور نئی صبح (The Passion, Divine Guidance & The New Dawn)"
}

for ep in all_episodes:
    if ep["season"] != current_season:
        current_season = ep["season"]
        # Season divider page
        doc.add_page_break()
        add_urdu_p(season_titles[current_season], size=24, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=72, space_after=24, color=(16, 85, 154))
        add_urdu_p("ناول: رجاء : ایک بیٹی کی سچی آپ بیتی", size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=72, color=(100, 100, 100))
        doc.add_page_break()
    else:
        doc.add_page_break()
    
    # Episode Header
    add_urdu_p(f"قسط {ep['id']}: {ep['title']}", size=20, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=6, color=(15, 32, 67))
    add_urdu_p(ep['subtitle'], size=14, italic=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=12, color=(100, 100, 100))
    
    # Synopsis box
    syn_p = add_urdu_p(f"خلاصہ: {ep['synopsis']}", size=11, bold=False, italic=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=16, color=(80, 50, 20))
    
    # Episode paragraphs
    paragraphs = [p.strip() for p in ep["content"].split("\n") if p.strip()]
    for p_text in paragraphs:
        add_urdu_p(p_text, size=13, space_after=10, align=WD_ALIGN_PARAGRAPH.JUSTIFY)

# Save Word Doc
docx_path = os.path.join(base_dir, "urdu_novel", "Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.docx")
doc.save(docx_path)
print(f"Saved master DOCX to {docx_path}")

# Copy to Downloads
downloads_docx = r"C:\Users\Huzaifa Mahi\Downloads\Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.docx"
shutil.copy2(docx_path, downloads_docx)
print(f"Copied DOCX to {downloads_docx}")

# 5. Convert to PDF using Microsoft Word COM
pdf_path = os.path.join(base_dir, "urdu_novel", "Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.pdf")
downloads_pdf = r"C:\Users\Huzaifa Mahi\Downloads\Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.pdf"

try:
    import win32com.client
    import pythoncom
    print("Exporting PDF via Word COM...")
    pythoncom.CoInitialize()
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    doc_com = word.Documents.Open(docx_path)
    # wdFormatPDF = 17
    doc_com.SaveAs(pdf_path, FileFormat=17)
    doc_com.Close()
    word.Quit()
    print(f"Generated PDF at {pdf_path}")
    shutil.copy2(pdf_path, downloads_pdf)
    print(f"Copied PDF to {downloads_pdf}")
except Exception as e:
    print(f"Word COM PDF export error: {e}")

print("Master publication build script completed successfully.")
