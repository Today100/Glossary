# from tkinter import *

# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill = Y )

# mylist = Listbox(root, yscrollcommand = scrollbar.set )
# for line in range(100):
#    mylist.insert(END, "This is line number " + str(line))

# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )

# mainloop()

import tkinter as tk
from tkinter import ttk


def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))


root1 = tk.Tk()
root = ttk.Frame(root1)
root.pack()

# --- create canvas with scrollbar ---

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

def _on_mousewheel(event):
    print(event, event.delta)
    print(event.widget)
    canvas.yview_scroll(-1*int((event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)
# ...



# --- put frame in canvas ---

frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

# --- add widgets in frame ---

l = tk.Label(frame, text="Hello", font="-size 50")
l.pack()

l = tk.Label(frame, text="World", font="-size 50")
l.pack()

l = tk.Label(frame, text="Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font="-size 20")
l.pack()

# --- start program ---

root.mainloop()

