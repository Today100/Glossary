from tkinter import *
from tkinter import ttk

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

    def toggle(self):
        """Switches the label frame to the opposite state."""
        print(self.variable.get())
        self.variable.set(not self.variable.get())
        self.activate()


def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))
    Undo_c.configure(scrollregion=Undo_c.bbox('all'))
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
    Fini_f['width'] = canvas_width
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

addB = Button(Fone, text='+', font='times, 20', name='addb')
addB.grid(row=0, column=1, padx=10)







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

# for x in range(1, 100):
#     s = Button(Undo_cf, text='hello' + str(x))
#     s.pack()




FINI = Cp(TaskF, expanded_text='>>Finished', collapsed_text='<<Finished', expanding=True)
FINI.pack(anchor='w', expand=True, fill='both', padx=10, pady=20)

Fini_f = Frame(FINI.frame, background='white', width=150, height=500)
Fini_f.pack(anchor='w', fill='both', expand=True)

Undo_f.bind("<Configure>", on_configure)
# Fini_f.bind("<Configure>", on_configure)
# UNDO.bind("<Configure>", on_configure)
# FINI.bind("<Configure>", on_configure)












root.mainloop()