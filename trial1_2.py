from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
import textwrap
import trial12
from win32api import *
from win32gui import *
import win32con
import sys, os
# import struct
import time
# import threading as TH
import base64
from pandas.io import clipboard
from tkinter import filedialog, font, colorchooser
import numexpr
from PIL import Image,ImageTk, ImageGrab


#region
# screen_w = root.winfo_screenwidth()
# screen_h = root.winfo_screenheight()

# x = (screen_w/2) - (app_w/2)
# y = (screen_h/2) - (app_h/2)

# root.geometry(f'{app_w}x{app_h}+{int(x)}+{int(y)}')
# root.attributes('-fullscreen', True)
#endregion



"""
Classes:
"""
#Tip
class Tip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 300     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

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
                            collapsed_text ="Expand >>"):

        ttk.Frame.__init__(self, parent)

        # These are the class variable
        # see a underscore in expanded_text and _collapsed_text
        # this means these are private to class
        self.parent = parent
        self._expanded_text = expanded_text
        self._collapsed_text = collapsed_text

        # Here weight implies that it can grow it's
        # size if extra space is available
        # default weight is 0
        self.columnconfigure(1, weight = 1)

        # Tkinter variable storing integer value
        self._variable = IntVar()

        # Checkbutton is created but will behave as Button
        # cause in style, Button is passed
        # main reason to do this is Button do not support
        # variable option but checkbutton do
        self._button = ttk.Checkbutton(self, variable = self._variable,
                            command = self._activate, style ="TButton")
        self._button.grid(row = 0, column = 0)

        # This wil create a separator
        # A separator is a line, we can also set thickness
        self._separator = ttk.Separator(self, orient ="horizontal")
        self._separator.grid(row = 0, column = 1, sticky ="we")

        self.frame = ttk.Frame(self)

        # This will call activate function of class
        self._activate()

    def _activate(self):
        if not self._variable.get():

            # As soon as button is pressed it removes this widget
            # but is not destroyed means can be displayed again
            self.frame.grid_forget()

            # This will change the text of the checkbutton
            self._button.configure(text = self._collapsed_text)

        elif self._variable.get():
            # increasing the frame area so new widgets
            # could reside in this container
            self.frame.grid(row = 1, column = 0, columnspan = 2)
            self._button.configure(text = self._expanded_text)

    def toggle(self):
        """Switches the label frame to the opposite state."""
        self._variable.set(not self._variable.get())
        self._activate()

#Full screen mode
class FSA(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        self.master.geometry(self._geom)
        self._geom=geom

#Zoomed screen mode
class Zm(object):
    def __init__(self, master, **kwargs):
        self.master=master
        self.master.state('zoomed')

#Text wrap
class Wrap(str):
    def __init__(self, string):
        self.string = string
    def length(self, length):
        return '\n'.join(textwrap.wrap(self.string, int(length)))

#Autosearch and Autofill
class ASF(object):

    """A class for autosearch and autofill listbox in tkinter"""

    def __init__(self, listbox, entry, data):
        self.listbox = listbox
        self.entry = entry
        self.data = data
        self.entry.bind("<KeyRelease>", self.check)
        self.listbox.bind("<<ListboxSelect>>", self.fillout)
        self.update(data)
    
    def check(self, e=None):
        typed = self.entry.get()
        if typed == '':
            data = self.data
        else:
            data = []
            for item in self.data:
                if typed.lower() in item.lower():
                    data.append(item)

        self.update(data)
    
    
    def update(self, data):
        self.listbox.delete(0, END)

        for item in data:
            self.listbox.insert(END, item)
    
    
    def fillout(self, e=None):
        self.entry.delete(0, END)
        
        self.entry.insert(0, self.listbox.get(ANCHOR))
    pass

#Notebook with x to close the window
class XNotebook(ttk.Notebook):
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
            tabs = Frame(self, height=APP_H, width=APP_W, bg='white')
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
                try:
                    if index == 0 and not self.tab(index+1, 'text'):
                        return
                except TclError:
                    return

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
        else:
            self.on_close_press(event)
            self.on_close_release(event)
    
    
    def change_name(self, e, ind):
        
        self.tab(ind, text=self.n.get())
        self.k.withdraw()


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

#Windows system notification
class WTip:
    def __init__(self, title, msg):
        message_map = {
                win32con.WM_DESTROY: self.OnDestroy,
        }
        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        classAtom = RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow( classAtom, "Taskbar", style, \
                0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                0, 0, hinst, None)
        UpdateWindow(self.hwnd)
        iconPathName = os.path.abspath(os.path.join( sys.path[0], "balloontip.ico" ))
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
           hicon = LoadImage(hinst, iconPathName, \
                    win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
          hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER+20, hicon, "tooltip")
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(NIM_MODIFY, \
                         (self.hwnd, 0, NIF_INFO, win32con.WM_USER+20,\
                          hicon, "Balloon  tooltip",msg,200,title))
        # self.show_balloon(title, msg)
        time.sleep(10)
        DestroyWindow(self.hwnd)
    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0) # Terminate the app.

