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

from NoteClass import NoteClass


root = Tk()




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

    print("runned")
    NoteClass(root, None, choosed)
    # return set_up_word(), set_up_timer()
    


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