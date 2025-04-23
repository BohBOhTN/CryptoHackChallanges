from pwn import xor

cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher_bytes = bytes.fromhex(cipher_hex)

# Known plaintext: the flag format starts with 'crypto{'
known_plaintext = b'crypto{'

# Get the first part of the key by XOR'ing known plaintext with the ciphertext
key_part = xor(cipher_bytes[:len(known_plaintext)], known_plaintext)

# The recovered key part is b"myXORke". The full key seems to be b"myXORkey"
full_key = key_part + b"y"

# Repeat the full key to cover the entire ciphertext length
repeating_key = (full_key * (len(cipher_bytes) // len(full_key) + 1))[:len(cipher_bytes)]

# XOR full ciphertext with the repeating key to recover the flag
flag = xor(cipher_bytes, repeating_key)
print(flag.decode())