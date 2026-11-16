# -*- coding: utf-8 -*-
"""
deepen_batch_1.py
Expands Chapters 00 to 04 of 'The Weight of Nodding' to ~3,200 - 3,500 words each.
Maintains plain writing: zero em dashes, zero en dashes.
Rich sensory detail, deep psychology, authentic Multan atmosphere.
"""
import os
import re

def clean_dashes(text):
    text = text.replace('\u2014', ', ')
    text = text.replace('\u2013', ', ')
    text = re.sub(r' +', ' ', text)
    return text

# We will read each chapter, expand its sections with rich scenes and dialogues, and write back.
