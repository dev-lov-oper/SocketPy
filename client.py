import socket

HOST = "127.0.0.1"
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")

    msg = s.recv(1024)
    print("Message:", msg.decode("utf-8"))

except ConnectionRefusedError:
    print("Server is not running.")

finally:
    s.close()