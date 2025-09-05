from tkinter import*

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

#Event Handler for Keypress
def handle_keypress(event):
    """Print the character associated with the Ketpress"""
    print(event.char)

#Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

#Event Handler for button click
def handle_click (event):
    print("The button was clicked!")

button = Button(text = "Clik Me!")
button.pack()

#Bind click event to handle click
button.bind("<Button-1>", handle_click)

window.mainloop()