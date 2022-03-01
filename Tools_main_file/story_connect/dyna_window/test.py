from tkinter import *
from tkinter import ttk
from dynamic_window import dyna


root = Tk()

for x in range(10):
    n = Label(root, text=x)
    n.grid(row=0, column=x, padx=20)


dyna(root)


root.mainloop()