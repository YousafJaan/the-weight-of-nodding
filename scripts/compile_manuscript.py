# -*- coding: utf-8 -*-
"""
compile_manuscript.py
Compiles all 18 chapters into FULL_MANUSCRIPT.md with complete front and back matter.
Zero em-dashes or en-dashes. Plain writing.
"""
import os
import glob
import re

manuscript_dir = os.path.join(os.path.dirname(__file__), '..', 'manuscript')

front_matter = """# THE WEIGHT OF NODDING
### A Political Scientist's Two-Year Chronicle of Hostel Life, Institutional Silence, and the Cost of Agreement

**By Anam Sajjad**  
*Department of Political Science, Bahauddin Zakariya University (BZU), Multan, Pakistan*  
*Lead Author & Empirical Researcher: Pakistan Is Not Poor, It Is Poorly Managed (CERN Zenodo DOI: 10.5281/zenodo.24054373)*  
*ORCID: 0009-0004-6169-1703 | Email: anoom994@gmail.com*

---

### Copyright & Publication Notice
**The Weight of Nodding: A Political Scientist's Two-Year Chronicle of Hostel Life, Institutional Silence, and the Cost of Agreement**  
Copyright (c) 2024-2026 by Anam Sajjad. All rights reserved.  
Definitive Expanded Edition: November 2026. Published in Multan and Islamabad, Pakistan.  
Academic Affiliation: Department of Political Science, Bahauddin Zakariya University, Bosan Road, Multan 60800, Punjab, Pakistan.  
Author Correspondence: `anoom994@gmail.com` | ORCID: `0009-0004-6169-1703`  
Co-Authored Empirical Research:  
Sajjad, A., & Yousaf. (2024). *Pakistan Is Not Poor, It Is Poorly Managed: An Empirical Investigation of Energy, Water, and Demographics in Pakistan*. CERN Zenodo. DOI: `10.5281/zenodo.24054373`.

All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the author, except in the case of brief quotations embodied in critical reviews, scholarly dissertations, and certain other noncommercial uses permitted by copyright law.

---

### Dedication
*To the young women of Southern Punjab,*  
*who drag heavy green tin trunks across the burning gravel of Bosan Road;*  

*To my seven sisters of Room 42: Aqsa, Anza, Saba, Momina, Sidra, Iqra, and Palwasha,*  
*who proved that when women stand together in the dark, no iron gate can hold them;*  

*To Yousaf and the team at Quick Services and Workx,*  
*who taught me that verified arithmetic is the ultimate weapon against institutional decay;*  

*And to my father,*  
*who worked thirty-four years with ink-stained hands in government offices so his daughter could enter the doors of higher education:*  

*This book is your mirror.*  
*Keep your head high. We will never nod again.*

---

### Author's Note & Preface: Why This Book Exists
I began writing this book on a freezing night in February 2024, sitting on an iron cot in Room 42 of Amna Hall at Bahauddin Zakariya University in Multan.

My hands were shaking from the lingering effects of an undiagnosed neurological breakdown: a physical collapse that forced me to take a one-year academic drop and spend months lying on rusted iron beds in Nishtar Hospital, listening to patriarchal doctors dismiss two years of systemic institutional exhaustion as female hysteria.

For two years, like thousands of young women across Pakistan, I had practiced the exhausting, soul-crushing art of reflexive agreement. I had nodded to corrupt hostel wardens who stole our food and maintenance budgets. I had nodded to arrogant professors who threatened our degrees if we questioned outdated dogmas. I had nodded to family elders who believed that a girl's only virtue is her silence.

I nodded until my body revolted.

The human body is not built to carry the burden of continuous lying. When your mouth is forbidden to speak the truth, your nervous system mounts a violent biological strike.

This book is the record of what happened when the nodding stopped.

It chronicles two years inside Amna Hall, our battles over sulfur bore water, food cartels, curfew registers, and campus tear gas. It documents how seven girls in a twelve-by-fourteen room formed an unbreakable garrison of mutual defense, how we rescued our sister Sidra from a forced marriage using an artist case and a Metro bus ticket, and how we rejected the commercial 5,000-rupee plagiarized thesis mills to produce an internationally indexed empirical study on sovereign circular debt.

As of 2026, I remain a student at Bahauddin Zakariya University. But I no longer walk Bosan Road with lowered eyes.

Every chapter of this volume concludes with **The Strategist's Margin: Tactical Protocols for Daring Women**: the operational rules of power, institutional game theory, legal self-defense, and psychological boundary enforcement that every young woman needs to survive and dominate behind institutional enemy lines.

Do not let them buy your peace with your own silence.

*Anam Sajjad*  
*Multan, February 2026*

---

### Table of Contents
- **Prologue: The Cost of the Reflex** (Seminar Room 4 and the Muscle in the Neck)
- **Chapter 1: The February Midnight (Room 42)** (The Immersion Rod and the First Page)
- **Chapter 2: The Red Line on Bosan Road** (The Elevated Metro Bus and the Father's Manual)
- **Chapter 3: Behind the Green Iron Gates** (Amna Hall, Razor Wire, and Maasi Sakina)
- **Chapter 4: The Currency of Sifarish (Allotment)** (Room 42 over the Open Sewer)
- **Chapter 5: The Circle of Seven (Room 42 Secrets)** (Aqsa, Anza, Saba, Momina, Sidra, Iqra, Palwasha)
- **Chapter 6: Khara Paani (The Saline Water)** (Sulfur Borewells and Chemical Forensics)
- **Chapter 7: The Mess Token and the Midnight Ration** (Haji Manzoor's Cartel and the Sovereign Kitchen)
- **Chapter 8: The Metro Encounter (Meeting Yousaf)** (The Storm, Workx, and Quick Services)
- **Chapter 9: The Curfew Slip and the Father's Honor** (Sidra's Extraction and the High Court Injunction)
- **Chapter 10: The Photostat Archives (Chacha Asghar's Den)** (The Industry of Manufactured Illiteracy)
- **Chapter 11: The Strike, The Tear Gas, and The Suspended Metro** (The Four-Day Siege)
- **Chapter 12: The 48-Degree Summer & Rooftop Secrets** (Breaking Padlocks and Slicing Mangoes)
- **Chapter 13: The Breakdown (The Unknown Disease & Nishtar Wards)** (When the Body Refuses to Subsidize Silence)
- **Chapter 14: The One-Year Drop (The Forge of Solitude)** (Weaponizing the Unscheduled Sabbatical)
- **Chapter 15: The Thesis Monopoly vs. The Empirical Truth** (Auditing the Sovereign Ledger)
- **Chapter 16: The Breakthrough Paper (Pakistan Is Not Poor, It Is Poorly Managed)** (The CERN Zenodo Defense)
- **Chapter 17: Walking Bosan Road in 2026 (The Unbowed Head)** (The Sovereign Woman's Creed)

---
"""

