# -*- coding: utf-8 -*-
"""
Compile Epic Two-Column Urdu Novel: 'رجاء: ایک بیٹی کی سچی آپ بیتی'
Author: Anam Sajjad | Protagonist: Rija (رجاء)
Format: 3 Seasons | 33 Episodes | ~90,000+ Words | Two-Column Digest Layout | 250-350+ Pages
Strict Plain Writing: ZERO em-dashes (—) or en-dashes (–).
"""

import os
import re
import sys
import json
import shutil
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

base_dir = r"C:\Users\Huzaifa Mahi\.gemini\antigravity\worktrees\remote-workspace\write_new_book"
urdu_dir = os.path.join(base_dir, "urdu_novel")
reader_dir = os.path.join(base_dir, "reader_app")
novel_reader_dir = os.path.join(urdu_dir, "novel_reader")
episodes_dir = os.path.join(urdu_dir, "episodes")
remote_novel_dir = r"C:\Users\Huzaifa Mahi\remote-workspace\novel"

os.makedirs(urdu_dir, exist_ok=True)
os.makedirs(episodes_dir, exist_ok=True)
os.makedirs(novel_reader_dir, exist_ok=True)
os.makedirs(remote_novel_dir, exist_ok=True)

# 1. Clean plain writing helper
def clean_plain_writing(text):
    if not text:
        return text
    # Strictly replace em-dashes and en-dashes with colons or commas
    text = text.replace("\u2014", " : ").replace("\u2013", " : ")
    # Clean redundant spaces around colons
    text = re.sub(r'\s*:\s*', ' : ', text)
    text = re.sub(r' +', ' ', text)
    return text

# 2. Load episodic narrative scenes
sys.path.insert(0, urdu_dir)
from generate_season_1_part1 import S1_EPISODES
from generate_season_1_part2 import S1_EPISODES_PART2
from generate_season_2_epic import S2_EPISODES
from generate_season_3_epic import S3_EPISODES

all_episodic_scripts = S1_EPISODES + S1_EPISODES_PART2 + S2_EPISODES + S3_EPISODES
print(f"Loaded {len(all_episodic_scripts)} episodic scripts.")

# 3. Load raw master chapters (57,683 words)
master_file = os.path.join(urdu_dir, "RIJA_NOVEL_FINAL_MASTER.md")
with open(master_file, "r", encoding="utf-8") as f:
    raw_master_text = f.read()

raw_master_text = clean_plain_writing(raw_master_text)
raw_sections = re.split(r'\n(?=## باب )', raw_master_text)
print(f"Loaded {len(raw_sections)} sections from master memoirs.")

def get_paragraphs(section_idx):
    if section_idx >= len(raw_sections):
        return []
    lines = raw_sections[section_idx].strip().splitlines()
    body_lines = [l for l in lines if not l.startswith('#') and not l.startswith('---')]
    full_text = "\n".join(body_lines)
    raw_paras = [clean_plain_writing(p.strip()) for p in full_text.split("\n\n") if p.strip()]
    return raw_paras

def chunk_list(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i*k + min(i, m):(i+1)*k + min(i+1, m)] for i in range(n)]

p_bab1 = get_paragraphs(1)   # Bab 1: کردار اور اس کی اہمیت (65 paras)
p_bab2 = get_paragraphs(2)   # Bab 2: نااہل نہیں، چنی ہوئی (95 paras)
p_bab3 = get_paragraphs(3)   # Bab 3: قرآن اور معاشرہ (45 paras)
p_bab4 = get_paragraphs(4)   # Bab 4: اپنوں سے رسوائی (72 paras)
p_bab5 = get_paragraphs(5)   # Bab 5: لوگ کیا کہیں گے (4 paras)
p_bab6 = get_paragraphs(6)   # Bab 6: اچھی بیٹی کون؟ (110 paras)
p_bab7 = get_paragraphs(7)   # Bab 7: ماؤں کے دکھ (135 paras)
p_bab8 = get_paragraphs(8)   # Bab 8: باپ کا کردار اور بیٹی کا جنون (5 paras)
p_bab9 = get_paragraphs(9)   # Bab 9: کامیابی کے بعد زندگی کا سفر (4 paras)
p_bab10 = get_paragraphs(10) # Bab 10: حاسد کی دوستی (155 paras)
p_bab11 = get_paragraphs(11) # Bab 11: باپ کی جدوجہد، بیٹی اور خاموش ممتا (48 paras)

