import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "127.0.0.1"

PORT=8000
try:
	s.connect((HOST, PORT))
	print(f"Connected to {HOST}:{PORT}")
except ConnectionRefusedError:
	print(f"Could not connect to {HOST}:{PORT}. Start the server first.")
finally:
	s.close()



