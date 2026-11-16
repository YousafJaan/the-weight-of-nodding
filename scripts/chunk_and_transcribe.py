import speech_recognition as sr
import subprocess
import os

r = sr.Recognizer()

def transcribe_file(wav_path):
    print(f"\nProcessing {wav_path}...", flush=True)
    # Get duration using ffprobe
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", wav_path]
    dur = float(subprocess.check_output(cmd).decode().strip())
    print(f"Duration: {dur:.1f}s", flush=True)
    
    # Process in 10-second chunks
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
            print(f"  [{offset:.0f}s - {offset+chunk_duration:.0f}s]: {chunk_text}", flush=True)
            if chunk_text:
                full_transcript.append(chunk_text)
            offset += chunk_duration
            
    return " ".join(full_transcript)

# Let's test on anam_vn2 (31 seconds)
vn2_wav = os.path.join("audio_notes", "anam_vn2.wav")
res2 = transcribe_file(vn2_wav)
print("\n=== FULL TRANSCRIPT VN2 ===")
print(res2)
