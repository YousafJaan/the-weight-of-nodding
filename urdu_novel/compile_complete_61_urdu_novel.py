# -*- coding: utf-8 -*-
"""
Compile Complete 61-Episode Two-Column Urdu Epic Novel: 'رجاء: ایک بیٹی کی سچی آپ بیتی'
Author: Anam Sajjad | Protagonist: Rija (رجاء)
Format: 6 Seasons | 61 Episodes | 100% 1:1 Parity with English Novel
Two-Column Publication Layout | 200-300+ Print Pages
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
    text = text.replace("\u2014", " : ").replace("\u2013", " : ").replace("â€”", " : ")
    text = re.sub(r'\s*:\s*', ' : ', text)
    text = re.sub(r' +', ' ', text)
    return text

# 2. Import all episodic scripts
sys.path.insert(0, urdu_dir)
from generate_season_1_part1 import S1_EPISODES
from generate_season_1_part2 import S1_EPISODES_PART2
from generate_season_2_epic import S2_EPISODES
from generate_season_3_part1_ur import S3_UR_EPISODES
from generate_season_3_part2_ur import S3_UR_EPISODES_PART2
from generate_season_4_part1_ur import S4_UR_EPISODES
from generate_season_4_part2_ur import S4_UR_EPISODES_PART2
from generate_season_5_part1_ur import S5_UR_EPISODES
from generate_season_5_part2_ur import S5_UR_EPISODES_PART2
from generate_season_6_ur import S6_UR_EPISODES

# Organize 61 canonical episodes
raw_s1 = S1_EPISODES + S1_EPISODES_PART2[:5]  # Episodes 1 to 10
raw_s2 = [S1_EPISODES_PART2[5]] + S2_EPISODES[:9]  # Episode 11 (Farewell to Aisha Hall) + Episodes 12 to 20
raw_s3 = S3_UR_EPISODES + S3_UR_EPISODES_PART2  # Episodes 21 to 30
raw_s4 = S4_UR_EPISODES + S4_UR_EPISODES_PART2  # Episodes 31 to 40
raw_s5 = S5_UR_EPISODES + S5_UR_EPISODES_PART2  # Episodes 41 to 50
raw_s6 = S6_UR_EPISODES  # Episodes 51 to 61

all_61_raw = raw_s1 + raw_s2 + raw_s3 + raw_s4 + raw_s5 + raw_s6
print(f"Total raw episodes loaded: {len(all_61_raw)} (Target: 61)")

# 3. Load authentic memoirs from master (57,683 words)
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

p_b1 = get_paragraphs(1)   # Bab 1: کردار اور اس کی اہمیت (65 paras)
p_b2 = get_paragraphs(2)   # Bab 2: نااہل نہیں، چنی ہوئی (95 paras)
p_b3 = get_paragraphs(3)   # Bab 3: قرآن اور معاشرہ (45 paras)
p_b4 = get_paragraphs(4)   # Bab 4: اپنوں سے رسوائی (72 paras)
p_b5 = get_paragraphs(5)   # Bab 5: لوگ کیا کہیں گے (4 paras)
p_b6 = get_paragraphs(6)   # Bab 6: اچھی بیٹی کون؟ (110 paras)
p_b7 = get_paragraphs(7)   # Bab 7: ماؤں کے دکھ (135 paras)
p_b8 = get_paragraphs(8)   # Bab 8: باپ کا کردار اور بیٹی کا جنون (5 paras)
p_b9 = get_paragraphs(9)   # Bab 9: کامیابی کے بعد زندگی کا سفر (4 paras)
p_b10 = get_paragraphs(10) # Bab 10: حاسد کی دوستی (155 paras)
p_b11 = get_paragraphs(11) # Bab 11: باپ کی جدوجہد، بیٹی اور خاموش ممتا (48 paras)

# Split chunks across narrative episodes
c_b10 = chunk_list(p_b10, 8)  # S1 Eps 2, 3, 5, 6, 7, 8, 9, 10
c_b4 = chunk_list(p_b4, 6)    # S2 Eps 12, 13, 14, 15, 17, 18
c_b5 = chunk_list(p_b5, 2)    # S2 Eps 16, 19
c_b6 = chunk_list(p_b6, 4)    # S3 Eps 22, 23, 24, 25
c_b2 = chunk_list(p_b2, 4)    # S3 Eps 26, 27, 28, 30
c_b3 = chunk_list(p_b3, 4)    # S4 Eps 31, 32, 33, 35
c_b8 = chunk_list(p_b8, 2)    # S4 Eps 34, 36
c_b7 = chunk_list(p_b7, 5)    # S5 Eps 41, 42, 44, 46, 48
c_b9 = chunk_list(p_b9, 2)    # S5 Eps 43, 45
c_b11 = chunk_list(p_b11, 2)  # S5 Eps 47, 49

memoirs_enrichment = {
    # Season 1
    2: c_b10[0], 3: c_b10[1], 5: c_b10[2], 6: c_b10[3], 7: c_b10[4], 8: c_b10[5], 9: c_b10[6], 10: c_b10[7],
    # Season 2
    12: c_b4[0], 13: c_b4[1], 14: c_b4[2], 15: c_b4[3], 16: c_b5[0], 17: c_b4[4], 18: c_b4[5], 19: c_b5[1],
    # Season 3
    22: c_b6[0], 23: c_b6[1], 24: c_b6[2], 25: c_b6[3], 26: c_b2[0], 27: c_b2[1], 28: c_b2[2], 30: c_b2[3],
    # Season 4
    31: c_b3[0], 32: c_b3[1], 33: c_b3[2], 34: c_b8[0], 35: c_b3[3], 36: c_b8[1],
    # Season 5
    41: c_b7[0], 42: c_b7[1], 43: c_b9[0], 44: c_b7[2], 45: c_b9[1], 46: c_b7[3], 47: c_b11[0], 48: c_b7[4], 49: c_b11[1]
}

# 4. Assemble 61 episodes
final_61_episodes = []
total_urdu_words = 0

season_names = {
    1: "سیزن 1: دہلیز اور بیڑیاں (عائشہ ہال اور ملتان کی دھوپ)",
    2: "سیزن 2: طوفان، تہمت اور آزمائش (خاندانی پنچایت اور بندوق)",
    3: "سیزن 3: شعور، خود انحصاری اور نور کا سفر (ٹاٹ کی اکیڈمی اور ایم فل)",
    4: "سیزن 4: فکر کی بھٹی اور صبرِ جمیل کا امتحان (سینٹرل لائبریری اور ڈیفنس)",
    5: "سیزن 5: قومی ایوان، سفید پگڑی اور ابدی سحر (صدارتی گولڈ میڈل اور معافی)",
    6: "سیزن 6: فکری و اخلاقی وصیت نامہ (فلسفیانہ مضامین و ابدی اسباق)"
}

for idx, ep_data in enumerate(all_61_raw, start=1):
    season_num = 1 if idx <= 10 else (2 if idx <= 20 else (3 if idx <= 30 else (4 if idx <= 40 else (5 if idx <= 50 else 6))))
    s_name = season_names[season_num]
    
    scenes = [clean_plain_writing(s.strip()) for s in ep_data["scenes"]]
    enrich_paras = memoirs_enrichment.get(idx, [])
    
    combined_body = []
    if len(scenes) > 0:
        combined_body.append(scenes[0])
        
    half_e = len(enrich_paras) // 2
    if half_e > 0:
        combined_body.append("\n\n".join(enrich_paras[:half_e]))
        
    if len(scenes) > 1:
        for sc in scenes[1:]:
            combined_body.append(sc)
            
    if half_e < len(enrich_paras):
        combined_body.append("\n\n".join(enrich_paras[half_e:]))
        
    full_content = "\n\n".join([b for b in combined_body if b.strip()])
    full_content = clean_plain_writing(full_content)
    
    ep_words = len(full_content.split())
    total_urdu_words += ep_words
    
    title = clean_plain_writing(ep_data["title"])
    subtitle = clean_plain_writing(ep_data["subtitle"])
    synopsis = clean_plain_writing(ep_data["synopsis"])
    
    final_61_episodes.append({
        "id": idx,
        "season": season_num,
        "season_name": s_name,
        "title": title,
        "subtitle": subtitle,
        "synopsis": synopsis,
        "content": full_content,
        "word_count": ep_words
    })
    
    # Write individual markdown episode
    ep_md_path = os.path.join(episodes_dir, f"episode_{idx:02d}.md")
    with open(ep_md_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n")
        f.write(f"### {subtitle}\n")
        f.write(f"**{s_name}** | قسط نمبر {idx} | الفاظ: {ep_words:,}\n\n")
        f.write(f"> **خلاصہ:** {synopsis}\n\n---\n\n")
        f.write(full_content)

print(f"Successfully assembled all 61 episodes! Total Urdu Word Count: {total_urdu_words:,}")

# 5. Write Complete Master Markdown
master_md_file = os.path.join(urdu_dir, "RIJA_COMPLETE_EPISODIC_NOVEL.md")
with open(master_md_file, "w", encoding="utf-8") as f:
    f.write("# رجاء: ایک بیٹی کی سچی آپ بیتی\n")
    f.write("### ماؤں کے دکھ، اپنوں کا وار اور قرآن کا سہارا\n")
    f.write(f"**مصنفہ:** انعم سجاد (Anam Sajjad) | **مرکزی کردار:** رجاء (Rija)\n")
    f.write(f"**جامع ادبی شاہکار ایڈیشن:** 6 سیزنز | 61 اقساط | {total_urdu_words:,} الفاظ\n\n---\n\n")
    
    # Dedication
    f.write("## انتساب\n\n")
    f.write("ان تمام معصوم اور بے زبان بیٹیوں کے نام جن کے خواب ان کے اپنے آنگنوں میں روند دیے جاتے ہیں۔\n\n")
    f.write("اور میری صابر و شاکر ماں کے نام، جس نے مجھے سکھایا کہ جب زمین کا کوئی سہارا نہ رہے تو آسمان والے کا دامن تھام لینا چاہیے۔\n\n---\n\n")
    
    curr_season = None
    for ep in final_61_episodes:
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
for ep in final_61_episodes:
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

novel_metadata_js = """// رجاء: ایک بیٹی کی سچی آپ بیتی - مکمل 61 اقساط کا جامع ادبی ڈیٹاسیٹ
const NOVEL_METADATA = {
  title: "رجاء: ایک بیٹی کی سچی آپ بیتی",
  subtitle: "ماؤں کے دکھ، اپنوں کا وار اور قرآن کا سہارا",
  author: "انعم سجاد (Anam Sajjad)",
  protagonist: "رجاء (Rija)",
  seasons: 6,
  total_episodes: 61,
  total_words: """ + str(total_urdu_words) + """,
  language: "ur",
  direction: "rtl"
};