#Creates the popup for the right click menu
class pop(object):
    def __init__(self, widget, widget_root):
        self.widget = widget
        self.widget_r = widget_root
        self.widget_r.bind("<Button-3>", self.popup)
    def popup(self, event):
        try:
            self.widget.tk_popup(event.x_root, event.y_root)
        finally:
            self.widget.grab_release()



def cp_text_example():
    cpane = Cp(root, 'Expanded', 'Collapsed')
    cpane.grid(row = 0, column = 0)

    # Button and checkbutton, these will
    # appear in collapsible pane container
    b1 = Button(cpane.frame, text ="GFG").grid(
                row = 1, column = 2, pady = 10)

    cb1 = Checkbutton(cpane.frame, text ="GFG").grid(
                    row = 2, column = 3, pady = 10)


"""
Tools class
"""

#Base 64 encoder
class ba64en():
    "turn file to base64 code with tkinter"
    def __init__(self, window):
        
        self.window = window
        self.window.focus()
        self.window.geometry("800x300")
        self.window.title('Base64 encoder')
        self.window.update()
        
        self.beginwin()
        

    def beginwin(self):
        self.upb = Button(self.window, text='Upload', command=self.getLocalFile)
        self.upb.pack()
        self.upb.place(x=380, y=20)
        self.copyb = Button(self.window, text='Copy', command=self.copy)
        self.copyb.pack()
        self.copyb.place(x=380, y=230)
        self.clearb = Button(self.window, text='Clear', command=self.clear)
        self.clearb.pack()
        self.clearb.place(x=745, y=210)
        self.upla = Text(self.window, bg='white', width=110, height=10)
        self.upla.pack()
        self.upla.place(x=10,y=70)
    
    def getLocalFile(self):

        self.filePath=filedialog.askopenfilename()
        with open(self.filePath, 'rb') as imagefile:
            self.encoded_string = base64.b64encode(imagefile.read())
        self.upla.insert(END, self.encoded_string)
    
    def copy(self):
        copy_string = self.upla.get("1.0",END)
        clipboard.copy(copy_string)

    def clear(self):
        self.upla.delete('1.0', END)

