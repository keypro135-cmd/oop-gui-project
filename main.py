from tkinter import *

root = Tk()
root.title("My project")

root.geometry("400x300")

#label
label_name = Label(root, text="Enter name:")
label_name.pack()
entry = Entry(root)
entry.pack()

# GPA
label_gpa = Label(root, text="Enter GPA:")
label_gpa.pack()
entry_gpa = Entry(root)
entry_gpa.pack()


# Year of Birth
label_year = Label(root, text="Year of Birth:")
label_year.pack()
scale_year = Scale(root, from_=1980, to=2009, orient=HORIZONTAL)
scale_year.pack()


root.mainloop()
