import tkinter as tk
from tkinter import ttk


form = tk.Tk()
form.geometry("500x280")
# a = tk.LabelFrame(form, width=385, height=460)
# a.grid(row=0, column=0)

tab_parent = ttk.Notebook(form)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="All records")
tab_parent.add(tab2, text="Add New record")
# tab_parent.pack(expand=1, fill='both')

q = tk.Frame(form)
q.grid(row=0, column=1)




def add_tab(): 


    s = ttk.Frame(tab_parent)
    tab_parent.add(s, text='random')
    k = tk.Button(s, text='hello world!')
    k.pack()


    


n = tk.Button(q, text='+', command=add_tab).grid(row=1, column=1)

tab_parent.pack(expand=1, fill='both', side=tk.LEFT)


form.mainloop()




# from tkinter import *
# from tkinter import ttk

# root = Tk()
# note = ttk.Notebook(root)

# b = Button(root, text="OK")
# b.grid()

# tab1 = Frame(note)
# tab2 = Frame(note)
# tab3 = Frame(note)
# n = Button(root, text='Exit', command=root.destroy).grid(row=1, column=1)

# note.add(tab1, text = "Tab One")
# note.add(tab2, text = "Tab Two")
# note.add(tab3, text = "Tab Three")
# note.grid(row=1)

# root.mainloop()