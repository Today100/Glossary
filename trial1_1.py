import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms

import trial1
root = Tk()




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



def cp_text():
    cpane = Cp(root, 'Expanded', 'Collapsed')
    cpane.grid(row = 0, column = 0)

    # Button and checkbutton, these will
    # appear in collapsible pane container
    b1 = Button(cpane.frame, text ="GFG").grid(
                row = 1, column = 2, pady = 10)

    cb1 = Checkbutton(cpane.frame, text ="GFG").grid(
                    row = 2, column = 3, pady = 10)







def modify_table():
    global bone
    try:
        bone.destroy()# type: ignore
    except:
        pass
    bone = Toplevel()
    B7 = Button(bone, text="Create table", command=creat_table)
    B8 = Button(bone, text="Delete table", command=delete_table)
    B9 = Button(bone, text="Rename table", command=rename_table)
    B7.pack()
    B8.pack()
    B9.pack()


def creat_table():
    global bsix
    try:
        bsix.destroy()# type: ignore
    except:
        pass
    bsix = Toplevel()
    B19 = Button(bsix, text="Create basic table", command=basic_table)
    B20 = Button(bsix, text="Create advance table", command=advance_table)
    B19.grid(row=0, column=0, padx=3, pady=3)
    B20.grid(row=1, column=0, padx=3, pady=3)
    Tip(B19, text = 'Table that use basic search')
    Tip(B20, text = 'Table that use advance search')






def basic_table():
    global bseven
    try:
        bseven.destroy()#type: ignore
    except:
        pass
    bseven = Toplevel()
    l1 = Label(bseven, text="Please type in the table name")
    l2 = Label(bseven, text="        Please type in the column name")
    add = Button(bseven, text="+", command=add_to_listbox)
    global ask_new_name
    ask_new_name = Entry(bseven)
    global ask_column_name
    ask_column_name = Entry(bseven)
    global lis
    lis = Listbox(bseven)
    ask_column_name.bind('<Return>', add_to_listbox)
    bu = Button(bseven, text='get all', command=getall)
    
    
    l1.grid(row=0, column=0, columnspan=2)
    ask_new_name.grid(row=1, column=0, columnspan=2)
    l2.grid(row=2, column=0)
    Tip(l2, text="*No more column can be add after this")
    add.grid(row=3, column=1, padx=5)
    ask_column_name.grid(row=3, column=0, columnspan=2)
    lis.grid(row=4, column=0, columnspan=2)
    bu.grid(row=5, columnspan=2, padx=5, pady=5)
    #trial1.create_easy_search_table()

def getall():
    n = lis.get(0, END)

    x = list(n)
    p = ask_new_name.get()
    if not p:
        ms.showinfo("Popup", "You typed nothing")
        return
    trial1.create_easy_search_table(p, x)

    ask_new_name.delete(0, 'end')
    lis.delete(0, 'end')

def add_to_listbox(e=None):
    i = ask_column_name.get()
    if not i:
        ms.showinfo("Popup", "You typed nothing")
        return
    lis.insert(END, i)
    ask_column_name.delete(0, 'end')







def advance_table():
    global beight
    try:
        beight.destroy()#type: ignore
    except:
        pass
    beight = Toplevel()

    l1 = Label(beight, text='Please type the table name:')
    global ask_advance_table_name
    ask_advance_table_name = Entry(beight)
    l2 = Label(beight, text="Please enter the column name:")
    Tip(l2, text="You can leave it blank")
    global ask_advance_column_name
    ask_advance_column_name = Entry(beight)
    global lis_advance
    lis_advance = Listbox(beight)
    add = Button(beight, text="+", command=insert_list_advance)
    get = Button(beight, text="get all", command=get_advance)
    ask_advance_column_name.bind('<Return>', insert_list_advance)

    l1.grid(row=0, column=0, columnspan=2)
    ask_advance_table_name.grid(row=1, column=0, columnspan=2)
    l2.grid(row=2, column=0)
    
    add.grid(row=3, column=1, padx=5)
    ask_advance_column_name.grid(row=3, column=0, columnspan=2)
    lis_advance.grid(row=4, column=0, columnspan=2)
    get.grid(row=5, columnspan=2, padx=5, pady=5)

def get_advance():
    n = lis_advance.get(0, END)
    if n:
        x = list(n)
    else:
        x = n
    p = ask_advance_table_name.get()
    if not p:
        ms.showinfo("Popup", "You typed nothing for the table name")
        return
    if not x:
        trial1.create_table(p)
    else:
        trial1.create_table(p)
        trial1.add_column(p, x)

    ask_advance_table_name.delete(0, 'end')
    lis_advance.delete(0, 'end')

def insert_list_advance(e=None):
    i = ask_advance_column_name.get()
    if not i:
        return
    lis_advance.insert(END, i)
    ask_advance_column_name.delete(0, 'end')






