import urllib.request
import os
import sys

from decrypt_wa_voice import decrypt_whatsapp_media

vn2_url = "https://mmg.whatsapp.net/v/t62.7117-24/911527347_3042274986141674_4523052296500345067_n.enc?ccb=11-4&oh=01_Q5Aa6AFDWkc-UkMWLyK02lo9CPBzvlqJrSz5sQV0ei3BUfXEnw&oe=6B222B49&_nc_sid=5e03e0&mms3=true"
vn2_key = "QUYRvgJPvsl94WZZ8i8UdSYrItw9QOBbtpA8gUpQzCQ="

print(f"Downloading from MMG...")
req = urllib.request.Request(vn2_url, headers={'User-Agent': 'WhatsApp/2.24.23.78 i'})
try:
    with urllib.request.urlopen(req) as resp:
        enc_data = resp.read()
    print(f"Downloaded {len(enc_data)} bytes. Decrypting...")
    decrypted = decrypt_whatsapp_media(enc_data, vn2_key, "ptt")
    print(f"Decrypted {len(decrypted)} bytes. Magic: {decrypted[:8]}")
    
    os.makedirs("audio_notes", exist_ok=True)
    out_path = os.path.join("audio_notes", "anam_vn2_31s.ogg")
    with open(out_path, "wb") as f:
        f.write(decrypted)
    print(f"Successfully saved to {out_path}!")
except Exception as e:
    print(f"Error: {e}")
