#library
from tkinter import *

#window
window = Tk()
window.title('Number Pad')
window.geometry('400x500')

#number grid
num = [[7, 8, 9], [4, 5, 6], [1, 2, 3], ['*', 0, '#']]

#Configure(arrange) row and coloumn to resize the window
for i in range(4):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

#create and place labels in the grid

for i in range(4):      #outer loop for row
    for j in range(3):     #inner loop for coloumn
        frame = Frame(master=window, relief=SUNKEN, borderwidth=1, bg="#7e807f")
        frame.grid(row = i, coloumn = j, sticky ='nsew')
        label = Label(master=frame, text = num[i][j], bg = '#939695', font=('Calibri', 18))
        label.pack(expand = True, fill='both', padx = 5, pady = 5)

window.mainloop()