import sys
import os
print("Importing faster_whisper...", flush=True)
from faster_whisper import WhisperModel
print("Loaded faster_whisper. Initializing model tiny...", flush=True)
model = WhisperModel("tiny", device="cpu", compute_type="int8")
print("Model initialized. Testing 31s file...", flush=True)

fpath = os.path.join("audio_notes", "anam_vn2_31s.ogg")
segments, info = model.transcribe(fpath, beam_size=1)
print(f"Detected language: {info.language}", flush=True)
for s in segments:
    print(f"[{s.start:.1f}s -> {s.end:.1f}s]: {s.text}", flush=True)
print("Test completed successfully!", flush=True)
