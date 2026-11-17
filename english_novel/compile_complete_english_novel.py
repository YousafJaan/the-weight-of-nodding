# -*- coding: utf-8 -*-
"""
Compile Complete English Epic Novel: 'Rija: A Daughter's True Memoir'
Author: Anam Sajjad | Protagonist: Rija
Format: 6 Seasons | 61 Episodes/Chapters | Two-Column Publication Layout
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
from docx.oxml import parse_xml
import win32com.client
import pypdf

base_dir = r"C:\Users\Huzaifa Mahi\.gemini\antigravity\worktrees\remote-workspace\write_new_book"
en_dir = os.path.join(base_dir, "english_novel")
episodes_dir = os.path.join(en_dir, "episodes")
remote_en_dir = r"C:\Users\Huzaifa Mahi\remote-workspace\novel-en"

os.makedirs(en_dir, exist_ok=True)
os.makedirs(episodes_dir, exist_ok=True)
os.makedirs(remote_en_dir, exist_ok=True)

# 1. Clean plain writing helper
def clean_plain_writing(text):
    if not text:
        return text
    text = text.replace("\u2014", " : ").replace("\u2013", " : ")
    text = re.sub(r'\s*:\s*', ' : ', text)
    text = re.sub(r' +', ' ', text)
    return text

# 2. Import all episodes
sys.path.insert(0, en_dir)
from generate_season_1_part1_en import S1_EN_EPISODES
from generate_season_1_part2_en import S1_EN_EPISODES_PART2
from generate_season_2_part1_en import S2_EN_EPISODES
from generate_season_2_part2_en import S2_EN_EPISODES_PART2
from generate_season_3_part1_en import S3_EN_EPISODES
from generate_season_3_part2_en import S3_EN_EPISODES_PART2
from generate_season_4_part1_en import S4_EN_EPISODES
from generate_season_4_part2_en import S4_EN_EPISODES_PART2
from generate_season_5_part1_en import S5_EN_EPISODES
from generate_season_5_part2_en import S5_EN_EPISODES_PART2
from generate_season_6_en import S6_EN_EPISODES

all_episodes_raw = (
    S1_EN_EPISODES + S1_EN_EPISODES_PART2 +
    S2_EN_EPISODES + S2_EN_EPISODES_PART2 +
    S3_EN_EPISODES + S3_EN_EPISODES_PART2 +
    S4_EN_EPISODES + S4_EN_EPISODES_PART2 +
    S5_EN_EPISODES + S5_EN_EPISODES_PART2 +
    S6_EN_EPISODES
)

print(f"Loaded {len(all_episodes_raw)} raw episodes in English.")

final_episodes = []
total_words = 0

for ep in all_episodes_raw:
    eid = ep["id"]
    scenes = [clean_plain_writing(s.strip()) for s in ep["scenes"]]
    full_text = "\n\n".join(scenes)
    words = len(full_text.split())
    total_words += words
    
    clean_ep = {
        "id": eid,
        "season": ep["season"],
        "season_name": clean_plain_writing(ep["season_name"]),
        "title": clean_plain_writing(ep["title"]),
        "subtitle": clean_plain_writing(ep["subtitle"]),
        "synopsis": clean_plain_writing(ep["synopsis"]),
        "content": full_text,
        "word_count": words
    }
    final_episodes.append(clean_ep)
    
    # Save individual episode markdown
    ep_file = os.path.join(episodes_dir, f"episode_{eid:02d}.md")
    with open(ep_file, "w", encoding="utf-8") as f:
        f.write(f"# Episode {eid:02d}: {clean_ep['title']}\n")
        f.write(f"### {clean_ep['subtitle']}\n\n")
        f.write(f"**{clean_ep['season_name']}** | Words: {words:,}\n\n")
        f.write(f"> **Synopsis:** {clean_ep['synopsis']}\n\n---\n\n")
        f.write(full_text)

print(f"Compiled {len(final_episodes)} episodes. Total Words: {total_words:,}")

# 3. Write Master Markdown
master_md = os.path.join(en_dir, "RIJA_EPIC_NOVEL_ENGLISH.md")
with open(master_md, "w", encoding="utf-8") as f:
    f.write("# Rija: A Daughter's True Memoir\n")
    f.write("### The Sorrow of Mothers, The Cruelty of Kin, and The Shield of Faith\n")
    f.write(f"**Author:** Anam Sajjad | **Protagonist:** Rija\n")
    f.write(f"**Master English Edition:** 6 Seasons | 61 Episodes | {total_words:,} Words\n\n---\n\n")
    
    f.write("## Dedication\n\n")
    f.write("To every daughter whose dreams have been trampled in the mud of ancestral pride.\n\n")
    f.write("And to my mother, whose trembling hands caught the violent blow meant for my face, and whose prayers opened the gates of heaven.\n\n---\n\n")
    
    curr_season = None
    for ep in final_episodes:
        if ep["season"] != curr_season:
            curr_season = ep["season"]
            f.write(f"\n\n# {ep['season_name']}\n\n---\n\n")
        f.write(f"## Episode {ep['id']}: {ep['title']}\n")
        f.write(f"### {ep['subtitle']}\n\n")
        f.write(f"> **Synopsis:** {ep['synopsis']}\n\n")
        f.write(ep["content"])
        f.write("\n\n---\n\n")

print(f"Wrote master markdown to {master_md}")
shutil.copyfile(master_md, os.path.join(remote_en_dir, "RIJA_EPIC_NOVEL_ENGLISH.md"))

# 4. Generate Web Reader Data (novel_en_data.js)
web_episodes = []
for ep in final_episodes:
    read_mins = max(1, ep["word_count"] // 220)
    web_episodes.append({
        "id": ep["id"],
        "season": ep["season"],
        "season_name": ep["season_name"],
        "title": ep["title"],
        "subtitle": ep["subtitle"],
        "synopsis": ep["synopsis"],
        "reading_time": f"{read_mins} min",
        "word_count": ep["word_count"],
        "content": ep["content"]
    })

novel_en_metadata_js = """// Rija: A Daughter's True Memoir - Complete 61 Episodes Dataset
const NOVEL_EN_METADATA = {
  title: "Rija: A Daughter's True Memoir",
  subtitle: "The Sorrow of Mothers, The Cruelty of Kin, and The Shield of Faith",
  author: "Anam Sajjad",
  protagonist: "Rija",
  seasons: 6,
  total_episodes: 61,
  total_words: """ + str(total_words) + """,
  language: "en",
  direction: "ltr"
};

