import socket
import json

HOST = "127.0.0.1"
PORT = 5001

packet = {
    "source": "Sender_a",
    "destination": "Receiver_c",
    "payload": "Hello from Sender_a"
}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

client.send(json.dumps(packet).encode())

print("Packet sent to Sender_a")

client.close()