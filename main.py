from tkinter import *

root = Tk()
root.title("My project")
root.geometry("400x300")

#label
label = Label(root, text="Enter name:")
label.pack()

entry = Entry(root)
entry.pack()

root.mainloop()