def delete_table():
    global bnine
    try:
        bnine.destroy()#type: ignore
    except:
        pass
    bnine = Toplevel()
    global search_entry_for_delete_table
    search_entry_for_delete_table = Entry(bnine)
    global search_list_box_for_delete_table
    search_list_box_for_delete_table = Listbox(bnine)
    search_list_box_for_delete_table.bind('<<ListboxSelect>>', fillout)
    search_entry_for_delete_table.bind('<KeyRelease>', check)
    delete_button = Button(bnine, text='Delete', command=delete_table2)

    delete_button.grid(row=3, columnspan=2, padx=5, pady=5)
    search_entry_for_delete_table.grid(row=0, columnspan=2, padx=5, pady=5)
    search_list_box_for_delete_table.grid(row=1, columnspan=2, padx=5, pady=5)
    data1 = trial1.show_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        data.append(i)
    
    update(data)

def delete_table2():
    n = search_entry_for_delete_table.get()
    trial1.delete_table(n)
    data1 = trial1.show_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        data.append(i)
    update(data)
    bnine.lift()
    ms.showinfo("Popup", "Table has been successfully deleted.")
    bnine.lift()
    search_entry_for_delete_table.delete(0, END)

def check(e):
    typed = search_entry_for_delete_table.get()
    if typed == '':
        data1 = trial1.show_table()
        data1 = list(data1)
        data = []
        for i in data1:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            # i = i.replace('(','')
            # i = i.replace(')','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            data.append(i)
    else:
        data = []
        n = trial1.show_table()
        n = list(n)
        for i in n:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            if typed.lower() in i.lower():
                data.append(i)
    update(data)

def update(data):
    search_list_box_for_delete_table.delete(0, END)
    #data = trial1.show_table()search_list_box_for_delete_table.delete(0, END)
    for item in data:
        search_list_box_for_delete_table.insert(END, item)

def fillout(e):
    search_entry_for_delete_table.delete(0, END)
    search_entry_for_delete_table.insert(0, search_list_box_for_delete_table.get(ANCHOR))






def rename_table():
    global bnine
    try:
        bnine.destroy()#type: ignore
    except:
        pass
    bnine = Toplevel()
    global search_entry_for_delete_table
    search_entry_for_delete_table = Entry(bnine)
    global search_list_box_for_delete_table
    search_list_box_for_delete_table = Listbox(bnine)
    search_list_box_for_delete_table.bind('<<ListboxSelect>>', fillout9)
    search_entry_for_delete_table.bind('<KeyRelease>', check9)
    rename_button = Button(bnine, text='Rename', command=rename_table2)
    rename_lable = Label(bnine, text='Please type the new name below:')
    global rename_box
    rename_box = Entry(bnine)

    rename_button.grid(row=5, columnspan=2, padx=5, pady=5)
    search_entry_for_delete_table.grid(row=0, columnspan=2, padx=5, pady=5)
    search_list_box_for_delete_table.grid(row=1, columnspan=2, padx=5, pady=5)
    rename_lable.grid(row=3, columnspan=2, padx=3, pady=3)
    rename_box.grid(row=4, columnspan=2, padx=5, pady=5)
    data1 = trial1.show_not_virtual_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        
        data.append(i)
    update9(data)

def rename_table2():
    n = search_entry_for_delete_table.get()
    n2 = rename_box.get()
    if not n2:
        ms.showinfo("Popup", 'New name can not be blank')
        return
    trial1.rename_table(n, n2)
    data1 = trial1.show_not_virtual_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        
        data.append(i)
    update(data)
    search_entry_for_delete_table.delete(0, END)
    rename_box.delete(0, END)
    bnine.lift()
    ms.showinfo("Popup", "Table has been successfully renamed.")
    bnine.lift()



def check9(e):
    typed = search_entry_for_delete_table.get()
    if typed == '':
        data1 = trial1.show_not_virtual_table()
        data1 = list(data1)
        data = []
        for i in data1:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            # i = i.replace('(','')
            # i = i.replace(')','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            
            data.append(i)
        
    else:
        data = []
        n = trial1.show_not_virtual_table()
        n = list(n)
        for i in n:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            if typed.lower() in i.lower():
                data.append(i)
    update9(data)

def update9(data):
    search_list_box_for_delete_table.delete(0, END)
    #data = trial1.show_table()search_list_box_for_delete_table.delete(0, END)
    for item in data:
        search_list_box_for_delete_table.insert(END, item)

def fillout9(e):
    search_entry_for_delete_table.delete(0, END)
    search_entry_for_delete_table.insert(0, search_list_box_for_delete_table.get(ANCHOR))














def modify_column():
    global btwo
    try:
        btwo.destroy()# type: ignore
    except:
        pass
    btwo = Toplevel()
    B10 = Button(btwo, text="Add column to table", command=add_column)
    B11 = Button(btwo, text="Delete column from table", command=delete_column)
    B21 = Button(btwo, text='Rename column from table', command=rename_column)
    B10.pack()
    B11.pack()
    B21.pack()




