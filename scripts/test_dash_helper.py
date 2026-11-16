import os
import re

def assert_no_dashes(text, filename):
    for dash in ["—", "–"]:
        if dash in text:
            raise ValueError(f"Found forbidden dash '{dash}' in {filename}!")
    if re.search(r'--+', text):
        raise ValueError(f"Found forbidden double-dash in {filename}!")

print("Validation helper ready.")
