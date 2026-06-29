import socket
from tkinter import *

# Send a message to the server
def send(listbox, entry):
    message = entry.get()
    listbox.insert(END, "Client: " + message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))

# Receive a message from the server
def receive(listbox):
    message = s.recv(1024)
    listbox.insert(END, "Server: " + message.decode("utf-8"))

# Create the main window
root = Tk()

# Text entry for typing messages
entry = Entry()
entry.pack(side=BOTTOM)

# Listbox to display chat messages
listbox = Listbox(root)
listbox.pack()

# Button to send a message
button = Button(root, text="Send", command=lambda: send(listbox, entry))
button.pack(side=BOTTOM)

# Button to receive a message
rbutton = Button(root, text="Receive", command=lambda: receive(listbox))
rbutton.pack(side=BOTTOM)

root.title("Client")

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = "127.0.0.1"
PORT = 12344

# Connect to the server
print("Connecting...")
s.connect((HOST_NAME, PORT))
print("Connected!")

# Start the GUI event loop
root.mainloop()