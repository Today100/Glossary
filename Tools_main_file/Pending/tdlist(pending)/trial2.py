from tkinter import *
from tkinter import ttk
import time
from tkinter import filedialog
from typing import Literal
import json

# from Tkinter import Widget
# Widget._nametowidget(parent)

file = open('E:\\1.Python_f\\Glossory\\Tools_main_file\\tdlist\\info.json', 'a')
root = Tk()
root.geometry("500x500")
#Collapsible pane
class Cp(ttk.Frame):
    """
    -----USAGE-----
    collapsiblePane = CollapsiblePane(parent,
                        expanded_text =[string],
                        collapsed_text =[string])

    collapsiblePane.pack()
    button = Button(collapsiblePane.frame).pack()
    """

    def __init__(self, parent, expanded_text ="Collapse <<",
                            collapsed_text ="Expand >>", expanding = False, name='cp'):

        ttk.Frame.__init__(self, parent, name=name)

        # These are the class variable
        # see a underscore in expanded_text and _collapsed_text
        # this means these are private to class
        self.parent = parent
        self.expanded_text = expanded_text
        self.collapsed_text = collapsed_text

        # Here weight implies that it can grow it's
        # size if extra space is available
        # default weight is 0
        self.columnconfigure(1, weight = 1)

        # Tkinter variable storing integer value
        self.variable = IntVar()

        # Checkbutton is created but will behave as Button
        # cause in style, Button is passed
        # main reason to do this is Button do not support
        # variable option but checkbutton do
        self.button = ttk.Checkbutton(self, variable = self.variable,
                            command = self.activate, style ="TButton")
        self.button.grid(row = 0, column = 0)

        # This wil create a separator
        # A separator is a line, we can also set thickness
        self.separator = ttk.Separator(self, orient ="horizontal")
        self.separator.grid(row = 0, column = 1, sticky ="we")

        self.frame = ttk.Frame(self, name='special')

        # This will call activate function of class
        self.activate()


        if expanding:
            self.toggle()

    def activate(self):
        if not self.variable.get():

            # As soon as button is pressed it removes this widget
            # but is not destroyed means can be displayed again
            self.frame.grid_forget()

            # This will change the text of the checkbutton
            self.button.configure(text = self.collapsed_text)

        elif self.variable.get():
            # increasing the frame area so new widgets
            # could reside in this container
            self.frame.grid(row = 1, column = 0, columnspan = 2)
            self.button.configure(text = self.expanded_text)

    def toggle(self, _state = 'default'):
        """Switches the label frame to the opposite state."""
        self.variable.set(not self.variable.get())
        if _state != 'default':
            self.variable.set(_state)
        self.activate()

dic = {}

class autoE(Entry):
    """please don't make fontcolor same to placecolor"""
    def __init__(self, parent, placeholder=None, placecolor='gray', fontcolor='black', only=Literal['None', 'Num', 'Text'], limit=int, space=True, quote=True, **arg):
        Entry.__init__(self, parent, fg=placecolor, **arg)
        self.bind("<Button-1>", self.click)
        self.bind("<FocusOut>", self.out)
        self.bind("<KeyRelease>", self.check)
        self.ph = placeholder
        self.fontc = fontcolor
        self.only = only
        self.limit = limit
        
        self.num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.quote = """[ ! @ # $ % ^ & * ( ) , . / < > ? ; ' \ : ` ~ - = _ +"""
        if space:
            self.num.append(' ')
            self.text.append(' ')
        if quote:
            self.num.extend(self.quote.split(' '))
            self.text.extend(self.quote.split(' ')) 
        self.placecolor = placecolor
        self.insert(END, self.ph)

    def click(self, e):
        if self.get() == self.ph and self['fg'] == self.placecolor:
            self.delete(0, END)
            self['fg'] = self.fontc
    def out(self, e):
        if not self.get():
            self['fg'] = self.placecolor
            self.insert(END, self.ph)
    def check(self, e):
        s = ''
        if self.only == 'Num':
            
            for w in self.get():
                if w in self.num:
                    s += w
            try:
                s = s[:self.limit]
            except TypeError:
                pass
            self.delete(0, END)
            self.insert(END, s)
        elif self.only == 'Text':
            for w in self.get():
                if w in self.text:
                    s += w
            try:
                s = s[:self.limit]
            except TypeError:
                pass
            self.delete(0, END)
            self.insert(END, s)
            return

