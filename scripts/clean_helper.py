import os
import re

def clean_dashes(text):
    text = text.replace("—", ", ")
    text = text.replace("–", ", ")
    # clean any leftover double dashes
    text = re.sub(r'--+', ', ', text)
    return text

print("Dash cleaner ready.")
