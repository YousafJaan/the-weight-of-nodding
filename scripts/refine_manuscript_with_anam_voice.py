# -*- coding: utf-8 -*-
import os
import re

def clean_dashes(text):
    text = text.replace("—", ", ")
    text = text.replace("–", ", ")
    while "--" in text:
        text = text.replace("--", ", ")
    return text

def assert_no_dashes(text, filename):
    for dash in ["—", "–"]:
        if dash in text:
            raise ValueError(f"Found forbidden dash '{dash}' in {filename}!")
    if "--" in text:
        raise ValueError(f"Found forbidden double-dash in {filename}!")

# Let's inspect each chapter file in manuscript/
print("Starting manuscript enrichment from Anam Sajjad's authentic voice notes...")
