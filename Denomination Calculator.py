#libraries
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

#main window
window = Tk
window.title("Denomination Calculator")
window.geometry("650x500")
window.configure(bg='#def2cb')

#adding images and labels to the main window
upload = Image.open("bg.jpeg")
#resize the image using the resize() method
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(window, image=image, bg="#def2cb")
label.place(x=180, y=20)

label1 = Label(root,
               text="Welcome to the Denomination Counter Application!",
               bg="#def2cb")
label1.place(relx=0.5, y=340, anchor=CENTER)

#function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == "ok":
        topwin()

