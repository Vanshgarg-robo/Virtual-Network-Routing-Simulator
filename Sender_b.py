import socket
import json

HOST = "127.0.0.1"
# Send both Sender_a and Sender_b into the same router process (port 5001)
PORT = 5002

packet = {
    "source": "Sender_b",
    "destination": "Receiver_b",
    "payload": "Hello from Sender_b",
}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.send(json.dumps(packet).encode())

print("Packet sent to router for Sender_b")

client.close()

