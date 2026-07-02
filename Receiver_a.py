import socket

HOST = "127.0.0.1"
PORT = 6001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Receiver_a is waiting...")

conn, addr = server.accept()

data = conn.recv(1024).decode()

print("\nPacket received at Receiver_a")
print(data)

conn.close()
server.close()