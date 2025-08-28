from tkinter import *

window = Tk()
window.title("Here's the Product!")
window.geometry('400x500')

# add label
lbl = Label(text="Welcome to the Multiplication App!", fg='white', bg='#154360', height=2, width=35)

# labels for number inputs
# num1
num1_lbl = Label(text="Enter number 1:- ", fg='#154360', bg='white', height=1, width=20)
num1_entry = Entry()
# num2
num2_lbl = Label(text="Enter number 2:-", fg='#154360', bg='white', height=1, width=20)
num2_entry = Entry()

# text widget to display information
text_box = Text(fg='#2C3E50', height=2, width=30)

# function to display message
def display():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    product = num1 * num2
    message = "The product is:- "
    # display the message contents in text box
    text_box.delete(1.0, END)
    text_box.insert(END, message + str(product))

# add button
btn = Button(text="Multiply", fg='white', bg='#2E86C1', height=1, width=10, command=display)

# organize all the widgets in the window
lbl.pack()
num1_lbl.pack()
num1_entry.pack()
num2_lbl.pack()
num2_entry.pack()
btn.pack()
text_box.pack()

# start the GUI loop
window.mainloop()
