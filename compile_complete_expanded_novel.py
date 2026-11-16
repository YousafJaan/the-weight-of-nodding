# -*- coding: utf-8 -*-
"""
Compile Complete Expanded Episodic Novel for 'Rija' (رجاء: ایک بیٹی کی سچی آپ بیتی)
Author: Anam Sajjad | Protagonist: Rija (رجاء)
Integrates both the episodic dramatic scripts and the comprehensive memoirs from RIJA_NOVEL_FINAL_MASTER.md.
Plain-writing compliant: ZERO em-dashes (—) or en-dashes (–).
"""

import os
import re
import sys
import json
import shutil
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml

base_dir = r"C:\Users\Huzaifa Mahi\.gemini\antigravity\worktrees\remote-workspace\write_new_book"
urdu_dir = os.path.join(base_dir, "urdu_novel")
reader_dir = os.path.join(base_dir, "reader_app")
novel_reader_dir = os.path.join(urdu_dir, "novel_reader")
os.makedirs(novel_reader_dir, exist_ok=True)

# 1. Load the raw master chapters
master_file = os.path.join(urdu_dir, "RIJA_NOVEL_FINAL_MASTER.md")
with open(master_file, "r", encoding="utf-8") as f:
    raw_master_text = f.read()

# Sanitize raw text to remove any forbidden dashes
def clean_plain_writing(text):
    if not text:
        return text
    # Replace em-dashes and en-dashes with colons or commas
    text = text.replace("\u2014", " : ").replace("\u2013", " : ")
    # Clean up excess spaces around colons
    text = re.sub(r'\s*:\s*', ' : ', text)
    text = re.sub(r' +', ' ', text)
    return text

raw_master_text = clean_plain_writing(raw_master_text)

# Split raw chapters
raw_sections = re.split(r'\n(?=## باب )', raw_master_text)
# raw_sections[0] is Frontmatter
# raw_sections[1] is Bab 1
# raw_sections[2] is Bab 2
# ...
# raw_sections[11] is Bab 11
print(f"Loaded {len(raw_sections)} raw sections from master.")

# Helper to slice chapter text into clean paragraphs
def get_paragraphs(section_idx):
    if section_idx >= len(raw_sections):
        return []
    lines = raw_sections[section_idx].strip().splitlines()
    # Skip heading lines
    body_lines = [l for l in lines if not l.startswith('#') and not l.startswith('---')]
    full_text = "\n".join(body_lines)
    # Split into paragraphs by blank lines or period/khatma
    raw_paras = [p.strip() for p in full_text.split("\n\n") if p.strip()]
    return raw_paras

# Load base episodic data
sys.path.insert(0, urdu_dir)
import season_1_data
import season_2_data
import season_3_data

s1_base = season_1_data.SEASON_1_EPISODES
s2_base = season_2_data.SEASON_2_EPISODES
s3_base = season_3_data.SEASON_3_EPISODES

# Now distribute raw chapter paragraphs across episodes
# Bab 1 (21k chars) -> Ep 1, 11
# Bab 10 (51k chars) -> Ep 2, 3, 5, 6, 7, 8, 9
# Bab 7 (43k chars) -> Ep 4, 21, 22
# Bab 6 (36k chars) -> Ep 10, 15, 17, 18, 19
# Bab 4 (23k chars) -> Ep 12, 13, 14, 20
# Bab 5 (1.2k chars) -> Ep 16
# Bab 2 (30k chars) -> Ep 23
# Bab 8 (1.3k chars) -> Ep 24, 25
# Bab 3 (15k chars) -> Ep 26, 27, 28
# Bab 9 (1.2k chars) -> Ep 29, 30
# Bab 11 (15k chars) -> Ep 31, 32, 33

def chunk_list(lst, n):
    """Split list into n chunks"""
    k, m = divmod(len(lst), n)
    return [lst[i*k + min(i, m):(i+1)*k + min(i+1, m)] for i in range(n)]

p_bab1 = get_paragraphs(1)
p_bab2 = get_paragraphs(2)
p_bab3 = get_paragraphs(3)
p_bab4 = get_paragraphs(4)
p_bab5 = get_paragraphs(5)
p_bab6 = get_paragraphs(6)
p_bab7 = get_paragraphs(7)
p_bab8 = get_paragraphs(8)
p_bab9 = get_paragraphs(9)
p_bab10 = get_paragraphs(10)
p_bab11 = get_paragraphs(11)

