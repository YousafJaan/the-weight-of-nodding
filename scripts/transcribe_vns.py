import os
import sys
from faster_whisper import WhisperModel

print("Loading Whisper model...")
# Using tiny or base model with CPU / int8 for fast execution
try:
    model = WhisperModel("base", device="cpu", compute_type="int8")
except Exception as e:
    print(f"Error loading base, trying tiny: {e}")
    model = WhisperModel("tiny", device="cpu", compute_type="int8")

audio_dir = "audio_notes"
files = [
    "anam_vn2_31s.ogg",
    "anam_vn3_96s_1m36s.ogg",
    "anam_vn1_349s_5m49s.ogg"
]

transcripts = {}

for fname in files:
    fpath = os.path.join(audio_dir, fname)
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        continue
    print(f"\n--- Transcribing {fname} ---")
    segments, info = model.transcribe(fpath, beam_size=5, language=None)
    print(f"Detected language: {info.language} with probability {info.language_probability:.2f}")
    
    text_segments = []
    for s in segments:
        seg_str = f"[{s.start:.1f}s -> {s.end:.1f}s]: {s.text}"
        print(seg_str)
        text_segments.append(seg_str)
        
    transcripts[fname] = {
        "language": info.language,
        "segments": text_segments,
        "full_text": " ".join([s.split("]: ", 1)[-1] for s in text_segments])
    }

import json
with open("audio_notes/transcriptions.json", "w", encoding="utf-8") as f:
    json.dump(transcripts, f, ensure_ascii=False, indent=2)

print("\nTranscription complete! Saved to audio_notes/transcriptions.json")
