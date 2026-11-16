# -*- coding: utf-8 -*-
"""
generate_reader_data.py
Generates the comprehensive JSON dataset for the interactive Web Reader App
from all 18 chapters of 'The Weight of Nodding'.
"""
import os
import json
import re

manuscript_dir = os.path.join(os.path.dirname(__file__), '..', 'manuscript')
output_dir = os.path.join(os.path.dirname(__file__), '..', 'reader_app')
os.makedirs(output_dir, exist_ok=True)

files_meta = [
    ('00_prologue.md', 'Prologue', 'The Cost of the Reflex (Seminar Room 4)'),
    ('01_chapter_1.md', 'Chapter 1', 'The February Midnight (Room 42 and the Immersion Rod)'),
    ('02_chapter_2.md', 'Chapter 2', 'The Red Line on Bosan Road (The Metro Corridor)'),
    ('03_chapter_3.md', 'Chapter 3', 'Behind the Green Iron Gates (Amna Hall and Maasi Sakina)'),
    ('04_chapter_4.md', 'Chapter 4', 'The Currency of Sifarish (Allotment over the Nullah)'),
    ('05_chapter_5.md', 'Chapter 5', 'The Circle of Seven (The Room 42 Secrets and Sisterhood)'),
    ('06_chapter_6.md', 'Chapter 6', 'Khara Paani (The Saline Water and Chemical Forensics)'),
    ('07_chapter_7.md', 'Chapter 7', "The Mess Token and the Midnight Ration (Haji Manzoor's Cartel)"),
    ('08_chapter_8.md', 'Chapter 8', 'The Metro Encounter (Meeting Yousaf - Workx / Quick Services)'),
    ('09_chapter_9.md', 'Chapter 9', "The Curfew Slip and the Father's Honor (Sidra's Extraction)"),
    ('10_chapter_10.md', 'Chapter 10', "The Photostat Archives (Chacha Asghar's Den)"),
    ('11_chapter_11.md', 'Chapter 11', 'The Strike, The Tear Gas, and The Suspended Metro'),
    ('12_chapter_12.md', 'Chapter 12', 'The 48-Degree Summer & Rooftop Secrets'),
    ('13_chapter_13.md', 'Chapter 13', 'The Breakdown (The Unknown Disease & Nishtar Wards)'),
    ('14_chapter_14.md', 'Chapter 14', 'The One-Year Drop (The Forge of Solitude)'),
    ('15_chapter_15.md', 'Chapter 15', 'The Thesis Monopoly vs. The Empirical Truth'),
    ('16_chapter_16.md', 'Chapter 16', 'The Breakthrough Paper (Pakistan Is Not Poor, It Is Poorly Managed)'),
    ('17_chapter_17.md', 'Chapter 17', 'Walking Bosan Road in 2026 (The Unbowed Head)')
]

chapters = []

for filename, part_num, title in files_meta:
    path = os.path.join(manuscript_dir, filename)
    with open(path, 'r', encoding='utf-8') as f:
        md = f.read()

    words = len(md.split())
    read_mins = max(1, round(words / 230))
    read_time = f"{read_mins} min read"

    lines = md.strip().split('\n')
    html_parts = []
    
    in_list = False
    list_type = None
    in_margin_box = False

    for line in lines:
        line_str = line.strip()
        if not line_str:
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
            continue

        if line_str.startswith('# '):
            continue
        elif "The Strategist's Margin" in line_str:
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
            if in_margin_box:
                html_parts.append("</div></div>")
            html_parts.append("<div class='strategist-margin-box'><div class='margin-header'><span class='margin-badge'>THE STRATEGIST'S MARGIN</span><h3>Tactical Protocols for Daring Women</h3></div><div class='margin-body'>")
            in_margin_box = True
        elif line_str.startswith('#### '):
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
            text = line_str[5:].strip()
            html_parts.append(f"<h4 class='protocol-title'>{text}</h4>")
        elif line_str.startswith('### '):
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
            text = line_str[4:].strip()
            html_parts.append(f"<h3>{text}</h3>")
        elif line_str.startswith('## '):
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
            text = line_str[3:].strip()
            html_parts.append(f"<h2>{text}</h2>")
        elif line_str.startswith('> '):
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
            text = line_str[2:].strip().replace('*', '')
            html_parts.append(f"<blockquote>{text}</blockquote>")
        elif line_str.startswith('* ') or line_str.startswith('- '):
            if not in_list or list_type != 'ul':
                if in_list: html_parts.append(f"</{list_type}>")
                html_parts.append("<ul>")
                in_list = True
                list_type = 'ul'
            item = line_str[2:].strip()
            item = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item)
            item = re.sub(r'\*(.*?)\*', r'<em>\1</em>', item)
            html_parts.append(f"<li>{item}</li>")
        elif re.match(r'^\d+\.\s', line_str):
            if not in_list or list_type != 'ol':
                if in_list: html_parts.append(f"</{list_type}>")
                html_parts.append("<ol>")
                in_list = True
                list_type = 'ol'
            item = re.sub(r'^\d+\.\s', '', line_str).strip()
            item = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item)
            item = re.sub(r'\*(.*?)\*', r'<em>\1</em>', item)
            html_parts.append(f"<li>{item}</li>")
        elif line_str == '---':
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
            if in_margin_box:
                html_parts.append("</div></div>")
                in_margin_box = False
            html_parts.append("<hr class='divider'/>")
        else:
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
            p = line_str
            p = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', p)
            p = re.sub(r'\*(.*?)\*', r'<em>\1</em>', p)
            html_parts.append(f"<p>{p}</p>")

    if in_list:
        html_parts.append(f"</{list_type}>")
    if in_margin_box:
        html_parts.append("</div></div>")

    chapters.append({
        "id": filename.replace('.md', ''),
        "part": part_num,
        "title": title,
        "words": words,
        "readTime": read_time,
        "contentHtml": "\n".join(html_parts)
    })

metadata = {
    "bookTitle": "The Weight of Nodding",
    "subtitle": "A Political Scientist's Two-Year Chronicle of Hostel Life, Institutional Silence, and the Cost of Agreement",
    "author": "Anam Sajjad",
    "institution": "Department of Political Science, Bahauddin Zakariya University (BZU), Multan",
    "leadResearch": "Pakistan Is Not Poor, It Is Poorly Managed",
    "doi": "10.5281/zenodo.24054373",
    "orcid": "0009-0004-6169-1703",
    "email": "anoom994@gmail.com",
    "totalWords": sum(c['words'] for c in chapters),
    "totalChapters": len(chapters),
    "edition": "Definitive 200+ Page Expanded Edition (November 2026)"
}

js_content = f"// The Weight of Nodding - Book Data & Metadata\nconst BOOK_METADATA = {json.dumps(metadata, indent=2, ensure_ascii=False)};\nconst BOOK_DATA = {json.dumps(chapters, indent=2, ensure_ascii=False)};\n"

out_file = os.path.join(output_dir, 'chapters_data.js')
with open(out_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully generated {out_file} with {len(chapters)} chapters, total words: {metadata['totalWords']:,}!")
