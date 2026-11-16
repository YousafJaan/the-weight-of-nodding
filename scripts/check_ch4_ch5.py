# -*- coding: utf-8 -*-
import os
import re

def clean_dashes(text):
    text = text.replace("—", ", ").replace("–", ", ")
    while "--" in text:
        text = text.replace("--", ", ")
    return text

def assert_no_dashes(text, filename):
    for dash in ["—", "–"]:
        if dash in text:
            raise ValueError(f"Found forbidden dash '{dash}' in {filename}!")
    if "--" in text:
        raise ValueError(f"Found forbidden double-dash in {filename}!")

# Let's inspect Chapter 4 and Chapter 5 in manuscript/
print("Reading Chapter 4 and Chapter 5...")
with open("manuscript/04_chapter_4.md", "r", encoding="utf-8") as f:
    ch4_text = f.read()
with open("manuscript/05_chapter_5.md", "r", encoding="utf-8") as f:
    ch5_text = f.read()

print(f"Chapter 4 current words: {len(ch4_text.split())}")
print(f"Chapter 5 current words: {len(ch5_text.split())}")
