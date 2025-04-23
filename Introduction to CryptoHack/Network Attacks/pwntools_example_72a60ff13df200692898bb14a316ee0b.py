#!/usr/bin/env python3

from pwn import *  # pip install pwntools
import json

HOST = "socket.cryptohack.org"
PORT = 11112

# Function to send JSON data
def json_send(data):
    request = json.dumps(data).encode()
    connection.sendline(request)

# Function to receive JSON data
def json_recv():
    while True:  # Keep trying until a valid JSON response is received
        response = connection.recvline().decode()
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            print(f"Skipping non-JSON response: {response}")

# Establish connection
connection = remote(HOST, PORT)

# Send the request
request = {
    "buy": "flag"
}
json_send(request)

# Receive and print the response
response = json_recv()
if response:
    print(response)
else:
    print("No valid response received.")

# Close the connection
connection.close()