from pwn import * # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote('socket.cryptohack.org', 13377, level='debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decode_data(data_type, encoded):
    if data_type == "base64":
        return base64.b64decode(encoded).decode()
    elif data_type == "hex":
        return bytes.fromhex(encoded).decode()
    elif data_type == "rot13":
        return codecs.decode(encoded, 'rot_13')
    elif data_type == "bigint":
        return long_to_bytes(int(encoded, 16)).decode()
    elif data_type == "utf-8":
        return ''.join(chr(b) for b in encoded)
    else:
        raise ValueError(f"Unknown encoding type: {data_type}")

for _ in range(100):
    received = json_recv()

    print("Received type: ", received["type"])
    print("Received encoded value: ", received["encoded"])

    decoded = decode_data(received["type"], received["encoded"])

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

final_response = json_recv()
print("Final response: ", final_response)
