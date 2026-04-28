from tkinter import *

#sql 
import sqlite3

root = Tk()
root.title("My project")

root.geometry("600x500")

# DATABASE
# connect to database
conn = sqlite3.connect("students.db")

# cursor
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    gender TEXT,
    gpa REAL,
    year INTEGER,
    course TEXT,
    support TEXT
)
""")

#save 
conn.commit()




#label_name
label_name = Label(root, text="Enter full name:")
label_name.pack()
entry_name = Entry(root)
entry_name.pack()

# Gender
label_gender = Label(root, text="Gender:")
label_gender.pack()

gender_var = StringVar()
gender_var.set("Male") 

Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
Radiobutton(root, text="Other", variable=gender_var, value="Other").pack()

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


# Course (dropdown)
label_course = Label(root, text="Course:")
label_course.pack()

course_var = StringVar()

course_var.set("Year 1")

dropdown = OptionMenu(root, course_var, "Year 1", "Year 2", "Year 3", "Year 4")
dropdown.pack()


# Support needed (checkboxes)
label_support = Label(root, text="Support needed:")
label_support.pack()

financial_var = IntVar()
accommodation_var = IntVar()
disability_var = IntVar()

checkbox1 = Checkbutton(root, text="Financial support", variable=financial_var)
checkbox1.pack()

checkbox2 = Checkbutton(root, text="Accommodation", variable=accommodation_var)
checkbox2.pack()

checkbox3 = Checkbutton(root, text="Disability support", variable=disability_var)
checkbox3.pack()


#save data function
def save_data():
    print("clicked")

    name = entry_name.get()
    gpa = entry_gpa.get()
    year = scale_year.get()
    course = course_var.get()
    gender = gender_var.get()

# check GPA
    try:
        gpa = float(gpa)
    except:
        print("Error: GPA must be a number")
        return
    if gpa < 0 or gpa > 4:
        print("Error: GPA must be between 0 and 4")
        return
    
    #support
    support = ""

    if financial_var.get() == 1:
        support += "Financial "

    if accommodation_var.get() == 1:
        support += "Accommodation "

    if disability_var.get() == 1:
        support += "Disability "

  
    print("Name:", name)
    print("GPA:", gpa)
    print("Year:", year)
    print("Course:", course)
    print("Gender:", gender)
    print("Support:", support)





















    #button
button = Button(root, text="Save", command=save_data)
button.pack()



























root.mainloop()
