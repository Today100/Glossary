from tkinter import *

root=Tk()
entries = []

for i in range(10):
    en = Entry(root)
    en.grid(row=i+1, column=0)
    entries.append(en)

def hallo():
    for entry in entries:
        print(entry.get())

button=Button(root,text="krijg",command=hallo).grid(row=12,column=0)

root.mainloop()