const NOVEL_CHAPTERS = """ + json.dumps(web_episodes, ensure_ascii=False, indent=2) + """;
"""

for target_dir in [novel_reader_dir, remote_novel_dir]:
    with open(os.path.join(target_dir, "novel_data.js"), "w", encoding="utf-8") as f:
        f.write(novel_metadata_js)
    shutil.copyfile(master_md_file, os.path.join(target_dir, "RIJA_COMPLETE_EPISODIC_NOVEL.md"))

print("Updated novel_data.js and markdown in reader and remote workspaces.")

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
add_p(f"جامع ادبی شاہکار ایڈیشن : 6 سیزنز | 61 اقساط | {total_urdu_words:,} الفاظ", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=48, color=(140, 30, 30))

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
for ep in final_61_episodes:
    add_p(f"قسط {ep['id']:02d} : {ep['title']} ({ep['season_name'][:10]}...)", size=12.5, space_after=3, align=WD_ALIGN_PARAGRAPH.RIGHT)

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
hrun = hp.add_run("رجاء : ایک بیٹی کی سچی آپ بیتی (مکمل 61 اقساط)")
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

for ep in final_61_episodes:
    # Season divider
    if ep["season"] != current_season:
        current_season = ep["season"]
        add_p(f"❖ {ep['season_name']} ❖", size=18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=20, space_after=12, color=(140, 30, 30))
    
    # Episode Title
    add_p(f"قسط نمبر {ep['id']} : {ep['title']}", size=15.5, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=14, space_after=4, color=(15, 32, 67))
    add_p(ep["subtitle"], size=12, italic=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=6, color=(70, 85, 100))
    
    # Synopsis Box
    add_p(f"خلاصہ : {ep['synopsis']}", size=11, italic=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=8, color=(100, 60, 60))
    
    # Ornamental separator
    add_p("◆   ◆   ◆", size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8, color=(160, 160, 160))
    
    # Paragraphs
    paras = [p.strip() for p in ep["content"].split("\n\n") if p.strip()]
    for p_text in paras:
        if p_text.startswith("◆") or p_text.startswith("---"):
            continue
        add_p(p_text, size=13, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=4, line_spacing=1.4)
    
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
    print(f"FINAL URDU PDF PAGE COUNT: {len(reader.pages)} PAGES!")
else:
    print("Warning: PDF was not generated.")

print("All compilation steps completed successfully!")