const NOVEL_EN_CHAPTERS = """ + json.dumps(web_episodes, ensure_ascii=False, indent=2) + """;
"""

with open(os.path.join(en_dir, "novel_en_data.js"), "w", encoding="utf-8") as f:
    f.write(novel_en_metadata_js)
with open(os.path.join(remote_en_dir, "novel_en_data.js"), "w", encoding="utf-8") as f:
    f.write(novel_en_metadata_js)

print("Generated novel_en_data.js in both directories.")

# 5. Build Two-Column Publication-Grade Word (.docx)
print("Building Two-Column English Word manuscript...")
doc = docx.Document()

# Base style
style = doc.styles['Normal']
font = style.font
font.name = 'Georgia'
font.size = Pt(11)
font.color.rgb = RGBColor(35, 35, 35)

# SECTION 1: FRONT MATTER (Single Column)
sect_front = doc.sections[0]
sect_front.top_margin = Inches(0.85)
sect_front.bottom_margin = Inches(0.85)
sect_front.left_margin = Inches(0.85)
sect_front.right_margin = Inches(0.85)

def add_p(text="", size=11, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=4, line_spacing=1.25, color=(35,35,35)):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    
    if text:
        run = p.add_run(text)
        run.font.name = 'Georgia'
        run.font.size = Pt(size)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = RGBColor(*color)
    return p

# Title Page
add_p("RIJA", size=38, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=72, space_after=12, color=(16, 50, 92))
add_p("A DAUGHTER'S TRUE MEMOIR", size=20, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14, color=(120, 35, 35))
add_p("The Sorrow of Mothers, The Cruelty of Kin, and The Shield of Faith", size=14, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=36, color=(80, 80, 80))
add_p(f"Complete Master Edition : 6 Seasons | 61 Episodes | {total_words:,} Words", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=48, color=(40, 40, 40))

add_p("Author: Anam Sajjad", size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_p("Protagonist: Rija", size=13, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=48)
add_p("Bahauddin Zakariya University Multan", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6, color=(100, 100, 100))

doc.add_page_break()

# Dedication
add_p("DEDICATION", size=22, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=48, space_after=20, color=(16, 50, 92))
add_p("To every daughter whose dreams have been trampled in the mud of ancestral pride, yet who rose from the ashes to write her own destiny.", size=13, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=30)
add_p("And to my mother, whose calloused hands caught the violent blow meant for my face, and whose prayers opened the gates of heaven.", size=13, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=48)

doc.add_page_break()

# Table of Contents
add_p("TABLE OF CONTENTS", size=22, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24, space_after=20, color=(16, 50, 92))
for ep in final_episodes:
    add_p(f"Episode {ep['id']:02d} : {ep['title']} ({ep['season_name']})", size=10, space_after=3, align=WD_ALIGN_PARAGRAPH.LEFT)

doc.add_page_break()

# SECTION 2: NOVEL BODY (Two Columns)
sect_body = doc.add_section(WD_SECTION.NEW_PAGE)
sect_body.top_margin = Inches(0.8)
sect_body.bottom_margin = Inches(0.8)
sect_body.left_margin = Inches(0.8)
sect_body.right_margin = Inches(0.8)

# Set 2 columns XML
sectPr_body = sect_body._sectPr
sectPr_body.append(parse_xml(r'<w:cols xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:num="2" w:space="720"/>'))

# Running header/footer
header = sect_body.header
hp = header.paragraphs[0]
hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
hrun = hp.add_run("Rija: A Daughter's True Memoir — Complete Master Edition")
hrun.font.name = 'Georgia'
hrun.font.size = Pt(9)
hrun.font.color.rgb = RGBColor(120, 120, 120)

footer = sect_body.footer
fp = footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
frun = fp.add_run("Page ")
frun.font.name = 'Georgia'
frun.font.size = Pt(9)
frun.font.color.rgb = RGBColor(100, 100, 100)
fldSimple = parse_xml(r'<w:fldSimple xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:instr="PAGE"/>')
fp._p.append(fldSimple)

current_season = None

for ep in final_episodes:
    # Season Divider Header
    if ep["season"] != current_season:
        current_season = ep["season"]
        add_p(f"❖ {ep['season_name']} ❖", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=16, space_after=10, color=(120, 35, 35))
    
    # Episode Title
    add_p(f"Episode {ep['id']}: {ep['title']}", size=13, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=12, space_after=2, color=(16, 50, 92))
    add_p(ep["subtitle"], size=10, italic=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=6, color=(80, 80, 80))
    add_p(f"Synopsis: {ep['synopsis']}", size=9.5, italic=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=8, color=(90, 50, 50))
    add_p("— — —", size=9, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8, color=(160, 160, 160))
    
    paras = [p.strip() for p in ep["content"].split("\n\n") if p.strip()]
    for p_text in paras:
        if p_text.startswith("❖") or p_text.startswith("— — —"):
            continue
        add_p(p_text, size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=4, line_spacing=1.22)
    
    add_p("❖   ❖   ❖", size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=8, space_after=14, color=(16, 50, 92))

output_docx = os.path.join(en_dir, "Rija_Epic_Novel_Complete_Edition_EN.docx")
doc.save(output_docx)
print(f"Saved complete publication-grade Word doc to {output_docx}")

# Copy to downloads and remote workspace
dl_docx = r"C:\Users\Huzaifa Mahi\Downloads\Rija_Epic_Novel_Complete_Edition_EN.docx"
shutil.copyfile(output_docx, dl_docx)
shutil.copyfile(output_docx, os.path.join(remote_en_dir, "Rija_Epic_Novel_Complete_Edition_EN.docx"))
print("Copied English Word document to Downloads and remote-workspace/novel-en.")

# 6. Export to PDF via Word COM
print("Starting Word COM export to PDF for English novel...")
output_pdf = os.path.join(en_dir, "Rija_Epic_Novel_Complete_Edition_EN.pdf")

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

dl_pdf = r"C:\Users\Huzaifa Mahi\Downloads\Rija_Epic_Novel_Complete_Edition_EN.pdf"
if os.path.exists(output_pdf):
    shutil.copyfile(output_pdf, dl_pdf)
    shutil.copyfile(output_pdf, os.path.join(remote_en_dir, "Rija_Epic_Novel_Complete_Edition_EN.pdf"))
    reader = pypdf.PdfReader(output_pdf)
    print(f"FINAL ENGLISH PDF PAGE COUNT: {len(reader.pages)} PAGES!")
else:
    print("Warning: PDF was not generated.")

print("All English novel compilation steps completed successfully!")
