import socket

HOST = "127.0.0.1"
PORT = 6002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Receiver_b is waiting...")

conn, addr = server.accept()

data = conn.recv(1024).decode()

print("\nPacket received at Receiver_b")
print(data)

conn.close()
server.close()