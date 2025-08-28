from tkinter import *
from datetime import date

#creating window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x500')

#add widgets
#add label
lbl = Label(text="Hey There!", fg="white", bg="#072f5f", height=1, width=300)

#add label for getting name as input from the user
#Use Entry Widget to create a text box for users to enter details
name_lbl = Label(text="Full Name: ", bg='#3895D3')
name_entry = Entry()

#function to display a message
def display():

    #name input from the user
    name = name_entry.get()

    #declaring a global variable
    #to make it accessible anywhere in the program
    global Message
    message = "Welcome to the Application! \nToday's Date is: "
    greet = "Hello "+name+"\n"

    #display details in text box
    #Specify where to add details inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

    #add a text widget to display information/messages
    text_box =Text(height=3)

    #add button and name of command as name of the function
    #press button, display function will be called automaticly
    btn = Button(text="Begin", command = display, height = 1, bg = '#1261A0', fg = 'white')

    #organize all the wedgets in the window 
    lbl.pack()
    name_lbl.pack()
    name_entry.pack()
    btn.pack()
    text_box.pack()

display()