# Split chunks across episodes
c_b1 = chunk_list(p_bab1, 3)     # Ep 1, 6, 11
c_b10 = chunk_list(p_bab10, 6)   # Ep 2, 3, 5, 7, 8, 9
c_b7 = chunk_list(p_bab7, 4)     # Ep 4, 20, 21, 33
c_b4 = chunk_list(p_bab4, 4)     # Ep 12, 13, 14, 15
c_b5 = chunk_list(p_bab5, 3)     # Ep 16, 17, 18
c_b6 = chunk_list(p_bab6, 4)     # Ep 10, 19, 22, 28
c_b2 = chunk_list(p_bab2, 3)     # Ep 23, 24, 25
c_b8 = chunk_list(p_bab8, 2)     # Ep 25, 32
c_b3 = chunk_list(p_bab3, 2)     # Ep 26, 27
c_b9 = chunk_list(p_bab9, 2)     # Ep 29, 30
c_b11 = chunk_list(p_bab11, 3)   # Ep 31, 32, 33

memoirs_mapping = {
    1: c_b1[0],
    2: c_b10[0],
    3: c_b10[1],
    4: c_b7[0],
    5: c_b10[2],
    6: c_b1[1],
    7: c_b10[3],
    8: c_b10[4],
    9: c_b10[5],
    10: c_b6[0],
    11: c_b1[2],
    12: c_b4[0],
    13: c_b4[1],
    14: c_b4[2],
    15: c_b4[3],
    16: c_b5[0],
    17: c_b5[1],
    18: c_b5[2],
    19: c_b6[1],
    20: c_b7[1],
    21: c_b7[2],
    22: c_b6[2],
    23: c_b2[0],
    24: c_b2[1],
    25: c_b2[2] + c_b8[0],
    26: c_b3[0],
    27: c_b3[1],
    28: c_b6[3],
    29: c_b9[0],
    30: c_b9[1],
    31: c_b11[0],
    32: c_b11[1] + c_b8[1],
    33: c_b11[2] + c_b7[3]
}

# 4. Assemble 33 expanded episodes
final_episodes = []
total_word_count = 0

for ep_data in all_episodic_scripts:
    eid = ep_data["id"]
    scenes = [clean_plain_writing(s.strip()) for s in ep_data["scenes"]]
    memoir_paras = memoirs_mapping.get(eid, [])
    
    # Construct seamlessly integrated episodic text
    combined_body = []
    
    # Scene 1: Dramatic opening scene
    if len(scenes) > 0:
        combined_body.append(scenes[0])
    
    # First half of philosophical memoirs
    half_m = len(memoir_paras) // 2
    if half_m > 0:
        combined_body.append("\n\n".join(memoir_paras[:half_m]))
    
    # Scene 2 (and subsequent scenes): Dramatic turning point
    if len(scenes) > 1:
        for sc in scenes[1:]:
            combined_body.append(sc)
            
    # Second half of philosophical memoirs and reflections
    if half_m < len(memoir_paras):
        combined_body.append("\n\n".join(memoir_paras[half_m:]))
        
    full_content = "\n\n".join([b for b in combined_body if b.strip()])
    full_content = clean_plain_writing(full_content)
    
    ep_words = len(full_content.split())
    total_word_count += ep_words
    
    final_episodes.append({
        "id": eid,
        "season": ep_data["season"],
        "season_name": ep_data["season_name"],
        "title": ep_data["title"],
        "subtitle": ep_data["subtitle"],
        "synopsis": ep_data["synopsis"],
        "content": full_content,
        "word_count": ep_words
    })
    
    # Write individual markdown episode
    ep_md_path = os.path.join(episodes_dir, f"episode_{eid:02d}.md")
    with open(ep_md_path, "w", encoding="utf-8") as f:
        f.write(f"# {ep_data['title']}\n")
        f.write(f"### {ep_data['subtitle']}\n")
        f.write(f"**{ep_data['season_name']}** | قسط نمبر {eid} | الفاظ: {ep_words:,}\n\n")
        f.write(f"> **خلاصہ:** {ep_data['synopsis']}\n\n---\n\n")
        f.write(full_content)

print(f"Successfully assembled 33 episodes. Total Word Count: {total_word_count:,}")