#Notepad calculator *needs to be improve
class cal():
    """A notepad calculator"""
    def __init__(self, widget):
        self.nenu=1
        self.root = widget
        self.root.focus()
        self.root.geometry('500x500')
        
        self.frame1 = Frame(self.root)
        self.frame2 = Frame(self.root)
        self.frame1.grid(column=0, row=0)
        self.frame1.place(x=10, y=10)
        self.frame2.grid(column=1, row=0)
        self.frame2.place(x=300, y=10)

        self.be = Entry(self.frame1)
        self.be2 = Entry(self.frame2)
        self.be.grid(row=self.nenu)
        self.be2.grid(row=self.nenu)

        self.be.bind('<Return>', self.get_n)
        self.be.bind('<Up>', self.sele_up)
        self.be.bind('<Down>', self.sele_down)
        self.be.bind('<KeyRelease>', lambda event: self.impo(event))

        
        self.dic = {
            self.nenu : (self.be)
        }

        self.cid = {
            (self.be) : self.nenu
        }

        self.dic2 = {
            self.nenu : (self.be2)
        }

        self.cid2 = {
            (self.be2) : self.nenu
        }
        
        self.av = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 
        'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.variables = {}

        self.nenu += 1

        self.mat = ['+', '-', 'x', '*', '/']
        self.eq = ['sqrt(', 'sin(']

    def sele_down(self, e):
        for key, value in self.dic.items():
            if self.root.focus_get() == value:
                key = key+1
                try:
                    s = self.dic[key]
                except:
                    return
                s.focus()
                return

    def sele_up(self, e):
        for key, value in self.dic.items():
            if self.root.focus_get() == value:
                key = key-1
                try:
                    s = self.dic[key]
                except:
                    return
                s.focus()
                return

    def calcu(self, string):
        try:
            strs = numexpr.evaluate(string)
            if strs is None:
                return string
            else:
                return strs
        except:
            return string
    
    def impo(self, e):
        w_i_d = str(e.widget).split(".")[-1]
        n_u_m = None
        for k_e_y in self.cid:
            if w_i_d in str(k_e_y):
                a_a = k_e_y
                n_u_m = self.cid[k_e_y]
        if n_u_m == None:
            return
        w_i_d2 = self.dic2[n_u_m]
        s_s = a_a.get()
        letters = ''
        n_s = None


        for x in s_s:
            if x in self.av:
                letters = letters + x
            elif x == '=' or x not in self.av:
                break
        # for x in eq:
        #     if letters in x:
        #         letters=''
    #search varible region
        #region
        if letters == 'variables':
            quick = 1
            global top
            try:
                top.destroy()#type: ignore
            except:
                pass

            top = Toplevel(self.root)
            top.geometry('10x100')
            for key, value in self.variables.items():
                xw = Label(top, text='Variable')
                yw = Label(top, text='Value')
                xw.grid(row=0, column=0)
                yw.grid(row=0, column=1)
                xs = Label(top, text=key)
                ys = Label(top, text=value)
                xs.grid(row=quick, column=0)
                ys.grid(row=quick, column=1)
                quick += 1
        
        if letters in list(self.variables):
            n_u = self.variables[letters]
            s_s = s_s.replace(str(letters), str(n_u))

        #endregion
        if "(" in s_s or "(" in str(n_s):
            n_string = str(s_s)
            try:
                braket = n_string.index('(')
                braket2 = n_string.index(')')
                the_n = n_string[braket+1:braket2]
                if the_n in list(self.variables):
                    s_s = s_s.replace(str(the_n), str(self.variables[the_n]))
            except:
                pass
            

        
        for x in s_s:
            if x == '=':
                y_y = s_s.index(x)
                
                y_y += 1
                n_n = s_s[y_y:len(s_s)]
                n_n = n_n.replace(' ', '')
                try:
                    k_k = self.calcu(n_n)
                    if k_k != n_n:
                        n_n = k_k
                except:
                    pass
                try:
                    n_n = float(n_n)
                except:
                    pass
                # if type(n_n) is int:
                try:
                    self.variables[letters] = float(n_n)
                except:
                    pass
                n_s = n_n
        try:
            if "(" in s_s or "(" in str(n_s):
                n_string = str(s_s)
                braket = n_string.index('(')
                braket2 = n_string.index(')')
                the_n = n_string[braket+1:braket2]
                if the_n in list(self.variables):
                    s_s = s_s.replace(str(the_n), str(self.variables[the_n]))
        except:
            pass
        if n_s == None:
            n_s = s_s
        n_s = self.calcu(str(n_s))
        w_i_d2.delete(0, END)
        w_i_d2.insert(END, str(n_s))
        return
    
    def get_n(self, e):
        for key, value in self.dic.items():
            if self.root.focus_get() == value:
                self.returnm(key)
                return 

    def returnm(self, n):
        global nenu
        ne = Entry(self.frame1)  
        bl = Entry(self.frame2)
        ne.focus()
        ne.bind('<Return>', self.get_n)
        ne.bind('<Up>', self.sele_up)
        ne.bind('<Down>', self.sele_down)
        ne.bind('<KeyRelease>', self.impo)
        if n != list(self.dic)[-1]:
            n += 1
            key, value = n, self.dic[n]
            key2, value2 = n, self.dic2[n]
            TEMV = value
            TE = value2
            T = True
            self.dic[n] = (ne)
            self.dic2[n] = (bl)
            self.cid[ne] = n
            self.cid2[bl] = n
            ne.grid(row=n)
            bl.grid(row=n)
            while True:
                try:
                    if T:
                        # print('I runned')
                        n += 1
                        TEMV.grid(row=n)
                        TE.grid(row=n)
                        temv = self.dic[n]
                        te = self.dic2[n]
                        self.dic[n] = TEMV
                        self.dic2[n] = TE
                        self.cid[TEMV] = n
                        self.cid2[TE] = n
                        T = False
                    elif not T:
                        # print('I also runned')
                        n += 1
                        temv.grid(row=n)
                        te.grid(row=n)
                        TEMV = self.dic[n]
                        
                        TE = self.dic2[n]
                        self.dic[n] = temv
                        self.dic2[n] = te
                        self.cid[temv] = n
                        self.cid2[te] = n
                        T = True
                        # print('IHIHIHIHIHIHIHIHIHIIHIHITEMV = ' + str(TEMV))
                except:
                    if TEMV and TE:
                        # print('it is TEMV')
                        self.dic[n] = TEMV
                        
                        self.dic2[n] = TE
                        self.cid[TEMV] = n
                        self.cid2[TE] = n
                        # print(self.dic)
                        return
                    elif temv and te:
                        # print('it is temv')
                        self.dic[n] = temv
                        self.dic2[n] = te
                        self.cid[temv] = n
                        self.cid2[te] = n
                        # print(self.dic)
                        return

        
        else:
            n += 1
            self.dic[n] = (ne)
            self.dic2[n] = (bl)
            self.cid[ne] = n
            self.cid2[bl] = n
            ne.grid(sticky='w', row=n)
            bl.grid(sticky='w', row=n)
            
            self.nenu += 1
            # print(self.dic)
            return

