import math
from tkinter import *
from tkinter import ttk
from tkinter import font
root = Tk()
root.geometry("500x500")

Frame1 = Frame(root)
Frame2 = Frame(root)

Frame2.grid(column=1, row=2)
Frame1.grid(column=0, row=2)


be = Entry(Frame1, name=str(0))
be2 = Entry(Frame2)

dic = {
    0 : (be)
}

beli = []

nenu = 1

beli.append(be)
be.grid(sticky='w')
be2.grid(sticky='ne')







def create_new(e):
    global nenu
    print(nenu)
    ne = Entry(Frame1, name=str(nenu))
    ne.grid(sticky='w')
    beli.append(ne)

    ne.focus()
    ne.bind('<Return>', create_new)
    ne.bind('<Up>', sele_up)
    ne.bind('<Down>', sele_down)

    bl = Entry(Frame2, name=str(nenu))
    bl.grid(sticky='w')
    
    nenu += 1
    # print(dic)






def sele_up(event):
    x = int(str(event.widget).split(".")[-1])
    print('first' + str(x))
    x = x-1
    print('second' + str(x))
    
    for be in beli:
        print(int(str(be).split(".")[-1]))
        if int(str(be).split(".")[-1]) == x or int(str(be).split(".")[-1]) == 0:
            
            be.focus()






def sele_down(event):
    x = int(str(event.widget).split(".")[-1])
    print('first' + str(x))
    x = x+1
    print('second' + str(x))
    
    for be in beli:
        print(int(str(be).split(".")[-1]))
        if int(str(be).split(".")[-1]) == x or int(str(be).split(".")[-1]) == 0:
            
            be.focus()





be.bind('<Return>', create_new)
be.bind('<Up>', lambda event: sele_up(event))
be.bind('<Down>', lambda event: sele_down(event))


mainloop()