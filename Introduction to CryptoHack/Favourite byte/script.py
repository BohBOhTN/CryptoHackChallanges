from pwn import xor

# The hex-encoded ciphertext
hex_data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# Convert from hex to bytes
cipher_bytes = bytes.fromhex(hex_data)

# Try all 256 possible single-byte keys
for key in range(256):
    decoded = xor(cipher_bytes, key)
    if b"crypto{" in decoded:
        print(f"Key: {key}")
        print(f"Flag: {decoded.decode()}")
        break