def add_column():
    global bten
    try:
        bten.destroy() #type: ignore
    except:
        pass
    bten = Toplevel()

    add_column_lable1 = Label(bten, text='Please enter the table')
    global add_column_entry1
    add_column_entry1 = Entry(bten)
    add_column_lable2 = Label(bten, text='Please enter the new column name:')
    global add_column_entry2
    add_column_entry2 = Entry(bten)
    global listbox1
    listbox1 = Listbox(bten)
    global listbox2
    listbox2 = Listbox(bten)
    space1 = Label(bten)
    add_column_lable3 = Label(bten, text='Below is the columns the table have')

    add_b = Button(bten, text="Add", command=add_column3)


    add_column_lable1.grid(row=0, column=0)
    add_column_entry1.grid(row=1, column=0)
    add_column_lable2.grid(row=3, column=0)
    add_column_entry2.grid(row=4, column=0)
    add_column_lable3.grid(row=6, column=0)
    listbox1.grid(row=2, column=0)
    space1.grid(row=5)
    listbox2.grid(row=7, column=0)
    Tip(add_column_entry2, text = 'The none column will be deleted\nafter you add new column to advance table')
    add_b.grid(row=8, column=0)

    global add_column_pylist
    add_column_pylist = []

    add_column_entry1.bind("<1>", insert_listbox2)
    #add_column_entry2.bind("<1>", insert_listbox2)
    add_column_entry2.bind("<Return>", add_column2)
    listbox1.bind('<<ListboxSelect>>', fillout2)
    add_column_entry1.bind('<KeyRelease>', check2)
    data1 = trial1.show_not_virtual_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        
        data.append(i)
    update2(data)


def add_column2(e=None):
    listbox2.insert(END, add_column_entry2.get())
    add_column_pylist.append(add_column_entry2.get())
    add_column_entry2.delete(0, END)

def add_column3(e=None):
    n = add_column_entry1.get()
    ls = add_column_pylist
    
    trial1.add_column(n, ls)
    ms.showinfo("Popup", "Column has been successfully added!")
    add_column_pylist.clear()
    bten.lift()






def delete_column():
    global bten
    try:
        bten.destroy() #type: ignore
    except:
        pass
    bten = Toplevel()

    add_column_lable1 = Label(bten, text='Please enter the table')
    global add_column_entry1
    add_column_entry1 = Entry(bten)
    add_column_lable2 = Label(bten, text='Select the column you want to delete:')

    global listbox1
    listbox1 = Listbox(bten)
    global listbox2
    listbox2 = Listbox(bten, selectmode=EXTENDED)
    space1 = Label(bten)
    add_column_lable3 = Label(bten, text='Below is the columns the table have')

    delete_b = Button(bten, text="Delete", command=delete_column2)


    add_column_lable1.grid(row=0, column=0)
    add_column_entry1.grid(row=1, column=0)
    add_column_lable2.grid(row=3, column=0)

    add_column_lable3.grid(row=5, column=0)
    listbox1.grid(row=2, column=0)
    space1.grid(row=4)
    listbox2.grid(row=6, column=0)
    delete_b.grid(row=7, column=0)

    global delete_column_pylist
    delete_column_pylist = []

    add_column_entry1.bind("<1>", insert_listbox2)
    #add_column_entry2.bind("<1>", insert_listbox2)
    listbox1.bind('<<ListboxSelect>>', fillout2)
    add_column_entry1.bind('<KeyRelease>', check2)
    data1 = trial1.show_not_virtual_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        
        data.append(i)
    update2(data)

def delete_column2():
    delete_column_pylist.clear()
    for i in listbox2.curselection():
        delete_column_pylist.append(listbox2.get(i))
    ls = delete_column_pylist
    n = add_column_entry1.get()
    trial1.delete_column(n, ls)
    insert_listbox2()
    ms.showinfo("Popup", "Column has been successfully deleted!")
    delete_column_pylist.clear()
    bten.lift()



def rename_column():
    global bten
    try:
        bten.destroy() #type: ignore
    except:
        pass
    bten = Toplevel()

    add_column_lable1 = Label(bten, text='Please enter the table')
    global add_column_entry1
    add_column_entry1 = Entry(bten)
    add_column_lable2 = Label(bten, text='Please enter the new column name:')
    global add_column_entry2
    add_column_entry2 = Entry(bten)
    global listbox1
    listbox1 = Listbox(bten)
    global listbox2
    listbox2 = Listbox(bten)
    space1 = Label(bten)
    add_column_lable3 = Label(bten, text='Below is the columns the table have\nPlease select one:')

    rename_b = Button(bten, text="Rename", command=rename_column2)


    add_column_lable1.grid(row=0, column=0)
    add_column_entry1.grid(row=1, column=0)
    add_column_lable2.grid(row=6, column=0)
    add_column_entry2.grid(row=7, column=0)
    add_column_lable3.grid(row=4, column=0)
    listbox1.grid(row=2, column=0)
    space1.grid(row=3)
    listbox2.grid(row=5, column=0)
    rename_b.grid(row=8, column=0)


    add_column_entry1.bind("<1>", insert_listbox2)
    #add_column_entry2.bind("<1>", insert_listbox2)
    add_column_entry2.bind("<Return>", add_column2)
    listbox1.bind('<<ListboxSelect>>', fillout2)
    add_column_entry1.bind('<KeyRelease>', check2)
    data1 = trial1.show_not_virtual_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        
        data.append(i)
    update2(data)

