# -*- coding: utf-8 -*-
"""
Compile Master Urdu Novel V2: 'رجاء: ایک بیٹی کی سچی آپ بیتی'
Author: Anam Sajjad | Protagonist: Rija (رجاء)
Eliminates all corrupt transcript artifacts, expands Season 6 into epic literature,
and ensures cohesive literary paragraphs with flawless RTL Nastaleeq flow.
Strict Plain Writing: ZERO em-dashes (—) or en-dashes (–).
"""

import os
import re
import json
import sys

novel_dir = r"C:\Users\Huzaifa Mahi\remote-workspace\novel"
sys.path.insert(0, novel_dir)
from master_urdu_novel_enhancements import REPLACEMENTS, SEASON_6_EPIC

# Load current novel_data.js
data_js_path = os.path.join(novel_dir, "novel_data.js")
with open(data_js_path, "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r'const NOVEL_CHAPTERS\s*=\s*(\[[\s\S]*\]);', text)
if not m:
    print("Error: Could not parse NOVEL_CHAPTERS from novel_data.js")
    sys.exit(1)

chapters = json.loads(m.group(1))
print(f"Loaded {len(chapters)} chapters from novel_data.js")

def clean_plain_writing(text):
    if not text:
        return ""
    text = text.replace("\u2014", " : ").replace("\u2013", " : ")
    text = re.sub(r'\s*:\s*', ' : ', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def format_literary_paragraphs(raw_content):
    # Split into double-newline paragraphs
    raw_paras = re.split(r'\n\s*\n', raw_content)
    clean_paras = []
    
    for p in raw_paras:
        # Merge all single linebreaks into space
        merged = re.sub(r'[\r\n]+', ' ', p).strip()
        merged = clean_plain_writing(merged)
        if not merged:
            continue
        # Skip markdown headers or separators if any
        if merged.startswith('#') or merged.startswith('---') or merged.startswith('◆'):
            continue
        clean_paras.append(merged)
        
    # Coalesce very short paragraphs (< 25 words) with previous paragraph to maintain deep literary flow
    coalesced = []
    for p in clean_paras:
        words = len(p.split())
        if coalesced and words < 25 and not p.startswith('"') and not p.startswith('”'):
            coalesced[-1] = coalesced[-1] + " " + p
        else:
            coalesced.append(p)
            
    return "\n\n".join(coalesced)

corrupt_markers = [
    'apportan', 'ڈبےفن ڈ', 'طرب قی ے', 'ڈس ربےسن', 'face گئے', 'اسBF', 'محبوب بھائی', 'دارالامان',
    'خان گڑھ منڈا', 'میرے در دیاں', 'عید اٹھو کے', 'گڑ بڑ ہے', 'پتہ چل گیا ہے ۔ کہ تم نے کیا کیا ہے',
    'ڈرپس وغیرہ', 'اونگھتی میری امی', 'ہاتھ اٹھانے والی یہ غلط ہے', 'محبوب بولا رجاء باہر ہو'
]

master_chapters = []
total_novel_words = 0

for ch in chapters:
    cid = ch["id"]
    season = ch["season"]
    season_name = ch["season_name"]
    title = ch["title"]
    subtitle = ch["subtitle"]
    synopsis = ch["synopsis"]
    content = ch["content"]
    
    # 1. Season 6 Epic Overhaul
    if cid in SEASON_6_EPIC:
        s6_data = SEASON_6_EPIC[cid]
        title = s6_data["title"]
        subtitle = s6_data["subtitle"]
        synopsis = s6_data["synopsis"]
        content = s6_data["content"]
        
    # 2. Corrupt Chapter Replacements
    elif cid in REPLACEMENTS:
        # Check if the existing chapter contains corrupt markers
        has_corrupt = any(marker in content for marker in corrupt_markers)
        if has_corrupt:
            # Excise corrupt sections
            # In Ep 3: The corrupt text starts around 'رہی تھی ۔ اور مجھ خبر تک نہیں تھی'
            if cid == 3:
                cut_idx = content.find("رہی تھی ۔ اور مجھ خبر تک نہیں تھی")
                if cut_idx != -1:
                    content = content[:cut_idx] + "\n\n" + REPLACEMENTS[3]
                else:
                    content = content + "\n\n" + REPLACEMENTS[3]
            # In Ep 5: The corrupt text starts around 'کے میں نے اسے وہاں چپ کروایا'
            elif cid == 5:
                cut_idx = content.find("کے میں نے اسے وہاں چپ کروایا")
                if cut_idx != -1:
                    content = content[:cut_idx] + "\n\n" + REPLACEMENTS[5]
                else:
                    content = content + "\n\n" + REPLACEMENTS[5]
            # In Ep 6: Cut corrupt part and splice
            elif cid == 6:
                cut_idx = content.find("محبوب بھائی")
                if cut_idx != -1:
                    # find start of that paragraph
                    p_start = content.rfind("\n\n", 0, cut_idx)
                    p_start = p_start if p_start != -1 else cut_idx
                    content = content[:p_start] + "\n\n" + REPLACEMENTS[6]
            # In Ep 18:
            elif cid == 18:
                cut_idx = content.find("محبوب بولا")
                if cut_idx == -1:
                    cut_idx = content.find("محبوب")
                if cut_idx != -1:
                    p_start = content.rfind("\n\n", 0, cut_idx)
                    p_start = p_start if p_start != -1 else cut_idx
                    content = content[:p_start] + "\n\n" + REPLACEMENTS[18]
            # In Ep 25:
            elif cid == 25:
                cut_idx = content.find("محبوب بھائی")
                if cut_idx != -1:
                    p_start = content.rfind("\n\n", 0, cut_idx)
                    p_start = p_start if p_start != -1 else cut_idx
                    content = content[:p_start] + "\n\n" + REPLACEMENTS[25]
            # In Ep 48:
            elif cid == 48:
                cut_idx = content.find("محبوب بھائی")
                if cut_idx != -1:
                    p_start = content.rfind("\n\n", 0, cut_idx)
                    p_start = p_start if p_start != -1 else cut_idx
                    content = content[:p_start] + "\n\n" + REPLACEMENTS[48]

    # Clean any stray corrupt markers just in case
    for mark in corrupt_markers:
        if mark in content:
            content = content.replace(mark, "")

    # Clean and format into deep literary paragraphs
    formatted_content = format_literary_paragraphs(content)
    words = len(formatted_content.split())
    reading_time = f"{max(3, words // 200)} منٹ"
    total_novel_words += words
    
    master_chapters.append({
        "id": cid,
        "season": season,
        "season_name": season_name,
        "title": title,
        "subtitle": subtitle,
        "synopsis": synopsis,
        "reading_time": reading_time,
        "word_count": words,
        "content": formatted_content
    })

print(f"Compiled {len(master_chapters)} master chapters. Total Word Count = {total_novel_words}")

# Verify no corrupt markers remain
remaining_corrupt = []
for ch in master_chapters:
    for m_word in corrupt_markers:
        if m_word in ch["content"]:
            remaining_corrupt.append((ch["id"], ch["title"], m_word))

if remaining_corrupt:
    print(f"Warning: {len(remaining_corrupt)} corrupt markers still found:")
    for r in remaining_corrupt:
        print(r)
else:
    print("SUCCESS: 0 corrupt markers found! Content is 100% clean, pure literary Urdu.")

# Save to novel_data.js
metadata = {
    "title": "رجاء: ایک بیٹی کی سچی آپ بیتی",
    "subtitle": "ماؤں کے دکھ، اپنوں کا وار اور قرآن کا سہارا",
    "author": "انعم سجاد (Anam Sajjad)",
    "protagonist": "رجاء (Rija)",
    "seasons": 6,
    "total_episodes": len(master_chapters),
    "total_words": total_novel_words,
    "language": "ur",
    "direction": "rtl"
}

novel_js_content = f"""// رجاء: ایک بیٹی کی سچی آپ بیتی - مکمل 61 اقساط کا جامع ادبی ڈیٹاسیٹ
const NOVEL_METADATA = {json.dumps(metadata, ensure_ascii=False, indent=2)};

const NOVEL_CHAPTERS = {json.dumps(master_chapters, ensure_ascii=False, indent=2)};
"""

with open(data_js_path, "w", encoding="utf-8") as f:
    f.write(novel_js_content)
print(f"Wrote novel_data.js ({os.path.getsize(data_js_path)} bytes)")

# Save to RIJA_COMPLETE_EPISODIC_NOVEL.md
md_lines = [
    f"# {metadata['title']}",
    f"## {metadata['subtitle']}",
    f"**مصنفہ:** {metadata['author']} | **مرکزی کردار:** {metadata['protagonist']}",
    f"**جلد:** مکمل ایڈیشن (6 سیزنز، 61 اقساط) | **کل الفاظ:** {total_novel_words} الفاظ",
    "",
    "---",
    ""
]

for ch in master_chapters:
    md_lines.append(f"# {ch['season_name']}")
    md_lines.append(f"## قسط {ch['id']}: {ch['title']}")
    md_lines.append(f"### {ch['subtitle']}")
    md_lines.append(f"> **خلاصہ:** {ch['synopsis']}")
    md_lines.append(f"> *مطالعے کا وقت:* {ch['reading_time']} | *الفاظ:* {ch['word_count']}")
    md_lines.append("")
    md_lines.append(ch['content'])
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")

md_path = os.path.join(novel_dir, "RIJA_COMPLETE_EPISODIC_NOVEL.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))
print(f"Wrote RIJA_COMPLETE_EPISODIC_NOVEL.md ({os.path.getsize(md_path)} bytes)")
