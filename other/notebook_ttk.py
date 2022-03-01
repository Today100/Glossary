from tkinter import *
from tkinter import ttk

root = Tk()
s = ttk.Style
s.theme_names = 'clam'
note = ttk.Notebook(root)
note.pack()

count = 1
for x in range(4):
    
    frame1 = Frame(note, height=500, width=500, bg='white')
    frame1.pack()
    note.add(frame1, text='hello' + str(count))
    count += 1

#b = Button(frame1, text='delete', command=delete)
#b.pack()
note.select(0)








def on_close_release(event):
    """Called when the button is released"""


    element =  note.identify(event.x, event.y)
    print(element)

    index = note.index(f"@{event.x},{event.y}")
    print(index)
    
    note.forget(index)
    # note.event_generate("<<NotebookTabClosed>>")
















def me(event):

    try:
        element =  note.identify(event.x, event.y)
        print(element)


        index = note.index("@%d,%d" % (event.x, event.y))
        print(f"@{event.x},{event.y}")
        if index or index==0:
            m = Menu(note, tearoff = 0)
            m.add_command(label ="Cut", command=lambda : on_close_release(event))
            m.add_command(label ="Copy")
            m.add_command(label ="Paste")
            m.add_command(label ="Reload")
            m.add_separator()
            m.add_command(label ="Rename")
            m.tk_popup(event.x_root, event.y_root)
            

    except:
        m = Menu(note, tearoff=10)
        m.add_command(label='add')
        m.tk_popup(event.x_root, event.y_root)
        
    # do_popup(event)
    # try:
    #     m.tk_popup(event.x_root, event.y_root)
    #     m.grab_release()
    # except:
    #     pass
    


root.bind("<Button-3>", me)

# note.bind("<ButtonPress-1>", on_close_press, True)
# note.bind("<ButtonRelease-1>", on_close_release)

# def motion(event):
#     global x, y
#     x, y = event.x_root, event.y_root
#     print(x, y)

# root.bind('<Motion>', motion)
root.mainloop()


