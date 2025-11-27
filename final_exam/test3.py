from base64 import b64encode # 1
def simple_cipher(text:str, key="xor") -> str: # 2
    if key == "xor":
        return ''.join(chr(ord(c) ^ 42) for c in text).encode().hex() # 3
    elif key == "caesar": # 4
        return ''.join(chr((ord(c) - 97 + 3) % 26 + 97 ) if c.isalpha() else c for c in text)
    else: # 5
        return b64encode(text.encode()).decode()

