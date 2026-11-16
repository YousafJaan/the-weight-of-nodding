import speech_recognition as sr
import subprocess
import os

r = sr.Recognizer()

def transcribe_file(wav_path, out_file):
    print(f"\n==========================================", flush=True)
    print(f"Processing {wav_path}...", flush=True)
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", wav_path]
    dur = float(subprocess.check_output(cmd).decode().strip())
    print(f"Duration: {dur:.1f}s", flush=True)
    
    chunk_len = 10
    full_transcript = []
    
    with sr.AudioFile(wav_path) as source:
        offset = 0
        while offset < dur:
            chunk_duration = min(chunk_len, dur - offset)
            audio_chunk = r.record(source, duration=chunk_duration)
            chunk_text = ""
            for lang in ["ur-PK", "hi-IN", "en-US"]:
                try:
                    text = r.recognize_google(audio_chunk, language=lang)
                    chunk_text = text
                    break
                except sr.UnknownValueError:
                    continue
                except Exception as e:
                    pass
            seg_str = f"[{offset:.0f}s - {offset+chunk_duration:.0f}s]: {chunk_text}"
            print(seg_str, flush=True)
            out_file.write(seg_str + "\n")
            out_file.flush()
            if chunk_text:
                full_transcript.append(chunk_text)
            offset += chunk_duration
            
    total_text = " ".join(full_transcript)
    out_file.write(f"\nFULL TEXT:\n{total_text}\n\n")
    out_file.flush()
    return total_text

# Convert ogg to wav if not done
for ogg_name, wav_name in [("anam_vn3_96s_1m36s.ogg", "anam_vn3.wav"), ("anam_vn1_349s_5m49s.ogg", "anam_vn1.wav")]:
    ogg_p = os.path.join("audio_notes", ogg_name)
    wav_p = os.path.join("audio_notes", wav_name)
    if not os.path.exists(wav_p):
        subprocess.run(["ffmpeg", "-y", "-i", ogg_p, "-ar", "16000", "-ac", "1", wav_p], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

with open("audio_notes/transcripts_all.txt", "w", encoding="utf-8") as out_f:
    out_f.write("=== VN3 (96s / 1m36s) ===\n")
    transcribe_file(os.path.join("audio_notes", "anam_vn3.wav"), out_f)
    
    out_f.write("=== VN1 (349s / 5m49s) ===\n")
    transcribe_file(os.path.join("audio_notes", "anam_vn1.wav"), out_f)

print("\nALL TRANSCRIPTIONS COMPLETED SUCCESSFULLY!", flush=True)