def rename_column2():
    t = add_column_entry1.get()
    c = listbox2.get(ANCHOR)
    new = add_column_entry2.get()
    trial1.update_column_name(t, c, new)
    add_column_entry2.delete(0, END)
    insert_listbox2()
    ms.showinfo("Popup", "Column has been successfully renamed!")
    bten.lift()




def check2(e):
    typed = add_column_entry1.get()
    if typed == '':
        data1 = trial1.show_not_virtual_table()
        data1 = list(data1)
        data = []
        for i in data1:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            # i = i.replace('(','')
            # i = i.replace(')','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
        
        data.append(i)
    else:
        data = []
        n = trial1.show_not_virtual_table()
        n = list(n)
        for i in n:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            if typed.lower() in i.lower():
                data.append(i)
    update2(data)

def fillout2(e):
    add_column_entry1.delete(0, END)
    add_column_entry1.insert(0, listbox1.get(ANCHOR))
    insert_listbox2()

def update2(data):
    listbox1.delete(0, END)
    #data = trial1.show_table()search_list_box_for_delete_table.delete(0, END)
    for item in data:
        listbox1.insert(END, item)

def insert_listbox2(e=None):
    listbox2.delete(0, END)
    n = add_column_entry1.get()
    p = listbox1.get(ANCHOR)
    
    x = trial1.get_column_name(n)

    for item in x:
        listbox2.insert(END, item)


















def modify_infos():
    global bthree
    try:
        bthree.destroy()# type: ignore
    except:
        pass
    bthree = Toplevel()
    B12 = Button(bthree, text="Add info", command=add_info)
    B13 = Button(bthree, text="Delete info", command=delete_info)
    B22 = Button(bthree, text="Update info", command=update_info)
    B12.pack()
    B13.pack()
    B22.pack()




def add_info():
    global beleven
    try:
        beleven.destory()#type: ignore
    except:
        pass
    beleven = Toplevel()
    global info_entry1
    global info_listbox1
    info_entry1 = Entry(beleven)
    info_listbox1 = Listbox(beleven)
    info_entry1_get = Button(beleven, text='Select')

    info_entry1.grid(row=0, columnspan=6)
    info_listbox1.grid(row=1, columnspan=6)
    info_entry1_get.grid(row=2, columnspan=6)
    info_listbox1.bind('<<ListboxSelect>>', fillout3)
    info_entry1.bind('<KeyRelease>', check3)
    info_entry1_get.bind('<1>', select_table)
    data1 = trial1.show_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        data.append(i)
    update3(data)
    global co
    global inco
    
    co = []
    inco = []
    try:
        for col in co:
            col.destroy()
        for inf in inco:
            inf.destroy()
        
        co.clear()
        inco.clear()
        
    except:
        pass
    
def select_table(e=None):
    
    try:
        for col in co:
            col.destroy()
        for inf in inco:
            inf.destroy()
        
        co.clear()
        inco.clear()
        
    except:
        pass

    n = info_entry1.get()
    k = trial1.column_number(n)
    f = trial1.get_column_name(n)
    x = k - 1
    count = 3
    count2 = 0
    # for i in range(1,k):
    for ins in f:
        column_name = Label(beleven, text=ins)
        info_column = Entry(beleven)
        column_name.grid(row=count, column=count2, padx=3, pady=3)
        count2 += 1
        info_column.grid(row=count, column=count2, padx=3, pady=3)
    
        co.append(column_name)
        inco.append(info_column)
        
        count2 += 1
        if count2 == 6:
            count += 1
            count2 = 0
    global add_info_b
    try:
        add_info_b.destroy()#type: ignore
    except:
        pass
    add_info_b = Button(beleven, text="Add all", command=add_info2)
    add_info_b.grid(row=count+1, columnspan=6, padx=5, pady=5)

def add_info2():
    k = []
    for inf in inco:
            n = inf.get()
            k.append(n)
    x = info_entry1.get()
    
    trial1.insert_info(x, k)
    ms.showinfo("Popup", "Info has been succesfully added")
    
    for i in inco:
        i.delete(0, END)






