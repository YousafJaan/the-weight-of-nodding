import os
import re

manuscript_dir = r"C:\Users\Huzaifa Mahi\.gemini\antigravity\worktrees\remote-workspace\write_new_book\manuscript"

# Let's check current word count per chapter
files = sorted([f for f in os.listdir(manuscript_dir) if f.endswith('.md') and not f.startswith('FULL')])

print("Checking chapters to enrich...")
for f in files:
    path = os.path.join(manuscript_dir, f)
    with open(path, 'r', encoding='utf-8') as fl:
        text = fl.read()
    print(f"{f}: {len(text.split())} words")
