from tkinter import *

root = Tk()
root.title("My project")

root.geometry("600x500")

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





















    #button
button = Button(root, text="Save", command=save_data)
button.pack()



























root.mainloop()