def delete_info():
    global beighteen
    try:
        beighteen.destory()#type: ignore
    except:
        pass
    beighteen = Toplevel()

    dinfo_la1 = Label(beighteen, text='Please select the table')
    global dinfo_e1
    dinfo_e1 = Entry(beighteen)
    global dinfo_li1
    dinfo_li1 = Listbox(beighteen)
    dinfo_b1 = Button(beighteen, text='Select', command=delete_info1)

    dinfo_la1.grid(row=0, column=0, padx=5, pady=5)
    dinfo_e1.grid(row=1, column=0, padx=5, pady=5)
    dinfo_li1.grid(row=2, column=0, padx=5, pady=5)
    dinfo_b1.grid(row=3, column=0, padx=5, pady=5)

    dinfo_li1.bind('<<ListboxSelect>>', fillout10)
    dinfo_e1.bind('<KeyRelease>', check10)

    data1 = trial1.show_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        data.append(i)
    update10(data)

def delete_info1():
    dinfo_op1 = trial1.show_table_info(dinfo_e1.get())
    dinfo_op = []
    for x in dinfo_op1:
        dinfo_op.append(x[0])
    dinfo_la2 = Label(beighteen, text='Please enter the id')
    global dinfo_cb
    dinfo_cb = ttk.Combobox(beighteen, value=dinfo_op)
    dinfo_b2 = Button(beighteen, text='Delete', command=delete_info2)


    dinfo_la2.grid(row=4, column=0, padx=5, pady=5)
    dinfo_cb.grid(row=5, column=0, padx=5, pady=5)
    dinfo_b2.grid(row=6, column=0, padx=5, pady=5)

def delete_info2():
    n = trial1.delete_info(dinfo_e1.get(), dinfo_cb.get())
    dinfo_cb.delete(0, END)
    ms.showinfo("Popup", 'Info has been succesfully deleted!')






def check10(e):
    typed = dinfo_e1.get()
    if typed == '':
        data1 = trial1.show_table()
        data1 = list(data1)
        data = []
        for i in data1:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            # i = i.replace('(','')
            # i = i.replace(')','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            data.append(i)
    else:
        data = []
        n = trial1.show_table()
        n = list(n)
        for i in n:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            if typed.lower() in i.lower():
                data.append(i)
    update10(data)

def fillout10(e):
    dinfo_e1.delete(0, END)
    dinfo_e1.insert(0, dinfo_li1.get(ANCHOR))

def update10(data):
    dinfo_li1.delete(0, END)
    #data = trial1.show_table()search_list_box_for_delete_table.delete(0, END)
    for item in data:
        dinfo_li1.insert(END, item)


























def update_info():
    global bfourteen
    try:
        bfourteen.destroy()#type: ignore
    except:
        pass
    bfourteen = Toplevel()

    update_label1 = Label(bfourteen, text='Please enter the table name:')
    global update_entry1
    update_entry1 = Entry(bfourteen)
    update_label2 = Label(bfourteen, text='\nPlease enter the id:')
    global update_entry2
    update_entry2 = Entry(bfourteen)
    global update_list
    update_list = Listbox(bfourteen)
    update_select_button = Button(bfourteen, text='Select', command=update_info1)

    update_label1.grid(row=0, column=0)
    update_entry1.grid(row=1, column=0)
    update_label2.grid(row=3, column=0)
    update_entry2.grid(row=4, column=0)
    update_list.grid(row=2, column=0)
    update_select_button.grid(row=5, column=0)
    
    update_list.bind("<<ListboxSelect>>", fillout5)
    update_entry1.bind("<KeyRelease>", check5)
    data1 = trial1.show_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        data.append(i)
    update5(data)

def update_info1():
    n = update_entry2.get()
    try:
        n = int(n)
    except:
        ms.showerror("Popup", 'You did not type a correct id')
        update_info()
        return

    n = str(n)
    p = trial1.select_info_with_rowid(update_entry1.get(), n)
    global bfifteen
    try:
        bfifteen.destroy()#type: ignore
    except:
        pass
    bfifteen = Toplevel()
    f = trial1.column_number(update_entry1.get())
    x = trial1.get_column_name(update_entry1.get())
    count = 0
    count2 = 0
    co2 = []
    global inco2
    inco2 = []
    for ins in x:
        column_name2 = Label(bfifteen, text=ins)
        info_column2 = Entry(bfifteen)
        column_name2.grid(row=count, column=0, padx=3, pady=3)
        
        info_column2.grid(row=count, column=1, padx=3, pady=3)
        count += 1
        co2.append(column_name2)
        inco2.append(info_column2)
    
    update_button = Button(bfifteen, text='Update', command = update_info2)
    update_button.grid(row=count, columnspan=2)
    for en in inco2:
        en.insert(0, p[0][count2])
        count2 += 1
    
def update_info2():
    lis = []
    for x in inco2:
        lis.append(x.get())
    trial1.update_info(update_entry1.get(), lis, update_entry2.get())
    bfifteen.destroy()
    ms.showinfo("Popup", "Your info has been succesfully updated!")







