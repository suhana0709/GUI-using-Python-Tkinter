from tkinter import*
#main window
main = Tk()
main.title("Main")
main.geometry("300x400")

#function for (Top Level) window
def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    #adding lable
    tlbl = Label(top, text="This is a top level window.")
    tlbl.pack()

    top.mainloop()

#adding label and btn th main window
lbl = Label(main, text="This is main window.")
btn = Button(main, text="Click here to open another window", command = topwin)


lbl.pack()
btn.pack()

main.mainloop()