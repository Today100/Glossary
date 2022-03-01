from tkinter import *



root = Tk()



root.geometry('20x10')

root.config(cursor = 'tcross')

root.configure(background='black')
root.attributes('-alpha', 0.01)
# root.attributes('-type', 'splash')
# root.attributes('-transparentcolor', 'black')




full = True
root.attributes('-fullscreen', TRUE)
# root.geometry('500x500')


def motion(event):
    # global x, y
    # x, y = event.x, event.y
    # print(x, y)

    cx=root.winfo_pointerx() - root.winfo_rootx()
    cy=root.winfo_pointery() - root.winfo_rooty()
    tip['text'] = str(cx)+', '+str(cy)
    tip.place(x=cx, y=cy)



tip = Label(root, text='', bg='white')


def small(event=None):
    global full
    if full == True:
        root.attributes('-fullscreen', FALSE)
        root.overrideredirect(1)
        root.geometry('2000x750')
        full = False
    elif full == False:
        root.overrideredirect(0)
        root.attributes('-fullscreen', TRUE)
        full = True
    


def destroy(event=None):
    root.destroy()



root.bind('<Motion>', motion)
root.bind('<Escape>', destroy)
root.bind('<Return>', small)


mainloop()