#Drawing board *needs to be improve
class drbo():
    "A tkinter drawing board"
    def __init__(self, tkinterwindow):
        self.window = tkinterwindow
        self.window.geometry("500x500")
        self.Fone = ttk.Labelframe(self.window)
        self.Fone.grid(row=0, columnspan=2, padx=6, pady=3)

        self.Ftwo = ttk.Labelframe(self.window)
        self.Ftwo.grid(row=1, column=0, rowspan=3)
        self.Ftwo.place(y=330, x=10)

        self.Fthree = ttk.Labelframe(self.window, text='3')
        self.Fthree.grid(row=1, column=1)
        self.Fthree.place(x=300, y=330)

        self.Ffour = ttk.Labelframe(self.window, text='4')
        self.Ffour.grid(row=2, column=1)
        self.Ffour.place(x=300, y=390)
        
        self.Ffive = ttk.LabelFrame(self.window, text='5')
        self.Ffive.grid(row=3, column=1)
        self.Ffive.place(x=300, y=450)

        self.main = Canvas(self.Fone, height=300, width=480, background='white')
        self.main.pack()


        self.samevar = IntVar()
        self.samevar.set(1)
        self.same = Scale(self.window, from_=0, to_=1, length=40, orient=HORIZONTAL, sliderlength=15, command=self.change, variable=self.samevar)
        self.same.place(x=450, y=450)

        self.sizevar = IntVar()
        self.sizevar.set(20)
        self.size = Scale(self.Fthree, from_=1, to_=100, orient='horizontal', variable=self.sizevar)
        self.size.grid(row=0, column=0)
        

        self.sizeen = Entry(self.Fthree, width=5)
        self.sizeen.grid(row=0, column=1, padx=2)
        self.sizeen.bind("<Return>", self.set_sizevar)

        self.main.bind('<Button-1>', self.draw_line)
        self.main.bind("<B1-Motion>", self.draw_line)
        self.main.bind("<ButtonRelease-1>", self.add)
        
        self.draw = []
        self.deleted = []
        self.finalde = []
        self.drawcount = 0
        self.wid=0
        self.widgets = []
        self.start = None
        self.outline = None
        self.outlinetrue = True
        self.angle = 'downright'
        self.cou = True
        
        self.set_up()
        self.bindings()


        
    def add(self, event):
        self.end = self.wid
        self.draw.append((self.start, self.end))
        self.start = None

    def change(self, event):
        if self.samevar.get() == 0:
            self.cou = False
        elif self.samevar.get() == 1:
            self.cou = True

    def set_sizevar(self, event):
        self.sizevar.set(int(self.sizeen.get()))

    def get_wid_name(self, event, widget):
        try:
            name = str(event.widget).split(".")[-1]
            return name
        except:
            name = str(widget).split(".")[-1]
            return name
    
    def set_up(self):
        self.colors = ['black', 'gray', 'white', 'dark red', 'brown', 'red', 'orange', 'yellow', 'pink', 'magenta', 'midnight blue', 'dark blue', 'blue', 'light blue', 'aquamarine', 'green', 'light green', 'erase']
        count = 0
        count2 = 0
        self.v = StringVar()
        self.v.set('black')
        
        for color in self.colors:
            if color == 'erase':
                self.clselect = Radiobutton(self.Ftwo, activebackground='white', indicatoron=0, height=2, width=4, name=color, variable=self.v, background='light gray', value='erase', wraplength=25, selectcolor='white', border=3)
                
            else:
                self.clselect = Radiobutton(self.Ftwo, activebackground=color, indicatoron=0, height=2, width=4, name=color, variable=self.v, background=color, value=color, wraplength=25, selectcolor=color, border=3)
                self.widgets.append(self.clselect)
            self.clselect.grid(row=count, column=count2, padx=3, pady=3)
            count2 += 1
            if count2 == 6:
                count += 1
                count2=0
        
        self.set_up2()
    
    def set_up2(self):
        count = 0
        names = ['save', 'undo', 'redo', 'clear', 'setting', 'open', 'fill', 'erase']
        for img in os.listdir("E:\\1.Python_f\\Glossory\\images"):
            img = Image.open(os.path.join("E:\\1.Python_f\\Glossory\\images", img))
            resized_image= img.resize((20,20), Image.ANTIALIAS)
            new_image= ImageTk.PhotoImage(resized_image)
            b3 = Button(self.Ffive, image=new_image, name=names[count], background='white')
            self.widgets.append(b3)
            b3.image = new_image
            b3.grid(row=0, column=count)
            count += 1
        self.set_up3()

    def set_up3(self):
        shapess = ['arc', 'oval', 'line', 'rectangle', 'polygon', 'image']
        self.shapetype = StringVar()
        self.shapetype.set("arc")
        count=0
        for img in os.listdir("E:\\1.Python_f\\Glossory\\shapes"):
            img = Image.open(os.path.join("E:\\1.Python_f\\Glossory\\shapes", img))
            resized_image = img.resize((20, 20), Image.ANTIALIAS)
            new_image = ImageTk.PhotoImage(resized_image)
            shab = Radiobutton(self.Ffour, height=25, width=25, indicatoron=0, variable=self.shapetype, value=shapess[count], image=new_image, name=shapess[count])
            shab.image = new_image
            shab.grid(row=0, column=count)
            count += 1
        
    
    def get_color(self, event):
        self.color = self.v.get()
        if self.color == 'erase':
            self.erase = 'Yes'
        else:
            self.erase = 'No'


    def draw_line(self, event):
        self.get_color(event)
        x1=event.x
        y1=event.y
        x2=event.x + self.sizevar.get()
        y2=event.y + self.sizevar.get()
        if self.erase == 'Yes':
            self.shape(self.shapetype.get(), x1-10, y1-10, x2+self.sizevar.get(), y2+self.sizevar.get(), fill='white', width=10, outline='white')
            return
        if not self.outline:
            self.outline = self.color
        
        else:
            if self.cou == True:
                self.outline = self.color
            else:
                try:
                    self.outline = self.outline.get()
                except:
                    pass
        self.shape(self.shapetype.get(), x1, y1, x2, y2, fill=self.color, width=1, outline=self.outline)
        # self.drawcount = self.wid
        # self.wid = self.main.create_rectangle(x1,y1,x2,y2, fill=self.color, width=1, outline='black')
        # self.main.gettags(3)
        # if not self.start:
        #     self.start = self.wid
        # self.drawcount = self.wid

    def undo(self, event):
        s, e = self.draw[len(self.draw)-1]
        for x in range(s, e+1):
            self.infowid_can(x)
            self.main.delete(x)
            
            self.drawcount = self.drawcount-1
            
        self.draw.pop(-1)
        self.deleted.append(self.finalde)
        self.finalde = []

    def infowid_can(self, wi):
        thelis = []
        self.type = self.main.type(wi)
        self.cordin = self.main.coords(wi)
        self.fi = self.main.itemcget(wi, 'fill')
        try:
            self.ou = self.main.itemcget(wi, 'outline')
        except:
            self.ou = None
        self.widt = self.main.itemcget(wi, 'width')
        thelis.extend((self.type, self.cordin, self.fi, self.ou, self.widt))
        self.finalde.append(thelis)
        # thelis.clear()
        
    def shape(self, shape, x, y, x1, y1, fill, outline, width):
        self.drawcount = self.wid
        if shape == 'rectangle':
            self.wid = self.main.create_rectangle(x-self.sizevar.get(), y-self.sizevar.get(), x1, y1, fill=fill, outline=outline, width=width)

        elif shape == 'oval':
            self.wid = self.main.create_oval(x-self.sizevar.get(), y-self.sizevar.get(), x1, y1, fill=fill, outline=outline, width=width)
        elif shape == 'line':
            try:
                angle = self.angle.get()
            except:
                angle = self.angle
            if angle == 'downright':
                x1 = x + self.sizevar.get()*4
                y1 = y + self.sizevar.get()*4
            elif angle == 'downleft':
                x1 = x -self.sizevar.get()*4
                y1 = y + self.sizevar.get()*4
            elif angle == 'horizonto':
                x1 = x + self.sizevar.get()*4
                y1 = y
            elif angle == 'verticle':
                x1 = x
                y1 = y + self.sizevar.get()*4
            self.wid = self.main.create_line(x, y, x1, y1, fill=fill, width=width)
        
        elif shape == 'arc':
            self.wid = self.main.create_arc(x-self.sizevar.get(), y-self.sizevar.get(), x1, y1, fill=fill, outline=outline, width=width)
        
        self.main.gettags(3)
        if not self.start:
            self.start = self.wid
        self.drawcount = self.wid
        
        

    def redo(self, event):
        try:
            turn = self.deleted[-1]
            for shape in turn:
                self.shape(shape[0], shape[1][0], shape[1][1], shape[1][2], shape[1][3], shape[2], shape[3], shape[4])
                
                
                # print(self.deleted)
            self.deleted.pop()
            self.add(None)
        except IndexError:
            pass

    def clear(self, event):
        self.main.delete('all')

    def settings(self, event):
        shape = self.shapetype.get()
        self.settingwin = Toplevel(self.main)
        self.settingwin.grab_set()
        self.settingwin.focus()
        self.settingwinFone = LabelFrame(self.settingwin, text='Outline')
        self.settingwinFone.pack()
        if shape == 'line':
            self.outlinetrue = False
        else:
            self.outlinetrue = True
        self.setting_set_up()

    def setting_set_up(self):
        if self.outlinetrue == False:
            self.angle = StringVar()
            try:
                self.angle.set(self.angle.get(1))
            except:
                self.angle.set(self.angle)
            self.anglechoice = ['downright', 'downleft', 'verticle', 'horizonto']
            count = 0
            for angle in self.anglechoice:
                angleradio = Radiobutton(self.settingwinFone, value = angle, variable=self.angle, text=angle)
                angleradio.grid(row=0, column=count)
                count += 1
        else:
            self.outline = StringVar()
            self.outline.set('black')
            count=0
            count2=0
            for color in self.colors:
                if color == 'erase':
                    break
                olradio = Radiobutton(self.settingwinFone, value=color, background=color, activebackground=color, activeforeground=color, indicatoron=0, variable=self.outline, selectcolor=color, height=3, width=3)
                olradio.grid(row=count, column=count2, padx=3, pady=3)
                count2 += 1
                if count2 == 6:
                    count += 1
                    count2 = 0

    def save(self, event):
        savefile = filedialog.asksaveasfile(defaultextension='.png', filetypes=(('image files', '*.jpg'), ('image file2', '*.png')))
        # self.main.update()
        # image = Image.open(self.main.postscript(file='canva.ps', colormode='color'))
        # image.save(savefile)
        x=self.window.winfo_rootx()+self.main.winfo_x()
        y=self.window.winfo_rooty()+self.main.winfo_y()
        x1=x+self.main.winfo_width()
        y1=y+self.main.winfo_height()
        # print(list(savefile))
        newpath = str(savefile).split()[1]
        newpath = newpath.split("'")
    
        ImageGrab.grab().crop((x+10,y+5,x1-15,y1-15)).save(newpath[1])
        return


    def bindings(self):
        for widgets in self.widgets:
            if self.get_wid_name(event=None, widget=widgets) == 'save':
                widgets.bind("<ButtonRelease-1>", self.save)
            elif self.get_wid_name(event=None, widget=widgets) == 'undo':
                widgets.bind("<Button-1>", self.undo)
            elif self.get_wid_name(event=None, widget=widgets) == 'redo':
                widgets.bind("<Button-1>", self.redo)
            elif self.get_wid_name(event=None, widget=widgets) == 'clear':
                widgets.bind("<Button-1>", self.clear)
            elif self.get_wid_name(event=None, widget=widgets) == 'setting':
                widgets.bind("<Button-1>", self.settings)

