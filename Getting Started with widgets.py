from tkinter import *
from datetime import date

# creating window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x500')

# add label
lbl = Label(text="Hey There!", fg="white", bg="#072f5f", height=1, width=300)

# add label for getting name as input from the user
name_lbl = Label(text="Full Name: ", bg='#3895D3')
name_entry = Entry()

# add a text widget to display information/messages
text_box = Text(height=5, width=40)

# function to display a message
def display():
    # name input from the user
    name = name_entry.get()

    # clear old text
    text_box.delete(1.0, END)

    # message content
    message = "Welcome to the Application!\nToday's Date is: "
    greet = "Hello " + name + "\n"

    # display details in text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, str(date.today()))

# add button
btn = Button(text="Begin", command=display, height=1, bg='#1261A0', fg='white')

# organize all the widgets in the window
lbl.pack(pady=5)
name_lbl.pack()
name_entry.pack()
btn.pack(pady=10)
text_box.pack()

# start the GUI loop
root.mainloop()
