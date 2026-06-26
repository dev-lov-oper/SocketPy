# Networking Basics

This document provides a concise introduction to computer networking and the concepts required to understand socket programming.

---

# What is Computer Networking?

Computer networking is the practice of connecting two or more devices so they can exchange data and share resources such as files, applications, and internet access.

Examples include:

* Browsing websites
* Sending emails
* Video conferencing
* Online gaming
* Cloud computing

---

# Types of Networks

| Type | Description                                |
| ---- | ------------------------------------------ |
| PAN  | Personal Area Network (Bluetooth, USB)     |
| LAN  | Local Area Network (Home, Office, College) |
| MAN  | Metropolitan Area Network (City-wide)      |
| WAN  | Wide Area Network (Internet)               |

---

# What is a Socket?

A socket is one endpoint of a two-way communication channel between two devices on a network.

A socket is identified by:

* IP Address
* Port Number

Example:

```text
192.168.1.10 : 8080
```

---

# IP Address

An IP (Internet Protocol) address uniquely identifies a device connected to a network.

Example IPv4 Address:

```text
192.168.1.15
```

Two common versions are:

* IPv4 (32-bit)
* IPv6 (128-bit)

---

# Port Number

A port identifies a specific service running on a computer.

Examples:

| Port  | Service |
| ----- | ------- |
| 20/21 | FTP     |
| 22    | SSH     |
| 25    | SMTP    |
| 53    | DNS     |
| 80    | HTTP    |
| 443   | HTTPS   |

---

# Client-Server Architecture

A client requests a service.

A server provides that service.

```
Client  ─────────────►  Server
       Request

Client  ◄─────────────  Server
       Response
```

Examples:

* Browser → Web Server
* Mobile App → Backend Server
* Chat Client → Chat Server

---

# TCP vs UDP

| Feature         | TCP                            | UDP                          |
| --------------- | ------------------------------ | ---------------------------- |
| Connection      | Connection-oriented            | Connectionless               |
| Reliability     | Reliable                       | Unreliable                   |
| Speed           | Slower                         | Faster                       |
| Error Checking  | Yes                            | Basic                        |
| Packet Ordering | Guaranteed                     | Not Guaranteed               |
| Typical Uses    | Websites, Email, File Transfer | Gaming, Live Streaming, VoIP |

---

# TCP Communication Process

1. Create Socket
2. Connect to Server
3. Send Request
4. Receive Response
5. Close Connection

---

# UDP Communication Process

1. Create Socket
2. Send Datagram
3. Receive Datagram
4. Close Socket

No connection is established before communication.

---

# Python Socket Module

Python includes the built-in `socket` module for network programming.

Important functions:

```python
socket.socket()
bind()
listen()
accept()
connect()
send()
recv()
sendto()
recvfrom()
close()
```

---

# Common Socket Types

```python
socket.AF_INET      # IPv4
socket.AF_INET6     # IPv6

socket.SOCK_STREAM  # TCP
socket.SOCK_DGRAM   # UDP
```

---

# Data Flow in TCP

```
Client
   │
Create Socket
   │
Connect
   │
Send Data
   │
──────────────►
               Server
            Accept Connection
                 │
             Receive Data
                 │
             Process Request
                 │
Send Response ◄──────────────
                 │
          Close Connection
```

---



# Best Practices

* Always close sockets after use.
* Handle exceptions to prevent crashes.
* Validate user input before processing.
* Use timeouts to avoid hanging connections.
* Prefer TCP when reliability matters.
* Prefer UDP when speed is more important than guaranteed delivery.

---

# Additional Learning Resources

### Documentation

* Python Socket Module
  https://docs.python.org/3/library/socket.html

* Python Socket HOWTO
  https://docs.python.org/3/howto/sockets.html

---





