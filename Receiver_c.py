import socket

HOST = "127.0.0.1"
PORT = 60045

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Receiver_c is waiting...")

conn, addr = server.accept()

data = conn.recv(1024).decode()

print("\nPacket received at Receiver_c")
print(data)

conn.close()
server.close()