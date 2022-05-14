from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# from django.conf import settings
import pandas as pd
import random
import pickle
import json
import sqlite3
import sys
import os


root = Tk()
root.geometry("+360+100")



sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

# read_file = open("E:\\1.Python_f\\Glossory\\Tools_main_file\\story_connect\\setting.json", "w")





setting = json.load(open("E:\\1.Python_f\\Glossory\\Tools_main_file\\story_connect\\setting.json"))


def du(e=None):
    write_file = open("E:\\1.Python_f\\Glossory\\Tools_main_file\\story_connect\\setting.json", "w")
    json.dump(setting, write_file, indent=4, separators=(", \n", " : "))



try:
    os.mkdir(os.path.join(os.path.dirname(__file__), "Story"))
    setting["first load"] = False
except:
    pass

du()


main_m = Menu(root)
syst_m = Menu(main_m, tearoff=0)
note_m = Menu(main_m, tearoff=0)

main_m.add_cascade(label="main", menu=syst_m)
main_m.add_cascade(label="notes", menu=note_m)
root.config(menu=main_m)

def open_note(path):
    note_window = Toplevel()
    note_pad = Text(note_window)
    note_pad.pack(expand=True, fill="both")
    note_file = open(path, "r")
    note_texts = note_file.readline()
    note_pad.insert(END, note_texts)
    
    print(path)

def note_load():
    for note, path in setting["names"].items():
        note_m.add_command(label=note, command=lambda path = path: open_note(path))

note_load()

m = Menu(root, tearoff = 0)
m.add_separator()
m.add_separator()
m.add_command(label ="Get Synonyms")
m.add_command(label ="Get Chinese Explaination")

def change_scale_color(e):
    if save_var.get():
        save_scale["bg"] = "green"
    else:
        save_scale["bg"] = "red"
    save_scale["label"] = str(save_var.get())
    setting["save_setting"] = save_var.get()
    # print(str(save_var.get()))
    
def change_button(e=None):
    global che_b_var
    if check_b["text"] == "Yes":
        # print(check_b)
        check_b["text"] = "No"
        setting["check_setting"] = "No"
    else:
        check_b["text"] = "Yes"
        setting["check_setting"] = "Yes"


def change_voc_num(e=None):
    if int(voc_spin.get()) > 20 or int(voc_spin.get()) < 1:
        return
    else:
        # print(voc_spin.get())
        setting["total_voc"] = int(voc_spin.get())
    
#     setting["save_setting"] = save_var.get()
#      che_b_var
#     # if voc_entry.get():
#     #     setting["total_voc"] = voc_entry.get()
#     du()

###### Creating save !!!!!!!


def saveTwo(name=None, window=None):
    global theTitlename
    theTitlename = name.get()
    window.destroy()
    if theTitlename:
        print(theTitlename)
    
    file = "Story\\" + theTitlename + ".txt"
    total_path = os.path.join(os.path.dirname(__file__), file)
    # os.mkdir(os.curdir())


    # total_path = total_path[:1].upper() + total_path[1:]
    titles = setting["names"]
    if theTitlename in titles:
        ms = messagebox.askyesno(title="File appears duplicate", message="There is already a file has the same name, do you want to replace it?")
        print(ms)
        if ms:
            titles.append(theTitlename)
            sto = open(total_path, "w")
            for word in main.get("1.0", END):
                sto.write(word)
            du()
        else:
            ms_two = messagebox.askyesno(title=None, message="Do you want to change a title(yes) or discard save?(no)")
            if ms_two:
                save(None)
            
    else:
        titles[theTitlename] = [total_path]
        sto = open(total_path, "w")
        for word in main.get("1.0", END):
            sto.write(word)
        du()
    
    note_load()

    

def save(e):
    thewin = Toplevel()
    thewin.geometry("+460+160")
    thewin.grab_set()
    l = Label(thewin, text="Title of the file\n Can leave it as blank and the title will be the first few word of the writing")
    name = Entry(thewin)
    
    l.pack()
    name.pack()
    name.focus()
    name.bind("<Return>", lambda x: saveTwo(name, thewin))
    





   