# 5. Write Complete Master Markdown
master_md_file = os.path.join(urdu_dir, "RIJA_COMPLETE_EPISODIC_NOVEL.md")
with open(master_md_file, "w", encoding="utf-8") as f:
    f.write("# رجاء: ایک بیٹی کی سچی آپ بیتی\n")
    f.write("### ماؤں کے دکھ، اپنوں کا وار اور قرآن کا سہارا\n")
    f.write(f"**مصنفہ:** انعم سجاد (Anam Sajjad) | **مرکزی کردار:** رجاء (Rija)\n")
    f.write(f"**جامع ادبی شاہکار ایڈیشن:** 3 سیزنز | 33 اقساط | {total_word_count:,} الفاظ\n\n---\n\n")
    
    # Dedication
    f.write("## انتساب\n\n")
    f.write("ان تمام بیٹیوں کے نام جن کے خواب ان کے اپنے آنگنوں میں روند دیے جاتے ہیں۔\n\n")
    f.write("اور میری ماں کے نام، جس نے مجھے سکھایا کہ جب زمین کا کوئی سہارا نہ رہے تو آسمان والے کا دامن تھام لینا چاہیے۔\n\n---\n\n")
    
    curr_season = None
    for ep in final_episodes:
        if ep["season"] != curr_season:
            curr_season = ep["season"]
            f.write(f"\n\n# {ep['season_name']}\n\n---\n\n")
        f.write(f"## قسط {ep['id']}: {ep['title']}\n")
        f.write(f"### {ep['subtitle']}\n\n")
        f.write(f"> {ep['synopsis']}\n\n")
        f.write(ep["content"])
        f.write("\n\n---\n\n")

print(f"Wrote master markdown to {master_md_file}")