#Note *needs to be improve
class notedoc():
    def __init__(self, window):
        self.window = window
        
        self.window.geometry("530x500")
        
        self.Fone = Frame(self.window, width=self.window.winfo_width())
        self.Fone.pack(anchor='center')
        self.Ftwo = Frame(self.window, width=self.window.winfo_width())
        self.Ftwo.pack(fill='both', expand=True)
        Font = [x for x in sorted(list(font.families())) if '@' not in x]
        self.fonts = ttk.Combobox(self.Fone, value=Font)
        self.fonts.grid(row=0, column=0)
        self.fonts.set(Font[0])

        self.sizt = IntVar()
        self.size = Spinbox(self.Fone, values=[n for n in range(100)], textvariable=self.sizt, command=lambda: self.change_font(None))
        self.size.grid(row=0, column=1)
        self.sizt.set(20)

        self.bolt=StringVar()
        self.bold = Checkbutton(self.Fone, text='Bold', variable=self.bolt, indicatoron=0, onvalue="bold", offvalue='None', command=lambda: self.change_font(None))
        self.bold.grid(row=0, column=6)
        self.bolt.set(None)

        self.italit = StringVar()
        self.italic = Checkbutton(self.Fone, text='italic', variable=self.italit, indicatoron=0, onvalue="italic", offvalue='None', command=lambda: self.change_font(None))
        self.italic.grid(row=0, column=5)
        self.italit.set(None)


        self.pint = BooleanVar()
        self.pin = Checkbutton(self.Fone, text='pin', command=lambda: self.pin_win(self.pint.get()), variable=self.pint, indicator=0)
        self.pin.grid(row=0, column=10, padx=8)
        # pin.pack(anchor='center')
        self.pint.set(False)



        self.menu = Menu(self.window, tearoff=0)
        self.tool = Menu(self.menu, tearoff=0)
        self.tool.add_command(label = 'Tranparency', command=self.transparent_wind)
        self.tool.add_command(label='add')
        self.menu.add_cascade(label='tool', menu=self.tool)

        self.bol = self.bolt.get()
        self.ita = self.italit.get()

        self.maintext = Text(self.Ftwo, undo=True, font=(str(self.fonts.get()).split()[0], self.sizt.get()), bg='white', width=30, height=50)

        self.maintext.pack(fill='both', expand=True)

        self.maintext.tag_configure("bigfont", font=("Helvetica", "24", "bold", "italic"))
        self.tagcount = 0

        self.fonts.bind("<<ComboboxSelected>>", self.change_font)
        self.size.bind("<Return>", self.change_font)
        self.run()

        self.window.config(menu=self.menu)

        self.color = ['0, 0, 0', '#000000']
        self.bgcolor = ['255, 255, 255', '#ffffff']

    def change_tran(self, trant):
        x = trant/10
        self.window.wm_attributes('-alpha', float(x))

    def transparent_wind(self, event=None):
        trans = Toplevel(self.window)
        trans.grab_set()
        trans.focus()
        tla = Label(trans, text='transparency sacle')
        tla.pack(anchor=N)
        trant = IntVar()

        translider = Scale(trans, from_=0, to=10, variable=trant, orient='horizontal', command= lambda x: self.change_tran(trant.get()))
        translider.pack()
        trant.set(10)

    def get_color(self):
        self.window.transient(root)
        self.color = colorchooser.askcolor()
        self.window.lift()
        self.change_font(None)

    def bgcolors(self):
        self.window.transient(root)
        self.bgcolor = colorchooser.askcolor()
        self.window.lift()
        self.change_font(None)

    def change_font(self, event):
        bol = self.bolt.get()
        ita = self.italit.get()
        if self.maintext.tag_ranges('sel'):
            self.maintext.tag_add('colortag_' + str(self.tagcount), SEL_FIRST,SEL_LAST)
            if bol != 'None' and ita != 'None':
                self.maintext.tag_configure('colortag_' + str(self.tagcount), font=((str(self.fonts.get()).split()[0]), self.size.get(), bol, ita), foreground=self.color[1], background=self.bgcolor[1])
            elif bol != 'None':
                self.maintext.tag_configure('colortag_' + str(self.tagcount), font=((str(self.fonts.get()).split()[0]), self.size.get(), bol), foreground=self.color[1], background=self.bgcolor[1])
            elif ita != 'None':
                self.maintext.tag_configure('colortag_' + str(self.tagcount), font=((str(self.fonts.get()).split()[0]), self.size.get(), ita), foreground=self.color[1], background=self.bgcolor[1])
            else:
                self.maintext.tag_configure('colortag_' + str(self.tagcount), font=((str(self.fonts.get()).split()[0]), self.size.get()), foreground=self.color[1], background=self.bgcolor[1])

            self.tagcount += 1
            self.run()
            return
        else:
            for tag in self.maintext.tag_names():
                self.maintext.tag_delete(tag)
            if bol != 'None' and ita != 'None':
                self.maintext.config(font=((str(self.fonts.get()).split()[0]), self.size.get(), bol, ita), foreground=self.color[1], background=self.bgcolor[1])
            elif bol != 'None':
                self.maintext.config(font=((str(self.fonts.get()).split()[0]), self.size.get(), bol), foreground=self.color[1], background=self.bgcolor[1])
            elif ita != 'None':
                self.maintext.config(font=((str(self.fonts.get()).split()[0]), self.size.get(), ita), foreground=self.color[1], background=self.bgcolor[1])
            else:
                self.maintext.config(font=((str(self.fonts.get()).split()[0]), self.size.get()), foreground=self.color[1], background=self.bgcolor[1])
            self.run()
            return
    
    def pin_win(self, yes):
        self.window.attributes('-topmost', yes)


    def save_text(self):
        
        try:
            self.window.transient(root)
            savefile = filedialog.asksaveasfile(defaultextension='.txt', filetypes=(('plain text', '*.txt'), ('image files', '*.jpg'), ('image file2', '*.png')))
            self.window.lift()
            # self.main.update()
            # image = Image.open(self.main.postscript(file='canva.ps', colormode='color'))
            # image.save(savefile)
            
            savefile = str(savefile).split()[1]
            savefile = savefile.split("'")[1]
            if 'png' in savefile or 'jpg' in savefile:
                x=self.window.winfo_self.windowx()+self.maintext.winfo_x()
                y=self.window.winfo_self.windowy()+self.maintext.winfo_y()
                x1=x+self.maintext.winfo_width()
                y1=y+self.maintext.winfo_height()
                # print(list(savefile))

                ImageGrab.grab().crop((x,y+30,x1,y1+20)).save(savefile)
            elif 'txt' in savefile:
                info = self.maintext.get('1.0', END)
                with open(savefile, 'w') as file:
                    file.write(info)
                    file.close()
            else:
                return
        except IndexError:
            return




    def run(self):
        fontcolor = Button(self.Fone, text='color', bg=self.maintext['foreground'], foreground='white', command=self.get_color)
        fontcolor.grid(row=0, column=7)
        backcolor = Button(self.Fone, text='background', bg=self.maintext['bg'], command=self.bgcolors)
        backcolor.grid(row=0, column=8)
        saveb = Button(self.Fone, text='save', command=self.save_text)
        saveb.grid(row=0, column=9)




