import socket
from tkinter import *

# Send a message to the client
def send(listbox, entry):
    message = entry.get()
    listbox.insert(END, "Server: " + message)
    entry.delete(0, END)
    client.send(message.encode("utf-8"))

# Receive a message from the client
def receive(listbox):
    message = client.recv(1024).decode("utf-8")
    listbox.insert(END, "Client: " + message)

# Create the main window
root = Tk()
root.title("Server")

# Text entry for typing messages
entry = Entry(root)
entry.pack(side=BOTTOM)

# Listbox to display chat messages
listbox = Listbox(root)
listbox.pack()

# Button to send a message
Button(root, text="Send", command=lambda: send(listbox, entry)).pack(side=BOTTOM)

# Button to receive a message
Button(root, text="Receive", command=lambda: receive(listbox)).pack(side=BOTTOM)

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = "127.0.0.1"
PORT = 12344

# Bind the socket to the address
s.bind((HOST_NAME, PORT))

# Start listening for client connections
s.listen(1)

# Accept a client connection
print("Waiting for client...")
client, address = s.accept()
print("Connected:", address)

# Start the GUI event loop
root.mainloop()