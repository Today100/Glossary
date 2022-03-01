from tkinter import *
from tkinter import ttk
import pandas as pd
import random
import pickle
import json

root = Tk()

m = Menu(root, tearoff = 0)
m.add_separator()
m.add_separator()
m.add_command(label ="Get Synonyms")
m.add_command(label ="Get Chinese Explaination")


def do_popup(event):
    m.delete(0)
    m.insert_command(0, label=event.widget.cget("text"), background="yellow")

    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()


def after():
    global Frame1, main_f

    Frame1 = Frame(root)
    Frame1.pack()
    main_f = Frame(root)
    main_f.pack(expand=True, fill=X)

    main = Text(main_f)
    main.pack(expand=True, fill=BOTH)

    

def run():
    choosed = {}
    while len(choosed) != 5:
        s = random.choice(list(dic_v.keys()))
        # print(list(v))
        if s in choosed.keys():
            pass
        choosed[s] = dic_v[s]
        # print(s)
        # print(dic_v[s])

    # print(choosed)
    count = 0

    for v in choosed.keys():
        vocabulary = Label(Frame1, text=v)
        vocabulary.bind("<Button-3>", do_popup)
        vocabulary.grid(row=0, column=count, padx=7, pady=5)
        count += 1
    

def reload():
    global vocab, dic_v
    vocab = pd.read_excel('E:\\1.Python_f\\Glossory\\Tools_main_file\\story_connect\\vocab2.xlsx')
    pickle.dump(vocab, open("E:\\1.Python_f\Glossory\\Tools_main_file\\story_connect\\vocab", "wb"))
    num = vocab.pop("Num")
    word_together = vocab.pop("word together")
    
    dic_v = vocab.set_index('Vocabulary').T.to_dict('list')
    pickle.dump(dic_v, open("E:\\1.Python_f\Glossory\\Tools_main_file\\story_connect\\dic", "wb"))
    
    run()


def go_on():
    global vocab, dic_v
    # try:
    pickle_in = open("E:\\1.Python_f\Glossory\\Tools_main_file\\story_connect\\vocab", "rb")
    vocab = pickle.load(pickle_in)
    print(vocab)
    print(vocab.loc["3.0"])
    pickle_in = open("E:\\1.Python_f\Glossory\\Tools_main_file\\story_connect\\dic", "rb")
    dic_v = pickle.load(pickle_in)
    print(dic_v)
    run()
    # except:
        # reload()


def get(e):
    ans = ques.get()
    if ans == "Yes":
        root.attributes('-alpha', 1)
        temp.destroy()
        after()
        reload()
    elif ans == "No":
        root.attributes('-alpha', 1)
        temp.destroy()
        after()
        go_on()
    

def set_up():
    global ques, temp
    temp = Toplevel()
    temp.grab_set()
    temp.wm_transient(root)
    # temp.attributes('-topmost', True)
    
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = sw/2-400/2
    y = sh/2-50/2
    temp.geometry(f"400x50+{int(x)}+{int(y)}")
    ask = Label(temp, text="Do you want to reload the vocabulary or just the ones before? (Yes/No)")
    ask.pack()
    ques = Entry(temp)
    ques.pack()
    root.attributes('-alpha', 0)
    ques.bind("<Return>", get)
    ques.focus()






set_up()
mainloop()