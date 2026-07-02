import socket
import json
import threading

HOST = "127.0.0.1"

# Router listens on these ports so both Senders can use the same router process.
SENDER_PORTS = [5001, 5002]

# Map destination name -> receiver TCP port
DEST_TO_PORT = {
    "Receiver_a": 6001,
    "Receiver_b": 6002,
    "Receiver_c": 60045,
}


def forward_to_receiver(packet_bytes: bytes, destination: str) -> None:
    destination_port = DEST_TO_PORT.get(destination)
    if destination_port is None:
        print(f"[router] Unknown destination: {destination!r}. Dropping packet.")
        return

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, destination_port))
    client.send(packet_bytes)
    client.close()

    print(f"[router] Forwarded to {destination} (port {destination_port})")


def handle_client(conn: socket.socket, addr) -> None:
    try:
        packet_bytes = conn.recv(4096)
        if not packet_bytes:
            return

        # Log what router received
        print(f"\n[router] Packet received from {addr}:")

        # Because senders use json.dumps(packet).encode(), decode/parse as JSON.
        try:
            packet_str = packet_bytes.decode()
            print(packet_str)
            packet = json.loads(packet_str)
            destination = packet.get("destination")
        except Exception:
            # If it's not JSON for some reason, drop
            print("[router] Failed to decode/parse JSON. Dropping packet.")
            return

        if destination is None:
            print("[router] 'destination' missing in packet. Dropping packet.")
            return

        forward_to_receiver(packet_bytes, destination)
    finally:
        conn.close()


def start_listener(port: int) -> None:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, port))
    server.listen(5)

    print(f"[router] Listening on port {port}...")

    while True:
        conn, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        t.start()


if __name__ == "__main__":
    # Run two listeners (5001 and 5002) so Sender_a and Sender_b can both connect to router.py.
    threads = []
    for p in SENDER_PORTS:
        t = threading.Thread(target=start_listener, args=(p,), daemon=True)
        t.start()
        threads.append(t)

    # Keep main thread alive.
    for t in threads:
        t.join()