##### ENDED ON trying to change the task from doing to finished. Since the master cannnot be changed, working on
##### to collect all the info of each widget in the task and moving it to the opposite pane. The get funtion will
##### trying to get the parents, the widget info and everything. Trying to work on that. Haven't finished yet.

def get(e):
    n = e.widget.winfo_parent()
    
    # n = n[0:-1]
    # n = '.'.join(n)
    print(n)
    get = [x for x in e.widget.config()]
    dic[e.widget] = {}
    for x in get:
        d = e.widget.cget(x)
        dic[e.widget][x] = d
    
    # s = "<tkinter.Frame object " + n + ">"
    n = root.nametowidget(n)
    n.destroy()
    # 
    # n['parent'] = Fini_cf
    return
count = 0

def add_task(e):
    global count
    task = mainE.get()
    if task:
        tf = Frame(Undo_cf, name=task.lower()+'-frame'+str(count))
        tf.pack(anchor='w')
        # var = StringVar()
        # for x in range(0, 10):
        check = ttk.Checkbutton(tf, text=task, variable=StringVar(), name=task.lower()+'-check'+str(count))
        check.state(['!alternate'])
        check.pack(padx=20)
        count += 1
        check.bind('<Button-1>', get)
        
        
        on_configure(None)
    return

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))
    Undo_c.configure(scrollregion=Undo_c.bbox('all'))
    Fini_c.configure(scrollregion=Fini_c.bbox('all'))
    return

def _on_mousewheel(event):
    print(event, event.delta)
    print(event.widget)
    sx, sy = scrollbar.get()
    if 'undo_cf' in str(event.widget):
        Undo_c.yview_scroll(-1*int((event.delta/120)), "units")
        if 1.0 in Undo_s.get() and event.delta == -120 or 0.0 in Undo_s.get() and event.delta == 120:
            canvas.yview_scroll(-1*int((event.delta/120)), "units")
        return
    elif 'fini_cf' in str(event.widget):
        Fini_c.yview_scroll(-1*int((event.delta/120)), "units")
        if 1.0 in Fini_s.get() and event.delta == -120 or 0.0 in Fini_s.get() and event.delta == 120:
            Fini_c.yview_scroll(-1*int((event.delta/120)), "units")
        return
    if sx == 0.0 and sy == 1.0:
        return
    canvas.yview_scroll(-1*int((event.delta/120)), "units")
    return

def FrameWidth(event):
    canvas_width = event.width
    canvas.itemconfig(canva_frame, width = canvas_width)
    Undo_c['width'] = canvas_width -50
    Undo_c.itemconfig(Undo_cff, width=canvas_width-50)
    Undo_c['height'] = root.winfo_height()-200
    Fini_c['width'] = canvas_width -50
    Fini_c.itemconfig(Fini_cff, width=canvas_width-50)
    Fini_c['height'] = root.winfo_height()-200
    return

Fone = Frame(root, name='fone')
Fone.pack(anchor='center')

canvas = Canvas(root, name='main_canvas')
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(root, command=canvas.yview, name='main_scrollbar')
scrollbar.pack(side=RIGHT, fill=Y)

# scrollbar.bind('<Enter>', on_configure)
# canvas.bind('<Enter>', on_configure)

canvas.configure(yscrollcommand = scrollbar.set)

canvas.bind('<Configure>', on_configure)

TaskF = Frame(canvas, name='taskf')
# TaskF.pack(expand=True, fill=BOTH)
canva_frame = canvas.create_window((0,0), window=TaskF, anchor='nw')
canvas.bind('<Configure>', FrameWidth)
canvas.bind_all("<MouseWheel>", _on_mousewheel)
# TaskF = Frame(root)
# TaskF.pack(anchor='w', padx=50, pady=50)

mainE = Entry(Fone, width=50, name='maine')
mainE.grid(row=0, column=0)
mainE.bind("<Button-1>", lambda x: maincp.toggle(_state=1))
mainE.bind("<Return>", add_task)

addB = Button(Fone, text='+', font='times, 20', name='addb')
addB.grid(row=0, column=1, padx=10)
# addB.bind("<Button-1>", add_task)