b10_chunks = chunk_list(p_bab10, 7) # for Ep 2, 3, 5, 6, 7, 8, 9
b1_chunks = chunk_list(p_bab1, 2)   # for Ep 1, 11
b7_chunks = chunk_list(p_bab7, 3)   # for Ep 4, 21, 22
b6_chunks = chunk_list(p_bab6, 5)   # for Ep 10, 15, 17, 18, 19
b4_chunks = chunk_list(p_bab4, 4)   # for Ep 12, 13, 14, 20
b8_chunks = chunk_list(p_bab8, 2)   # for Ep 24, 25
b3_chunks = chunk_list(p_bab3, 3)   # for Ep 26, 27, 28
b9_chunks = chunk_list(p_bab9, 2)   # for Ep 29, 30
b11_chunks = chunk_list(p_bab11, 3) # for Ep 31, 32, 33

expanded_episodes = []

# Season 1 Assembly
s1_raw_mapping = {
    1: b1_chunks[0],
    2: b10_chunks[0],
    3: b10_chunks[1],
    4: b7_chunks[0],
    5: b10_chunks[2],
    6: b10_chunks[3],
    7: b10_chunks[4],
    8: b10_chunks[5],
    9: b10_chunks[6],
    10: b6_chunks[0],
    11: b1_chunks[1]
}

for ep in s1_base:
    eid = ep["id"]
    extra_paras = s1_raw_mapping.get(eid, [])
    merged_content = ep["content"] + "\n\n" + "\n\n".join(extra_paras)
    merged_content = clean_plain_writing(merged_content)
    expanded_episodes.append({
        "id": eid,
        "season": 1,
        "season_name": "سیزن 1: دہلیز اور بیڑیاں",
        "title": clean_plain_writing(ep["title"]),
        "subtitle": clean_plain_writing(ep["subtitle"]),
        "synopsis": clean_plain_writing(ep["synopsis"]),
        "content": merged_content
    })

# Season 2 Assembly
s2_raw_mapping = {
    12: b4_chunks[0],
    13: b4_chunks[1],
    14: b4_chunks[2],
    15: b6_chunks[1],
    16: p_bab5,
    17: b6_chunks[2],
    18: b6_chunks[3],
    19: b6_chunks[4],
    20: b4_chunks[3],
    21: b7_chunks[1],
    22: b7_chunks[2]
}

for ep in s2_base:
    eid = ep["id"]
    extra_paras = s2_raw_mapping.get(eid, [])
    merged_content = ep["content"] + "\n\n" + "\n\n".join(extra_paras)
    merged_content = clean_plain_writing(merged_content)
    expanded_episodes.append({
        "id": eid,
        "season": 2,
        "season_name": "سیزن 2: کردار، رسوائی اور زہر",
        "title": clean_plain_writing(ep["title"]),
        "subtitle": clean_plain_writing(ep["subtitle"]),
        "synopsis": clean_plain_writing(ep["synopsis"]),
        "content": merged_content
    })

# Season 3 Assembly
s3_raw_mapping = {
    23: p_bab2,
    24: b8_chunks[0],
    25: b8_chunks[1],
    26: b3_chunks[0],
    27: b3_chunks[1],
    28: b3_chunks[2],
    29: b9_chunks[0],
    30: b9_chunks[1],
    31: b11_chunks[0],
    32: b11_chunks[1],
    33: b11_chunks[2]
}

for ep in s3_base:
    eid = ep["id"]
    extra_paras = s3_raw_mapping.get(eid, [])
    merged_content = ep["content"] + "\n\n" + "\n\n".join(extra_paras)
    merged_content = clean_plain_writing(merged_content)
    expanded_episodes.append({
        "id": eid,
        "season": 3,
        "season_name": "سیزن 3: جنون، قرآن اور نئی صبح",
        "title": clean_plain_writing(ep["title"]),
        "subtitle": clean_plain_writing(ep["subtitle"]),
        "synopsis": clean_plain_writing(ep["synopsis"]),
        "content": merged_content
    })

# Metrics calculation
total_words = sum(len(ep["content"].split()) for ep in expanded_episodes)
total_chars = sum(len(ep["content"]) for ep in expanded_episodes)
print(f"EXPANDED NOVEL STATS -> Total Episodes: {len(expanded_episodes)} | Total Words: {total_words:,} | Total Chars: {total_chars:,}")

# 2. Write Markdown Episode Files
episodes_dir = os.path.join(urdu_dir, "episodes")
os.makedirs(episodes_dir, exist_ok=True)

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

s1_eps = [e for e in expanded_episodes if e["season"] == 1]
s2_eps = [e for e in expanded_episodes if e["season"] == 2]
s3_eps = [e for e in expanded_episodes if e["season"] == 3]

write_season_md(s1_eps, "season_1_episodes_01_to_11.md", 1, "دہلیز اور بیڑیاں")
write_season_md(s2_eps, "season_2_episodes_12_to_22.md", 2, "کردار، رسوائی اور زہر")
write_season_md(s3_eps, "season_3_episodes_23_to_33.md", 3, "جنون، قرآن اور نئی صبح")

