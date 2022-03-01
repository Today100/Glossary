import tkinter as tk
from tkinter import ttk

def add_tab(event):
    all_tabs = note.tabs() # gets tuple of tab ids
    sel = note.select() # gets id of selected tab

    # if the selected tab is the last tab in the Notebook
    if sel == all_tabs[-1]:
        # Change the text from '+++' to 'New Tab'
        note.tab(sel, text = 'New Tab')
        # root.nametowidget is used to map the id to widget
        # this shows adding widgets to the existing tab
        tab_id = root.nametowidget(sel)
        tk.Label(tab_id, text = 'This is a new tab').pack()

        # add a new 'New Tab' button
        note.add(tk.Frame(note), text = '+++')

root = tk.Tk()
root.minsize(250, 250)

note = ttk.Notebook(root, height = 200, width = 200)

note.add(tk.Frame(note), text = '+++')

note.pack()
note.bind('<ButtonRelease-1>', add_tab)

root.mainloop()