import speech_recognition as sr
import subprocess
import os

files = [
    ("anam_vn2_31s.ogg", "anam_vn2.wav"),
    ("anam_vn3_96s_1m36s.ogg", "anam_vn3.wav"),
    ("anam_vn1_349s_5m49s.ogg", "anam_vn1.wav")
]

r = sr.Recognizer()

for ogg_name, wav_name in files:
    ogg_path = os.path.join("audio_notes", ogg_name)
    wav_path = os.path.join("audio_notes", wav_name)
    
    if not os.path.exists(wav_path):
        subprocess.run(["ffmpeg", "-y", "-i", ogg_path, "-ar", "16000", "-ac", "1", wav_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    print(f"\n--- Google Speech Recognition for {ogg_name} ---", flush=True)
    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)
    
    # Try Urdu (ur-PK) first
    for lang in ["ur-PK", "hi-IN", "en-US"]:
        try:
            text = r.recognize_google(audio, language=lang)
            print(f"[{lang}]: {text}", flush=True)
            break
        except sr.UnknownValueError:
            print(f"[{lang}]: could not understand audio", flush=True)
        except Exception as e:
            print(f"[{lang}]: error: {e}", flush=True)
