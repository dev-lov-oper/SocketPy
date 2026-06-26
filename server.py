import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TCP connection
HOST = "127.0.0.1"
PORT=8000

s.bind((HOST, PORT))

s.listen(4) #number of clients that can connect to the server
print(f"Server listening on {HOST}:{PORT}")

while True:
    client,addr=s.accept()
    print("client is connected and has address: ", addr)
    client.send(bytes("Welcome to the server!", "utf-8"))
    client.close()

