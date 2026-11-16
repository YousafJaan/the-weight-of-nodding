# -*- coding: utf-8 -*-
"""
build_docx.py
Compiles 'The Weight of Nodding' into a publishing-grade 6x9 trade paperback Word document (.docx)
and automatically exports it to a high-resolution, print-ready PDF via Word COM.
"""
import os
import re
import glob
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_formatted_runs(paragraph, text, base_font='Georgia', base_size=Pt(10.5), base_color=RGBColor(0x22, 0x22, 0x22)):
    tokens = re.split(r'(\*\*.*?\*\*|\*.*?\*)', text)
    for token in tokens:
        if not token:
            continue
        if token.startswith('**') and token.endswith('**'):
            r = paragraph.add_run(token[2:-2])
            r.font.name = base_font
            r.font.size = base_size
            r.font.bold = True
            r.font.color.rgb = base_color
        elif token.startswith('*') and token.endswith('*'):
            r = paragraph.add_run(token[1:-1])
            r.font.name = base_font
            r.font.size = base_size
            r.font.italic = True
            r.font.color.rgb = base_color
        else:
            r = paragraph.add_run(token)
            r.font.name = base_font
            r.font.size = base_size
            r.font.color.rgb = base_color

def create_book_document():
    doc = Document()

    # 6x9 inch Trade Paperback Geometry
    for section in doc.sections:
        section.page_width = Inches(6.0)
        section.page_height = Inches(9.0)
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.85)   # Inside gutter margin for binding
        section.right_margin = Inches(0.75)  # Outside margin
        section.different_first_page_header_footer = True

    # Base Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Georgia'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    normal_style.paragraph_format.line_spacing = 1.35
    normal_style.paragraph_format.space_after = Pt(6)

    # ---------------------------------------------------------------------------
    # HALF-TITLE PAGE
    # ---------------------------------------------------------------------------
    p_ht = doc.add_paragraph()
    p_ht.paragraph_format.space_before = Pt(144)
    p_ht.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_ht = p_ht.add_run("THE WEIGHT OF NODDING")
    r_ht.font.name = 'Georgia'
    r_ht.font.size = Pt(18)
    r_ht.font.bold = True
    r_ht.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    doc.add_page_break()

    # ---------------------------------------------------------------------------
    # MAIN TITLE PAGE
    # ---------------------------------------------------------------------------
    p_pre = doc.add_paragraph()
    p_pre.paragraph_format.space_before = Pt(72)
    p_pre.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(10)
    r_t1 = p_title.add_run("THE WEIGHT OF NODDING")
    r_t1.font.name = 'Georgia'
    r_t1.font.size = Pt(22)
    r_t1.font.bold = True
    r_t1.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(36)
    r_sub = p_sub.add_run("A Political Scientist's Two-Year Chronicle of Hostel Life,\nInstitutional Silence, and the Cost of Agreement")
    r_sub.font.name = 'Georgia'
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    p_author = doc.add_paragraph()
    p_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_author.paragraph_format.space_before = Pt(40)
    p_author.paragraph_format.space_after = Pt(4)
    r_auth = p_author.add_run("ANAM SAJJAD")
    r_auth.font.name = 'Georgia'
    r_auth.font.size = Pt(13)
    r_auth.font.bold = True
    r_auth.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

    p_affil = doc.add_paragraph()
    p_affil.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_affil.paragraph_format.space_after = Pt(72)
    r_aff = p_affil.add_run("Department of Political Science\nBahauddin Zakariya University, Multan\nLead Author: Pakistan Is Not Poor, It Is Poorly Managed\nCERN Zenodo DOI: 10.5281/zenodo.24054373")
    r_aff.font.name = 'Georgia'
    r_aff.font.size = Pt(9.5)
    r_aff.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    doc.add_page_break()

    # ---------------------------------------------------------------------------
    # COPYRIGHT PAGE
    # ---------------------------------------------------------------------------
    p_c = doc.add_paragraph()
    p_c.paragraph_format.space_before = Pt(160)
    r_c = p_c.add_run("The Weight of Nodding: A Political Scientist's Two-Year Chronicle of Hostel Life, Institutional Silence, and the Cost of Agreement\n\n"
                      "Copyright (c) 2024-2026 by Anam Sajjad. All rights reserved.\n"
                      "Definitive Expanded Edition: November 2026.\n"
                      "Published in Multan & Islamabad, Pakistan.\n\n"
                      "Academic Affiliation:\n"
                      "Department of Political Science, Bahauddin Zakariya University, Bosan Road, Multan 60800, Punjab, Pakistan.\n"
                      "Author Email: anoom994@gmail.com | ORCID iD: 0009-0004-6169-1703\n\n"
                      "Peer-Reviewed Empirical Publication:\n"
                      "Sajjad, A., & Yousaf. (2024). Pakistan Is Not Poor, It Is Poorly Managed: An Empirical Investigation of Energy, Water, and Demographics in Pakistan. CERN Zenodo. DOI: 10.5281/zenodo.24054373.\n\n"
                      "Cataloging-in-Publication Data:\n"
                      "1. Political Science -- Pakistan -- Higher Education. 2. Student Movements -- Southern Punjab -- Bahauddin Zakariya University. 3. Women in Higher Education -- Social Conditions. 4. Governance, Energy Economics & Public Policy -- Pakistan.\n\n"
                      "Typeset in Georgia Pro and Garamond styles in 6x9 trade paperback format.\n"
                      "Printed and bound in the Islamic Republic of Pakistan.")
    r_c.font.name = 'Georgia'
    r_c.font.size = Pt(8.5)
    r_c.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    doc.add_page_break()

    # ---------------------------------------------------------------------------
    # DEDICATION
    # ---------------------------------------------------------------------------
    p_ded = doc.add_paragraph()
    p_ded.paragraph_format.space_before = Pt(120)
    p_ded.paragraph_format.space_after = Pt(16)
    p_ded.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_ded = p_ded.add_run("To the young women of Southern Punjab,\nwho drag heavy green tin trunks across the burning gravel of Bosan Road;\n\n"
                          "To my seven sisters of Room 42:\nAqsa, Anza, Saba, Momina, Sidra, Iqra, and Palwasha,\nwho proved that when women stand together in the dark, no iron gate can hold them;\n\n"
                          "To Yousaf and the team at Quick Services and Workx,\nwho taught me that verified arithmetic is the ultimate weapon against institutional decay;\n\n"
                          "And to my father,\nwho worked thirty-four years with ink-stained hands in government offices so his daughter could enter the doors of higher education:\n\n"
                          "This book is your mirror.\nKeep your head high. We will never nod again.")
    r_ded.font.name = 'Georgia'
    r_ded.font.size = Pt(10.5)
    r_ded.font.italic = True
    r_ded.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

    doc.add_page_break()

    # ---------------------------------------------------------------------------
    # TABLE OF CONTENTS
    # ---------------------------------------------------------------------------
    p_toctitle = doc.add_paragraph()
    p_toctitle.paragraph_format.space_before = Pt(36)
    p_toctitle.paragraph_format.space_after = Pt(20)
    p_toctitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_tt = p_toctitle.add_run("TABLE OF CONTENTS")
    r_tt.font.name = 'Georgia'
    r_tt.font.size = Pt(14)
    r_tt.font.bold = True
    r_tt.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    toc_items = [
        ("Prologue", "The Cost of the Reflex (Seminar Room 4)"),
        ("Chapter 1", "The February Midnight (Room 42 and the Immersion Rod)"),
        ("Chapter 2", "The Red Line on Bosan Road (The Metro Corridor)"),
        ("Chapter 3", "Behind the Green Iron Gates (Amna Hall and Maasi Sakina)"),
        ("Chapter 4", "The Currency of Sifarish (Allotment over the Nullah)"),
        ("Chapter 5", "The Circle of Seven (The Room 42 Secrets and Sisterhood)"),
        ("Chapter 6", "Khara Paani (The Saline Water and Chemical Forensics)"),
        ("Chapter 7", "The Mess Token and the Midnight Ration (Haji Manzoor's Cartel)"),
        ("Chapter 8", "The Metro Encounter (Meeting Yousaf - Workx / Quick Services)"),
        ("Chapter 9", "The Curfew Slip and the Father's Honor (Sidra's Extraction)"),
        ("Chapter 10", "The Photostat Archives (Chacha Asghar's Den)"),
        ("Chapter 11", "The Strike, The Tear Gas, and The Suspended Metro"),
        ("Chapter 12", "The 48-Degree Summer & Rooftop Secrets"),
        ("Chapter 13", "The Breakdown (The Unknown Disease & Nishtar Wards)"),
        ("Chapter 14", "The One-Year Drop (The Forge of Solitude)"),
        ("Chapter 15", "The Thesis Monopoly vs. The Empirical Truth"),
        ("Chapter 16", "The Breakthrough Paper (Pakistan Is Not Poor, It Is Poorly Managed)"),
        ("Chapter 17", "Walking Bosan Road in 2026 (The Unbowed Head)")
    ]

    table = doc.add_table(rows=0, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    for part, title in toc_items:
        row = table.add_row()
        c0 = row.cells[0]
        c1 = row.cells[1]
        c0.width = Inches(1.5)
        c1.width = Inches(3.2)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(4)
        r0 = p0.add_run(part)
        r0.font.bold = True
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(4)
        r1 = p1.add_run(title)
        r1.font.size = Pt(9.5)

    doc.add_page_break()

    # ---------------------------------------------------------------------------
    # CHAPTERS
    # ---------------------------------------------------------------------------
    manuscript_dir = os.path.join(os.path.dirname(__file__), '..', 'manuscript')
    files = sorted([f for f in glob.glob(os.path.join(manuscript_dir, '*.md')) if not f.endswith('FULL_MANUSCRIPT.md')])

    for idx, filepath in enumerate(files):
        with open(filepath, 'r', encoding='utf-8') as fl:
            raw = fl.read()

        lines = raw.strip().split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue

            # CHAPTER HEADER (# Title)
            if line.startswith('# '):
                p_ch = doc.add_paragraph()
                p_ch.paragraph_format.space_before = Pt(48)
                p_ch.paragraph_format.space_after = Pt(18)
                p_ch.alignment = WD_ALIGN_PARAGRAPH.CENTER
                title_text = line[2:].strip().upper()
                r_ch = p_ch.add_run(title_text)
                r_ch.font.name = 'Georgia'
                r_ch.font.size = Pt(14)
                r_ch.font.bold = True
                r_ch.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

            # SUBHEADER (### The Strategist's Margin)
            elif 'The Strategist\'s Margin' in line:
                # Add elegant decorative divider
                p_div = doc.add_paragraph()
                p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_div.paragraph_format.space_before = Pt(20)
                p_div.paragraph_format.space_after = Pt(12)
                r_div = p_div.add_run("* * *")
                r_div.font.size = Pt(12)
                r_div.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

                # Callout Box Table
                callout_table = doc.add_table(rows=1, cols=1)
                callout_table.alignment = WD_TABLE_ALIGNMENT.CENTER
                callout_table.autofit = False
                callout_cell = callout_table.cell(0, 0)
                callout_cell.width = Inches(4.7)
                set_cell_background(callout_cell, "F4F6F9")
                set_cell_margins(callout_cell, top=160, bottom=160, left=200, right=200)

                cp = callout_cell.paragraphs[0]
                cp.paragraph_format.space_after = Pt(6)
                r_sm = cp.add_run("THE STRATEGIST'S MARGIN\nTactical Protocols for Daring Women")
                r_sm.font.name = 'Georgia'
                r_sm.font.bold = True
                r_sm.font.size = Pt(11)
                r_sm.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

                # Process the protocol lines within the box
                i += 1
                while i < len(lines):
                    subline = lines[i].strip()
                    if not subline:
                        i += 1
                        continue
                    if subline.startswith('#') and not subline.startswith('####'):
                        # End of chapter
                        break
                    if subline.startswith('---'):
                        i += 1
                        continue

                    cp_item = callout_cell.add_paragraph()
                    cp_item.paragraph_format.space_after = Pt(4)
                    if subline.startswith('#### '):
                        r_proto = cp_item.add_run(subline[5:].strip())
                        r_proto.font.name = 'Georgia'
                        r_proto.font.bold = True
                        r_proto.font.size = Pt(10)
                        r_proto.font.color.rgb = RGBColor(0x22, 0x33, 0x55)
                    else:
                        add_formatted_runs(cp_item, subline, base_font='Georgia', base_size=Pt(9.5), base_color=RGBColor(0x2B, 0x2B, 0x2B))
                    i += 1
                continue

            elif line.startswith('---'):
                i += 1
                continue

            # Standard Paragraphs
            else:
                p = doc.add_paragraph()
                p.paragraph_format.line_spacing = 1.35
                p.paragraph_format.space_after = Pt(6)
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                add_formatted_runs(p, line, base_font='Georgia', base_size=Pt(10.5), base_color=RGBColor(0x22, 0x22, 0x22))

            i += 1

        if idx < len(files) - 1:
            doc.add_page_break()

    # Save to primary and expanded Word documents
    docx_file = os.path.join(os.path.dirname(__file__), '..', 'The_Weight_of_Nodding_Expanded_Edition.docx')
    doc.save(docx_file)
    print(f"Word Document saved successfully: {docx_file} ({os.path.getsize(docx_file):,} bytes)")

    # Attempt PDF conversion via Word COM
    pdf_file = os.path.join(os.path.dirname(__file__), '..', 'The_Weight_of_Nodding_Expanded_Edition.pdf')
    try:
        import win32com.client
        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False
        doc_com = word.Documents.Open(os.path.abspath(docx_file))
        # 17 represents wdExportFormatPDF
        doc_com.ExportAsFixedFormat(os.path.abspath(pdf_file), 17)
        doc_com.Close(False)
        word.Quit()
        print(f"Print-Ready PDF generated successfully via Word COM: {pdf_file} ({os.path.getsize(pdf_file):,} bytes)")
    except Exception as e:
        print(f"Word COM conversion notice: {e}")

if __name__ == '__main__':
    create_book_document()