back_matter = """
---

### Acknowledgments & Research Attribution
This book and the empirical research underpinning it would not have been possible without the courage, brilliance, and solidarity of the following individuals and organizations:

1. **The Sisters of Room 42:** Aqsa, Anza, Saba, Momina, Sidra, Iqra, and Palwasha. You gave me safety when the world was dark. You held my hand when my fingers trembled. You proved that sisterhood in Pakistan is not a sentimental slogan; it is an impenetrable fortress.
2. **Yousaf & Quick Services / Workx:** To Yousaf, co-researcher, operational architect, and founder of Workx and Quick Services. Thank you for holding my work to the highest standards of data engineering, for opening your enterprise databases, for auditing every regression model, and for being the first peer who refused to let me nod. Quick Services stands as an example of what ethical, high-integrity enterprise problem-solving can accomplish in a broken economy.
3. **Dr. Nabila (Department of Chemistry, BZU):** For providing the objective spectrophotometric analysis of Multan's groundwater that gave us the empirical proof of environmental contamination.
4. **Miss Rubina Malik, Advocate High Court:** For deploying the power of constitutional law to protect our sister Sidra from patriarchal abduction.
5. **My Father, Sajjad Sahib:** For thirty-four years of quiet, honest labor, and for having the courage to stand beside his daughter when she refused to bow.

---

### About the Author
**Anam Sajjad** is a political scientist, empirical researcher, and author based in Multan, Pakistan. She is a research scholar in the Department of Political Science at Bahauddin Zakariya University (BZU), specializing in public sector governance, circular debt, and sovereign institutional extraction.

She is the lead author and principal investigator of the landmark empirical monograph:  
*Pakistan Is Not Poor, It Is Poorly Managed: An Empirical Investigation of Energy, Water, and Demographics in Pakistan*, permanently archived in the international open-science repository at CERN in Switzerland under Digital Object Identifier: `10.5281/zenodo.24054373`.

She lives in Multan, where she mentors young female scholars and coordinates independent research networks across Southern Punjab.

Correspondence: `anoom994@gmail.com` | ORCID: `0009-0004-6169-1703`
"""

def clean(text):
    text = text.replace('\u2014', ', ')
    text = text.replace('\u2013', ', ')
    text = re.sub(r' +', ' ', text)
    return text

chapter_files = sorted([f for f in glob.glob(os.path.join(manuscript_dir, '*.md')) if not f.endswith('FULL_MANUSCRIPT.md')])

compiled_parts = [front_matter.strip()]

for cf in chapter_files:
    with open(cf, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    compiled_parts.append("\n\n---\n\n" + content)

compiled_parts.append(back_matter.strip())

full_text = clean("\n\n".join(compiled_parts))

out_path = os.path.join(manuscript_dir, 'FULL_MANUSCRIPT.md')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(full_text)

words = len(full_text.split())
dashes = full_text.count('\u2014') + full_text.count('\u2013')
print(f"Compiled FULL_MANUSCRIPT.md: {words:,} words, {len(full_text):,} characters, {dashes} dashes.")
