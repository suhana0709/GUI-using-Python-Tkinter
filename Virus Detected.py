from tkinter import *      #this imports all the exsisting libraries
from tkinter import messagebox         #the messagebox is a sub library

window = Tk()
window.title("")
window.configure(bg = "#e3e3e3")        #window colour
window.geometry("200x200")

def msg():
    messagebox.showwarning("Alert!", "Stop!! Virus Found.")

button = Button(window, text="Scan for Virus", command=msg)
button.place(x=40, y=40)

window.mainloop()