def syslook(e=None):
    global save_var, save_scale, check_b, voc_spin
    syst = Toplevel()
    syst.grab_set()
    syst.bind("<Destroy>", du)
    syst.geometry(f"+{int(sw/2-int(syst.winfo_width())-150)}+{int(sh/2-int(syst.winfo_height())-200)}")
    
    note = ttk.Notebook(syst)
    note.pack(fill=BOTH, expand=True)
    pre_pane = Frame(note, bg="white")
    tex_pane = Frame(note, bg="white")
    note.add(pre_pane, text="Preference")
    note.add(tex_pane, text="Text")
    p_one = Frame(pre_pane, bg="white")
    p_one.grid(row=0, column=0, sticky=W)
    p_two = Frame(pre_pane, bg="white")
    p_two.grid(row=1, column=0, sticky=W)
    p_three = Frame(pre_pane, bg="white")
    p_three.grid(row=2, column=0, sticky=W)
    save_setting = Label(p_one, text="Check save setting:", bg="white")
    check_setting = Label(p_two, text="Checked setting option:", bg="white")
    total_voc = Label(p_three, text="Total generate vocabulary:", bg="white")
    save_setting.grid(row=0, column=0, sticky=W, pady=5)
    check_setting.grid(row=0, column=0, sticky=W, pady=5)
    total_voc.grid(row=0, column=0, sticky=W, pady=5)
    save_var = BooleanVar()
    voc_var = IntVar()
    save_scale = Scale(p_one, orient="horizontal", showvalue=0, from_=0, to=1, bg="white", command=change_scale_color, variable=save_var)
    check_b = Button(p_two, text=setting["check_setting"], name="checkbutton", command=change_button)
    voc_spin = Spinbox(p_three, from_=1, to=20, command=change_voc_num, textvariable=voc_var)
    save_scale.grid(row=0, column=1, sticky=E, padx=10)
    check_b.grid(row=0, column=1, sticky=E, padx=5)
    voc_spin.grid(row=0, column=1, sticky=E, padx=5)
    save_var.set(setting["save_setting"])
    change_scale_color(None)
    che_b_var = setting["check_setting"]
    voc_var.set(setting["total_voc"])
    
root.bind("<Control-s>", save)

root.bind("<Control-Shift-P>", syslook)
syst_m.add_command(label="Preference", command=syslook)

def win_show(word):
    show = Toplevel()
    show.grab_set()
    l = Label(show, text=word)
    l.pack(anchor=CENTER)
    show.geometry("+600+200")

def get_sy(v):
    # print("running")
    m.delete(2, END)
    c = 0
    li = dic_v[v]
    # print(v)
    # print(li)
    if any(isinstance(l, list) for l in li):
        for lis in li:
            if type(lis[1]) == str:
                m.add_command(label="Get Synonyms "+str(c), command=lambda x=lis[1]: win_show(x))
                c += 1
            else:
                # print(type(li[1]))
                pass
    else:
        if type(li[1]) == str:
            m.add_command(label="Get Synonyms", command=lambda y=li[1]: win_show(y))
        else:
            # print(type(li[1]))
            pass

def get_ch(v):
    # print("running")
    # m.delete(2, END)
    c = 1
    li = dic_v[v]
    # print(v)
    # print(li)
    if any(isinstance(l, list) for l in li):
        for lis in li:
            m.add_command(label="Get Chinese Explaination "+str(c), command=lambda x=lis[0]: win_show(x))
            c += 1
    else:
        m.add_command(label="Get Chinese Explaination", command=lambda y=li[0]: win_show(y))
    pass


def do_popup(event):
    v = event.widget.cget("text")
    m.delete(0)
    m.insert_command(0, label=v, background="yellow")
    get_sy(v)
    get_ch(v)



    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()


def check_le(e):
    x = main.get("1.0", END)
    for key in choosed.keys():
        if key in x:
            wid = root.nametowidget(".frame1."+key)
            wid["fg"] = setting["after_write"]

        else:
            wid = root.nametowidget(".frame1."+key)
            wid["fg"] = setting["before_write"]

def after():
    global Frame1, main_f, main, Frame2

    Frame1 = Frame(root, name="frame1")
    Frame1.pack(side=TOP)
    main_f = Frame(root, name="mainf")
    main_f.pack(expand=True, fill=BOTH)
    Frame2 = Frame(root, name="frame2")
    Frame2.pack(side=BOTTOM)

    main = Text(main_f, name="maintext")
    main.pack(expand=True, fill=BOTH)
    main.bind("<Control-R>", check_le)
    
    main.bind("<KeyRelease>", check_le)
    return

def set_up_word():
    pass
    
def set_up_timer():
    pass

def run():
    global choosed, vocabulary_labels
    choosed = {}
    while len(choosed) != setting["total_voc"]:
        s = random.choice(list(dic_v.keys()))
        # print(list(v))
        if s in choosed.keys():
            pass
        choosed[s] = dic_v[s]
        # print(s)
        # print(dic_v[s])

    # print(choosed)
    count = 0
    rowc = 0
    # vocabulary_labels = []
    for v in choosed.keys():
        vocabulary = Label(Frame1, text=v, name=v)
        # vocabulary_labels.append(vocabulary)
        vocabulary.bind("<Button-3>", do_popup)
        vocabulary.grid(row=rowc, column=count, padx=7, pady=5)
        count += 1
        if count >= 10 and count == int(setting["total_voc"]/2):
            rowc += 1
            count = 0
    
    return set_up_word(), set_up_timer()
    

