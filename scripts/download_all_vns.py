import urllib.request
import os
import sys

from decrypt_wa_voice import decrypt_whatsapp_media

voice_notes = [
    {
        "name": "anam_vn1_349s_5m49s.ogg",
        "duration": 349,
        "url": "https://mmg.whatsapp.net/v/t62.7117-24/910288667_2329458151176270_4953939201102091525_n.enc?ccb=11-4&oh=01_Q5Aa6AEXw6IN-qv5lY3EwUgZ2ysnRuojEx9jAe0VhiJB2_UqaA&oe=6B22213C&_nc_sid=5e03e0&mms3=true",
        "key": "jaO/oriRCY0w+EyccygB0D8OGclazJzux9P02AkHSh8="
    },
    {
        "name": "anam_vn2_31s.ogg",
        "duration": 31,
        "url": "https://mmg.whatsapp.net/v/t62.7117-24/911527347_3042274986141674_4523052296500345067_n.enc?ccb=11-4&oh=01_Q5Aa6AFDWkc-UkMWLyK02lo9CPBzvlqJrSz5sQV0ei3BUfXEnw&oe=6B222B49&_nc_sid=5e03e0&mms3=true",
        "key": "QUYRvgJPvsl94WZZ8i8UdSYrItw9QOBbtpA8gUpQzCQ="
    },
    {
        "name": "anam_vn3_96s_1m36s.ogg",
        "duration": 96,
        "url": "https://mmg.whatsapp.net/v/t62.7117-24/906332096_29445418271809452_7317090805210505022_n.enc?ccb=11-4&oh=01_Q5Aa6AFmmf8QoqMaQwakU_pVvPTznGvFHajLXbN_qE5Ck_DRvQ&oe=6B2244F6&_nc_sid=5e03e0&mms3=true",
        "key": "FXU/b8vzIqMnkCwKwJy2rLbhLGr8+EVmEWHMK9fmT80="
    }
]

os.makedirs("audio_notes", exist_ok=True)

for vn in voice_notes:
    out_path = os.path.join("audio_notes", vn["name"])
    print(f"Downloading {vn['name']} ({vn['duration']}s)...")
    req = urllib.request.Request(vn["url"], headers={'User-Agent': 'WhatsApp/2.24.23.78 i'})
    try:
        with urllib.request.urlopen(req) as resp:
            enc_data = resp.read()
        print(f"  Downloaded {len(enc_data)} bytes. Decrypting...")
        decrypted = decrypt_whatsapp_media(enc_data, vn["key"], "ptt")
        print(f"  Decrypted {len(decrypted)} bytes. Magic: {decrypted[:8]}")
        with open(out_path, "wb") as f:
            f.write(decrypted)
        print(f"  Saved to {out_path}!")
    except Exception as e:
        print(f"  Error for {vn['name']}: {e}")