# 3. Write Master Consolidated Markdown File
master_md_path = os.path.join(urdu_dir, "RIJA_COMPLETE_EPISODIC_NOVEL.md")
with open(master_md_path, "w", encoding="utf-8") as f:
    f.write(f"""# رجاء: ایک بیٹی کی سچی آپ بیتی

### ماؤں کے دکھ، اپنوں کا وار اور قرآن کا سہارا
**مکمل شاہکار ادبی اشاعت: 3 سیزنز | 33 اقساط | {total_words:,} الفاظ**

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

print(f"Wrote updated master markdown: {master_md_path}")

# 4. Write Web Reader Datasets
chapters_payload = []
for ep in expanded_episodes:
    words = len(ep["content"].split())
    read_mins = max(3, round(words / 150))
    chapters_payload.append({
        "id": ep["id"],
        "season": ep["season"],
        "season_name": ep["season_name"],
        "title": ep["title"],
        "subtitle": ep["subtitle"],
        "synopsis": ep["synopsis"],
        "reading_time": f"{read_mins} منٹ",
        "word_count": words,
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
  total_words: """ + str(total_words) + """,
  language: "ur",
  direction: "rtl"
};

const NOVEL_CHAPTERS = """ + json.dumps(chapters_payload, ensure_ascii=False, indent=2) + """;
"""

# Write to both locations
with open(os.path.join(novel_reader_dir, "novel_data.js"), "w", encoding="utf-8") as f:
    f.write(novel_metadata_js)

# Also update reader_app/ur_chapters_data.js for cross-compatibility
with open(os.path.join(reader_dir, "ur_chapters_data.js"), "w", encoding="utf-8") as f:
    f.write(novel_metadata_js.replace("NOVEL_METADATA", "UR_BOOK_METADATA").replace("NOVEL_CHAPTERS", "UR_CHAPTERS"))

print("Wrote novel_data.js and ur_chapters_data.js")

# 5. Build Standalone Web Reader App in urdu_novel/novel_reader/index.html
# Dedicated completely to the Novel (100% separate from the book)
with open(os.path.join(reader_dir, "rija_reader.html"), "r", encoding="utf-8") as f:
    standalone_html = f.read()

# Replace scripts and links to make novel_reader completely independent
standalone_html = standalone_html.replace('src="ur_chapters_data.js"', 'src="novel_data.js"')
standalone_html = standalone_html.replace('UR_CHAPTERS', 'NOVEL_CHAPTERS')
standalone_html = standalone_html.replace('href="../urdu_novel/Rija_Ek_Beti', 'href="../Rija_Ek_Beti')
standalone_html = standalone_html.replace('<!-- Switch to English Book -->', '<!-- Standalone Novel Reader -->')
# remove English book link in standalone reader
standalone_html = re.sub(r'<a href="index\.html" class="switch-pill".*?</a>', '<span class="switch-pill" style="border:none; background:transparent; font-size:15px; font-weight:700;">ادبی شاہکار ایڈیشن</span>', standalone_html, flags=re.DOTALL)

with open(os.path.join(novel_reader_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(standalone_html)

print("Created dedicated standalone reader at urdu_novel/novel_reader/index.html")

# 6. Generate Publication-Grade Word (.docx)
print("Building Word (.docx) document...")
doc = docx.Document()

# Page Margins 1 inch
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    sectPr = section._sectPr
    sectPr.append(parse_xml(r'<w:bidi xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))

def add_urdu_p(text, size=13, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=6, color=(30,30,30)):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.35
    pPr = p._p.get_or_add_pPr()
    pPr.append(parse_xml(r'<w:bidi xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))
    
    run = p.add_run(text)
    run.font.name = 'Jameel Noori Nastaleeq'
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(*color)
    
    rPr = run._r.get_or_add_rPr()
    rFonts = parse_xml(r'<w:rFonts xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:ascii="Jameel Noori Nastaleeq" w:hAnsi="Jameel Noori Nastaleeq" w:cs="Jameel Noori Nastaleeq"/>')
    rPr.append(rFonts)
    return p

# COVER PAGE
doc.add_paragraph()
doc.add_paragraph()
add_urdu_p("بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ", size=18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24, color=(16, 85, 154))
add_urdu_p("رجاء: ایک بیٹی کی سچی آپ بیتی", size=32, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12, color=(15, 32, 67))
add_urdu_p("ماؤں کے دکھ، اپنوں کا وار اور قرآن کا سہارا", size=18, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24, color=(90, 105, 120))
add_urdu_p(f"مکمل شاہکار ادبی اشاعت: 3 سیزنز | 33 اقساط | {total_words:,} الفاظ", size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=36, color=(120, 40, 40))

add_urdu_p("مرکزی کردار: رجاء (Rija)", size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_urdu_p("مصنفہ: انعم سجاد (Anam Sajjad)", size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=48)
add_urdu_p("بہاء الدین زکریا یونیورسٹی ملتان", size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6, color=(100, 100, 100))
add_urdu_p("2026ء", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24, color=(120, 120, 120))

doc.add_page_break()

# DEDICATION & FOREWORD
add_urdu_p("انتساب", size=20, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=12, color=(15, 32, 67))
add_urdu_p("یہ کتاب ان تمام بیٹیوں کے نام ہے جن کے پر معاشرے کے جھوٹے رواجوں نے کاٹ دیے، جنہوں نے راتوں کے اندھیرے میں تکیوں پر آنسو بہائے مگر صبح سجدے میں سر جھکا کر دوبارہ جینے کی ہمت باندھی۔ اور میری ماں کے نام، جس کا ایک آنسو زمانے کے ہر زہر کا تریاق تھا۔", size=14, italic=True, space_after=24)

add_urdu_p("پیش لفظ", size=20, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=12, color=(15, 32, 67))
add_urdu_p("یہ محض ایک افسانہ نہیں ہے، یہ دل کے خون سے لکھی گئی وہ سچی داستان ہے جو ملتان کی تپتی ہوئی سڑکوں، عائشہ ہال کے کمرہ نمبر بیالیس کی دیواروں، اور خاندانی فیصلوں کے زہریلے کمروں سے گزری ہے۔ جب اپنوں نے کہا کہ 'تم سے کچھ نہیں ہوگا'، تو اس ایک جملے نے اندر وہ آگ جلائی جس نے جہالت کے ہر بت کو خاکستر کر دیا۔ قرآن کی آیات نے رہنمائی کی اور قلم نے گواہی دی۔", size=14, space_after=24)

doc.add_page_break()

# TABLE OF CONTENTS
add_urdu_p("فہرستِ ابواب و اقساط", size=22, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=18, color=(15, 32, 67))
for ep in expanded_episodes:
    season_tag = f"سیزن {ep['season']}"
    line = f"{ep['id']}. {ep['title']} : {ep['subtitle']} ({season_tag})"
    add_urdu_p(line, size=12, space_after=4, color=(40, 40, 40))

# CHAPTER BODIES
current_season = 0
season_titles = {
    1: "سیزن 1: دہلیز اور بیڑیاں (The Threshold and The Iron Gate)",
    2: "سیزن 2: کردار، رسوائی اور زہر (Slander, Betrayal & The Crucible)",
    3: "سیزن 3: جنون، قرآن اور نئی صبح (The Passion, Divine Guidance & The New Dawn)"
}

for ep in expanded_episodes:
    if ep["season"] != current_season:
        current_season = ep["season"]
        doc.add_page_break()
        add_urdu_p(season_titles[current_season], size=24, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=72, space_after=24, color=(16, 85, 154))
        add_urdu_p("ناول: رجاء : ایک بیٹی کی سچی آپ بیتی", size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=72, color=(100, 100, 100))
        doc.add_page_break()
    else:
        doc.add_page_break()
    
    add_urdu_p(f"قسط {ep['id']}: {ep['title']}", size=20, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=6, color=(15, 32, 67))
    add_urdu_p(ep['subtitle'], size=14, italic=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=12, color=(100, 100, 100))
    add_urdu_p(f"خلاصہ: {ep['synopsis']}", size=11, italic=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=16, color=(80, 50, 20))
    
    paragraphs = [p.strip() for p in ep["content"].split("\n") if p.strip()]
    for p_text in paragraphs:
        add_urdu_p(p_text, size=13, space_after=10, align=WD_ALIGN_PARAGRAPH.JUSTIFY)

docx_path = os.path.join(urdu_dir, "Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.docx")
doc.save(docx_path)
print(f"Saved DOCX to {docx_path}")

downloads_docx = r"C:\Users\Huzaifa Mahi\Downloads\Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.docx"
shutil.copy2(docx_path, downloads_docx)
print(f"Copied DOCX to {downloads_docx}")

# 7. Convert to PDF using Microsoft Word COM
pdf_path = os.path.join(urdu_dir, "Rija_Ek_Beti_Ki_Sachi_Aap_Beeti_Complete_Edition.pdf")
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
    doc_com.SaveAs(pdf_path, FileFormat=17) # 17 = wdFormatPDF
    doc_com.Close()
    word.Quit()
    print(f"Generated PDF at {pdf_path}")
    shutil.copy2(pdf_path, downloads_pdf)
    print(f"Copied PDF to {downloads_pdf}")
except Exception as e:
    print(f"Word COM PDF export error: {e}")

print("Complete expanded novel build finished successfully!")
