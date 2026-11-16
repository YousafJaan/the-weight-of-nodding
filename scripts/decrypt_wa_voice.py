import base64
import hashlib
import hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def hkdf_expand(pseudo_random_key, info, length):
    hash_len = 32
    iterations = (length + hash_len - 1) // hash_len
    expanded = b""
    t = b""
    for i in range(1, iterations + 1):
        t = hmac.new(pseudo_random_key, t + info + bytes([i]), hashlib.sha256).digest()
        expanded += t
    return expanded[:length]

def hkdf(salt, ikm, info, length):
    prk = hmac.new(salt, ikm, hashlib.sha256).digest()
    return hkdf_expand(prk, info, length)

def decrypt_whatsapp_media(enc_bytes, media_key_b64, media_type="audio"):
    media_key = base64.b64decode(media_key_b64)
    info_map = {
        "audio": b"WhatsApp Audio Keys",
        "ptt": b"WhatsApp Audio Keys",
        "image": b"WhatsApp Image Keys",
        "video": b"WhatsApp Video Keys",
        "document": b"WhatsApp Document Keys"
    }
    info = info_map.get(media_type, b"WhatsApp Audio Keys")
    salt = b"\x00" * 32
    key_stream = hkdf(salt, media_key, info, 112)
    
    iv = key_stream[:16]
    cipher_key = key_stream[16:48]
    mac_key = key_stream[48:80]
    
    # In WhatsApp, last 10 bytes of enc_bytes is the truncated HMAC-SHA256
    file_bytes = enc_bytes[:-10]
    mac = enc_bytes[-10:]
    
    cipher = Cipher(algorithms.AES(cipher_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(file_bytes) + decryptor.finalize()
    
    # Remove PKCS7 padding
    pad_len = decrypted[-1]
    if pad_len < 16:
        decrypted = decrypted[:-pad_len]
        
    return decrypted

if __name__ == "__main__":
    print("WhatsApp decrypt helper loaded successfully.")
