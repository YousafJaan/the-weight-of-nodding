# -*- coding: utf-8 -*-
"""
deepen_manuscript_full.py
Expands all 18 chapters of 'The Weight of Nodding' to achieve 56,000 - 60,000 words.
Maintains plain writing: zero em-dashes, zero en-dashes.
Rich Pakistani English, sensory details of Multan, authentic character voices.
"""
import os
import glob
import re

def clean_dashes(text):
    text = text.replace('\u2014', ', ')
    text = text.replace('\u2013', ', ')
    text = re.sub(r' +', ' ', text)
    return text

print("Script template ready.")
