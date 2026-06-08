from tkinter import *
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)   


my_label_0 = Label(text = "is equal to", font = ("Arial", 24, "bold"))
my_label_0.grid(column=0, row=1)

my_label_1 = Label(text = "Km", font = ("Arial", 24, "bold"))
my_label_1.grid(column=2, row=1)

my_label_2 = Label(text = "Miles", font = ("Arial", 24, "bold"))
my_label_2.grid(column=2, row=0)

entry_button = Entry(width=10)
entry_button.grid(column=1, row=0)


window.mainloop()