# 6. Update Web Reader Dataset
web_episodes = []
for ep in final_episodes:
    read_mins = max(1, ep["word_count"] // 200)
    web_episodes.append({
        "id": ep["id"],
        "season": ep["season"],
        "season_name": ep["season_name"],
        "title": ep["title"],
        "subtitle": ep["subtitle"],
        "synopsis": ep["synopsis"],
        "reading_time": f"{read_mins} منٹ",
        "word_count": ep["word_count"],
        "content": ep["content"]
    })

novel_metadata_js = """// رجاء: ایک بیٹی کی سچی آپ بیتی - مکمل 33 اقساط کا جامع ادبی ڈیٹاسیٹ
const NOVEL_METADATA = {
  title: "رجاء: ایک بیٹی کی سچی آپ بیتی",
  subtitle: "ماؤں کے دکھ، اپنوں کا وار اور قرآن کا سہارا",
  author: "انعم سجاد (Anam Sajjad)",
  protagonist: "رجاء (Rija)",
  seasons: 3,
  total_episodes: 33,
  total_words: """ + str(total_word_count) + """,
  language: "ur",
  direction: "rtl"
};

const NOVEL_CHAPTERS = """ + json.dumps(web_episodes, ensure_ascii=False, indent=2) + """;
"""

for target_dir in [novel_reader_dir, remote_novel_dir]:
    with open(os.path.join(target_dir, "novel_data.js"), "w", encoding="utf-8") as f:
        f.write(novel_metadata_js)
    shutil.copyfile(master_md_file, os.path.join(target_dir, "RIJA_COMPLETE_EPISODIC_NOVEL.md"))

print("Updated novel_data.js in reader and remote workspaces.")

# 7. Generate Two-Column Publication-Grade Word (.docx)
print("Building Two-Column Publication-Grade Word document...")
doc = docx.Document()

# Set up Normal style font
style = doc.styles['Normal']
font = style.font
font.name = 'Jameel Noori Nastaleeq'
font.size = Pt(13.5)
font.color.rgb = RGBColor(25, 25, 25)

# SECTION 1: FRONT MATTER (Single Column)
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
add_p(f"جامع ادبی شاہکار ایڈیشن : 3 سیزنز | 33 اقساط | {total_word_count:,} الفاظ", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=48, color=(140, 30, 30))

add_p("مرکزی کردار: رجاء (Rija)", size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
add_p("مصنفہ: انعم سجاد (Anam Sajjad)", size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=48)
add_p("بہاء الدین زکریا یونیورسٹی ملتان", size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6, color=(90, 90, 90))

doc.add_page_break()

# INTISAB / DEDICATION
add_p("انتساب", size=26, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=48, space_after=24, color=(16, 85, 154))
add_p("ان تمام معصوم اور بے زبان بیٹیوں کے نام", size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_p("جن کے خوابوں اور تمناؤں کا گلا ان کے اپنے خونی آنگنوں میں روایتی انا اور جھوٹی غیرت کے نام پر گھونٹ دیا جاتا ہے، مگر وہ راکھ سے اٹھ کر اپنے مقدر کا سورج خود طلوع کرتی ہیں۔", size=14.5, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=36)

add_p("اور میری صابر و شاکر ماں کے نام", size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_p("جس کے خاموش آنسوؤں نے تہمت کی جلتی آگ کو گلزار بنایا، اور جس کے ہاتھ میں موجود کلامِ پاک نے مجھے ہر تاریک موڑ پر ثابت قدم رکھا۔", size=14.5, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=48)

doc.add_page_break()

# TAQREEZ / FOREWORD
add_p("حرفِ آغاز : اعترافِ حق", size=24, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24, space_after=18, color=(15, 32, 67))
add_p("""یہ ناول کوئی خیالی داستان یا سستا افسانہ نہیں ہے، یہ جنوبی پنجاب کے دیہی اور شہری تضادات کے درمیان گھری ایک ایسی بیٹی کی سچی آپ بیتی ہے جس نے بہاء الدین زکریا یونیورسٹی ملتان کی دہلیز پر قدم رکھنے سے لے کر خاندانی پنچایتوں، رشتے کے بازار، اور کردار کشی کی سازشوں کا اکیلے مقابلہ کیا۔

اس آپ بیتی کا ایک ایک لفظ حقیقت پر مبنی ہے۔ یہ داستان ثابت کرتی ہے کہ عورت کمزور نہیں ہوتی، کمزور وہ سماج ہوتا ہے جو بیٹی کی کامیابی سے خوفزدہ ہو جاتا ہے۔ جب بیٹی اپنے رب کے ساتھ سچا تعلق قائم کر لے تو وہ راکھ سے اٹھ کر اسلام آباد کے ایوانوں تک اپنا لوہا منوا سکتی ہے۔""", size=14, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=24)

doc.add_page_break()

# TABLE OF CONTENTS
add_p("فہرستِ عناوین", size=26, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24, space_after=20, color=(16, 85, 154))
for ep in final_episodes:
    add_p(f"قسط {ep['id']:02d} : {ep['title']} ({ep['season_name']})", size=13, space_after=4, align=WD_ALIGN_PARAGRAPH.RIGHT)

doc.add_page_break()

# SECTION 2: NOVEL BODY (Two Columns)
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
# Page number field
fldSimple = parse_xml(r'<w:fldSimple xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:instr="PAGE"/>')
fp._p.append(fldSimple)

current_season = None

for ep in final_episodes:
    # Season divider
    if ep["season"] != current_season:
        current_season = ep["season"]
        add_p(f"❖ {ep['season_name']} ❖", size=18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=16, space_after=12, color=(140, 30, 30))
    
    # Episode Title
    add_p(f"قسط نمبر {ep['id']} : {ep['title']}", size=16, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=14, space_after=4, color=(15, 32, 67))
    add_p(ep["subtitle"], size=12.5, italic=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=8, color=(70, 85, 100))
    
    # Synopsis Box
    add_p(f"خلاصہ : {ep['synopsis']}", size=11.5, italic=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=10, color=(100, 60, 60))
    
    # Ornamental separator
    add_p("◆   ◆   ◆", size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10, color=(160, 160, 160))
    
    # Paragraphs
    paras = [p.strip() for p in ep["content"].split("\n\n") if p.strip()]
    for p_text in paras:
        if p_text.startswith("◆") or p_text.startswith("---"):
            continue
        add_p(p_text, size=13.5, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=5, line_spacing=1.45)
    
    # Episode end divider
    add_p("❖   ❖   ❖", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=16, color=(16, 85, 154))

output_docx = os.path.join(urdu_dir, "Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.docx")
doc.save(output_docx)
print(f"Saved complete publication-grade Word doc to {output_docx}")

# Copy to downloads and remote workspace
dl_docx = r"C:\Users\Huzaifa Mahi\Downloads\Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.docx"
shutil.copyfile(output_docx, dl_docx)
shutil.copyfile(output_docx, os.path.join(remote_novel_dir, "Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.docx"))
print("Copied Word document to Downloads and remote-workspace/novel.")

# 8. Export to PDF via Word COM
print("Starting Word COM export to PDF...")
import win32com.client

output_pdf = os.path.join(urdu_dir, "Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.pdf")

word = win32com.client.DispatchEx("Word.Application")
word.Visible = False
word.DisplayAlerts = 0

try:
    wdoc = word.Documents.Open(os.path.abspath(output_docx))
    wdoc.SaveAs2(os.path.abspath(output_pdf), FileFormat=17) # 17 = wdFormatPDF
    wdoc.Close(False)
    print(f"Successfully exported PDF to {output_pdf}")
except Exception as e:
    print(f"Error during Word PDF export: {e}")
finally:
    word.Quit()

# Copy PDF to downloads and remote workspace
dl_pdf = r"C:\Users\Huzaifa Mahi\Downloads\Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.pdf"
if os.path.exists(output_pdf):
    shutil.copyfile(output_pdf, dl_pdf)
    shutil.copyfile(output_pdf, os.path.join(remote_novel_dir, "Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.pdf"))
    import pypdf
    reader = pypdf.PdfReader(output_pdf)
    print(f"FINAL PDF PAGE COUNT: {len(reader.pages)} PAGES!")
else:
    print("Warning: PDF was not generated.")

print("All compilation steps completed successfully!")
