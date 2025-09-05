from tkinter import *

window = Tk()
window.title("Age Calculator App")
window.geometry('400x500')

# add label
lbl = Label(text="Welcome to the Age Calculator App!", fg='white', bg='#154360', height=2, width=35)

# labels for number inputs
# num1
yb_lbl = Label(text="Enter your birth year:- ", fg="#156049", bg='white', height=1, width=20)
yb_entry = Entry()
# num2
cy_lbl = Label(text="Enter the current year:-", fg='#154360', bg='white', height=1, width=20)
cy_entry = Entry()

# text widget to display information
text_box = Text(fg='#2C3E50', height=2, width=30)

# function to display message
def display():
    year_born = float(yb_entry.get())
    current_year = float(cy_entry.get())
    age = str(current_year - year_born)
    message = "The age is:- "
    # display the message contents in text box
    text_box.delete(1.0, END)
    text_box.insert(END, message + str(age))

# add button
btn = Button(text="Calculate", fg='white', bg='#2E86C1', height=1, width=10, command=display)

# organize all the widgets in the window
lbl.pack()
yb_lbl.pack()
yb_entry.pack()
cy_lbl.pack()
cy_entry.pack()
btn.pack()
text_box.pack()

# start the GUI loop
window.mainloop()
