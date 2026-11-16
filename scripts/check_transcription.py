import os
import json

# Check if audio_notes/transcriptions.json exists yet
if os.path.exists("audio_notes/transcriptions.json"):
    print("Found transcriptions.json:")
    with open("audio_notes/transcriptions.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for k, v in data.items():
            print(f"\n=== {k} ({v.get('language')}) ===")
            print(v.get('full_text'))
else:
    print("transcriptions.json not ready yet.")