"""
Other
"""

def run_tools(tool):
    if tool == 'ba64':
        global BA64
        try:
            BA64.focus()#type: ignore
            BA64.lift()#type: ignore
            return
        except:
            pass
        BA64 = Toplevel(root)
        ba64en(BA64)
    elif tool == 'cal':
        global CAL
        try:
            CAL.focus()#type: ignore
            CAL.lift()#type: ignore
            return
        except:
            pass
        CAL = Toplevel(root)
        cal(CAL)
    elif tool == 'drbo':
        global DRBO
        try:
            DRBO.focus()#type: ignore
            DRBO.lift()#type: ignore
            return
        except:
            DRBO = Toplevel(root)
            drbo(DRBO)
    elif tool == 'nodc':
        global NODC
        try:
            NODC.focus()#type: ignore
            NODC.lift()#type: ignore
            return
        except:
            NODC = Toplevel(root)
            notedoc(NODC)







"""
Codes:
"""

root = Tk()
Zm(root)

APP_W = root.winfo_screenwidth()
APP_H = root.winfo_screenheight()

mainbook = XNotebook(root)
mainbook.pack()

main = Frame(mainbook, height=APP_H, width=APP_W, bg='white')
main.pack()
mainbook.add(main, text='       Main       ')

mainmenu = Menu(root)

tool = Menu(mainmenu, tearoff=0)
tool.add_command(label='Calculator', command=lambda: run_tools('cal'))
tool.add_command(label='Drawing board', command=lambda: run_tools('drbo'))
tool.add_command(label='Notes', command=lambda: run_tools('nodc'))
tool.add_command(label='Base64', command=lambda: run_tools('ba64'))
mainmenu.add_cascade(label='Tool', menu=tool)








root.config(menu=mainmenu)
root.mainloop()