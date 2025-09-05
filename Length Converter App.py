from tkinter import*

def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text="Length in cm: " + str(cm))
    
    except ValueError():
        result_label.config(text="Please, enter a valid number.")
        
#window
window = Tk()
window.title("Length Converter App")
window.configure(bg="#2b6e4c")
window.geometry("300x200")

#creating and placing widgets
label = Label(window, text="Enter length in inches: ", bg="#52a87d")
label.pack(pady=5)

entry = Entry(window)
entry.pack(pady=5)

convert_button = Button(window, text="Convert", command=convert)
convert_button.pack(pady=5)

result_label = Label(window, text="Lenth in cm: ", bg = "#edd46f")
result_label.pack(pady=5)


window.mainloop()