def check3(e):
    typed = info_entry1.get()
    if typed == '':
        data1 = trial1.show_table()
        data1 = list(data1)
        data = []
        for i in data1:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            # i = i.replace('(','')
            # i = i.replace(')','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            data.append(i)
    else:
        data = []
        n = trial1.show_table()
        n = list(n)
        for i in n:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            if typed.lower() in i.lower():
                data.append(i)
    update3(data)

def fillout3(e):
    info_entry1.delete(0, END)
    info_entry1.insert(0, info_listbox1.get(ANCHOR))

def update3(data):
    info_listbox1.delete(0, END)
    #data = trial1.show_table()search_list_box_for_delete_table.delete(0, END)
    for item in data:
        info_listbox1.insert(END, item)





def check5(e):
    typed = update_entry1.get()
    if typed == '':
        data1 = trial1.show_table()
        data1 = list(data1)
        data = []
        for i in data1:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            # i = i.replace('(','')
            # i = i.replace(')','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            data.append(i)
    else:
        data = []
        n = trial1.show_table()
        n = list(n)
        for i in n:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            if typed.lower() in i.lower():
                data.append(i)
    update5(data)

def fillout5(e):
    update_entry1.delete(0, END)
    update_entry1.insert(0, update_list.get(ANCHOR))

def update5(data):
    update_list.delete(0, END)
    #data = trial1.show_table()search_list_box_for_delete_table.delete(0, END)
    for item in data:
        update_list.insert(END, item)






















def show():
    global bfour
    try:
        bfour.destroy()# type: ignore
    except:
        pass
    bfour = Toplevel()
    B14 = Button(bfour, text="Show all table", command=show_all_table)
    B15 = Button(bfour, text="Show basic table", command=show_basic_table)
    B23 = Button(bfour, text="Show advance table", command=show_advance_table)
    B24 = Button(bfour, text="Show table info", command=show_info)
    # B25 = Button(bfour, text='Treeview', command=treeview_list1)
    B14.pack()
    B15.pack()
    B23.pack()
    B24.pack()
    # B25.pack()

def show_all_table():
    global btwelve
    try:
        btwelve.destroy()#type: ignore
    except:
        pass
    btwelve = Toplevel()
    data1 = trial1.show_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        data.append(i)
    li = Listbox(btwelve)
    for i in data:
        li.insert(END, i)
    li.pack()


def show_basic_table():
    global btwelve
    try:
        btwelve.destroy()#type: ignore
    except:
        pass
    btwelve = Toplevel()
    data1 = trial1.show_virtual_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        
        data.append(i)
    li = Listbox(btwelve)
    for i in data:
        li.insert(END, i)
    li.pack()


def show_advance_table():
    global btwelve
    try:
        btwelve.destroy()#type: ignore
    except:
        pass
    btwelve = Toplevel()
    data1 = trial1.show_not_virtual_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        
        data.append(i)
    li = Listbox(btwelve)
    for i in data:
        li.insert(END, i)
    li.pack()




def show_info():
    global bthirteen
    try:
        bthirteen.destory()#type: ignore
    except:
        pass
    bthirteen = Toplevel()
    global show_entry1
    global show_listbox1
    show_entry1 = Entry(bthirteen)
    show_listbox1 = Listbox(bthirteen)
    show_entry1_get = Button(bthirteen, text='Show info', command=show_info2)

    show_entry1.grid(row=0, columnspan=6)
    show_listbox1.grid(row=1, columnspan=6)
    show_entry1_get.grid(row=2, columnspan=6)
    show_listbox1.bind('<<ListboxSelect>>', fillout4)
    show_entry1.bind('<KeyRelease>', check4)
    data1 = trial1.show_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        data.append(i)
    
    update4(data)

def show_info2(n=None):
    n = show_entry1.get()
    k = trial1.show_table_info(n)
    treeview_list(n)






def check4(e):
    typed = show_entry1.get()
    if typed == '':
        data1 = trial1.show_table()
        data1 = list(data1)
        data = []
        for i in data1:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            # i = i.replace('(','')
            # i = i.replace(')','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            data.append(i)
    else:
        data = []
        n = trial1.show_table()
        n = list(n)
        for i in n:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            if typed.lower() in i.lower():
                data.append(i)
    update4(data)

def fillout4(e):
    show_entry1.delete(0, END)
    show_entry1.insert(0, show_listbox1.get(ANCHOR))

def update4(data):
    show_listbox1.delete(0, END)
    #data = trial1.show_table()search_list_box_for_delete_table.delete(0, END)
    for item in data:
        show_listbox1.insert(END, item)