maincp = Cp(Fone, expanded_text='Description____________', collapsed_text='Description------------------', expanding=False, name='maincp')
mainT = Text(maincp.frame, height=5, width=50, name='maint')
mainT.grid(row=10, column=0, sticky='w')
maincp.grid(row=3, columnspan=2, sticky='w')

due = Frame(maincp.frame)
due.grid(row=1, columnspan=2)

minute_e = autoE(due, 'min', only='Num', limit=2, space=False, quote=False, width=4)
minute_e.grid(row=0, column=2)

lab = Label(due, text=':')
lab.grid(row=0, column=1)

hour_e = autoE(due, 'hour', only='Num', limit=2, space=False, quote=False, width=4)
hour_e.grid(row=0, column=0)

day_e = autoE(due, 'day', only='Num', space=False, quote=False, limit=2, width=4)
day_e.grid(row=0, column=5, pady=10, padx=20)

month_e = autoE(due, placeholder='month', only='Num', space=False, quote=False, limit=2, width=6)
month_e.grid(row=0, column=4)

year_e = autoE(due, placeholder='year', only='Num', limit=4, space=False, quote=False, width=4)
year_e.grid(row=0, column=3, padx=20)

priF = Frame(maincp.frame)
priF.grid(row=2, columnspan=2)

def fore(e):
    
    for b in radio:
        b['foreground'] = 'white'
    if e == "de":
        pri.set(0)
        return
    e.widget['foreground'] = 'black'

pri = IntVar()
color = ['None', 'red', 'blue', 'green', 'brown', 'gray']
radio = []
for x in range(1, 6):
    pri_O = Radiobutton(priF, variable=pri, text='priority ' + str(x), indicatoron=0, background=color[x], value=x, foreground='white', selectcolor='yellow')
    pri_O.bind('<ButtonRelease-1>', fore)
    pri_O.grid(row=0, column=x)
    radio.append(pri_O)
pri_Od = Button(priF, text='No priority', command= lambda: fore("de"), bg='pink', fg='black')
pri_Od.grid(row=0, column=6, padx=5, pady=5)



UNDO = Cp(TaskF, expanded_text =">>Unfinished Works", collapsed_text ="<<Unfinished Works", expanding=True, name='undo')
UNDO.pack(anchor='w', expand=True, fill=BOTH, padx=10, pady=20)

Undo_f = Frame(UNDO.frame, background='white', height=300, name='undo_f')
Undo_f.pack(fill=BOTH, expand=True)

Undo_c = Canvas(Undo_f, background='black', name='undo_c', height=300)
Undo_c.pack(side=LEFT)
# Undo_c.pack_propagate(False)

Undo_f.bind('<Configure>', FrameWidth)

Undo_s = Scrollbar(Undo_f, command=Undo_c.yview, name='undo_s')
Undo_s.pack(side=RIGHT, fill='y')

Undo_cf = Frame(Undo_c, name='undo_cf', bg='white')
Undo_cff = Undo_c.create_window((0,0), window=Undo_cf, anchor='nw')

Undo_c.configure(yscrollcommand=Undo_s.set)


Undo_c.bind('<Configure>', on_configure)





FINI = Cp(TaskF, expanded_text='>>Finished', collapsed_text='<<Finished', expanding=True, name='fini')
FINI.pack(anchor='w', expand=True, fill='both', padx=10, pady=20)

Fini_f = Frame(FINI.frame, background='white', name='fini_f')
Fini_f.pack(anchor='w', fill='both', expand=True)

Fini_c = Canvas(Fini_f, background='black', name='fini_c', height=300)
Fini_c.pack(side=LEFT)
# Undo_c.pack_propagate(False)

Fini_f.bind('<Configure>', FrameWidth)

Fini_s = Scrollbar(Fini_f, command=Fini_c.yview, name='fini_s')
Fini_s.pack(side=RIGHT, fill='y')

Fini_cf = Frame(Fini_c, name='fini_cf', bg='white')
Fini_cff = Fini_c.create_window((0,0), window=Fini_cf, anchor='nw')

Fini_c.configure(yscrollcommand=Fini_s.set)


Fini_c.bind('<Configure>', on_configure)













Undo_f.bind("<Configure>", on_configure)
Fini_f.bind("<Configure>", on_configure)
UNDO.bind("<Configure>", on_configure)
FINI.bind("<Configure>", on_configure)












root.mainloop()