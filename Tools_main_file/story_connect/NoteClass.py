from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from django.conf import settings

import pandas as pd
import random
import sqlite3

import json
import os





def open_note(path):
    note_window = Toplevel()
    print(path)
    NoteClass(note_window, path[0], json.loads(str(path[1])))

    
    





class NoteClass():
    def __init__(self, window, NoteText, ChoosedWords, openDoc=False):
        self.root = window
        self.root.geometry("+360+100")

        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()

        self.setting = json.load(open("E:\\1.Python_f\\Glossory\\Tools_main_file\\story_connect\\setting.json"))

        
        self.checkdatabase()

        self.main_m = Menu(self.root)
        self.syst_m = Menu(self.main_m, tearoff=0)
        self.note_m = Menu(self.main_m, tearoff=0)

        self.main_m.add_cascade(label="main", menu=self.syst_m)
        self.main_m.add_cascade(label="notes", menu=self.note_m)


        self.m = Menu(self.root, tearoff = 0)
        self.m.add_separator()
        self.m.add_separator()
        self.m.add_command(label ="Get Synonyms")
        self.m.add_command(label ="Get Chinese Explaination")

        self.root.config(menu=self.main_m)

                
        self.root.bind("<Control-s>", self.save)

        self.root.bind("<Control-Shift-P>", self.syslook)
        self.syst_m.add_command(label="Preference", command=self.syslook)

        

        self.NoteText = NoteText
        self.choosed = ChoosedWords

        self.after()
        self.run()
        self.note_load()

    def checkdatabase(self):
        print("running")
        
        if self.setting["established database"]:
            self.conn = sqlite3.connect(self.setting["database path"])
            self.c = self.conn.cursor()
        
        elif not self.setting["established database"]:
            database_path = os.path.join(os.path.dirname(__file__), "MainStoryFiles.db")
            self.conn = sqlite3.connect(database_path)
            self.c = self.conn.cursor()
            self.setting["database path"] = database_path
        
            self.setting["established database"] = True

            # Remember to think about a backup database
            self.set_up_table()
            self.du()
        
    
    def set_up_table(self):
        print("running")
        self.c.execute("""CREATE TABLE MainTable (  name TEXT type UNIQUE,
                                                    path TEXT type UNIQUE,
                                                    vocab TEXT)""")
        self.conn.commit()


    def du(self, e=None):         #Dump
        write_file = open("E:\\1.Python_f\\Glossory\\Tools_main_file\\story_connect\\setting.json", "w")
        json.dump(self.setting, write_file, indent=4, separators=(", \n", " : "))

    def note_load(self):
        self.c.execute("SELECT rowid, * FROM [MainTable]")
        items = self.c.fetchall()
        # print(items)
        self.conn.commit()

        # items = json.loads(items)

        for item in items:
            self.note_m.add_command(label=item[1], command=lambda path = item[2:]: open_note(path))
        for note, path in self.setting["names"].items():
            self.note_m.add_command(label=note, command=lambda path = path: open_note(path))


    def get_dic_v(self):
        dic_v = self.dic_v_path

    def change_scale_color(self, e):
        if self.save_var.get():
            self.save_scale["bg"] = "green"
        else:
            self.save_scale["bg"] = "red"
        self.save_scale["label"] = str(self.save_var.get())
        self.setting["save_setting"] = self.save_var.get()
        # print(str(save_var.get()))
        
    def change_button(self, e=None):
        if self.check_b["text"] == "Yes":
            # print(check_b)
            self.check_b["text"] = "No"
            self.setting["check_setting"] = "No"
        else:
            self.check_b["text"] = "Yes"
            self.setting["check_setting"] = "Yes"


    def change_voc_num(self, e=None):             #Change generate vocabulary number
        if int(self.voc_spin.get()) > 20 or int(self.voc_spin.get()) < 1:
            return
        else:
            # print(voc_spin.get())
            self.setting["total_voc"] = int(self.voc_spin.get())
        


    def saveTwo(self, name=None, window=None):            #Real Save
        
        self.theTitlename = str(name.get()).replace(" ", "_")
        window.destroy()
        if self.theTitlename:
            print(self.theTitlename)
        
        file = "Story\\" + self.theTitlename + ".txt"
        total_path = os.path.join(os.path.dirname(__file__), file)
        # os.mkdir(os.curdir())
        # print(self.choosed)
        keys = list(self.choosed.keys())
        values = list(self.choosed.values())
        chose = []
        nuum = 0
        for x in keys:
            chose.append([x, values[nuum]])
            nuum += 1

        
        
        try:
            sto = open(total_path, "w")
            self.c.execute("INSERT INTO MainTable (name, path, vocab) VALUES (?, ?, ?)", (self.theTitlename, total_path, str(self.choosed)))
            self.conn.commit()
            for word in self.main.get("1.0", END):
                sto.write(word)
        except sqlite3.IntegrityError:
            ms = messagebox.askyesno(title="File appears duplicate", message="There is already a file has the same name, do you want to replace it?")
            print(ms)
            if ms:
                sto = open(total_path, "w")
                self.c.execute("REPLACE INTO MainTable (name, path, vocab) VALUES (?, ?, ?)", (self.theTitlename, total_path, str(chose)))
                self.conn.commit()
                for word in self.main.get("1.0", END):
                    sto.write(word)
            else:
                ms_two = messagebox.askyesno(title=None, message="Do you want to change a title(yes) or discard save?(no)")
                if ms_two:
                    self.save(None)
                else:
                    return None
        # total_path = total_path[:1].upper() + total_path[1:]

        # titles = self.setting["names"]
        # if self.theTitlename in titles:
        #     ms = messagebox.askyesno(title="File appears duplicate", message="There is already a file has the same name, do you want to replace it?")
        #     print(ms)
        #     if ms:
        #         titles.append(self.theTitlename)
        #         sto = open(total_path, "w")
        #         for word in self.main.get("1.0", END):
        #             sto.write(word)
        #         self.du()
        #     else:
        #         ms_two = messagebox.askyesno(title=None, message="Do you want to change a title(yes) or discard save?(no)")
        #         if ms_two:
        #             self.save(None)
                
        # else:
        #     print(self.choosed)
        #     titles[self.theTitlename] = [total_path, self.choosed]
        #     sto = open(total_path, "w")
        #     for word in self.main.get("1.0", END):
        #         sto.write(word)
        #     self.du()
        
        self.note_load()

        

    def save(self, e):            #Save
        thewin = Toplevel()
        thewin.geometry("+460+160")
        thewin.grab_set()
        l = Label(thewin, text="Title of the file\n Can leave it as blank and the title will be the first few word of the writing")
        name = Entry(thewin)
        
        l.pack()
        name.pack()
        name.focus()
        name.bind("<Return>", lambda x: self.saveTwo(name, thewin))
        


    def syslook(self, e=None):            #System menu creation

        self.syst = Toplevel()
        self.syst.grab_set()
        self.syst.bind("<Destroy>", self.du)
        self.syst.geometry(f"+{int(self.sw/2-int(self.syst.winfo_width())-150)}+{int(self.sh/2-int(self.syst.winfo_height())-200)}")
        
        self.note = ttk.Notebook(self.syst)
        self.note.pack(fill=BOTH, expand=True)
        self.pre_pane = Frame(self.note, bg="white")
        self.tex_pane = Frame(self.note, bg="white")
        self.note.add(self.pre_pane, text="Preference")
        self.note.add(self.tex_pane, text="Text")
        self.p_one = Frame(self.pre_pane, bg="white")
        self.p_one.grid(row=0, column=0, sticky=W)
        self.p_two = Frame(self.pre_pane, bg="white")
        self.p_two.grid(row=1, column=0, sticky=W)
        self.p_three = Frame(self.pre_pane, bg="white")
        self.p_three.grid(row=2, column=0, sticky=W)
        self.save_setting = Label(self.p_one, text="Check save setting:", bg="white")
        self.check_setting = Label(self.p_two, text="Checked setting option:", bg="white")
        self.total_voc = Label(self.p_three, text="Total generate vocabulary:", bg="white")
        self.save_setting.grid(row=0, column=0, sticky=W, pady=5)
        self.check_setting.grid(row=0, column=0, sticky=W, pady=5)
        self.total_voc.grid(row=0, column=0, sticky=W, pady=5)
        self.save_var = BooleanVar()
        self.voc_var = IntVar()
        self.save_scale = Scale(self.p_one, orient="horizontal", showvalue=0, from_=0, to=1, bg="white", command=self.change_scale_color, variable=self.save_var)
        self.check_b = Button(self.p_two, text=self.setting["check_setting"], name="checkbutton", command=self.change_button)
        self.voc_spin = Spinbox(self.p_three, from_=1, to=20, command=self.change_voc_num, textvariable=self.voc_var)
        self.save_scale.grid(row=0, column=1, sticky=E, padx=10)
        self.check_b.grid(row=0, column=1, sticky=E, padx=5)
        self.voc_spin.grid(row=0, column=1, sticky=E, padx=5)
        self.save_var.set(self.setting["save_setting"])
        self.change_scale_color(None)
        self.che_b_var = self.setting["check_setting"]
        self.voc_var.set(self.setting["total_voc"])


    def win_show(self, word):  #Show word
        print("yes???")
        show = Toplevel()
        show.grab_set()
        l = Label(show, text=word)
        l.pack(anchor=CENTER)
        show.geometry("+600+200")

    def get_sy(self, v):          #Get Synonyms
        # print("running")
        self.m.delete(2, END)
        c = 0
        li = self.choosed[v]
        # print(v)
        # print(li)
        if any(isinstance(l, list) for l in li):
            for lis in li:
                if type(lis[1]) == str:
                    self.m.add_command(label="Get Synonyms "+str(c), command=lambda x=lis[1]: self.win_show(x))
                    c += 1
                else:
                    # print(type(li[1]))
                    pass
        else:
            if type(li[1]) == str:
                self.m.add_command(label="Get Synonyms", command=lambda y=li[1]: self.win_show(y))
            else:
                # print(type(li[1]))
                pass

    def get_ch(self, v):              #Get Chinese explanation
        # print("running")
        # m.delete(2, END)
        c = 1
        li = self.choosed[v]
        # print(v)
        # print(li)
        if any(isinstance(l, list) for l in li):
            for lis in li:
                self.m.add_command(label="Get Chinese Explaination "+str(c), command=lambda x=lis[0]: self.win_show(x))
                c += 1
        else:
            self.m.add_command(label="Get Chinese Explaination", command=lambda y=li[0]: self.win_show(y))
        pass


    def do_popup(self, event):            #Pop up menu
        v = event.widget.cget("text")
        self.m.delete(0)
        self.m.insert_command(0, label=v, background="yellow")
        self.get_sy(v)
        self.get_ch(v)



        try:
            self.m.tk_popup(event.x_root, event.y_root)
        finally:
            self.m.grab_release()



    def check_le(self, e):            #detect setting of fg
        x = self.main.get("1.0", END)
        for key in self.choosed.keys():
            if key in x:
                wid = self.root.nametowidget(".frame1."+key)
                wid["fg"] = self.setting["after_write"]

            else:
                wid = self.root.nametowidget(".frame1."+key)
                wid["fg"] = self.setting["before_write"]

    def after(self):                #Set up window
        

        self.Frame1 = Frame(self.root, name="frame1")
        self.Frame1.pack(side=TOP)
        self.main_f = Frame(self.root, name="mainf")
        self.main_f.pack(expand=True, fill=BOTH)
        self.Frame2 = Frame(self.root, name="frame2")
        self.Frame2.pack(side=BOTTOM)

        self.main = Text(self.main_f, name="maintext")
        self.main.pack(expand=True, fill=BOTH)
        self.main.bind("<Control-R>", self.check_le)
        
        self.main.bind("<KeyRelease>", self.check_le)

        if self.NoteText:
            self.insert_text()

        return

    def insert_text(self):

        note_file = open(self.NoteText, "r")
        note_texts = note_file.readline()
        self.main.insert(END, note_texts)


    def set_up_word(self):
        pass
        
    def set_up_timer(self):
        pass


    def run(self):
        # global choosed, vocabulary_labels
        # choosed = {}
        # while len(choosed) != self.setting["total_voc"]:
        #     s = random.choice(list(self.dic_v.keys()))
        #     # print(list(v))
        #     if s in choosed.keys():
        #         pass
        #     choosed[s] = self.dic_v[s]
        #     # print(s)
        #     # print(dic_v[s])

        # print(choosed)
        count = 0
        rowc = 0
        # vocabulary_labels = []
        for v in self.choosed.keys():
            vocabulary = Label(self.Frame1, text=v, name=v)
            # vocabulary_labels.append(vocabulary)
            vocabulary.bind("<Button-3>", self.do_popup)
            vocabulary.grid(row=rowc, column=count, padx=7, pady=5)
            count += 1
            if count >= 10 and count == int(self.setting["total_voc"]/2):
                rowc += 1
                count = 0
        
        return self.set_up_word(), self.set_up_timer()
    