def reload():
    global vocab, dic_v
    vocab = pd.read_excel('E:\\1.Python_f\\Glossory\\Tools_main_file\\story_connect\\vocab2.xlsx')
    pickle.dump(vocab, open("E:\\1.Python_f\Glossory\\Tools_main_file\\story_connect\\vocab23", "wb"))
    num = vocab.pop("Num")
    word_together = vocab.pop("word together")

    c = 0
    dic_v = {}
    for x in vocab["Vocabulary"]:
        # print(type(x))
        if type(x) is float:
            m_s = vocab.loc[c]
            s = m_s[["Meaning", "Synonyms"]].to_list()
            
            try:
                last = vocab.loc[c-1]["Vocabulary"]
                n = dic_v[last]
            except KeyError:
                last = vocab.loc[c-2]["Vocabulary"]
                n = dic_v[last]

            

            if any(isinstance(i, list) for i in n):
                n.append(s)
                dic_v[last] = n

            else:
                dic_v[last] = [n, s]
        elif type(x) is str:
            m_s = vocab.loc[c]
            dic_v[x] = m_s[["Meaning", "Synonyms"]].to_list()

        c += 1


    
    
    # dic_v = vocab.set_index('Vocabulary').T.to_dict('list')
    pickle.dump(dic_v, open("E:\\1.Python_f\Glossory\\Tools_main_file\\story_connect\\dic23", "wb"))
    # print(dic_v)
    
    return run()


def go_on():
    global vocab, dic_v
    try:
        pickle_in = open("E:\\1.Python_f\Glossory\\Tools_main_file\\story_connect\\vocab23", "rb")
        vocab = pickle.load(pickle_in)


        pickle_in = open("E:\\1.Python_f\Glossory\\Tools_main_file\\story_connect\\dic23", "rb")
        dic_v = pickle.load(pickle_in)
        return run()
    # print(dic_v)

    except:
        return reload()


def get(e, select=None):    
    # print("running")
    exist("Running from here")
    if not select:
        ans = ques.get()
    else:
        ans = select
    if ans == "Yes":
        try:
            if che.get():
                check(ans)
        except:
            pass
        try:
            temp.unbind("<Destroy>")
            temp.destroy()
        except:
            pass
        
        root.attributes('-alpha', 1)
        
        # print("Done")
        after()
        return reload()
    elif ans == "No":
        try:
            if che.get():
                check(ans)
        except:
            pass
        try:
            temp.unbind("<Destroy>")
            temp.destroy()
        except:
            pass
        # print("again")
        # thread.join()
        # print("thread killed")
        
        root.attributes('-alpha', 1)
        go()
        # print("Done")
        after()
        return go_on()
    


def go(e=None):
    try:
        temp.unbind("<Destroy>")
    except:
        pass
   

def exist(e=None, s=None):
    if s:
        root.quit()

        
def check(tick):
    # write_file = open("E:\\1.Python_f\\Glossory\\Tools_main_file\\story_connect\\setting.json", "w")
    setting["save_setting"] = che.get()
    print(tick)
    setting["check_setting"] = tick
    print(setting)
    # json.dump(setting, write_file, indent=4, separators=(", \n", " : "))
    du()



def set_up():
    global ques, temp, thread, stop, che
    # print(setting["save_setting"])
    if not setting["save_setting"]:
        print("running")
        temp = Toplevel()
        temp.grab_set()
        temp.wm_transient(root)
        x = sw/2-400/2
        y = sh/2-50/2
        temp.geometry(f"400x70+{int(x)}+{int(y)-100}")
        ask = Label(temp, text="Do you want to reload the vocabulary or just the ones before? (Yes/No)")
        ask.pack()
        ques = Entry(temp)
        ques.pack()
        root.attributes('-alpha', 0)
        ques.bind("<Return>", get)
        # ques.bind("<Return>", exist, add="+")
        ques.focus()
        che = BooleanVar()
        chet = Checkbutton(temp, text="Keep selection the whole time. Change in setting", variable=che)
        chet.pack()

        temp.bind("<Destroy>", lambda x: exist(True, True))
        return
    else:
        get(None, setting["check_setting"])
    # return exist()
    # thread = threading.Thread(target=exist)
    # thread.setDaemon(True)
    # thread.start()

    # # get(None)
    # # print("wait for finish")
    
    
    # thread.join()

    







set_up()
# after()
# go_on()
root.mainloop()