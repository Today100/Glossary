import math
from tkinter import *
from tkinter import ttk
from tkinter import font




root = Tk()
root.geometry("500x500")

def enter(e=None):
    li['state'] = DISABLED

def leave(e=None):
    li['state'] = NORMAL

def de(e=None):
    x = li.get('1.0', END)
    li.delete('1.0', END)
    li.insert(END, x)

def countlines(event):
    print(event)
    (line, c) = map(int, event.widget.index("end-1c").split("."))
    print (line)
    run(line)

def run(line):
    line= str(float(line))
    x = text.get(line, line + " lineend")
    print(x)
    if x == '\n':
        return
    else:
        line = int(float(line))
        print(line, x)
        li.delete(line-1)
        li.insert(line-1, x)

sf = font.Font(size=10)
text = Text(root, width=35, height=50, font=("Helvetica", "13"))
text.pack()
# text.bind('<Return>', run)
text.bind("<KeyRelease>", countlines)
text.place(x=0, y=0)

li = Listbox(root, width=35, height=50, font=("Helvetica", "13"))

# li = Text(root, width=35, height=50, font=sf)
li.pack()
li.place(x=250, y=0)
# li.bind("<Enter>", enter)
# li.bind("<Leave>", leave)
mainloop()