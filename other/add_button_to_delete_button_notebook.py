from tkinter import *
from tkinter import ttk

class Cb(ttk.Notebook):
    """A ttk Notebook with close buttons on each tab"""

    __initialized = False

    def __init__(self, window, *args, **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__inititialized = True

        kwargs["style"] = "CustomNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs)

        self._active = None

        self.labelcount = 0
        self.window = window
        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)
        self.bind("<Double-Button-1>", self.double)

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)

        if 'add' in element:
            self.state(['pressed'])
            print('ok')
        
        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
         
            self._active = index
            return "break"
        
    def on_close_release(self, event):
        """Called when the button is released"""
        if not self.instate(['pressed']):
            
            return

        element =  self.identify(event.x, event.y)

        if 'add' in element:
            tabs = Frame(self)
            self.add(tabs, text='new tab')
            
            self.state(["!pressed"])
            self._active = None
            return

        if "close" not in element and 'add' not in element:
            # user moved the mouse off of the close button
            return

        else:
            index = self.index("@%d,%d" % (event.x, event.y))

            if self._active == index:
                self.forget(index)
                self.event_generate("<<NotebookTabClosed>>")

            self.state(["!pressed"])
            self._active = None
    
    def double(self, event):
        element =  self.identify(event.x, event.y)
        if 'label' in element:

            self.k = Toplevel()
            self.n = Entry(self.k)
            self.n.pack()
            self.n.bind("<Return>", lambda x: self.change_name(e=None, ind=self.index("@%d,%d" % (event.x, event.y))))
            print(event)
        else:
            self.on_close_press(event)
            self.on_close_release(event)
    
    
    def change_name(self, e, ind):
        
        self.tab(ind, text=self.n.get())
        self.k.withdraw()

    
    #region
    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            '''),
            PhotoImage('img_add', data='''iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAI
            AAAACUFjqAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7
            DAcdvqGQAAABrSURBVChTdY9tC4AgDITnadCX/v9PDQK3zrlKix4Qd+7tFBsoy5YSQji
            QAa27iIVw5rTWiC6mNFs5PEIn8eSyaj3MtGmHt5kAmTG9tMQNwAHtHbmw6vHifXTAFf3
            hvZv0muCb/v9YNxWCiJxJSTIio3ZmtAAAAABJRU5ErkJggg==
            '''),
            PhotoImage('img_addpressed', data='''iVBORw0KGgoAAAANSUhEUgAAAA
            oAAAAKCAIAAAACUFjqAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcw
            AADsMAAA7DAcdvqGQAAABnSURBVChThY7RDYAwCESBgVxAt4cu4CgOQL1CRT+a+JK2dx
            xpjlWVAmbetwOinQbdA8kMwJRw97RvvEQAHvyWvsBk0K/pl/x8zmY2GorgXjTHwaiqJh
            E9zbEbw8l3dcRpaglxCiK6AaifRXf2P6UOAAAAAElFTkSuQmCC
            '''),
            PhotoImage('img_addactive', data='''iVBORw0KGgoAAAANSUhEUgAAAAoAA
            AAKCAIAAAACUFjqAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAD
            sMAAA7DAcdvqGQAAABgSURBVChThY5RDoAwCEOBa+34266FvoFDP5b4El1LCan23iVQ1
            dYaYs6JvgLLDDAl3D3tGx8x4OFa+oLJom4e+TmuY4zV0Iz/oTkfo6qaRLSbsxvDh+/qi
            tPUEnEKEbkBaN9GgzcHQJAAAAAASUVORK5CYII=
            ''')
        )

        style.element_create("close", "image", "img_close",
                            ("active", "pressed", "!disabled", "img_closepressed"),
                            ("active", "!disabled", "img_closeactive"),border=8, sticky='')
        
        style.element_create("add", 'image', 'img_add', 
                            ('active', 'pressed', '!disabled', 'img_addpressed'),
                            ('active', '!disabled', 'img_addactive'), border=8, sticky='')

        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        # style.layout("CustomNotebook", [("CustomNotebook.add", {'sticky' : 'ne'})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nwse",
                    "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {'side':'left', 'sticky' : 'ne'}),
                                    ("CustomNotebook.add", {"side":'left', 'sticky':'nwse'})
                                    
                                ]
                        })
                    ]
                })
            ]
        })
    ])
#endregion


class Zm(object):
    def __init__(self, master):
        self.master=master
        self.master.state('zoomed')



if __name__ == "__main__":
    root = Tk()
    Zm(root)
    app_w = root.winfo_screenwidth()
    app_h = root.winfo_screenheight()
    notebook = Cb(window=root, width=app_w, height=app_h)
    notebook.pack(side="top", fill="both", expand=True)

    for color in ("red", "orange", "green", "blue", "violet", 'white', 'black', 'yellow', 'brown'):
        frame = Frame(notebook, background=color)
        notebook.add(frame, text=color)

    root.mainloop()



