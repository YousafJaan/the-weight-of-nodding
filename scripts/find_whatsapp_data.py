import os
import glob
import subprocess

try:
    import psutil
    procs = []
    for p in psutil.process_iter(['pid', 'name']):
        name = (p.info['name'] or '').lower()
        if any(b in name for b in ['whatsapp', 'chrome', 'edge', 'msedge', 'brave', 'firefox', 'opera']):
            procs.append((p.info['pid'], p.info['name']))
    print("Running Browser / WhatsApp Processes:")
    for pid, name in set(procs):
        print(f"  [{pid}] {name}")
except Exception as e:
    print(f"psutil check failed: {e}")

user_home = os.path.expanduser('~')
print(f"\nUser Home: {user_home}")

search_dirs = [
    os.path.join(user_home, 'Downloads'),
    os.path.join(user_home, 'Desktop'),
    os.path.join(user_home, 'Documents'),
    os.path.join(user_home, 'AppData', 'Local', 'Packages'),
    os.path.join(user_home, 'AppData', 'Local', 'WhatsApp'),
    os.path.join(user_home, 'AppData', 'Roaming', 'WhatsApp'),
]

patterns = ['*.opus', '*.m4a', '*.ogg', '*.mp3', '*.wav', '*whatsapp*', '*anam*', '*sajjad*', '*voice*']

print("\nSearching directories for WhatsApp & audio artifacts...")
for s_dir in search_dirs:
    if not os.path.exists(s_dir):
        continue
    print(f"\nChecking: {s_dir}")
    try:
        for root, dirs, files in os.walk(s_dir):
            # don't traverse too deep in AppData/Local/Packages unless WhatsApp
            if 'Packages' in root and 'WhatsApp' not in root:
                dirs[:] = [d for d in dirs if 'WhatsApp' in d or 'whatsapp' in d.lower()]
                continue
            for f in files:
                f_lower = f.lower()
                if any(f_lower.endswith(ext) for ext in ['.opus', '.m4a', '.ogg', '.mp3', '.wav', '.aac', '.txt']):
                    full_p = os.path.join(root, f)
                    size = os.path.getsize(full_p)
                    print(f"  Found file: {full_p} ({size} bytes)")
    except Exception as err:
        print(f"  Error walking {s_dir}: {err}")
