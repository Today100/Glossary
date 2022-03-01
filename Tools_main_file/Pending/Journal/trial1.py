from tkinter import *
from tkinter import ttk

root = Tk()

Frame1 = Frame(root)
Frame1.pack()
main_f = Frame(root)
main_f.pack(expand=True, fill=X)

main = Text(main_f)
main.pack(expand=True, fill=BOTH)




mainloop()