def treeview_list(t): 
    #table name, column many number, column name, info

    c = trial1.column_number(t)
    cn = trial1.get_column_name(t)
    i = trial1.show_table_info(t)

    b = Toplevel()
    l = ['id']
    count=0
    for x in range(1,c):
        st = 'c' + str(x)
        l.append(st)

    tree = ttk.Treeview(b, column=(l), show='headings')

    tree.column('id', anchor=CENTER, minwidth=2, width=20)
    tree.heading('id', text='id')
    
    for x in range(2,c+1):
        tree.column('#' + str(x), anchor=CENTER, minwidth=2, width=100)
        tree.heading('#'+str(x), text=cn[count])
        count += 1

    for ii in i:
        tree.insert("", END, values=ii)


    tree.pack()










def search():
    global bfive
    try:
        bfive.destroy()#type: ignore
    except:
        pass
    bfive = Toplevel()
    B16 = Button(bfive, text="Search table", command=search_table)
    B17 = Button(bfive, text="Advance table info search", command=advance_table_search)
    B18 = Button(bfive, text="Basic table info search", command=basic_table_search)
    B16.pack()
    B17.pack()
    B18.pack()

def search_table():
    pass

def advance_table_search():
    global bsixteen
    try:
        bsixteen.destroy()#type: ignore
    except:
        pass
    bsixteen = Toplevel()
    global advance_e1, advance_li1, advance_b1
    advance_la1 = Label(bsixteen, text='Please enter the table name:')
    advance_e1 = Entry(bsixteen)
    advance_li1 = Listbox(bsixteen)
    advance_b1 = Button(bsixteen, text='Next', command=advance_table_search1)

    advance_la1.grid(row=0, column=0)
    advance_e1.grid(row=1, column=0)
    advance_li1.grid(row=2, column=0)
    advance_b1.grid(row=3, column=0)

    advance_li1.bind('<<ListboxSelect>>', fillout6)
    advance_e1.bind('<KeyRelease>', check6)
    advance_e1.bind("<Return>", advance_table_search1)
    advance_li1.bind("<Return>", advance_table_search1)

    data1 = trial1.show_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        data.append(i)
    update6(data)


def advance_table_search1(n=None):
    global advance_op1
    try:
        advance_op1.destroy()#type: ignore
    except:
        pass
    lt = trial1.get_column_name(advance_e1.get())
    advance_la2 = Label(bsixteen, text='Please enter the criteria:')
    global column
    column = StringVar()
    advance_op1 = OptionMenu(bsixteen, column, *lt, command=advance_table_search2)
    advance_la2.grid(row=4, column=0)
    advance_op1.grid(row=5, column=0)
    # column.set(lt[0])
    # advance_table_search2(None)

def advance_table_search2(c):
    advance_la3 = Label(bsixteen, text='Pleaser enter the info you want to search:')
    global advance_e2
    advance_e2 = Entry(bsixteen)
    advance_b2 = Button(bsixteen, text='Search', command = advance_table_search3)
    advance_la3.grid(row=6, column=0)
    advance_e2.grid(row=7, column=0)
    advance_b2.grid(row=8, column=0)

def advance_table_search3():
    a = trial1.advance_search_in_table(advance_e1.get(), column.get(), advance_e2.get())
    treeview_list1(advance_e1.get(), a)
    



def basic_table_search():
    global bseventeen
    try:
        bseventeen.destory()#type: ignore
    except:
        pass
    bseventeen = Toplevel()
    global basic_e1, basic_li1
    basic_la1 = Label(bseventeen, text='Please enter the table name:')
    basic_e1 = Entry(bseventeen)
    basic_li1 = Listbox(bseventeen)
    basic_b1 = Button(bseventeen, text='Select', command=basic_table_search1)

    basic_la1.grid(row=0, column=0)
    basic_e1.grid(row=1, column=0)
    basic_li1.grid(row=2, column=0)
    basic_b1.grid(row=3, column=0)

    basic_li1.bind('<<ListboxSelect>>', fillout7)
    basic_e1.bind('<KeyRelease>', check7)
    
    data1 = trial1.show_virtual_table()
    data1 = list(data1)
    data = []
    for i in data1:
        i = str(i)
        i = i.replace('(\'', '')
        i = i.replace('\',)','')
        # i = i.replace('(','')
        # i = i.replace(')','')
        i = i.replace('(\"', '')
        i = i.replace('\",)','')
        i = i.replace('{', '')
        i = i.replace('{', '')
        i = str(i)
        
        data.append(i)
    update7(data)

def basic_table_search1():
    global tree1
    try:
        tree1.destroy()
    except:
        pass
    basic_la2 = Label(bseventeen, text='Please enter the info:')
    global basic_e2
    basic_e2 = Entry(bseventeen)

    
    basic_la2.grid(row=4, column=0)
    basic_e2.grid(row=5, column=0)
    
    basic_e2.bind('<KeyRelease>', check8)
    
    treeview_list2(basic_e1.get())




