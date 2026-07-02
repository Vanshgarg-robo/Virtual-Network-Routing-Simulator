# Packet Forwarding Simulator using Python

A Python-based networking project that demonstrates **virtual communication between multiple nodes** using **TCP socket programming**. The project simulates how a router receives packets from sender nodes and forwards them to the appropriate receiver based on the packet destination.

---

## 📌 Project Overview

This project simulates a small computer network consisting of multiple senders, a router, and multiple receivers.

The router acts as an intermediate node that receives packets, examines their destination, and forwards them to the correct receiver.

The project demonstrates the basic concepts of:

- Virtual Node Communication
- Packet Forwarding
- TCP Socket Programming
- JSON Packet Structure
- Router-Based Communication

---

## 🏗️ Network Architecture

```
        Sender A               Sender B
            |                     |
            |                     |
        Port 5001             Port 5002
            |                     |
            |                     |
            |    +---------+      |
            |----| Router  |------|
                 +---------+
                 /    |    \
                /     |     \
               /      |      \
      Receiver A Receiver B Receiver C
        Port6001  Port6002   Port60045

```

---

## 📂 Project Structure

```
Packet-Forwarding-Simulator/

│── Sender_a.py
│── Sender_b.py
│── router.py
│── Receiver_a.py
│── Receiver_b.py
│── Receiver_c.py
│── README.md
```

---

## 🚀 Features

- Virtual communication between network nodes
- Multiple sender nodes
- Multiple receiver nodes
- Router-based packet forwarding
- JSON packet format
- TCP socket communication
- Multi-threaded router for handling multiple connections

---

## 🛠️ Technologies Used

- Python 3
- Socket Programming
- TCP/IP
- JSON
- Multi-threading

---

## 📦 Packet Format

Packets are transmitted in JSON format.

Example:

```json
{
    "source": "Sender_a",
    "destination": "Receiver_c",
    "payload": "Hello from Sender_a"
}
```

---

## ▶️ How to Run

### Step 1

Start all receivers.

```bash
python Receiver_a.py
```

```bash
python Receiver_b.py
```

```bash
python Receiver_c.py
```

---

### Step 2

Start the router.

```bash
python router.py
```

---

### Step 3

Run any sender.

```bash
python Sender_a.py
```

or

```bash
python Sender_b.py
```

---

## 📸 Sample Output

### Sender

```
Packet sent to router
```

### Router

```
Packet received

Source : Sender_a

Destination : Receiver_c

Payload : Hello from Sender_a

Forwarding packet...

Packet forwarded successfully.
```

### Receiver

```
Packet received

Source : Sender_a

Destination : Receiver_c

Payload : Hello from Sender_a
```

---

## 📖 Concepts Covered

- Computer Networks
- Virtual Communication
- TCP Socket Programming
- Packet Forwarding
- Client-Server Architecture
- Multi-threading
- JSON Packet Transmission

---

## 📚 Future Improvements

- Graph-based Network Representation
- Neighbor Discovery
- Dijkstra Shortest Path Algorithm
- Dynamic Routing Table
- Time-To-Live (TTL)
- Packet Acknowledgement
- Network Topology Visualization

---

## 👨‍💻 Author

**Vansh Garg**
