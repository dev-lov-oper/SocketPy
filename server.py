import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

HOST = "127.0.0.1"
PORT = 12351

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Server")
root.geometry("500x500")

chat_box = ScrolledText(root, state="disabled", font=("Arial", 12))
chat_box.pack(fill="both", expand=True, padx=10, pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(fill="x", padx=10, pady=5)


def add_message(sender, msg):
    chat_box.config(state="normal")
    chat_box.insert(tk.END, f"{sender}: {msg}\n")
    chat_box.config(state="disabled")
    chat_box.see(tk.END)


# ---------------- Socket ---------------- #

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server listening on {HOST}:{PORT}")

client, addr = server.accept()

print("Connected:", addr)
add_message("System", f"Client connected: {addr}")


# ---------------- Receive Thread ---------------- #

def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")

            if not message:
                break

            root.after(0, add_message, "Client", message)

        except:
            break


threading.Thread(target=receive, daemon=True).start()


# ---------------- Send ---------------- #

def send(event=None):
    message = entry.get().strip()

    if message == "":
        return

    client.send(message.encode("utf-8"))

    add_message("You", message)

    entry.delete(0, tk.END)


send_button = tk.Button(root, text="Send", command=send)
send_button.pack(pady=5)

entry.bind("<Return>", send)

root.mainloop()

client.close()
server.close()