def treeview_list2(t): 
    #table name, column many number, column name, info

    global tree1

    c = trial1.column_number(t)
    cn = trial1.get_column_name(t)
    i = trial1.show_table_info(t)

    
    l = ['id']
    count=0
    for x in range(1,c):
        st = 'c' + str(x)
        l.append(st)

    tree1 = ttk.Treeview(bseventeen, column=(l), show='headings')

    tree1.column('id', anchor=CENTER, minwidth=2, width=20)
    tree1.heading('id', text='id')
    
    for x in range(2,c+1):
        tree1.column('#' + str(x), anchor=CENTER, minwidth=2, width=100)
        tree1.heading('#'+str(x), text=cn[count])
        count += 1

    for ii in i:
        tree1.insert("", END, values=ii)


    tree1.grid(stick='s')
    update8(i)





def treeview_list1(t, i): 
    #table name, info

    c = trial1.column_number(t)
    cn = trial1.get_column_name(t)
    

    b = Toplevel()
    l = ['id']
    count=0
    for x in range(1,c):
        st = 'c' + str(x)
        l.append(st)

    tree = ttk.Treeview(b, column=(l), show='headings')

    tree.column('id', anchor=CENTER, minwidth=2, width=20)
    tree.heading('id', text='id')
    
    for x in range(2,c+1):
        tree.column('#' + str(x), anchor=CENTER, minwidth=2, width=100)
        tree.heading('#'+str(x), text=cn[count])
        count += 1

    for ii in i:
        tree.insert("", END, values=ii)


    tree.pack()










def check6(e):
    typed = advance_e1.get()
    if typed == '':
        data1 = trial1.show_table()
        data1 = list(data1)
        data = []
        for i in data1:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            # i = i.replace('(','')
            # i = i.replace(')','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            data.append(i)
    else:
        data = []
        n = trial1.show_table()
        n = list(n)
        for i in n:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            if typed.lower() in i.lower():
                data.append(i)
    update6(data)

def fillout6(e):
    advance_e1.delete(0, END)
    advance_e1.insert(0, advance_li1.get(ANCHOR))

def update6(data):
    advance_li1.delete(0, END)
    #data = trial1.show_table()search_list_box_for_delete_table.delete(0, END)
    for item in data:
        advance_li1.insert(END, item)





def check7(e):
    typed = basic_e1.get()
    if typed == '':
        data1 = trial1.show_virtual_table()
        data1 = list(data1)
        data = []
        for i in data1:
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            # i = i.replace('(','')
            # i = i.replace(')','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            
            data.append(i)
    else:
        data = []
        n = trial1.show_virtual_table()
        
        for i in n:
            
            i = str(i)
            i = i.replace('(\'', '')
            i = i.replace('\',)','')
            i = i.replace('(\"', '')
            i = i.replace('\",)','')
            i = i.replace('{', '')
            i = i.replace('{', '')
            i = str(i)
            if typed.lower() in i.lower():
                data.append(i)
    
    update7(data)

def fillout7(e):
    basic_e1.delete(0, END)
    basic_e1.insert(0, basic_li1.get(ANCHOR))

def update7(data):
    basic_li1.delete(0, END)
    #data = trial1.show_table()search_list_box_for_delete_table.delete(0, END)
    for item in data:
        # for item in item:
        basic_li1.insert(END, item)





def check8(e):
    typed = basic_e2.get()
    if typed == '':
        data = trial1.show_table_info(basic_e1.get())
    else:
        data = trial1.basic_search(basic_e1.get(), basic_e2.get())
        # data = []
        # n = trial1.show_table_info(basic_e1.get())
        # n = list(n)
        # for i in n:
        #     i = str(i)
        #     i = i.replace('(\'', '')
        #     i = i.replace('\',)','')
        #     i = str(i)
        #     if typed.lower() in i.lower():
        #         data.append(i)
    update8(data)

# def fillout8(e):
#     advance_e1.delete(0, END)
#     advance_e1.insert(0, advance_li1.get(ANCHOR))

def update8(data):
    # advance_li1.delete(0, END)
    tree1.delete(*tree1.get_children())
    #data = trial1.show_table()search_list_box_for_delete_table.delete(0, END)
    for item in data:
        tree1.insert("", END, values=item)


























def endi():
    root.destroy()



B1 = Button(root, text="Modifying tables", command=modify_table)
B2 = Button(root, text="Modifying columns", command=modify_column)
B3 = Button(root, text="Modifying infos", command=modify_infos)
B4 = Button(root, text="Show", command=show)
B5 = Button(root, text="Search", command=search)
B6 = Button(root, text="Exit", command=endi)

B1.grid(sticky="nsew", padx=5, pady=1)
B2.grid(sticky="nsew", padx=5, pady=1)
B3.grid(sticky="nsew", padx=5, pady=1)
B4.grid(sticky="nsew", padx=5, pady=1)
B5.grid(sticky="nsew", padx=5, pady=1)
B6.grid(row=5,column=0)





root.mainloop()