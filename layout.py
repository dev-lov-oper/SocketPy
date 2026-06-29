from tkinter import *

from server import send
root = Tk()
entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root) 
listbox.pack()

button = Button(root, text="Send", command=lambda: send(listbox, entry))
button.pack(side=BOTTOM)

root.mainloop()
    